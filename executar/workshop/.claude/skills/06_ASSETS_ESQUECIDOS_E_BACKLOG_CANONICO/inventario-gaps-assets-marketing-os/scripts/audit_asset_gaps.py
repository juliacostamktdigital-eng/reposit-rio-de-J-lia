#!/usr/bin/env python3
"""Audit Marketing OS asset gaps and prioritize them."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "cliente",
    "asset",
    "componente",
    "status",
    "evidencia",
    "gap",
    "severidade",
    "impacto",
    "dono",
    "proxima_acao",
    "score",
    "prioridade",
    "encaminhamento",
]

SEVERITY_SCORE = {
    "critica": 100,
    "crítica": 100,
    "alta": 75,
    "media": 50,
    "média": 50,
    "baixa": 25,
}

STATUS_SCORE = {
    "inexistente": 30,
    "rascunho": 20,
    "incompleto": 15,
    "n2": 0,
    "n3": 0,
}


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def score_asset(asset: dict[str, Any]) -> int:
    severity = str(asset.get("severidade", "")).strip().lower()
    status = str(asset.get("status", "")).strip().lower()
    evidence = str(asset.get("evidencia", "")).strip()
    score = SEVERITY_SCORE.get(severity, 0) + STATUS_SCORE.get(status, 0)
    if not evidence:
        score += 10
    return score


def priority(score: int) -> str:
    if score >= 110:
        return "p0"
    if score >= 85:
        return "p1"
    if score >= 60:
        return "p2"
    return "p3"


def forwarding(asset: dict[str, Any], score: int) -> str:
    severity = str(asset.get("severidade", "")).strip().lower()
    status = str(asset.get("status", "")).strip().lower()
    if severity in {"critica", "crítica"}:
        return "backlog_operacional_go_no_go"
    if status in {"inexistente", "rascunho", "incompleto"} and score >= 60:
        return "backlog_operacional"
    return "monitorar"


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    assets = payload.get("assets", [])
    if not isinstance(assets, list):
        raise ValueError("'assets' must be a list.")
    rows: list[dict[str, str]] = []
    for asset in assets:
        if not isinstance(asset, dict):
            continue
        score = score_asset(asset)
        rows.append({
            "cliente": str(payload.get("cliente", "")),
            "asset": str(asset.get("asset", "")),
            "componente": str(asset.get("componente", "")),
            "status": str(asset.get("status", "")),
            "evidencia": str(asset.get("evidencia", "")),
            "gap": str(asset.get("gap", "")),
            "severidade": str(asset.get("severidade", "")),
            "impacto": str(asset.get("impacto", "")),
            "dono": str(asset.get("dono", "")),
            "proxima_acao": str(asset.get("proxima_acao", "")),
            "score": str(score),
            "prioridade": priority(score),
            "encaminhamento": forwarding(asset, score),
        })
    return sorted(rows, key=lambda row: int(row["score"]), reverse=True)


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
    fields = ["prioridade", "asset", "status", "severidade", "gap", "dono", "encaminhamento"]
    lines = [
        "# Inventário De Gaps De Assets Marketing OS",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Data: {payload.get('data', '')}",
        f"- Responsável: {payload.get('responsavel', '')}",
        "",
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    blockers = [row for row in rows if row["encaminhamento"] == "backlog_operacional_go_no_go"]
    if blockers:
        lines.extend(["", "## Bloqueadores", ""])
        for row in blockers:
            lines.append(f"- {row['asset']}: {row['gap']} ({row['dono']})")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit and prioritize Marketing OS asset gaps.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    rows = build_rows(payload)
    if not args.md_path and not args.csv_path:
        for row in rows:
            print(f"{row['prioridade']} {row['asset']}: {row['encaminhamento']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
