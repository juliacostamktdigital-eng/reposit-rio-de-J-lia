#!/usr/bin/env python3
"""Gera Markdown de especificacao Meta Engajamento/Remarketing e audita requisitos criticos."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def block(value: Any) -> str:
    text = str(value or "").strip()
    return text if text else "_[preencher]_"


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def check(data: dict[str, Any], key: str) -> str:
    return "[x]" if data.get(key) else "[ ]"


def render_md(data: dict[str, Any]) -> str:
    meta = data.get("meta") or {}
    funil = data.get("funcao_funil") or {}
    publicos = data.get("publicos") or {}
    inicial = publicos.get("publico_inicial") or {}
    exclusoes = publicos.get("exclusoes") or {}
    pool = data.get("pool_aquecido") or {}
    matriz = data.get("matriz_testes") or {}
    gov = data.get("orcamento_governanca") or {}
    pre = data.get("pre_go_live_engajamento") or {}

    parts: list[str] = []
    parts.append("# Meta Ads — Engajamento e remarketing\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente | {block(meta.get('cliente'))} |\n"
        f"| Versao | {block(meta.get('versao_doc'))} |\n"
        f"| Data | {block(meta.get('data'))} |\n"
        f"| Responsavel | {block(meta.get('responsavel_media'))} |\n"
        f"| Plano de midia | {block(meta.get('link_plano_midia'))} |\n"
        f"| Setup Meta geral | {block(meta.get('ref_setup_meta'))} |\n"
    )

    parts.append("## Funcao no funil\n")
    for key, label in (
        ("objetivo", "Objetivo"),
        ("etapa_que_aquece", "Etapa que aquece"),
        ("campanha_ou_etapa_seguinte", "Campanha/etapa seguinte"),
        ("metrica_leitura", "Metrica de leitura"),
        ("janela_leitura", "Janela de leitura"),
    ):
        parts.append(f"- **{label}:** {block(funil.get(key))}\n")

    parts.append("## Publicos\n")
    parts.append(f"- **Temperatura inicial:** {block(inicial.get('temperatura'))}\n")
    parts.append(f"- **Descricao:** {block(inicial.get('descricao'))}\n")
    parts.append(f"- **Origem:** {block(inicial.get('origem'))}\n")
    parts.append("### Exclusoes\n")
    for key, label in (
        ("anti_icp", "Anti-ICP"),
        ("leads_clientes_convertidos", "Leads/clientes/convertidos"),
        ("saturados", "Saturados"),
        ("outras", "Outras"),
    ):
        parts.append(f"- **{label}:** {block(exclusoes.get(key))}\n")

    parts.append("## Pool aquecido / remarketing\n")
    for key, label in (
        ("nome_publico", "Nome do publico"),
        ("criterio_entrada", "Criterio de entrada"),
        ("janela", "Janela"),
        ("tamanho_minimo_esperado", "Tamanho minimo esperado"),
        ("destino_campanha_seguinte", "Destino/campanha seguinte"),
        ("regra_saida", "Regra de saida"),
    ):
        parts.append(f"- **{label}:** {block(pool.get(key))}\n")

    parts.append("## Criativos por hipotese\n")
    parts.append("| creative_id | formato | tema/angulo | hipotese | CTA/proximo passo | criterio |\n")
    parts.append("| --- | --- | --- | --- | --- | --- |\n")
    for row in data.get("criativos") or []:
        if isinstance(row, dict):
            parts.append(
                f"| {block(row.get('creative_id'))} | {block(row.get('formato'))} | "
                f"{block(row.get('tema_angulo'))} | {block(row.get('hipotese'))} | "
                f"{block(row.get('cta_proximo_passo'))} | {block(row.get('criterio_leitura'))} |\n"
            )

    parts.append("## Matriz de testes\n")
    parts.append(f"- **Varia:** {block(matriz.get('o_que_varia'))}\n")
    parts.append(f"- **Constante:** {block(matriz.get('o_que_constante'))}\n")

    parts.append("## Orcamento e governanca\n")
    for key, label in (
        ("budget", "Budget"),
        ("modo_orcamento", "Modo de orcamento"),
        ("frequencia_pressao", "Frequencia/pressao"),
        ("condicao_pausar", "Condicao para pausar"),
        ("condicao_levar_publico_remarketing", "Condicao para remarketing"),
    ):
        parts.append(f"- **{label}:** {block(gov.get(key))}\n")

    parts.append("## Pre go-live — engajamento\n")
    for key, label in (
        ("funcao_funil_definida", "Funcao no funil definida"),
        ("publico_inicial_definido", "Publico inicial definido"),
        ("exclusoes_definidas", "Exclusoes definidas"),
        ("pool_aquecido_definido", "Pool aquecido definido"),
        ("campanha_seguinte_definida", "Campanha seguinte definida"),
        ("criativos_ids_hipoteses", "Criativos com IDs e hipoteses"),
        ("matriz_testes_registrada", "Matriz de testes registrada"),
        ("subtipo_marcado_setup_meta", "Subtipo marcado no setup Meta"),
        ("qa_go_live_meta_rodado", "QA go-live Meta rodado"),
    ):
        parts.append(f"- {check(pre, key)} {label}\n")

    parts.append("\n## Gaps N2\n")
    parts.append(block(data.get("n2_gaps")) + "\n")
    return "\n".join(parts)


def audit(data: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    funil = data.get("funcao_funil") or {}
    for key in ("objetivo", "campanha_ou_etapa_seguinte", "metrica_leitura"):
        if not nonempty(funil.get(key)):
            issues.append(f"funcao_funil.{key} vazio")

    pool = data.get("pool_aquecido") or {}
    for key in ("criterio_entrada", "janela", "destino_campanha_seguinte"):
        if not nonempty(pool.get(key)):
            issues.append(f"pool_aquecido.{key} vazio")

    publicos = data.get("publicos") or {}
    exclusoes = publicos.get("exclusoes") or {}
    if not any(nonempty(exclusoes.get(k)) for k in ("anti_icp", "leads_clientes_convertidos", "outras")):
        issues.append("publicos.exclusoes: documentar pelo menos anti-ICP, convertidos/leads ou outra exclusao")

    criativos = data.get("criativos") or []
    if not any(isinstance(c, dict) and nonempty(c.get("creative_id")) and nonempty(c.get("hipotese")) for c in criativos):
        issues.append("criativos: incluir pelo menos um creative_id com hipotese")

    matriz = data.get("matriz_testes") or {}
    if not nonempty(matriz.get("o_que_varia")) or not nonempty(matriz.get("o_que_constante")):
        issues.append("matriz_testes: preencher o_que_varia e o_que_constante")

    pre = data.get("pre_go_live_engajamento") or {}
    for key in (
        "funcao_funil_definida",
        "pool_aquecido_definido",
        "campanha_seguinte_definida",
        "criativos_ids_hipoteses",
        "subtipo_marcado_setup_meta",
    ):
        if not pre.get(key):
            issues.append(f"pre_go_live_engajamento.{key} precisa true para N2 minimo")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--audit", action="store_true")
    args = parser.parse_args()

    data = load(args.input_json)
    if args.md_path:
        args.md_path.write_text(render_md(data), encoding="utf-8")
    if args.audit:
        issues = audit(data)
        if issues:
            print("Lacunas (Meta engajamento / playbook 15):")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("Auditoria: funcao no funil, pool aquecido, criativos, matriz e pre go-live criticos OK.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
