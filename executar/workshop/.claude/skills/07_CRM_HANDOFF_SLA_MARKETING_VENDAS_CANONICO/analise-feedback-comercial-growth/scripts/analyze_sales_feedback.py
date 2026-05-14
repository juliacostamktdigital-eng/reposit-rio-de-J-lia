#!/usr/bin/env python3
"""Analyze sales feedback by campaign and creative."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


FIELDS = [
    "campaign_id",
    "creative_id",
    "test_id",
    "leads",
    "mqls",
    "sqls",
    "opportunities",
    "wins",
    "mql_rate",
    "sql_rate",
    "opportunity_rate",
    "win_rate",
    "avg_speed_to_lead_minutes",
    "quality_high",
    "quality_medium",
    "quality_low",
    "top_disqualification_reason",
    "diagnostico",
    "recomendacao",
]


def truthy(value: str) -> bool:
    return value.strip().lower() in {"true", "1", "sim", "yes"}


def as_float(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def group_rows(rows: list[dict[str, str]]) -> dict[tuple[str, str, str], list[dict[str, str]]]:
    groups: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        key = (row.get("campaign_id", ""), row.get("creative_id", ""), row.get("test_id", ""))
        groups[key].append(row)
    return groups


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def diagnose(leads: int, mqls: int, sqls: int, avg_speed: float, reasons: Counter[str], quality: Counter[str]) -> tuple[str, str]:
    mql_rate = safe_div(mqls, leads)
    sql_rate = safe_div(sqls, mqls)
    top_reason = reasons.most_common(1)[0][0] if reasons else ""
    low_quality = quality.get("baixa", 0)

    if avg_speed > 120 and top_reason == "nao-responde":
        return "sla_comercial", "Revisar speed-to-lead, roteamento e cadência antes de culpar mídia."
    if mql_rate < 0.3 and low_quality >= max(1, leads // 2):
        return "lead_ruim", "Revisar público, promessa, formulário e critérios de qualificação."
    if top_reason in {"sem-fit", "cargo-inadequado", "empresa-inadequada"}:
        return "fit_icp", "Ajustar segmentação, ICP e mensagem de qualificação."
    if top_reason in {"timing-ruim", "sem-budget"}:
        return "oferta_timing", "Revisar oferta, CTA e qualificação por maturidade/timing."
    if mqls and sql_rate < 0.4:
        return "handoff_sql", "Revisar critérios SQL, script e contexto enviado a vendas."
    return "sinal_positivo_ou_inconclusivo", "Manter leitura por volume e cruzar com mídia/funil."


def summarize_group(key: tuple[str, str, str], rows: list[dict[str, str]]) -> dict[str, str]:
    campaign_id, creative_id, test_id = key
    leads = len(rows)
    mqls = sum(1 for row in rows if truthy(row.get("is_mql", "")))
    sqls = sum(1 for row in rows if truthy(row.get("is_sql", "")))
    opportunities = sum(1 for row in rows if truthy(row.get("is_opportunity", "")))
    wins = sum(1 for row in rows if truthy(row.get("is_won", "")))
    speeds = [as_float(row.get("speed_to_lead_minutes", "")) for row in rows if row.get("speed_to_lead_minutes", "")]
    avg_speed = sum(speeds) / len(speeds) if speeds else 0.0
    quality = Counter(row.get("lead_quality", "").strip().lower() for row in rows if row.get("lead_quality", ""))
    reasons = Counter(row.get("disqualification_reason", "").strip() for row in rows if row.get("disqualification_reason", "").strip())
    diagnostic, recommendation = diagnose(leads, mqls, sqls, avg_speed, reasons, quality)
    top_reason = reasons.most_common(1)[0][0] if reasons else ""
    return {
        "campaign_id": campaign_id,
        "creative_id": creative_id,
        "test_id": test_id,
        "leads": str(leads),
        "mqls": str(mqls),
        "sqls": str(sqls),
        "opportunities": str(opportunities),
        "wins": str(wins),
        "mql_rate": f"{safe_div(mqls, leads):.0%}",
        "sql_rate": f"{safe_div(sqls, mqls):.0%}",
        "opportunity_rate": f"{safe_div(opportunities, sqls):.0%}",
        "win_rate": f"{safe_div(wins, opportunities):.0%}",
        "avg_speed_to_lead_minutes": f"{avg_speed:.0f}",
        "quality_high": str(quality.get("alta", 0)),
        "quality_medium": str(quality.get("media", 0) + quality.get("média", 0)),
        "quality_low": str(quality.get("baixa", 0)),
        "top_disqualification_reason": top_reason,
        "diagnostico": diagnostic,
        "recomendacao": recommendation,
    }


def analyze(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [summarize_group(key, group) for key, group in group_rows(rows).items()]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["campaign_id", "creative_id", "leads", "mql_rate", "sql_rate", "avg_speed_to_lead_minutes", "diagnostico", "recomendacao"]
    lines = [
        "# Relatório De Feedback Comercial Growth",
        "",
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze sales feedback by campaign and creative.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    output_rows = analyze(read_rows(args.input_csv))
    if not args.md_path and not args.csv_path:
        for row in output_rows:
            print(f"{row['creative_id']}: {row['diagnostico']} -> {row['recomendacao']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, output_rows)
    if args.md_path:
        write_markdown(args.md_path, output_rows)


if __name__ == "__main__":
    main()
