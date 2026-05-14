#!/usr/bin/env python3
"""Build sales summaries from lead campaign context."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "lead_id",
    "nome",
    "empresa",
    "cargo",
    "sales_owner",
    "campaign_id",
    "creative_id",
    "test_id",
    "persona",
    "dor_angulo",
    "promessa",
    "abordagem_sugerida",
    "pergunta_qualificacao",
    "proximo_passo",
    "campos_feedback",
]


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_approach(lead: dict[str, Any]) -> str:
    name = lead.get("nome", "[nome]")
    offer = lead.get("oferta", "[oferta]")
    pain = lead.get("dor_angulo", "[dor]")
    promise = lead.get("promessa", "[promessa]")
    return (
        f"Oi, {name}. Vi que você pediu mais informações sobre {offer}. "
        f"Normalmente quem chega por esse material está tentando resolver {pain}. "
        f"A ideia é entender se faz sentido avaliar {promise} no contexto de vocês."
    )


def qualification_question(lead: dict[str, Any]) -> str:
    pain = str(lead.get("dor_angulo", "esse ponto"))
    return f"Hoje {pain} é um problema relevante para o time de vocês? Como isso aparece no processo atual?"


def next_step(lead: dict[str, Any]) -> str:
    offer = lead.get("oferta", "a oferta")
    return f"Se houver fit, agendar conversa para avaliar {offer} e confirmar critérios de MQL/SQL."


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    leads = payload.get("leads", [])
    if not isinstance(leads, list):
        raise ValueError("'leads' must be a list.")
    rows: list[dict[str, str]] = []
    for lead in leads:
        if not isinstance(lead, dict):
            continue
        rows.append({
            "lead_id": str(lead.get("lead_id", "")),
            "nome": str(lead.get("nome", "")),
            "empresa": str(lead.get("empresa", "")),
            "cargo": str(lead.get("cargo", "")),
            "sales_owner": str(lead.get("sales_owner", "")),
            "campaign_id": str(lead.get("campaign_id", "")),
            "creative_id": str(lead.get("creative_id", "")),
            "test_id": str(lead.get("test_id", "")),
            "persona": str(lead.get("persona", "")),
            "dor_angulo": str(lead.get("dor_angulo", "")),
            "promessa": str(lead.get("promessa", "")),
            "abordagem_sugerida": build_approach(lead),
            "pergunta_qualificacao": qualification_question(lead),
            "proximo_passo": next_step(lead),
            "campos_feedback": "is_mql,is_sql,is_opportunity,is_won,disqualification_reason,lead_quality,speed_to_lead_minutes,feedback_notes",
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
    lead_map = {str(lead.get("lead_id", "")): lead for lead in payload.get("leads", []) if isinstance(lead, dict)}
    lines = ["# Resumos De Leads Para Vendas", ""]
    for row in rows:
        lead = lead_map.get(row["lead_id"], {})
        lines.extend([
            f"## {row['lead_id']} - {row['nome']}",
            "",
            f"- Empresa/cargo: {row['empresa']} / {row['cargo']}",
            f"- Dono comercial: {row['sales_owner']}",
            f"- Campanha: {lead.get('campaign_name', '')} (`{row['campaign_id']}`)",
            f"- Criativo: {lead.get('creative_context', '')} (`{row['creative_id']}`)",
            f"- LP: {lead.get('lp', '')}",
            f"- CTA: {lead.get('cta', '')}",
            f"- Persona presumida: {row['persona']}",
            f"- Dor/ângulo: {row['dor_angulo']}",
            f"- Promessa vista: {row['promessa']}",
            "",
            "### Abordagem Sugerida",
            "",
            row["abordagem_sugerida"],
            "",
            "### Pergunta De Qualificação",
            "",
            row["pergunta_qualificacao"],
            "",
            "### Próximo Passo",
            "",
            row["proximo_passo"],
            "",
            "### Feedback Obrigatório",
            "",
            "| Campo | Preencher |",
            "| --- | --- |",
        ])
        for field in row["campos_feedback"].split(","):
            lines.append(f"| `{escape_md(field)}` |  |")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build sales summaries from lead campaign context.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    rows = build_rows(payload)
    if not args.md_path and not args.csv_path:
        for row in rows:
            print(f"{row['lead_id']}: {row['pergunta_qualificacao']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
