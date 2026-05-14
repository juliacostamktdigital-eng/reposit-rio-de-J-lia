#!/usr/bin/env python3
"""Build Growth Testing workbook structure as CSVs, Markdown and optional XLSX."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


def load_schema(path: Path) -> dict[str, Any]:
    schema = json.loads(path.read_text(encoding="utf-8"))
    sheets = schema.get("sheets")
    if not isinstance(sheets, list) or not sheets:
        raise ValueError("Schema must contain a non-empty 'sheets' list.")
    for index, sheet in enumerate(sheets, start=1):
        if not isinstance(sheet, dict):
            raise ValueError(f"Sheet #{index} must be an object.")
        if not sheet.get("name"):
            raise ValueError(f"Sheet #{index} is missing 'name'.")
        columns = sheet.get("columns")
        if not isinstance(columns, list) or not columns:
            raise ValueError(f"Sheet {sheet.get('name')} must contain non-empty 'columns'.")
    return schema


def safe_filename(name: str) -> str:
    return "".join(char if char.isalnum() or char in "._-" else "_" for char in name)


def normalize_rows(columns: list[str], sample_rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for item in sample_rows:
        rows.append({column: str(item.get(column, "")) for column in columns})
    return rows


def write_csvs(schema: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for sheet in schema["sheets"]:
        columns = [str(column) for column in sheet["columns"]]
        rows = normalize_rows(columns, sheet.get("sample_rows", []))
        path = out_dir / f"{safe_filename(str(sheet['name']))}.csv"
        with path.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerows(rows)


def write_markdown(schema: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {schema.get('workbook', 'planilha-testes-growth')}",
        "",
        "## Abas",
        "",
        "| Aba | Descrição | Colunas |",
        "| --- | --- | --- |",
    ]
    for sheet in schema["sheets"]:
        columns = ", ".join(f"`{column}`" for column in sheet["columns"])
        lines.append(f"| `{sheet['name']}` | {sheet.get('description', '')} | {columns} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_xlsx(schema: dict[str, Any], path: Path) -> None:
    try:
        from openpyxl import Workbook
    except ImportError as exc:
        raise RuntimeError("openpyxl is not installed. Generate CSVs or install openpyxl to create XLSX.") from exc

    workbook = Workbook()
    default = workbook.active
    workbook.remove(default)
    for sheet in schema["sheets"]:
        ws = workbook.create_sheet(title=str(sheet["name"])[:31])
        columns = [str(column) for column in sheet["columns"]]
        ws.append(columns)
        for row in normalize_rows(columns, sheet.get("sample_rows", [])):
            ws.append([row[column] for column in columns])
        ws.freeze_panes = "A2"
    path.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build canonical Growth Testing workbook structure.")
    parser.add_argument("schema_json", type=Path)
    parser.add_argument("--out", dest="out_dir", type=Path, help="Directory to write one CSV per sheet.")
    parser.add_argument("--md", dest="md_path", type=Path, help="Markdown documentation output path.")
    parser.add_argument("--xlsx", dest="xlsx_path", type=Path, help="Optional XLSX output path. Requires openpyxl.")
    args = parser.parse_args()

    schema = load_schema(args.schema_json)
    if not args.out_dir and not args.md_path and not args.xlsx_path:
        raise SystemExit("Provide at least one output: --out, --md or --xlsx.")
    if args.out_dir:
        write_csvs(schema, args.out_dir)
    if args.md_path:
        write_markdown(schema, args.md_path)
    if args.xlsx_path:
        write_xlsx(schema, args.xlsx_path)


if __name__ == "__main__":
    main()
