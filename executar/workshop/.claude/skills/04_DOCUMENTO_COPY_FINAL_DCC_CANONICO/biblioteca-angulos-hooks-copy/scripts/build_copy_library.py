#!/usr/bin/env python3
"""Build a copy angle and hook library from JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "cliente",
    "produto_oferta",
    "angulo",
    "persona",
    "papel",
    "nivel_consciencia",
    "dor",
    "desejo",
    "objecao",
    "resposta_objecao",
    "promessa",
    "hook",
    "tipo_hook",
    "prova",
    "etapa",
    "formato",
    "risco",
    "claim_status",
    "claim",
    "fmt",
    "icp",
    "hook_param",
    "mot",
    "dor_param",
    "ang",
    "stage",
    "ver",
    "utm_content_attrs",
]


def normalize_angle(payload: dict[str, Any], item: dict[str, Any]) -> dict[str, str]:
    tracking = item.get("tracking", {})
    if not isinstance(tracking, dict):
        tracking = {}
    row = {
        "cliente": str(payload.get("cliente", "")),
        "produto_oferta": str(payload.get("produto_oferta", "")),
        "angulo": str(item.get("angulo", "")),
        "persona": str(item.get("persona", "")),
        "papel": str(item.get("papel", "")),
        "nivel_consciencia": str(item.get("nivel_consciencia", "")),
        "dor": str(item.get("dor", "")),
        "desejo": str(item.get("desejo", "")),
        "objecao": str(item.get("objecao", "")),
        "resposta_objecao": str(item.get("resposta_objecao", "")),
        "promessa": str(item.get("promessa", "")),
        "hook": str(item.get("hook", "")),
        "tipo_hook": str(item.get("tipo_hook", "")),
        "prova": str(item.get("prova", "")),
        "etapa": str(item.get("etapa", "")),
        "formato": str(item.get("formato", "")),
        "risco": str(item.get("risco", "")),
        "claim_status": str(item.get("claim_status", "")),
        "claim": str(item.get("claim", "")),
        "fmt": str(tracking.get("fmt", "")),
        "icp": str(tracking.get("icp", "")),
        "hook_param": str(tracking.get("hook", "")),
        "mot": str(tracking.get("mot", "")),
        "dor_param": str(tracking.get("dor", "")),
        "ang": str(tracking.get("ang", "")),
        "stage": str(tracking.get("stage", "")),
        "ver": str(tracking.get("ver", "")),
        "utm_content_attrs": "",
    }
    row["utm_content_attrs"] = build_utm_attrs(row)
    return row


def build_utm_attrs(row: dict[str, str]) -> str:
    attrs = [
        ("fmt", row["fmt"]),
        ("icp", row["icp"]),
        ("hook", row["hook_param"]),
        ("mot", row["mot"]),
        ("dor", row["dor_param"]),
        ("ang", row["ang"]),
        ("stage", row["stage"]),
        ("ver", row["ver"]),
    ]
    return "__".join(f"{key}-{value}" for key, value in attrs if value)


def load_rows(path: Path) -> tuple[dict[str, Any], list[dict[str, str]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    angles = payload.get("angulos", [])
    if not isinstance(angles, list):
        raise ValueError("'angulos' must be a list.")
    rows = [normalize_angle(payload, item) for item in angles if isinstance(item, dict)]
    return payload, rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def markdown_table(fields: list[str], rows: list[dict[str, str]]) -> list[str]:
    lines = [
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    return lines


def write_markdown(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Biblioteca De Ângulos E Hooks",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Produto/oferta: {payload.get('produto_oferta', '')}",
        f"- Fonte estratégica: {payload.get('fonte_estrategica', '')}",
        "",
        "## Ângulos E Hooks",
        "",
        *markdown_table(
            ["angulo", "persona", "dor", "promessa", "hook", "tipo_hook", "prova", "etapa", "risco"],
            rows,
        ),
        "",
        "## Atributos Para Tracking",
        "",
        *markdown_table(["angulo", "utm_content_attrs"], rows),
    ]
    claims = payload.get("claims_proibidos", [])
    if isinstance(claims, list) and claims:
        lines.extend(["", "## Claims Proibidos", "", "| claim | motivo | alternativa |", "| --- | --- | --- |"])
        for claim in claims:
            if isinstance(claim, dict):
                lines.append(
                    "| "
                    + " | ".join(
                        escape_md(str(claim.get(field, ""))) for field in ["claim", "motivo", "alternativa"]
                    )
                    + " |"
                )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build copy angle and hook library from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    args = parser.parse_args()

    payload, rows = load_rows(args.input_json)
    if not args.csv_path and not args.md_path:
        for row in rows:
            print(f"{row['angulo']}: {row['hook']} -> {row['utm_content_attrs']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
