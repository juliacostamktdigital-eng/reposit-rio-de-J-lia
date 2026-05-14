#!/usr/bin/env python3
"""Monitor lead SLA and routing risks from CRM exports."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


FIELDS = [
    "lead_id",
    "lead_temperature",
    "sales_owner",
    "lead_status",
    "alerta",
    "severidade",
    "acao_recomendada",
]

SUMMARY_FIELDS = ["sales_owner", "leads_em_risco", "criticos", "altos", "medios"]


def parse_dt(value: str) -> datetime | None:
    value = value.strip()
    if not value:
        return None
    return datetime.fromisoformat(value)


def minutes_between(start: datetime | None, end: datetime) -> float:
    if not start:
        return 0.0
    return (end - start).total_seconds() / 60


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def classify(row: dict[str, str], now: datetime) -> list[dict[str, str]]:
    alerts: list[dict[str, str]] = []
    lead_id = row.get("lead_id", "")
    temperature = row.get("lead_temperature", "").strip().lower()
    owner = row.get("sales_owner", "").strip()
    status = row.get("lead_status", "")
    created_at = parse_dt(row.get("created_at", ""))
    first_contact_at = parse_dt(row.get("first_contact_at", ""))
    attempts = int((row.get("contact_attempts", "0") or "0").strip() or 0)
    next_step = row.get("next_step", "").strip()
    age_minutes = minutes_between(created_at, now)

    def add(alert: str, severity: str, action: str) -> None:
        alerts.append({
            "lead_id": lead_id,
            "lead_temperature": temperature,
            "sales_owner": owner or "sem_dono",
            "lead_status": status,
            "alerta": alert,
            "severidade": severity,
            "acao_recomendada": action,
        })

    if not owner:
        add("lead_sem_dono", "critica" if temperature == "quente" else "alta", "atribuir responsável imediatamente")
    if temperature == "quente" and not first_contact_at and age_minutes > 5:
        add("sla_primeiro_contato_estourado", "critica", "fazer primeiro contato e alertar gestor")
    if temperature == "morno" and not first_contact_at and age_minutes > 120:
        add("sla_primeiro_contato_estourado", "alta", "fazer primeiro contato")
    if temperature == "quente" and age_minutes <= 1440 and attempts < 3:
        add("tentativas_primeiro_dia_insuficientes", "media", "executar cadência mínima do primeiro dia")
    if age_minutes >= 10080 and attempts < 6:
        add("tentativas_7_dias_insuficientes", "media", "completar cadência ou mover para nurture")
    if status in {"conectado", "contatado"} and not next_step:
        add("sem_proximo_passo", "media", "preencher próximo passo e data")
    return alerts


def analyze(rows: list[dict[str, str]], now: datetime) -> list[dict[str, str]]:
    alerts: list[dict[str, str]] = []
    for row in rows:
        alerts.extend(classify(row, now))
    return alerts


def summarize(alerts: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[str, Counter[str]] = defaultdict(Counter)
    for alert in alerts:
        owner = alert["sales_owner"]
        grouped[owner]["leads_em_risco"] += 1
        grouped[owner][alert["severidade"]] += 1
    return [{
        "sales_owner": owner,
        "leads_em_risco": str(counts["leads_em_risco"]),
        "criticos": str(counts["critica"]),
        "altos": str(counts["alta"]),
        "medios": str(counts["media"]),
    } for owner, counts in grouped.items()]


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, alerts: list[dict[str, str]], summary_rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Monitor SLA Leads",
        "",
        "## Alertas",
        "",
        "| lead_id | temperatura | dono | alerta | severidade | ação |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for alert in alerts:
        fields = ["lead_id", "lead_temperature", "sales_owner", "alerta", "severidade", "acao_recomendada"]
        lines.append("| " + " | ".join(escape_md(alert[field]) for field in fields) + " |")
    lines.extend(["", "## Resumo Por Responsável", "", "| dono | leads em risco | críticos | altos | médios |", "| --- | --- | --- | --- | --- |"])
    for row in summary_rows:
        fields = ["sales_owner", "leads_em_risco", "criticos", "altos", "medios"]
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Monitor CRM lead SLA from CSV.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--now", required=True, help="Current timestamp in ISO format, e.g. 2026-05-03T12:00:00")
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    parser.add_argument("--summary-csv", dest="summary_csv_path", type=Path)
    args = parser.parse_args()

    now = datetime.fromisoformat(args.now)
    alerts = analyze(read_rows(args.input_csv), now)
    summary_rows = summarize(alerts)
    if not args.md_path and not args.csv_path and not args.summary_csv_path:
        for alert in alerts:
            print(f"{alert['lead_id']}: {alert['severidade']} -> {alert['alerta']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, FIELDS, alerts)
    if args.summary_csv_path:
        write_csv(args.summary_csv_path, SUMMARY_FIELDS, summary_rows)
    if args.md_path:
        write_markdown(args.md_path, alerts, summary_rows)


if __name__ == "__main__":
    main()
