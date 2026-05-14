#!/usr/bin/env python3
"""Lê checklist-go-live-google.json, audita status (playbook 16), emite resumo e relatório Markdown."""

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
    def row(gr: str, ref: str, iid: str, lab: str) -> dict[str, Any]:
        return {"grupo": gr, "id": iid, "ref": ref, "label": lab, "status": "", "nota": ""}

    rows: list[dict[str, Any]] = []
    for iid, lab in [
        ("p-01", "Conta e faturamento aptos a rodar verba"),
        ("p-02", "Tag/GA4/GTM e conversões alinhadas ao objetivo de otimização"),
        ("p-03", "Estrutura evita fragmentação excessiva vs orçamento"),
        ("p-04", "Termos, URLs finais e assets coerentes com a oferta"),
        ("p-05", "UTMs e v4_* previstos até backup/CRM"),
        ("p-06", "Hipótese e plano de leitura registrados"),
    ]:
        rows.append(row("principio", "§1", iid, lab))
    for iid, lab in [
        ("c-01", "Conta Google Ads correta"),
        ("c-02", "Faturamento ativo"),
        ("c-03", "Permissões do time conferidas"),
        ("c-04", "Auto-tagging avaliado"),
        ("c-05", "GA4 vinculado quando aplicável"),
        ("c-06", "GTM publicado e tag Google instalada"),
        ("c-07", "Listas remarketing elegíveis quando o plano exige"),
        ("c-08", "Customer Match preparado quando houver base"),
        ("c-09", "Enhanced conversions avaliadas/ativas quando possível"),
    ]:
        rows.append(row("conta", "§4", iid, lab))
    for iid, lab in [
        ("cv-01", "Otimização na conversão mais profunda com volume viável (documentado)"),
        ("cv-02", "Principais vs secundárias/observação diferenciadas quando aplicável"),
        ("cv-03", "Importação offline MQL/SQL/venda planejada quando há CRM"),
    ]:
        rows.append(row("conversoes", "§5", iid, lab))
    for iid, lab in [
        ("g-01", "gclid preservado no fluxo"),
        ("g-02", "gbraid / wbraid quando aplicável"),
        ("g-03", "UTMs preservadas"),
        ("g-04", "v4_client_id, v4_campaign_id, v4_adgroup_id, v4_creative_id, v4_test_id mapeados"),
        ("g-05", "Campos hidden no formulário conforme contrato"),
        ("g-06", "Planilha backup recebendo teste real"),
        ("g-07", "CRM recebe ou há plano de conciliação"),
        ("g-08", "Submissão real de lead testada antes do ar"),
    ]:
        rows.append(row("gtm_dados", "§6", iid, lab))
    for iid, lab in [
        ("n-01", "Campanhas com campaign_id na convenção"),
        ("n-02", "Grupos/asset groups com adgroup_id"),
        ("n-03", "Criativos/anúncios com creative_id"),
    ]:
        rows.append(row("nomenclatura", "§10", iid, lab))
    for iid, lab in [
        ("ng-01", "Lista inicial de negativas aplicável ao escopo"),
        ("ng-02", "Cadência de revisão de termos definida (1ª semana / semanal inicial)"),
    ]:
        rows.append(row("negativas", "§11", iid, lab))
    for iid, lab in [
        ("o-01", "Orçamento compatível com aprendizado"),
        ("o-02", "Sem mudanças grandes/diárias sem evidência"),
        ("o-03", "Estratégia de lance/objetivo documentada para a fase"),
    ]:
        rows.append(row("orcamento", "§12", iid, lab))
    gl = [
        ("gl-01", "Conversões testadas"),
        ("gl-02", "Enhanced conversions avaliadas"),
        ("gl-03", "UTMs e IDs aplicados"),
        ("gl-04", "Lead teste na planilha backup"),
        ("gl-05", "CRM recebeu ou será conciliado"),
        ("gl-06", "Search com negativas iniciais"),
        ("gl-07", "PMax com assets suficientes"),
        ("gl-08", "Audience signals configurados (quando PMax no escopo)"),
        ("gl-09", "Search: clusters, negativas e RSAs conferidos (quando aplicável)"),
        ("gl-10", "PMax: asset groups, URL expansion, brand controls e metas conferidos (quando aplicável)"),
        ("gl-11", "Display: placements/apps, frequência, exclusões e brand safety (quando aplicável)"),
        ("gl-12", "URLs finais conferidas"),
        ("gl-13", "Orçamento, lances e datas conferidos"),
        ("gl-14", "Hipótese na planilha de growth"),
        ("gl-15", "Change log preparado para mudanças relevantes"),
    ]
    for iid, lab in gl:
        rows.append(row("go_live", "§14", iid, lab))
    for iid, lab in [
        ("n2-01", "Conta e faturamento prontos"),
        ("n2-02", "GTM/tag/conversões funcionando"),
        ("n2-03", "UTMs e IDs aplicados"),
        ("n2-04", "Estrutura Search/PMax/Display documentada conforme escopo"),
        ("n2-05", "Públicos/listas/sinais configurados conforme escopo"),
        ("n2-06", "Planilha backup captura lead teste"),
        ("n2-07", "Hipótese e critério de leitura registrados"),
    ]:
        rows.append(row("n2", "§15", iid, lab))
    return rows


def build_default_anti() -> list[dict[str, Any]]:
    labs = [
        "Campanha sem conversão testada",
        "PMax sem asset decente",
        "PMax sem audience signal",
        "Marca e não-marca misturadas sem leitura separada",
        "Otimizar para clique quando o objetivo é lead qualificado",
        "Não importar/evoluir qualidade offline quando o funil exige",
        "Search sem negativas",
        "Alterar budget/lance todo dia sem evidência",
        "Lead sem planilha backup",
        "Avaliar Google só por CPL sem MQL/SQL",
        "Display como sobra de verba sem função, exclusões, frequência ou brand safety",
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
            "search": {"aplicavel": False, "checklist_subskill_ok": False},
            "pmax": {"aplicavel": False, "checklist_subskill_ok": False},
            "display": {"aplicavel": False, "checklist_subskill_ok": False},
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
        ("search", "Search aplicável exige checklist da subskill (setup-google-search-leadgen)"),
        ("pmax", "PMax aplicável exige checklist da subskill (setup-google-pmax-leadgen)"),
        ("display", "Display aplicável exige checklist da subskill (setup-google-display-remarketing)"),
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
        tail = ", ".join(pending[:25]) + ("..." if len(pending) > 25 else "")
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
    lines.append("# Relatório QA — go-live Google Ads (playbook 16)\n")
    lines.append(
        f"- **Cliente/projeto:** {m.get('cliente_projeto', '')}\n"
        f"- **Data:** {m.get('data_revisao', '')}\n"
        f"- **Revisor:** {m.get('revisor', '')}\n"
        f"- **Plano mídia:** {m.get('link_plano_midia', '')}\n"
        f"- **Setup:** {m.get('link_setup_estrutura', '')}\n"
        f"- **Planilha growth/backup:** {m.get('link_planilha_growth', '')}\n"
        f"- **Decisão humana:** {m.get('decisao_humana', '')}\n"
    )
    lines.append("\n## Sugestão automática (revisão humana obrigatória)\n\n")
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

    lines.append("\n## Anti-padrões (Seção 17)\n")
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
    parser = argparse.ArgumentParser(description="QA go-live Google Ads (playbook 16)")
    parser.add_argument("input_json", nargs="?", type=Path, help="checklist-go-live-google.json")
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
