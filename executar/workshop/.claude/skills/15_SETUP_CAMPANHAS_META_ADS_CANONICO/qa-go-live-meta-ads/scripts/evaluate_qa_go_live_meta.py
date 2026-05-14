#!/usr/bin/env python3
"""Lê checklist-go-live-meta.json, audita status (playbook 15), emite resumo e relatório Markdown."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


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
    if t in ("gap", "falha", "fail", "não", "nao", "no"):
        return "gap"
    return None


def build_default_checklist() -> list[dict[str, Any]]:
    def a(gr: str, ref: str, iid: str, lab: str) -> dict[str, Any]:
        return {"grupo": gr, "id": iid, "ref": ref, "label": lab, "status": "", "nota": ""}

    rows: list[dict[str, Any]] = []
    for iid, lab in [
        ("p-01", "Conta de anúncio configurada corretamente (BM, ad account)"),
        ("p-02", "Pixel/CAPI/eventos funcionando"),
        ("p-03", "Públicos básicos existem para o movimento"),
        ("p-04", "Campanha, conjunto e anúncio têm IDs"),
        ("p-05", "Estrutura permite teste sem fragmentar demais o orçamento"),
        ("p-06", "Hipótese clara"),
        ("p-07", "Plano de leitura definido"),
        ("p-08", "Planilha backup e contrato de dados ativos e alinhados"),
    ]:
        rows.append(a("principio", "§1", iid, lab))
    for iid, lab in [
        ("c-01", "Business Manager correto"),
        ("c-02", "Conta de anúncios correta"),
        ("c-03", "Método de pagamento ativo"),
        ("c-04", "Página Facebook vinculada"),
        ("c-05", "Instagram vinculado"),
        ("c-06", "Domínio verificado quando aplicável"),
        ("c-07", "Permissões do time conferidas"),
        ("c-08", "Pixel instalado"),
        ("c-09", "CAPI configurada quando possível"),
        ("c-10", "Eventos principais testados"),
        ("c-11", "UTMs preservadas na LP/formulário"),
        ("c-12", "Backup recebendo lead; CRM recebendo ou conciliável"),
    ]:
        rows.append(a("conta", "§4", iid, lab))
    for iid, lab in [
        ("e-01", "Evento de otimização: mais profundo possível sem matar volume (documentado)"),
        ("e-02", "Eventos do funil disparando de forma verificável"),
        ("e-03", "Eventos priorizados na conta quando aplicável"),
    ]:
        rows.append(a("eventos", "§5", iid, lab))
    for iid, lab in [
        ("pv-01", "Temperatura separada (sem misturar quente/frio sem intenção)"),
        ("pv-02", "Exclusões aplicadas (aquisição, remarketing, convertidos)"),
        ("pv-03", "Quantidade de conjuntos compatível com orçamento (evitar 12+ sem motivo)"),
        ("pv-04", "Públicos coerentes com objetivo e criativo"),
        ("pv-05", "Estrutura mínima se budget baixo (consolidação)"),
    ]:
        rows.append(a("publicos_estrutura", "§6-8", iid, lab))
    for iid, lab in [
        ("n-01", "Nomes de campanha seguem taxonomia (campaign_id)"),
        ("n-02", "Conjuntos com adgroup_id nos nomes"),
        ("n-03", "Anúncios com creative_id nos nomes"),
    ]:
        rows.append(a("nomenclatura_ids", "§10", iid, lab))
    for iid, lab in [
        ("cr-01", "3–5 anúncios por conjunto (faixa inicial)"),
        ("cr-02", "Variações reais (não peças quase idênticas)"),
        ("cr-03", "Cada criativo com creative_id"),
        ("cr-04", "Cada criativo com hipótese de leitura"),
    ]:
        rows.append(a("criativos", "§11", iid, lab))
    for iid, lab in [
        ("o-01", "Orçamento mínimo por conjunto viável para aprendizado"),
        ("o-02", "CBO vs ABO coerente com o experimento"),
        ("o-03", "Sem fragmentação excessiva vs verba"),
    ]:
        rows.append(a("orcamento", "§12", iid, lab))
    gl = [
        "Campanha criada com ID",
        "Conjuntos criados com ID",
        "Anúncios criados com ID",
        "Público e temperatura corretos",
        "Exclusões aplicadas",
        "Pixel/eventos testados",
        "UTMs aplicadas",
        "Planilha backup testada",
        "CRM/handoff testado",
        "Criativos aprovados",
        "Matriz de testes registrada",
        "Campos/perguntas lead nativo conferidos (se aplicável)",
        "Regra engajamento/vídeo definida (se aplicável)",
        "Orçamento e datas conferidos",
        "Hipótese na planilha de growth",
        "Change log preparado",
    ]
    for i, lab in enumerate(gl, 1):
        rows.append(a("go_live", "§13", f"gl-{i:02d}", lab))
    for iid, lab in [
        ("n2-01", "UTMs e campos v4_* aplicados"),
        ("n2-02", "Públicos padrão da estratégia criados"),
        ("n2-03", "Checklist pré go-live consolidado preenchido"),
    ]:
        rows.append(a("n2_complemento", "§14", iid, lab))
    return rows


def build_default_anti() -> list[dict[str, Any]]:
    labs = [
        "Campanha sem ID",
        "Criativo sem ID",
        "Público quente e frio misturados sem intenção",
        "12+ conjuntos com pouca verba",
        "Muitos interesses pequenos sem volume",
        "Remarketing sem exclusão de convertidos",
        "Criativos genéricos que não segmentam pelo conteúdo",
        "Pixel/evento não testado",
        "Lead sem planilha backup",
        "Otimizar só por CPL sem qualidade comercial",
        "Lead nativo sem SLA ou sem perguntas mínimas",
        "Conversão no site sem evento validado",
        "Engajamento indefinido sem ponte remarketing/performance",
    ]
    return [
        {"id": f"ap-{i:02d}", "label": lab, "detectado": False, "nota": ""}
        for i, lab in enumerate(labs, 1)
    ]


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "cliente_projeto": "[Nome]",
            "data_revisao": "YYYY-MM-DD",
            "revisor": "",
            "link_plano_midia": "",
            "link_setup_estrutura": "",
            "link_planilha_growth": "",
            "decisao_humana": "",
        },
        "checklist": build_default_checklist(),
        "anti_padroes": build_default_anti(),
        "subtipos": {
            "lead_nativo": {"aplicavel": False, "checklist_subskill_ok": False},
            "conversao_site": {"aplicavel": False, "checklist_subskill_ok": False},
            "engajamento": {"aplicavel": False, "checklist_subskill_ok": False},
        },
        "gaps_bloqueadores_livre": "",
        "acoes_corretivas": [],
    }


def load(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not data.get("checklist"):
        data["checklist"] = build_default_checklist()
    if not data.get("anti_padroes"):
        data["anti_padroes"] = build_default_anti()
    data.setdefault("subtipos", default_document()["subtipos"])
    data.setdefault("meta", {})
    data.setdefault("gaps_bloqueadores_livre", "")
    data.setdefault("acoes_corretivas", [])
    return data


def summarize_checklist(items: list[dict[str, Any]]) -> tuple[dict[str, dict[str, int]], list[str], list[str]]:
    by_gr: dict[str, dict[str, int]] = defaultdict(
        lambda: {"ok": 0, "na": 0, "gap": 0, "pend": 0}
    )
    pending: list[str] = []
    gaps: list[str] = []
    for it in items:
        if not isinstance(it, dict):
            continue
        st = norm_status(it.get("status"))
        gid = str(it.get("grupo", "?"))
        iid = str(it.get("id", "?"))
        if st is None:
            by_gr[gid]["pend"] += 1
            pending.append(iid)
        elif st == "ok":
            by_gr[gid]["ok"] += 1
        elif st == "na":
            by_gr[gid]["na"] += 1
        else:
            by_gr[gid]["gap"] += 1
            gaps.append(f"{iid}: {it.get('label', '')}")
    return dict(by_gr), pending, gaps


def subtipo_blockers(sub: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for key, lab in (
        ("lead_nativo", "Lead nativo aplicável exige checklist da subskill"),
        ("conversao_site", "Conversão site aplicável exige checklist da subskill"),
        ("engajamento", "Engajamento aplicável exige regra/ponte remarketing (subskill)"),
    ):
        b = sub.get(key) or {}
        if b.get("aplicavel") and not b.get("checklist_subskill_ok"):
            out.append(f"{lab} ({key})")
    return out


def verdict(data: dict[str, Any]) -> tuple[str, list[str]]:
    notes: list[str] = []
    _, pending, gaps = summarize_checklist(data.get("checklist") or [])
    anti_hits = []
    for it in data.get("anti_padroes") or []:
        if isinstance(it, dict) and it.get("detectado") is True:
            anti_hits.append(f"{it.get('id')}: {it.get('label')}")

    st = subtipo_blockers(data.get("subtipos") or {})

    if pending:
        tail = ", ".join(pending[:20]) + ("..." if len(pending) > 20 else "")
        notes.append(f"Pendente: {tail}")
        return "incompleto", notes

    if anti_hits:
        notes.extend(anti_hits)
        return "nao_pronto", notes

    if gaps:
        notes.extend(gaps)
        return "nao_pronto", notes

    if st:
        return "nao_pronto", notes + st

    return "pronto", notes


def render_md(data: dict[str, Any], sug: str, detail_notes: list[str]) -> str:
    m = data.get("meta") or {}
    lines: list[str] = []
    lines.append("# Relatório QA — go-live Meta Ads (playbook 15)\n")
    lines.append(
        f"- **Cliente/projeto:** {m.get('cliente_projeto', '')}\n"
        f"- **Data:** {m.get('data_revisao', '')}\n"
        f"- **Revisor:** {m.get('revisor', '')}\n"
        f"- **Plano mídia:** {m.get('link_plano_midia', '')}\n"
        f"- **Setup:** {m.get('link_setup_estrutura', '')}\n"
    )
    lines.append("## Sugestão automática (revisão humana obrigatória)\n\n")
    lines.append(f"**{sug}**\n")

    if detail_notes:
        lines.append("\n## Detalhes\n")
        for n in detail_notes:
            lines.append(f"- {n}\n")

    by_gr, _, _ = summarize_checklist(data.get("checklist") or [])
    lines.append("\n## Resumo por grupo\n")
    for gr, counts in sorted(by_gr.items()):
        lines.append(
            f"- **{gr}:** ok={counts['ok']} · n.a.={counts['na']} · "
            f"gap={counts['gap']} · pendente={counts['pend']}\n"
        )

    lines.append("\n## Anti-padrões (Seção 16)\n")
    for it in data.get("anti_padroes") or []:
        if not isinstance(it, dict):
            continue
        mark = "DETECTADO" if it.get("detectado") else "não"
        lines.append(f"- [{mark}] {it.get('id')}: {it.get('label')}\n")

    lines.append("\n## Subtipos\n")
    for k, v in (data.get("subtipos") or {}).items():
        if isinstance(v, dict):
            lines.append(
                f"- **{k}:** aplicável={v.get('aplicavel')} · "
                f"checklist OK={v.get('checklist_subskill_ok')}\n"
            )

    gb = data.get("gaps_bloqueadores_livre") or ""
    if gb.strip():
        lines.append("\n## Gaps bloqueadores (livre)\n\n" + gb.strip() + "\n")

    ac = data.get("acoes_corretivas") or []
    if ac:
        lines.append("\n## Ações corretivas\n")
        for x in ac:
            lines.append(f"- {x}\n")

    return "".join(lines)


def suggest_text(v: str) -> str:
    return {
        "pronto": (
            "pronto — sem pendências, sem gap em itens aplicáveis, sem anti-padrão detectado "
            "e subtipos coerentes."
        ),
        "nao_pronto": (
            "não pronto — corrija gaps, anti-padrões ou subtipo antes de ativar verba."
        ),
        "incompleto": (
            "incompleto — preencha cada item do checklist com ok, gap ou n.a. antes do parecer final."
        ),
    }.get(v, v)


def main() -> None:
    parser = argparse.ArgumentParser(description="QA go-live Meta Ads (playbook 15)")
    parser.add_argument("input_json", nargs="?", type=Path, help="checklist-go-live-meta.json")
    parser.add_argument("--md", dest="md_path", type=Path, help="escrever relatório Markdown")
    parser.add_argument("--summary", action="store_true", help="imprimir veredito e contagem")
    parser.add_argument(
        "--write-default",
        dest="out_json",
        type=Path,
        help="gerar JSON template padrão",
    )
    args = parser.parse_args()

    if args.out_json:
        args.out_json.write_text(
            json.dumps(default_document(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Escrito: {args.out_json}")
        return

    if not args.input_json:
        parser.error("informe input_json ou use --write-default")

    data = load(args.input_json)
    v, notes = verdict(data)
    sug = suggest_text(v)

    if args.summary:
        print(f"Veredito: {v}")
        print(sug)
        by_gr, _, _ = summarize_checklist(data.get("checklist") or [])
        for gr, c in sorted(by_gr.items()):
            print(f"  {gr}: {c}")

    if args.md_path:
        args.md_path.write_text(
            render_md(data, sug, notes if v != "pronto" else []),
            encoding="utf-8",
        )

    if not args.summary and not args.md_path:
        print(render_md(data, sug, notes if v != "pronto" else []), end="")


if __name__ == "__main__":
    main()
