#!/usr/bin/env python3
"""Gera Markdown de especificação Lead Nativo Meta a partir de JSON e audita requisitos críticos (playbook 15)."""

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


def _bool_check(pr: dict[str, Any], key: str) -> str:
    return "[x]" if pr.get(key) else "[ ]"


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    pr = d.get("pre_requisitos") or {}
    lf = d.get("lead_form") or {}
    orig = d.get("origem_rastreio") or {}
    inte = d.get("integracao") or {}
    sla = d.get("sla") or {}
    pub = d.get("publicos_form") or {}
    tst = d.get("teste_p2p") or {}
    mt = d.get("matriz_testes") or {}
    pg = d.get("pre_go_live_lead_nativo") or {}

    parts: list[str] = []
    parts.append("# Meta Ads — Lead nativo — consolidado\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente | {block(m.get('cliente'))} |\n"
        f"| Versão | {block(m.get('versao_doc'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Responsável | {block(m.get('responsavel_media'))} |\n"
        f"| Planilha growth/backup | {block(m.get('link_planilha_growth_backup'))} |\n"
        f"| Contrato dados | {block(m.get('link_contrato_dados'))} |\n"
        f"| Ref. setup estrutura | {block(m.get('ref_setup_estrutura'))} |\n"
    )

    parts.append("## Pré-requisitos (captação / nativo)\n")
    for k, label in (
        ("oferta_deoc_alinhada", "Oferta DEOC/guardrails"),
        ("crm_sla_definido", "CRM e SLA"),
        ("planilha_backup_ativa", "Backup ativo"),
        ("sla_followup_aceito_antes_ativar", "SLA aceito antes de ativar nativo"),
        ("hipotese_leitura_planilha", "Hipótese e leitura na planilha"),
    ):
        parts.append(f"- {_bool_check(pr, k)} {label}\n")

    parts.append("## Lead Form\n")
    parts.append(f"- **Nome interno:** {block(lf.get('nome_interno_meta'))}\n")
    parts.append(f"- **Idioma:** {block(lf.get('idioma'))}\n")
    parts.append(f"- **Estratégia volume/intenção:** {block(lf.get('estrategia_volume_intencao'))}\n")
    parts.append(f"- **Headline:** {block(lf.get('headline'))}\n")
    parts.append(f"- **Benefício imediato:** {block(lf.get('beneficio_imediato'))}\n")
    parts.append(f"- **Coerência com anúncio:** {block(lf.get('coerencia_anuncio'))}\n")

    pad = lf.get("campos_padrao") or []
    parts.append("**Campos padrão:** " + (", ".join(str(x) for x in pad) if pad else "_[preencher]_") + "\n")

    parts.append("### Campos custom\n")
    for row in lf.get("campos_custom") or []:
        if isinstance(row, dict):
            parts.append(
                f"- {block(row.get('campo'))} | obrig: {row.get('obrigatorio', '')} | "
                f"MQL: {block(row.get('criterio_mql'))}\n"
            )
    if not lf.get("campos_custom"):
        parts.append("- _[nenhum ou preencher no JSON]_\n")

    parts.append("### Perguntas de qualificação\n")
    for row in lf.get("perguntas_qualificacao") or []:
        if isinstance(row, dict):
            parts.append(
                f"- {block(row.get('pergunta'))} ({block(row.get('tipo_resposta'))}) → {block(row.get('criterio_mql'))}\n"
            )
    if not lf.get("perguntas_qualificacao"):
        parts.append("- _[preencher]_\n")

    parts.append(f"- **Privacidade (resumo):** {block(lf.get('privacidade_resumo'))}\n")
    parts.append(f"- **Thank you:** {block(lf.get('thank_you_texto'))}\n")
    parts.append(f"- **CTA pós-submit:** {block(lf.get('cta_pos_submit'))}\n")

    parts.append("## Origem e rastreio\n")
    cids = orig.get("campaign_ids") or []
    parts.append(
        "**campaign_id(s):** "
        + (", ".join(str(x) for x in cids) if cids else "_[preencher]_")
        + "\n"
    )
    parts.append(f"- **IDs no CRM:** {block(orig.get('como_ids_chegam_crm'))}\n")
    parts.append(f"- **UTMs:** {block(orig.get('utms_resumo'))}\n")
    crm_f = orig.get("campos_crm_obrigatorios") or []
    parts.append(
        "**Campos CRM obrigatórios:** "
        + (", ".join(str(x) for x in crm_f) if crm_f else "_[preencher]_")
        + "\n"
    )

    parts.append("## Integração\n")
    parts.append(f"- **Modo:** {block(inte.get('modo'))}\n")
    parts.append(f"- **Detalhe:** {block(inte.get('detalhe'))}\n")
    parts.append(f"- **Owner técnico:** {block(inte.get('owner_tecnico'))}\n")

    parts.append("## SLA\n")
    parts.append(f"- **Tempo máx. 1º contato:** {block(sla.get('tempo_max_primeiro_contato'))}\n")
    parts.append(f"- **Canal:** {block(sla.get('canal_primeiro_contato'))}\n")
    parts.append(f"- **Script comercial:** {block(sla.get('script_comercial_link'))}\n")
    parts.append(f"- **Owner comercial:** {block(sla.get('owner_comercial'))}\n")

    parts.append("## Públicos (form)\n")
    parts.append(f"- **Remarketing abriu não enviou:** {block(pub.get('remarketing_abriu_nao_enviou'))}\n")
    parts.append(f"- **Exclusões:** {block(pub.get('exclusoes'))}\n")

    parts.append("## Teste ponta a ponta\n")
    parts.append(f"- Data: {block(tst.get('data'))}\n")
    for k, label in (
        ("lead_teste_enviado", "Lead teste enviado"),
        ("crm_ok", "CRM OK"),
        ("backup_ok", "Backup OK"),
        ("origem_ids_ok", "Origem/IDs OK"),
    ):
        parts.append(f"- {_bool_check(tst, k)} {label}\n")

    parts.append("## Matriz de testes\n")
    parts.append(f"- **Varia:** {block(mt.get('o_que_varia'))}\n")
    parts.append(f"- **Constante:** {block(mt.get('o_que_constante'))}\n")

    parts.append("## Pré go-live — lead nativo\n")
    for k, label in (
        ("campos_perguntas_conferidos_mql", "Campos/perguntas conferidos (MQL)"),
        ("integracao_testada_lead_real", "Integração testada (lead real)"),
        ("sla_comunicado_time", "SLA comunicado ao time"),
        ("remarketing_form_aberto_definido", "Remarketing form aberto (se aplicável)"),
        ("qualidade_comercial_planilha_ok", "Qualidade comercial na planilha (não só CPL)"),
    ):
        parts.append(f"- {_bool_check(pg, k)} {label}\n")

    parts.append("\n## Gaps N2\n")
    parts.append(block(d.get("n2_gaps")) + "\n")
    return "\n".join(parts)


def _qualificacao_presente(lf: dict[str, Any]) -> bool:
    pers = lf.get("perguntas_qualificacao") or []
    customs = lf.get("campos_custom") or []
    if pers and any(isinstance(p, dict) and nonempty_str(p.get("pergunta")) for p in pers):
        return True
    if customs and any(isinstance(c, dict) and nonempty_str(c.get("criterio_mql")) for c in customs):
        return True
    return False


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not nonempty_str(m.get("cliente")):
        issues.append("meta.cliente vazio")

    pr = d.get("pre_requisitos") or {}
    for key, lab in (
        ("crm_sla_definido", "pre_requisitos.crm_sla_definido"),
        ("planilha_backup_ativa", "pre_requisitos.planilha_backup_ativa"),
        ("sla_followup_aceito_antes_ativar", "pre_requisitos.sla_followup_aceito_antes_ativar"),
    ):
        if not pr.get(key):
            issues.append(f"{lab}: obrigatório para lead nativo (playbook 15/16)")

    lf = d.get("lead_form") or {}
    if not nonempty_str(lf.get("nome_interno_meta")):
        issues.append("lead_form.nome_interno_meta vazio")
    if not _qualificacao_presente(lf):
        issues.append(
            "lead_form: incluir perguntas_qualificacao ou campos_custom com criterio_mql "
            "(evitar 'sem perguntas mínimas' — canônico seção 16)"
        )

    inte = d.get("integracao") or {}
    if not nonempty_str(inte.get("modo")):
        issues.append("integracao.modo vazio")

    sla = d.get("sla") or {}
    if not nonempty_str(sla.get("tempo_max_primeiro_contato")):
        issues.append("sla.tempo_max_primeiro_contato vazio (SLA incompleto)")

    tst = d.get("teste_p2p") or {}
    for key, lab in (
        ("crm_ok", "teste_p2p.crm_ok"),
        ("backup_ok", "teste_p2p.backup_ok"),
    ):
        if not tst.get(key):
            issues.append(f"{lab}: lead teste deve passar no CRM e backup para N2")

    mt = d.get("matriz_testes") or {}
    if not nonempty_str(mt.get("o_que_varia")) or not nonempty_str(mt.get("o_que_constante")):
        issues.append("matriz_testes: preencher o_que_varia e o_que_constante")

    pg = d.get("pre_go_live_lead_nativo") or {}
    critical = (
        "campos_perguntas_conferidos_mql",
        "integracao_testada_lead_real",
        "qualidade_comercial_planilha_ok",
    )
    for k in critical:
        if not pg.get(k):
            issues.append(f"pre_go_live_lead_nativo.{k} precisa true para N2 mínimo (subtipo nativo)")

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
            print("Lacunas (lead nativo / playbook 15):")
            for i in iss:
                print(f"  - {i}")
        else:
            print("Auditoria: pré-requisitos, qualificação, integração, SLA, teste e pré go-live críticos OK.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
