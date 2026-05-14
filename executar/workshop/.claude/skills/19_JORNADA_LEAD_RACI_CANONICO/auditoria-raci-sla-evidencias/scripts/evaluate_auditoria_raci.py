#!/usr/bin/env python3
"""Auditoria RACI / SLA / evidências (playbook 19 § Gerenciado)."""

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


def filled(v: Any) -> bool:
    if v is None:
        return False
    if isinstance(v, str):
        x = v.strip()
        if not x or x == "[Nome]" or "yyyy" in x.lower():
            return False
        return True
    return bool(v)


def default_dimensoes() -> list[dict[str, Any]]:
    rows = [
        (
            "ar-01",
            "Etapas com Accountable claro na operação",
            "KPI % etapas com dono",
        ),
        (
            "ar-02",
            "Handoffs com responsável assumido",
            "Vermelho: handoff sem responsável",
        ),
        (
            "ar-03",
            "Rotas sem dono / lead sumindo",
            "Vermelho",
        ),
        (
            "ar-04",
            "Evidência mínima gerada na prática",
            "Amarelo: dono sem evidência",
        ),
        (
            "ar-05",
            "SLA: violações e ação quando estoura",
            "Amarelo/verde",
        ),
        (
            "ar-06",
            "Change log RACI quando papel muda",
            "Registro obrigatório",
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
            "periodo": "",
            "parecer_humano": "",
        },
        "referencias": {
            "link_jornada_lead_raci": "",
            "link_funil_a2": "",
            "link_protocolo_a4": "",
            "link_crm_ou_relatorios": "",
        },
        "kpis_medidos": [
            {
                "id": "kpi-dono",
                "nome": "% etapas com dono (A claro)",
                "valor": "",
                "meta_ou_threshold": "",
                "nota": "",
            },
            {
                "id": "kpi-sla",
                "nome": "% violações de SLA",
                "valor": "",
                "meta_ou_threshold": "",
                "nota": "",
            },
            {
                "id": "kpi-evid",
                "nome": "% etapas sem evidência mínima",
                "valor": "",
                "meta_ou_threshold": "",
                "nota": "",
            },
        ],
        "dimensoes": default_dimensoes(),
        "achados_criticos": "",
        "backlog": [
            {"acao": "", "prioridade": "", "dono": "", "prazo": ""},
        ],
        "proxima_revisao": "",
    }


def consolidado(d: dict[str, Any]) -> tuple[str, list[str]]:
    notes: list[str] = []
    if str(d.get("achados_criticos") or "").strip():
        notes.append("Achados críticos → consolidado vermelho por política.")
        return "vermelho", notes

    aplicaveis: list[str] = []
    pend = False
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
        return "incompleto", ["Preencha semáforo em cada dimensão aplicável (ou n.a.)."]

    if "vermelho" in aplicaveis:
        notes.append("Dimensão em vermelho.")
        return "vermelho", notes
    if "amarelo" in aplicaveis:
        notes.append("Dimensão em amarelo.")
        return "amarelo", notes
    if not aplicaveis:
        return "incompleto", ["Nenhuma dimensão aplicável avaliada."]
    return "verde", notes


def render_md(d: dict[str, Any], diag: str, extra: list[str]) -> str:
    m = d.get("meta") or {}
    ref = d.get("referencias") or {}
    parts: list[str] = []
    parts.append("# Relatório — auditoria RACI / SLA / evidências (playbook 19)\n\n")
    parts.append("## Identificação\n\n")
    parts.append(
        f"- **Projeto:** {block(m.get('projeto'))}\n"
        f"- **Data:** {block(m.get('data_auditoria'))}\n"
        f"- **Auditor:** {block(m.get('auditor'))}\n"
        f"- **Período:** {block(m.get('periodo'))}\n"
    )
    parts.append(
        f"- **Jornada+RACI:** {block(ref.get('link_jornada_lead_raci'))}\n"
        f"- **Funil A-2:** {block(ref.get('link_funil_a2'))}\n"
        f"- **Protocolo A-4:** {block(ref.get('link_protocolo_a4'))}\n"
        f"- **CRM:** {block(ref.get('link_crm_ou_relatorios'))}\n\n"
    )

    parts.append("## KPIs (§ Gerenciado)\n\n")
    for k in d.get("kpis_medidos") or []:
        if isinstance(k, dict):
            parts.append(
                f"- **{block(k.get('nome'))}:** {block(k.get('valor'))} "
                f"(meta {block(k.get('meta_ou_threshold'))}) — {block(k.get('nota'))}\n"
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

    parts.append("\n## Achados críticos\n\n")
    ac = str(d.get("achados_criticos") or "").strip()
    parts.append("_(nenhum registrado)_\n\n" if not ac else ac + "\n\n")

    parts.append("## Backlog\n\n")
    for b in d.get("backlog") or []:
        if isinstance(b, dict) and str(b.get("acao", "")).strip():
            parts.append(
                f"- **{block(b.get('prioridade'))}** · {b.get('acao')} — "
                f"{block(b.get('dono'))} até {block(b.get('prazo'))}\n"
            )

    parts.append("\n## Consolidado sugerido\n\n")
    parts.append(f"**{diag.upper()}**\n")
    for n in extra:
        parts.append(f"- {n}\n")
    ph = m.get("parecer_humano") or ""
    if str(ph).strip():
        parts.append("\n## Parecer humano\n\n" + str(ph).strip() + "\n")
    parts.append(f"\n**Próxima revisão:** {block(d.get('proxima_revisao'))}\n")
    return "".join(parts)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not filled(m.get("projeto")):
        issues.append("meta.projeto")
    if not filled(m.get("data_auditoria")):
        issues.append("meta.data_auditoria")
    if not filled(m.get("auditor")):
        issues.append("meta.auditor")
    if not filled(m.get("periodo")):
        issues.append("meta.periodo")

    ref = d.get("referencias") or {}
    if not filled(ref.get("link_jornada_lead_raci")):
        issues.append("(aviso) referencias.link_jornada_lead_raci — recomendado ter artefato de referência")

    for dim in d.get("dimensoes") or []:
        if isinstance(dim, dict) and norm_semaforo(dim.get("semaforo")) is None:
            issues.append(f"dimensão pendente: {dim.get('id')}")

    return issues


def main() -> None:
    p = argparse.ArgumentParser(description="Auditoria RACI/SLA playbook 19")
    p.add_argument("input_json", nargs="?", type=Path)
    p.add_argument("--md", dest="md_path", type=Path)
    p.add_argument("--summary", action="store_true")
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

    doc = load(args.input_json)
    diag, notes = consolidado(doc)

    if args.audit:
        print("Lacunas / avisos (auditoria RACI):")
        for x in audit(doc):
            print(f"  - {x}")
        return

    if args.summary:
        print(f"Consolidado sugerido: {diag}")
        for n in notes:
            print(f"  {n}")

    body = render_md(doc, diag, notes)
    if args.md_path:
        args.md_path.write_text(body, encoding="utf-8")
        print(f"Escrito: {args.md_path}")
    elif not args.summary and not args.audit:
        print(body, end="")


if __name__ == "__main__":
    main()
