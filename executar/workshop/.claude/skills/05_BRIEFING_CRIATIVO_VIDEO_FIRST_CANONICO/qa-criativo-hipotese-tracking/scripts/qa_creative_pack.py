#!/usr/bin/env python3
"""QA creative packs for hypothesis, claims, LP coherence and tracking."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


CREATIVE_FIELDS = [
    "cliente",
    "campanha",
    "creative_id",
    "brief_id",
    "test_id",
    "formato",
    "canal",
    "placement",
    "decisao",
    "bloqueios",
    "pendencias",
]

BACKLOG_FIELDS = [
    "cliente",
    "campanha",
    "creative_id",
    "pendencia",
    "categoria",
    "severidade",
    "dono",
    "decisao",
    "prazo",
    "impacto",
]

BLOCKING_CRITERIA = {"tracking_completo", "claim_permitido", "prova_presente", "lp_coerente"}
TRACKING_FIELDS = ["creative_id", "fmt", "icp", "hook", "mot", "dor", "ang", "stage", "ver", "utm_content"]


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_status(value: Any) -> str:
    return str(value or "").strip().lower()


def missing_tracking(tracking: dict[str, Any]) -> list[str]:
    return [field for field in TRACKING_FIELDS if not str(tracking.get(field, "")).strip()]


def decide(creative: dict[str, Any]) -> tuple[str, list[str], list[str]]:
    criteria = creative.get("criterios", {})
    if not isinstance(criteria, dict):
        criteria = {}
    tracking = creative.get("tracking", {})
    if not isinstance(tracking, dict):
        tracking = {}

    blocks: list[str] = []
    pending: list[str] = []
    for key, value in criteria.items():
        status = normalize_status(value)
        if status == "bloqueio":
            blocks.append(key)
        elif status == "pendencia":
            pending.append(key)

    missing = missing_tracking(tracking)
    if missing:
        blocks.append("tracking_incompleto:" + ",".join(missing))

    hard_blocks = [block for block in blocks if any(criteria in block for criteria in BLOCKING_CRITERIA)]
    if hard_blocks:
        if any("tracking" in block for block in hard_blocks):
            decision = "bloquear_tracking"
        elif any("claim" in block for block in hard_blocks):
            decision = "bloquear_claim"
        elif any("prova" in block for block in hard_blocks):
            decision = "bloquear_prova"
        else:
            decision = "no_go"
    elif blocks:
        decision = "no_go"
    elif pending:
        decision = "go_com_pendencia"
    else:
        decision = "go"
    return decision, blocks, pending


def build_creative_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for creative in iter_creatives(payload):
        decision, blocks, pending = decide(creative)
        rows.append({
            "cliente": str(payload.get("cliente", "")),
            "campanha": str(payload.get("campanha", "")),
            "creative_id": str(creative.get("creative_id", "")),
            "brief_id": str(creative.get("brief_id", "")),
            "test_id": str(creative.get("test_id", "")),
            "formato": str(creative.get("formato", "")),
            "canal": str(creative.get("canal", "")),
            "placement": str(creative.get("placement", "")),
            "decisao": decision,
            "bloqueios": "; ".join(blocks),
            "pendencias": "; ".join(pending),
        })
    return rows


def build_backlog_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for creative in iter_creatives(payload):
        pending_items = creative.get("pendencias", [])
        if not isinstance(pending_items, list):
            continue
        for item in pending_items:
            if not isinstance(item, dict):
                continue
            rows.append({
                "cliente": str(payload.get("cliente", "")),
                "campanha": str(payload.get("campanha", "")),
                "creative_id": str(creative.get("creative_id", "")),
                "pendencia": str(item.get("pendencia", "")),
                "categoria": str(item.get("categoria", "")),
                "severidade": str(item.get("severidade", "")),
                "dono": str(item.get("dono", "")),
                "decisao": str(item.get("decisao", "")),
                "prazo": str(item.get("prazo", "")),
                "impacto": str(item.get("impacto", "")),
            })
    return rows


def iter_creatives(payload: dict[str, Any]) -> list[dict[str, Any]]:
    creatives = payload.get("criativos", [])
    if not isinstance(creatives, list):
        raise ValueError("'criativos' must be a list.")
    return [creative for creative in creatives if isinstance(creative, dict)]


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, creative_rows: list[dict[str, str]], backlog_rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# QA Criativo Hipótese Tracking",
        "",
        "## Decisões",
        "",
        "| creative_id | formato | decisao | bloqueios | pendencias |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in creative_rows:
        fields = ["creative_id", "formato", "decisao", "bloqueios", "pendencias"]
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    lines.extend(["", "## Backlog 06", "", "| creative_id | pendencia | categoria | severidade | dono | decisao | prazo |", "| --- | --- | --- | --- | --- | --- | --- |"])
    for row in backlog_rows:
        fields = ["creative_id", "pendencia", "categoria", "severidade", "dono", "decisao", "prazo"]
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="QA creative pack for hypothesis and tracking.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path, help="Backlog CSV output.")
    parser.add_argument("--decisions-csv", dest="decisions_csv_path", type=Path, help="Optional decisions CSV output.")
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    creative_rows = build_creative_rows(payload)
    backlog_rows = build_backlog_rows(payload)
    if not args.md_path and not args.csv_path and not args.decisions_csv_path:
        for row in creative_rows:
            print(f"{row['creative_id']}: {row['decisao']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, BACKLOG_FIELDS, backlog_rows)
    if args.decisions_csv_path:
        write_csv(args.decisions_csv_path, CREATIVE_FIELDS, creative_rows)
    if args.md_path:
        write_markdown(args.md_path, creative_rows, backlog_rows)


if __name__ == "__main__":
    main()
