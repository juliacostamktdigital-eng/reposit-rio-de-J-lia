#!/usr/bin/env python3
"""Build persona and decision-role maps from JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = ["persona", "papel", "rotina", "dores", "desejos", "medos", "objecoes", "linguagem", "provas", "cta", "canal"]


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def join_values(value: Any) -> str:
    if isinstance(value, list):
        return "; ".join(str(item) for item in value)
    return str(value or "")


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    personas = payload.get("personas", [])
    if not isinstance(personas, list):
        raise ValueError("'personas' must be a list.")
    rows = []
    for persona in personas:
        if not isinstance(persona, dict):
            continue
        rows.append({field: join_values(persona.get(field)) for field in FIELDS})
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Mapa De Personas E Papéis De Decisão",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Oferta: {payload.get('oferta', '')}",
        f"- Segmento: {payload.get('segmento', '')}",
        f"- Tipo de compra: {payload.get('tipo_compra', '')}",
        "",
        "| Persona | Papel | Dores | Objeções | Provas | CTA | Canal |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        fields = ["persona", "papel", "dores", "objecoes", "provas", "cta", "canal"]
        lines.append("| " + " | ".join(esc(row[field]) for field in fields) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build persona decision map.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    rows = build_rows(payload)
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)
    if not args.csv_path and not args.md_path:
        for row in rows:
            print(f"{row['persona']} - {row['papel']}")


if __name__ == "__main__":
    main()
