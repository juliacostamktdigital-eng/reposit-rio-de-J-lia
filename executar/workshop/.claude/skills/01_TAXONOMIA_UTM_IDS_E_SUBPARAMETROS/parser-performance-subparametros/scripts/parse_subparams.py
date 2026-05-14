#!/usr/bin/env python3
"""Parse Marketing OS UTM subparameters from CSV exports."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


DERIVED_FIELDS = [
    "parsed_campaign_id",
    "tipo_campanha",
    "objetivo",
    "movimento",
    "campaign_slug",
    "cohort",
    "segmento",
    "periodo",
    "parsed_adgroup_id",
    "publico",
    "keyword",
    "match_type",
    "temperatura",
    "posicionamento",
    "adgroup_slug",
    "placement",
    "geo",
    "parsed_creative_id",
    "formato",
    "hook",
    "persona",
    "creative_slug",
    "dor",
    "angulo",
    "etapa_funil",
    "versao",
    "missing_campaign_id",
    "missing_adgroup_id",
    "missing_creative_id",
    "missing_test_id",
    "malformed_utm_campaign",
    "malformed_utm_content",
    "malformed_utm_term",
    "v4_campaign_mismatch",
    "v4_adgroup_mismatch",
    "v4_creative_mismatch",
    "unknown_source",
    "missing_commercial_feedback",
]


def split_subparams(value: str) -> tuple[str, dict[str, str], bool]:
    value = (value or "").strip()
    if not value:
        return "", {}, True
    parts = value.split("__")
    base = parts[0]
    params: dict[str, str] = {}
    malformed = False
    for part in parts[1:]:
        if "-" not in part:
            malformed = True
            continue
        key, raw = part.split("-", 1)
        if not key or not raw:
            malformed = True
            continue
        params[key] = raw
    return base, params, malformed


def truth(value: bool) -> str:
    return "true" if value else "false"


def parse_row(row: dict[str, str]) -> dict[str, str]:
    campaign_id, campaign, malformed_campaign = split_subparams(row.get("utm_campaign", ""))
    adgroup_id, term, malformed_term = split_subparams(row.get("utm_term", ""))
    creative_id, content, malformed_content = split_subparams(row.get("utm_content", ""))

    v4_campaign = row.get("v4_campaign_id", "").strip()
    v4_adgroup = row.get("v4_adgroup_id", "").strip()
    v4_creative = row.get("v4_creative_id", "").strip()
    v4_test = row.get("v4_test_id", "").strip()

    parsed = {
        "parsed_campaign_id": v4_campaign or campaign_id,
        "tipo_campanha": campaign.get("typ", ""),
        "objetivo": campaign.get("obj", ""),
        "movimento": campaign.get("mov", ""),
        "campaign_slug": campaign.get("slug", ""),
        "cohort": campaign.get("coh", ""),
        "segmento": campaign.get("seg", ""),
        "periodo": campaign.get("per", ""),
        "parsed_adgroup_id": v4_adgroup or adgroup_id,
        "publico": term.get("pub", ""),
        "keyword": term.get("kw", ""),
        "match_type": term.get("match", ""),
        "temperatura": term.get("temp", ""),
        "posicionamento": term.get("pos", ""),
        "adgroup_slug": term.get("slug", ""),
        "placement": term.get("plc", ""),
        "geo": term.get("geo", ""),
        "parsed_creative_id": v4_creative or creative_id,
        "formato": content.get("fmt", ""),
        "hook": content.get("hook", ""),
        "persona": content.get("per", ""),
        "creative_slug": content.get("slug", ""),
        "dor": content.get("dor", ""),
        "angulo": content.get("ang", ""),
        "etapa_funil": content.get("stage", ""),
        "versao": content.get("ver", ""),
        "missing_campaign_id": truth(not (v4_campaign or campaign_id)),
        "missing_adgroup_id": truth(not (v4_adgroup or adgroup_id)),
        "missing_creative_id": truth(not (v4_creative or creative_id)),
        "missing_test_id": truth(not v4_test),
        "malformed_utm_campaign": truth(malformed_campaign),
        "malformed_utm_content": truth(malformed_content),
        "malformed_utm_term": truth(malformed_term),
        "v4_campaign_mismatch": truth(bool(v4_campaign and campaign_id and v4_campaign != campaign_id)),
        "v4_adgroup_mismatch": truth(bool(v4_adgroup and adgroup_id and v4_adgroup != adgroup_id)),
        "v4_creative_mismatch": truth(bool(v4_creative and creative_id and v4_creative != creative_id)),
        "unknown_source": truth(not row.get("utm_source", "").strip() or row.get("utm_source", "").strip() == "unknown"),
        "missing_commercial_feedback": truth(not row.get("feedback_quality", "").strip()),
    }
    return parsed


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = list(reader.fieldnames or [])
        rows = [dict(row) for row in reader]
    if not fieldnames:
        raise ValueError("CSV has no header.")
    return fieldnames, rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, str]]) -> list[tuple[str, int]]:
    flags = [field for field in DERIVED_FIELDS if field.startswith(("missing_", "malformed_", "v4_", "unknown_"))]
    return [(flag, sum(1 for row in rows if row.get(flag) == "true")) for flag in flags]


def write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    summary = summarize(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Relatório Parser Performance Subparâmetros",
        "",
        f"- Linhas processadas: {len(rows)}",
        "",
        "| Flag | Linhas afetadas |",
        "| --- | --- |",
    ]
    for flag, count in summary:
        lines.append(f"| `{flag}` | {count} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse Marketing OS UTM subparameters from CSV.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    args = parser.parse_args()

    original_fields, rows = read_csv(args.input_csv)
    output_rows = []
    for row in rows:
        parsed = parse_row(row)
        output_rows.append({**row, **parsed})

    output_fields = original_fields + [field for field in DERIVED_FIELDS if field not in original_fields]
    if not args.csv_path and not args.md_path:
        for flag, count in summarize(output_rows):
            print(f"{flag}: {count}")
        return
    if args.csv_path:
        write_csv(args.csv_path, output_fields, output_rows)
    if args.md_path:
        write_markdown(args.md_path, output_rows)


if __name__ == "__main__":
    main()
