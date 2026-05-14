#!/usr/bin/env python3
"""Gera Markdown de setup Google Ads a partir de JSON e audita campos críticos (playbook 16)."""

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


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    esc = d.get("escopo") or {}
    ch = (d.get("conta") or {}).get("checklist_conta") or {}
    conv = d.get("conversoes") or {}
    gtm = d.get("gtm") or {}
    neg = d.get("negativas_resumo") or []
    orc = d.get("orcamento") or {}
    camps = d.get("campanhas") or []
    mt = d.get("matriz_testes") or {}
    pg = d.get("pre_go_live") or {}

    parts: list[str] = []
    parts.append("# Setup Google Ads — estrutura (pré go-live)\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente | {block(m.get('cliente'))} |\n"
        f"| Versão | {block(m.get('versao_doc'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Responsável | {block(m.get('responsavel_media'))} |\n"
        f"| Google Ads CID | {block(m.get('google_ads_customer_id'))} |\n"
        f"| Planilha growth/backup | {block(m.get('link_planilha_growth_backup'))} |\n"
        f"| Contrato dados | {block(m.get('link_contrato_dados'))} |\n"
        f"| GA4 | {block(m.get('ga4_property'))} |\n"
        f"| GTM | {block(m.get('gtm_container'))} |\n"
    )
    parts.append("## Escopo\n")
    parts.append(
        f"- [ {'x' if esc.get('search') else ' '} ] Search\n"
        f"- [ {'x' if esc.get('pmax') else ' '} ] Performance Max\n"
        f"- [ {'x' if esc.get('display') else ' '} ] Display / vídeo / remarketing\n"
    )
    parts.append(f"- **Estrutura plano:** {block(d.get('estrutura_plano'))}\n")

    parts.append("## Checklist conta (Seção 4)\n")
    for k, label in (
        ("conta_correta", "Conta correta"),
        ("faturamento_ativo", "Faturamento"),
        ("permissoes_time", "Permissões"),
        ("auto_tagging_avaliado", "Auto-tagging avaliado"),
        ("ga4_vinculado", "GA4 vinculado"),
        ("gtm_publicado", "GTM publicado"),
        ("tag_google_instalada", "Tag Google"),
        ("conversoes_principais_config", "Conversões principais"),
        ("enhanced_conversions", "Enhanced conversions"),
        ("import_offline_planejada", "Import offline planejada"),
        ("listas_remarketing", "Listas remarketing"),
        ("customer_match_preparado", "Customer Match"),
        ("utms_crm_backup", "UTMs até CRM/backup"),
    ):
        ok = "[x]" if ch.get(k) else "[ ]"
        parts.append(f"- {ok} {label}\n")

    parts.append("## Conversões (Seção 5)\n")
    parts.append(f"- **Otimização:** {block(conv.get('otimizacao_principal'))}\n")
    parts.append(f"- **Principais vs secundárias:** {block(conv.get('principais_vs_secundarias'))}\n")
    parts.append(f"- **Profundidade vs volume:** {block(conv.get('justificativa_profundidade_volume'))}\n")

    parts.append("## GTM e parâmetros (Seção 6)\n")
    for k, label in (
        ("gclid_ok", "gclid"),
        ("gbraid_wbraid_ok", "gbraid/wbraid"),
        ("utms_ok", "UTMs"),
        ("v4_client_id_ok", "v4_client_id"),
        ("v4_campaign_id_ok", "v4_campaign_id"),
        ("v4_adgroup_id_ok", "v4_adgroup_id"),
        ("v4_creative_id_ok", "v4_creative_id"),
        ("v4_test_id_ok", "v4_test_id"),
        ("hidden_form_ok", "Campos hidden"),
        ("backup_ok", "Backup"),
        ("crm_ok", "CRM"),
        ("submissao_lead_testada", "Submissão lead testada"),
    ):
        ok = "[x]" if gtm.get(k) else "[ ]"
        parts.append(f"- {ok} {label}\n")

    parts.append("## Negativas (resumo)\n")
    if neg and isinstance(neg, list):
        for n in neg:
            if isinstance(n, str) and n.strip():
                parts.append(f"- {n.strip()}\n")
            elif isinstance(n, dict):
                parts.append(f"- {block(n.get('termo'))}: {block(n.get('motivo'))}\n")
    else:
        parts.append("- _[preencher]_\n")

    parts.append("## Orçamento (Seção 12)\n")
    parts.append(f"- **Lance / objetivo:** {block(orc.get('estrategia_lance'))}\n")
    parts.append(f"- **tCPA/tROAS:** {block(orc.get('tcpa_troas_nota'))}\n")
    parts.append(f"- **Regra mudança budget:** {block(orc.get('regra_mudanca_budget'))}\n")

    parts.append("## Campanhas\n")
    for i, c in enumerate(camps, 1):
        if not isinstance(c, dict):
            continue
        parts.append(f"### Campanha {i}: {block(c.get('nome_taxonomia'))}\n")
        parts.append(f"- `campaign_id`: {block(c.get('campaign_id'))}\n")
        parts.append(f"- Canal: {block(c.get('canal'))} | Objetivo: {block(c.get('objetivo_google'))}\n")
        parts.append(f"- Orçamento: {block(c.get('orcamento_modo'))} | {block(c.get('valor_ou_logica_orcamento'))}\n")
        parts.append(f"- Hipótese: {block(c.get('hipotese'))}\n")
        for j, g in enumerate(c.get("grupos") or [], 1):
            if not isinstance(g, dict):
                continue
            parts.append(f"#### Grupo / asset group {j}: {block(g.get('nome_taxonomia'))}\n")
            parts.append(
                f"- `adgroup_id`: {block(g.get('adgroup_id'))} | "
                f"{block(g.get('intencao_temperatura_tipo'))}\n"
            )
            parts.append(f"- Detalhe: {block(g.get('detalhe_keywords_signals_targeting'))}\n")
            parts.append("| creative_id | Formato | Hipótese |\n|---|---|---|")
            for cr in g.get("criativos") or []:
                if isinstance(cr, dict):
                    parts.append(
                        f"| {block(cr.get('creative_id'))} | {block(cr.get('formato'))} | "
                        f"{block(cr.get('hipotese_leitura'))} |"
                    )
            parts.append("")

    parts.append("## Matriz de testes\n")
    parts.append(f"- **Varia:** {block(mt.get('o_que_varia'))}\n")
    parts.append(f"- **Constante:** {block(mt.get('o_que_constante'))}\n")

    parts.append("## Pré go-live (Seção 14)\n")
    for k, label in (
        ("conversoes_testadas", "Conversões testadas"),
        ("enhanced_conv_avaliadas", "Enhanced conversions avaliadas"),
        ("utms_ids_aplicados", "UTMs e IDs aplicados"),
        ("lead_teste_backup", "Lead teste backup"),
        ("crm_conciliado", "CRM conciliado"),
        ("search_negativas_iniciais", "Search negativas iniciais"),
        ("pmax_assets_suficientes", "PMax assets suficientes"),
        ("audience_signals_config", "Audience signals"),
        ("search_clusters_rsa_ok", "Search clusters/RSAs"),
        ("pmax_assetgroups_url_brand_ok", "PMax asset groups/URL/brand"),
        ("display_placements_freq_safety_ok", "Display placements/freq/safety"),
        ("urls_finais_ok", "URLs finais"),
        ("orcamento_lances_datas_ok", "Orçamento/lances/datas"),
        ("hipotese_planilha_ok", "Hipótese planilha"),
        ("changelog_preparado", "Changelog"),
    ):
        ok = "[x]" if pg.get(k) else "[ ]"
        parts.append(f"- {ok} {label}\n")

    parts.append("\n## Gaps N2\n")
    parts.append(block(d.get("n2_gaps")) + "\n")
    return "\n".join(parts)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not nonempty_str(m.get("cliente")):
        issues.append("meta.cliente vazio")
    if not nonempty_str(m.get("google_ads_customer_id")):
        issues.append("meta.google_ads_customer_id vazio")

    ch = (d.get("conta") or {}).get("checklist_conta") or {}
    for key, lab in (
        ("faturamento_ativo", "conta.faturamento_ativo"),
        ("gtm_publicado", "conta.gtm_publicado"),
        ("tag_google_instalada", "conta.tag_google_instalada"),
        ("conversoes_principais_config", "conta.conversoes_principais_config"),
    ):
        if not ch.get(key):
            issues.append(f"{lab}: marcar OK para N2")

    gtm = d.get("gtm") or {}
    for key, lab in (
        ("submissao_lead_testada", "gtm.submissao_lead_testada"),
        ("utms_ok", "gtm.utms_ok"),
        ("backup_ok", "gtm.backup_ok"),
        ("crm_ok", "gtm.crm_ok"),
        ("v4_campaign_id_ok", "gtm.v4_campaign_id_ok"),
    ):
        if not gtm.get(key):
            issues.append(f"{lab}: obrigatório (Seção 6)")

    conv = d.get("conversoes") or {}
    if not nonempty_str(conv.get("otimizacao_principal")):
        issues.append("conversoes.otimizacao_principal vazio")

    mt = d.get("matriz_testes") or {}
    if not nonempty_str(mt.get("o_que_varia")) or not nonempty_str(mt.get("o_que_constante")):
        issues.append("matriz_testes: preencher o_que_varia e o_que_constante")

    has_c = has_g = has_cr = False
    for c in d.get("campanhas") or []:
        if not isinstance(c, dict):
            continue
        if nonempty_str(c.get("campaign_id")):
            has_c = True
        for g in c.get("grupos") or []:
            if isinstance(g, dict) and nonempty_str(g.get("adgroup_id")):
                has_g = True
                for cr in g.get("criativos") or []:
                    if isinstance(cr, dict) and nonempty_str(cr.get("creative_id")):
                        has_cr = True
    if not has_c:
        issues.append("campanhas: pelo menos um campaign_id")
    if not has_g:
        issues.append("estrutura: pelo menos um adgroup_id (grupo ou asset group)")
    if not has_cr:
        issues.append("estrutura: pelo menos um creative_id")

    pg = d.get("pre_go_live") or {}
    core = (
        "conversoes_testadas",
        "utms_ids_aplicados",
        "lead_teste_backup",
        "crm_conciliado",
        "urls_finais_ok",
    )
    for k in core:
        if not pg.get(k):
            issues.append(f"pre_go_live.{k} precisa true para N2 mínimo")

    esc = d.get("escopo") or {}
    if esc.get("search") and not pg.get("search_negativas_iniciais"):
        issues.append("escopo Search: search_negativas_iniciais (Seção 7/14)")
    if esc.get("search") and not pg.get("search_clusters_rsa_ok"):
        issues.append("escopo Search: search_clusters_rsa_ok quando há Search no ar")

    if esc.get("pmax"):
        for k, lab in (
            ("pmax_assets_suficientes", "pre_go_live.pmax_assets_suficientes"),
            ("audience_signals_config", "pre_go_live.audience_signals_config"),
            ("pmax_assetgroups_url_brand_ok", "pre_go_live.pmax_assetgroups_url_brand_ok"),
        ):
            if not pg.get(k):
                issues.append(f"PMax ativo: {lab} (Seções 8–9/14)")

    if esc.get("display") and not pg.get("display_placements_freq_safety_ok"):
        issues.append("Display no escopo: display_placements_freq_safety_ok (Seção 9/14)")

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
            print("Lacunas (setup Google / playbook 16):")
            for i in iss:
                print(f"  - {i}")
        else:
            print("Auditoria: N2 mínimo, GTM/lead teste e pre_go_live críticos OK.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
