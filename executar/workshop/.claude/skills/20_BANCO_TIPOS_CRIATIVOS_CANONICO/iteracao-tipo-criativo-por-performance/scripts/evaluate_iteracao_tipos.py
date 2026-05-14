#!/usr/bin/env python3
"""Iteração de tipos criativos por performance (playbook 20 § Gerenciado) — MD, auditoria e resumo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


VEREDITOS = frozenset(
    {"manter", "alterar", "descontinuar", "pausar", "expandir", "inconclusivo"}
)


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
        if not t or t == "[Nome]" or t.lower() == "yyyy-mm-dd":
            return False
        return True
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return bool(v)


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "projeto": "[Nome]",
            "periodo_analise": "",
            "data_relatorio": "YYYY-MM-DD",
            "responsavel": "",
            "link_banco_tipos": "",
            "link_pack_origem": "",
            "fontes_dados": "",
            "notas_amostra": "",
        },
        "analise": [
            {
                "tipo_id": "",
                "nome_tipo_ref": "",
                "campanhas_creative_refs": "",
                "metrica_primaria": "",
                "valor_observado": "",
                "baseline_ou_esperado": "",
                "volume_notas": "",
                "veredito": "",
                "evidencia_resumida": "",
                "mudanca_proposta": "",
                "nova_hipotese": "",
                "novas_variacoes_sugeridas": [],
                "prioridade_proximo_pack": "",
            }
        ],
        "change_log_sugerido": [],
    }


def _row_started(r: dict[str, Any]) -> bool:
    keys = (
        "tipo_id",
        "veredito",
        "evidencia_resumida",
        "metrica_primaria",
        "mudanca_proposta",
    )
    return any(filled(r.get(k)) for k in keys)


def _norm_veredito(v: Any) -> str | None:
    if not filled(v):
        return None
    t = str(v).strip().lower()
    return t if t in VEREDITOS else "__invalid__"


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not filled(m.get("projeto")):
        issues.append("meta.projeto")
    if not filled(m.get("periodo_analise")):
        issues.append("meta.periodo_analise")
    if not filled(m.get("responsavel")):
        issues.append("meta.responsavel")
    if not filled(m.get("data_relatorio")):
        issues.append("meta.data_relatorio")
    if not filled(m.get("link_banco_tipos")):
        issues.append("(aviso) meta.link_banco_tipos — recomendado para encadeamento")
    if not filled(m.get("fontes_dados")):
        issues.append("(aviso) meta.fontes_dados vazio")

    rows = d.get("analise") or []
    if not isinstance(rows, list):
        issues.append("analise deve ser lista")
        return issues

    started = [r for r in rows if isinstance(r, dict) and _row_started(r)]
    if not started:
        issues.append("analise: nenhuma linha iniciada")

    needs_cl = False
    for i, r in enumerate(rows, 1):
        if not isinstance(r, dict) or not _row_started(r):
            continue
        pr = f"analise[{i}]"
        if not filled(r.get("tipo_id")):
            issues.append(f"{pr}.tipo_id")
        vd = _norm_veredito(r.get("veredito"))
        if vd is None:
            issues.append(f"{pr}.veredito")
        elif vd == "__invalid__":
            issues.append(f"{pr}.veredito (usar: {', '.join(sorted(VEREDITOS))})")
        else:
            if vd != "inconclusivo":
                if not filled(r.get("metrica_primaria")):
                    issues.append(f"{pr}.metrica_primaria")
                if not filled(r.get("evidencia_resumida")):
                    issues.append(f"{pr}.evidencia_resumida")
            else:
                if not filled(r.get("evidencia_resumida")) and not filled(
                    r.get("volume_notas")
                ):
                    issues.append(
                        f"{pr}: inconclusivo sem evidencia_resumida nem volume_notas"
                    )
            if vd in ("alterar", "expandir"):
                if not filled(r.get("mudanca_proposta")) and not filled(
                    r.get("nova_hipotese")
                ):
                    issues.append(
                        f"{pr}: veredito {vd} sem mudanca_proposta nem nova_hipotese"
                    )
                needs_cl = True
            if vd == "descontinuar":
                needs_cl = True

    if needs_cl:
        clog = d.get("change_log_sugerido") or []
        ok = False
        if isinstance(clog, list):
            for e in clog:
                if isinstance(e, dict) and filled(e.get("resumo")) and filled(
                    e.get("tipo_id")
                ):
                    ok = True
                    break
        if not ok:
            issues.append(
                "(aviso) change_log_sugerido vazio ou incompleto — registrar mudança planejada no banco"
            )

    return issues


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    parts: list[str] = []
    parts.append("# Iteração de tipos criativos — performance (playbook 20)\n\n")
    parts.append(
        f"- **Projeto:** {block(m.get('projeto'))}\n"
        f"- **Período:** {block(m.get('periodo_analise'))}\n"
        f"- **Data relatório:** {block(m.get('data_relatorio'))}\n"
        f"- **Responsável:** {block(m.get('responsavel'))}\n"
        f"- **Banco tipos:** {block(m.get('link_banco_tipos'))}\n"
        f"- **Pack origem:** {block(m.get('link_pack_origem'))}\n"
        f"- **Fontes:** {block(m.get('fontes_dados'))}\n"
        f"- **Notas amostra:** {block(m.get('notas_amostra'))}\n"
    )
    parts.append("\n## Análise por tipo\n\n")
    for r in d.get("analise") or []:
        if not isinstance(r, dict) or not _row_started(r):
            continue
        nv = r.get("novas_variacoes_sugeridas") or []
        nv_s = ", ".join(str(x) for x in nv) if nv else "_[preencher]_"
        parts.append(f"### {block(r.get('tipo_id'))} — {block(r.get('nome_tipo_ref'))}\n\n")
        parts.append(
            f"- **Veredito:** {block(r.get('veredito'))}\n"
            f"- **Métrica:** {block(r.get('metrica_primaria'))} — "
            f"obs: {block(r.get('valor_observado'))} vs base: {block(r.get('baseline_ou_esperado'))}\n"
            f"- **Volume:** {block(r.get('volume_notas'))}\n"
            f"- **Refs campanha/criativo:** {block(r.get('campanhas_creative_refs'))}\n"
        )
        parts.append(f"\n**Evidência:** {block(r.get('evidencia_resumida'))}\n\n")
        parts.append(
            f"**Mudança proposta:** {block(r.get('mudanca_proposta'))}\n\n"
            f"**Nova hipótese:** {block(r.get('nova_hipotese'))}\n\n"
            f"**Novas variações:** {nv_s}\n\n"
            f"**Prioridade próximo pack:** {block(r.get('prioridade_proximo_pack'))}\n\n---\n\n"
        )

    if not any(isinstance(r, dict) and _row_started(r) for r in d.get("analise") or []):
        parts.append("_Nenhuma linha de análise iniciada._\n\n")

    parts.append("## Change log sugerido (→ banco)\n\n")
    for e in d.get("change_log_sugerido") or []:
        if isinstance(e, dict) and (
            filled(e.get("resumo")) or filled(e.get("tipo_id"))
        ):
            parts.append(
                f"- **{block(e.get('data'))}** `{block(e.get('tipo_id'))}` "
                f"v{block(e.get('versao_tipo_apos'))} — {block(e.get('resumo'))}\n"
                f"  - Motivo: {block(e.get('motivo'))} · Autor: {block(e.get('autor'))}\n"
            )
    if not any(
        isinstance(e, dict) and filled(e.get("resumo"))
        for e in (d.get("change_log_sugerido") or [])
    ):
        parts.append("_Nenhuma entrada._\n")

    return "".join(parts)


def summary(d: dict[str, Any]) -> None:
    from collections import Counter

    c = Counter()
    for r in d.get("analise") or []:
        if isinstance(r, dict) and _row_started(r):
            v = _norm_veredito(r.get("veredito"))
            if v and v != "__invalid__":
                c[v] += 1
    print("Vereditos (linhas iniciadas):")
    for k, n in sorted(c.items()):
        print(f"  {k}: {n}")
    print(f"  total: {sum(c.values())}")


def main() -> None:
    p = argparse.ArgumentParser(description="Iteração tipos por performance (pb20)")
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
        print("Lacunas (iteração tipos):")
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
