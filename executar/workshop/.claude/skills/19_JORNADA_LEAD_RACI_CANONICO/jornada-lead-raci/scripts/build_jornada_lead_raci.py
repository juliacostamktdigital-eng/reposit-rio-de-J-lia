#!/usr/bin/env python3
"""Jornada do lead + RACI (playbook 19) — Markdown consolidado e auditoria DoD."""

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
        x = v.strip()
        if not x or x.lower().startswith("_[preencher]"):
            return False
        if x == "[Nome]" or "yyyy" in x.lower():
            return False
        return True
    if isinstance(v, list):
        return any(filled(i) for i in v)
    return bool(v)


def fmt_ci(val: Any) -> str:
    if isinstance(val, list):
        xs = [str(x).strip() for x in val if str(x).strip()]
        return "; ".join(xs) if xs else ""
    return str(val or "").strip()


def default_etapas() -> list[dict[str, Any]]:
    return [
        {
            "etapa_funil": "",
            "touchpoints": [],
            "responsible": "",
            "accountable": "",
            "consulted": [],
            "informed": [],
            "evidencia_minima": "",
            "notas_sla_handoff": "",
        }
        for _ in range(3)
    ]


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "projeto": "[Nome]",
            "versao_artefato": "v1",
            "data": "YYYY-MM-DD",
            "responsavel_artefato": "",
            "link_funil_unificado_a2": "",
            "link_protocolo_a4": "",
        },
        "publicacao": {
            "onde_colado_funil": "",
            "onde_colado_protocolo": "",
        },
        "etapas": default_etapas(),
        "validacao_capacidade_sla": {
            "resumo": "",
        },
        "gerenciado_notas": {
            "kpi_dono": "",
            "kpi_sla": "",
            "kpi_evidencia": "",
            "cadencia_revisao": "mensal ou ao mudar estrutura do time",
        },
    }


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    pub = d.get("publicacao") or {}
    val = d.get("validacao_capacidade_sla") or {}
    ger = d.get("gerenciado_notas") or {}

    parts: list[str] = []
    parts.append("# Jornada do lead + RACI — consolidado\n\n")
    parts.append("## Cabeçalho\n\n")
    parts.append(
        f"- **Projeto:** {block(m.get('projeto'))}\n"
        f"- **Versão:** {block(m.get('versao_artefato'))}\n"
        f"- **Data:** {block(m.get('data'))}\n"
        f"- **Responsável:** {block(m.get('responsavel_artefato'))}\n"
        f"- **Funil A-2:** {block(m.get('link_funil_unificado_a2'))}\n"
        f"- **Protocolo A-4:** {block(m.get('link_protocolo_a4'))}\n"
    )
    parts.append(
        f"\n**Publicação:** funil → {block(pub.get('onde_colado_funil'))} · "
        f"protocolo → {block(pub.get('onde_colado_protocolo'))}\n\n"
    )

    parts.append("## Etapas (touchpoints + RACI)\n\n")
    for i, et in enumerate(d.get("etapas") or [], 1):
        if not isinstance(et, dict):
            continue
        tps = et.get("touchpoints") or []
        if isinstance(tps, list):
            tp_txt = ", ".join(str(x) for x in tps if str(x).strip()) or "_[preencher]_"
        else:
            tp_txt = block(tps)
        parts.append(f"### {i}. {block(et.get('etapa_funil'))}\n\n")
        parts.append(f"- **Touchpoints:** {tp_txt}\n")
        parts.append(f"- **R:** {block(et.get('responsible'))}\n")
        parts.append(f"- **A:** {block(et.get('accountable'))}\n")
        parts.append(f"- **C:** {block(fmt_ci(et.get('consulted')))}\n")
        parts.append(f"- **I:** {block(fmt_ci(et.get('informed')))}\n")
        parts.append(f"- **Evidência mínima:** {block(et.get('evidencia_minima'))}\n")
        parts.append(
            f"- **SLA / handoff:** {block(et.get('notas_sla_handoff'))}\n\n"
        )

    parts.append("## Validação capacidade × SLA (passo 4)\n\n")
    parts.append(f"{block(val.get('resumo'))}\n\n")

    parts.append("## Gerenciado (notas)\n\n")
    parts.append(
        f"- **KPI dono:** {block(ger.get('kpi_dono'))}\n"
        f"- **KPI SLA:** {block(ger.get('kpi_sla'))}\n"
        f"- **KPI evidência:** {block(ger.get('kpi_evidencia'))}\n"
        f"- **Cadência:** {block(ger.get('cadencia_revisao'))}\n"
    )
    return "".join(parts)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not filled(m.get("projeto")):
        issues.append("meta.projeto")
    if not filled(m.get("responsavel_artefato")):
        issues.append("meta.responsavel_artefato")
    if not filled(m.get("link_funil_unificado_a2")):
        issues.append("meta.link_funil_unificado_a2")
    if not filled(m.get("link_protocolo_a4")):
        issues.append("meta.link_protocolo_a4")

    etapas = [e for e in (d.get("etapas") or []) if isinstance(e, dict)]
    real = [e for e in etapas if filled(e.get("etapa_funil"))]
    if len(real) < 2:
        issues.append("etapas: ≥2 etapas com etapa_funil (mapar jornada mínima)")

    for i, e in enumerate(real, 1):
        pr = f"etapas[{i}]"
        for k in ("responsible", "accountable", "evidencia_minima"):
            if not filled(e.get(k)):
                issues.append(f"{pr}.{k}")

    v = d.get("validacao_capacidade_sla") or {}
    if not filled(v.get("resumo")):
        issues.append("validacao_capacidade_sla.resumo")

    if not filled((d.get("publicacao") or {}).get("onde_colado_funil")) and not filled(
        (d.get("publicacao") or {}).get("onde_colado_protocolo")
    ):
        issues.append("(aviso) publicacao: documentar onde foi colado no funil e/ou protocolo")

    return issues


def main() -> None:
    p = argparse.ArgumentParser(description="Jornada lead + RACI (playbook 19)")
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

    doc = load(args.input_json)
    if args.audit:
        print("Lacunas / avisos (jornada + RACI / playbook 19):")
        for x in audit(doc):
            print(f"  - {x}")
        return

    out = render_md(doc)
    if args.md_path:
        args.md_path.write_text(out, encoding="utf-8")
        print(f"Escrito: {args.md_path}")
    else:
        print(out, end="")


if __name__ == "__main__":
    main()
