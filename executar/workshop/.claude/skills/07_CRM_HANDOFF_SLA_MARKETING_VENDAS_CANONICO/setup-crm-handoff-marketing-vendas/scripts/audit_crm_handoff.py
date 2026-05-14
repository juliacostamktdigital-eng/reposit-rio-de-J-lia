#!/usr/bin/env python3
"""Audit CRM handoff fields, statuses, SLA and N2 readiness."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "lead_id",
    "created_at",
    "nome",
    "email",
    "telefone",
    "empresa",
    "cargo",
    "segmento",
    "first_utm_source",
    "first_utm_medium",
    "first_utm_campaign",
    "first_utm_content",
    "first_utm_term",
    "last_utm_source",
    "last_utm_medium",
    "last_utm_campaign",
    "last_utm_content",
    "last_utm_term",
    "campaign_id",
    "adgroup_id",
    "creative_id",
    "test_id",
    "lead_status",
    "mql_status",
    "sql_status",
    "opportunity_status",
    "deal_status",
    "lifecycle_stage",
    "sales_owner",
    "assigned_at",
    "first_contact_at",
    "speed_to_lead_minutes",
    "contact_attempts",
    "last_contact_at",
    "next_step",
    "next_step_date",
    "fit_score",
    "intent_score",
    "lead_quality",
    "disqualification_reason",
    "feedback_notes",
    "deal_value",
    "expected_close_date",
    "lost_reason",
    "won_at",
    "lost_at",
]

REQUIRED_STATUSES = {
    "lead_status": ["novo", "atribuido", "contatado", "conectado", "sem-resposta", "qualificado", "desqualificado", "duplicado", "invalido"],
    "mql_status": ["pendente-validacao", "aceito-marketing", "rejeitado-marketing", "enviado-vendas"],
    "sql_status": ["pendente-vendas", "aceito-vendas", "rejeitado-vendas", "em-diagnostico"],
    "opportunity_status": ["aberta", "proposta-enviada", "negociacao", "ganha", "perdida", "sem-fit"],
}

REQUIRED_DISQUALIFICATION = [
    "sem-fit",
    "sem-budget",
    "timing-ruim",
    "nao-responde",
    "fora-regiao",
    "cargo-inadequado",
    "empresa-inadequada",
    "concorrente",
    "estudante",
    "fornecedor",
    "duplicado",
    "dados-invalidos",
    "curioso",
    "ja-cliente",
    "outro",
]

FIELDS = ["tipo", "item", "status", "severidade", "observacao"]


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def as_set(value: Any) -> set[str]:
    if isinstance(value, list):
        return {str(item) for item in value}
    return set()


def audit_fields(payload: dict[str, Any]) -> list[dict[str, str]]:
    existing = as_set(payload.get("campos_existentes", []))
    rows = []
    for field in REQUIRED_FIELDS:
        ok = field in existing
        rows.append({
            "tipo": "campo",
            "item": field,
            "status": "ok" if ok else "faltante",
            "severidade": "alta" if not ok and field in {"first_utm_content", "creative_id", "sales_owner", "disqualification_reason"} else ("media" if not ok else "baixa"),
            "observacao": "" if ok else "campo obrigatório ausente",
        })
    return rows


def audit_statuses(payload: dict[str, Any]) -> list[dict[str, str]]:
    configured = payload.get("status_configurados", {})
    if not isinstance(configured, dict):
        configured = {}
    rows = []
    for group, required_values in REQUIRED_STATUSES.items():
        existing = as_set(configured.get(group, []))
        for value in required_values:
            ok = value in existing
            rows.append({
                "tipo": group,
                "item": value,
                "status": "ok" if ok else "faltante",
                "severidade": "media" if not ok else "baixa",
                "observacao": "" if ok else "status canônico ausente",
            })
    return rows


def audit_disqualification(payload: dict[str, Any]) -> list[dict[str, str]]:
    existing = as_set(payload.get("motivos_desqualificacao", []))
    rows = []
    for reason in REQUIRED_DISQUALIFICATION:
        ok = reason in existing
        rows.append({
            "tipo": "motivo_desqualificacao",
            "item": reason,
            "status": "ok" if ok else "faltante",
            "severidade": "media" if not ok else "baixa",
            "observacao": "" if ok else "motivo fechado ausente",
        })
    return rows


def audit_sla(payload: dict[str, Any]) -> list[dict[str, str]]:
    sla = payload.get("sla", {})
    if not isinstance(sla, dict):
        sla = {}
    checks = {
        "lead_quente_minutos": sla.get("lead_quente_minutos", 999) <= 5,
        "lead_morno_minutos": sla.get("lead_morno_minutos", 999) <= 120,
        "tentativas_primeiro_dia": sla.get("tentativas_primeiro_dia", 0) >= 3,
        "tentativas_7_dias": sla.get("tentativas_7_dias", 0) >= 6,
    }
    return [{
        "tipo": "sla",
        "item": key,
        "status": "ok" if ok else "faltante",
        "severidade": "alta" if not ok else "baixa",
        "observacao": "" if ok else "regra de SLA abaixo do mínimo",
    } for key, ok in checks.items()]


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    return audit_fields(payload) + audit_statuses(payload) + audit_disqualification(payload) + audit_sla(payload)


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def decision(rows: list[dict[str, str]]) -> str:
    high_missing = [row for row in rows if row["status"] == "faltante" and row["severidade"] == "alta"]
    if high_missing:
        return "CRM/handoff ainda não está N2. Corrigir campos/SLA críticos antes do go-live."
    missing = [row for row in rows if row["status"] == "faltante"]
    if missing:
        return "CRM/handoff parcialmente pronto. Pode avançar apenas com plano de correção registrado."
    return "CRM/handoff atende ao checklist operacional N2."


def write_markdown(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    missing = [row for row in rows if row["status"] == "faltante"]
    lines = [
        "# Auditoria CRM Handoff Marketing-Vendas",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- CRM: {payload.get('crm', '')}",
        f"- Decisão: {decision(rows)}",
        "",
        "## Gaps",
        "",
        "| tipo | item | severidade | observacao |",
        "| --- | --- | --- | --- |",
    ]
    for row in missing:
        lines.append("| " + " | ".join(escape_md(row[field]) for field in ["tipo", "item", "severidade", "observacao"]) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit CRM handoff setup against canonical requirements.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    rows = build_rows(payload)
    if not args.md_path and not args.csv_path:
        print(decision(rows))
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
