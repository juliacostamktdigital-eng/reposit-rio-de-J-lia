#!/usr/bin/env python3
"""Convert a Marketing OS asset matrix JSON into CSV and Markdown tables."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "etapa",
    "asset",
    "status",
    "evidencia",
    "dono",
    "prioridade",
    "dependencia",
    "dod",
]


def load_assets(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assets = payload.get("assets")
    if not isinstance(assets, list):
        raise ValueError("JSON must contain an 'assets' list.")

    normalized: list[dict[str, Any]] = []
    for index, item in enumerate(assets, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Asset #{index} must be an object.")
        missing = [field for field in ("etapa", "asset", "status", "prioridade", "dono", "dod") if field not in item]
        if missing:
            raise ValueError(f"Asset #{index} is missing required fields: {', '.join(missing)}")
        normalized.append({field: str(item.get(field, "")).strip() for field in FIELDS})
    return normalized


def write_csv(assets: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(assets)


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(assets: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Matriz De Assets AI-Native",
        "",
        "| " + " | ".join(FIELDS) + " |",
        "| " + " | ".join("---" for _ in FIELDS) + " |",
    ]
    for item in assets:
        lines.append("| " + " | ".join(markdown_escape(item[field]) for field in FIELDS) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Marketing OS asset matrix JSON to CSV and Markdown.")
    parser.add_argument("input_json", type=Path, help="Path to matriz-assets JSON file.")
    parser.add_argument("--csv", dest="csv_path", type=Path, help="Optional CSV output path.")
    parser.add_argument("--md", dest="md_path", type=Path, help="Optional Markdown output path.")
    args = parser.parse_args()

    assets = load_assets(args.input_json)
    if not args.csv_path and not args.md_path:
        raise SystemExit("Provide at least one output: --csv or --md.")

    if args.csv_path:
        write_csv(assets, args.csv_path)
    if args.md_path:
        write_markdown(assets, args.md_path)


if __name__ == "__main__":
    main()
