#!/usr/bin/env python3
"""Generate backup leads spreadsheet schema as CSV files."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


SHEETS: dict[str, list[str]] = {
    "00_README": ["field", "value"],
    "01_RAW_LEADS": [
        "raw_row_id", "captured_at", "source_form", "landing_page_url", "conversion_url", "thank_you_url",
        "ip_hash", "user_agent", "name", "email", "phone", "company", "role", "segment", "message",
        "consent_lgpd", "raw_payload",
    ],
    "02_ATTRIBUTION": [
        "lead_id", "raw_row_id", "client_id", "first_utm_source", "first_utm_medium", "first_utm_campaign",
        "first_utm_content", "first_utm_term", "first_landing_page_url", "first_seen_at", "last_utm_source",
        "last_utm_medium", "last_utm_campaign", "last_utm_content", "last_utm_term", "last_landing_page_url",
        "last_seen_at", "v4_campaign_id", "v4_adgroup_id", "v4_creative_id", "v4_test_id",
    ],
    "03_PARSED_PARAMS": [
        "lead_id", "campaign_id", "adgroup_id", "creative_id", "test_id", "objetivo", "tipo_campanha",
        "movimento", "campaign_slug", "cohort", "segmento", "periodo", "publico", "temperatura",
        "posicionamento", "adgroup_slug", "formato", "persona", "hook", "creative_slug", "dor", "angulo",
        "stage", "versao", "placement", "geo", "keyword", "match_type",
    ],
    "04_CRM_MATCH": [
        "lead_id", "crm_contact_id", "crm_deal_id", "crm_owner", "crm_created_at", "lead_status",
        "mql_status", "mql_at", "sql_status", "sql_at", "opportunity_status", "opportunity_at",
        "deal_status", "won_at", "lost_at", "deal_value", "disqualification_reason", "lost_reason",
        "feedback_quality", "feedback_notes", "match_method", "match_confidence",
    ],
    "05_MEDIA_EXPORT": [
        "date", "source", "campaign_id", "campaign_name", "adgroup_id", "adgroup_name", "creative_id",
        "creative_name", "spend", "impressions", "clicks", "ctr", "cpc", "cpm", "platform_leads",
        "platform_conversions",
    ],
    "06_ANALYTICS_READY": [
        "lead_id", "captured_at", "campaign_id", "adgroup_id", "creative_id", "test_id", "source",
        "medium", "cohort", "segmento", "tipo_campanha", "movimento", "publico", "temperatura",
        "posicionamento", "persona", "formato", "hook", "creative_slug", "dor", "angulo", "stage",
        "versao", "lead_status", "is_mql", "is_sql", "is_opportunity", "is_won", "deal_value",
        "disqualification_reason", "feedback_quality", "speed_to_lead_minutes",
    ],
    "07_PIVOTS": ["view_name", "grain", "metric", "dimension", "notes"],
}


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_sheet(path: Path, columns: list[str], rows: list[dict[str, str]] | None = None) -> None:
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for row in rows or []:
            writer.writerow(row)


def readme_rows(payload: dict[str, Any], spreadsheet_name: str) -> list[dict[str, str]]:
    links = payload.get("links", {})
    if not isinstance(links, dict):
        links = {}
    values = {
        "spreadsheet_name": spreadsheet_name,
        "cliente": str(payload.get("cliente", "")),
        "client_id": str(payload.get("client_id", "")),
        "periodo": str(payload.get("periodo", "")),
        "dono": str(payload.get("dono", "")),
        "link_lp": str(links.get("lp", "")),
        "link_crm": str(links.get("crm", "")),
        "link_plano_midia": str(links.get("plano_midia", "")),
        "link_taxonomia_utm": str(links.get("taxonomia_utm", "")),
    }
    return [{"field": key, "value": value} for key, value in values.items()]


def write_manifest(out_dir: Path, payload: dict[str, Any], spreadsheet_name: str) -> None:
    lines = [
        "# Backup Leads UTMs",
        "",
        f"- Planilha: `{spreadsheet_name}`",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Client ID: `{payload.get('client_id', '')}`",
        f"- Período: {payload.get('periodo', '')}",
        "",
        "## Arquivos Gerados",
    ]
    for sheet in SHEETS:
        lines.append(f"- `{sheet}.csv`")
    (out_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate backup leads CSV schema.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    client_id = str(payload.get("client_id", "client"))
    period = str(payload.get("periodo", "yyyy-mm"))
    spreadsheet_name = f"backup_leads_{client_id}_{period}"
    out_dir = args.out / spreadsheet_name
    out_dir.mkdir(parents=True, exist_ok=True)

    for sheet, columns in SHEETS.items():
        rows = readme_rows(payload, spreadsheet_name) if sheet == "00_README" else None
        write_sheet(out_dir / f"{sheet}.csv", columns, rows)
    write_manifest(out_dir, payload, spreadsheet_name)
    print(out_dir)


if __name__ == "__main__":
    main()
