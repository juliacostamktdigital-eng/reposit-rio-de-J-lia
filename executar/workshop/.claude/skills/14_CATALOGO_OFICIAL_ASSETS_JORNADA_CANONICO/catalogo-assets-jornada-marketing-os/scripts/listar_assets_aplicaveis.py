#!/usr/bin/env python3
"""Filtra o catalogo de assets (playbook 14) por contexto booleano e gera Markdown."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def applies(item: dict[str, Any], ctx: dict[str, Any]) -> tuple[bool | None, str]:
    cl = (item.get("classificacao") or "").strip()
    gat = item.get("gatilhos_condicionais") or []

    if cl == "Obrigatório":
        if not gat:
            return True, "obrigatório"
        if all(ctx.get(g) for g in gat):
            return True, "obrigatório (gatilhos satisfeitos)"
        return False, f"obrig. pendentes gatilhos {gat}"

    if "Obrigatório quando Meta entra no plano" in cl:
        return bool(ctx.get("meta_plano")), "quando Meta no plano"
    if "Obrigatório quando Google entra no plano" in cl:
        return bool(ctx.get("google_plano")), "quando Google no plano"
    if cl == "Obrigatório para Meta":
        return bool(ctx.get("meta_plano")), "para Meta"
    if cl == "Obrigatório para Google":
        return bool(ctx.get("google_plano")), "para Google"
    if cl == "Obrigatório para Search":
        return bool(ctx.get("google_search")), "para Search"

    if cl == "Condicional":
        if not gat:
            return None, "condicional — revisar manualmente"
        if any(ctx.get(g) for g in gat):
            return True, "condicional aplicável"
        return False, "condicional não acionada"

    if cl == "Suporte":
        return None, "suporte"
    if cl == "Evidência":
        return None, "evidência"
    if cl == "Legado":
        return None, "legado"

    return None, cl or "?"


def iter_itens(data: dict[str, Any]):
    for grp in data.get("grupos") or []:
        titulo = grp.get("titulo", "")
        for it in grp.get("itens") or []:
            yield titulo, it


def render_md(data: dict[str, Any], ctx: dict[str, Any]) -> str:
    meta = ctx.get("meta") or {}
    lines: list[str] = [
        "# Assets aplicáveis ao contexto\n",
        f"- **Cliente/projeto:** {meta.get('cliente_projeto', '')}\n",
        f"- **Data:** {meta.get('data', '')}\n",
    ]
    if meta.get("nota_contexto"):
        lines.append(f"- **Nota:** {meta.get('nota_contexto')}\n")

    sec_sim: list[tuple[str, str, dict, str]] = []
    sec_nao: list[tuple[str, str, dict, str]] = []
    sec_manual: list[tuple[str, str, dict, str]] = []

    for titulo, it in iter_itens(data):
        dec, motivo = applies(it, ctx)
        nome = it.get("nome", "")
        if dec is True:
            sec_sim.append((titulo, nome, it, motivo))
        elif dec is False:
            sec_nao.append((titulo, nome, it, motivo))
        else:
            sec_manual.append((titulo, nome, it, motivo))

    lines.append("## Incluir neste contexto\n")
    lines.append("| Grupo | Asset | Classificação | Quando entra | Motivo |\n|---|---|---|---|---|")
    for titulo, nome, it, motivo in sorted(sec_sim, key=lambda x: (x[0], x[1])):
        cl = str(it.get("classificacao", "")).replace("|", "\\|")
        qd = str(it.get("quando_entra", "")).replace("|", "\\|")
        lines.append(f"| {titulo} | {nome} | {cl} | {qd} | {motivo} |")
    lines.append("")

    lines.append("## Fora do contexto (por gatilho/canal)\n")
    lines.append("| Grupo | Asset | Classificação | Quando entra | Motivo |\n|---|---|---|---|---|")
    if sec_nao:
        for titulo, nome, it, motivo in sorted(sec_nao, key=lambda x: (x[0], x[1])):
            cl = str(it.get("classificacao", "")).replace("|", "\\|")
            qd = str(it.get("quando_entra", "")).replace("|", "\\|")
            lines.append(f"| {titulo} | {nome} | {cl} | {qd} | {motivo} |")
    else:
        lines.append("| — | — | — | — | Nenhum item excluído automaticamente. |")
    lines.append("")

    lines.append("## Revisão manual / suporte / evidência / legado\n")
    lines.append("| Grupo | Asset | Classificação | Quando entra | Nota |\n|---|---|---|---|---|")
    for titulo, nome, it, motivo in sorted(sec_manual, key=lambda x: (x[0], x[1])):
        cl = str(it.get("classificacao", "")).replace("|", "\\|")
        qd = str(it.get("quando_entra", "")).replace("|", "\\|")
        lines.append(f"| {titulo} | {nome} | {cl} | {qd} | {motivo} |")
    lines.append("")
    return "\n".join(lines)


def resumo(data: dict[str, Any]) -> None:
    by: dict[str, int] = {}
    for _titulo, it in iter_itens(data):
        cl = it.get("classificacao") or "?"
        by[cl] = by.get(cl, 0) + 1
    print("Catálogo playbook 14 — por classificação:")
    for k in sorted(by):
        print(f"  {k}: {by[k]}")
    print(f"  Total: {sum(by.values())}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Listar assets do catálogo conforme contexto.")
    parser.add_argument(
        "--catalogo",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data" / "catalogo_assets.json",
    )
    parser.add_argument("--context", type=Path, help="JSON de contexto")
    parser.add_argument("--md", type=Path, help="Escrever Markdown")
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--resumo", action="store_true")
    args = parser.parse_args()

    data = load_json(args.catalogo)
    if args.resumo:
        resumo(data)
        return

    if not args.context:
        print("Defina --context para filtrar, ou use --resumo.")
        return

    raw = load_json(args.context)
    ctx: dict[str, Any] = {k: v for k, v in raw.items() if k != "meta"}
    ctx["meta"] = raw.get("meta") or {}

    n_sim = n_nao = n_manual = 0
    for _t, it in iter_itens(data):
        dec, _ = applies(it, ctx)
        if dec is True:
            n_sim += 1
        elif dec is False:
            n_nao += 1
        else:
            n_manual += 1

    if args.audit:
        print(f"Incluir (auto): {n_sim}")
        print(f"Excluir por contexto (auto): {n_nao}")
        print(f"Manual / suporte / evidência / legado: {n_manual}")

    if args.md:
        args.md.write_text(render_md(data, ctx), encoding="utf-8")

    if not args.audit and not args.md:
        print(render_md(data, ctx), end="")


if __name__ == "__main__":
    main()
