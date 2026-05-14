#!/usr/bin/env python3
"""Auditoria de funil / fontes da verdade (playbook 17 § Gerenciado) — relatório e heurística de consolidado."""

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


def norm_semaforo(raw: Any) -> str | None:
    if raw is None:
        return None
    t = str(raw).strip().lower()
    if not t:
        return None
    if t in ("n.a.", "n/a", "na"):
        return "na"
    if t in ("verde", "v", "green"):
        return "verde"
    if t in ("amarelo", "a", "ambar", "yellow"):
        return "amarelo"
    if t in ("vermelho", "vm", "red"):
        return "vermelho"
    return None


def default_dimensoes() -> list[dict[str, Any]]:
    rows = [
        (
            "fvt-01",
            "Conciliação CRM × backup × plataforma",
            "§ Gerenciado — vermelho: discrepância entre fontes",
        ),
        (
            "fvt-02",
            "Uma fonte preferencial por etapa respeitada",
            "Componentes críticos; DoD",
        ),
        (
            "trk-01",
            "Eventos de tracking declarados existem e disparam",
            "Passo 5; saídas",
        ),
        (
            "crm-01",
            "Campos mínimos com adesão aceitável",
            "KPI % campos; amarelo: pouco dado confiável",
        ),
        (
            "gov-01",
            "Governança de dado (donos, treino, change log)",
            "§ Gerenciado; dono (lacuna)",
        ),
        (
            "ops-01",
            "Funil cabível vs capacidade operacional",
            "Passo 6; componentes críticos",
        ),
    ]
    return [
        {
            "id": rid,
            "nome": nome,
            "ref_playbook": ref,
            "semaforo": "",
            "evidencia": "",
            "gap": "",
        }
        for rid, nome, ref in rows
    ]


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "projeto": "[Nome]",
            "data_auditoria": "YYYY-MM-DD",
            "auditor": "",
            "cadencia_rodada": "quinzenal",
            "parecer_humano": "",
        },
        "referencia_funil": {
            "link_artefato": "",
            "versao": "v1",
        },
        "amostra": {
            "periodo": "",
            "metodo": "",
            "n_registros_ordem_grandeza": "",
        },
        "dimensoes": default_dimensoes(),
        "conciliacao_etapas": [
            {
                "etapa": "",
                "fonte_declarada": "",
                "observado_pratica": "",
                "semaforo": "",
                "nota": "",
            }
        ],
        "etapas_sem_dono": [
            {"etapa": "", "impacto": "", "nota": ""},
        ],
        "eventos_tracking": [
            {
                "evento": "",
                "declarado_funil": "",
                "observado": "",
                "semaforo": "",
                "nota": "",
            }
        ],
        "campos_minimos": [
            {"campo": "", "evidencia_adesao": "", "semaforo": "", "nota": ""},
        ],
        "kpis": [
            {
                "id": "kpi-status",
                "nome": "% leads com status válido",
                "valor": "",
                "meta_referencia": "",
                "semaforo": "",
            },
            {
                "id": "kpi-campos",
                "nome": "% campos mínimos preenchidos",
                "valor": "",
                "meta_referencia": "",
                "semaforo": "",
            },
            {
                "id": "kpi-ciclo",
                "nome": "Tempo de ciclo por etapa",
                "valor": "",
                "meta_referencia": "",
                "semaforo": "",
            },
        ],
        "backlog": [
            {"item": "", "prioridade": "", "dono_sugerido": "", "link": ""},
        ],
        "proxima_revisao": "",
    }


def _impacto_alto(rows: list[dict[str, Any]]) -> bool:
    for r in rows:
        if not isinstance(r, dict):
            continue
        imp = str(r.get("impacto", "")).strip().lower()
        et = str(r.get("etapa", "")).strip()
        if et and imp in ("alto", "high", "crítico", "critico", "p0"):
            return True
    return False


def _etapas_sem_dono_relevantes(rows: list[dict[str, Any]]) -> bool:
    for r in rows:
        if not isinstance(r, dict):
            continue
        if str(r.get("etapa", "")).strip():
            return True
    return False


def consolidado(d: dict[str, Any]) -> tuple[str, list[str]]:
    notes: list[str] = []
    pend = False
    aplicaveis: list[str] = []

    for dim in d.get("dimensoes") or []:
        if not isinstance(dim, dict):
            continue
        st = norm_semaforo(dim.get("semaforo"))
        if st is None:
            pend = True
        elif st == "na":
            continue
        else:
            aplicaveis.append(st)

    if pend:
        return "incompleto", ["Dimensão(is) sem semáforo (ok: verde/amarelo/vermelho/n.a.)."]

    if "vermelho" in aplicaveis:
        notes.append("Pelo menos uma dimensão obrigatória em vermelho.")
        return "vermelho", notes

    etapas = [e for e in (d.get("etapas_sem_dono") or []) if isinstance(e, dict)]
    if _impacto_alto(etapas):
        notes.append("Etapa(s) sem dono com impacto alto.")
        return "vermelho", notes

    if "amarelo" in aplicaveis:
        notes.append("Dimensão em amarelo.")
        return "amarelo", notes

    if _etapas_sem_dono_relevantes(etapas):
        notes.append("Há etapas sem dono registradas (revisar severidade).")
        return "amarelo", notes

    if not aplicaveis:
        return "incompleto", ["Nenhuma dimensão aplicável preenchida (todas n.a.?)."]

    return "verde", notes


def render_md(d: dict[str, Any], diag: str, extra: list[str]) -> str:
    m = d.get("meta") or {}
    ref = d.get("referencia_funil") or {}
    am = d.get("amostra") or {}
    parts: list[str] = []
    parts.append("# Relatório — auditoria funil / fontes da verdade (playbook 17)\n\n")
    parts.append("## Identificação\n\n")
    parts.append(
        f"- **Projeto:** {block(m.get('projeto'))}\n"
        f"- **Data:** {block(m.get('data_auditoria'))}\n"
        f"- **Auditor:** {block(m.get('auditor'))}\n"
        f"- **Cadência:** {block(m.get('cadencia_rodada'))}\n"
        f"- **Artefato A-2:** {block(ref.get('link_artefato'))} (versão {block(ref.get('versao'))})\n"
    )
    parts.append("\n## Amostra\n\n")
    parts.append(
        f"- **Período:** {block(am.get('periodo'))}\n"
        f"- **Método:** {block(am.get('metodo'))}\n"
        f"- **N (ordem de grandeza):** {block(am.get('n_registros_ordem_grandeza'))}\n"
    )
    parts.append("\n## Dimensões\n\n")
    parts.append("| ID | Dimensão | Semáforo | Evidência | Gap |\n|---|---|---|---|---|\n")
    for dim in d.get("dimensoes") or []:
        if isinstance(dim, dict):
            parts.append(
                f"| {block(dim.get('id'))} | {block(dim.get('nome'))} | "
                f"{block(dim.get('semaforo'))} | {block(dim.get('evidencia'))} | "
                f"{block(dim.get('gap'))} |\n"
            )
    parts.append("\n## Conciliação por etapa\n\n")
    for row in d.get("conciliacao_etapas") or []:
        if isinstance(row, dict) and any(row.get(k) for k in row):
            parts.append(
                f"- **{block(row.get('etapa'))}:** declarado {block(row.get('fonte_declarada'))} · "
                f"observado {block(row.get('observado_pratica'))} → **{block(row.get('semaforo'))}** — "
                f"{block(row.get('nota'))}\n"
            )
    parts.append("\n## Etapas sem dono\n\n")
    for row in d.get("etapas_sem_dono") or []:
        if isinstance(row, dict) and str(row.get("etapa", "")).strip():
            parts.append(
                f"- **{row.get('etapa')}** (impacto {block(row.get('impacto'))}): "
                f"{block(row.get('nota'))}\n"
            )
    parts.append("\n## Eventos de tracking\n\n")
    for row in d.get("eventos_tracking") or []:
        if isinstance(row, dict):
            parts.append(
                f"- **{block(row.get('evento'))}:** declarado {block(row.get('declarado_funil'))} · "
                f"observado {block(row.get('observado'))} → **{block(row.get('semaforo'))}**\n"
            )
    parts.append("\n## Campos mínimos\n\n")
    for row in d.get("campos_minimos") or []:
        if isinstance(row, dict):
            parts.append(
                f"- **{block(row.get('campo'))}:** {block(row.get('evidencia_adesao'))} "
                f"→ **{block(row.get('semaforo'))}** — {block(row.get('nota'))}\n"
            )
    parts.append("\n## KPIs (§ Gerenciado)\n\n")
    for k in d.get("kpis") or []:
        if isinstance(k, dict):
            parts.append(
                f"- **{block(k.get('nome'))}:** {block(k.get('valor'))} "
                f"(meta {block(k.get('meta_referencia'))}) → **{block(k.get('semaforo'))}**\n"
            )
    parts.append("\n## Backlog sugerido\n\n")
    for b in d.get("backlog") or []:
        if isinstance(b, dict) and str(b.get("item", "")).strip():
            parts.append(
                f"- **{block(b.get('prioridade'))}** — {b.get('item')} "
                f"(dono: {block(b.get('dono_sugerido'))}, link: {block(b.get('link'))})\n"
            )
    parts.append("\n## Consolidado automático (revisar)\n\n")
    parts.append(f"**{diag.upper()}**\n")
    for n in extra:
        parts.append(f"- {n}\n")
    ph = m.get("parecer_humano") or ""
    if str(ph).strip():
        parts.append("\n## Parecer humano\n\n" + str(ph).strip() + "\n")
    parts.append(f"\n**Próxima revisão sugerida:** {block(d.get('proxima_revisao'))}\n")
    return "".join(parts)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not str(m.get("projeto", "")).strip() or str(m.get("projeto", "")).strip() == "[Nome]":
        issues.append("meta.projeto")
    if not str(m.get("data_auditoria", "")).strip() or "yyyy" in str(m.get("data_auditoria", "")).lower():
        issues.append("meta.data_auditoria")
    if not str(m.get("auditor", "")).strip():
        issues.append("meta.auditor")
    am = d.get("amostra") or {}
    for k in ("periodo", "metodo"):
        if not str(am.get(k, "")).strip():
            issues.append(f"amostra.{k}")
    for dim in d.get("dimensoes") or []:
        if isinstance(dim, dict) and norm_semaforo(dim.get("semaforo")) is None:
            issues.append(f"dimensão pendente: {dim.get('id')}")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Auditoria funil / fontes da verdade (17)")
    parser.add_argument("input_json", nargs="?", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--write-default", dest="out_json", type=Path)
    args = parser.parse_args()

    if args.out_json:
        args.out_json.write_text(
            json.dumps(default_document(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Escrito: {args.out_json}")
        return

    if not args.input_json:
        parser.error("informe input_json ou --write-default")

    d = load(args.input_json)
    diag, notes = consolidado(d)

    if args.audit:
        xs = audit(d)
        print("Lacunas (auditoria funil):")
        for x in xs:
            print(f"  - {x}")
        return

    if args.summary:
        print(f"Consolidado sugerido: {diag}")
        for n in notes:
            print(f"  {n}")

    if args.md_path:
        args.md_path.write_text(render_md(d, diag, notes), encoding="utf-8")
        print(f"Escrito: {args.md_path}")
    elif not args.summary and not args.audit:
        print(render_md(d, diag, notes), end="")


if __name__ == "__main__":
    main()
