#!/usr/bin/env python3
"""Prioritize next-cycle growth backlog items from JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "prioridade",
    "acao",
    "tipo",
    "componente",
    "severidade",
    "impacto",
    "confianca",
    "esforco",
    "score",
    "dono",
    "metrica",
    "evidencia",
]

SEVERITY_WEIGHT = {
    "bloqueador": 6,
    "alto": 4,
    "medio": 2,
    "baixo": 1,
}


def as_int(value: Any, field: str, index: int) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Item #{index} has invalid integer field '{field}'.") from exc
    if parsed < 1 or parsed > 5:
        raise ValueError(f"Item #{index} field '{field}' must be between 1 and 5.")
    return parsed


def load_items(path: Path) -> list[dict[str, str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    items = payload.get("itens")
    if not isinstance(items, list):
        raise ValueError("JSON must contain an 'itens' list.")

    rows: list[dict[str, str]] = []
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Item #{index} must be an object.")
        action = str(item.get("acao", "")).strip()
        severity = str(item.get("severidade", "medio")).strip()
        if not action:
            raise ValueError(f"Item #{index} is missing 'acao'.")
        if severity not in SEVERITY_WEIGHT:
            raise ValueError(f"Item #{index} has invalid severidade '{severity}'.")

        impact = as_int(item.get("impacto"), "impacto", index)
        confidence = as_int(item.get("confianca"), "confianca", index)
        effort = as_int(item.get("esforco"), "esforco", index)
        score = (impact * confidence) + SEVERITY_WEIGHT[severity] - effort

        row = {field: str(item.get(field, "")).strip() for field in FIELDS}
        row["acao"] = action
        row["severidade"] = severity
        row["impacto"] = str(impact)
        row["confianca"] = str(confidence)
        row["esforco"] = str(effort)
        row["score"] = str(score)
        rows.append(row)

    rows.sort(key=lambda item: int(item["score"]), reverse=True)
    for priority, row in enumerate(rows, start=1):
        row["prioridade"] = str(priority)
    return rows


def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Backlog Priorizado Do Próximo Ciclo",
        "",
        "| " + " | ".join(FIELDS) + " |",
        "| " + " | ".join("---" for _ in FIELDS) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in FIELDS) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prioritize next-cycle growth backlog JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    rows = load_items(args.input_json)
    if not args.md_path and not args.csv_path:
        for row in rows:
            print(f"{row['prioridade']}. [{row['score']}] {row['acao']}")
        return
    if args.md_path:
        write_markdown(rows, args.md_path)
    if args.csv_path:
        write_csv(rows, args.csv_path)


if __name__ == "__main__":
    main()
