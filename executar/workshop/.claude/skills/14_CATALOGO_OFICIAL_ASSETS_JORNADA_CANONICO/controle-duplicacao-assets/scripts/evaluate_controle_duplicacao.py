#!/usr/bin/env python3
"""Renderiza auditoria de duplicacao de assets e valida decisoes (playbook 14)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def yn(x: bool) -> str:
    return "sim" if x else "não"


def block(t: str) -> str:
    s = (t or "").strip()
    return s if s else "_[preencher]_"


def norm_decisao(d: str) -> str:
    return (d or "").strip().lower()


def any_p14(row: dict[str, Any]) -> bool:
    keys = (
        "p14_processo_nao_roda",
        "p14_auditar_n2",
        "p14_aprender_n3",
        "p14_recoleta_contexto",
        "p14_midia_lp_vendas_escuro",
    )
    return any(row.get(k) is True for k in keys)


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    docs = d.get("documentos") or []
    gaps = d.get("gaps_criar") or []
    res = d.get("resumo_executivo") or {}
    risc = d.get("riscos_se_nao_executar") or []

    parts: list[str] = []
    parts.append("# Auditoria — controle de duplicação de assets\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente | {block(m.get('cliente_projeto'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Revisor | {block(m.get('revisor'))} |\n"
        f"| Objetivo | {block(m.get('objetivo_auditoria'))} |\n"
        f"| Pacote v1 | {block(m.get('link_pacote_v1'))} |\n"
    )

    parts.append("## Documentos existentes\n")
    parts.append(
        "| ID | Nome | Local | Catálogo 14 | P1..P5 | Decisão | Alvo mescla/arq | Motivo | Owner | Prazo |\n"
        "|---|---|---|---|---|---|---|---|---|---|"
    )
    for row in docs:
        if not isinstance(row, dict):
            continue
        p5 = "/".join(
            [
                yn(row.get("p14_processo_nao_roda") is True),
                yn(row.get("p14_auditar_n2") is True),
                yn(row.get("p14_aprender_n3") is True),
                yn(row.get("p14_recoleta_contexto") is True),
                yn(row.get("p14_midia_lp_vendas_escuro") is True),
            ]
        )
        parts.append(
            f"| {block(row.get('id'))} | {block(row.get('nome_titulo'))} | {block(row.get('local_link_path'))} | "
            f"{block(row.get('pareamento_catalogo_14'))} | {p5} | {block(row.get('decisao'))} | "
            f"{block(row.get('mesclar_em_ou_arquivar_em'))} | {block(row.get('motivo'))} | "
            f"{block(row.get('owner_acao'))} | {block(row.get('prazo'))} |"
        )
    parts.append("")

    parts.append("## Gaps — criar\n")
    parts.append("| Descrição | Asset catálogo 14 | Owner | Prazo | Deps |\n|---|---|---|---|---|")
    for g in gaps:
        if isinstance(g, dict):
            parts.append(
                f"| {block(g.get('descricao'))} | {block(g.get('asset_alvo_catalogo_14'))} | {block(g.get('owner'))} | "
                f"{block(g.get('prazo'))} | {block(g.get('dependencias'))} |"
            )
    parts.append("")

    parts.append("## Resumo executivo\n")
    parts.append(f"- **Manter:** {block(res.get('manter'))}\n")
    parts.append(f"- **Mesclar:** {block(res.get('mesclar'))}\n")
    parts.append(f"- **Arquivar:** {block(res.get('arquivar'))}\n")
    parts.append(f"- **Criar:** {block(res.get('criar_gaps'))}\n")

    parts.append("## Riscos se não executar\n")
    for r in risc:
        parts.append(f"- {r}")
    if not risc:
        parts.append("- _[nenhum listado]_")
    parts.append("")
    return "\n".join(parts)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    docs = [x for x in (d.get("documentos") or []) if isinstance(x, dict)]
    named = [x for x in docs if (x.get("nome_titulo") or "").strip()]
    if not named:
        issues.append("documentos: pelo menos um item com nome_titulo")

    allowed = {"manter", "mesclar", "arquivar"}
    for row in named:
        rid = row.get("id", "?")
        de = norm_decisao(str(row.get("decisao", "")))
        if de not in allowed:
            issues.append(f"{rid}: decisao deve ser manter, mesclar ou arquivar")
            continue
        if de == "mesclar" and not (row.get("mesclar_em_ou_arquivar_em") or "").strip():
            issues.append(f"{rid}: mesclar exige alvo em mesclar_em_ou_arquivar_em")
        if de == "arquivar" and not (row.get("motivo") or "").strip():
            issues.append(f"{rid}: arquivar exige motivo")
        if de == "manter" and not any_p14(row) and not (row.get("motivo") or "").strip():
            issues.append(
                f"{rid}: manter com todos P14=false — documente excecao em motivo ou mudar decisao (sec 14)"
            )

    for g in d.get("gaps_criar") or []:
        if not isinstance(g, dict):
            continue
        if (g.get("descricao") or "").strip() and not (g.get("owner") or "").strip():
            issues.append("gaps_criar: linha com descricao precisa owner")

    return issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", type=Path, dest="md_path")
    parser.add_argument("--audit", action="store_true")
    args = parser.parse_args()

    data = load(args.input_json)
    if args.md_path:
        args.md_path.write_text(render_md(data), encoding="utf-8")
    if args.audit:
        iss = audit(data)
        if iss:
            print("Lacunas / alertas:")
            for i in iss:
                print(f"  - {i}")
        else:
            print("Auditoria: linhas nomeadas com decisoes coerentes.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
