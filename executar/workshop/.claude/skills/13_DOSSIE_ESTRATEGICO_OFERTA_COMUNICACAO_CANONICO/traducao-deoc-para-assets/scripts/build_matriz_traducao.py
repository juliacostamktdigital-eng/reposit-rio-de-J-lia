#!/usr/bin/env python3
"""Gera Markdown da matriz DEOC -> assets (playbook 13.5.9) e audita campos obrigatorios.

Inclui:
- Matriz deterministica com tracking_event PascalCase como coluna obrigatoria.
- Variacoes de oferta por canal (email, LP, call, LinkedIn, WhatsApp).
- Message-match audit (KlientBoost: inconsistencia ad<->LP e #1 driver de bounce).

Backwards-compatible: arquivos antigos (sem matriz_deterministica /
variacoes_por_canal / message_match_audit) ainda renderizam e auditam — o
script apenas sinaliza esses blocos como ausentes em --audit.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


CANAIS_ESPERADOS = ("Email", "LP", "Call de Vendas", "LinkedIn", "WhatsApp")
PASCAL_CASE_RE = re.compile(r"^[A-Z][A-Za-z0-9]*$")
MESSAGE_MATCH_CHECKS = ("headline_match", "promessa_match", "cta_match", "tracking_match")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def block(text: str) -> str:
    s = (text or "").strip()
    return s if s else "_[preencher]_"


def bullets(items: list[Any]) -> str:
    if not items:
        return "- _[preencher]_"
    return "\n".join(f"- {it}".strip() for it in items)


def table_docs(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "| Documento | Owner | Dependência | Prazo |\n|---|---|---|---|\n| | | | |"
    lines = ["| Documento | Owner | Dependência | Prazo |", "|---|---|---|---|"]
    for r in rows:
        if not isinstance(r, dict):
            continue
        lines.append(
            f"| {block(r.get('documento'))} | {block(r.get('owner'))} | "
            f"{block(r.get('dependencia'))} | {block(r.get('prazo_alvo'))} |"
        )
    return "\n".join(lines)


def table_changelog(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "| Versão | Data | Mudança |\n|---|---|---|\n| | | |"
    lines = ["| Versão | Data | Mudança |", "|---|---|---|"]
    for r in rows:
        if not isinstance(r, dict):
            continue
        lines.append(
            f"| {block(r.get('versao'))} | {block(r.get('data'))} | {block(r.get('mudanca'))} |"
        )
    return "\n".join(lines)


def table_matriz_deterministica(rows: list[dict[str, str]]) -> str:
    header = (
        "| Elemento | Tipo | Headline Ad | Headline LP | Subheadline LP | "
        "CTA | Sales pitch step | Tracking Event |"
    )
    sep = "|---|---|---|---|---|---|---|---|"
    if not rows:
        return f"{header}\n{sep}\n| | | | | | | | |"
    lines = [header, sep]
    for r in rows:
        if not isinstance(r, dict):
            continue
        lines.append(
            f"| {block(r.get('elemento'))} | {block(r.get('tipo'))} | "
            f"{block(r.get('headline_ad'))} | {block(r.get('headline_lp'))} | "
            f"{block(r.get('subheadline_lp'))} | {block(r.get('cta'))} | "
            f"{block(r.get('sales_pitch_step'))} | {block(r.get('tracking_event'))} |"
        )
    return "\n".join(lines)


def table_variacoes_canal(rows: list[dict[str, str]]) -> str:
    header = "| Canal | Ângulo de copy | Headline adaptado |"
    sep = "|---|---|---|"
    if not rows:
        return f"{header}\n{sep}\n" + "\n".join(f"| {c} | _[preencher]_ | _[preencher]_ |" for c in CANAIS_ESPERADOS)
    lines = [header, sep]
    for r in rows:
        if not isinstance(r, dict):
            continue
        lines.append(
            f"| {block(r.get('canal'))} | {block(r.get('angulo_copy'))} | "
            f"{block(r.get('headline_adaptado'))} |"
        )
    return "\n".join(lines)


def table_message_match(audit_obj: dict[str, Any]) -> str:
    header = "| Check | Status |"
    sep = "|---|---|"
    rotulo = {
        "headline_match": "Headline match (ad ↔ hero LP)",
        "promessa_match": "Promessa match (ad ↔ LP ↔ vendas)",
        "cta_match": "CTA match (ad ↔ CTA primário LP)",
        "tracking_match": "Tracking match (event reflete promessa)",
    }
    lines = [header, sep]
    for k in MESSAGE_MATCH_CHECKS:
        v = audit_obj.get(k)
        if v is True:
            status = "✅"
        elif v is False:
            status = "❌"
        else:
            status = "_[preencher]_"
        lines.append(f"| {rotulo[k]} | {status} |")
    notas = (audit_obj.get("notas") or "").strip()
    out = "\n".join(lines)
    if notas:
        out += f"\n\n**Notas:** {notas}"
    return out


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    mr = d.get("matriz_resumo") or {}
    md_rows = d.get("matriz_deterministica") or []
    var_canal = d.get("variacoes_por_canal") or []
    mm_audit = d.get("message_match_audit") or {}
    pm = d.get("plano_midia") or {}
    bc = d.get("briefing_criativo") or {}
    lp = d.get("lp") or {}
    ca = d.get("copy_anuncios") or {}
    vd = d.get("vendas") or {}
    tr = d.get("tracking") or {}
    prox = d.get("proximos_documentos") or []
    clog = d.get("changelog_matriz") or []

    parts: list[str] = []
    parts.append("# Matriz de tradução DEOC → execução\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente / produto | {block(m.get('cliente_ou_produto'))} |\n"
        f"| Versão desta matriz | {block(m.get('versao_matriz'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Responsável | {block(m.get('responsavel'))} |\n"
        f"| Versão / link do DEOC | {block(m.get('versao_link_deoc'))} |\n"
    )

    parts.append("## 1. Matriz resumo (5.9)\n")
    parts.append("| Saída | O que recebe do DEOC |\n|---|---|")
    parts.append(f"| Plano de mídia | {block(mr.get('plano_midia'))} |")
    parts.append(f"| Briefing criativo | {block(mr.get('briefing_criativo'))} |")
    parts.append(f"| LP | {block(mr.get('lp'))} |")
    parts.append(f"| Copy de anúncios | {block(mr.get('copy_anuncios'))} |")
    parts.append(f"| Vendas | {block(mr.get('vendas'))} |")
    parts.append(f"| Tracking | {block(mr.get('tracking'))} |\n")

    parts.append("## 1A. Matriz determinística (tracking event obrigatório)\n")
    parts.append(
        "Cada elemento estratégico (POV / Differentiator / Proof Point / Oferta) "
        "vira uma linha. `Tracking Event` em PascalCase.\n"
    )
    parts.append(table_matriz_deterministica([dict(x) for x in md_rows if isinstance(x, dict)]) + "\n")

    parts.append("## 1B. Variações de oferta por canal\n")
    parts.append(
        "Mesma promessa, mesma prova, mesmo ICP. Muda só o ângulo de leitura por canal.\n"
    )
    parts.append(table_variacoes_canal([dict(x) for x in var_canal if isinstance(x, dict)]) + "\n")

    parts.append("## 1C. Message-match audit\n")
    parts.append(
        "Inconsistência ad↔LP é o #1 driver de bounce em mídia paga (KlientBoost). "
        "Linha com check ❌ volta pra ajuste antes de declarar pronto.\n"
    )
    parts.append(table_message_match(mm_audit) + "\n")

    parts.append("## 2. Plano de mídia\n")
    parts.append(f"**Beachhead:** {block(pm.get('beachhead'))}\n")
    parts.append(f"**Canais prováveis:** {block(pm.get('canais_provaveis'))}\n")
    parts.append("**Ângulos:**\n" + bullets(list(pm.get("angulos_mensagem") or [])) + "\n")
    parts.append(f"**Premissas:** {block(pm.get('premissas'))}\n")
    parts.append(f"**ICP / anti-ICP:** {block(pm.get('icp_anti_icp'))}\n")
    parts.append(f"**Oferta (ciclo):** {block(pm.get('oferta_comunicada_ciclo'))}\n")
    parts.append(f"**Critérios de lead correto:** {block(pm.get('criterios_lead_correto'))}\n")
    parts.append(f"**Notas teste/cohort:** {block(pm.get('notas_teste_cohort'))}\n")

    parts.append("## 3. Briefing criativo\n")
    for label, key in (
        ("Persona", "persona"),
        ("Hook", "hook"),
        ("Dor", "dor"),
        ("Mecanismo", "mecanismo"),
        ("Prova", "prova"),
        ("CTA", "cta"),
        ("Tom", "tom"),
        ("Tabus", "tabus"),
        ("Refs / inimigo", "referencias_visuais_ou_inimigo"),
    ):
        parts.append(f"**{label}:** {block(bc.get(key))}\n")

    parts.append("## 4. LP\n")
    for label, key in (
        ("Narrativa", "narrativa"),
        ("Seções", "secoes_planejadas"),
        ("Promessa", "promessa"),
        ("Provas por seção", "provas_por_secao"),
        ("Objeções", "objecoes"),
        ("Formulário", "formulario_campos"),
        ("Escopo / limites", "escopo_limites"),
        ("CTA primário/secundário", "cta_primario_secundario"),
    ):
        parts.append(f"**{label}:** {block(lp.get(key))}\n")

    parts.append("## 5. Copy de anúncios\n")
    parts.append("**Hooks:**\n" + bullets(list(ca.get("hooks") or [])) + "\n")
    parts.append("**Headlines:**\n" + bullets(list(ca.get("headlines") or [])) + "\n")
    parts.append("**CTAs:**\n" + bullets(list(ca.get("ctas") or [])) + "\n")
    parts.append(f"**Variações:** {block(ca.get('variacoes_por_segmento'))}\n")
    parts.append(f"**Claims (ref. DEOC seção 5.8):** {block(ca.get('claims_referencia_deoc'))}\n")
    parts.append(f"**Formatos/canais:** {block(ca.get('formatos_canais_alvo'))}\n")

    parts.append("## 6. Vendas\n")
    parts.append(f"**Promessa vista pelo lead:** {block(vd.get('promessa_vista_pelo_lead'))}\n")
    parts.append(f"**Objeções / respostas:** {block(vd.get('objecoes_respostas'))}\n")
    parts.append(f"**Anti-ICP:** {block(vd.get('anti_icp'))}\n")
    parts.append("**Perguntas de qualificação:**\n" + bullets(list(vd.get("perguntas_qualificacao") or [])) + "\n")
    parts.append(f"**Limites da oferta:** {block(vd.get('limites_oferta'))}\n")
    parts.append(f"**Handoff / materiais:** {block(vd.get('handoff_materiais'))}\n")

    parts.append("## 7. Tracking\n")
    parts.append("### Dimensões UTM / creative ID (5.9)\n")
    parts.append("| Dimensão | Valor |\n|---|---|")
    for label, key in (
        ("persona", "utm_persona"),
        ("hook", "utm_hook"),
        ("dor", "utm_dor"),
        ("ângulo", "utm_angulo"),
        ("etapa", "utm_etapa"),
    ):
        parts.append(f"| {label} | {block(tr.get(key))} |")
    parts.append("")
    parts.append(f"**Eventos / conversões:** {block(tr.get('eventos_conversoes'))}\n")
    parts.append(f"**North Star / KPI:** {block(tr.get('north_star_ou_kpi'))}\n")
    parts.append(f"**Link taxonomia:** {block(tr.get('link_taxonomia_projeto'))}\n")

    parts.append("## 8. Próximos documentos\n")
    parts.append(table_docs([dict(x) for x in prox if isinstance(x, dict)]) + "\n")

    parts.append("## 9. Changelog\n")
    parts.append(table_changelog([dict(x) for x in clog if isinstance(x, dict)]) + "\n")

    return "\n".join(parts)


def nonempty_str(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def nonempty_list(v: Any, min_n: int = 1) -> bool:
    if not isinstance(v, list) or len(v) < min_n:
        return False
    for x in v:
        if isinstance(x, str) and x.strip():
            return True
        if x:
            return True
    return False


def is_pascal_case(v: Any) -> bool:
    return isinstance(v, str) and bool(PASCAL_CASE_RE.match(v.strip()))


def audit_matriz_deterministica(rows: list[Any]) -> list[str]:
    """Warning se elemento sem tracking_event ou tracking_event nao-PascalCase."""
    issues: list[str] = []
    if not isinstance(rows, list) or not rows:
        issues.append(
            "matriz_deterministica ausente ou vazia: cada elemento estratégico "
            "(POV/Differentiator/Proof Point/Oferta) deve virar uma linha"
        )
        return issues
    for i, r in enumerate(rows):
        if not isinstance(r, dict):
            issues.append(f"matriz_deterministica[{i}]: linha não é objeto")
            continue
        elem = (r.get("elemento") or "").strip() or f"linha {i}"
        # campos textuais obrigatorios da linha
        for k in ("headline_ad", "headline_lp", "cta", "sales_pitch_step"):
            if not nonempty_str(r.get(k)):
                issues.append(f"matriz_deterministica[{elem}].{k} vazio")
        # tracking_event obrigatorio + PascalCase
        te = r.get("tracking_event")
        if not nonempty_str(te):
            issues.append(
                f"matriz_deterministica[{elem}].tracking_event vazio "
                "(coluna obrigatória — sem ele não dá pra otimizar por ângulo nem atribuir pós-iOS 14.5)"
            )
        elif not is_pascal_case(te):
            issues.append(
                f"matriz_deterministica[{elem}].tracking_event '{te}' não está em PascalCase "
                "(ex.: 'ViewBeloRooftop', 'LeadAlmocoExecutivo')"
            )
    return issues


def audit_variacoes_canal(rows: list[Any]) -> list[str]:
    issues: list[str] = []
    if not isinstance(rows, list) or not rows:
        issues.append(
            "variacoes_por_canal ausente ou vazia: esperado um item para cada canal "
            f"({', '.join(CANAIS_ESPERADOS)})"
        )
        return issues
    canais_vistos: set[str] = set()
    for i, r in enumerate(rows):
        if not isinstance(r, dict):
            issues.append(f"variacoes_por_canal[{i}]: linha não é objeto")
            continue
        canal = (r.get("canal") or "").strip() or f"linha {i}"
        canais_vistos.add(canal)
        for k in ("angulo_copy", "headline_adaptado"):
            if not nonempty_str(r.get(k)):
                issues.append(f"variacoes_por_canal[{canal}].{k} vazio")
    faltantes = [c for c in CANAIS_ESPERADOS if c not in canais_vistos]
    if faltantes:
        issues.append(
            f"variacoes_por_canal: canais ausentes — {', '.join(faltantes)} "
            "(mesmo núcleo de oferta, ângulo adaptado por canal)"
        )
    return issues


def audit_message_match(obj: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if not isinstance(obj, dict) or not obj:
        issues.append(
            "message_match_audit ausente: rode os 4 checks (headline/promessa/CTA/tracking) "
            "antes de declarar tradução pronta — KlientBoost: inconsistência ad↔LP é #1 driver de bounce"
        )
        return issues
    for k in MESSAGE_MATCH_CHECKS:
        v = obj.get(k)
        if v is None:
            issues.append(f"message_match_audit.{k} não respondido (preencher true/false)")
        elif v is False:
            issues.append(
                f"message_match_audit.{k} = false — corrigir inconsistência antes de publicar "
                "(linha da matriz determinística volta pra ajuste)"
            )
    return issues


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    mr = d.get("matriz_resumo") or {}
    for k in ("plano_midia", "briefing_criativo", "lp", "copy_anuncios", "vendas", "tracking"):
        if not nonempty_str(mr.get(k)):
            issues.append(f"matriz_resumo.{k} vazio (resumo da linha 5.9)")

    pm = d.get("plano_midia") or {}
    for k in (
        "beachhead",
        "canais_provaveis",
        "premissas",
        "icp_anti_icp",
        "oferta_comunicada_ciclo",
        "criterios_lead_correto",
    ):
        if not nonempty_str(pm.get(k)):
            issues.append(f"plano_midia.{k} vazio")
    if not nonempty_list(pm.get("angulos_mensagem"), 1):
        issues.append("plano_midia.angulos_mensagem: pelo menos um item")

    bc = d.get("briefing_criativo") or {}
    for k in ("persona", "hook", "dor", "mecanismo", "prova", "cta"):
        if not nonempty_str(bc.get(k)):
            issues.append(f"briefing_criativo.{k} vazio")
    if not nonempty_str(bc.get("tom")):
        issues.append("briefing_criativo.tom vazio (preencher ou explicitar N/A)")
    if not nonempty_str(bc.get("tabus")):
        issues.append("briefing_criativo.tabus vazio (preencher ou explicitar Nenhum)")

    lp = d.get("lp") or {}
    for k in (
        "narrativa",
        "secoes_planejadas",
        "promessa",
        "provas_por_secao",
        "objecoes",
        "formulario_campos",
        "escopo_limites",
        "cta_primario_secundario",
    ):
        if not nonempty_str(lp.get(k)):
            issues.append(f"lp.{k} vazio")

    ca = d.get("copy_anuncios") or {}
    for k in ("hooks", "headlines", "ctas"):
        if not nonempty_list(ca.get(k), 1):
            issues.append(f"copy_anuncios.{k}: pelo menos uma linha")
    for k in ("variacoes_por_segmento", "claims_referencia_deoc", "formatos_canais_alvo"):
        if not nonempty_str(ca.get(k)):
            issues.append(f"copy_anuncios.{k} vazio")

    vd = d.get("vendas") or {}
    for k in (
        "promessa_vista_pelo_lead",
        "objecoes_respostas",
        "anti_icp",
        "limites_oferta",
        "handoff_materiais",
    ):
        if not nonempty_str(vd.get(k)):
            issues.append(f"vendas.{k} vazio")
    if not nonempty_list(vd.get("perguntas_qualificacao"), 1):
        issues.append("vendas.perguntas_qualificacao: pelo menos uma pergunta")

    tr = d.get("tracking") or {}
    for k in (
        "utm_persona",
        "utm_hook",
        "utm_dor",
        "utm_angulo",
        "utm_etapa",
        "eventos_conversoes",
    ):
        if not nonempty_str(tr.get(k)):
            issues.append(f"tracking.{k} vazio")

    # Novos blocos (matriz determinística + variações canal + message-match)
    issues.extend(audit_matriz_deterministica(d.get("matriz_deterministica") or []))
    issues.extend(audit_variacoes_canal(d.get("variacoes_por_canal") or []))
    issues.extend(audit_message_match(d.get("message_match_audit") or {}))

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Build matriz traducao DEOC Markdown; audit 5.9.")
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
            print("Lacunas (traducao 5.9 / playbook 13):")
            for line in issues:
                print(f"  - {line}")
        else:
            print("Auditoria: nenhuma lacuna obrigatoria detectada neste schema.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
