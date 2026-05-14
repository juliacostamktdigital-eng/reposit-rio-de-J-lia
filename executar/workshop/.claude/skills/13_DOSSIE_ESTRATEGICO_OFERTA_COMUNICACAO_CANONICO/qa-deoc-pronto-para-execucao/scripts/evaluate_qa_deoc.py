#!/usr/bin/env python3
"""Le checklist QA DEOC (JSON), audita completude N2/implementacao/estrutura e gera relatorio Markdown."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def norm_status(raw: Any) -> str | None:
    if raw is None:
        return None
    t = str(raw).strip().lower()
    if not t:
        return None
    if t in ("n.a.", "n/a", "na"):
        return "na"
    if t in ("ok", "sim", "s"):
        return "ok"
    if t in ("gap", "falha", "fail"):
        return "gap"
    return None


def summarize_block(items: list[dict[str, Any]], status_key: str = "status") -> tuple[int, int, int, list[str]]:
    ok = na = gap = 0
    pending: list[str] = []
    for it in items:
        if not isinstance(it, dict):
            continue
        st = norm_status(it.get(status_key))
        iid = it.get("id", "?")
        if st is None:
            pending.append(str(iid))
        elif st == "ok":
            ok += 1
        elif st == "na":
            na += 1
        else:
            gap += 1
            pending.append(f"{iid}(gap)")
    return ok, na, gap, pending


def recommend(
    n2_pending: list[str],
    n2_gap: int,
    impl_gap: int,
    struct_gap: int,
    anti_hit: int,
) -> str:
    if n2_pending:
        return "incompleto — preencher todos os itens N2 com ok, gap ou n.a."
    if n2_gap:
        return "nao pronto — existe gap em criterio N2 (playbook 13 seção 6)."
    if anti_hit:
        return "nao pronto — anti-padrão da seção 8 marcado como detectado."
    if impl_gap:
        return "condicional — falha em pergunta de implementação (seção 3); execução com risco."
    if struct_gap:
        return "condicional — lacuna em cobertura estrutural 5.x; revisar antes de escalar."
    return "pronto — N2 sem gap; implementação e estrutura sem gap; sem anti-padrão detectado."


def render_md(data: dict[str, Any], rec: str) -> str:
    m = data.get("meta") or {}
    lines: list[str] = []
    lines.append("# Relatório de QA — DEOC\n")
    lines.append(
        f"- **Cliente/projeto:** {m.get('cliente_projeto', '')}\n"
        f"- **Data:** {m.get('data_revisao', '')}\n"
        f"- **Revisor:** {m.get('revisor', '')}\n"
        f"- **DEOC:** {m.get('versao_link_deoc', '')}\n"
    )
    lines.append(f"## Sugestão automática (revisão humana obrigatória)\n\n**{rec}**\n")

    n2 = data.get("n2") or []
    n2_ok, n2_na, n2_gap, n2_pend = summarize_block(n2)
    lines.append("## N2 (Seção 6)\n")
    lines.append(f"- ok: {n2_ok} · n.a.: {n2_na} · gap: {n2_gap}\n")
    if n2_pend:
        lines.append("- Itens a revisar: " + ", ".join(n2_pend) + "\n")

    impl = data.get("implementacao") or []
    i_ok, i_na, i_gap, i_pend = summarize_block(impl)
    lines.append("## Implementação (Seção 3)\n")
    lines.append(f"- ok: {i_ok} · n.a.: {i_na} · gap: {i_gap}\n")
    if i_pend:
        lines.append("- Itens a revisar: " + ", ".join(i_pend) + "\n")

    st = data.get("estrutura") or []
    s_ok, s_na, s_gap, s_pend = summarize_block(st)
    lines.append("## Cobertura 5.1–5.9\n")
    lines.append(f"- ok: {s_ok} · n.a.: {s_na} · gap: {s_gap}\n")
    if s_pend:
        lines.append("- Itens a revisar: " + ", ".join(s_pend) + "\n")

    n3 = data.get("n3") or []
    n3_ok, n3_na, n3_gap, n3_pend = summarize_block(n3)
    lines.append("## N3 (Seção 7) — referência de maturidade\n")
    lines.append(f"- ok: {n3_ok} · n.a.: {n3_na} · gap: {n3_gap}\n")
    if n3_pend:
        lines.append("- Incompletos ou gap: " + ", ".join(n3_pend) + "\n")

    anti = data.get("anti_padroes_sec8") or []
    hits = []
    for it in anti:
        if isinstance(it, dict) and it.get("detectado") is True:
            hits.append(f"{it.get('id')}: {it.get('descricao', '')} — {it.get('detalhe', '')}")
    lines.append("## Anti-padrões (Seção 8)\n")
    if hits:
        for h in hits:
            lines.append(f"- **DETECTADO:** {h}\n")
    else:
        lines.append("- Nenhum marcado como detectado.\n")

    dec = data.get("decisao") or {}
    lines.append("## Decisão registrada no JSON\n")
    lines.append(f"- **Resultado:** {dec.get('resultado', '_(vazio)_')}\n")
    lines.append(f"- **Justificativa:** {dec.get('justificativa', '')}\n")
    if dec.get("condicionais"):
        lines.append(f"- **Condicionais:** {dec.get('condicionais')}\n")
    steps = dec.get("proximos_passos") or []
    if steps:
        lines.append("- **Próximos passos:**\n")
        for s in steps:
            lines.append(f"  - {s}\n")

    return "\n".join(lines)


def audit_stdout(data: dict[str, Any], rec: str, anti_hit: int) -> None:
    n2 = data.get("n2") or []
    _, _, n2_gap, n2_pend = summarize_block(n2)
    impl = data.get("implementacao") or []
    _, _, impl_gap, impl_pend = summarize_block(impl)
    st = data.get("estrutura") or []
    _, _, struct_gap, struct_pend = summarize_block(st)

    print("QA DEOC (playbook 13)")
    print(f"  Sugestão: {rec}")
    if n2_pend:
        print(f"  N2 pendente/incompleto: {', '.join(n2_pend)}")
    if n2_gap:
        print(f"  N2 com gap: {n2_gap} item(ns)")
    if impl_pend:
        print(f"  Implementação pendente: {', '.join(impl_pend)}")
    if impl_gap:
        print(f"  Implementação com gap: {impl_gap} item(ns)")
    if struct_pend:
        print(f"  Estrutura pendente: {', '.join(struct_pend)}")
    if struct_gap:
        print(f"  Estrutura com gap: {struct_gap} item(ns)")
    if anti_hit:
        print(f"  Anti-padrões detectados: {anti_hit}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate DEOC QA checklist JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path, help="Write Markdown report")
    parser.add_argument("--audit", action="store_true", help="Print summary to stdout")
    args = parser.parse_args()

    data = load(args.input_json)
    anti = data.get("anti_padroes_sec8") or []
    anti_hit = sum(1 for it in anti if isinstance(it, dict) and it.get("detectado") is True)

    n2 = data.get("n2") or []
    _, _, n2_gap, n2_pend = summarize_block(n2)
    impl = data.get("implementacao") or []
    _, _, impl_gap, _impl_pend = summarize_block(impl)
    st = data.get("estrutura") or []
    _, _, struct_gap, _st_pend = summarize_block(st)

    rec = recommend(
        n2_pending=n2_pend,
        n2_gap=n2_gap,
        impl_gap=impl_gap,
        struct_gap=struct_gap,
        anti_hit=anti_hit,
    )

    if args.md_path:
        args.md_path.write_text(render_md(data, rec), encoding="utf-8")
    if args.audit:
        audit_stdout(data, rec, anti_hit)
    if not args.md_path and not args.audit:
        print(render_md(data, rec), end="")


if __name__ == "__main__":
    main()
