#!/usr/bin/env python3
"""Gera Markdown de especificação Conversão no site (Meta) a partir de JSON e audita requisitos críticos (playbook 15)."""

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


def _bool_check(d: dict[str, Any], key: str) -> str:
    return "[x]" if d.get(key) else "[ ]"


def _render_linhas(rows: Any, keys: tuple[str, ...]) -> str:
    if not rows or not isinstance(rows, list):
        return "_[preencher no JSON: lista de objetos]_\n"
    out: list[str] = []
    for r in rows:
        if not isinstance(r, dict):
            continue
        cells = [block(r.get(k)) for k in keys]
        out.append("| " + " | ".join(cells) + " |\n")
    return "".join(out) if out else "_[preencher]_\n"


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    esc = d.get("escopo_conversao") or {}
    pr = d.get("pre_requisitos") or {}
    urls = d.get("urls") or {}
    pc = d.get("pixel_capi") or {}
    ev = d.get("evento_otimizacao") or {}
    pub = d.get("publicos") or {}
    camps = d.get("campanhas_resumo") or {}
    mt = d.get("matriz_testes") or {}
    tst = d.get("teste_p2p") or {}
    pg = d.get("pre_go_live_conversao") or {}

    parts: list[str] = []
    parts.append("# Meta Ads — Conversão no site — consolidado\n")
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

    parts.append("## Escopo (Seção 9)\n")
    parts.append(f"- **Tipo conversão:** {block(esc.get('tipo_conversao'))}\n")
    parts.append(f"- **Evento (interface Meta):** {block(esc.get('evento_meta_interface'))}\n")
    parts.append(f"- **Evento funil (fonte da verdade):** {block(esc.get('evento_funil_fonte_verdade'))}\n")
    parts.append(f"- **Volume / hipótese:** {block(esc.get('volume_hipotese_resumo'))}\n")
    parts.append(f"- **Profundidade vs volume:** {block(esc.get('justificativa_profundidade_volume'))}\n")

    parts.append("## Pré-requisitos\n")
    for k, label in (
        ("lp_qa_ok", "LP QA"),
        ("evento_disparo_testado", "Evento disparado em teste"),
        ("pixel_eventos_conferidos", "Pixel/eventos conferidos"),
        ("capi_quando_aplicavel", "CAPI quando aplicável"),
        ("dominio_verificado_quando_necessario", "Domínio verificado (se necessário)"),
        ("utms_taxonomia_ok", "UTMs / taxonomia"),
    ):
        parts.append(f"- {_bool_check(pr, k)} {label}\n")

    parts.append("## URLs\n")
    parts.append(f"- **LP final:** {block(urls.get('lp_final'))}\n")
    parts.append(f"- **Thank you:** {block(urls.get('thank_you'))}\n")
    parts.append(f"- **Intermediária:** {block(urls.get('intermediaria'))}\n")
    parts.append(f"- **UTMs (resumo):** {block(urls.get('utm_parametros_resumo'))}\n")

    parts.append("## Pixel / CAPI\n")
    parts.append(f"- **Pixel ID:** {block(pc.get('pixel_id'))}\n")
    parts.append(f"- **Eventos priorizados:** {block(pc.get('eventos_priorizados_resumo'))}\n")
    parts.append(f"- **CAPI:** {block(pc.get('capi_resumo'))}\n")
    parts.append(f"- **Dedup / notas:** {block(pc.get('dedup_notas'))}\n")

    sup = ev.get("eventos_suporte") or []
    parts.append(
        "**Eventos suporte:** "
        + (", ".join(str(x) for x in sup) if sup else "_[opcional]_")
        + "\n"
    )
    parts.append(f"- **Otimização (registro):** {block(ev.get('nome_otimizacao'))}\n")

    parts.append("## Públicos\n")
    parts.append("| Audiência | Temperatura | Uso |\n|---|---|---|")
    parts.append(_render_linhas(pub.get("linhas"), ("audience", "temperatura", "uso")))
    parts.append(f"**Exclusões:** {block(pub.get('exclusoes'))}\n")
    parts.append(f"**Remarketing visitantes:** {block(pub.get('remarketing_visitantes_resumo'))}\n")

    parts.append("## Campanhas (resumo)\n")
    parts.append("| campaign_id | Objetivo Meta | Notas |\n|---|---|---|")
    parts.append(_render_linhas(camps.get("linhas"), ("campaign_id", "objetivo_meta", "notas")))

    parts.append("## Matriz de testes\n")
    parts.append(f"- **Varia:** {block(mt.get('o_que_varia'))}\n")
    parts.append(f"- **Constante:** {block(mt.get('o_que_constante'))}\n")

    parts.append("## Teste ponta a ponta\n")
    parts.append(f"- Data: {block(tst.get('data'))}\n")
    for k, label in (
        ("disparo_meta_ok", "Disparo visto na Meta"),
        ("backup_ok", "Backup (se lead LP)"),
        ("crm_ok", "CRM (se lead LP)"),
        ("utms_origem_ok", "UTMs / origem"),
    ):
        parts.append(f"- {_bool_check(tst, k)} {label}\n")

    parts.append("## Pré go-live — conversão site\n")
    for k, label in (
        ("evento_validado_nao_apenas_nome", "Evento validado (não só nome em campanha)"),
        ("pixel_testado_checklist_global", "Pixel testado (checklist global)"),
        ("exclusoes_convertidos_ok", "Exclusões convertidos"),
        ("orcamento_aprendizado_ok", "Orçamento / aprendizado"),
        ("changelog_evento_url", "Changelog evento/URL"),
    ):
        parts.append(f"- {_bool_check(pg, k)} {label}\n")

    parts.append("\n## Gaps N2\n")
    parts.append(block(d.get("n2_gaps")) + "\n")
    return "\n".join(parts)


def _lead_lp(tipo: str) -> bool:
    t = (tipo or "").lower()
    return "lead" in t or "form" in t or "mql" in t


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not nonempty_str(m.get("cliente")):
        issues.append("meta.cliente vazio")

    esc = d.get("escopo_conversao") or {}
    for key, lab in (
        ("evento_meta_interface", "escopo_conversao.evento_meta_interface"),
        ("evento_funil_fonte_verdade", "escopo_conversao.evento_funil_fonte_verdade"),
        ("justificativa_profundidade_volume", "escopo_conversao.justificativa_profundidade_volume"),
    ):
        if not nonempty_str(esc.get(key)):
            issues.append(f"{lab} vazio (Seção 5 e 9)")

    pr = d.get("pre_requisitos") or {}
    for key, lab in (
        ("lp_qa_ok", "pre_requisitos.lp_qa_ok"),
        ("evento_disparo_testado", "pre_requisitos.evento_disparo_testado"),
        ("pixel_eventos_conferidos", "pre_requisitos.pixel_eventos_conferidos"),
    ):
        if not pr.get(key):
            issues.append(f"{lab}: obrigatório (Seções 4, 9 e 16)")

    urls = d.get("urls") or {}
    if not nonempty_str(urls.get("lp_final")):
        issues.append("urls.lp_final vazio")

    pc = d.get("pixel_capi") or {}
    if not nonempty_str(pc.get("pixel_id")):
        issues.append("pixel_capi.pixel_id vazio")

    mt = d.get("matriz_testes") or {}
    if not nonempty_str(mt.get("o_que_varia")) or not nonempty_str(mt.get("o_que_constante")):
        issues.append("matriz_testes: preencher o_que_varia e o_que_constante")

    tst = d.get("teste_p2p") or {}
    if not tst.get("disparo_meta_ok"):
        issues.append("teste_p2p.disparo_meta_ok: prova de evento (Seção 13/16)")

    tipo = str(esc.get("tipo_conversao") or "")
    if _lead_lp(tipo):
        for key, lab in (("backup_ok", "teste_p2p.backup_ok"), ("crm_ok", "teste_p2p.crm_ok")):
            if not tst.get(key):
                issues.append(f"{lab}: exigido quando conversão é lead na LP (N2 geral)")

    pg = d.get("pre_go_live_conversao") or {}
    for key, lab in (
        ("evento_validado_nao_apenas_nome", "pre_go_live_conversao.evento_validado_nao_apenas_nome"),
        ("pixel_testado_checklist_global", "pre_go_live_conversao.pixel_testado_checklist_global"),
    ):
        if not pg.get(key):
            issues.append(f"{lab} precisa true para N2 mínimo (subtipo conversão)")

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
            print("Lacunas (conversão site / playbook 15):")
            for i in iss:
                print(f"  - {i}")
        else:
            print("Auditoria: evento, LP, pixel, teste e pré go-live críticos OK.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
