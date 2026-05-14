#!/usr/bin/env python3
"""Pontua segmentos beachhead e gera Markdown (2x2, SWOT, scorecard) + CSV."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

DEFAULT_PESOS = {
    "urgencia_dor": 2,
    "capacidade_pagar": 2,
    "facilidade_acesso": 1,
    "tamanho_segmento": 1,
    "espaco_mercado": 2,
    "alinhamento_forcas": 2,
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def weighted_total(scores: dict[str, Any], pesos: dict[str, int]) -> float:
    total = 0.0
    for key, weight in pesos.items():
        try:
            s = float(scores.get(key, 0) or 0)
        except (TypeError, ValueError):
            s = 0.0
        total += s * weight
    return round(total, 2)


def esc(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def swot_section(title: str, items: list[Any]) -> list[str]:
    lines = [f"### {title}", ""]
    if not items:
        lines.append("_Nenhum item._")
        lines.append("")
        return lines
    for item in items:
        if isinstance(item, dict):
            lines.append(f"- **{esc(item.get('titulo', ''))}** — evidência: {esc(item.get('evidencia', ''))}; impacto: {esc(item.get('impacto', ''))}; implicação: {esc(item.get('implicacao', ''))}")
        else:
            lines.append(f"- {esc(str(item))}")
    lines.append("")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description="Score beachhead segments and build report.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    data = load(args.input_json)
    pesos = data.get("pesos") or DEFAULT_PESOS
    if not isinstance(pesos, dict):
        pesos = DEFAULT_PESOS
    pesos = {k: int(v) for k, v in {**DEFAULT_PESOS, **pesos}.items() if k in DEFAULT_PESOS}

    segmentos = data.get("segmentos", [])
    if not isinstance(segmentos, list):
        segmentos = []

    results = []
    for seg in segmentos:
        if not isinstance(seg, dict):
            continue
        scores = seg.get("scores") or {}
        if not isinstance(scores, dict):
            scores = {}
        total = weighted_total(scores, pesos)
        results.append({"segmento": str(seg.get("nome", "")), **{k: scores.get(k, "") for k in pesos}, "total_ponderado": total})

    results.sort(key=lambda r: float(r["total_ponderado"]), reverse=True)
    winner = results[0]["segmento"] if results else ""

    if args.csv_path:
        fields = ["segmento"] + list(pesos.keys()) + ["total_ponderado"]
        args.csv_path.parent.mkdir(parents=True, exist_ok=True)
        with args.csv_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            w.writerows(results)

    if args.md_path:
        lines = [
            "# Posicionamento Competitivo E Beachhead",
            "",
            f"- Cliente: {data.get('cliente', '')}",
            f"- Data: {data.get('data', '')}",
            f"- Beachhead recomendado (score): **{winner}**",
            "",
        ]

        m = data.get("mapa_2x2") or {}
        if isinstance(m, dict) and m:
            lines.extend([
                "## Mapa 2x2",
                "",
                f"- Eixo X: {m.get('eixo_x', '')}",
                f"- Eixo Y: {m.get('eixo_y', '')}",
                "",
                "| Nome | X | Y |",
                "| --- | --- | --- |",
            ])
            for p in m.get("pontos", []) or []:
                if isinstance(p, dict):
                    lines.append(f"| {esc(p.get('nome', ''))} | {esc(p.get('x', ''))} | {esc(p.get('y', ''))} |")
            lines.append("")

        sw = data.get("swot") or {}
        if isinstance(sw, dict) and sw:
            lines.append("## SWOT específica")
            lines.append("")
            lines.extend(swot_section("Forças", sw.get("forcas") or []))
            lines.extend(swot_section("Fraquezas", sw.get("fraquezas") or []))
            lines.extend(swot_section("Oportunidades", sw.get("oportunidades") or []))
            lines.extend(swot_section("Ameaças", sw.get("ameacas") or []))

        lines.extend([
            "## Scorecard beachhead",
            "",
            "| Segmento | Total ponderado |",
            "| --- | --- |",
        ])
        for r in results:
            lines.append(f"| {esc(r['segmento'])} | {r['total_ponderado']} |")
        lines.extend(["", "_Critérios: pontos 1 a 5 por dimensão; pesos conforme JSON (padrão playbook Alta=2, Média=1)._ ", ""])

        args.md_path.parent.mkdir(parents=True, exist_ok=True)
        args.md_path.write_text("\n".join(lines), encoding="utf-8")

    if not args.csv_path and not args.md_path:
        print(winner)


if __name__ == "__main__":
    main()
