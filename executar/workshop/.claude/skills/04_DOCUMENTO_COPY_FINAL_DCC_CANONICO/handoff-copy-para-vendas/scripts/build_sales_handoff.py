#!/usr/bin/env python3
"""Build a sales handoff from campaign copy context."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "cliente",
    "campanha",
    "oferta",
    "persona",
    "dor",
    "desejo",
    "objecao",
    "resposta",
    "prova",
    "pergunta_qualificacao",
    "sinal_positivo",
    "sinal_negativo",
]


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    personas = payload.get("personas", [])
    if not isinstance(personas, list):
        raise ValueError("'personas' must be a list.")
    rows: list[dict[str, str]] = []
    for persona in personas:
        if not isinstance(persona, dict):
            continue
        rows.append({
            "cliente": str(payload.get("cliente", "")),
            "campanha": str(payload.get("campanha", "")),
            "oferta": str(payload.get("oferta", "")),
            "persona": str(persona.get("persona", "")),
            "dor": str(persona.get("dor", "")),
            "desejo": str(persona.get("desejo", "")),
            "objecao": str(persona.get("objecao", "")),
            "resposta": str(persona.get("resposta", "")),
            "prova": str(persona.get("prova", "")),
            "pergunta_qualificacao": str(persona.get("pergunta_qualificacao", "")),
            "sinal_positivo": str(persona.get("sinal_positivo", "")),
            "sinal_negativo": str(persona.get("sinal_negativo", "")),
        })
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def bullet_list(items: Any) -> list[str]:
    if not isinstance(items, list):
        return []
    return [f"- {item}" for item in items]


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Handoff De Copy Para Vendas",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Campanha: {payload.get('campanha', '')}",
        f"- Oferta: {payload.get('oferta', '')}",
        f"- CTA: {payload.get('cta', '')}",
        f"- LP: {payload.get('lp', '')}",
        "",
        "## Promessa E Expectativa",
        "",
        f"- Promessa: {payload.get('promessa', '')}",
        f"- Problema nomeado: {payload.get('problema_nomeado', '')}",
        f"- Mecanismo: {payload.get('mecanismo', '')}",
        f"- Prova: {payload.get('prova', '')}",
        f"- Não prometido: {payload.get('nao_prometido', '')}",
        "",
        "## Personas E Abordagem",
        "",
        "| Persona | Dor | Objeção | Resposta | Pergunta de qualificação |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                escape_md(row[field]) for field in ["persona", "dor", "objecao", "resposta", "pergunta_qualificacao"]
            )
            + " |"
        )
    lines.extend([
        "",
        "## Script Inicial",
        "",
        "```text",
        f"Vi que você se interessou por {payload.get('oferta', '')}, sobre {payload.get('problema_nomeado', '')}.",
        f"Normalmente esse tema aparece quando {rows[0]['dor'] if rows else '[dor principal]'}.",
        "Hoje, como vocês lidam com esse ponto no processo atual?",
        "Isso impacta alguma métrica comercial, operacional ou financeira?",
        f"Se fizer sentido, posso te mostrar como {payload.get('oferta', '')} identifica esses pontos.",
        "Vamos marcar uma conversa rápida para avaliar se existe fit?",
        "```",
        "",
        "## Critérios MQL",
        "",
        *bullet_list(payload.get("criterios_mql", [])),
        "",
        "## Critérios SQL",
        "",
        *bullet_list(payload.get("criterios_sql", [])),
        "",
        "## Motivos De Desqualificação",
        "",
        *bullet_list(payload.get("desqualificacao", [])),
        "",
        "## Feedback Para Marketing",
        "",
        *bullet_list(payload.get("feedback_marketing", [])),
    ])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a sales handoff from campaign copy context.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    rows = build_rows(payload)
    if not args.md_path and not args.csv_path:
        for row in rows:
            print(f"{row['persona']}: {row['pergunta_qualificacao']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
