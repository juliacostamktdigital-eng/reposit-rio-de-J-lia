#!/usr/bin/env python3
"""Prioritize LP optimization tests."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = ["prioridade", "score", "hipotese", "evidencia", "alavanca", "variacao", "metrica_primaria", "metrica_secundaria", "criterio_sucesso"]


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def as_int(item: dict[str, Any], field: str) -> int:
    try:
        return int(item.get(field, 0) or 0)
    except ValueError:
        return 0


def score(item: dict[str, Any]) -> int:
    return (as_int(item, "impacto") * as_int(item, "confianca")) - as_int(item, "esforco") - as_int(item, "risco")


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    tests = payload.get("testes", [])
    if not isinstance(tests, list):
        raise ValueError("'testes' must be a list.")
    rows = []
    for item in tests:
        if not isinstance(item, dict):
            continue
        rows.append({
            "prioridade": "",
            "score": str(score(item)),
            "hipotese": str(item.get("hipotese", "")),
            "evidencia": str(item.get("evidencia", "")),
            "alavanca": str(item.get("alavanca", "")),
            "variacao": str(item.get("variacao", "")),
            "metrica_primaria": str(item.get("metrica_primaria", "")),
            "metrica_secundaria": str(item.get("metrica_secundaria", "")),
            "criterio_sucesso": str(item.get("criterio_sucesso", "")),
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
    lines = [
        "# Backlog De Testes De LP",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- LP: {payload.get('lp', '')}",
        "",
        "| prioridade | hipótese | alavanca | métrica primária | critério de sucesso |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        fields = ["prioridade", "hipotese", "alavanca", "metrica_primaria", "criterio_sucesso"]
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prioritize LP tests from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    rows = build_rows(payload)
    if not args.md_path and not args.csv_path:
        for row in rows:
            print(f"{row['prioridade']}. {row['hipotese']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
