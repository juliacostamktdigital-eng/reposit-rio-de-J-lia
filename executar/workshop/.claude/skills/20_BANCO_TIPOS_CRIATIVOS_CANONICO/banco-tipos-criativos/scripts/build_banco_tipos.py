#!/usr/bin/env python3
"""Catálogo de tipos de criativo (playbook 20) — Markdown consolidado, resumo e auditoria DoD."""

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
        if not t or t == "[Nome]":
            return False
        return True
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return bool(v)


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "projeto": "[Nome]",
            "versao_catalogo": "v1.0",
            "dono_catalogo": "",
            "link_deoc": "",
            "link_plano_midia": "",
            "link_benchmark": "",
            "link_empacotamento_oferta": "",
            "cadencia_revisao": "Mensal por canal/segmento e após ciclos relevantes (playbook 20 § Gerenciado).",
            "notas_kpi": "",
        },
        "taxonomia": {
            "formatos_padrao": ["estatico", "video", "carrossel", "outro"],
            "temperaturas_padrao": ["frio", "morno", "quente"],
            "objetivos_funil_catalogados": [],
        },
        "tipos": [],
        "change_log_catalogo": [],
    }


def _tipo_started(t: dict[str, Any]) -> bool:
    keys = ("id", "nome", "hipotese", "promessa_central", "objetivo_funil")
    return any(filled(t.get(k)) for k in keys)


def _tipo_dod_completo(t: dict[str, Any], pr: str) -> list[str]:
    miss: list[str] = []
    for k in (
        "id",
        "nome",
        "formato",
        "temperatura",
        "objetivo_funil",
        "hipotese",
    ):
        if not filled(t.get(k)):
            miss.append(f"{pr}.{k}")
    if not filled(t.get("componentes_obrigatorios")):
        miss.append(f"{pr}.componentes_obrigatorios (lista não vazia)")
    vlist = t.get("variacoes") or []
    if not isinstance(vlist, list) or len(vlist) < 3:
        miss.append(f"{pr}.variacoes (mínimo A/B/C)")
    else:
        for i, v in enumerate(vlist[:3], 1):
            if not isinstance(v, dict) or not filled(v.get("descricao")):
                miss.append(f"{pr}.variacoes[{i}].descricao")
    if not filled(t.get("referencias_benchmark")):
        miss.append(f"{pr}.referencias_benchmark (mínimo 1)")
    if not filled(t.get("dod_checklist")):
        miss.append(f"{pr}.dod_checklist")
    return miss


def _tipos_prontos_count(tipos: list[Any]) -> int:
    n = 0
    for i, t in enumerate(tipos, 1):
        if not isinstance(t, dict):
            continue
        st = str(t.get("status", "")).strip().lower()
        if st == "arquivado":
            continue
        pr = f"tipos[{i}]"
        if not _tipo_started(t):
            continue
        if not _tipo_dod_completo(t, pr):
            continue
        n += 1
    return n


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not filled(m.get("projeto")):
        issues.append("meta.projeto")
    if not filled(m.get("dono_catalogo")):
        issues.append("meta.dono_catalogo")

    tax = d.get("taxonomia") or {}
    if not filled(tax.get("formatos_padrao")):
        issues.append("taxonomia.formatos_padrao")
    if not filled(tax.get("temperaturas_padrao")):
        issues.append("taxonomia.temperaturas_padrao")

    tipos = d.get("tipos") or []
    if not isinstance(tipos, list):
        issues.append("tipos deve ser lista")
        return issues

    prontos = _tipos_prontos_count(tipos)
    if prontos < 10:
        issues.append(
            f"(DoD playbook) tipos com template completo: {prontos}/10 mínimo — "
            "complete campos ou marque status arquivado para não contar rascunhos vazios"
        )

    for i, t in enumerate(tipos, 1):
        if not isinstance(t, dict):
            continue
        pr = f"tipos[{i}]"
        if not _tipo_started(t):
            continue
        issues.extend(_tipo_dod_completo(t, pr))

    clog = d.get("change_log_catalogo") or []
    if prontos >= 10:
        started = False
        if isinstance(clog, list):
            for e in clog:
                if isinstance(e, dict) and (
                    filled(e.get("resumo")) or filled(e.get("tipo_id"))
                ):
                    started = True
                    break
        if not started:
            issues.append(
                "(Gerenciado) change_log_catalogo vazio — registre baseline v1 ou mudanças por tipo"
            )

    return issues


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    tax = d.get("taxonomia") or {}
    parts: list[str] = []
    parts.append("# Catálogo — Banco de tipos de criativo (playbook 20)\n\n")
    parts.append(
        f"- **Projeto:** {block(m.get('projeto'))}\n"
        f"- **Versão catálogo:** {block(m.get('versao_catalogo'))}\n"
        f"- **Dono:** {block(m.get('dono_catalogo'))}\n"
        f"- **DEOC:** {block(m.get('link_deoc'))}\n"
        f"- **Plano mídia:** {block(m.get('link_plano_midia'))}\n"
        f"- **Benchmark:** {block(m.get('link_benchmark'))}\n"
        f"- **Empacotamento oferta:** {block(m.get('link_empacotamento_oferta'))}\n"
        f"- **Cadência:** {block(m.get('cadencia_revisao'))}\n"
        f"- **Notas KPI:** {block(m.get('notas_kpi'))}\n"
    )

    fp = tax.get("formatos_padrao") or []
    tp = tax.get("temperaturas_padrao") or []
    of = tax.get("objetivos_funil_catalogados") or []
    parts.append("\n## Taxonomia\n\n")
    parts.append(
        f"- **Formatos:** {', '.join(str(x) for x in fp) if fp else '_[preencher]_'}\n"
    )
    parts.append(
        f"- **Temperaturas:** {', '.join(str(x) for x in tp) if tp else '_[preencher]_'}\n"
    )
    parts.append(
        f"- **Objetivos funil catalogados:** {', '.join(str(x) for x in of) if of else '_[preencher]_'}\n"
    )

    parts.append("\n## Tipos\n\n")
    parts.append(
        "| ID | Nome | Formato | Temp. | Objetivo | Status | v |\n"
        "|---|---|---|---|---|---|---|\n"
    )
    for t in d.get("tipos") or []:
        if isinstance(t, dict):
            parts.append(
                f"| {block(t.get('id'))} | {block(t.get('nome'))} | {block(t.get('formato'))} | "
                f"{block(t.get('temperatura'))} | {block(t.get('objetivo_funil'))} | "
                f"{block(t.get('status'))} | {block(t.get('versao_tipo'))} |\n"
            )

    if not (d.get("tipos") or []):
        parts.append("\n_Nenhum tipo em tipos[] ainda._\n")

    parts.append("\n## Change log do catálogo\n\n")
    for e in d.get("change_log_catalogo") or []:
        if isinstance(e, dict) and (
            filled(e.get("data")) or filled(e.get("resumo")) or filled(e.get("tipo_id"))
        ):
            parts.append(
                f"- **{block(e.get('data'))}** · `{block(e.get('tipo_id'))}` — {block(e.get('resumo'))}\n"
                f"  - Motivo: {block(e.get('motivo'))} · Autor: {block(e.get('autor'))}\n"
            )

    if not any(
        isinstance(e, dict) and filled(e.get("resumo"))
        for e in (d.get("change_log_catalogo") or [])
    ):
        parts.append("\n_Nenhuma entrada de change log ainda._\n")

    parts.append(
        f"\n---\n\n**Tipos com DoD completo (heurística script):** {_tipos_prontos_count(d.get('tipos') or [])}\n"
    )
    return "".join(parts)


def summary(d: dict[str, Any]) -> None:
    tipos = d.get("tipos") if isinstance(d.get("tipos"), list) else []
    n = len([t for t in tipos if isinstance(t, dict)])
    prontos = _tipos_prontos_count(tipos)
    ativos = sum(
        1
        for t in tipos
        if isinstance(t, dict) and str(t.get("status", "")).lower() == "ativo"
    )
    print(f"Registros em tipos[]: {n}")
    print(f"Status=ativo: {ativos}")
    print(f"DoD completo (contagem): {prontos} (meta playbook: ≥10)")


def main() -> None:
    p = argparse.ArgumentParser(description="Banco de tipos criativos (playbook 20)")
    p.add_argument("input_json", nargs="?", type=Path)
    p.add_argument("--md", dest="md_path", type=Path)
    p.add_argument("--audit", action="store_true")
    p.add_argument("--summary", action="store_true")
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
        xs = audit(doc)
        print("Lacunas / DoD (banco de tipos):")
        for x in xs:
            print(f"  - {x}")
        return

    if args.summary:
        summary(doc)
        return

    if args.md_path:
        args.md_path.write_text(render_md(doc), encoding="utf-8")
        print(f"Escrito: {args.md_path}")
    else:
        print(render_md(doc), end="")


if __name__ == "__main__":
    main()
