#!/usr/bin/env python3
"""Consolidado do Protocolo A-4 (playbook 18) a partir de JSON + auditoria DoD."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def block(t: Any) -> str:
    s = "" if t is None else str(t).strip()
    return s if s else "_[preencher]_"


def filled(v: Any) -> bool:
    if v is None:
        return False
    if isinstance(v, str):
        t = v.strip()
        if not t or t.lower().startswith("_[preencher]"):
            return False
        if t.lower() in ("[nome]", "yyyy-mm-dd"):
            return False
        return True
    if isinstance(v, bool):
        return True
    return bool(v)


def default_kpis() -> list[dict[str, Any]]:
    specs = [
        ("Taxa MQL → SQL", "Leads SQL / MQL no período (definir janela)"),
        ("Taxa SQL → venda", "Vendas ou oportunidades ganhas / SQL"),
        ("Tempo até 1º contato", "Média ou mediana após handoff/MQL"),
        ("% rejeições por motivo", "Distribuição por código de motivo"),
        ("% leads sem status válido", "Leads em branco ou status inválido / total"),
    ]
    return [
        {
            "nome": nome,
            "descricao_calculo": desc,
            "threshold_verde": "",
            "threshold_amarelo": "",
            "threshold_vermelho": "",
            "acao_se_vermelho": "",
        }
        for nome, desc in specs
    ]


def default_motivos() -> list[dict[str, Any]]:
    return [
        {"codigo": "R01", "label": "", "quando_usar": ""},
        {"codigo": "R02", "label": "", "quando_usar": ""},
        {"codigo": "R03", "label": "", "quando_usar": ""},
    ]


def default_campos() -> list[dict[str, Any]]:
    return [
        {"campo": "", "obrigatorio": True, "regra_preenchimento": ""},
        {"campo": "", "obrigatorio": True, "regra_preenchimento": ""},
    ]


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "projeto": "[Nome]",
            "versao_protocolo": "v1",
            "data": "YYYY-MM-DD",
            "responsavel": "",
            "link_funil_unificado_a2": "",
            "link_plano_midia": "",
            "link_deoc": "",
            "link_crm_sla_07": "",
        },
        "concordancia": {
            "marketing_concorda": False,
            "vendas_concorda": False,
            "data_acordo": "",
        },
        "lead_correto": {
            "resumo_icp": "",
            "anti_icp_operacional": "",
        },
        "mql": {
            "condicao_entrada": "",
            "evidencia_minima": "",
            "criterio_passa": "",
            "criterio_nao_passa": "",
        },
        "sql": {
            "condicao_entrada": "",
            "evidencia_minima": "",
            "criterio_passa": "",
            "criterio_nao_passa": "",
        },
        "aceitacao_rejeicao": {
            "criterios_aceitacao_resumo": "",
            "motivos_rejeicao": default_motivos(),
        },
        "crm_campos": default_campos(),
        "sla": {
            "primeiro_contato_horas": "",
            "unidade_tempo": "horas úteis",
            "canal_preferencial": "",
            "responsavel_papel": "",
            "regra_redistribuicao": "",
            "regra_excecao": "",
        },
        "rotina": {
            "cadencia_operacional": "semanal",
            "cadencia_estrutural": "mensal",
            "registro_decisoes": "",
            "change_log_ajustes": "",
            "kpis": default_kpis(),
        },
        "evidencia_auditavel": {
            "rastro_obrigatorio": "",
            "exemplos_registro": "",
            "proxima_auditoria_aderencia": "",
        },
        "loop_ajuste": {
            "dono_ajuste_marketing": "",
            "notas": "",
        },
    }


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    conc = d.get("concordancia") or {}
    lc = d.get("lead_correto") or {}
    mq = d.get("mql") or {}
    sq = d.get("sql") or {}
    ar = d.get("aceitacao_rejeicao") or {}
    sla = d.get("sla") or {}
    rot = d.get("rotina") or {}
    ev = d.get("evidencia_auditavel") or {}
    la = d.get("loop_ajuste") or {}

    parts: list[str] = []
    parts.append("# Protocolo de handoff (A-4) — consolidado\n\n")
    parts.append("## Cabeçalho\n\n")
    parts.append(
        f"- **Projeto:** {block(m.get('projeto'))}\n"
        f"- **Versão:** {block(m.get('versao_protocolo'))}\n"
        f"- **Data:** {block(m.get('data'))}\n"
        f"- **Responsável:** {block(m.get('responsavel'))}\n"
        f"- **Funil A-2:** {block(m.get('link_funil_unificado_a2'))}\n"
        f"- **Plano mídia:** {block(m.get('link_plano_midia'))}\n"
        f"- **DEOC:** {block(m.get('link_deoc'))}\n"
        f"- **CRM/SLA (07):** {block(m.get('link_crm_sla_07'))}\n"
    )
    parts.append(
        f"\n**Concordância:** Mkt {conc.get('marketing_concorda')} · "
        f"Vendas {conc.get('vendas_concorda')} · Data {block(conc.get('data_acordo'))}\n\n"
    )
    parts.append("## 1. Lead correto\n\n")
    parts.append(f"{block(lc.get('resumo_icp'))}\n\n**Anti-ICP:** {block(lc.get('anti_icp_operacional'))}\n\n")
    parts.append("## 2. MQL\n\n")
    for k, lab in (
        ("condicao_entrada", "Condição de entrada"),
        ("evidencia_minima", "Evidência mínima"),
        ("criterio_passa", "Critério passa"),
        ("criterio_nao_passa", "Critério não passa"),
    ):
        parts.append(f"- **{lab}:** {block(mq.get(k))}\n")
    parts.append("\n## 3. SQL\n\n")
    for k, lab in (
        ("condicao_entrada", "Condição de entrada"),
        ("evidencia_minima", "Evidência mínima"),
        ("criterio_passa", "Critério passa"),
        ("criterio_nao_passa", "Critério não passa"),
    ):
        parts.append(f"- **{lab}:** {block(sq.get(k))}\n")
    parts.append("\n## 4. Aceitação / rejeição\n\n")
    parts.append(f"{block(ar.get('criterios_aceitacao_resumo'))}\n\n")
    for mot in ar.get("motivos_rejeicao") or []:
        if isinstance(mot, dict):
            parts.append(
                f"- **{block(mot.get('codigo'))}** {block(mot.get('label'))} — {block(mot.get('quando_usar'))}\n"
            )
    parts.append("\n## 5. Campos CRM\n\n")
    for c in d.get("crm_campos") or []:
        if isinstance(c, dict):
            ob = "sim" if c.get("obrigatorio") else "não"
            parts.append(
                f"- **{block(c.get('campo'))}** (obrig. {ob}): {block(c.get('regra_preenchimento'))}\n"
            )
    parts.append("\n## 6. SLA\n\n")
    parts.append(
        f"- **1º contato:** {block(sla.get('primeiro_contato_horas'))} {block(sla.get('unidade_tempo'))}\n"
        f"- **Canal:** {block(sla.get('canal_preferencial'))}\n"
        f"- **Responsável (papel):** {block(sla.get('responsavel_papel'))}\n"
        f"- **Redistribuição:** {block(sla.get('regra_redistribuicao'))}\n"
        f"- **Exceções:** {block(sla.get('regra_excecao'))}\n"
    )
    parts.append("\n## 7. Rotina e KPIs\n\n")
    parts.append(
        f"- **Cadência:** {block(rot.get('cadencia_operacional'))} (op.) · "
        f"{block(rot.get('cadencia_estrutural'))} (estrutural)\n"
        f"- **Registro decisões:** {block(rot.get('registro_decisoes'))}\n"
        f"- **Change log ajustes:** {block(rot.get('change_log_ajustes'))}\n\n"
    )
    for k in rot.get("kpis") or []:
        if isinstance(k, dict):
            parts.append(f"### {block(k.get('nome'))}\n\n")
            parts.append(f"- Cálculo: {block(k.get('descricao_calculo'))}\n")
            parts.append(
                f"- V: {block(k.get('threshold_verde'))} · A: {block(k.get('threshold_amarelo'))} · "
                f"VM: {block(k.get('threshold_vermelho'))}\n"
            )
            parts.append(f"- **Ação se VM:** {block(k.get('acao_se_vermelho'))}\n\n")
    parts.append("## 8. Evidência e auditoria\n\n")
    parts.append(f"{block(ev.get('rastro_obrigatorio'))}\n\n**Exemplos:** {block(ev.get('exemplos_registro'))}\n\n")
    parts.append(f"**Próxima auditoria aderência:** {block(ev.get('proxima_auditoria_aderencia'))}\n\n")
    parts.append("## 9. Loop de ajuste (Marketing)\n\n")
    parts.append(
        f"**Dono:** {block(la.get('dono_ajuste_marketing'))}\n\n{block(la.get('notas'))}\n"
    )
    return "".join(parts)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not filled(m.get("projeto")):
        issues.append("meta.projeto")
    if not filled(m.get("link_funil_unificado_a2")):
        issues.append("meta.link_funil_unificado_a2")

    lc = d.get("lead_correto") or {}
    for k in ("resumo_icp", "anti_icp_operacional"):
        if not filled(lc.get(k)):
            issues.append(f"lead_correto.{k}")

    for stage in ("mql", "sql"):
        bl = d.get(stage) or {}
        for k in (
            "condicao_entrada",
            "evidencia_minima",
            "criterio_passa",
            "criterio_nao_passa",
        ):
            if not filled(bl.get(k)):
                issues.append(f"{stage}.{k}")

    ar = d.get("aceitacao_rejeicao") or {}
    if not filled(ar.get("criterios_aceitacao_resumo")):
        issues.append("aceitacao_rejeicao.criterios_aceitacao_resumo")
    mot_ok = 0
    for mot in ar.get("motivos_rejeicao") or []:
        if isinstance(mot, dict) and filled(mot.get("label")) and filled(mot.get("codigo")):
            mot_ok += 1
    if mot_ok < 2:
        issues.append("motivos_rejeicao: ≥2 motivos com codigo+label")

    cam_ok = 0
    for c in d.get("crm_campos") or []:
        if isinstance(c, dict) and filled(c.get("campo")) and filled(c.get("regra_preenchimento")):
            cam_ok += 1
    if cam_ok < 2:
        issues.append("crm_campos: ≥2 campos com regra")

    sla = d.get("sla") or {}
    for k in (
        "primeiro_contato_horas",
        "responsavel_papel",
        "regra_redistribuicao",
    ):
        if not filled(sla.get(k)):
            issues.append(f"sla.{k}")

    rot = d.get("rotina") or {}
    if not filled(rot.get("registro_decisoes")):
        issues.append("rotina.registro_decisoes")
    kpi_ok = 0
    for k in rot.get("kpis") or []:
        if not isinstance(k, dict):
            continue
        if filled(k.get("nome")) and filled(k.get("acao_se_vermelho")):
            if filled(k.get("threshold_vermelho")):
                kpi_ok += 1
    if kpi_ok < 2:
        issues.append("rotina.kpis: ≥2 KPIs com threshold_vermelho + acao_se_vermelho")

    ev = d.get("evidencia_auditavel") or {}
    if not filled(ev.get("rastro_obrigatorio")):
        issues.append("evidencia_auditavel.rastro_obrigatorio")

    conc = d.get("concordancia") or {}
    if not conc.get("marketing_concorda") or not conc.get("vendas_concorda"):
        issues.append("(aviso) concordancia: confirmar marketing + vendas após alinhamento")

    return issues


def main() -> None:
    p = argparse.ArgumentParser(description="Protocolo A-4 MQL/SQL (playbook 18)")
    p.add_argument("input_json", nargs="?", type=Path)
    p.add_argument("--md", dest="md_path", type=Path)
    p.add_argument("--audit", action="store_true")
    p.add_argument("--write-default", dest="out_json", type=Path)
    args = p.parse_args()

    if args.out_json:
        args.out_json.write_text(
            json.dumps(default_document(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Escrito: {args.out_json}")
        return

    if not args.input_json:
        p.error("informe input_json ou --write-default")

    d = load(args.input_json)
    if args.audit:
        print("Lacunas / avisos (protocolo A-4 / playbook 18):")
        for x in audit(d):
            print(f"  - {x}")
        return

    out = render_md(d)
    if args.md_path:
        args.md_path.write_text(out, encoding="utf-8")
        print(f"Escrito: {args.md_path}")
    else:
        print(out, end="")


if __name__ == "__main__":
    main()
