#!/usr/bin/env python3
"""Gera Markdown de setup Meta Ads a partir de JSON e audita campos criticos (playbook 15)."""

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
    co = d.get("conta") or {}
    ch = co.get("checklist_conta") or {}
    ev = d.get("eventos") or {}
    pub = d.get("publicos_resumo") or {}
    camps = d.get("campanhas") or []
    mt = d.get("matriz_testes") or {}
    pg = d.get("pre_go_live") or {}
    sub = d.get("subtipos") or {}

    parts: list[str] = []
    parts.append("# Setup Meta Ads — estrutura (pré go-live)\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente | {block(m.get('cliente'))} |\n"
        f"| Versão | {block(m.get('versao_doc'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Responsável | {block(m.get('responsavel_media'))} |\n"
        f"| Planilha growth/backup | {block(m.get('link_planilha_growth_backup'))} |\n"
        f"| Contrato dados | {block(m.get('link_contrato_dados'))} |\n"
    )

    parts.append("## Conta e IDs\n")
    parts.append(f"- BM ID: {block(co.get('bm_id'))}\n")
    parts.append(f"- Ad account ID: {block(co.get('ad_account_id'))}\n")
    parts.append(f"- Pixel ID: {block(co.get('pixel_id'))}\n")
    parts.append("### Checklist conta\n")
    for k, label in (
        ("bm_correto", "BM correto"),
        ("conta_anuncios_correta", "Conta anúncios"),
        ("pagamento_ativo", "Pagamento"),
        ("pagina_fb", "Página FB"),
        ("instagram", "Instagram"),
        ("dominio_verificado", "Domínio verificado"),
        ("permissoes_time", "Permissões"),
        ("pixel_instalado", "Pixel instalado"),
        ("capi_configurada", "CAPI"),
        ("eventos_testados", "Eventos testados"),
        ("utms_lp", "UTMs na LP"),
        ("backup_lead", "Backup lead"),
        ("crm_conciliavel", "CRM/conciliação"),
    ):
        ok = "[x]" if ch.get(k) else "[ ]"
        parts.append(f"- {ok} {label}\n")

    parts.append("## Eventos\n")
    parts.append(f"- **Otimização:** {block(ev.get('otimizacao_principal'))}\n")
    parts.append(f"- **Nota:** {block(ev.get('justificativa_profundidade_volume'))}\n")

    parts.append("## Públicos (resumo)\n")
    frios = "\n".join(f"- {x}" for x in (pub.get("frios") or []))
    parts.append("**Frios:**\n" + (frios if frios else "- _[preencher]_") + "\n")
    mornos = "\n".join(f"- {x}" for x in (pub.get("mornos") or []))
    parts.append("**Mornos:**\n" + (mornos if mornos else "- _[preencher]_") + "\n")
    quentes = "\n".join(f"- {x}" for x in (pub.get("quentes") or []))
    parts.append("**Quentes:**\n" + (quentes if quentes else "- _[preencher]_") + "\n")
    parts.append(f"**Exclusões:** {block(pub.get('exclusoes'))}\n")

    parts.append("## Campanhas\n")
    for i, c in enumerate(camps, 1):
        if not isinstance(c, dict):
            continue
        parts.append(f"### Campanha {i}: {block(c.get('nome_taxonomia'))}\n")
        parts.append(f"- `campaign_id`: {block(c.get('campaign_id'))}\n")
        parts.append(f"- Objetivo Meta: {block(c.get('objetivo_meta'))}\n")
        parts.append(f"- Tipo: {block(c.get('tipo_movimento'))} | Orçamento: {block(c.get('orcamento_modo'))}\n")
        parts.append(f"- Hipótese: {block(c.get('hipotese'))}\n")
        for j, aj in enumerate(c.get("conjuntos") or [], 1):
            if not isinstance(aj, dict):
                continue
            parts.append(f"#### Conjunto {j}: {block(aj.get('nome_taxonomia'))}\n")
            parts.append(
                f"- `adgroup_id`: {block(aj.get('adgroup_id'))} | Temp: {block(aj.get('temperatura'))}\n"
            )
            parts.append(f"- Público: {block(aj.get('publico_resumo'))}\n")
            parts.append(f"- Exclusões: {block(aj.get('exclusoes'))}\n")
            parts.append("| creative_id | Nome | Formato | Hipótese |\n|---|---|---|---|")
            for an in aj.get("anuncios") or []:
                if isinstance(an, dict):
                    parts.append(
                        f"| {block(an.get('creative_id'))} | {block(an.get('nome_taxonomia'))} | "
                        f"{block(an.get('formato'))} | {block(an.get('hipotese_leitura'))} |"
                    )
            parts.append("")

    parts.append("## Matriz de testes\n")
    parts.append(f"- **Varia:** {block(mt.get('o_que_varia'))}\n")
    parts.append(f"- **Constante:** {block(mt.get('o_que_constante'))}\n")

    parts.append("## Pré go-live\n")
    for k, label in (
        ("campanha_id_ok", "Campanha com ID"),
        ("conjuntos_id_ok", "Conjuntos com ID"),
        ("anuncios_id_ok", "Anúncios com ID"),
        ("publico_temperatura_ok", "Público/temperatura"),
        ("exclusoes_ok", "Exclusões"),
        ("pixel_eventos_ok", "Pixel/eventos"),
        ("utms_ok", "UTMs"),
        ("backup_testada", "Backup testada"),
        ("crm_handoff_testado", "CRM/handoff"),
        ("criativos_aprovados", "Criativos aprovados"),
        ("matriz_testes_registrada", "Matriz testes"),
        ("orcamento_datas_ok", "Orçamento/datas"),
        ("hipotese_planilha_ok", "Hipótese na planilha"),
        ("changelog_preparado", "Changelog"),
    ):
        ok = "[x]" if pg.get(k) else "[ ]"
        parts.append(f"- {ok} {label}\n")

    parts.append("## Subtipos\n")
    parts.append(f"- [ {'x' if sub.get('lead_formulario_nativo') else ' '} ] Lead nativo\n")
    parts.append(f"- [ {'x' if sub.get('conversao_site') else ' '} ] Conversão site\n")
    parts.append(f"- [ {'x' if sub.get('engajamento_construcao_audiencia') else ' '} ] Engajamento/construção audiência\n")

    parts.append("\n## Gaps N2\n")
    parts.append(block(d.get("n2_gaps")) + "\n")

    return "\n".join(parts)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not nonempty_str(m.get("cliente")):
        issues.append("meta.cliente vazio")

    co = d.get("conta") or {}
    if not nonempty_str(co.get("ad_account_id")):
        issues.append("conta.ad_account_id vazio")
    if not nonempty_str(co.get("pixel_id")):
        issues.append("conta.pixel_id vazio")

    ch = co.get("checklist_conta") or {}
    for key, lab in (
        ("pixel_instalado", "checklist.pixel_instalado"),
        ("eventos_testados", "checklist.eventos_testados"),
        ("backup_lead", "checklist.backup_lead"),
    ):
        if not ch.get(key):
            issues.append(f"{lab}: marcar OK para N2")

    ev = d.get("eventos") or {}
    if not nonempty_str(ev.get("otimizacao_principal")):
        issues.append("eventos.otimizacao_principal vazio")

    mt = d.get("matriz_testes") or {}
    if not nonempty_str(mt.get("o_que_varia")) or not nonempty_str(mt.get("o_que_constante")):
        issues.append("matriz_testes: preencher o_que_varia e o_que_constante")

    has_c = has_a = has_cr = False
    for c in d.get("campanhas") or []:
        if not isinstance(c, dict):
            continue
        if nonempty_str(c.get("campaign_id")):
            has_c = True
        for aj in c.get("conjuntos") or []:
            if isinstance(aj, dict) and nonempty_str(aj.get("adgroup_id")):
                has_a = True
                for an in aj.get("anuncios") or []:
                    if isinstance(an, dict) and nonempty_str(an.get("creative_id")):
                        has_cr = True
    if not has_c:
        issues.append("campanhas: pelo menos um campaign_id")
    if not has_a:
        issues.append("estrutura: pelo menos um adgroup_id")
    if not has_cr:
        issues.append("estrutura: pelo menos um creative_id")

    pg = d.get("pre_go_live") or {}
    pre_critical = (
        "campanha_id_ok",
        "conjuntos_id_ok",
        "anuncios_id_ok",
        "pixel_eventos_ok",
        "utms_ok",
        "backup_testada",
        "crm_handoff_testado",
    )
    for k in pre_critical:
        if pg.get(k) is not True:
            issues.append(f"pre_go_live.{k} precisa true para N2 minimo")

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
            print("Lacunas (setup Meta / playbook 15):")
            for i in iss:
                print(f"  - {i}")
        else:
            print("Auditoria: IDs minimos, eventos, backup/CRM e pre_go_live critico OK.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
