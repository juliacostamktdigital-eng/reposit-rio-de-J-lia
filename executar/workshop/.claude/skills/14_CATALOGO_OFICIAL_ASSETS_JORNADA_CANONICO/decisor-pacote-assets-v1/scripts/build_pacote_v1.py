#!/usr/bin/env python3
"""Gera Markdown do pacote de assets v1 e audita os quatro entregaveis do playbook 14 secao 6."""

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


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    ctx = d.get("contexto") or {}
    pv = d.get("pacote_v1") or []
    fc = d.get("fora_do_ciclo") or []
    dep = d.get("dependencias_cliente") or []
    n2 = d.get("criterios_n2_por_componente") or []
    log = d.get("changelog") or []

    parts: list[str] = []
    parts.append("# Pacote de assets — ciclo v1\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente / projeto | {block(m.get('cliente_projeto'))} |\n"
        f"| Versão do pacote | {block(m.get('versao_pacote'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Responsável | {block(m.get('responsavel_decisor'))} |\n"
        f"| Aprovação cliente | {block(m.get('aprovacao_cliente'))} |\n"
    )

    parts.append("## 1. Contexto da decisão\n")
    parts.append(f"**Objetivo v1:** {block(ctx.get('objetivo_ciclo_v1'))}\n")
    parts.append("**Canais previstos:**\n")
    for c in ctx.get("canais_previstos") or []:
        parts.append(f"- {c}")
    if not ctx.get("canais_previstos"):
        parts.append("- _[preencher]_")
    parts.append("")
    parts.append(f"**Prazo macro:** {block(ctx.get('prazo_macro'))}\n")
    parts.append(f"**Orçamento (ordem de grandeza):** {block(ctx.get('orcamento_ordem_grandeza'))}\n")
    parts.append(f"**Maturidade / diagnóstico:** {block(ctx.get('maturidade_e_diagnostico_ref'))}\n")
    parts.append(f"**Riscos:** {block(ctx.get('riscos_restricoes'))}\n")
    parts.append(f"**Filtro catálogo:** {block(ctx.get('link_filtro_catalogo'))}\n")

    parts.append("## 2. Lista curta — assets v1\n")
    parts.append(
        "| # | Asset | P | Owner | Depende de | N2 (resumo) | Notas |\n"
        "|---|-------|---|-------|------------|-------------|-------|"
    )
    for i, row in enumerate(pv, 1):
        if not isinstance(row, dict):
            continue
        depends = row.get("depende_de_ids") or []
        ds = ", ".join(str(x) for x in depends) if depends else ""
        parts.append(
            f"| {i} | {block(row.get('asset'))} | {block(row.get('prioridade'))} | "
            f"{block(row.get('owner'))} | {block(ds)} | {block(row.get('criterio_n2_resumido'))} | "
            f"{block(row.get('notas'))} |"
        )
    if not pv:
        parts.append("| 1 | | | | | | |")
    parts.append("")

    parts.append("## 3. Fora do ciclo\n")
    parts.append("| Asset ou pedido | Motivo | Reavaliar |\n|---|---|---|")
    for row in fc:
        if isinstance(row, dict):
            parts.append(
                f"| {block(row.get('asset_ou_pedido'))} | {block(row.get('motivo_exclusao'))} | "
                f"{block(row.get('reavaliar_quando'))} |"
            )
    if not fc:
        parts.append("| | | |")
    parts.append("")

    parts.append("## 4. Dependências do cliente\n")
    if m.get("sem_dependencias_criticas_declarado"):
        parts.append(
            f"**Declaração:** sem dependências críticas identificadas. "
            f"{block(m.get('sem_dependencias_nota'))}\n"
        )
    parts.append(
        "| ID | Dependência | Tipo | Bloqueia | Owner cliente | SLA |\n|---|---|---|---|---|---|"
    )
    for row in dep:
        if isinstance(row, dict):
            parts.append(
                f"| {block(row.get('id'))} | {block(row.get('descricao'))} | {block(row.get('tipo'))} | "
                f"{block(row.get('bloqueia'))} | {block(row.get('owner_cliente'))} | "
                f"{block(row.get('sla_ou_data'))} |"
            )
    if not dep and not m.get("sem_dependencias_criticas_declarado"):
        parts.append("| | | | | | |")
    parts.append("")

    parts.append("## 5. Critérios N2 por componente\n")
    parts.append("| Componente | N2 mínimo | Evidência |\n|---|---|---|")
    for row in n2:
        if isinstance(row, dict):
            parts.append(
                f"| {block(row.get('componente'))} | {block(row.get('n2_minimo'))} | "
                f"{block(row.get('evidencia_esperada'))} |"
            )
    if not n2:
        parts.append("| | | |")
    parts.append("")

    parts.append("## 6. Changelog\n")
    parts.append("| Versão | Data | Mudança |\n|---|---|---|")
    for row in log:
        if isinstance(row, dict):
            parts.append(
                f"| {block(row.get('versao'))} | {block(row.get('data'))} | {block(row.get('mudanca'))} |"
            )
    if not log:
        parts.append("| | | |")
    parts.append("")

    return "\n".join(parts)


def nonempty_str(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    ctx = d.get("contexto") or {}
    if not nonempty_str(ctx.get("objetivo_ciclo_v1")):
        issues.append("contexto.objetivo_ciclo_v1 vazio")
    cp = ctx.get("canais_previstos") or []
    if not isinstance(cp, list) or not cp or not all(isinstance(x, str) and nonempty_str(x) for x in cp):
        issues.append("contexto.canais_previstos: pelo menos um canal")

    pv = [x for x in (d.get("pacote_v1") or []) if isinstance(x, dict)]
    good_pv = [
        x
        for x in pv
        if nonempty_str(x.get("asset"))
        and nonempty_str(x.get("owner"))
        and nonempty_str(x.get("criterio_n2_resumido"))
    ]
    if len(good_pv) < 2:
        issues.append("pacote_v1: pelo menos 2 linhas com asset, owner e criterio_n2_resumido")
    for x in pv:
        if nonempty_str(x.get("asset")) and not nonempty_str(x.get("prioridade")):
            issues.append("pacote: prioridade vazia em linha com asset")

    fc = [x for x in (d.get("fora_do_ciclo") or []) if isinstance(x, dict)]
    good_fc = [
        x
        for x in fc
        if nonempty_str(x.get("asset_ou_pedido")) and nonempty_str(x.get("motivo_exclusao"))
    ]
    if not good_fc:
        issues.append("fora_do_ciclo: pelo menos uma linha com pedido e motivo")

    m = d.get("meta") or {}
    dep = [x for x in (d.get("dependencias_cliente") or []) if isinstance(x, dict)]
    good_dep = [
        x
        for x in dep
        if nonempty_str(x.get("descricao")) and nonempty_str(x.get("bloqueia"))
    ]
    if m.get("sem_dependencias_criticas_declarado"):
        if not nonempty_str(m.get("sem_dependencias_nota")):
            issues.append("meta: sem_dependencias_nota vazio quando declarado sem dependencias")
    else:
        if not good_dep:
            issues.append("dependencias_cliente: pelo menos uma linha ou marcar sem_dependencias_criticas_declarado")

    n2rows = [x for x in (d.get("criterios_n2_por_componente") or []) if isinstance(x, dict)]
    good_n2 = [
        x
        for x in n2rows
        if nonempty_str(x.get("componente"))
        and nonempty_str(x.get("n2_minimo"))
        and nonempty_str(x.get("evidencia_esperada"))
    ]
    if len(good_n2) < 2:
        issues.append("criterios_n2_por_componente: pelo menos 2 linhas completas")

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
            print("Lacunas (playbook 14 secao 6):")
            for i in iss:
                print(f"  - {i}")
        else:
            print("Auditoria: quatro entregaveis minimamente preenchidos.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
