#!/usr/bin/env python3
"""Build creative briefs in Markdown and CSV from structured JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "brief_id",
    "test_id",
    "creative_id",
    "cliente",
    "campanha",
    "adgroup",
    "status",
    "objetivo",
    "etapa_funil",
    "metrica_primaria",
    "hipotese",
    "persona",
    "dor",
    "angulo",
    "hook",
    "promessa",
    "prova",
    "cta",
    "formato",
    "canal",
    "placement",
    "utm_content",
    "metrica_leitura",
    "pendencias",
    "qa_flags",
]


def build_utm_content(brief: dict[str, Any]) -> str:
    creative_id = str(brief.get("creative_id", ""))
    tracking = brief.get("tracking", {})
    if not isinstance(tracking, dict):
        tracking = {}
    attrs = [
        ("fmt", tracking.get("fmt", "")),
        ("icp", tracking.get("icp", "")),
        ("hook", tracking.get("hook", "")),
        ("mot", tracking.get("mot", "")),
        ("dor", tracking.get("dor", "")),
        ("ang", tracking.get("ang", "")),
        ("stage", tracking.get("stage", "")),
        ("ver", tracking.get("ver", "")),
    ]
    suffix = "__".join(f"{key}-{value}" for key, value in attrs if value)
    return "__".join(part for part in [creative_id, suffix] if part)


def qa_flags(brief: dict[str, Any], utm_content: str) -> str:
    required = ["brief_id", "test_id", "creative_id", "objetivo", "hipotese", "persona", "hook", "prova", "cta"]
    flags = [f"faltando_{field}" for field in required if not str(brief.get(field, "")).strip()]
    if not utm_content:
        flags.append("tracking_incompleto")
    if not str(brief.get("metrica_leitura", "")).strip():
        flags.append("sem_metrica_leitura")
    return "; ".join(flags) if flags else "ok"


def normalize_brief(brief: dict[str, Any]) -> dict[str, str]:
    utm_content = build_utm_content(brief)
    row = {field: str(brief.get(field, "")) for field in FIELDS if field not in {"utm_content", "qa_flags"}}
    row["utm_content"] = utm_content
    row["qa_flags"] = qa_flags(brief, utm_content)
    return row


def load_rows(path: Path) -> tuple[dict[str, Any], list[dict[str, str]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    briefs = payload.get("briefs", [])
    if not isinstance(briefs, list):
        raise ValueError("'briefs' must be a list.")
    return payload, [normalize_brief(brief) for brief in briefs if isinstance(brief, dict)]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_script(brief: dict[str, Any]) -> list[str]:
    script = brief.get("roteiro", {})
    if not isinstance(script, dict):
        return []
    labels = [
        ("hook_inicial", "Hook inicial"),
        ("contexto", "Contexto"),
        ("tensao", "Tensão"),
        ("mecanismo", "Mecanismo"),
        ("prova", "Prova"),
        ("cta", "CTA"),
    ]
    lines = ["```text"]
    for key, label in labels:
        lines.append(f"{label}: {script.get(key, '')}")
    lines.append("```")
    return lines


def render_visual_direction(brief: dict[str, Any]) -> list[str]:
    direction = brief.get("direcao_visual", {})
    if not isinstance(direction, dict):
        return []
    return [f"- {key}: {value}" for key, value in direction.items()]


def write_markdown(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw_briefs = payload.get("briefs", [])
    briefs = [brief for brief in raw_briefs if isinstance(brief, dict)] if isinstance(raw_briefs, list) else []
    lines = ["# Briefs Criativos Video-First", ""]
    for brief, row in zip(briefs, rows):
        lines.extend([
            f"## {row['creative_id']} - {row['persona']}",
            "",
            f"- Brief ID: {row['brief_id']}",
            f"- Test ID: {row['test_id']}",
            f"- Cliente: {row['cliente']}",
            f"- Campanha: {row['campanha']}",
            f"- Objetivo: {row['objetivo']}",
            f"- Hipótese: {row['hipotese']}",
            f"- Métrica de leitura: {row['metrica_leitura']}",
            "",
            "### Mensagem",
            "",
            f"- Hook: {row['hook']}",
            f"- Dor: {row['dor']}",
            f"- Ângulo: {row['angulo']}",
            f"- Promessa: {row['promessa']}",
            f"- Prova: {row['prova']}",
            f"- CTA: {row['cta']}",
            "",
            "### Roteiro Base",
            "",
            *render_script(brief),
            "",
            "### Direção Visual",
            "",
            *render_visual_direction(brief),
            "",
            "### Tracking E QA",
            "",
            f"- UTM content: `{escape_md(row['utm_content'])}`",
            f"- QA flags: {row['qa_flags']}",
            f"- Pendências: {row['pendencias']}",
            "",
        ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build creative briefs from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload, rows = load_rows(args.input_json)
    if not args.md_path and not args.csv_path:
        for row in rows:
            print(f"{row['creative_id']}: {row['hipotese']} [{row['qa_flags']}]")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
