#!/usr/bin/env python3
"""Build a Growth N3 debrief and backlog from learnings CSV."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


REQUIRED_FIELDS = [
    "test_id",
    "hipotese",
    "resultado",
    "decisao",
    "padrao_observado",
    "evidencia",
    "limite_da_conclusao",
    "recomendacao",
]

BACKLOG_FIELDS = [
    "prioridade",
    "test_id",
    "hipotese",
    "decisao",
    "recomendacao",
    "dono",
]

DECISION_WEIGHT = {
    "corrigir-tracking": 1,
    "escalar": 2,
    "ajustar": 3,
    "criar-novo-teste": 4,
    "revisar-oferta": 5,
    "acionar-vendas": 6,
    "manter": 7,
    "replicar": 8,
    "matar": 9,
    "inconclusivo": 10,
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        missing = [field for field in REQUIRED_FIELDS if field not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"CSV missing required fields: {', '.join(missing)}")
        return [dict(row) for row in reader]


def truth(value: str) -> bool:
    return value.strip().lower() in {"true", "sim", "yes", "1"}


def priority(row: dict[str, str]) -> int:
    decision = row.get("decisao", "").strip()
    base = DECISION_WEIGHT.get(decision, 99)
    if truth(row.get("vira_novo_teste", "")):
        base -= 1
    if truth(row.get("vira_playbook", "")):
        base -= 1
    return max(base, 1)


def write_backlog(rows: list[dict[str, str]], path: Path) -> None:
    sorted_rows = sorted(rows, key=priority)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=BACKLOG_FIELDS)
        writer.writeheader()
        for index, row in enumerate(sorted_rows, start=1):
            writer.writerow({
                "prioridade": index,
                "test_id": row.get("test_id", ""),
                "hipotese": row.get("hipotese", ""),
                "decisao": row.get("decisao", ""),
                "recomendacao": row.get("recomendacao", ""),
                "dono": row.get("dono", ""),
            })


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    decisions = Counter(row.get("decisao", "sem-decisao") for row in rows)
    playbooks = [row for row in rows if truth(row.get("vira_playbook", ""))]
    antipatterns = [row for row in rows if truth(row.get("vira_antipadrao", ""))]
    new_tests = [row for row in rows if truth(row.get("vira_novo_teste", ""))]

    lines = [
        "# Debrief N3 Growth",
        "",
        "## Sumário",
        "",
        f"- Testes analisados: {len(rows)}",
        f"- Padrões candidatos: {len(playbooks)}",
        f"- Anti-padrões candidatos: {len(antipatterns)}",
        f"- Novos testes candidatos: {len(new_tests)}",
        "",
        "## Decisões",
        "",
    ]
    for decision, count in sorted(decisions.items()):
        lines.append(f"- `{decision}`: {count}")

    lines.extend([
        "",
        "## Aprendizados",
        "",
        "| Teste | Decisão | Padrão | Evidência | Limite | Recomendação |",
        "| --- | --- | --- | --- | --- | --- |",
    ])
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                escape_md(row.get(field, ""))
                for field in ["test_id", "decisao", "padrao_observado", "evidencia", "limite_da_conclusao", "recomendacao"]
            )
            + " |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Growth N3 debrief from learnings CSV.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--backlog", dest="backlog_path", type=Path)
    args = parser.parse_args()

    rows = read_rows(args.input_csv)
    if not args.md_path and not args.backlog_path:
        for row in sorted(rows, key=priority):
            print(f"{row.get('test_id')}: {row.get('decisao')} -> {row.get('recomendacao')}")
        return
    if args.md_path:
        write_markdown(rows, args.md_path)
    if args.backlog_path:
        write_backlog(rows, args.backlog_path)


if __name__ == "__main__":
    main()
