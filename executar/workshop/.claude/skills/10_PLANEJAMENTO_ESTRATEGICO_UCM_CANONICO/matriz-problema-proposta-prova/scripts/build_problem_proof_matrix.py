#!/usr/bin/env python3
"""Build a problem-proposition-proof matrix from JSON.

Suporta:
- matriz tradicional (problema x proposta x prova);
- matriz 3D (provas_por_papel: economic_buyer | user | technical_buyer | champion);
- anti_claims (categoria: regulatorio | comparativo | factual);
- message_house (roof_claim, pillars, proof_points).

Backwards-compat: arquivos JSON sem os novos campos rodam sem erro.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any


FIELDS = [
    "prioridade", "score", "problema", "impacto", "voz_cliente", "persona", "stage", "proposta",
    "mecanismo", "promessa", "objecao", "prova", "status_prova", "claim_pendente", "risco",
]

VALID_PAPEIS = {"economic_buyer", "user", "technical_buyer", "champion"}
VALID_ANTI_CATEGORIAS = {"regulatorio", "comparativo", "factual"}
VALID_STATUS_PROVA = {"forte", "parcial", "ausente", "restrita", ""}


def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def as_int(item: dict[str, Any], field: str) -> int:
    try:
        return int(item.get(field, 0) or 0)
    except ValueError:
        return 0


def score(item: dict[str, Any]) -> int:
    return (
        as_int(item, "impacto_score") * 2
        + as_int(item, "frequencia_score")
        + as_int(item, "evidencia_score")
        - as_int(item, "risco_score")
    )


def is_claim_pending(item: dict[str, Any]) -> bool:
    status = str(item.get("status_prova", "")).strip().lower()
    proof = str(item.get("prova", "")).strip()
    return status in {"ausente", "restrita"} or proof == ""


def is_strong_promise(item: dict[str, Any]) -> bool:
    """Promessa-forte: status forte/parcial e prova preenchida."""
    status = str(item.get("status_prova", "")).strip().lower()
    proof = str(item.get("prova", "")).strip()
    return status in {"forte", "parcial"} and proof != ""


def validate_payload(payload: dict[str, Any]) -> list[str]:
    """Valida tipos e enums dos novos campos. Retorna lista de erros (vazia = OK)."""
    errors: list[str] = []

    # message_house
    mh = payload.get("message_house")
    if mh is not None:
        if not isinstance(mh, dict):
            errors.append("'message_house' deve ser objeto.")
        else:
            if "pillars" in mh and not isinstance(mh.get("pillars"), list):
                errors.append("'message_house.pillars' deve ser lista.")
            pps = mh.get("proof_points")
            if pps is not None:
                if not isinstance(pps, list):
                    errors.append("'message_house.proof_points' deve ser lista.")
                else:
                    for index, pp in enumerate(pps):
                        if not isinstance(pp, dict):
                            errors.append(f"message_house.proof_points[{index}] deve ser objeto.")

    # anti_claims
    acs = payload.get("anti_claims")
    if acs is not None:
        if not isinstance(acs, list):
            errors.append("'anti_claims' deve ser lista.")
        else:
            for index, ac in enumerate(acs):
                if not isinstance(ac, dict):
                    errors.append(f"anti_claims[{index}] deve ser objeto.")
                    continue
                cat = str(ac.get("categoria", "")).strip().lower()
                if cat and cat not in VALID_ANTI_CATEGORIAS:
                    errors.append(
                        f"anti_claims[{index}].categoria='{cat}' inválido. "
                        f"Use: {sorted(VALID_ANTI_CATEGORIAS)}."
                    )

    # provas_por_papel por problema
    problemas = payload.get("problemas", [])
    if isinstance(problemas, list):
        for pidx, item in enumerate(problemas):
            if not isinstance(item, dict):
                continue
            pps = item.get("provas_por_papel")
            if pps is None:
                continue
            if not isinstance(pps, list):
                errors.append(f"problemas[{pidx}].provas_por_papel deve ser lista.")
                continue
            for index, pp in enumerate(pps):
                if not isinstance(pp, dict):
                    errors.append(f"problemas[{pidx}].provas_por_papel[{index}] deve ser objeto.")
                    continue
                papel = str(pp.get("papel", "")).strip().lower()
                if papel and papel not in VALID_PAPEIS:
                    errors.append(
                        f"problemas[{pidx}].provas_por_papel[{index}].papel='{papel}' inválido. "
                        f"Use: {sorted(VALID_PAPEIS)}."
                    )

    return errors


def audit_payload(payload: dict[str, Any]) -> list[str]:
    """Warnings não-bloqueantes (modo --audit). Retorna lista de avisos."""
    warnings: list[str] = []
    problemas = payload.get("problemas", [])
    if not isinstance(problemas, list):
        return warnings

    for pidx, item in enumerate(problemas):
        if not isinstance(item, dict):
            continue
        problema = str(item.get("problema", f"#{pidx}"))

        if is_strong_promise(item):
            pps = item.get("provas_por_papel")
            if not isinstance(pps, list) or len(pps) == 0:
                warnings.append(
                    f"[promessa-forte sem provas-por-papel] '{problema}' tem prova mas não mapeou "
                    f"provas_por_papel — Economic Buyer / User / Technical Buyer / Champion."
                )
            else:
                papeis_mapeados = {
                    str(pp.get("papel", "")).strip().lower()
                    for pp in pps if isinstance(pp, dict)
                }
                faltantes = VALID_PAPEIS - papeis_mapeados
                if faltantes:
                    warnings.append(
                        f"[cobertura parcial papel] '{problema}' não tem prova para: "
                        f"{sorted(faltantes)}."
                    )

        status = str(item.get("status_prova", "")).strip().lower()
        if status and status not in VALID_STATUS_PROVA:
            warnings.append(
                f"[status_prova suspeito] '{problema}' tem status_prova='{status}' "
                f"fora do conjunto canônico {sorted(VALID_STATUS_PROVA - {''})}."
            )

    if not payload.get("message_house"):
        warnings.append(
            "[message_house ausente] Considere declarar roof_claim + pillars + proof_points "
            "para garantir consistência narrativa entre ativos."
        )

    if not payload.get("anti_claims"):
        warnings.append(
            "[anti_claims ausente] Liste o que NÃO podemos afirmar "
            "(regulatorio / comparativo / factual) antes de copy/criativo."
        )

    return warnings


def build_rows(payload: dict[str, Any]) -> list[dict[str, str]]:
    problems = payload.get("problemas", [])
    if not isinstance(problems, list):
        raise ValueError("'problemas' must be a list.")
    rows = []
    for item in problems:
        if not isinstance(item, dict):
            continue
        rows.append({
            "prioridade": "",
            "score": str(score(item)),
            "problema": str(item.get("problema", "")),
            "impacto": str(item.get("impacto", "")),
            "voz_cliente": str(item.get("voz_cliente", "")),
            "persona": str(item.get("persona", "")),
            "stage": str(item.get("stage", "")),
            "proposta": str(item.get("proposta", "")),
            "mecanismo": str(item.get("mecanismo", "")),
            "promessa": str(item.get("promessa", "")),
            "objecao": str(item.get("objecao", "")),
            "prova": str(item.get("prova", "")),
            "status_prova": str(item.get("status_prova", "")),
            "claim_pendente": "sim" if is_claim_pending(item) else "nao",
            "risco": str(item.get("risco", "")),
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


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_message_house(mh: dict[str, Any]) -> list[str]:
    lines = ["", "## Message House", ""]
    roof = str(mh.get("roof_claim", "")).strip()
    lines.append(f"- Roof Claim: {roof}" if roof else "- Roof Claim: _(não declarado)_")
    pillars = mh.get("pillars") or []
    if isinstance(pillars, list) and pillars:
        lines.extend(["", "### Pillars", "", "| # | Pillar |", "| --- | --- |"])
        for idx, pillar in enumerate(pillars, start=1):
            lines.append(f"| {idx} | {esc(str(pillar))} |")
    pps = mh.get("proof_points") or []
    if isinstance(pps, list) and pps:
        lines.extend(["", "### Proof Points", "", "| Pillar | Proof Point |", "| --- | --- |"])
        for pp in pps:
            if not isinstance(pp, dict):
                continue
            pillar = esc(str(pp.get("pillar", "")))
            proof = esc(str(pp.get("proof", "")))
            lines.append(f"| {pillar} | {proof} |")
    return lines


def render_provas_por_papel(payload: dict[str, Any]) -> list[str]:
    problemas = payload.get("problemas", [])
    if not isinstance(problemas, list):
        return []
    any_mapped = False
    rows: list[str] = []
    for item in problemas:
        if not isinstance(item, dict):
            continue
        pps = item.get("provas_por_papel")
        if not isinstance(pps, list) or not pps:
            continue
        problema = esc(str(item.get("problema", "")))
        for pp in pps:
            if not isinstance(pp, dict):
                continue
            any_mapped = True
            rows.append(
                f"| {problema} | {esc(str(pp.get('papel', '')))} | "
                f"{esc(str(pp.get('tipo_prova', '')))} | "
                f"{esc(str(pp.get('evidencia', '')))} |"
            )
    if not any_mapped:
        return []
    return [
        "",
        "## Provas Por Papel (Matriz 3D)",
        "",
        "| Problema | Papel | Tipo de prova | Evidência |",
        "| --- | --- | --- | --- |",
        *rows,
    ]


def render_anti_claims(acs: list[Any]) -> list[str]:
    if not acs:
        return []
    lines = [
        "",
        "## Anti-Claims (O Que NÃO Podemos Afirmar)",
        "",
        "| Claim proibido | Categoria | Motivo |",
        "| --- | --- | --- |",
    ]
    for ac in acs:
        if not isinstance(ac, dict):
            continue
        lines.append(
            f"| {esc(str(ac.get('claim_proibido', '')))} | "
            f"{esc(str(ac.get('categoria', '')))} | "
            f"{esc(str(ac.get('motivo', '')))} |"
        )
    return lines


def write_markdown(path: Path, payload: dict[str, Any], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Matriz Problema Proposta Prova",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Oferta: {payload.get('oferta', '')}",
        f"- Fonte: {payload.get('fonte', '')}",
    ]

    mh = payload.get("message_house")
    if isinstance(mh, dict) and mh:
        lines.extend(render_message_house(mh))

    lines.extend([
        "",
        "## Matriz",
        "",
        "| prioridade | problema | proposta | mecanismo | promessa | prova | claim pendente |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ])
    for row in rows:
        fields = ["prioridade", "problema", "proposta", "mecanismo", "promessa", "prova", "claim_pendente"]
        lines.append("| " + " | ".join(esc(row[field]) for field in fields) + " |")

    lines.extend(render_provas_por_papel(payload))

    acs = payload.get("anti_claims")
    if isinstance(acs, list) and acs:
        lines.extend(render_anti_claims(acs))

    pending = [row for row in rows if row["claim_pendente"] == "sim"]
    if pending:
        lines.extend(["", "## Claims Pendentes", ""])
        for row in pending:
            lines.append(f"- `{row['promessa']}` precisa de prova para `{row['problema']}`.")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build problem-proposition-proof matrix.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--csv", dest="csv_path", type=Path)
    parser.add_argument(
        "--audit",
        action="store_true",
        help="Imprime warnings (promessa-forte sem provas-por-papel, message_house ausente, etc).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Sai com código !=0 se validação dos novos campos falhar.",
    )
    args = parser.parse_args()

    payload = load_payload(args.input_json)

    errors = validate_payload(payload)
    if errors:
        for err in errors:
            print(f"[validation] {err}", file=sys.stderr)
        if args.strict:
            sys.exit(2)

    if args.audit:
        warnings = audit_payload(payload)
        for warn in warnings:
            print(f"[audit] {warn}", file=sys.stderr)

    rows = build_rows(payload)
    if args.csv_path:
        write_csv(args.csv_path, rows)
    if args.md_path:
        write_markdown(args.md_path, payload, rows)
    if not args.csv_path and not args.md_path:
        for row in rows:
            print(f"{row['prioridade']}. {row['problema']} - claim pendente: {row['claim_pendente']}")


if __name__ == "__main__":
    main()
