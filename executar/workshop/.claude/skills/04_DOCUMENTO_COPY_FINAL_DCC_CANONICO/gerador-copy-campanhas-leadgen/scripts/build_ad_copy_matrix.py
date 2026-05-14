#!/usr/bin/env python3
"""Build a leadgen ad copy matrix from structured briefs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "cliente",
    "campanha",
    "campaign_id",
    "creative_id",
    "persona",
    "etapa",
    "formato",
    "oferta",
    "cta",
    "hipotese",
    "variavel_testada",
    "dor",
    "desejo",
    "angulo",
    "tipo_hook",
    "hook",
    "promessa",
    "prova",
    "objecao_atacada",
    "claim",
    "texto_principal",
    "headline",
    "descricao",
    "risco",
    "utm_content_attrs",
    "qa_flags",
]


def build_utm_attrs(tracking: dict[str, Any]) -> str:
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
    return "__".join(f"{key}-{value}" for key, value in attrs if value)


def qa_flags(ad: dict[str, Any], utm_attrs: str) -> str:
    flags: list[str] = []
    required = ["creative_id", "persona", "etapa", "formato", "hook", "texto_principal", "headline", "cta", "prova"]
    for field in required:
        if not str(ad.get(field, "")).strip():
            flags.append(f"faltando_{field}")
    if not utm_attrs:
        flags.append("tracking_incompleto")
    if not str(ad.get("claim", "")).strip():
        flags.append("claim_nao_declarado")
    if not str(ad.get("variavel_testada", "")).strip():
        flags.append("variavel_nao_declarada")
    return "; ".join(flags) if flags else "ok"


def normalize_ad(payload: dict[str, Any], ad: dict[str, Any]) -> dict[str, str]:
    tracking = ad.get("tracking", {})
    if not isinstance(tracking, dict):
        tracking = {}
    utm_attrs = build_utm_attrs(tracking)
    row = {
        "cliente": str(payload.get("cliente", "")),
        "campanha": str(payload.get("campanha", "")),
        "campaign_id": str(payload.get("campaign_id", "")),
        "creative_id": str(ad.get("creative_id", "")),
        "persona": str(ad.get("persona", "")),
        "etapa": str(ad.get("etapa", "")),
        "formato": str(ad.get("formato", "")),
        "oferta": str(ad.get("oferta", "")),
        "cta": str(ad.get("cta", "")),
        "hipotese": str(ad.get("hipotese", "")),
        "variavel_testada": str(ad.get("variavel_testada", "")),
        "dor": str(ad.get("dor", "")),
        "desejo": str(ad.get("desejo", "")),
        "angulo": str(ad.get("angulo", "")),
        "tipo_hook": str(ad.get("tipo_hook", "")),
        "hook": str(ad.get("hook", "")),
        "promessa": str(ad.get("promessa", "")),
        "prova": str(ad.get("prova", "")),
        "objecao_atacada": str(ad.get("objecao_atacada", "")),
        "claim": str(ad.get("claim", "")),
        "texto_principal": str(ad.get("texto_principal", "")),
        "headline": str(ad.get("headline", "")),
        "descricao": str(ad.get("descricao", "")),
        "risco": str(ad.get("risco", "")),
        "utm_content_attrs": utm_attrs,
        "qa_flags": "",
    }
    row["qa_flags"] = qa_flags(ad, utm_attrs)
    return row


def load_rows(path: Path) -> tuple[dict[str, Any], list[dict[str, str]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    ads = payload.get("anuncios", [])
    if not isinstance(ads, list):
        raise ValueError("'anuncios' must be a list.")
    return payload, [normalize_ad(payload, ad) for ad in ads if isinstance(ad, dict)]


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
    fields = ["creative_id", "persona", "etapa", "formato", "hook", "headline", "cta", "utm_content_attrs", "qa_flags"]
    lines = [
        "# Matriz De Copy Leadgen",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Campanha: {payload.get('campanha', '')}",
        f"- Campaign ID: {payload.get('campaign_id', '')}",
        "",
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    lines.extend(["", "## Copies", ""])
    for row in rows:
        lines.extend([
            f"### {row['creative_id']}",
            "",
            f"**Hipótese:** {row['hipotese']}",
            "",
            f"**Texto principal:** {row['texto_principal']}",
            "",
            f"**Headline:** {row['headline']}",
            "",
            f"**Descrição:** {row['descricao']}",
            "",
        ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a leadgen ad copy matrix from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    args = parser.parse_args()

    payload, rows = load_rows(args.input_json)
    if not args.csv_path and not args.md_path:
        for row in rows:
            print(f"{row['creative_id']}: {row['headline']} [{row['qa_flags']}]")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
