#!/usr/bin/env python3
"""Gera Markdown do blueprint Google Search (leadgen) a partir de JSON e audita (playbook 16 / Seção 7)."""

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


def _render_keywords(rows: list[Any]) -> str:
    if not rows:
        return "| _[nenhuma]_ | | |\n"
    parts = "| Keyword | Match | Nota |\n|---|---|---|\n"
    for r in rows:
        if isinstance(r, dict):
            parts += f"| {block(r.get('termo'))} | {block(r.get('match'))} | {block(r.get('nota'))} |\n"
    return parts


def _render_rsa(rsa: dict[str, Any]) -> str:
    h = rsa.get("headlines") or []
    d = rsa.get("descricoes") or []
    hs = "\n".join(f"- {x}" for x in h if nonempty_str(str(x))) or "- _[preencher]_"
    ds = "\n".join(f"- {x}" for x in d if nonempty_str(str(x))) or "- _[preencher]_"
    return f"**Headlines:**\n{hs}\n**Descrições:**\n{ds}\n**Path1:** {block(rsa.get('path1'))} **Path2:** {block(rsa.get('path2'))}\n"


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    dem = d.get("demanda_ativa") or {}
    pol = d.get("politica_match") or {}
    parts: list[str] = []
    parts.append("# Google Search — leadgen — consolidado\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente | {block(m.get('cliente'))} |\n"
        f"| Versão | {block(m.get('versao_doc'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Responsável | {block(m.get('responsavel'))} |\n"
        f"| Plano mídia | {block(m.get('link_plano_midia_search'))} |\n"
        f"| Setup base | {block(m.get('link_setup_google_base'))} |\n"
        f"| URL LP | {block(m.get('url_final_lp'))} |\n"
        f"| Conversão | {block(m.get('conversao_primaria'))} |\n"
    )

    parts.append("## Demanda ativa (Seção 7)\n")
    for k, label in (
        ("problema", "Problema"),
        ("solucao_categoria", "Solução/categoria"),
        ("concorrente_permitido", "Concorrência permitida"),
        ("marca_defesa_captura", "Marca defesa/captura"),
    ):
        parts.append(f"- [ {'x' if dem.get(k) else ' '} ] {label}\n")
    parts.append(f"- **Hipótese:** {block(dem.get('hipotese_search'))}\n")

    parts.append("## Política de match\n")
    parts.append(f"- **Inicial:** {block(pol.get('fase_inicial'))}\n")
    parts.append(f"- **Ampliar quando:** {block(pol.get('criterio_ampliar_match'))}\n")

    for i, c in enumerate(d.get("campanhas") or [], 1):
        if not isinstance(c, dict):
            continue
        parts.append(f"## Campanha {i} — {block(c.get('tipo'))}\n")
        parts.append(f"- `campaign_id`: {block(c.get('campaign_id'))}\n")
        parts.append(f"- Nome: {block(c.get('nome_taxonomia'))}\n")
        parts.append(f"- URL final: {block(c.get('url_final'))}\n")
        parts.append(f"- Objetivo/lances: {block(c.get('objetivo_lances_resumo'))}\n")
        parts.append(f"- UTMs/contrato: {'OK' if c.get('utms_contrato_ok') else 'pendente'}\n")
        parts.append(f"- Hipótese: {block(c.get('hipotese'))}\n")
        for j, g in enumerate(c.get("grupos") or [], 1):
            if not isinstance(g, dict):
                continue
            parts.append(f"### Grupo {j}: {block(g.get('cluster'))}\n")
            parts.append(f"- `adgroup_id`: {block(g.get('adgroup_id'))}\n")
            parts.append(f"- Nome: {block(g.get('nome_taxonomia'))}\n")
            parts.append(_render_keywords(g.get("keywords") or []))
            parts.append(_render_rsa(g.get("rsa") or {}))

    cm = d.get("campanha_marca") or {}
    if cm.get("ativa"):
        parts.append("## Campanha marca\n")
        parts.append(f"- `campaign_id`: {block(cm.get('campaign_id'))}\n")
        parts.append(f"- {block(cm.get('nome_taxonomia'))} | URL: {block(cm.get('url_final'))}\n")
        parts.append(f"- Notas: {block(cm.get('notas'))}\n")

    cc = d.get("campanha_concorrentes") or {}
    if cc.get("ativa"):
        parts.append("## Campanha concorrentes\n")
        parts.append(f"- Compliance: {'sim' if cc.get('compliance_ok') else 'NÃO'}\n")
        parts.append(f"- `campaign_id`: {block(cc.get('campaign_id'))}\n")
        parts.append(f"- Guardrails: {block(cc.get('guardrails_copy'))}\n")

    parts.append("## Negativas baseline\n")
    for n in d.get("negativas_baseline") or []:
        if isinstance(n, dict):
            parts.append(
                f"- **{block(n.get('termo'))}** — {block(n.get('motivo'))} "
                f"({block(n.get('escopo'))})\n"
            )
        elif isinstance(n, str) and n.strip():
            parts.append(f"- {n.strip()}\n")
    if not d.get("negativas_baseline"):
        parts.append("- _[preencher]_\n")

    mn = d.get("marca_negativa_nao_marca") or {}
    parts.append(
        f"## Marca como negativa na não-marca\n- Aplica: {mn.get('aplica')} — {block(mn.get('notas'))}\n"
    )

    parts.append(f"## Rotina search terms\n{block(d.get('rotina_search_terms'))}\n")
    parts.append(f"## Extensões\n{block(d.get('extensoes_resumo'))}\n")

    mt = d.get("matriz_testes") or {}
    parts.append("## Matriz de testes\n")
    parts.append(f"- **Varia:** {block(mt.get('o_que_varia'))}\n")
    parts.append(f"- **Constante:** {block(mt.get('o_que_constante'))}\n")

    pg = d.get("pre_go_live_search") or {}
    parts.append("## Pré go-live Search\n")
    for k, label in (
        ("clusters_ok", "Clusters sem mistura indevida"),
        ("negativas_iniciais", "Negativas iniciais"),
        ("rsas_conferidas", "RSAs conferidas"),
        ("urls_rastreio_ok", "URLs e rastreio"),
        ("leitura_marca_separada", "Leitura marca vs não-marca"),
        ("concorrentes_compliance", "Concorrentes / compliance"),
        ("hipotese_planilha", "Hipótese planilha"),
        ("changelog", "Changelog"),
    ):
        ok = "[x]" if pg.get(k) else "[ ]"
        parts.append(f"- {ok} {label}\n")

    parts.append("\n## Gaps N2\n")
    parts.append(block(d.get("n2_gaps")) + "\n")
    return "\n".join(parts)


def _count_keywords(camps: list[Any]) -> int:
    n = 0
    for c in camps or []:
        if not isinstance(c, dict):
            continue
        for g in c.get("grupos") or []:
            if not isinstance(g, dict):
                continue
            for kw in g.get("keywords") or []:
                if isinstance(kw, dict) and nonempty_str(kw.get("termo")):
                    n += 1
    return n


def _rsa_ok(rsa: dict[str, Any]) -> bool:
    h = [x for x in (rsa.get("headlines") or []) if nonempty_str(str(x))]
    d = [x for x in (rsa.get("descricoes") or []) if nonempty_str(str(x))]
    return len(h) >= 3 and len(d) >= 2


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not nonempty_str(m.get("cliente")):
        issues.append("meta.cliente vazio")

    dem = d.get("demanda_ativa") or {}
    if not any(
        dem.get(k)
        for k in ("problema", "solucao_categoria", "concorrente_permitido", "marca_defesa_captura")
    ):
        if not nonempty_str(dem.get("hipotese_search")):
            issues.append("demanda_ativa: marcar pelo menos um tipo (Seção 7) ou hipótese")

    if not nonempty_str(d.get("rotina_search_terms")):
        issues.append("rotina_search_terms vazio (Seção 11 — cadência)")

    neg = d.get("negativas_baseline") or []
    if len(neg) < 1:
        issues.append("negativas_baseline: pelo menos 1 termo (Seção 7/11)")

    mt = d.get("matriz_testes") or {}
    if not nonempty_str(mt.get("o_que_varia")) or not nonempty_str(mt.get("o_que_constante")):
        issues.append("matriz_testes incompleta")

    camps = d.get("campanhas") or []
    has_nao_marca = False
    for c in camps:
        if not isinstance(c, dict):
            continue
        if c.get("tipo") == "nao_marca":
            has_nao_marca = True
            if not nonempty_str(c.get("campaign_id")):
                issues.append("campanha não-marca: campaign_id vazio")
            if not nonempty_str(c.get("url_final")):
                issues.append("campanha não-marca: url_final vazio")
            grupos = c.get("grupos") or []
            if len(grupos) < 1:
                issues.append("não-marca: pelo menos um ad group (Seção 7)")
            for g in grupos:
                if not isinstance(g, dict):
                    continue
                if not nonempty_str(g.get("adgroup_id")):
                    issues.append("grupo: adgroup_id vazio")
                if not _rsa_ok(g.get("rsa") or {}):
                    issues.append(
                        f"grupo {g.get('adgroup_id', '?')}: RSA mínimo 3 headlines e 2 descrições"
                    )

    if not has_nao_marca:
        issues.append("incluir campanha tipo nao_marca (Seção 7)")

    if _count_keywords(camps) < 5:
        issues.append("keywords: pelo menos 5 termos no conjunto não-marca (controle inicial)")

    cm = d.get("campanha_marca") or {}
    if cm.get("ativa") and not nonempty_str(cm.get("campaign_id")):
        issues.append("campanha_marca ativa sem campaign_id")

    cc = d.get("campanha_concorrentes") or {}
    if cc.get("ativa"):
        if not cc.get("compliance_ok"):
            issues.append("concorrentes ativos: compliance_ok precisa true (Seção 7)")
        if not nonempty_str(cc.get("campaign_id")):
            issues.append("campanha_concorrentes: campaign_id vazio")

    pg = d.get("pre_go_live_search") or {}
    for k, lab in (
        ("clusters_ok", "pre_go_live_search.clusters_ok"),
        ("negativas_iniciais", "pre_go_live_search.negativas_iniciais"),
        ("rsas_conferidas", "pre_go_live_search.rsas_conferidas"),
        ("urls_rastreio_ok", "pre_go_live_search.urls_rastreio_ok"),
    ):
        if not pg.get(k):
            issues.append(f"{lab} para N2 mínimo Search")

    if cm.get("ativa") and not pg.get("leitura_marca_separada"):
        issues.append("marca ativa: leitura_marca_separada (Seção 7/17)")

    if cc.get("ativa") and not pg.get("concorrentes_compliance"):
        issues.append("concorrentes: marcar concorrentes_compliance no pré go-live")

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
        iss = audit(data)
        if iss:
            print("Lacunas (Search leadgen / playbook 16):")
            for i in iss:
                print(f"  - {i}")
        else:
            print("Auditoria: não-marca, negativas, RSA, keywords e pré go-live críticos OK.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
