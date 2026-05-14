#!/usr/bin/env python3
"""Audit marketing to CRM data contract coverage.

Schema v2: 8 camadas + dicionario de 22 campos por classe LGPD + dedup CAPI
+ Consent Mode v2 granular. Backwards-compat com v1 (6 camadas, sem
dicionario_campos / regras_match / lgpd_compliance) -- nao quebra na leitura,
apenas pula as validacoes novas.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = {
    "lead_id",
    "first_utm_source",
    "first_utm_medium",
    "first_utm_campaign",
    "last_utm_source",
    "last_utm_medium",
    "last_utm_campaign",
    "v4_client_id",
    "v4_campaign_id",
    "v4_adgroup_id",
    "v4_creative_id",
    "v4_test_id",
}

REQUIRED_N2 = [
    "backup_padronizado",
    "utms_chegam_conversao",
    "ids_chegam_planilha",
    "crm_recebe_origem_ou_match",
    "first_last_touch_preservados",
    "dicionario_dados_existe",
    "teste_ponta_a_ponta_existe",
    "analise_pos_campanha_possivel",
]

# Schema v2: 22 campos esperados por classe LGPD.
DICIONARIO_22_CAMPOS = {
    "pii_bruto": ["email_raw", "phone_raw", "nome_raw"],
    "pii_hash": [
        "email_sha256",
        "phone_e164",
        "phone_sha256",
        "first_name_sha256",
        "user_id",
    ],
    "id_tecnico": [
        "event_id",
        "session_id",
        "client_id",
        "lead_id",
        "cf_lead_id",
    ],
    "metadata_marketing": [
        "gclid",
        "fbclid",
        "wbraid",
        "gbraid",
        "fbp",
        "fbc",
        "ttclid",
        "li_fat_id",
        "first_touch_source",
        "last_touch_source",
    ],
    "consent": [
        "consent_analytics",
        "consent_ads",
        "consent_ad_user_data",
        "consent_ad_personalization",
    ],
}

PII_RAW_PROIBIDO_EM_PLATAFORMA = {"email_raw", "phone_raw", "nome_raw"}
PLATAFORMAS_MIDIA = {"Meta", "Google_Ads", "TikTok", "LinkedIn"}


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_v2(payload: dict[str, Any]) -> bool:
    """Detecta se o payload segue schema v2."""
    if str(payload.get("schema_version", "")).strip().lower() == "v2":
        return True
    return any(
        key in payload
        for key in ("dicionario_campos", "regras_match", "lgpd_compliance")
    )


def field_names(payload: dict[str, Any]) -> set[str]:
    fields = payload.get("campos", [])
    if not isinstance(fields, list):
        raise ValueError("'campos' must be a list.")
    return {str(item.get("campo", "")).strip() for item in fields if isinstance(item, dict)}


def dicionario_field_names(payload: dict[str, Any]) -> set[str]:
    """Coleta nomes de campos do bloco dicionario_campos (v2), por classe."""
    dicio = payload.get("dicionario_campos", {})
    if not isinstance(dicio, dict):
        return set()
    names: set[str] = set()
    for classe_lista in dicio.values():
        if isinstance(classe_lista, list):
            for item in classe_lista:
                if isinstance(item, dict):
                    nome = str(item.get("campo", "")).strip()
                    if nome:
                        names.add(nome)
    return names


def audit(payload: dict[str, Any]) -> list[dict[str, str]]:
    names = field_names(payload)
    n2 = payload.get("criterios_n2", {})
    if not isinstance(n2, dict):
        n2 = {}
    rows: list[dict[str, str]] = []

    # Validacao v1 (campos obrigatorios) -- mantida pra backwards-compat.
    for field in sorted(REQUIRED_FIELDS):
        rows.append({
            "tipo": "campo",
            "item": field,
            "status": "ok" if field in names else "gap",
            "severidade": "alta" if field not in names else "ok",
            "acao": "Adicionar ao dicionario e ao fluxo form/backup/CRM." if field not in names else "Manter.",
        })

    for criterion in REQUIRED_N2:
        ok = bool(n2.get(criterion))
        rows.append({
            "tipo": "criterio_n2",
            "item": criterion,
            "status": "ok" if ok else "gap",
            "severidade": "critica" if not ok else "ok",
            "acao": "Resolver antes de considerar contrato N2." if not ok else "Manter evidencia.",
        })

    # Validacao v2 (so roda se schema v2).
    if is_v2(payload):
        rows.extend(audit_v2(payload))
    return rows


def audit_v2(payload: dict[str, Any]) -> list[dict[str, str]]:
    """Validacoes v2: 22 campos por classe + ERROR/WARNING contextual."""
    rows: list[dict[str, str]] = []
    dicio_names = dicionario_field_names(payload)

    # 1) 22 campos por classe LGPD.
    for classe, campos_esperados in DICIONARIO_22_CAMPOS.items():
        for campo in campos_esperados:
            presente = campo in dicio_names
            rows.append({
                "tipo": f"dicionario_{classe}",
                "item": campo,
                "status": "ok" if presente else "gap",
                "severidade": "media" if not presente else "ok",
                "acao": (
                    f"Adicionar {campo} a classe {classe} em dicionario_campos."
                    if not presente else "Manter."
                ),
            })

    # 2) ERRO: camada CAPI (7) ausente em projeto com Meta no scope.
    scope = payload.get("scope_plataformas", []) or []
    if isinstance(scope, list):
        scope_set = {str(s) for s in scope}
    else:
        scope_set = set()

    camadas = payload.get("camadas", {})
    camada_7_presente = isinstance(camadas, dict) and "7" in camadas
    capi_ativo = bool(payload.get("capi_ativo", False))

    if "Meta" in scope_set and not (camada_7_presente and capi_ativo):
        rows.append({
            "tipo": "erro_capi",
            "item": "camada_7_servidor_capi",
            "status": "gap",
            "severidade": "erro",
            "acao": "ERROR: projeto tem Meta no scope mas camada 7 (Servidor CAPI) ausente ou capi_ativo=false. Sem CAPI, dedup quebra e EMQ trava.",
        })

    # 3) ERRO: PII raw enviada pra plataforma de midia.
    pii_raw_em_plataforma = []
    for item in payload.get("dicionario_campos", {}).get("pii_bruto", []) or []:
        if not isinstance(item, dict):
            continue
        destinos = item.get("destino_permitido", []) or []
        if not isinstance(destinos, list):
            continue
        destinos_set = {str(d) for d in destinos}
        if destinos_set & PLATAFORMAS_MIDIA:
            pii_raw_em_plataforma.append(str(item.get("campo", "")))

    if pii_raw_em_plataforma:
        rows.append({
            "tipo": "erro_lgpd",
            "item": ",".join(pii_raw_em_plataforma),
            "status": "gap",
            "severidade": "erro",
            "acao": "ERROR: PII raw declarada com destino plataforma de midia (Meta/Google/TikTok/LinkedIn). Violacao LGPD + Politica da Plataforma. Use sha256_hex.",
        })

    # 4) ERRO: banner LGPD ausente.
    banner_ativo = bool(payload.get("banner_lgpd_ativo", False))
    lgpd = payload.get("lgpd_compliance", {})
    banner_4_categorias = (
        isinstance(lgpd, dict)
        and isinstance(lgpd.get("banner_4_categorias"), dict)
        and len(lgpd.get("banner_4_categorias", {})) >= 4
    )
    if not (banner_ativo and banner_4_categorias):
        rows.append({
            "tipo": "erro_lgpd",
            "item": "banner_lgpd_4_categorias",
            "status": "gap",
            "severidade": "erro",
            "acao": "ERROR: banner LGPD com 4 categorias granulares (necessario/funcional/analytics/marketing) ausente. ANPD exige granularidade.",
        })

    # 5) WARNING: hashing canonico nao declarado.
    hashing_declarado = bool(payload.get("hashing_canonico_declarado", False)) or (
        isinstance(lgpd, dict) and "hashing_canonico" in lgpd
    )
    if not hashing_declarado:
        rows.append({
            "tipo": "warning_hashing",
            "item": "hashing_canonico",
            "status": "gap",
            "severidade": "warning",
            "acao": "WARNING: hashing canonico nao declarado. Garantir email lowercase->trim->sha256_hex e phone E.164->sha256_hex.",
        })

    # 6) WARNING: match key fallback ausente.
    regras_match = payload.get("regras_match", {})
    fallback = (
        isinstance(regras_match, dict)
        and str(regras_match.get("match_key_fallback", "")).strip()
    )
    if not fallback:
        rows.append({
            "tipo": "warning_match",
            "item": "match_key_fallback",
            "status": "gap",
            "severidade": "warning",
            "acao": "WARNING: match_key_fallback ausente em regras_match. Recomendado email_sha256.",
        })

    # 7) WARNING: dedup CAPI sem mesmo event_id declarado.
    dedup = (
        regras_match.get("dedup_capi") if isinstance(regras_match, dict) else None
    )
    if "Meta" in scope_set and not (
        isinstance(dedup, dict)
        and "event_id" in str(dedup.get("estrategia", "")).lower()
    ):
        rows.append({
            "tipo": "warning_dedup",
            "item": "dedup_capi_event_id",
            "status": "gap",
            "severidade": "warning",
            "acao": "WARNING: estrategia de dedup CAPI por event_id UUID v4 nao declarada. Sem isso, Meta conta em duplicidade.",
        })

    return rows


def decision(rows: list[dict[str, str]]) -> str:
    erro = sum(1 for row in rows if row["severidade"] == "erro")
    critical = sum(1 for row in rows if row["severidade"] == "critica")
    high = sum(1 for row in rows if row["severidade"] == "alta")
    if erro:
        return "bloqueado_erro_v2"
    if critical:
        return "nao_n2"
    if high:
        return "n2_parcial"
    return "n2"


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["tipo", "item", "status", "severidade", "acao"])
        writer.writeheader()
        writer.writerows(rows)


def render_dicionario_section(payload: dict[str, Any]) -> list[str]:
    """Renderiza secao do dicionario de 22 campos no markdown (so v2)."""
    if not is_v2(payload):
        return []
    dicio = payload.get("dicionario_campos", {})
    if not isinstance(dicio, dict) or not dicio:
        return []
    lines = ["", "## Dicionario De 22 Campos Por Classe LGPD", ""]
    for classe in ("pii_bruto", "pii_hash", "id_tecnico", "metadata_marketing", "consent"):
        items = dicio.get(classe, [])
        if not isinstance(items, list) or not items:
            continue
        lines.append(f"### Classe `{classe}` ({len(items)} campos)")
        lines.append("")
        lines.append("| Campo | Tipo | Origem | Regra |")
        lines.append("| --- | --- | --- | --- |")
        for item in items:
            if not isinstance(item, dict):
                continue
            campo = item.get("campo", "")
            tipo = item.get("tipo", "")
            origem = item.get("origem", "")
            regra = item.get("regra", "") or item.get("quando", "") or item.get("controla", "")
            lines.append(f"| `{campo}` | {tipo} | {origem} | {regra} |")
        lines.append("")
    return lines


def render_regras_section(payload: dict[str, Any]) -> list[str]:
    if not is_v2(payload):
        return []
    regras = payload.get("regras_match", {})
    lgpd = payload.get("lgpd_compliance", {})
    if not isinstance(regras, dict) and not isinstance(lgpd, dict):
        return []
    lines = ["", "## Regras De Match E LGPD", ""]
    if isinstance(regras, dict) and regras:
        lines.append(f"- Match key primaria: `{regras.get('match_key_primaria', '?')}`")
        lines.append(f"- Match key fallback: `{regras.get('match_key_fallback', '?')}`")
        lines.append(f"- Tag se ambos ausentes: `{regras.get('tag_ambos_ausentes', '?')}`")
        dedup = regras.get("dedup_capi", {})
        if isinstance(dedup, dict):
            lines.append(f"- Dedup CAPI: {dedup.get('estrategia', '?')}")
    if isinstance(lgpd, dict) and lgpd:
        banner = lgpd.get("banner_4_categorias", {})
        if isinstance(banner, dict):
            lines.append(f"- Banner LGPD 4 categorias: {', '.join(banner.keys())}")
        cmv2 = lgpd.get("consent_mode_v2_sinais", {})
        if isinstance(cmv2, dict):
            lines.append(f"- Consent Mode v2 sinais: {', '.join(cmv2.keys())}")
        if "regra_inviolavel" in lgpd:
            lines.append(f"- Regra inviolavel: {lgpd['regra_inviolavel']}")
    return lines


def write_markdown(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    schema_version = payload.get("schema_version", "v1")
    lines = [
        "# Auditoria Do Contrato De Dados",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Contrato: {payload.get('contrato', '')}",
        f"- Schema: {schema_version}",
        f"- Decisao: {decision(rows)}",
        "",
        "## Resultado Da Auditoria",
        "",
        "| tipo | item | status | severidade | acao |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(f"| {row['tipo']} | `{row['item']}` | {row['status']} | {row['severidade']} | {row['acao']} |")

    lines.extend(render_dicionario_section(payload))
    lines.extend(render_regras_section(payload))

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit data contract coverage.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    rows = audit(payload)
    if not args.md_path and not args.csv_path:
        print(decision(rows))
        return
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)


if __name__ == "__main__":
    main()
