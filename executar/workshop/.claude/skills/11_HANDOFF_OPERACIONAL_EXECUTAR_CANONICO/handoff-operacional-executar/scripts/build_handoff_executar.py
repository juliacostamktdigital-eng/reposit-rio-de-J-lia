#!/usr/bin/env python3
"""Gera Markdown do handoff operacional EXECUTAR a partir de JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def section(title: str, body: str) -> str:
    text = (body or "").strip()
    return f"## {title}\n\n{text}\n" if text else f"## {title}\n\n_\n"


def build_md(data: dict[str, Any]) -> str:
    links = data.get("links") or {}
    if not isinstance(links, dict):
        links = {}

    lines = [
        "# Handoff Operacional EXECUTAR",
        "",
        f"Cliente: {data.get('cliente', '')}",
        f"Produto contratado: {data.get('produto_contratado', '')}",
        f"Data do fechamento: {data.get('data_fechamento', '')}",
        f"Data da Growth Class: {data.get('data_growth_class', '')}",
        f"Squad/Responsável: {data.get('squad_responsavel', '')}",
        "",
        "## Links dos insumos",
        "",
        f"Plano de ROI: {links.get('plano_roi', '')}",
        f"Transcrição da call de vendas: {links.get('transcricao_vendas', '')}",
        f"Transcrição da Growth Class: {links.get('transcricao_growth_class', '')}",
        "",
    ]
    blocks = [
        ("Resumo executivo", data.get("resumo_executivo", "")),
        ("Escopo contratado", data.get("escopo_contratado", "")),
        ("Premissas do Plano de ROI", data.get("premissas_roi", "")),
        ("Promessas e expectativas", data.get("promessas_expectativas", "")),
        ("Dores e objetivos declarados", data.get("dores_objetivos", "")),
        ("Stakeholders", data.get("stakeholders", "")),
        ("Riscos e red flags", data.get("riscos_red_flags", "")),
        ("Divergências venda vs. boas-vindas", data.get("divergencias", "")),
        ("Pendências", data.get("pendencias", "")),
        ("Próximos passos", data.get("proximos_passos", "")),
        ("Síntese da call de vendas", data.get("sintese_vendas", "")),
        ("Síntese da Growth Class", data.get("sintese_growth_class", "")),
        ("Status de completude", data.get("status_completude", "")),
        ("Decisão do responsável", data.get("decisao_responsavel", "")),
    ]
    for title, body in blocks:
        lines.append(section(title, str(body)))
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build EXECUTAR handoff markdown from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path, required=True)
    args = parser.parse_args()
    md = build_md(load(args.input_json))
    args.md_path.parent.mkdir(parents=True, exist_ok=True)
    args.md_path.write_text(md, encoding="utf-8")


if __name__ == "__main__":
    main()
