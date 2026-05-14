#!/usr/bin/env python3
"""Prioriza hipóteses vindas do benchmark, audita DoD mínimo e gera MD/CSV + changelog."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def as_int(item: dict[str, Any], field: str) -> int:
    try:
        return int(item.get(field, 0) or 0)
    except (TypeError, ValueError):
        return 0


def score(item: dict[str, Any]) -> int:
    return (as_int(item, "impacto") * as_int(item, "confianca")) - as_int(item, "esforco") - as_int(item, "risco")


def esc(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def capacidade_top_n(cap: str) -> int:
    key = (cap or "").strip().lower()
    if key in {"baixa", "low"}:
        return 2
    if key in {"media", "média", "medium"}:
        return 4
    if key in {"alta", "high"}:
        return 8
    return 4


def audit_dod(h_items: list[dict[str, Any]]) -> list[str]:
    issues = []
    if not h_items:
        issues.append("DoD (Seção 10.1): backlog de hipóteses vazio.")
    for item in h_items:
        if not str(item.get("metrica_primaria", "")).strip():
            issues.append(f"Item {item.get('id', '?')}: falta métrica primária.")
        if not str(item.get("evidencia", "")).strip():
            issues.append(f"Item {item.get('id', '?')}: falta evidência de benchmark.")
        if not str(item.get("criterio_sucesso", "")).strip():
            issues.append(f"Item {item.get('id', '?')}: falta critério de sucesso mensurável.")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Prioritize benchmark hypotheses backlog.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    data = load(args.input_json)
    hip = data.get("hipoteses", [])
    if not isinstance(hip, list):
        hip = []

    rows: list[dict[str, str]] = []
    for item in hip:
        if not isinstance(item, dict):
            continue
        rows.append({
            "prioridade": "",
            "score": str(score(item)),
            "id": str(item.get("id", "")),
            "hipotese": str(item.get("hipotese", "")),
            "evidencia": str(item.get("evidencia", "")),
            "tipo": str(item.get("tipo", "")),
            "asset_impactado": str(item.get("asset_impactado", "")),
            "metrica_primaria": str(item.get("metrica_primaria", "")),
            "metrica_secundaria": str(item.get("metrica_secundaria", "")),
            "criterio_sucesso": str(item.get("criterio_sucesso", "")),
            "dono": str(item.get("dono", "")),
            "status": str(item.get("status", "backlog")),
            "v4_test_id": str(item.get("v4_test_id", "")),
        })

    rows.sort(key=lambda r: int(r["score"]), reverse=True)
    cap = capacidade_top_n(str(data.get("capacidade_teste", "")))
    for i, row in enumerate(rows, start=1):
        row["prioridade"] = str(i)
    executavel = rows[:cap]

    fields = [
        "prioridade", "score", "id", "hipotese", "evidencia", "tipo", "asset_impactado",
        "metrica_primaria", "metrica_secundaria", "criterio_sucesso", "dono", "status", "v4_test_id",
    ]

    if args.csv_path:
        args.csv_path.parent.mkdir(parents=True, exist_ok=True)
        with args.csv_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)

    if args.md_path:
        issues = audit_dod(hip)
        lines = [
            "# Backlog De Hipóteses (Benchmark → Growth)",
            "",
            f"- Cliente: {data.get('cliente', '')}",
            f"- Ciclo: {data.get('ciclo', '')}",
            f"- Pergunta de negócio: {data.get('pergunta_negocio', '')}",
            f"- Capacidade de teste: {data.get('capacidade_teste', '')} → sugerido rodar **até {cap}** hipóteses em paralelo neste ciclo",
            "",
            "## Baseline e diferenciação",
            "",
            f"- Baseline: {data.get('baseline_mercado', '')}",
            f"- Diferenciação: {data.get('diferenciacao', '')}",
            "",
            "## Priorização (todas)",
            "",
            "| pri | score | id | tipo | métrica 1ª | asset | critério de sucesso |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        for row in rows:
            lines.append(
                f"| {row['prioridade']} | {row['score']} | `{esc(row['id'])}` | {esc(row['tipo'])} | {esc(row['metrica_primaria'])} | {esc(row['asset_impactado'])} | {esc(row['criterio_sucesso'])} |"
            )
        lines.extend([
            "",
            f"## Sugestão de fila executável (top {len(executavel)})",
            "",
        ])
        for row in executavel:
            lines.append(f"{row['prioridade']}. `{row['id']}` — {esc(row['hipotese'])} (**{esc(row['metrica_primaria'])}**)")
        lines.extend([
            "",
            "## Auditoria DoD (Seção 10.1 — backlog com métrica e prioridade)",
            "",
        ])
        if issues:
            for issue in issues:
                lines.append(f"- ALERTA: {issue}")
        else:
            lines.append("- OK: cada item tem métrica primária, evidência e critério declarados.")
        lines.extend(["", "## Changelog (atual)", "", "| Data | Benchmark | Decisão | Teste | Resultado |", "| --- | --- | --- | --- | --- |"])
        for entry in data.get("changelog", []) or []:
            if isinstance(entry, dict):
                lines.append(
                    f"| {esc(entry.get('data', ''))} | {esc(entry.get('benchmark_observado', ''))} | {esc(entry.get('decisao', ''))} | {esc(entry.get('teste', ''))} | {esc(entry.get('resultado', ''))} |"
                )
        lines.extend([
            "",
            "## Semáforo (Seção 12 — lembrete)",
            "",
            "- Verde: hipóteses testadas na cadência combinada.",
            "- Amarelo: muito benchmark, pouco teste.",
            "- Vermelho: nenhuma mudança em mídia/dossiê por dois ciclos.",
            "",
        ])
        args.md_path.parent.mkdir(parents=True, exist_ok=True)
        args.md_path.write_text("\n".join(lines), encoding="utf-8")

    if not args.csv_path and not args.md_path:
        for row in rows[:5]:
            print(row["id"], row["score"])


if __name__ == "__main__":
    main()
