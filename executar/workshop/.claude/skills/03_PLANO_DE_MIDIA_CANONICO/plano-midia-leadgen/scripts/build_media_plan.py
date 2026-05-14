#!/usr/bin/env python3
"""Build channel and campaign tables for a leadgen media plan."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


CHANNEL_FIELDS = [
    "canal",
    "objetivo",
    "etapa_funil",
    "investimento",
    "percentual_budget",
    "cpl_previsto",
    "leads_previstos",
    "mqls_previstos",
    "cpmql_previsto",
    "sqls_previstos",
    "cpsql_previsto",
    "vendas_previstas",
    "cac_previsto",
    "roas_previsto",
    "papel",
    "risco",
    "criterio_revisao",
]

CAMPAIGN_FIELDS = [
    "campaign_id",
    "canal",
    "objetivo",
    "etapa",
    "orcamento",
    "evento",
    "publico",
    "oferta",
    "lp",
    "criativos",
    "hipotese",
    "metrica",
    "janela",
]


def as_float(payload: dict[str, Any], field: str, default: float = 0) -> float:
    try:
        return float(payload.get(field, default) or default)
    except (TypeError, ValueError):
        return default


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def build_channels(payload: dict[str, Any]) -> list[dict[str, str]]:
    budget_total = as_float(payload, "budget_total")
    ticket = as_float(payload, "ticket_medio")
    lead_mql = as_float(payload, "taxa_lead_mql")
    mql_sql = as_float(payload, "taxa_mql_sql")
    sql_venda = as_float(payload, "taxa_sql_venda")

    rows: list[dict[str, str]] = []
    channels = payload.get("canais", [])
    if not isinstance(channels, list):
        raise ValueError("'canais' must be a list.")

    for channel in channels:
        if not isinstance(channel, dict):
            raise ValueError("Each channel must be an object.")
        investimento = as_float(channel, "investimento")
        cpl = as_float(channel, "cpl_previsto")
        leads = safe_div(investimento, cpl)
        mqls = leads * lead_mql
        sqls = mqls * mql_sql
        vendas = sqls * sql_venda
        receita = vendas * ticket
        rows.append({
            "canal": str(channel.get("canal", "")),
            "objetivo": str(channel.get("objetivo", "")),
            "etapa_funil": str(channel.get("etapa_funil", "")),
            "investimento": f"{investimento:.2f}",
            "percentual_budget": f"{safe_div(investimento, budget_total):.2%}",
            "cpl_previsto": f"{cpl:.2f}",
            "leads_previstos": f"{leads:.0f}",
            "mqls_previstos": f"{mqls:.0f}",
            "cpmql_previsto": f"{safe_div(investimento, mqls):.2f}",
            "sqls_previstos": f"{sqls:.0f}",
            "cpsql_previsto": f"{safe_div(investimento, sqls):.2f}",
            "vendas_previstas": f"{vendas:.1f}",
            "cac_previsto": f"{safe_div(investimento, vendas):.2f}",
            "roas_previsto": f"{safe_div(receita, investimento):.2f}",
            "papel": str(channel.get("papel", "")),
            "risco": str(channel.get("risco", "")),
            "criterio_revisao": str(channel.get("criterio_revisao", "")),
        })
    return rows


def build_campaigns(payload: dict[str, Any]) -> list[dict[str, str]]:
    campaigns = payload.get("campanhas", [])
    if not isinstance(campaigns, list):
        raise ValueError("'campanhas' must be a list.")
    return [{field: str(item.get(field, "")) for field in CAMPAIGN_FIELDS} for item in campaigns if isinstance(item, dict)]


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def markdown_table(fields: list[str], rows: list[dict[str, str]]) -> list[str]:
    lines = [
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    return lines


def write_markdown(path: Path, payload: dict[str, Any], channels: list[dict[str, str]], campaigns: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Plano De Mídia Leadgen",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Período: {payload.get('periodo', '')}",
        f"- Budget total: {payload.get('budget_total', '')}",
        "",
        "## Distribuição Por Canal",
        "",
        *markdown_table(CHANNEL_FIELDS, channels),
        "",
        "## Campanhas Planejadas",
        "",
        *markdown_table(CAMPAIGN_FIELDS, campaigns),
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build leadgen media plan tables from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--out", dest="out_dir", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.input_json.read_text(encoding="utf-8"))
    channels = build_channels(payload)
    campaigns = build_campaigns(payload)
    if not args.out_dir and not args.md_path:
        for row in channels:
            print(f"{row['canal']}: {row['investimento']} -> {row['mqls_previstos']} MQLs")
        return
    if args.out_dir:
        write_csv(args.out_dir / "canais.csv", CHANNEL_FIELDS, channels)
        write_csv(args.out_dir / "campanhas.csv", CAMPAIGN_FIELDS, campaigns)
    if args.md_path:
        write_markdown(args.md_path, payload, channels, campaigns)


if __name__ == "__main__":
    main()
