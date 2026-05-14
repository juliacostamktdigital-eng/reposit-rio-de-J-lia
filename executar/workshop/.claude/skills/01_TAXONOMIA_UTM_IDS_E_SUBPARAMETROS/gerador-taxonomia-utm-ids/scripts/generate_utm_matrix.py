#!/usr/bin/env python3
"""Generate canonical Marketing OS IDs, names and UTM URLs from JSON.

Regras enforçadas (2026):
- lowercase enforçado (warning + autoconvert);
- hífen como separador interno (`-`), `__` separa blocos;
- `utm_campaign` ≤ 150 chars (configurável via `max_utm_campaign_chars`);
- canonical tag SEO: warning emitido se `canonical_tag_present` for false;
- versionamento imutável: sequencial aceita sufixo `-v2`, `-v3` (ex: `014-v2`).

Backwards-compat: JSON antigo sem campos novos (`canonical_url`,
`canonical_tag_present`, `max_utm_campaign_chars`, `iteracao_de`,
`motivo_iteracao`) continua sendo lido sem erro.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import urlencode


FIELDS = [
    "client_id",
    "campaign_id",
    "adgroup_id",
    "creative_id",
    "test_id",
    "campaign_name",
    "adgroup_name",
    "creative_name",
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
    "final_url",
    "utm_campaign_len",
    "utm_campaign_within_cap",
    "iteracao_de",
    "motivo_iteracao",
]

DEFAULT_UTM_CAMPAIGN_CAP = 150


def slugify(value: Any) -> str:
    text = str(value or "").strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = re.sub(r"[^a-z0-9_-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")


def required(item: dict[str, Any], field: str, context: str) -> str:
    value = slugify(item.get(field))
    if not value:
        raise ValueError(f"Missing required field '{field}' in {context}.")
    return value


def seq(value: Any, context: str) -> str:
    """Aceita sequencial numérico (`001`, `014`) ou versionado (`014-v2`, `014-v3`).

    Versionamento imutável: ID original `014` permanece; iteração vira `014-v2`.
    """
    raw = str(value or "").strip().lower()
    if not raw:
        raise ValueError(f"Missing sequencial in {context}.")
    # Aceita formatos: `014`, `014-v2`, `014-v3`, etc.
    match = re.fullmatch(r"(\d+)(-v\d+)?", raw)
    if not match:
        raise ValueError(
            f"Sequencial must be numeric or numeric-vN in {context}: {raw}"
        )
    number, version = match.groups()
    return number.zfill(3) + (version or "")


def validate_lowercase(payload: dict[str, Any], warnings: list[str]) -> None:
    """Emite warning se algum valor de string contiver maiúsculas.

    Não bloqueia (slugify já aplica lowercase), só sinaliza pra operador
    saber que input estava fora da convenção.
    """

    def walk(node: Any, path: str) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                walk(value, f"{path}.{key}" if path else key)
        elif isinstance(node, list):
            for index, value in enumerate(node):
                walk(value, f"{path}[{index}]")
        elif isinstance(node, str) and node != node.lower():
            warnings.append(
                f"lowercase-violation em '{path}': '{node}' (autoconvertido)."
            )

    walk(payload, "")


def warn_canonical(payload: dict[str, Any], warnings: list[str]) -> None:
    canonical_url = str(payload.get("canonical_url", "")).strip()
    canonical_present = payload.get("canonical_tag_present")
    if not canonical_url:
        warnings.append(
            "canonical-url-missing: campo 'canonical_url' não declarado. "
            "Toda LP que recebe UTM deve ter <link rel='canonical'> apontando "
            "pra URL base sem UTMs."
        )
    if canonical_present is False:
        warnings.append(
            "canonical-tag-absent: 'canonical_tag_present=false'. "
            "Sem canonical, Google Search indexa cada UTM como duplicata. "
            "Adicionar <link rel='canonical' href='{}'> no <head> da LP "
            "antes do go-live.".format(canonical_url or "URL_BASE_SEM_UTMS")
        )
    if canonical_present is None:
        warnings.append(
            "canonical-tag-unknown: 'canonical_tag_present' não declarado. "
            "Validar manualmente que <link rel='canonical'> existe na LP."
        )


def build_rows(
    payload: dict[str, Any], warnings: list[str]
) -> list[dict[str, str]]:
    base_url = str(payload.get("base_url", "")).strip()
    if not base_url:
        raise ValueError("Missing 'base_url'.")

    cap = int(payload.get("max_utm_campaign_chars") or DEFAULT_UTM_CAMPAIGN_CAP)

    client_slug = required(payload, "cliente", "root")
    year_month = str(payload.get("ano_mes", "")).strip()
    if not re.fullmatch(r"\d{6}", year_month):
        raise ValueError("'ano_mes' must use YYYYMM.")

    client_id = f"cli-{client_slug}"
    utm_source = required(payload, "utm_source", "root")
    utm_medium = required(payload, "utm_medium", "root")

    rows: list[dict[str, str]] = []
    campaigns = payload.get("campanhas")
    if not isinstance(campaigns, list):
        raise ValueError("'campanhas' must be a list.")

    for campaign in campaigns:
        if not isinstance(campaign, dict):
            raise ValueError("Each campaign must be an object.")
        campaign_id = (
            f"cmp-{client_slug}-{year_month}-"
            f"{seq(campaign.get('sequencial'), 'campaign')}"
        )
        typ = required(campaign, "tipo_campanha", campaign_id)
        obj = required(campaign, "objetivo", campaign_id)
        mov = required(campaign, "movimento", campaign_id)
        campaign_slug = required(campaign, "slug", campaign_id)
        cohort = required(campaign, "cohort", campaign_id)
        segmento = required(campaign, "segmento", campaign_id)
        periodo = required(campaign, "periodo", campaign_id)
        campaign_name = (
            f"{campaign_id} | {typ} | {obj} | {mov} | {campaign_slug}"
        )
        utm_campaign = (
            f"{campaign_id}__typ-{typ}__obj-{obj}__mov-{mov}__slug-{campaign_slug}"
            f"__coh-{cohort}__seg-{segmento}__per-{periodo}"
        )
        utm_campaign_len = len(utm_campaign)
        within_cap = utm_campaign_len <= cap
        if not within_cap:
            warnings.append(
                f"utm-campaign-overflow: '{campaign_id}' utm_campaign tem "
                f"{utm_campaign_len} chars (cap={cap}). Abreviar tokens "
                "(`aquisicao`→`aq`, `conversao`→`cv`, `prospeccao`→`pp`, "
                "`remarketing`→`rmkt`, etc) — ver reference.md."
            )

        adgroups = campaign.get("adgroups")
        if not isinstance(adgroups, list):
            raise ValueError(f"'adgroups' must be a list in {campaign_id}.")

        for adgroup in adgroups:
            if not isinstance(adgroup, dict):
                raise ValueError(
                    f"Each adgroup in {campaign_id} must be an object."
                )
            adgroup_id = (
                f"adg-{client_slug}-{year_month}-"
                f"{seq(adgroup.get('sequencial'), 'adgroup')}"
            )
            publico = required(adgroup, "publico", adgroup_id)
            temperatura = required(adgroup, "temperatura", adgroup_id)
            posicionamento = required(adgroup, "posicionamento", adgroup_id)
            adgroup_slug = required(adgroup, "slug", adgroup_id)
            placement = slugify(adgroup.get("placement")) or "na"
            geo = slugify(adgroup.get("geo")) or "na"
            keyword = slugify(adgroup.get("keyword"))
            match_type = slugify(adgroup.get("match_type"))
            adgroup_name = (
                f"{adgroup_id} | {publico} | {temperatura} | "
                f"{posicionamento} | {adgroup_slug}"
            )
            if keyword:
                utm_term = (
                    f"{adgroup_id}__kw-{keyword}__match-"
                    f"{match_type or 'na'}__temp-{temperatura}"
                    f"__slug-{adgroup_slug}__geo-{geo}"
                )
            else:
                utm_term = (
                    f"{adgroup_id}__pub-{publico}__temp-{temperatura}"
                    f"__pos-{posicionamento}__slug-{adgroup_slug}"
                    f"__plc-{placement}__geo-{geo}"
                )

            creatives = adgroup.get("criativos")
            if not isinstance(creatives, list):
                raise ValueError(
                    f"'criativos' must be a list in {adgroup_id}."
                )

            for creative in creatives:
                if not isinstance(creative, dict):
                    raise ValueError(
                        f"Each creative in {adgroup_id} must be an object."
                    )
                creative_id = (
                    f"crv-{client_slug}-{year_month}-"
                    f"{seq(creative.get('sequencial'), 'creative')}"
                )
                test_id = (
                    f"tst-{client_slug}-{year_month}-"
                    f"{seq(creative.get('test_sequencial'), 'test')}"
                )
                formato = required(creative, "formato", creative_id)
                hook = required(creative, "hook", creative_id)
                persona = required(creative, "persona", creative_id)
                creative_slug = required(creative, "slug", creative_id)
                dor = required(creative, "dor", creative_id)
                angulo = required(creative, "angulo", creative_id)
                etapa = required(creative, "etapa", creative_id)
                versao = required(creative, "versao", creative_id)
                iteracao_de = slugify(creative.get("iteracao_de"))
                motivo_iteracao = slugify(creative.get("motivo_iteracao"))
                creative_name = (
                    f"{creative_id} | {formato} | {hook} | {persona} | "
                    f"{creative_slug} | {versao}"
                )
                utm_content = (
                    f"{creative_id}__fmt-{formato}__hook-{hook}__per-{persona}"
                    f"__slug-{creative_slug}__dor-{dor}__ang-{angulo}"
                    f"__stage-{etapa}__ver-{versao}"
                )
                query = {
                    "utm_source": utm_source,
                    "utm_medium": utm_medium,
                    "utm_campaign": utm_campaign,
                    "utm_content": utm_content,
                    "utm_term": utm_term,
                    "v4_client_id": client_id,
                    "v4_campaign_id": campaign_id,
                    "v4_adgroup_id": adgroup_id,
                    "v4_creative_id": creative_id,
                    "v4_test_id": test_id,
                }
                separator = "&" if "?" in base_url else "?"
                final_url = f"{base_url}{separator}{urlencode(query)}"
                rows.append({
                    "client_id": client_id,
                    "campaign_id": campaign_id,
                    "adgroup_id": adgroup_id,
                    "creative_id": creative_id,
                    "test_id": test_id,
                    "campaign_name": campaign_name,
                    "adgroup_name": adgroup_name,
                    "creative_name": creative_name,
                    "utm_source": utm_source,
                    "utm_medium": utm_medium,
                    "utm_campaign": utm_campaign,
                    "utm_content": utm_content,
                    "utm_term": utm_term,
                    "v4_client_id": client_id,
                    "v4_campaign_id": campaign_id,
                    "v4_adgroup_id": adgroup_id,
                    "v4_creative_id": creative_id,
                    "v4_test_id": test_id,
                    "final_url": final_url,
                    "utm_campaign_len": str(utm_campaign_len),
                    "utm_campaign_within_cap": "yes" if within_cap else "no",
                    "iteracao_de": iteracao_de,
                    "motivo_iteracao": motivo_iteracao,
                })
    return rows


def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Matriz De UTMs E IDs",
        "",
        "| " + " | ".join(FIELDS) + " |",
        "| " + " | ".join("---" for _ in FIELDS) + " |",
    ]
    for row in rows:
        lines.append(
            "| " + " | ".join(escape_md(row[field]) for field in FIELDS) + " |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def emit_warnings(warnings: list[str]) -> None:
    if not warnings:
        return
    print("== AVISOS ==", file=sys.stderr)
    for warning in warnings:
        print(f"[warn] {warning}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Marketing OS UTM matrix from JSON."
    )
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Promove warnings (cap, canonical, lowercase) a erro fatal.",
    )
    args = parser.parse_args()

    payload = json.loads(args.input_json.read_text(encoding="utf-8"))
    warnings: list[str] = []
    validate_lowercase(payload, warnings)
    warn_canonical(payload, warnings)
    rows = build_rows(payload, warnings)

    if not args.csv_path and not args.md_path:
        for row in rows:
            print(row["final_url"])
    else:
        if args.csv_path:
            write_csv(rows, args.csv_path)
        if args.md_path:
            write_markdown(rows, args.md_path)

    emit_warnings(warnings)
    if args.strict and warnings:
        sys.exit(2)


if __name__ == "__main__":
    main()
