#!/usr/bin/env python3
"""Gera Markdown de Oferta Executavel a partir de JSON e audita lacunas N2 para a fatia 5.2/5.8."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def block(text: str) -> str:
    s = (text or "").strip()
    return s if s else "_[preencher]_"


def bullets(items: list[Any]) -> str:
    if not items:
        return "- _[preencher]_"
    return "\n".join(f"- {it}".strip() for it in items)


def table_two_col(rows: list[dict[str, str]], k1: str, k2: str, h1: str, h2: str) -> str:
    if not rows:
        return f"| {h1} | {h2} |\n|---|---|\n| _[preencher]_ | _[preencher]_ |"
    lines = [f"| {h1} | {h2} |", "|---|---|"]
    for r in rows:
        lines.append(f"| {block(r.get(k1, ''))} | {block(r.get(k2, ''))} |")
    return "\n".join(lines)


def table_claims(rows: list[dict[str, str]], keys: tuple[str, ...], titles: tuple[str, ...]) -> str:
    if not rows:
        return "| " + " | ".join(titles) + " |\n|" + "|".join(["---"] * len(titles)) + "|"
    header = "| " + " | ".join(titles) + " |"
    sep = "|" + "|".join(["---"] * len(titles)) + "|"
    body = ["| " + " | ".join(block(r.get(k, "")) for k in keys) + " |" for r in rows]
    return "\n".join([header, sep, *body])


def cb(done: bool) -> str:
    return "[x]" if done else "[ ]"


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    n = d.get("norte") or {}
    mec = d.get("mecanismo") or {}
    feats = d.get("features") or []
    cd = d.get("condicoes_diferenciais") or []
    esc = d.get("escopo") or {}
    lim = d.get("limites") or {}
    cl = d.get("claims") or {}
    der = d.get("derivados") or {}
    chk = d.get("checklist_risco") or {}
    bl = d.get("backlog_fortalecimento") or []

    parts: list[str] = []
    parts.append("# Oferta executável (empacotamento v1)\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente / produto | {block(m.get('cliente_ou_produto'))} |\n"
        f"| Versão | {block(m.get('versao'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Responsável | {block(m.get('responsavel'))} |\n"
        f"| DEOC / link | {block(m.get('deoc_link'))} |\n"
    )

    parts.append("## 1. Norte\n")
    parts.append(f"**O que é vendido:** {block(n.get('o_que_e_vendido'))}\n")
    parts.append(f"**Para quem (ICP resumido):** {block(n.get('para_quem_icp_resumido'))}\n")
    parts.append(f"**Quando faz sentido:** {block(n.get('quando_faz_sentido'))}\n")
    parts.append(f"**Quando não faz sentido (anti-ICP):** {block(n.get('quando_nao_faz_sentido_anti_icp'))}\n")

    parts.append("## 2. Brainer comercial\n")
    parts.append(f"*Faço X em Y, para Z, com W.* → {block(d.get('brainer'))}\n")

    parts.append("## 3. Mecanismo\n")
    parts.append(f"**Como funciona:** {block(mec.get('como_funciona_visao_geral'))}\n")
    parts.append(f"**Mecanismo de resultado:** {block(mec.get('mecanismo_geracao_resultado'))}\n")

    parts.append("## 4. Features (formato DEOC 5.2)\n")
    for i, f in enumerate(feats, 1):
        if not isinstance(f, dict):
            continue
        titulo = block(f.get("nome", f"Feature {i}"))
        parts.append(f"### {titulo}\n")
        parts.append("| Campo | Conteúdo |\n|---|---|")
        for label, key in (
            ("Feature", "feature"),
            ("Como funciona", "como_funciona"),
            ("Implicação", "implicacao"),
            ("Benefício", "beneficio"),
            ("Prova", "prova"),
            ("Como vira copy", "como_vira_copy"),
        ):
            parts.append(f"| {label} | {block(f.get(key, ''))} |")
        parts.append("")
    if not feats:
        parts.append("_[Adicionar pelo menos uma feature no JSON]_\n")

    parts.append("## 5. Condições diferenciais\n")
    parts.append(table_two_col([dict(x) for x in cd if isinstance(x, dict)], "condicao", "lastro", "Condição", "Lastro") + "\n")

    parts.append("## 6. Escopo explícito\n")
    parts.append("### Entra\n" + bullets(list(esc.get("entra") or [])) + "\n")
    parts.append("### Não entra\n" + bullets(list(esc.get("nao_entra") or [])) + "\n")
    parts.append("### Pré-requisitos do cliente\n" + bullets(list(esc.get("pre_requisitos_cliente") or [])) + "\n")
    parts.append(f"**Nota preço (só comunicação / lógica):** {block(esc.get('nota_preco_apenas_comunicacao'))}\n")

    parts.append("## 7. Limites da promessa\n")
    parts.append(f"**Quando não vender:** {block(lim.get('quando_nao_vender'))}\n")
    parts.append(f"**Risco de passivo:** {block(lim.get('risco_passivo'))}\n")
    parts.append(f"**Sinais de lead mal qualificado:** {block(lim.get('sinais_lead_mal_qualificado'))}\n")

    perm = [dict(x) for x in (cl.get("permitidos") or []) if isinstance(x, dict)]
    prob = [dict(x) for x in (cl.get("proibidos") or []) if isinstance(x, dict)]
    pend = [dict(x) for x in (cl.get("pendentes") or []) if isinstance(x, dict)]
    parts.append("## 8. Claims\n")
    parts.append("### Permitidos\n" + table_claims(perm, ("claim", "ancora"), ("Claim", "Âncora")) + "\n")
    parts.append("### Proibidos\n" + table_claims(prob, ("claim", "motivo"), ("Claim", "Motivo")) + "\n")
    parts.append(
        "### Pendentes\n"
        + table_claims(
            pend,
            ("claim", "evidencia_necessaria", "owner"),
            ("Claim", "Evidência necessária", "Owner"),
        )
        + "\n"
    )

    parts.append("## 9. Derivados\n")
    parts.append(f"**Headline / promessa central:** {block(der.get('headline_ou_promessa_central'))}\n")
    parts.append("**Ângulos de campanha:**\n" + bullets(list(der.get("angulos_campanha") or [])) + "\n")
    parts.append("**Checklist de qualificação:**\n" + bullets(list(der.get("checklist_qualificacao") or [])) + "\n")

    parts.append("## 10. Checklist de risco\n")
    parts.append(f"- {cb(chk.get('entrega_sem_heroi'))} Entrega possível sem heroísmo operacional\n")
    parts.append(f"- {cb(chk.get('promessa_auditavel'))} Promessa auditável ou plano de prova\n")
    parts.append(f"- {cb(chk.get('condicoes_sem_passivo_impossivel'))} Condições diferenciais sem passivo impossível\n")
    parts.append(f"- {cb(chk.get('brainer_repetivel'))} Brainer repetível por marketing e vendas\n")
    parts.append(f"- {cb(chk.get('escopo_explicito'))} Escopo e pré-requisitos explícitos para o cliente\n")

    parts.append("## Backlog — fortalecimento\n")
    if bl:
        parts.append("| Item | Tipo | Prioridade |\n|---|---|---|")
        for r in bl:
            if isinstance(r, dict):
                parts.append(
                    f"| {block(r.get('item'))} | {block(r.get('tipo'))} | {block(r.get('prioridade'))} |"
                )
        parts.append("")
    else:
        parts.append("| Item | Tipo | Prioridade |\n|---|---|---|\n| | | |\n")

    return "\n".join(parts)


def nonempty_str(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def feature_complete(f: dict[str, Any]) -> bool:
    keys = ("feature", "como_funciona", "implicacao", "beneficio", "prova", "como_vira_copy")
    return all(nonempty_str(f.get(k)) for k in keys)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    n = d.get("norte") or {}
    for key, label in (
        ("o_que_e_vendido", "norte.o_que_e_vendido"),
        ("para_quem_icp_resumido", "norte.para_quem_icp_resumido"),
        ("quando_faz_sentido", "norte.quando_faz_sentido"),
        ("quando_nao_faz_sentido_anti_icp", "norte.quando_nao_faz_sentido_anti_icp"),
    ):
        if not nonempty_str(n.get(key)):
            issues.append(f"{label} vazio")

    if not nonempty_str(d.get("brainer")):
        issues.append("brainer vazio")

    mec = d.get("mecanismo") or {}
    if not nonempty_str(mec.get("como_funciona_visao_geral")):
        issues.append("mecanismo.como_funciona_visao_geral vazio")
    if not nonempty_str(mec.get("mecanismo_geracao_resultado")):
        issues.append("mecanismo.mecanismo_geracao_resultado vazio")

    feats = [f for f in (d.get("features") or []) if isinstance(f, dict)]
    if not feats:
        issues.append("features: pelo menos uma entrada")
    elif not any(feature_complete(f) for f in feats):
        issues.append("features: pelo menos uma linha com todos os campos canonicos preenchidos")

    esc = d.get("escopo") or {}
    entra = esc.get("entra") or []
    nent = esc.get("nao_entra") or []
    if not (isinstance(entra, list) and entra):
        issues.append("escopo.entra: pelo menos um item")
    if not (isinstance(nent, list) and nent):
        issues.append("escopo.nao_entra: pelo menos um item")

    lim = d.get("limites") or {}
    if not nonempty_str(lim.get("quando_nao_vender")):
        issues.append("limites.quando_nao_vender vazio")

    cd = [x for x in (d.get("condicoes_diferenciais") or []) if isinstance(x, dict)]
    if not cd or not any(nonempty_str(x.get("condicao")) and nonempty_str(x.get("lastro")) for x in cd):
        issues.append("condicoes_diferenciais: pelo menos uma linha com condicao e lastro")

    cl = d.get("claims") or {}
    perm = cl.get("permitidos") or []
    if not (
        isinstance(perm, list)
        and perm
        and any(nonempty_str(x.get("claim")) for x in perm if isinstance(x, dict))
    ):
        issues.append("claims.permitidos: pelo menos um claim com texto")

    prob = cl.get("proibidos") or []
    if not (
        isinstance(prob, list)
        and prob
        and any(nonempty_str(x.get("claim")) for x in prob if isinstance(x, dict))
    ):
        issues.append("claims.proibidos: pelo menos um claim governado (ex. superlativo sem prova)")

    chk = d.get("checklist_risco") or {}
    for key, label in (
        ("entrega_sem_heroi", "checklist.entrega_sem_heroi"),
        ("promessa_auditavel", "checklist.promessa_auditavel"),
        ("condicoes_sem_passivo_impossivel", "checklist.condicoes_sem_passivo_impossivel"),
        ("brainer_repetivel", "checklist.brainer_repetivel"),
        ("escopo_explicito", "checklist.escopo_explicito"),
    ):
        if not chk.get(key):
            issues.append(f"{label} nao marcado como ok")

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Oferta Executavel Markdown; audit N2 fatia 5.2.")
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
            print("Lacunas (fatia oferta N2 / playbook 13):")
            for line in issues:
                print(f"  - {line}")
        else:
            print("Auditoria: nenhuma lacuna obrigatoria detectada neste schema.")
    if not args.md_path and not args.audit:
        print(render_md(data), end="")


if __name__ == "__main__":
    main()
