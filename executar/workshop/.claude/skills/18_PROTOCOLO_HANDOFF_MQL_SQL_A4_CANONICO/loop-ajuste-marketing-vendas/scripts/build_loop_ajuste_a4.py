#!/usr/bin/env python3
"""Loop de ajuste Mkt×Vendas (playbook 18 — passo 5, loop componentes, Gerenciado)."""

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


def norm_faixa(raw: Any) -> str | None:
    if raw is None:
        return None
    t = str(raw).strip().lower()
    if not t:
        return None
    if t in ("verde", "v", "green"):
        return "verde"
    if t in ("amarelo", "a", "ambar", "yellow"):
        return "amarelo"
    if t in ("vermelho", "vm", "red"):
        return "vermelho"
    return None


def filled(v: Any) -> bool:
    if v is None:
        return False
    if isinstance(v, str):
        x = v.strip()
        if not x or x == "[Nome]" or "yyyy" in x.lower():
            return False
        return True
    return bool(v)


def default_kpis() -> list[dict[str, Any]]:
    nomes = [
        "Taxa MQL → SQL",
        "Taxa SQL → venda",
        "Tempo até 1º contato",
        "% rejeições por motivo (resumo)",
        "% leads sem status válido",
    ]
    return [
        {
            "kpi": n,
            "valor": "",
            "faixa": "",
            "threshold_ref": "",
            "nota": "",
        }
        for n in nomes
    ]


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "projeto": "[Nome]",
            "data_rodada": "YYYY-MM-DD",
            "periodo_dados": "",
            "facilitador": "",
            "cadencia": "semanal_operacional",
            "link_protocolo_a4": "",
            "link_plano_midia": "",
            "link_auditoria_aderencia": "",
        },
        "leitura_kpis": default_kpis(),
        "sinais_qualitativos": {
            "rejeicoes_por_motivo_resumo": "",
            "atrasos_sla_resumo": "",
            "feedback_vendas_resumo": "",
        },
        "hipoteses_causa": [
            {"hipotese": "", "evidencia": "", "confianca": ""},
        ],
        "plano_acao": [
            {
                "id": "A01",
                "descricao": "",
                "leva_em": "",
                "faixa_origem": "",
                "kpi_alvo": "",
                "responsavel": "",
                "prazo": "",
                "impacto_esperado": "",
            },
        ],
        "registro": {
            "ata_ou_card": "",
            "changelog_funil_ou_protocolo": "",
            "proxima_revisao": "",
            "justificativa_sem_acao": "",
        },
    }


def _pior_faixa(leitura: list[dict[str, Any]]) -> str | None:
    order = {"verde": 0, "amarelo": 1, "vermelho": 2}
    worst = -1
    name: str | None = None
    for row in leitura:
        if not isinstance(row, dict):
            continue
        fx = norm_faixa(row.get("faixa"))
        if fx is None:
            continue
        if order[fx] > worst:
            worst = order[fx]
            name = fx
    return name


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    sq = d.get("sinais_qualitativos") or {}
    reg = d.get("registro") or {}
    pior = _pior_faixa(d.get("leitura_kpis") or [])

    parts: list[str] = []
    parts.append("# Loop de ajuste — consolidado (A-4)\n\n")
    parts.append("## Cabeçalho\n\n")
    parts.append(
        f"- **Projeto:** {block(m.get('projeto'))}\n"
        f"- **Data rodada:** {block(m.get('data_rodada'))}\n"
        f"- **Período dados:** {block(m.get('periodo_dados'))}\n"
        f"- **Facilitador:** {block(m.get('facilitador'))}\n"
        f"- **Cadência:** {block(m.get('cadencia'))}\n"
        f"- **Protocolo A-4:** {block(m.get('link_protocolo_a4'))}\n"
        f"- **Plano mídia:** {block(m.get('link_plano_midia'))}\n"
        f"- **Auditoria aderência:** {block(m.get('link_auditoria_aderencia'))}\n\n"
    )
    if pior:
        parts.append(f"**Pior faixa observada:** {pior}\n\n")

    parts.append("## 1. Leitura KPIs\n\n")
    for row in d.get("leitura_kpis") or []:
        if isinstance(row, dict):
            parts.append(
                f"- **{block(row.get('kpi'))}:** {block(row.get('valor'))} → "
                f"**{block(row.get('faixa'))}** (ref. threshold: {block(row.get('threshold_ref'))}) — {block(row.get('nota'))}\n"
            )

    parts.append("\n## 2. Sinais qualitativos\n\n")
    parts.append(
        f"- **Rejeições:** {block(sq.get('rejeicoes_por_motivo_resumo'))}\n"
        f"- **SLA/atrasos:** {block(sq.get('atrasos_sla_resumo'))}\n"
        f"- **Feedback vendas:** {block(sq.get('feedback_vendas_resumo'))}\n\n"
    )

    parts.append("## 3. Hipóteses\n\n")
    for h in d.get("hipoteses_causa") or []:
        if isinstance(h, dict) and any(filled(h.get(k)) for k in ("hipotese", "evidencia")):
            parts.append(
                f"- **{block(h.get('hipotese'))}** (conf. {block(h.get('confianca'))}): "
                f"{block(h.get('evidencia'))}\n"
            )

    parts.append("\n## 4. Plano de ação\n\n")
    for a in d.get("plano_acao") or []:
        if isinstance(a, dict):
            parts.append(f"### {block(a.get('id'))}\n\n")
            parts.append(
                f"- **O quê:** {block(a.get('descricao'))}\n"
                f"- **Leva em:** {block(a.get('leva_em'))} · Origem faixa: {block(a.get('faixa_origem'))}\n"
                f"- **KPI alvo:** {block(a.get('kpi_alvo'))}\n"
                f"- **Quem / prazo:** {block(a.get('responsavel'))} · {block(a.get('prazo'))}\n"
                f"- **Impacto esperado:** {block(a.get('impacto_esperado'))}\n\n"
            )

    parts.append("## 5. Registro\n\n")
    parts.append(
        f"- **Ata/card:** {block(reg.get('ata_ou_card'))}\n"
        f"- **Change log:** {block(reg.get('changelog_funil_ou_protocolo'))}\n"
        f"- **Próxima revisão:** {block(reg.get('proxima_revisao'))}\n"
    )
    js = str(reg.get("justificativa_sem_acao") or "").strip()
    if js:
        parts.append(f"\n**Sem ação (justificativa):** {js}\n")
    return "".join(parts)


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    m = d.get("meta") or {}
    if not filled(m.get("projeto")):
        issues.append("meta.projeto")
    if not filled(m.get("periodo_dados")):
        issues.append("meta.periodo_dados")
    if not filled(m.get("link_protocolo_a4")):
        issues.append("meta.link_protocolo_a4")

    cnt = 0
    tem_a = False
    for row in d.get("leitura_kpis") or []:
        if isinstance(row, dict) and norm_faixa(row.get("faixa")) is not None:
            cnt += 1
            fx = norm_faixa(row.get("faixa"))
            if fx in ("amarelo", "vermelho"):
                tem_a = True

    if cnt < 3:
        issues.append("leitura_kpis: ≥3 linhas com faixa (verde/amarelo/vermelho)")

    precisa_acao = tem_a or tem_v
    reg = d.get("registro") or {}
    just = str(reg.get("justificativa_sem_acao") or "").strip()

    acoes_ok = 0
    for a in d.get("plano_acao") or []:
        if isinstance(a, dict) and filled(a.get("descricao")) and filled(a.get("responsavel")):
            acoes_ok += 1

    if precisa_acao and acoes_ok < 1 and not filled(just):
        issues.append("plano_acao: ≥1 ação com descricao+responsavel OU registro.justificativa_sem_acao")

    if acoes_ok >= 1:
        if not filled(reg.get("ata_ou_card")) and not filled(reg.get("changelog_funil_ou_protocolo")):
            issues.append("registro: preencher ata_ou_card ou changelog após definir ações")

    if not filled(reg.get("proxima_revisao")):
        issues.append("(aviso) registro.proxima_revisao")

    return issues


def main() -> None:
    p = argparse.ArgumentParser(description="Loop ajuste A-4 (playbook 18)")
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
        print("Lacunas / avisos (loop ajuste A-4):")
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
