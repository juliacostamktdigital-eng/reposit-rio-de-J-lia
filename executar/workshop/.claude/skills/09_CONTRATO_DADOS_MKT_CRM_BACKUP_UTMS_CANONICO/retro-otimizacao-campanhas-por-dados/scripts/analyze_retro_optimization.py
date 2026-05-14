#!/usr/bin/env python3
"""Analyze campaign retro-optimization from analytics-ready CSV."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def to_float(value: str | None) -> float:
    try:
        return float(value or 0)
    except ValueError:
        return 0.0


def to_bool(value: str | None) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "sim", "yes", "won", "ganho"}


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def classify(item: dict[str, float]) -> str:
    leads = item["leads"]
    mql = item["mql"]
    sql = item["sql"]
    won = item["won"]
    if leads < 3 and won == 0:
        return "inconclusivo"
    if won > 0 or sql >= 2:
        return "vencedor"
    if mql > 0 and sql > 0:
        return "promissor"
    if leads > 0 and mql == 0:
        return "barato_mas_ruim" if item["cpl"] <= item["avg_cpl"] else "sem_qualidade"
    if mql > 0 and item["cpl"] > item["avg_cpl"]:
        return "caro_mas_qualificado"
    return "promissor"


def aggregate(rows: list[dict[str, str]], group_by: str) -> list[dict[str, str]]:
    groups: dict[str, dict[str, float]] = defaultdict(lambda: {
        "spend": 0.0, "leads": 0.0, "mql": 0.0, "sql": 0.0, "won": 0.0, "revenue": 0.0, "bad_leads": 0.0,
    })
    for row in rows:
        key = row.get(group_by, "").strip() or "unknown"
        group = groups[key]
        group["spend"] += to_float(row.get("spend"))
        group["leads"] += 1
        group["mql"] += 1 if to_bool(row.get("is_mql")) else 0
        group["sql"] += 1 if to_bool(row.get("is_sql")) else 0
        group["won"] += 1 if to_bool(row.get("is_won")) else 0
        group["revenue"] += to_float(row.get("deal_value"))
        group["bad_leads"] += 1 if row.get("disqualification_reason", "").strip() else 0

    total_spend = sum(item["spend"] for item in groups.values())
    total_leads = sum(item["leads"] for item in groups.values())
    avg_cpl = total_spend / total_leads if total_leads else 0.0

    output = []
    for key, item in groups.items():
        item["cpl"] = item["spend"] / item["leads"] if item["leads"] else 0.0
        item["cpmql"] = item["spend"] / item["mql"] if item["mql"] else 0.0
        item["cpsql"] = item["spend"] / item["sql"] if item["sql"] else 0.0
        item["avg_cpl"] = avg_cpl
        output.append({
            "dimensao": group_by,
            "valor": key,
            "spend": f"{item['spend']:.2f}",
            "leads": str(int(item["leads"])),
            "mql": str(int(item["mql"])),
            "sql": str(int(item["sql"])),
            "vendas": str(int(item["won"])),
            "receita": f"{item['revenue']:.2f}",
            "cpl": f"{item['cpl']:.2f}",
            "cpmql": f"{item['cpmql']:.2f}",
            "cpsql": f"{item['cpsql']:.2f}",
            "taxa_desqualificacao": f"{(item['bad_leads'] / item['leads'] * 100) if item['leads'] else 0:.2f}%",
            "classificacao": classify(item),
        })
    return sorted(output, key=lambda row: (row["classificacao"] != "vencedor", -float(row["receita"]), -int(row["mql"])))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["dimensao", "valor", "spend", "leads", "mql", "sql", "vendas", "receita", "cpl", "cpmql", "cpsql", "taxa_desqualificacao", "classificacao"]
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Análise De Retro Otimização",
        "",
        "| dimensão | valor | spend | leads | MQL | SQL | vendas | CPL | CPMQL | classificação |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['dimensao']} | `{row['valor']}` | {row['spend']} | {row['leads']} | {row['mql']} | {row['sql']} | {row['vendas']} | {row['cpl']} | {row['cpmql']} | {row['classificacao']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze retro-optimization by selected dimension.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--group-by", default="creative_id")
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    rows = aggregate(load_rows(args.input_csv), args.group_by)
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, rows)
    if not args.csv_path and not args.md_path:
        for row in rows:
            print(f"{row['valor']}: {row['classificacao']}")


if __name__ == "__main__":
    main()
