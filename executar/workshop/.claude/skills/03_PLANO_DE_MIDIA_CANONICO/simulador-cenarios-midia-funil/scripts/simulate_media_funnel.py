#!/usr/bin/env python3
"""Simulate pessimistic, likely and optimistic media funnel scenarios."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "cenario",
    "budget",
    "cpl",
    "leads",
    "taxa_lead_mql",
    "mqls",
    "cpmql",
    "taxa_mql_sql",
    "sqls",
    "cpsql",
    "taxa_sql_opp",
    "oportunidades",
    "custo_oportunidade",
    "taxa_opp_venda",
    "taxa_sql_venda",
    "vendas",
    "receita",
    "cac",
    "roas",
    "alertas",
    "fonte_premissas",
]


def as_float(payload: dict[str, Any], field: str, default: float = 0) -> float:
    try:
        return float(payload.get(field, default) or default)
    except (TypeError, ValueError):
        return default


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def simulate(scenario: dict[str, Any], goals: dict[str, Any]) -> dict[str, str]:
    budget = as_float(scenario, "budget")
    cpl = as_float(scenario, "cpl")
    lead_mql = as_float(scenario, "taxa_lead_mql")
    mql_sql = as_float(scenario, "taxa_mql_sql")
    sql_opp = as_float(scenario, "taxa_sql_opp")
    opp_venda = as_float(scenario, "taxa_opp_venda")
    sql_venda = as_float(scenario, "taxa_sql_venda")
    ticket = as_float(scenario, "ticket_medio")

    leads = safe_div(budget, cpl)
    mqls = leads * lead_mql
    sqls = mqls * mql_sql
    oportunidades = sqls * sql_opp if sql_opp else 0
    vendas = oportunidades * opp_venda if oportunidades and opp_venda else sqls * sql_venda
    receita = vendas * ticket
    cac = safe_div(budget, vendas)
    roas = safe_div(receita, budget)

    alerts = build_alerts(
        leads=leads,
        mqls=mqls,
        sqls=sqls,
        vendas=vendas,
        receita=receita,
        cac=cac,
        roas=roas,
        goals=goals,
        source=str(scenario.get("fonte_premissas", "")),
    )

    return {
        "cenario": str(scenario.get("cenario", "")),
        "budget": f"{budget:.2f}",
        "cpl": f"{cpl:.2f}",
        "leads": f"{leads:.0f}",
        "taxa_lead_mql": f"{lead_mql:.2%}",
        "mqls": f"{mqls:.0f}",
        "cpmql": f"{safe_div(budget, mqls):.2f}",
        "taxa_mql_sql": f"{mql_sql:.2%}",
        "sqls": f"{sqls:.0f}",
        "cpsql": f"{safe_div(budget, sqls):.2f}",
        "taxa_sql_opp": f"{sql_opp:.2%}",
        "oportunidades": f"{oportunidades:.0f}",
        "custo_oportunidade": f"{safe_div(budget, oportunidades):.2f}",
        "taxa_opp_venda": f"{opp_venda:.2%}",
        "taxa_sql_venda": f"{sql_venda:.2%}",
        "vendas": f"{vendas:.1f}",
        "receita": f"{receita:.2f}",
        "cac": f"{cac:.2f}",
        "roas": f"{roas:.2f}",
        "alertas": "; ".join(alerts) if alerts else "sem alertas críticos",
        "fonte_premissas": str(scenario.get("fonte_premissas", "")),
    }


def build_alerts(
    *,
    leads: float,
    mqls: float,
    sqls: float,
    vendas: float,
    receita: float,
    cac: float,
    roas: float,
    goals: dict[str, Any],
    source: str,
) -> list[str]:
    alerts: list[str] = []
    if as_float(goals, "leads") and leads < as_float(goals, "leads"):
        alerts.append("abaixo da meta de leads")
    if as_float(goals, "mqls") and mqls < as_float(goals, "mqls"):
        alerts.append("abaixo da meta de MQLs")
    if as_float(goals, "sqls") and sqls < as_float(goals, "sqls"):
        alerts.append("abaixo da meta de SQLs")
    if as_float(goals, "vendas") and vendas < as_float(goals, "vendas"):
        alerts.append("abaixo da meta de vendas")
    if as_float(goals, "receita") and receita < as_float(goals, "receita"):
        alerts.append("abaixo da meta de receita")
    if as_float(goals, "cac_maximo") and cac > as_float(goals, "cac_maximo"):
        alerts.append("CAC acima do limite")
    if as_float(goals, "roas_alvo") and roas < as_float(goals, "roas_alvo"):
        alerts.append("ROAS abaixo do alvo")
    if as_float(goals, "capacidade_atendimento") and leads > as_float(goals, "capacidade_atendimento"):
        alerts.append("volume acima da capacidade comercial")
    if not source:
        alerts.append("fonte de premissas ausente")
    return alerts


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


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
    fields = ["cenario", "budget", "cpl", "leads", "mqls", "sqls", "vendas", "receita", "cac", "roas", "alertas"]
    lines = [
        "# Simulação De Cenários Mídia Funil",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        "",
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    lines.extend(["", "## Recomendação", "", recommendation(rows)])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def recommendation(rows: list[dict[str, str]]) -> str:
    likely = next((row for row in rows if row["cenario"].lower() in {"provavel", "provável"}), None)
    optimistic = next((row for row in rows if row["cenario"].lower() == "otimista"), None)
    if likely and "sem alertas críticos" in likely["alertas"]:
        return "Cenário provável sustenta a meta. Avançar com plano, mantendo guardrails e leitura semanal."
    if optimistic and "sem alertas críticos" in optimistic["alertas"]:
        return "Apenas o cenário otimista parece saudável. Recalibrar meta, budget ou premissas antes de prometer resultado."
    return "Cenários indicam inviabilidade ou risco alto. Revisar budget, meta, canal, conversões ou capacidade comercial."


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate media funnel scenarios from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    scenarios = payload.get("cenarios", [])
    goals = payload.get("meta", {})
    if not isinstance(scenarios, list):
        raise ValueError("'cenarios' must be a list.")
    rows = [simulate(scenario, goals if isinstance(goals, dict) else {}) for scenario in scenarios if isinstance(scenario, dict)]
    if not args.csv_path and not args.md_path:
        for row in rows:
            print(f"{row['cenario']}: {row['vendas']} vendas, ROAS {row['roas']} - {row['alertas']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
