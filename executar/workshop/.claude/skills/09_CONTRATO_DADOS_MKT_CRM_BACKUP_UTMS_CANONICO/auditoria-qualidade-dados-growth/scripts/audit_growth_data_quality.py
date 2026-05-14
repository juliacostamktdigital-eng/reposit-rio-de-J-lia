#!/usr/bin/env python3
"""Audit growth data quality from an analytics-ready CSV."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def is_blank(value: str | None) -> bool:
    return value is None or value.strip() == ""


def is_unknown_source(row: dict[str, str]) -> bool:
    source = row.get("source") or row.get("utm_source") or row.get("last_utm_source") or row.get("first_utm_source") or ""
    return source.strip().lower() in {"", "unknown", "not_set", "none", "(not set)"}


def has_crm_match(row: dict[str, str]) -> bool:
    confidence = row.get("match_confidence", "").strip().lower()
    return confidence in {"high", "medium"} or not is_blank(row.get("crm_contact_id")) or not is_blank(row.get("crm_deal_id"))


def has_creative_id(row: dict[str, str]) -> bool:
    return not is_blank(row.get("creative_id")) or not is_blank(row.get("v4_creative_id"))


def is_mql(row: dict[str, str]) -> bool:
    status = row.get("mql_status", "").strip().lower()
    flag = row.get("is_mql", "").strip().lower()
    return status in {"sim", "yes", "true", "mql", "qualified"} or flag in {"1", "sim", "yes", "true"}


def has_feedback(row: dict[str, str]) -> bool:
    return any(not is_blank(row.get(field)) for field in ["feedback_quality", "feedback_notes", "disqualification_reason", "lost_reason"])


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def pct(numerator: int, denominator: int) -> float:
    return 0.0 if denominator == 0 else round((numerator / denominator) * 100, 2)


def classify_metric(metric: str, value: float) -> tuple[str, str]:
    if metric == "unknown_source_rate":
        if value < 10:
            return "ok", "baixa fonte desconhecida"
        if value > 15:
            return "alerta", "origem desconhecida acima do limite"
        return "ressalva", "origem desconhecida exige cautela"
    if metric == "crm_match_rate":
        return ("ok", "match CRM saudavel") if value > 90 else ("alerta", "match CRM insuficiente")
    if metric == "creative_id_fill_rate":
        return ("ok", "creative ID preenchido") if value > 95 else ("alerta", "creative ID incompleto")
    if metric == "mql_feedback_rate":
        return ("ok", "feedback MQL suficiente") if value > 80 else ("alerta", "feedback comercial insuficiente")
    if metric == "lead_id_duplicate_rate":
        return ("ok", "duplicidade baixa") if value <= 2 else ("alerta", "duplicidade de lead_id relevante")
    return "ok", ""


def audit(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    total = len(rows)
    lead_ids = [row.get("lead_id", "").strip() for row in rows if row.get("lead_id", "").strip()]
    duplicate_count = len(lead_ids) - len(set(lead_ids))
    mql_rows = [row for row in rows if is_mql(row)]

    metrics = {
        "unknown_source_rate": pct(sum(1 for row in rows if is_unknown_source(row)), total),
        "crm_match_rate": pct(sum(1 for row in rows if has_crm_match(row)), total),
        "creative_id_fill_rate": pct(sum(1 for row in rows if has_creative_id(row)), total),
        "mql_feedback_rate": pct(sum(1 for row in mql_rows if has_feedback(row)), len(mql_rows)),
        "lead_id_duplicate_rate": pct(duplicate_count, total),
    }

    output = []
    for metric, value in metrics.items():
        status, observation = classify_metric(metric, value)
        output.append({
            "metric": metric,
            "value": f"{value:.2f}%",
            "status": status,
            "observation": observation,
        })
    return output


def decision(results: list[dict[str, str]]) -> str:
    alerts = sum(1 for row in results if row["status"] == "alerta")
    warnings = sum(1 for row in results if row["status"] == "ressalva")
    if alerts >= 3:
        return "nao_confiavel"
    if alerts or warnings:
        return "confiavel_com_ressalvas"
    return "confiavel"


def write_csv(path: Path, results: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["metric", "value", "status", "observation"])
        writer.writeheader()
        writer.writerows(results)


def write_markdown(path: Path, results: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Relatório De Qualidade De Dados Growth",
        "",
        f"- Decisão de confiabilidade: {decision(results)}",
        "",
        "| métrica | resultado | status | observação |",
        "| --- | --- | --- | --- |",
    ]
    for row in results:
        lines.append(f"| `{row['metric']}` | {row['value']} | {row['status']} | {row['observation']} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit growth data quality.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    rows = load_rows(args.input_csv)
    results = audit(rows)
    if not args.md_path and not args.csv_path:
        print(decision(results))
        return
    if args.csv_path:
        write_csv(args.csv_path, results)
    if args.md_path:
        write_markdown(args.md_path, results)


if __name__ == "__main__":
    main()
