#!/usr/bin/env python3
"""Gera Markdown do blueprint PMax (leadgen) a partir de JSON e audita (playbook 16, Seções 8–9)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def block(t: str) -> str:
    s = (t or "").strip()
    return s if s else "_[preencher]_"


def nonempty_str(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def _lines(label: str, items: list[Any]) -> str:
    xs = [str(x).strip() for x in (items or []) if nonempty_str(str(x))]
    if not xs:
        return f"**{label}:** _[preencher]_\n"
    out = f"**{label}:**\n"
    for x in xs:
        out += f"- {x}\n"
    return out


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    gates = d.get("gates") or {}
    camp = d.get("campanha") or {}
    guard = d.get("guardrails") or {}
    mt = d.get("matriz_testes") or {}
    pg = d.get("pre_go_live_pmax") or {}

    parts: list[str] = []
    parts.append("# Google Ads PMax — leadgen — consolidado\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente | {block(m.get('cliente'))} |\n"
        f"| Versão | {block(m.get('versao_doc'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Responsável | {block(m.get('responsavel'))} |\n"
        f"| Plano mídia | {block(m.get('link_plano_midia_pmax'))} |\n"
        f"| Setup base | {block(m.get('link_setup_google_base'))} |\n"
        f"| Conversão | {block(m.get('conversao_primaria'))} |\n"
    )

    parts.append("## Gates (Seção 8)\n")
    for k, label in (
        ("conversao_bem_configurada", "Conversão bem configurada"),
        ("lp_preserva_dados", "LP preserva dados"),
        ("assets_razoaveis_planejados", "Assets planejados"),
        ("sinal_audience_relevante", "Audience signal relevante"),
        ("budget_aprendizado_adequado", "Budget aprendizado"),
        ("objetivo_expandir_alem_search", "Expandir além de Search"),
    ):
        parts.append(f"- [ {'x' if gates.get(k) else ' '} ] {label}\n")
    parts.append(
        f"- **Exceção risco:** {gates.get('excecao_risco_aceita')} — {block(gates.get('excecao_nota'))}\n"
    )

    parts.append("## Campanha\n")
    parts.append(f"- `campaign_id`: {block(camp.get('campaign_id'))}\n")
    parts.append(f"- Nome: {block(camp.get('nome_taxonomia'))}\n")
    parts.append(f"- URL final: {block(camp.get('url_final'))}\n")
    parts.append(f"- Otimização: {block(camp.get('conversao_otimizacao'))}\n")
    parts.append(f"- Orçamento/aprendizado: {block(camp.get('orcamento_aprendizado_resumo'))}\n")
    parts.append(f"- Prospecção/remarketing: {block(camp.get('prospeccao_remarketing'))}\n")

    parts.append("## Audience signals\n")
    for s in camp.get("audience_signals") or []:
        if isinstance(s, dict):
            parts.append(
                f"- **{block(s.get('tipo'))}:** {block(s.get('descricao'))} ({block(s.get('notas'))})\n"
            )
    if not camp.get("audience_signals"):
        parts.append("- _[preencher]_\n")

    parts.append("## Asset groups\n")
    for i, ag in enumerate(camp.get("asset_groups") or [], 1):
        if not isinstance(ag, dict):
            continue
        parts.append(f"### Grupo {i}: {block(ag.get('angulo'))}\n")
        parts.append(f"- `adgroup_id`: {block(ag.get('adgroup_id'))}\n")
        parts.append(f"- Nome: {block(ag.get('nome_taxonomia'))}\n")
        parts.append(f"- URL override: {block(ag.get('url_final_override'))}\n")
        parts.append(_lines("Headlines curtas", list(ag.get("headlines_curtas") or [])))
        parts.append(_lines("Headlines longas", list(ag.get("headlines_longas") or [])))
        parts.append(_lines("Descrições", list(ag.get("descricoes") or [])))
        parts.append(
            f"- Logo: {ag.get('tem_logo')} | "
            f"Img □: {ag.get('tem_imagem_quadrada')} | "
            f"Img —: {ag.get('tem_imagem_horizontal')} | "
            f"Img |: {ag.get('tem_imagem_vertical')} | "
            f"Vídeo próprio: {ag.get('video_proprio')}\n"
        )
        parts.append(f"- Sitelinks/snippets: {block(ag.get('sitelinks_snippets_resumo'))}\n")

    parts.append("## Guardrails\n")
    parts.append(f"- **URL expansion:** {block(guard.get('url_expansion_politica'))}\n")
    parts.append(f"- **Brand controls:** {block(guard.get('brand_controls'))}\n")
    parts.append(f"- **Metas conversão:** {block(guard.get('metas_conversao'))}\n")
    parts.append(f"- **Lances:** {block(guard.get('lances_estrategia'))}\n")

    parts.append("## Matriz de testes\n")
    parts.append(f"- **Varia:** {block(mt.get('o_que_varia'))}\n")
    parts.append(f"- **Constante:** {block(mt.get('o_que_constante'))}\n")

    parts.append("## Pré go-live PMax\n")
    for k, label in (
        ("assets_suficientes", "Assets suficientes"),
        ("audience_signals_ok", "Audience signals OK"),
        ("asset_groups_url_ok", "Asset groups + URL"),
        ("url_expansion_brand_metas_ok", "URL expansion + brand + metas"),
        ("rastreio_base_ok", "Rastreio base (UTMs/lead teste)"),
        ("hipotese_planilha", "Hipótese planilha"),
        ("changelog", "Changelog"),
        ("sem_ajuste_diario_sem_evidencia", "Sem ajuste diário sem evidência"),
    ):
        parts.append(f"- [ {'x' if pg.get(k) else ' '} ] {label}\n")

    parts.append("\n## Gaps N2\n")
    parts.append(block(d.get("n2_gaps")) + "\n")
    return "\n".join(parts)


def _headline_count(ag: dict[str, Any]) -> int:
    n = 0
    for key in ("headlines_curtas", "headlines_longas"):
        for x in ag.get(key) or []:
            if nonempty_str(str(x)):
                n += 1
    return n


def _desc_count(ag: dict[str, Any]) -> int:
    return sum(1 for x in (ag.get("descricoes") or []) if nonempty_str(str(x)))


def gates_pass(g: dict[str, Any]) -> bool:
    keys = (
        "conversao_bem_configurada",
        "lp_preserva_dados",
        "assets_razoaveis_planejados",
        "sinal_audience_relevante",
        "budget_aprendizado_adequado",
        "objetivo_expandir_alem_search",
    )
    if all(g.get(k) for k in keys):
        return True
    return bool(g.get("excecao_risco_aceita")) and nonempty_str(g.get("excecao_nota"))


def audit(d: dict[str, Any]) -> tuple[list[str], list[str]]:
    issues: list[str] = []
    warns: list[str] = []
    m = d.get("meta") or {}
    if not nonempty_str(m.get("cliente")):
        issues.append("meta.cliente vazio")

    gates = d.get("gates") or {}
    if not gates_pass(gates):
        issues.append("gates Seção 8: atender pré-requisitos ou excecao_risco_aceita + excecao_nota")

    camp = d.get("campanha") or {}
    for key, lab in (
        ("campaign_id", "campanha.campaign_id"),
        ("url_final", "campanha.url_final"),
        ("conversao_otimizacao", "campanha.conversao_otimizacao"),
    ):
        if not nonempty_str(camp.get(key)):
            issues.append(f"{lab} vazio")

    sigs = camp.get("audience_signals") or []
    ok_sig = False
    for s in sigs:
        if isinstance(s, dict) and nonempty_str(s.get("tipo")) and nonempty_str(s.get("descricao")):
            ok_sig = True
    if not ok_sig:
        issues.append("audience_signals: pelo menos um sinal com tipo e descricao (Seção 8/17)")

    ags = [x for x in (camp.get("asset_groups") or []) if isinstance(x, dict)]
    n_ag = len(ags)
    if n_ag < 2:
        issues.append("asset_groups: mínimo 2 no início (Seção 8)")
    if n_ag > 5:
        warns.append(f"{n_ag} asset groups — playbook sugere 2–5 no início (Seção 8)")

    any_video = False
    for ag in ags:
        if not nonempty_str(ag.get("adgroup_id")):
            issues.append("asset_group: adgroup_id vazio")
        if _headline_count(ag) < 3:
            issues.append(
                f"asset_group {ag.get('adgroup_id', '?')}: "
                "mínimo 3 headlines (curtas+longas) por grupo"
            )
        if _desc_count(ag) < 2:
            issues.append(
                f"asset_group {ag.get('adgroup_id', '?')}: mínimo 2 descrições (Seção 9)"
            )
        img = ag.get("tem_imagem_quadrada") or ag.get("tem_imagem_horizontal") or ag.get(
            "tem_imagem_vertical"
        )
        if not img:
            issues.append(
                f"asset_group {ag.get('adgroup_id', '?')}: "
                "marcar pelo menos um formato de imagem (Seção 9)"
            )
        if not ag.get("tem_logo"):
            issues.append(f"asset_group {ag.get('adgroup_id', '?')}: logo necessário (Seção 9)")
        if ag.get("video_proprio"):
            any_video = True
    if not any_video and n_ag:
        warns.append("Nenhum grupo com video_proprio — Seção 9 recomenda vídeo aprovado no DEOC")

    guard = d.get("guardrails") or {}
    for key, lab in (
        ("url_expansion_politica", "guardrails.url_expansion_politica"),
        ("brand_controls", "guardrails.brand_controls"),
        ("metas_conversao", "guardrails.metas_conversao"),
        ("lances_estrategia", "guardrails.lances_estrategia"),
    ):
        if not nonempty_str(guard.get(key)):
            issues.append(f"{lab} vazio (Seção 14 PMax)")

    mt = d.get("matriz_testes") or {}
    if not nonempty_str(mt.get("o_que_varia")) or not nonempty_str(mt.get("o_que_constante")):
        issues.append("matriz_testes incompleta")

    pg = d.get("pre_go_live_pmax") or {}
    for key, lab in (
        ("assets_suficientes", "pre_go_live_pmax.assets_suficientes"),
        ("audience_signals_ok", "pre_go_live_pmax.audience_signals_ok"),
        ("asset_groups_url_ok", "pre_go_live_pmax.asset_groups_url_ok"),
        ("url_expansion_brand_metas_ok", "pre_go_live_pmax.url_expansion_brand_metas_ok"),
    ):
        if not pg.get(key):
            issues.append(f"{lab} para N2 mínimo PMax")

    return issues, warns


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
        iss, warns = audit(data)
        if iss:
            print("Lacunas (PMax leadgen / playbook 16):")
            for i in iss:
                print(f"  - {i}")
        else:
            print("Auditoria: gates, asset groups, sinais, guardrails e pré go-live críticos OK.")
        if warns:
            print("Avisos:")
            for w in warns:
                print(f"  - {w}")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
