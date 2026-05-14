#!/usr/bin/env python3
"""Join media and funnel exports and compute Growth N3 metrics."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


KEYS = ["campaign_id", "adgroup_id", "creative_id"]
FIELDS = [
    "campaign_id",
    "adgroup_id",
    "creative_id",
    "canal",
    "spend",
    "impressions",
    "clicks",
    "lp_views",
    "leads_media",
    "leads_funil",
    "cpl",
    "mqls",
    "cost_per_mql",
    "sqls",
    "cost_per_sql",
    "opportunities",
    "sales",
    "revenue",
    "cac",
    "roas",
    "avg_speed_to_lead_minutes",
    "feedback_quality",
    "unknown_source_rate",
    "classification",
    "recommended_decision",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return [dict(row) for row in csv.DictReader(file)]


def as_float(value: str) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def key(row: dict[str, str]) -> tuple[str, str, str]:
    return tuple(row.get(field, "").strip() for field in KEYS)  # type: ignore[return-value]


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def classify(row: dict[str, str]) -> tuple[str, str]:
    unknown = as_float(row["unknown_source_rate"])
    leads = as_float(row["leads_funil"])
    mqls = as_float(row["mqls"])
    sqls = as_float(row["sqls"])
    feedback = row.get("feedback_quality", "")

    if unknown > 0.15:
        return "inconclusivo por tracking", "corrigir-tracking"
    if leads < 20:
        return "inconclusivo por volume", "manter"
    if mqls == 0:
        return "perdedor", "ajustar"
    if sqls > 0 and feedback in {"bom", "otimo"}:
        return "vencedor", "escalar"
    if mqls > 0 and feedback in {"ruim", "invalido"}:
        return "lead barato/qualidade baixa", "revisar-oferta"
    return "sinal parcial", "ajustar"


def analyze(media_rows: list[dict[str, str]], funnel_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    funnel_by_key = {key(row): row for row in funnel_rows}
    output: list[dict[str, str]] = []
    for media in media_rows:
        funnel = funnel_by_key.get(key(media), {})
        spend = as_float(media.get("spend", ""))
        leads_media = as_float(media.get("leads", ""))
        leads_funil = as_float(funnel.get("leads", ""))
        mqls = as_float(funnel.get("mqls", ""))
        sqls = as_float(funnel.get("sqls", ""))
        sales = as_float(funnel.get("sales", ""))
        revenue = as_float(funnel.get("revenue", ""))
        row = {
            "campaign_id": media.get("campaign_id", ""),
            "adgroup_id": media.get("adgroup_id", ""),
            "creative_id": media.get("creative_id", ""),
            "canal": media.get("canal", ""),
            "spend": f"{spend:.2f}",
            "impressions": media.get("impressions", ""),
            "clicks": media.get("clicks", ""),
            "lp_views": media.get("lp_views", ""),
            "leads_media": f"{leads_media:.0f}",
            "leads_funil": f"{leads_funil:.0f}",
            "cpl": f"{safe_div(spend, leads_media):.2f}",
            "mqls": f"{mqls:.0f}",
            "cost_per_mql": f"{safe_div(spend, mqls):.2f}",
            "sqls": f"{sqls:.0f}",
            "cost_per_sql": f"{safe_div(spend, sqls):.2f}",
            "opportunities": funnel.get("opportunities", "0"),
            "sales": f"{sales:.0f}",
            "revenue": f"{revenue:.2f}",
            "cac": f"{safe_div(spend, sales):.2f}",
            "roas": f"{safe_div(revenue, spend):.2f}",
            "avg_speed_to_lead_minutes": funnel.get("avg_speed_to_lead_minutes", ""),
            "feedback_quality": funnel.get("feedback_quality", ""),
            "unknown_source_rate": funnel.get("unknown_source_rate", "0"),
            "classification": "",
            "recommended_decision": "",
        }
        classification, decision = classify(row)
        row["classification"] = classification
        row["recommended_decision"] = decision
        output.append(row)
    return output


def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Leitura Performance Growth N3",
        "",
        "| creative_id | spend | leads | cpl | mqls | cost_per_mql | sqls | classification | decision |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        values = [
            row["creative_id"],
            row["spend"],
            row["leads_media"],
            row["cpl"],
            row["mqls"],
            row["cost_per_mql"],
            row["sqls"],
            row["classification"],
            row["recommended_decision"],
        ]
        lines.append("| " + " | ".join(escape_md(value) for value in values) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze Growth N3 performance from media and funnel CSVs.")
    parser.add_argument("--media", required=True, type=Path)
    parser.add_argument("--funnel", required=True, type=Path)
    parser.add_argument("--out", dest="out_csv", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    args = parser.parse_args()

    rows = analyze(read_csv(args.media), read_csv(args.funnel))
    if not args.out_csv and not args.md_path:
        for row in rows:
            print(f"{row['creative_id']}: {row['classification']} -> {row['recommended_decision']}")
        return
    if args.out_csv:
        write_csv(rows, args.out_csv)
    if args.md_path:
        write_markdown(rows, args.md_path)


if __name__ == "__main__":
    main()
