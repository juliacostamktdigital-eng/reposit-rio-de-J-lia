#!/usr/bin/env python3
"""Prioritize AI-native automation opportunities."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "prioridade",
    "score",
    "cliente",
    "etapa",
    "tarefa",
    "input",
    "output",
    "ferramenta",
    "nivel_atual",
    "nivel_desejado",
    "frequencia",
    "esforco_manual",
    "impacto",
    "risco",
    "dono",
    "evidencia",
    "proximo_passo",
    "decisao",
]

SCORES = {
    "frequencia": {"alta": 30, "media": 20, "média": 20, "baixa": 10},
    "esforco_manual": {"alto": 30, "medio": 20, "médio": 20, "baixo": 10},
    "impacto": {"alto": 35, "medio": 20, "médio": 20, "baixo": 10},
    "risco": {"baixo": 0, "medio": -15, "médio": -15, "alto": -35},
}


def normalized(value: Any) -> str:
    return str(value or "").strip().lower()


def default_payload() -> dict[str, Any]:
    return {
        "cliente": "[Nome]",
        "responsavel": "",
        "tarefas": [
            {
                "etapa": "",
                "tarefa": "",
                "input": "",
                "output": "",
                "ferramenta": "",
                "nivel_atual": "manual",
                "nivel_desejado": "assistido",
                "frequencia": "media",
                "esforco_manual": "medio",
                "impacto": "medio",
                "risco": "medio",
                "dono": "",
                "evidencia": "",
                "proximo_passo": "",
            }
        ],
    }


def audit_payload(payload: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    c = str(payload.get("cliente", "")).strip()
    if not c or c == "[Nome]":
        issues.append("cliente")
    if not str(payload.get("responsavel", "")).strip():
        issues.append("responsavel")
    tasks = payload.get("tarefas")
    if not isinstance(tasks, list) or len(tasks) == 0:
        issues.append("tarefas: lista vazia")
        return issues
    req = (
        "etapa",
        "tarefa",
        "input",
        "output",
        "ferramenta",
        "nivel_atual",
        "nivel_desejado",
        "risco",
        "dono",
        "evidencia",
        "proximo_passo",
    )
    any_started = False
    for i, t in enumerate(tasks, 1):
        if not isinstance(t, dict):
            continue
        if not str(t.get("tarefa", "")).strip() and not str(t.get("etapa", "")).strip():
            continue
        any_started = True
        pr = f"tarefas[{i}]"
        for k in req:
            if not str(t.get(k, "")).strip():
                issues.append(f"{pr}.{k}")
    if not any_started:
        issues.append("tarefas: nenhuma linha com etapa/tarefa preenchida")
    return issues


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def score_task(task: dict[str, Any]) -> int:
    score = 0
    for field, values in SCORES.items():
        score += values.get(normalized(task.get(field)), 0)
    if not str(task.get("dono", "")).strip():
        score -= 20
    if not str(task.get("input", "")).strip() or not str(task.get("output", "")).strip():
        score -= 25
    return score


def decision(task: dict[str, Any], score: int) -> str:
    risk = normalized(task.get("risco"))
    desired = normalized(task.get("nivel_desejado"))
    if risk == "alto" and desired == "automatico":
        return "bloquear_automacao_total"
    if score >= 70:
        return "priorizar_agora"
    if score >= 45:
        return "planejar"
    if risk == "alto":
        return "manter_assistido"
    return "monitorar"


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    tasks = payload.get("tarefas", [])
    if not isinstance(tasks, list):
        raise ValueError("'tarefas' must be a list.")
    rows: list[dict[str, str]] = []
    for task in tasks:
        if not isinstance(task, dict):
            continue
        score = score_task(task)
        rows.append({
            "prioridade": "",
            "score": str(score),
            "cliente": str(payload.get("cliente", "")),
            "etapa": str(task.get("etapa", "")),
            "tarefa": str(task.get("tarefa", "")),
            "input": str(task.get("input", "")),
            "output": str(task.get("output", "")),
            "ferramenta": str(task.get("ferramenta", "")),
            "nivel_atual": str(task.get("nivel_atual", "")),
            "nivel_desejado": str(task.get("nivel_desejado", "")),
            "frequencia": str(task.get("frequencia", "")),
            "esforco_manual": str(task.get("esforco_manual", "")),
            "impacto": str(task.get("impacto", "")),
            "risco": str(task.get("risco", "")),
            "dono": str(task.get("dono", "")),
            "evidencia": str(task.get("evidencia", "")),
            "proximo_passo": str(task.get("proximo_passo", "")),
            "decisao": decision(task, score),
        })
    rows.sort(key=lambda row: int(row["score"]), reverse=True)
    for index, row in enumerate(rows, start=1):
        row["prioridade"] = str(index)
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["prioridade", "etapa", "tarefa", "nivel_atual", "nivel_desejado", "risco", "decisao", "proximo_passo"]
    lines = [
        "# Plano De Automação AI-Native",
        "",
        f"- Cliente/operação: {payload.get('cliente', '')}",
        f"- Responsável: {payload.get('responsavel', '')}",
        "",
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join("---" for _ in fields) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in fields) + " |")
    blocked = [row for row in rows if row["decisao"] == "bloquear_automacao_total"]
    if blocked:
        lines.extend(["", "## Bloqueios De Automação Total", ""])
        for row in blocked:
            lines.append(f"- {row['tarefa']}: risco {row['risco']}; manter revisão humana.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prioritize AI-native automation opportunities.")
    parser.add_argument("input_json", nargs="?", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--write-default", dest="out_json", type=Path)
    args = parser.parse_args()

    if args.out_json:
        args.out_json.write_text(
            json.dumps(default_payload(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Escrito: {args.out_json}")
        return

    if not args.input_json:
        parser.error("informe input_json ou --write-default")

    payload = load_payload(args.input_json)
    if args.audit:
        xs = audit_payload(payload)
        print("Lacunas (plano automação — playbook 06 §2.20):")
        if not xs:
            print("  (nenhuma lacuna estrutural)")
        else:
            for x in xs:
                print(f"  - {x}")
        return

    rows = build_rows(payload)
    if not args.md_path and not args.csv_path:
        for row in rows:
            print(f"{row['prioridade']}. {row['tarefa']} -> {row['decisao']}")
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
