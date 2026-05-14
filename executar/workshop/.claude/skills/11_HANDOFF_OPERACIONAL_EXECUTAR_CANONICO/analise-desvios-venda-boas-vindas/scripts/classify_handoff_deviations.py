#!/usr/bin/env python3
"""Classifica desvios handoff venda vs. Growth Class e gera matriz Markdown/CSV."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

RISK_ORDER = {"baixo": 0, "baixa": 0, "low": 0, "medio": 1, "médio": 1, "medium": 1, "alto": 2, "alta": 2, "high": 2}


def norm_risk(value: str) -> str:
    key = (value or "").strip().lower()
    if key in {"baixo", "baixa", "low"}:
        return "Baixo"
    if key in {"medio", "médio", "medium"}:
        return "Médio"
    if key in {"alto", "alta", "high"}:
        return "Alto"
    return "Médio"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def decision(eixos: list[dict[str, Any]]) -> tuple[str, str]:
    worst = 0
    for row in eixos:
        r = norm_risk(str(row.get("risco", "")))
        worst = max(worst, RISK_ORDER.get(r.lower(), 1))
    if worst >= 2:
        return "incompleto", "Existem eixos com risco Alto; registrar ação corretiva antes de concluir handoff."
    if worst >= 1:
        return "incompleto", "Existem eixos com risco Médio; handoff incompleto até ações registradas."
    return "completo", "Riscos baixos nos eixos avaliados; validar revisão humana antes de fechar."


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    eixos = payload.get("eixos", [])
    if not isinstance(eixos, list):
        raise ValueError("'eixos' must be a list.")
    rows = []
    for item in eixos:
        if not isinstance(item, dict):
            continue
        rows.append({
            "eixo": str(item.get("eixo", "")),
            "call_vendas": str(item.get("call_vendas", "")),
            "growth_class": str(item.get("growth_class", "")),
            "risco": norm_risk(str(item.get("risco", ""))),
            "evidencia": str(item.get("evidencia", "")),
            "acao_corretiva": str(item.get("acao_corretiva", "")),
            "dono": str(item.get("dono", "")),
            "prazo": str(item.get("prazo", "")),
        })
    return rows


def esc(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def write_md(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    status, note = decision(payload.get("eixos", []))
    lines = [
        "# Análise De Desvios Venda vs. Boas-vindas",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Data: {payload.get('data_analise', '')}",
        f"- Responsável: {payload.get('responsavel', '')}",
        f"- Plano de ROI: {payload.get('referencia_roi', '')}",
        f"- Decisão de completude: **{status}**",
        f"- Nota: {note}",
        "",
        "| Eixo | Call de vendas | Growth Class | Risco | Ação corretiva |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {esc(row['eixo'])} | {esc(row['call_vendas'])} | {esc(row['growth_class'])} | {row['risco']} | {esc(row['acao_corretiva'])} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fields = ["eixo", "call_vendas", "growth_class", "risco", "evidencia", "acao_corretiva", "dono", "prazo"]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify handoff deviations.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()
    payload = load(args.input_json)
    rows = build_rows(payload)
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_md(args.md_path, payload, rows)
    if not args.csv_path and not args.md_path:
        print(decision(payload.get("eixos", []))[0])


if __name__ == "__main__":
    main()
