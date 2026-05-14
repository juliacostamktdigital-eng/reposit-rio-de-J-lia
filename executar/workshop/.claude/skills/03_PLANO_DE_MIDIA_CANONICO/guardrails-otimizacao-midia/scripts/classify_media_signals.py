#!/usr/bin/env python3
"""Classify media optimization signals using canonical guardrails."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


RULES = {
    "cpl_alto_cpmql_saudavel": {
        "severidade": "media",
        "acao": "manter ou ajustar com cautela",
        "racional": "CPL alto nao justifica pausa se MQL/SQL estao saudaveis.",
        "risco": "Matar uma fonte cara, mas qualificada.",
    },
    "cpl_baixo_mql_baixo": {
        "severidade": "alta",
        "acao": "revisar publico, promessa ou formulario",
        "racional": "Lead barato sem qualidade deteriora o funil.",
        "risco": "Escalar volume ruim.",
    },
    "lead_bom_sql_baixo": {
        "severidade": "alta",
        "acao": "revisar SLA e handoff comercial",
        "racional": "Gargalo pode estar depois do MQL.",
        "risco": "Cortar midia que gera lead correto.",
    },
    "gasto_zero_evento": {
        "severidade": "critica",
        "acao": "investigar tracking antes de otimizar",
        "racional": "Sem evento confiavel, a leitura de midia esta invalida.",
        "risco": "Otimizar em cima de dado quebrado.",
    },
    "ctr_alto_conversao_baixa": {
        "severidade": "alta",
        "acao": "revisar LP, oferta e coerencia anuncio-pagina",
        "racional": "Criativo atrai clique, mas a conversao quebra depois.",
        "risco": "Trocar criativo quando o problema e a experiencia.",
    },
    "ctr_baixo_mql_bom": {
        "severidade": "media",
        "acao": "testar variacao de hook/formato",
        "racional": "Baixo clique com boa qualidade sugere problema de escala criativa.",
        "risco": "Matar aprendizagem qualificada cedo demais.",
    },
    "lp_views_abaixo_cliques": {
        "severidade": "alta",
        "acao": "investigar velocidade, tracking e mobile",
        "racional": "Queda entre clique e LP view aponta problema tecnico ou experiencia.",
        "risco": "Culpar publico/criativo por falha de pagina.",
    },
    "previsto_diverge_realizado": {
        "severidade": "media",
        "acao": "recalcular projecao antes de prometer acumulado",
        "racional": "Plano precisa refletir realizado por lote ou semana.",
        "risco": "Manter promessa financeira desatualizada.",
    },
}

FIELDS = [
    "sinal",
    "evidencia",
    "severidade",
    "acao",
    "racional",
    "risco",
    "tracking_confiavel",
    "volume_minimo",
    "changelog_obrigatorio",
]


def truthy(value: str) -> bool:
    return value.strip().lower() in {"true", "sim", "yes", "1"}


def classify(row: dict[str, str]) -> dict[str, str]:
    signal = row.get("sinal", "").strip()
    rule = RULES.get(signal, {
        "severidade": "baixa",
        "acao": "monitorar e qualificar sinal",
        "racional": "Sinal nao mapeado nos guardrails canonicos.",
        "risco": "Tomar decisao sem regra explicita.",
    })
    tracking_ok = truthy(row.get("tracking_confiavel", ""))
    volume_ok = truthy(row.get("volume_minimo", ""))
    severity = rule["severidade"]
    action = rule["acao"]
    if not tracking_ok:
        severity = "critica"
        action = "validar tracking antes de qualquer decisao de midia"
    elif not volume_ok and severity != "critica":
        action = f"{action}; aguardar volume minimo para decisao final"
    return {
        "sinal": signal,
        "evidencia": row.get("evidencia", ""),
        "severidade": severity,
        "acao": action,
        "racional": rule["racional"],
        "risco": rule["risco"],
        "tracking_confiavel": str(tracking_ok).lower(),
        "volume_minimo": str(volume_ok).lower(),
        "changelog_obrigatorio": "true" if severity in {"critica", "alta"} else "avaliar",
    }


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["sinal", "severidade", "acao", "risco", "changelog_obrigatorio"]
    lines = [
        "# Guardrails De Otimizacao De Midia",
        "",
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify media optimization signals.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    args = parser.parse_args()

    rows = [classify(row) for row in read_rows(args.input_csv)]
    if not args.csv_path and not args.md_path:
        for row in rows:
            print(f"{row['sinal']}: {row['severidade']} -> {row['acao']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, rows)


if __name__ == "__main__":
    main()
