#!/usr/bin/env python3
"""Compara parametros esperados (URL) vs capturados (5 saltos: URL -> LP -> form -> backup -> CRM -> analise).

Inclui:
- validacao dos 5 saltos com identificacao de gap por salto;
- deteccao de dedup CAPI (event_id browser vs server, event_name, delta de tempo);
- classificacao automatica de severidade por padroes conhecidos;
- decisao formal codificada (go / go-com-risco / no-go / retestar) com plano de correcao;
- backwards-compat: JSON antigo (apenas backup/crm/rules) continua funcionando.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse


FIELDS = [
    "camada",
    "campo",
    "esperado",
    "capturado",
    "status",
    "severidade",
    "codigo",
]

REQUIRED_FIELDS = [
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_content",
    "utm_term",
    "v4_client_id",
    "v4_campaign_id",
    "v4_adgroup_id",
    "v4_creative_id",
    "v4_test_id",
]

CLICK_IDS = ["gclid", "gbraid", "wbraid", "fbclid", "_fbp", "_fbc", "ttclid", "li_fat_id", "msclkid"]

RULE_LABELS = {
    "first_touch_preserved": "First-touch preservado",
    "last_touch_updates": "Last-touch atualiza",
    "dedupe_ok": "Dedupe ok",
    "conversion_event_ok": "Evento de conversao ok",
    "export_match_ok": "Export permite match",
}

EXPECTED_SALTOS = [
    "1_url_para_lp",
    "2_lp_para_form",
    "3_form_para_backup",
    "4_backup_para_crm",
    "5_crm_para_analise",
]


# ---------------------------------------------------------------------------
# Classificacao automatica de severidade por padrao conhecido
# ---------------------------------------------------------------------------

def classify_severity(field: str, expected: str, captured: str) -> str:
    """Classifica severidade quando campo tem padrao conhecido."""
    if expected == captured:
        return "baixo"
    # v4_* IDs sao bloqueadores: sem eles o cruzamento de criativo/campanha quebra
    if field.startswith("v4_"):
        return "bloqueador"
    # utm_content carrega creative_id em texto: bloqueador para leitura de criativo
    if field == "utm_content":
        return "bloqueador"
    # click IDs perdidos -> alto (perde dedup CAPI / Enhanced Conversions)
    if field in CLICK_IDS:
        return "alto"
    # utm_source/medium/campaign perdidos -> alto
    if field in ("utm_source", "utm_medium", "utm_campaign"):
        return "alto"
    # demais (utm_term) -> medio
    return "medio"


def code_for(severity: str, counter: dict[str, int]) -> str:
    counter[severity] = counter.get(severity, 0) + 1
    return f"{severity}-N{counter[severity]}"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_url_params(url: str) -> dict[str, str]:
    parsed = urlparse(url)
    values = parse_qs(parsed.query)
    return {key: value[0] for key, value in values.items() if value}


def compare_layer(
    expected: dict[str, str],
    captured: dict[str, Any],
    layer: str,
    counter: dict[str, int],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for field in REQUIRED_FIELDS:
        expected_value = expected.get(field, "")
        captured_value = str(captured.get(field, "")).strip()
        ok = expected_value == captured_value
        severity = "baixo" if ok else classify_severity(field, expected_value, captured_value)
        rows.append({
            "camada": layer,
            "campo": field,
            "esperado": expected_value,
            "capturado": captured_value,
            "status": "ok" if ok else "erro",
            "severidade": severity,
            "codigo": "" if ok else code_for(severity, counter),
        })
    return rows


def compare_rules(rules: dict[str, Any], counter: dict[str, int]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for field, label in RULE_LABELS.items():
        value = bool(rules.get(field))
        rows.append({
            "camada": "rules",
            "campo": label,
            "esperado": "true",
            "capturado": str(value).lower(),
            "status": "ok" if value else "erro",
            "severidade": "baixo" if value else "bloqueador",
            "codigo": "" if value else code_for("bloqueador", counter),
        })
    return rows


def compare_saltos(saltos: list[dict[str, Any]], counter: dict[str, int]) -> list[dict[str, str]]:
    """Valida os 5 saltos. Cada salto compara campos_esperados vs campos_capturados."""
    rows: list[dict[str, str]] = []
    seen = {s.get("nome", ""): s for s in saltos}
    for salto_nome in EXPECTED_SALTOS:
        salto = seen.get(salto_nome)
        if salto is None:
            # Backwards-compat: JSON antigo nao tinha saltos 4 e 5 explicitos -> warning
            rows.append({
                "camada": f"salto:{salto_nome}",
                "campo": "_presenca_salto",
                "esperado": "presente",
                "capturado": "ausente",
                "status": "warning",
                "severidade": "medio",
                "codigo": code_for("medio", counter),
            })
            continue
        esperados = salto.get("campos_esperados", {}) or {}
        capturados = salto.get("campos_capturados", {}) or {}
        for campo, esp in esperados.items():
            cap = capturados.get(campo)
            esp_str = str(esp)
            cap_str = "" if cap is None else str(cap)
            ok = esp_str == cap_str
            severity = "baixo" if ok else classify_severity(campo, esp_str, cap_str)
            rows.append({
                "camada": f"salto:{salto_nome}",
                "campo": campo,
                "esperado": esp_str,
                "capturado": cap_str,
                "status": "ok" if ok else "erro",
                "severidade": severity,
                "codigo": "" if ok else code_for(severity, counter),
            })
    return rows


def compare_dedup_capi(dedup: dict[str, Any], counter: dict[str, int]) -> list[dict[str, str]]:
    """Detecta divergencia em dedup CAPI."""
    rows: list[dict[str, str]] = []
    if not dedup:
        return rows

    eid_browser = str(dedup.get("event_id_browser", "")).strip()
    eid_server = str(dedup.get("event_id_server", "")).strip()
    en_browser = str(dedup.get("event_name_browser", "")).strip()
    en_server = str(dedup.get("event_name_server", "")).strip()
    delta = dedup.get("event_time_delta_seconds")
    dedup_status = str(dedup.get("deduplicated_status", "")).strip().lower()
    emq = dedup.get("emq_score")

    # event_id identico
    eid_ok = bool(eid_browser) and eid_browser == eid_server
    rows.append({
        "camada": "dedup_capi",
        "campo": "event_id_browser_eq_server",
        "esperado": eid_browser or "<uuid v4>",
        "capturado": eid_server,
        "status": "ok" if eid_ok else "erro",
        "severidade": "baixo" if eid_ok else "bloqueador",
        "codigo": "" if eid_ok else code_for("bloqueador", counter),
    })

    # event_name identico
    en_ok = bool(en_browser) and en_browser == en_server
    rows.append({
        "camada": "dedup_capi",
        "campo": "event_name_identico",
        "esperado": en_browser or "Lead",
        "capturado": en_server,
        "status": "ok" if en_ok else "erro",
        "severidade": "baixo" if en_ok else "alto",
        "codigo": "" if en_ok else code_for("alto", counter),
    })

    # delta de tempo < 60s
    if delta is not None:
        try:
            delta_val = float(delta)
            delta_ok = delta_val < 60
        except (TypeError, ValueError):
            delta_ok = False
        rows.append({
            "camada": "dedup_capi",
            "campo": "event_time_delta_lt_60s",
            "esperado": "< 60",
            "capturado": str(delta),
            "status": "ok" if delta_ok else "warning",
            "severidade": "baixo" if delta_ok else "alto",
            "codigo": "" if delta_ok else code_for("alto", counter),
        })

    # status Deduplicated Yes
    dedup_ok = dedup_status in ("yes", "true", "deduplicated")
    rows.append({
        "camada": "dedup_capi",
        "campo": "deduplicated_status",
        "esperado": "Yes",
        "capturado": dedup_status or "",
        "status": "ok" if dedup_ok else "erro",
        "severidade": "baixo" if dedup_ok else "bloqueador",
        "codigo": "" if dedup_ok else code_for("bloqueador", counter),
    })

    # EMQ >= 7.0
    if emq is not None:
        try:
            emq_ok = float(emq) >= 7.0
        except (TypeError, ValueError):
            emq_ok = False
        rows.append({
            "camada": "dedup_capi",
            "campo": "emq_score_gte_7",
            "esperado": ">= 7.0",
            "capturado": str(emq),
            "status": "ok" if emq_ok else "warning",
            "severidade": "baixo" if emq_ok else "medio",
            "codigo": "" if emq_ok else code_for("medio", counter),
        })

    return rows


def compare_lead_teste(lead_teste: dict[str, Any], counter: dict[str, int]) -> list[dict[str, str]]:
    """Valida convencao de lead teste."""
    rows: list[dict[str, str]] = []
    if not lead_teste:
        return rows

    is_test = bool(lead_teste.get("is_test"))
    rows.append({
        "camada": "lead_teste",
        "campo": "is_test_flag",
        "esperado": "true",
        "capturado": str(is_test).lower(),
        "status": "ok" if is_test else "erro",
        "severidade": "baixo" if is_test else "bloqueador",
        "codigo": "" if is_test else code_for("bloqueador", counter),
    })

    excl_meta = bool(lead_teste.get("exclusao_audiences_meta"))
    excl_google = bool(lead_teste.get("exclusao_customer_match_google"))
    excl_bi = bool(lead_teste.get("exclusao_dashboards_bi"))
    for label, value in [
        ("exclusao_audiences_meta", excl_meta),
        ("exclusao_customer_match_google", excl_google),
        ("exclusao_dashboards_bi", excl_bi),
    ]:
        rows.append({
            "camada": "lead_teste",
            "campo": label,
            "esperado": "true",
            "capturado": str(value).lower(),
            "status": "ok" if value else "warning",
            "severidade": "baixo" if value else "alto",
            "codigo": "" if value else code_for("alto", counter),
        })

    email_pattern = str(lead_teste.get("email_pattern", "")).strip()
    pattern_ok = email_pattern.startswith("qa+") and "{timestamp}" in email_pattern and "@" in email_pattern
    rows.append({
        "camada": "lead_teste",
        "campo": "email_pattern_qa_timestamp",
        "esperado": "qa+{timestamp}@dominio",
        "capturado": email_pattern,
        "status": "ok" if pattern_ok else "warning",
        "severidade": "baixo" if pattern_ok else "medio",
        "codigo": "" if pattern_ok else code_for("medio", counter),
    })

    return rows


def compare_dark_traffic(gap: dict[str, Any]) -> list[dict[str, str]]:
    """Anota dark traffic como informacao (nao gera severidade automatica, so observacao)."""
    rows: list[dict[str, str]] = []
    if not gap:
        return rows
    pct = gap.get("gap_percentual")
    try:
        pct_val = float(pct) if pct is not None else None
    except (TypeError, ValueError):
        pct_val = None
    if pct_val is None:
        avaliacao = "indeterminado"
        severity = "medio"
    elif pct_val < 0.15:
        avaliacao = "saudavel"
        severity = "baixo"
    elif pct_val < 0.40:
        avaliacao = "atencao"
        severity = "medio"
    else:
        avaliacao = "alto-gap"
        severity = "alto"
    rows.append({
        "camada": "dark_traffic",
        "campo": "gap_percentual",
        "esperado": "< 0.15 (saudavel)",
        "capturado": f"{pct_val:.4f}" if pct_val is not None else "",
        "status": "ok" if severity == "baixo" else "warning",
        "severidade": severity,
        "codigo": "",
    })
    rows.append({
        "camada": "dark_traffic",
        "campo": "avaliacao",
        "esperado": "saudavel",
        "capturado": avaliacao,
        "status": "ok" if avaliacao == "saudavel" else "warning",
        "severidade": severity,
        "codigo": "",
    })
    return rows


# ---------------------------------------------------------------------------
# Decisao formal
# ---------------------------------------------------------------------------

def decision(rows: list[dict[str, str]]) -> str:
    bad = [row for row in rows if row["status"] != "ok"]
    severities = [row["severidade"] for row in bad]
    bloq = severities.count("bloqueador")
    alto = severities.count("alto")
    if bloq >= 1:
        return "no-go"
    if alto > 2:
        return "no-go"
    if alto >= 1:
        return "go-com-risco"
    if "medio" in severities:
        return "go-com-risco"
    return "go"


def correction_plan(achados: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Normaliza plano de correcao (achados) com campos obrigatorios."""
    plan: list[dict[str, Any]] = []
    for ach in achados or []:
        plan.append({
            "codigo": ach.get("codigo", ""),
            "descricao": ach.get("descricao", ""),
            "salto": ach.get("salto", ""),
            "dono": ach.get("dono", ""),
            "esforco": ach.get("esforco", ""),
            "bloqueia_golive": bool(ach.get("bloqueia_golive", False)),
            "mitigacao": ach.get("mitigacao", ""),
            "prazo": ach.get("prazo", ""),
        })
    return plan


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------

def load_rows(path: Path) -> tuple[list[dict[str, str]], dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    url = str(payload.get("url", "")).strip()
    if not url:
        raise ValueError("JSON deve conter 'url'.")
    expected = parse_url_params(url)
    missing = [field for field in REQUIRED_FIELDS if field not in expected]
    if missing:
        raise ValueError(f"URL nao tem todos os params obrigatorios: {', '.join(missing)}")

    counter: dict[str, int] = {}
    rows: list[dict[str, str]] = []

    # Lead teste (novo)
    rows.extend(compare_lead_teste(payload.get("lead_teste", {}) or {}, counter))

    # Saltos (novo) - se existir; senao backwards-compat usando backup/crm
    saltos = payload.get("saltos")
    if saltos:
        rows.extend(compare_saltos(saltos, counter))
    else:
        # Backwards-compat: JSON antigo so tem backup/crm/rules.
        # Saltos 1-3 ausentes -> warning medio. Backup -> salto 3->4. CRM -> salto 4->5.
        for salto_nome in ("1_url_para_lp", "2_lp_para_form", "3_form_para_backup"):
            rows.append({
                "camada": f"salto:{salto_nome}",
                "campo": "_presenca_salto",
                "esperado": "presente",
                "capturado": "ausente (json schema 1.0)",
                "status": "warning",
                "severidade": "medio",
                "codigo": code_for("medio", counter),
            })

    # Backup e CRM (compat com schema 1.0; tambem complementa schema 2.0)
    rows.extend(compare_layer(expected, payload.get("backup", {}) or {}, "backup", counter))
    rows.extend(compare_layer(expected, payload.get("crm", {}) or {}, "crm", counter))

    # Rules
    rows.extend(compare_rules(payload.get("rules", {}) or {}, counter))

    # Dedup CAPI (novo)
    rows.extend(compare_dedup_capi(payload.get("dedup_capi", {}) or {}, counter))

    # Dark traffic (novo, informativo)
    rows.extend(compare_dark_traffic(payload.get("dark_traffic_gap", {}) or {}))

    return rows, payload


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(rows: list[dict[str, str]], payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    decisao_payload = payload.get("decisao", {}) or {}
    decisao_valor = decisao_payload.get("valor") or decision(rows)
    decisao_calculada = decision(rows)
    achados = correction_plan(payload.get("achados", []) or [])
    dark = payload.get("dark_traffic_gap", {}) or {}
    dedup = payload.get("dedup_capi", {}) or {}
    lead_teste = payload.get("lead_teste", {}) or {}

    lines = [
        "# QA Tracking UTM CRM",
        "",
        "## Decisao Formal Codificada",
        "",
        f"- Decisao declarada: `{decisao_valor}`",
        f"- Decisao calculada (auto): `{decisao_calculada}`",
    ]
    if decisao_payload.get("justificativa"):
        lines.append(f"- Justificativa: {decisao_payload['justificativa']}")
    if decisao_payload.get("aceite_escrito_operador"):
        lines.append(f"- Aceite escrito do operador: {decisao_payload['aceite_escrito_operador']}")
    cond = decisao_payload.get("condicoes_golive") or []
    if cond:
        lines.append("- Condicoes para go-live:")
        for c in cond:
            lines.append(f"  - {c}")

    # Lead teste
    if lead_teste:
        lines.extend([
            "",
            "## Lead Teste",
            f"- Email pattern: `{lead_teste.get('email_pattern', '')}`",
            f"- Exemplo: `{lead_teste.get('email_exemplo', '')}`",
            f"- is_test: `{lead_teste.get('is_test', False)}`",
            f"- Exclusao audiences Meta: `{lead_teste.get('exclusao_audiences_meta', False)}`",
            f"- Exclusao Customer Match Google: `{lead_teste.get('exclusao_customer_match_google', False)}`",
            f"- Exclusao dashboards BI: `{lead_teste.get('exclusao_dashboards_bi', False)}`",
        ])

    # Dedup CAPI
    if dedup:
        lines.extend([
            "",
            "## Dedup CAPI",
            f"- event_id browser: `{dedup.get('event_id_browser', '')}`",
            f"- event_id server: `{dedup.get('event_id_server', '')}`",
            f"- Identicos: `{dedup.get('event_id_browser') == dedup.get('event_id_server') and bool(dedup.get('event_id_browser'))}`",
            f"- Status Deduplicated: `{dedup.get('deduplicated_status', '')}`",
            f"- EMQ score: `{dedup.get('emq_score', '')}`",
        ])

    # Dark traffic
    if dark:
        pct = dark.get("gap_percentual")
        pct_str = f"{pct*100:.2f}%" if isinstance(pct, (int, float)) else str(pct)
        lines.extend([
            "",
            "## Dark Traffic Gap",
            f"- Periodo: {dark.get('periodo', '')}",
            f"- Leads CRM: {dark.get('leads_crm', '')}",
            f"- Leads Meta: {dark.get('leads_plataforma_meta', '')}",
            f"- Leads Google: {dark.get('leads_plataforma_google', '')}",
            f"- Gap absoluto: {dark.get('gap_absoluto', '')}",
            f"- Gap percentual: {pct_str}",
            f"- Avaliacao: `{dark.get('avaliacao', '')}`",
        ])

    # Plano de correcao
    if achados:
        lines.extend([
            "",
            "## Plano De Correcao",
            "",
            "| Codigo | Descricao | Salto | Dono | Esforco | Bloqueia go-live | Mitigacao | Prazo |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ])
        for ach in achados:
            lines.append(
                "| "
                + " | ".join(
                    escape_md(str(ach[k])) for k in [
                        "codigo", "descricao", "salto", "dono", "esforco",
                        "bloqueia_golive", "mitigacao", "prazo",
                    ]
                )
                + " |"
            )

    # Tabela de gaps
    lines.extend([
        "",
        "## Comparacao Esperado vs Capturado",
        "",
        "| " + " | ".join(FIELDS) + " |",
        "| " + " | ".join("---" for _ in FIELDS) + " |",
    ])
    for row in rows:
        lines.append("| " + " | ".join(escape_md(str(row.get(field, ""))) for field in FIELDS) + " |")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compara params da URL vs capturas de backup/CRM/saltos/dedup CAPI/dark traffic."
    )
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    rows, payload = load_rows(args.input_json)
    if not args.md_path and not args.csv_path:
        print(decision(rows))
        return
    if args.md_path:
        write_markdown(rows, payload, args.md_path)
    if args.csv_path:
        write_csv(rows, args.csv_path)


if __name__ == "__main__":
    main()
