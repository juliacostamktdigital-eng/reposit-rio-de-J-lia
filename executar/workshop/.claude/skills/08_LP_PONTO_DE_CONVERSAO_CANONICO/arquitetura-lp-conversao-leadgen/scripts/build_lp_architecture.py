#!/usr/bin/env python3
"""Build LP / conversion point architecture docs from JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


SECTION_FIELDS = [
    "cliente",
    "campanha",
    "tipo_ponto_conversao",
    "ordem",
    "secao",
    "objetivo",
    "titulo",
    "subtitulo",
    "conteudo",
    "prova_asset",
    "cta",
    "evento",
    "tracking",
]

REQUIRED_HIDDEN = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_content",
    "utm_term",
    "v4_client_id",
    "v4_campaign_id",
    "v4_adgroup_id",
    "v4_creative_id",
    "v4_test_id",
    "landing_page_url",
    "conversion_page_url",
    "timestamp",
}

REQUIRED_EVENTS = {"page_view", "lp_view", "form_start", "form_submit", "lead_created", "thank_you_view"}


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_section_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    sections = payload.get("secoes", [])
    if not isinstance(sections, list):
        raise ValueError("'secoes' must be a list.")
    rows: list[dict[str, str]] = []
    for section in sections:
        if not isinstance(section, dict):
            continue
        rows.append({
            "cliente": str(payload.get("cliente", "")),
            "campanha": str(payload.get("campanha", "")),
            "tipo_ponto_conversao": str(payload.get("tipo_ponto_conversao", "")),
            "ordem": str(section.get("ordem", "")),
            "secao": str(section.get("secao", "")),
            "objetivo": str(section.get("objetivo", "")),
            "titulo": str(section.get("titulo", "")),
            "subtitulo": str(section.get("subtitulo", "")),
            "conteudo": str(section.get("conteudo", "")),
            "prova_asset": str(section.get("prova_asset", "")),
            "cta": str(section.get("cta", "")),
            "evento": str(section.get("evento", "")),
            "tracking": str(section.get("tracking", "")),
        })
    return rows


def missing_items(payload: dict[str, Any], field: str, required: set[str]) -> list[str]:
    values = payload.get(field, [])
    if not isinstance(values, list):
        return sorted(required)
    existing = {str(value) for value in values}
    return sorted(required - existing)


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=SECTION_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["ordem", "secao", "objetivo", "titulo", "cta", "evento", "tracking"]
    missing_hidden = missing_items(payload, "campos_ocultos", REQUIRED_HIDDEN)
    missing_events = missing_items(payload, "eventos", REQUIRED_EVENTS)
    lines = [
        "# Mapa De LP / Ponto De Conversão",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Campanha: {payload.get('campanha', '')}",
        f"- Tipo: {payload.get('tipo_ponto_conversao', '')}",
        f"- Persona: {payload.get('persona', '')}",
        f"- Promessa: {payload.get('promessa', '')}",
        f"- CTA principal: {payload.get('cta_principal', '')}",
        "",
        "## Seções",
        "",
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    lines.extend(["", "## Checklist Técnico", ""])
    lines.append(f"- Campos ocultos faltantes: {', '.join(missing_hidden) if missing_hidden else 'nenhum'}")
    lines.append(f"- Eventos faltantes: {', '.join(missing_events) if missing_events else 'nenhum'}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build LP conversion architecture from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    rows = build_section_rows(payload)
    if not args.md_path and not args.csv_path:
        print(f"{payload.get('cliente', '')}: {len(rows)} seções")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
