#!/usr/bin/env python3
"""Gera Markdown do blueprint Google Display a partir de JSON e audita (playbook 16 §9 Display, §14)."""

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


def _ex_row(x: Any) -> tuple[str, str]:
    if isinstance(x, dict):
        return block(x.get("item") or x.get("termo")), block(x.get("motivo"))
    if isinstance(x, str):
        return x.strip(), ""
    return "", ""


def _count_exclusoes(ex: dict[str, Any]) -> int:
    n = 0
    for key in ("anti_icp", "placements_apps_bloqueados"):
        for x in ex.get(key) or []:
            a, _ = _ex_row(x)
            if a and a != "_[preencher]_":
                n += 1
    return n


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    ff = d.get("funcao_funil") or {}
    ex = d.get("exclusoes") or {}
    freq = d.get("frequencia") or {}
    mt = d.get("matriz_testes") or {}
    pg = d.get("pre_go_live_display") or {}

    parts: list[str] = []
    parts.append("# Google Ads Display — consolidado\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente | {block(m.get('cliente'))} |\n"
        f"| Versão | {block(m.get('versao_doc'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Responsável | {block(m.get('responsavel'))} |\n"
        f"| Plano mídia | {block(m.get('link_plano_midia_display'))} |\n"
        f"| Setup base | {block(m.get('link_setup_google_base'))} |\n"
    )

    parts.append("## Função no funil (§9)\n")
    parts.append(f"- **Tipo:** {block(ff.get('tipo'))}\n")
    parts.append(f"- **Descrição:** {block(ff.get('descricao'))}\n")
    parts.append(f"- **Métrica de leitura:** {block(ff.get('metrica_leitura'))}\n")
    parts.append(
        f"- **Não é sobra de verba (confirmação):** {d.get('compromisso_nao_sobra_verba')}\n"
    )

    parts.append("## Exclusões\n")
    parts.append("### Anti-ICP\n")
    for x in ex.get("anti_icp") or []:
        a, b = _ex_row(x)
        parts.append(f"- {a} — {b}\n")
    parts.append("### Placements / apps bloqueados\n")
    for x in ex.get("placements_apps_bloqueados") or []:
        a, b = _ex_row(x)
        parts.append(f"- {a} — {b}\n")

    parts.append(f"## Brand safety\n{block(d.get('brand_safety'))}\n")
    parts.append("## Frequência\n")
    parts.append(f"- **Regra:** {block(freq.get('regra'))}\n")
    parts.append(f"- **Notas:** {block(freq.get('notas'))}\n")
    parts.append(f"## Janela remarketing\n{block(d.get('janela_remarketing'))}\n")

    parts.append("## Campanhas\n")
    for i, c in enumerate(d.get("campanhas") or [], 1):
        if not isinstance(c, dict):
            continue
        parts.append(f"### Campanha {i}\n")
        parts.append(f"- `campaign_id`: {block(c.get('campaign_id'))}\n")
        parts.append(f"- Nome: {block(c.get('nome_taxonomia'))}\n")
        parts.append(f"- URL: {block(c.get('url_final'))}\n")
        parts.append(f"- Objetivo Display: {block(c.get('objetivo_display'))}\n")
        parts.append(f"- Orçamento: {block(c.get('orcamento_lances_resumo'))}\n")
        parts.append(f"- Hipótese: {block(c.get('hipotese'))}\n")
        for j, g in enumerate(c.get("grupos") or [], 1):
            if not isinstance(g, dict):
                continue
            parts.append(f"#### Grupo {j}\n")
            parts.append(f"- `adgroup_id`: {block(g.get('adgroup_id'))}\n")
            parts.append(f"- Audiência/temp: {block(g.get('temperatura_audiencia'))}\n")
            parts.append(f"- Targeting: {block(g.get('targeting_resumo'))}\n")
            parts.append(f"- Exclusões grupo: {block(g.get('exclusoes_grupo'))}\n")
            parts.append("| creative_id | Formato | Hipótese |\n|---|---|---|")
            for cr in g.get("criativos") or []:
                if isinstance(cr, dict):
                    parts.append(
                        f"| {block(cr.get('creative_id'))} | {block(cr.get('formato'))} | "
                        f"{block(cr.get('hipotese_leitura'))} |"
                    )
            parts.append("")

    parts.append("## Matriz de testes\n")
    parts.append(f"- **Varia:** {block(mt.get('o_que_varia'))}\n")
    parts.append(f"- **Constante:** {block(mt.get('o_que_constante'))}\n")

    parts.append("## Pré go-live Display (§14)\n")
    for k, label in (
        ("placements_apps_ok", "Placements/apps"),
        ("frequencia_ok", "Frequência"),
        ("exclusoes_ok", "Exclusões"),
        ("brand_safety_ok", "Brand safety"),
        ("urls_rastreio_ok", "URLs/rastreio"),
        ("hipotese_planilha", "Hipótese planilha"),
        ("changelog", "Changelog"),
    ):
        parts.append(f"- [ {'x' if pg.get(k) else ' '} ] {label}\n")

    parts.append("\n## Gaps N2\n")
    parts.append(block(d.get("n2_gaps")) + "\n")
    return "\n".join(parts)


def _needs_janela(tipo: str) -> bool:
    t = (tipo or "").lower()
    return "remarketing" in t or "recuper" in t


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not nonempty_str(m.get("cliente")):
        issues.append("meta.cliente vazio")

    if not d.get("compromisso_nao_sobra_verba"):
        issues.append("compromisso_nao_sobra_verba: confirmar true (playbook §9)")

    ff = d.get("funcao_funil") or {}
    if not nonempty_str(ff.get("descricao")):
        issues.append("funcao_funil.descricao vazio")
    if not nonempty_str(ff.get("metrica_leitura")):
        issues.append("funcao_funil.metrica_leitura vazio")

    if not nonempty_str(d.get("brand_safety")):
        issues.append("brand_safety vazio (§9)")

    freq = d.get("frequencia") or {}
    if not nonempty_str(freq.get("regra")):
        issues.append("frequencia.regra vazio (§9/§14)")

    ex = d.get("exclusoes") or {}
    if _count_exclusoes(ex) < 1:
        issues.append("exclusoes: registrar pelo menos uma exclusão anti-ICP ou placement/app")

    if _needs_janela(ff.get("tipo") or "") and not nonempty_str(d.get("janela_remarketing")):
        issues.append("janela_remarketing obrigatória para remarketing/recuperação (§9)")

    mt = d.get("matriz_testes") or {}
    if not nonempty_str(mt.get("o_que_varia")) or not nonempty_str(mt.get("o_que_constante")):
        issues.append("matriz_testes incompleta")

    has_c = has_g = has_cr = False
    for c in d.get("campanhas") or []:
        if not isinstance(c, dict):
            continue
        if nonempty_str(c.get("campaign_id")):
            has_c = True
        if not nonempty_str(c.get("url_final")):
            issues.append("campanha: url_final vazio")
        for g in c.get("grupos") or []:
            if isinstance(g, dict) and nonempty_str(g.get("adgroup_id")):
                has_g = True
                if not nonempty_str(g.get("targeting_resumo")):
                    issues.append(
                        f"grupo {g.get('adgroup_id', '?')}: targeting_resumo vazio"
                    )
                for cr in g.get("criativos") or []:
                    if isinstance(cr, dict) and nonempty_str(cr.get("creative_id")):
                        has_cr = True
    if not has_c:
        issues.append("campanhas: campaign_id")
    if not has_g:
        issues.append("estrutura: pelo menos um adgroup_id")
    if not has_cr:
        issues.append("criativos: pelo menos um creative_id")

    pg = d.get("pre_go_live_display") or {}
    for k, lab in (
        ("placements_apps_ok", "pre_go_live_display.placements_apps_ok"),
        ("frequencia_ok", "pre_go_live_display.frequencia_ok"),
        ("exclusoes_ok", "pre_go_live_display.exclusoes_ok"),
        ("brand_safety_ok", "pre_go_live_display.brand_safety_ok"),
    ):
        if not pg.get(k):
            issues.append(f"{lab} (§14 Display)")

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
            print("Lacunas (Display / playbook 16):")
            for i in iss:
                print(f"  - {i}")
        else:
            print("Auditoria: função, exclusões, brand safety, frequência e pré go-live críticos OK.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
