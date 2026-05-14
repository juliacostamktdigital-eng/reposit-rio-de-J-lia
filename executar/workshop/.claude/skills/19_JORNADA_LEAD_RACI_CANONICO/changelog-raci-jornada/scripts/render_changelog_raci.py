#!/usr/bin/env python3
"""Change log do RACI da jornada do lead (playbook 19 § Gerenciado) — Markdown e auditoria."""

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
        if not t or t.lower() == "yyyy-mm-dd":
            return False
        if t.startswith("_[preencher]"):
            return False
        if t == "[Nome]":
            return False
        return True
    return bool(v)


def default_entry() -> dict[str, Any]:
    return {
        "id": "",
        "data": "",
        "autor": "",
        "dimensao": "",
        "etapa_funil": "",
        "papel_afetado": "",
        "resumo": "",
        "antes": "",
        "depois": "",
        "motivo": "",
        "impacto_esperado": "",
        "impacto_observado": "",
        "data_revisao_impacto": "",
        "versao_raci_apos": "",
        "comunicacao_alvos": "",
        "comunicacao_status": "pendente",
        "aprovadores": "",
        "links": "",
        "estado": "rascunho",
    }


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "projeto": "[Nome]",
            "versao_raci_atual": "v1.0",
            "dono_changelog": "",
            "link_artefato_jornada_raci": "",
            "link_funil_unificado_a2": "",
            "link_protocolo_a4": "",
            "notas_cadencia": "Mensal ou ao mudar estrutura do time (playbook 19 § Gerenciado).",
        },
        "historico": [default_entry()],
    }


def _entry_started(e: dict[str, Any]) -> bool:
    keys = (
        "resumo",
        "antes",
        "depois",
        "motivo",
        "impacto_esperado",
        "dimensao",
        "id",
    )
    return any(filled(e.get(k)) for k in keys)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not filled(m.get("projeto")):
        issues.append("meta.projeto")
    if not filled(m.get("dono_changelog")):
        issues.append("meta.dono_changelog")
    if not filled(m.get("link_artefato_jornada_raci")):
        issues.append("meta.link_artefato_jornada_raci")

    for i, e in enumerate(d.get("historico") or [], 1):
        if not isinstance(e, dict):
            continue
        if not _entry_started(e):
            continue
        pr = f"historico[{i}]"
        for k in (
            "data",
            "autor",
            "dimensao",
            "resumo",
            "antes",
            "depois",
            "motivo",
            "impacto_esperado",
        ):
            if not filled(e.get(k)):
                issues.append(f"{pr}.{k}")
        st = str(e.get("estado", "")).strip().lower()
        if st == "publicado":
            if not filled(e.get("comunicacao_alvos")):
                issues.append(f"(aviso) {pr}.comunicacao_alvos vazio — recomendado para mudança publicada")
            if not filled(e.get("versao_raci_apos")):
                issues.append(f"(aviso) {pr}.versao_raci_apos vazio — alinhar com jornada-lead-raci")
        if st == "publicado" and not filled(e.get("impacto_observado")):
            issues.append(f"(aviso) {pr}: impacto_observado vazio — preencher na revisão de dados")
        if st == "revisao_pendente" and not filled(e.get("data_revisao_impacto")):
            issues.append(f"{pr}.data_revisao_impacto (sugerido quando estado=revisao_pendente)")
    return issues


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    parts: list[str] = []
    parts.append("# Change log — RACI / jornada do lead (playbook 19)\n\n")
    parts.append(
        f"- **Projeto:** {block(m.get('projeto'))}\n"
        f"- **Versão RACI/jornada (registro):** {block(m.get('versao_raci_atual'))}\n"
        f"- **Dono do log:** {block(m.get('dono_changelog'))}\n"
        f"- **Artefato jornada+RACI:** {block(m.get('link_artefato_jornada_raci'))}\n"
        f"- **Funil A-2:** {block(m.get('link_funil_unificado_a2'))}\n"
        f"- **Protocolo A-4:** {block(m.get('link_protocolo_a4'))}\n"
        f"- **Cadência:** {block(m.get('notas_cadencia'))}\n"
    )
    parts.append("\n---\n\n## Histórico\n\n")

    hist = [e for e in (d.get("historico") or []) if isinstance(e, dict)]
    hist_sorted = sorted(hist, key=lambda x: str(x.get("data") or ""), reverse=True)

    for e in hist_sorted:
        if not _entry_started(e):
            continue
        parts.append(f"### {block(e.get('id'))} · {block(e.get('data'))}\n\n")
        parts.append(
            f"- **Estado:** {block(e.get('estado'))}\n"
            f"- **Autor:** {block(e.get('autor'))}\n"
            f"- **Dimensão:** {block(e.get('dimensao'))}\n"
            f"- **Etapa funil:** {block(e.get('etapa_funil'))}\n"
            f"- **Papel afetado:** {block(e.get('papel_afetado'))}\n"
            f"- **Resumo:** {block(e.get('resumo'))}\n"
        )
        parts.append(f"\n**Antes:** {block(e.get('antes'))}\n\n**Depois:** {block(e.get('depois'))}\n\n")
        parts.append(f"**Motivo:** {block(e.get('motivo'))}\n\n")
        parts.append(
            f"**Impacto esperado:** {block(e.get('impacto_esperado'))}\n\n"
            f"**Impacto observado:** {block(e.get('impacto_observado'))}\n\n"
            f"**Data revisão impacto:** {block(e.get('data_revisao_impacto'))}\n\n"
        )
        parts.append(
            f"**Versão RACI após:** {block(e.get('versao_raci_apos'))}\n"
            f"**Comunicação — alvos:** {block(e.get('comunicacao_alvos'))}\n"
            f"**Comunicação — status:** {block(e.get('comunicacao_status'))}\n"
            f"**Aprovadores:** {block(e.get('aprovadores'))}\n"
            f"**Links:** {block(e.get('links'))}\n\n---\n\n"
        )

    if not any(_entry_started(e) for e in hist):
        parts.append("_Nenhuma entrada preenchida ainda._\n")

    return "".join(parts)


def main() -> None:
    p = argparse.ArgumentParser(description="Change log RACI jornada (playbook 19)")
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
        xs = audit(d)
        print("Lacunas (changelog RACI):")
        for x in xs:
            print(f"  - {x}")
        return

    if args.md_path:
        args.md_path.write_text(render_md(d), encoding="utf-8")
        print(f"Escrito: {args.md_path}")
    else:
        print(render_md(d), end="")


if __name__ == "__main__":
    main()
