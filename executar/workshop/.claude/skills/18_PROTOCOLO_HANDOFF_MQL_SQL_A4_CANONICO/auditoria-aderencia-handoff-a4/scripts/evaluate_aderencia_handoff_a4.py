#!/usr/bin/env python3
"""Auditoria de aderência ao Protocolo A-4 (playbook 18 passo 6 + DoD + Gerenciado)."""

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
        ("ad-01", "MQL/SQL no CRM vs definições do protocolo", "Passos 2 e 6; DoD"),
        ("ad-02", "Motivos padronizados em rejeições/desqualificações", "Passo 3"),
        ("ad-03", "Campos mínimos do handoff (aderência)", "Passo 3; DoD"),
        ("ad-04", "SLA 1º contato (amostra ou métrica)", "Passo 4"),
        ("ad-05", "Enforcement: redistribuição quando SLA estoura", "Passo 4"),
        ("ad-06", "Rotina semanal operacional + ata/card", "Passo 5; DoD"),
        ("ad-07", "KPIs medidos vs thresholds do protocolo", "Passo 5; Gerenciado"),
        ("ad-08", "% leads sem status dentro do aceitável", "Gerenciado"),
        ("ad-09", "Rejeições por motivo utilizáveis (loop de ajuste)", "Componentes críticos"),
        ("ad-10", "Change log / atas de ajustes Mkt–Vendas", "DoD; Gerenciado"),
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


def default_indicadores() -> list[dict[str, Any]]:
    return [
        {"nome": "Taxa MQL → SQL", "valor_periodo": "", "threshold_protocolo": "", "nota": ""},
        {"nome": "Taxa SQL → venda", "valor_periodo": "", "threshold_protocolo": "", "nota": ""},
        {"nome": "Tempo 1º contato", "valor_periodo": "", "threshold_protocolo": "", "nota": ""},
        {"nome": "% rejeições por motivo (top)", "valor_periodo": "", "threshold_protocolo": "", "nota": ""},
        {"nome": "% leads sem status válido", "valor_periodo": "", "threshold_protocolo": "", "nota": ""},
    ]


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "projeto": "[Nome]",
            "data_auditoria": "YYYY-MM-DD",
            "auditor": "",
            "parecer_humano": "",
        },
        "amostra": {
            "periodo": "",
            "descricao_metodo": "",
            "n_ordem_grandeza": "",
        },
        "referencias": {
            "link_protocolo_a4": "",
            "link_funil_a2": "",
            "link_crm_07": "",
        },
        "dimensoes": default_dimensoes(),
        "indicadores": default_indicadores(),
        "achados_criticos": "",
        "backlog": [
            {"acao": "", "prioridade": "", "dono": "", "prazo": ""},
        ],
        "proxima_auditoria": "",
    }


def consolidado(d: dict[str, Any]) -> tuple[str, list[str]]:
    notes: list[str] = []
    if str(d.get("achados_criticos") or "").strip():
        notes.append("Achados críticos preenchidos → consolidado vermelho por política.")
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
        return "incompleto", ["Preencha semáforo em todas as dimensões aplicáveis (ou n.a.)."]

    if "vermelho" in aplicaveis:
        notes.append("Pelo menos uma dimensão em vermelho.")
        return "vermelho", notes
    if "amarelo" in aplicaveis:
        notes.append("Pelo menos uma dimensão em amarelo.")
        return "amarelo", notes
    if not aplicaveis:
        return "incompleto", ["Nenhuma dimensão aplicável avaliada (todas n.a.?)."]
    return "verde", notes


def render_md(d: dict[str, Any], diag: str, extra: list[str]) -> str:
    m = d.get("meta") or {}
    am = d.get("amostra") or {}
    ref = d.get("referencias") or {}
    parts: list[str] = []
    parts.append("# Relatório — aderência Protocolo A-4 (playbook 18)\n\n")
    parts.append("## Identificação\n\n")
    parts.append(
        f"- **Projeto:** {block(m.get('projeto'))}\n"
        f"- **Data:** {block(m.get('data_auditoria'))}\n"
        f"- **Auditor:** {block(m.get('auditor'))}\n"
        f"- **Período:** {block(am.get('periodo'))}\n"
        f"- **Amostra:** {block(am.get('descricao_metodo'))} (N≈ {block(am.get('n_ordem_grandeza'))})\n"
    )
    parts.append(
        f"- **Protocolo A-4:** {block(ref.get('link_protocolo_a4'))}\n"
        f"- **Funil A-2:** {block(ref.get('link_funil_a2'))}\n"
        f"- **CRM/07:** {block(ref.get('link_crm_07'))}\n\n"
    )
    parts.append("## Dimensões\n\n")
    parts.append("| ID | Dimensão | Semáforo | Evidência | Gap |\n|---|---|---|---|---|\n")
    for dim in d.get("dimensoes") or []:
        if isinstance(dim, dict):
            parts.append(
                f"| {block(dim.get('id'))} | {block(dim.get('nome'))} | "
                f"{block(dim.get('semaforo'))} | {block(dim.get('evidencia'))} | {block(dim.get('gap'))} |\n"
            )
    parts.append("\n## Indicadores (§ Gerenciado)\n\n")
    parts.append("| Indicador | Valor | Threshold protocolo | Nota |\n|---|---|---|---|\n")
    for row in d.get("indicadores") or []:
        if isinstance(row, dict):
            parts.append(
                f"| {block(row.get('nome'))} | {block(row.get('valor_periodo'))} | "
                f"{block(row.get('threshold_protocolo'))} | {block(row.get('nota'))} |\n"
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
    parts.append(f"\n**Próxima auditoria:** {block(d.get('proxima_auditoria'))}\n")
    return "".join(parts)


def filled(v: Any) -> bool:
    if v is None:
        return False
    if isinstance(v, str):
        t = v.strip()
        if not t or t == "[Nome]" or "yyyy" in t.lower():
            return False
        return True
    return bool(v)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not filled(m.get("projeto")):
        issues.append("meta.projeto")
    if not filled(m.get("data_auditoria")):
        issues.append("meta.data_auditoria")
    if not filled(m.get("auditor")):
        issues.append("meta.auditor")
    am = d.get("amostra") or {}
    if not filled(am.get("periodo")):
        issues.append("amostra.periodo")
    ref = d.get("referencias") or {}
    if not filled(ref.get("link_protocolo_a4")):
        issues.append("referencias.link_protocolo_a4")
    for dim in d.get("dimensoes") or []:
        if isinstance(dim, dict) and norm_semaforo(dim.get("semaforo")) is None:
            issues.append(f"dimensão pendente: {dim.get('id')}")
    return issues


def main() -> None:
    p = argparse.ArgumentParser(description="Auditoria aderência A-4 (playbook 18)")
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

    d = load(args.input_json)
    diag, notes = consolidado(d)

    if args.audit:
        print("Lacunas (aderência A-4):")
        for x in audit(d):
            print(f"  - {x}")
        return

    if args.summary:
        print(f"Consolidado sugerido: {diag}")
        for n in notes:
            print(f"  {n}")

    body = render_md(d, diag, notes)
    if args.md_path:
        args.md_path.write_text(body, encoding="utf-8")
        print(f"Escrito: {args.md_path}")
    elif not args.summary and not args.audit:
        print(body, end="")


if __name__ == "__main__":
    main()
