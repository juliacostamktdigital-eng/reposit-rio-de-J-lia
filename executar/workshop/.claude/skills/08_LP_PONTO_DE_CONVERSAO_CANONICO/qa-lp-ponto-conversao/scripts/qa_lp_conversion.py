#!/usr/bin/env python3
"""QA LP / conversion point readiness before go-live."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


CRITICAL = {
    "formulario_funciona",
    "utms_campos_ocultos",
    "first_touch_preservado",
    "crm_recebe_origem",
    "backup_recebe_lead",
    "evento_principal_dispara",
    "thank_you_funciona",
    "claims_permitidos",
}

TRACKING = {
    "utms_campos_ocultos",
    "v4_ids_capturados",
    "first_touch_preservado",
    "last_touch_atualizado",
    "crm_recebe_origem",
    "backup_recebe_lead",
    "evento_principal_dispara",
    "dedupe_validado",
}

BACKLOG_FIELDS = ["cliente", "campanha", "gap", "categoria", "severidade", "dono", "decisao", "prazo", "impacto"]
CHECK_FIELDS = ["criterio", "status", "severidade", "categoria"]


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(value: Any) -> str:
    return str(value or "").strip().lower()


def classify_checks(payload: dict[str, Any]) -> list[dict[str, str]]:
    criteria = payload.get("criterios", {})
    if not isinstance(criteria, dict):
        raise ValueError("'criterios' must be an object.")
    rows = []
    for criterion, status_value in criteria.items():
        status = normalize(status_value)
        severity = "baixa"
        if status == "bloqueio":
            severity = "critica" if criterion in CRITICAL else "alta"
        elif status == "pendencia":
            severity = "alta" if criterion in CRITICAL or criterion in TRACKING else "media"
        rows.append({
            "criterio": criterion,
            "status": status,
            "severidade": severity,
            "categoria": "tracking" if criterion in TRACKING else "conversao",
        })
    return rows


def decision(checks: list[dict[str, str]]) -> str:
    blocked = [row for row in checks if row["status"] == "bloqueio"]
    if any(row["criterio"] in TRACKING for row in blocked):
        return "bloquear_tracking"
    if any(row["criterio"] == "formulario_funciona" for row in blocked):
        return "bloquear_formulario"
    if any(row["criterio"] == "claims_permitidos" for row in blocked):
        return "bloquear_claim"
    if blocked:
        return "no_go"
    pending = [row for row in checks if row["status"] == "pendencia"]
    return "go_com_pendencia" if pending else "go"


def build_backlog(payload: dict[str, Any]) -> list[dict[str, str]]:
    gaps = payload.get("gaps", [])
    if not isinstance(gaps, list):
        return []
    rows = []
    for gap in gaps:
        if not isinstance(gap, dict):
            continue
        rows.append({
            "cliente": str(payload.get("cliente", "")),
            "campanha": str(payload.get("campanha", "")),
            "gap": str(gap.get("gap", "")),
            "categoria": str(gap.get("categoria", "")),
            "severidade": str(gap.get("severidade", "")),
            "dono": str(gap.get("dono", "")),
            "decisao": str(gap.get("decisao", "")),
            "prazo": str(gap.get("prazo", "")),
            "impacto": str(gap.get("impacto", "")),
        })
    return rows


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, payload: dict[str, Any], checks: list[dict[str, str]], backlog: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# QA LP / Ponto De Conversão",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Campanha: {payload.get('campanha', '')}",
        f"- URL teste: {payload.get('url_teste', '')}",
        f"- Decisão: {decision(checks)}",
        "",
        "## Critérios",
        "",
        "| critério | status | severidade | categoria |",
        "| --- | --- | --- | --- |",
    ]
    for row in checks:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in CHECK_FIELDS) + " |")
    lines.extend(["", "## Backlog 06", "", "| gap | categoria | severidade | dono | decisão | prazo |", "| --- | --- | --- | --- | --- | --- |"])
    for row in backlog:
        fields = ["gap", "categoria", "severidade", "dono", "decisao", "prazo"]
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="QA LP conversion point from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path, help="Backlog CSV output.")
    parser.add_argument("--checks-csv", dest="checks_csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    checks = classify_checks(payload)
    backlog = build_backlog(payload)
    if not args.md_path and not args.csv_path and not args.checks_csv_path:
        print(decision(checks))
        return
    if args.csv_path:
        write_csv(args.csv_path, BACKLOG_FIELDS, backlog)
    if args.checks_csv_path:
        write_csv(args.checks_csv_path, CHECK_FIELDS, checks)
    if args.md_path:
        write_markdown(args.md_path, payload, checks, backlog)


if __name__ == "__main__":
    main()
