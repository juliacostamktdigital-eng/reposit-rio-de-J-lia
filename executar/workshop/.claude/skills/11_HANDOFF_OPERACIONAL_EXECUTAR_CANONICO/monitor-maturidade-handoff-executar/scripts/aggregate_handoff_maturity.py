#!/usr/bin/env python3
"""Agrega histórico de handoffs EXECUTAR e gera relatório Markdown/CSV."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from statistics import mean, median
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sev_score(value: str) -> int:
    key = (value or "").strip().lower()
    if key in {"baixo", "baixa", "low"}:
        return 0
    if key in {"medio", "médio", "medium"}:
        return 1
    if key in {"alto", "alta", "high"}:
        return 2
    return 1


def risk_score(value: str) -> int:
    return sev_score(value)


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate handoff maturity metrics.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load(args.input_json)
    rows = payload.get("handoffs", [])
    if not isinstance(rows, list):
        raise ValueError("'handoffs' must be a list.")
    n = len(rows)
    if n == 0:
        raise ValueError("No handoffs in file.")

    completos = sum(1 for r in rows if r.get("pacote_completo"))
    dias = [int(r.get("dias_fechamento_ate_completo") or 0) for r in rows]
    comp_pct = [float(r.get("completude_pct") or 0) for r in rows]
    pends = [float(r.get("pendencias_abertas") or 0) for r in rows]
    desvios = [float(r.get("num_desvios_venda_gc") or 0) for r in rows]
    com_desvio = sum(1 for r in rows if float(r.get("num_desvios_venda_gc") or 0) > 0)
    retrab = sum(1 for r in rows if r.get("retrabalho_planning"))
    churn_alto = sum(1 for r in rows if risk_score(str(r.get("risco_churn_m0", ""))) >= 2)

    sev_max = [sev_score(str(r.get("severidade_max_desvio", ""))) for r in rows]
    avg_sev = mean(sev_max) if sev_max else 0.0

    # Heurística simples N2/N3 processo
    pct_complete = 100.0 * completos / n
    avg_pend = mean(pends)
    if pct_complete >= 90 and avg_pend <= 1.5 and retrab / n <= 0.1 and churn_alto == 0 and avg_sev < 1.2:
        nivel = "proximo_n3"
        nota = "Processo consistente; focar em cadência de feedback e tempo médio."
    elif pct_complete >= 75 and retrab / n <= 0.25:
        nivel = "n2_solido"
        nota = "N2 sustentável com ressalvas; atacar outliers e desvios de alta severidade."
    else:
        nivel = "abaixo_n2"
        nota = "Handoff instável; priorizar insumos, revisão supervisionada e fechamento de pendências."

    summary_rows = [
        {"metric": "contas", "value": str(n)},
        {"metric": "pacotes_completos", "value": str(completos)},
        {"metric": "pct_pacotes_completos", "value": f"{pct_complete:.1f}%"},
        {"metric": "tempo_medio_dias", "value": f"{mean(dias):.1f}"},
        {"metric": "tempo_mediana_dias", "value": f"{median(dias):.1f}"},
        {"metric": "completude_media_pct", "value": f"{mean(comp_pct):.1f}"},
        {"metric": "pendencias_media", "value": f"{avg_pend:.2f}"},
        {"metric": "pct_com_desvio_venda_gc", "value": f"{100.0 * com_desvio / n:.1f}%"},
        {"metric": "pct_retrabalho_planning", "value": f"{100.0 * retrab / n:.1f}%"},
        {"metric": "contas_risco_churn_m0_alto", "value": str(churn_alto)},
        {"metric": "severidade_media_desvio", "value": f"{avg_sev:.2f}"},
        {"metric": "avaliacao_processo", "value": nivel},
    ]

    if args.csv_path:
        args.csv_path.parent.mkdir(parents=True, exist_ok=True)
        with args.csv_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["metric", "value"])
            w.writeheader()
            w.writerows(summary_rows)

    if args.md_path:
        lines = [
            "# Relatório De Maturidade Handoff EXECUTAR",
            "",
            f"- Período: {payload.get('periodo', '')}",
            f"- Avaliação heurística: **{nivel}**",
            f"- Nota: {nota}",
            "",
            "| métrica | valor |",
            "| --- | --- |",
        ]
        for row in summary_rows:
            lines.append(f"| {row['metric']} | {row['value']} |")
        args.md_path.parent.mkdir(parents=True, exist_ok=True)
        args.md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if not args.csv_path and not args.md_path:
        print(nivel)


if __name__ == "__main__":
    main()
