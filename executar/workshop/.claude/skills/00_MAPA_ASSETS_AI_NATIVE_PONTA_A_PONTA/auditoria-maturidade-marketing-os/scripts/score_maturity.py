#!/usr/bin/env python3
"""Score Marketing OS maturity audits from JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


LEVEL_POINTS = {
    "N0": 0,
    "N1": 1,
    "N2": 2,
    "N3": 3,
    "bloqueado": 0,
}

FIELDS = [
    "componente",
    "nivel",
    "score",
    "severidade",
    "evidencia",
    "lacuna",
    "risco",
    "dono",
    "proxima_acao",
]


def load_components(path: Path) -> list[dict[str, str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    components = payload.get("componentes")
    if not isinstance(components, list):
        raise ValueError("JSON must contain a 'componentes' list.")

    result: list[dict[str, str]] = []
    for index, item in enumerate(components, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Component #{index} must be an object.")
        component = str(item.get("componente", "")).strip()
        level = str(item.get("nivel", "")).strip()
        if not component:
            raise ValueError(f"Component #{index} is missing 'componente'.")
        if level not in LEVEL_POINTS:
            raise ValueError(f"Component #{index} has invalid nivel '{level}'. Use N0, N1, N2, N3 or bloqueado.")
        row = {field: str(item.get(field, "")).strip() for field in FIELDS}
        row["componente"] = component
        row["nivel"] = level
        row["score"] = str(LEVEL_POINTS[level])
        if level == "bloqueado" and row.get("severidade") not in {"bloqueador", "alto"}:
            row["severidade"] = "bloqueador"
        result.append(row)
    return result


def classify(score_ratio: float) -> str:
    if score_ratio < 0.4:
        return "vermelho - sistema nao confiavel"
    if score_ratio < 0.7:
        return "amarelo - operacao parcial com riscos"
    if score_ratio < 0.85:
        return "verde parcial - N2 predominante"
    return "verde forte - N2/N3 consistente"


def summary(components: list[dict[str, str]]) -> tuple[int, int, float, str]:
    total = sum(int(item["score"]) for item in components)
    possible = len(components) * 3
    ratio = total / possible if possible else 0
    return total, possible, ratio, classify(ratio)


def write_csv(components: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(components)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(components: list[dict[str, str]], path: Path) -> None:
    total, possible, ratio, label = summary(components)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Auditoria De Maturidade Marketing OS",
        "",
        f"- Score: {total}/{possible} ({ratio:.0%})",
        f"- Classificacao: {label}",
        "",
        "| " + " | ".join(FIELDS) + " |",
        "| " + " | ".join("---" for _ in FIELDS) + " |",
    ]
    for item in components:
        lines.append("| " + " | ".join(escape_md(item[field]) for field in FIELDS) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Score a Marketing OS maturity audit JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    components = load_components(args.input_json)
    if not args.md_path and not args.csv_path:
        total, possible, ratio, label = summary(components)
        print(f"Score: {total}/{possible} ({ratio:.0%}) - {label}")
        return
    if args.md_path:
        write_markdown(components, args.md_path)
    if args.csv_path:
        write_csv(components, args.csv_path)


if __name__ == "__main__":
    main()
