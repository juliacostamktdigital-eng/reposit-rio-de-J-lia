#!/usr/bin/env python3
"""Validate N1/N2/N3 maturity by Marketing OS component."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "cliente",
    "componente",
    "nivel_declarado",
    "nivel_validado",
    "evidencias",
    "falsos_positivos",
    "dono",
    "frequencia_revisao",
    "recomendacao",
    "backlog",
]

LEVEL_ORDER = {"n0": 0, "n1": 1, "n2": 2, "n3": 3}


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_level(value: Any) -> str:
    level = str(value or "").strip().lower()
    return level if level in LEVEL_ORDER else "n0"


def validate_level(component: dict[str, Any]) -> str:
    declared = normalize_level(component.get("nivel_declarado"))
    evidences = component.get("evidencias", [])
    false_positives = component.get("falsos_positivos", [])
    evidence_count = len(evidences) if isinstance(evidences, list) else 0
    false_positive_count = len(false_positives) if isinstance(false_positives, list) else 0
    owner = str(component.get("dono", "")).strip()
    frequency = str(component.get("frequencia_revisao", "")).strip()

    level_score = LEVEL_ORDER[declared]
    if evidence_count == 0 or not owner:
        level_score = min(level_score, 1)
    if declared in {"n2", "n3"} and false_positive_count:
        level_score = min(level_score, 1)
    if declared == "n3" and not frequency:
        level_score = min(level_score, 2)
    for level, score in LEVEL_ORDER.items():
        if score == level_score:
            return level
    return "n0"


def recommendation(validated: str) -> str:
    if validated == "n0":
        return "criar asset mínimo com dono e evidência"
    if validated == "n1":
        return "tornar auditável: dados mínimos, execução e prova ponta a ponta"
    if validated == "n2":
        return "criar cadência de leitura, decisões registradas e changelog"
    return "manter cadência, canonizar aprendizados e monitorar anti-padrões"


def should_backlog(validated: str, declared: str) -> str:
    if LEVEL_ORDER[validated] < LEVEL_ORDER[declared]:
        return "sim_rebaixamento"
    if validated in {"n0", "n1"}:
        return "sim"
    return "avaliar"


def list_to_text(value: Any) -> str:
    if isinstance(value, list):
        return "; ".join(str(item) for item in value)
    return str(value or "")


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    components = payload.get("componentes", [])
    if not isinstance(components, list):
        raise ValueError("'componentes' must be a list.")
    rows: list[dict[str, str]] = []
    for component in components:
        if not isinstance(component, dict):
            continue
        declared = normalize_level(component.get("nivel_declarado"))
        validated = validate_level(component)
        rows.append({
            "cliente": str(payload.get("cliente", "")),
            "componente": str(component.get("componente", "")),
            "nivel_declarado": declared,
            "nivel_validado": validated,
            "evidencias": list_to_text(component.get("evidencias", [])),
            "falsos_positivos": list_to_text(component.get("falsos_positivos", [])),
            "dono": str(component.get("dono", "")),
            "frequencia_revisao": str(component.get("frequencia_revisao", "")),
            "recomendacao": recommendation(validated),
            "backlog": should_backlog(validated, declared),
        })
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
    fields = ["componente", "nivel_declarado", "nivel_validado", "falsos_positivos", "recomendacao", "backlog"]
    lines = [
        "# Rubrica N1/N2/N3 Por Componente",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Avaliador: {payload.get('avaliador', '')}",
        "",
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    downgraded = [row for row in rows if LEVEL_ORDER[row["nivel_validado"]] < LEVEL_ORDER[row["nivel_declarado"]]]
    if downgraded:
        lines.extend(["", "## Rebaixamentos Por Falso Positivo", ""])
        for row in downgraded:
            lines.append(f"- {row['componente']}: {row['nivel_declarado']} -> {row['nivel_validado']} ({row['falsos_positivos']})")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Score N1/N2/N3 maturity by component.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    rows = build_rows(payload)
    if not args.md_path and not args.csv_path:
        for row in rows:
            print(f"{row['componente']}: {row['nivel_declarado']} -> {row['nivel_validado']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
