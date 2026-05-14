#!/usr/bin/env python3
"""Calcula linhas da tabela SOM e gera Markdown/CSV a partir de JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def fmt_money(value: float, moeda: str) -> str:
    if moeda.upper() == "BRL":
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{moeda} {value:,.2f}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate TAM/SAM/SOM table.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    data = load(args.input_json)
    moeda = str(data.get("moeda", "BRL"))
    som = data.get("som_inputs") or {}
    if not isinstance(som, dict):
        som = {}

    cap = float(som.get("capacidade_operacional_mes") or 0)
    budget = float(som.get("budget_mensal_aquisicao") or 0)
    cpl = float(som.get("cpl_estimado") or 0)
    taxa = float(som.get("taxa_conversao_lead_cliente") or 0)
    ticket = float(som.get("ticket_medio") or 0)

    leads_mes = budget / cpl if cpl else 0.0
    clientes_bruto = leads_mes * taxa
    clientes_mes = min(cap, clientes_bruto) if cap else clientes_bruto
    fat_mes = clientes_mes * ticket
    som_anual = fat_mes * 12

    rows = [
        ("Capacidade operacional", f"{cap:.0f} clientes/mês" if cap == int(cap) else f"{cap} clientes/mês", "cliente/operação"),
        ("Budget mensal de aquisição", fmt_money(budget, moeda), "cliente/operação"),
        ("CPL ou custo de oportunidade estimado", fmt_money(cpl, moeda), "histórico/benchmark"),
        ("Leads/mês possíveis", f"{leads_mes:.1f}", "cálculo"),
        ("Taxa de conversão estimada", f"{taxa * 100:.2f}%", "histórico/benchmark"),
        ("Clientes/mês capturáveis", f"{clientes_mes:.2f}", "cálculo"),
        ("Faturamento potencial/mês", fmt_money(fat_mes, moeda), "cálculo"),
        ("SOM anual", fmt_money(som_anual, moeda), "cálculo"),
    ]

    if args.csv_path:
        args.csv_path.parent.mkdir(parents=True, exist_ok=True)
        with args.csv_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["variavel", "valor", "fonte"])
            w.writerows(rows)

    if args.md_path:
        tam = data.get("tam") or {}
        sam = data.get("sam") or {}
        lines = [
            "# TAM / SAM / SOM",
            "",
            f"- Cliente: {data.get('cliente', '')}",
            f"- Segmento: {data.get('segmento', '')}",
            f"- Geografia: {data.get('geografia', '')}",
            "",
            "## TAM",
            "",
            f"- Valor: {fmt_money(float(tam.get('valor') or 0), moeda) if isinstance(tam, dict) else ''}",
        ]
        if isinstance(tam, dict):
            lines.extend([
                f"- Fonte: {tam.get('fonte', '')}",
                f"- Ano: {tam.get('ano_fonte', '')}",
                f"- Método: {tam.get('metodo', '')}",
                f"- Incerteza: {tam.get('incerteza', '')}",
            ])
        lines.extend(["", "## SAM", ""])
        if isinstance(sam, dict):
            lines.extend([
                f"- Filtros: {sam.get('filtros', '')}",
                f"- Valor final: {fmt_money(float(sam.get('valor_final') or 0), moeda)}",
                f"- Exclusões: {sam.get('exclusoes', '')}",
            ])
        lines.extend(["", "## SOM (tabela)", "", "| Variável | Valor | Fonte |", "| --- | --- | --- |"])
        for var, val, src in rows:
            lines.append(f"| {var} | {val} | {src} |")
        lines.extend(["", "## Observação", "", "Validar limites de capacidade e premissas de conversão com o cliente antes de usar em ROAS/CAC.", ""])
        args.md_path.parent.mkdir(parents=True, exist_ok=True)
        args.md_path.write_text("\n".join(lines), encoding="utf-8")

    if not args.csv_path and not args.md_path:
        print(f"clientes_mes={clientes_mes:.2f} som_anual={som_anual:.2f}")


if __name__ == "__main__":
    main()
