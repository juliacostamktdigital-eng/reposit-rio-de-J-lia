#!/usr/bin/env python3
"""Prioritize operational growth gaps into an actionable backlog."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "prioridade",
    "score",
    "cliente",
    "ciclo",
    "gap",
    "categoria",
    "componente",
    "impacto",
    "severidade",
    "urgencia",
    "esforco",
    "decisao",
    "dono",
    "prazo",
    "dependencia",
    "evidencia",
    "status",
    "classe",
]

SEVERITY = {"critica": 100, "crítica": 100, "alta": 75, "media": 50, "média": 50, "baixa": 25}
URGENCY = {"alta": 30, "media": 20, "média": 20, "baixa": 10}
EFFORT_PENALTY = {"alto": 20, "medio": 10, "médio": 10, "baixo": 0}
DECISION_BOOST = {
    "bloquear_go_live": 50,
    "resolver_antes_go_live": 35,
    "substituir_hipotese": 25,
    "aceitar_risco_por_ciclo": 10,
    "retirar_pacote_v1": 0,
}


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalized(value: Any) -> str:
    return str(value or "").strip().lower()


def score_gap(gap: dict[str, Any]) -> int:
    severity = SEVERITY.get(normalized(gap.get("severidade")), 0)
    urgency = URGENCY.get(normalized(gap.get("urgencia")), 0)
    decision = DECISION_BOOST.get(normalized(gap.get("decisao")), 0)
    effort = EFFORT_PENALTY.get(normalized(gap.get("esforco")), 0)
    missing_owner = 25 if not str(gap.get("dono", "")).strip() else 0
    missing_deadline = 15 if not str(gap.get("prazo", "")).strip() else 0
    return severity + urgency + decision + missing_owner + missing_deadline - effort


def classify(gap: dict[str, Any]) -> str:
    decision = normalized(gap.get("decisao"))
    severity = normalized(gap.get("severidade"))
    if decision == "bloquear_go_live" or severity in {"critica", "crítica"}:
        return "bloqueador"
    if decision == "aceitar_risco_por_ciclo":
        return "risco_aceito"
    if decision == "retirar_pacote_v1":
        return "fora_v1"
    return "acao"


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    gaps = payload.get("gaps", [])
    if not isinstance(gaps, list):
        raise ValueError("'gaps' must be a list.")
    rows: list[dict[str, str]] = []
    for gap in gaps:
        if not isinstance(gap, dict):
            continue
        score = score_gap(gap)
        rows.append({
            "prioridade": "",
            "score": str(score),
            "cliente": str(payload.get("cliente", "")),
            "ciclo": str(payload.get("ciclo", "")),
            "gap": str(gap.get("gap", "")),
            "categoria": str(gap.get("categoria", "")),
            "componente": str(gap.get("componente", "")),
            "impacto": str(gap.get("impacto", "")),
            "severidade": str(gap.get("severidade", "")),
            "urgencia": str(gap.get("urgencia", "")),
            "esforco": str(gap.get("esforco", "")),
            "decisao": str(gap.get("decisao", "")),
            "dono": str(gap.get("dono", "")),
            "prazo": str(gap.get("prazo", "")),
            "dependencia": str(gap.get("dependencia", "")),
            "evidencia": str(gap.get("evidencia", "")),
            "status": str(gap.get("status", "")),
            "classe": classify(gap),
        })
    rows.sort(key=lambda row: int(row["score"]), reverse=True)
    for index, row in enumerate(rows, start=1):
        row["prioridade"] = str(index)
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["prioridade", "gap", "severidade", "urgencia", "decisao", "dono", "prazo", "classe"]
    lines = [
        "# Backlog Operacional Growth",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Ciclo: {payload.get('ciclo', '')}",
        f"- Go-live: {payload.get('go_live', '')}",
        "",
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    blockers = [row for row in rows if row["classe"] == "bloqueador"]
    if blockers:
        lines.extend(["", "## Bloqueadores De Go-Live", ""])
        for row in blockers:
            lines.append(f"- {row['gap']} -> {row['dono']} até {row['prazo']}. Evidência: {row['evidencia']}")
    risks = [row for row in rows if row["classe"] == "risco_aceito"]
    if risks:
        lines.extend(["", "## Riscos Aceitos", ""])
        for row in risks:
            lines.append(f"- {row['gap']} ({row['impacto']})")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prioritize operational growth backlog gaps.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    rows = build_rows(payload)
    if not args.md_path and not args.csv_path:
        for row in rows:
            print(f"{row['prioridade']}. {row['gap']} [{row['classe']}]")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
