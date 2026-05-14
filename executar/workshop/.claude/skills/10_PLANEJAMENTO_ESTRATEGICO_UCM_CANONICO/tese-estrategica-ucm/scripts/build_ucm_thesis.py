#!/usr/bin/env python3
"""Build an initial UCM strategic thesis from JSON.

Suporta os 14 itens da estrutura mínima:
contexto, problemas, personas, Champion-tipo, JTBD core (Ulwick ODI),
alternativas, Forces of Progress (Bob Moesta), frequência, proposta de valor,
inimigo, provas, narrativa, vocabulário, tradução para ativos.

Modos:
  --md PATH       gera Markdown completo
  --audit         só roda lint do JSON (sem escrever output)

Backwards-compat: JSON antigo (sem champion_tipo / jtbd_core / forces_of_progress)
roda sem erro; o script só emite warnings em --audit e omite seções no Markdown.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


# ---------- helpers ----------

def load_payload(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def list_text(values: Any) -> str:
    if isinstance(values, list):
        return ", ".join(str(value) for value in values)
    return str(values or "")


def has_value(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ""
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return True


# ---------- audit (lint) ----------

def audit_payload(payload: dict[str, Any]) -> list[str]:
    """Retorna lista de warnings sobre campos novos ausentes/incompletos."""
    warnings: list[str] = []

    # Champion-tipo
    champion = payload.get("champion_tipo")
    if not isinstance(champion, dict) or not champion:
        warnings.append("champion_tipo ausente — defina perfil que vende internamente (não cliente genérico).")
    else:
        for required in ("nome_funcional", "dor_especifica", "credito_interno",
                         "risco_interno", "vocabulario_proprio", "comportamento_esperado"):
            if not has_value(champion.get(required)):
                warnings.append(f"champion_tipo.{required} vazio.")

    # JTBD core sintético (Ulwick)
    jtbd = payload.get("jtbd_core")
    if not isinstance(jtbd, dict) or not jtbd:
        warnings.append("jtbd_core ausente — escreva 1 linha solution-free padrão Ulwick ODI.")
    else:
        if not has_value(jtbd.get("statement")):
            warnings.append("jtbd_core.statement vazio (formato: [verbo] + [objeto] + [contexto]).")
        if jtbd.get("solution_free") is False:
            warnings.append("jtbd_core.solution_free=false — reescreva sem mencionar produto/solução.")
        # Heurística leve: detectar palavras que sugerem solução
        statement = str(jtbd.get("statement", "")).lower()
        contaminantes = [" via ", " usando ", " com a ferramenta", " com o produto",
                         " através do nosso", " por meio do nosso"]
        for c in contaminantes:
            if c in statement:
                warnings.append(f"jtbd_core.statement parece mencionar solução ('{c.strip()}') — Ulwick ODI exige solution-free.")
                break

    # Forces of Progress (Bob Moesta)
    forces = payload.get("forces_of_progress")
    if not isinstance(forces, dict) or not forces:
        warnings.append("forces_of_progress ausente — mapeie push/pull/anxiety/habit + struggling_moment.")
    else:
        for required in ("struggling_moment", "push", "pull", "anxiety", "habit"):
            if not has_value(forces.get(required)):
                warnings.append(f"forces_of_progress.{required} vazio.")

    # Itens canônicos antigos (sanity)
    if not has_value(payload.get("batalha")):
        warnings.append("batalha vazia — declare a batalha estratégica antes da copy.")
    if not payload.get("personas"):
        warnings.append("personas vazia — separe personas e papéis de decisão.")
    if not payload.get("problemas"):
        warnings.append("problemas vazio — priorize problemas com impacto e voz do cliente.")

    return warnings


# ---------- markdown render ----------

def render_champion(payload: dict[str, Any]) -> list[str]:
    champion = payload.get("champion_tipo")
    if not isinstance(champion, dict) or not champion:
        return []
    return [
        "",
        "## Champion-tipo",
        "",
        f"- Nome funcional: {champion.get('nome_funcional', '')}",
        f"- Dor específica: {champion.get('dor_especifica', '')}",
        f"- Crédito interno: {champion.get('credito_interno', '')}",
        f"- Risco interno: {champion.get('risco_interno', '')}",
        f"- Vocabulário próprio: {list_text(champion.get('vocabulario_proprio'))}",
        f"- Comportamento esperado: {champion.get('comportamento_esperado', '')}",
    ]


def render_jtbd(payload: dict[str, Any]) -> list[str]:
    jtbd = payload.get("jtbd_core")
    if not isinstance(jtbd, dict) or not jtbd:
        return []
    lines = [
        "",
        "## JTBD Core Sintético (Ulwick ODI)",
        "",
        f"- Statement: {jtbd.get('statement', '')}",
    ]
    if has_value(jtbd.get("verbo")):
        lines.append(f"- Verbo: {jtbd.get('verbo', '')}")
    if has_value(jtbd.get("objeto")):
        lines.append(f"- Objeto: {jtbd.get('objeto', '')}")
    if has_value(jtbd.get("contexto")):
        lines.append(f"- Contexto: {jtbd.get('contexto', '')}")
    if "solution_free" in jtbd:
        lines.append(f"- Solution-free: {'sim' if jtbd.get('solution_free') else 'NÃO — reescrever'}")
    return lines


def render_forces(payload: dict[str, Any]) -> list[str]:
    forces = payload.get("forces_of_progress")
    if not isinstance(forces, dict) or not forces:
        return []
    return [
        "",
        "## Forces of Progress (Bob Moesta)",
        "",
        f"- Struggling moment: {forces.get('struggling_moment', '')}",
        f"- Push do status quo: {forces.get('push', '')}",
        f"- Pull da nova solução: {forces.get('pull', '')}",
        f"- Anxiety da mudança: {forces.get('anxiety', '')}",
        f"- Habit da inércia: {forces.get('habit', '')}",
        "",
        "Regra: a tese só vence quando push + pull > anxiety + habit.",
    ]


def build_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Tese Estratégica UCM",
        "",
        "## Contexto",
        "",
        f"- Cliente: {payload.get('cliente', '')}",
        f"- Produto/oferta foco: {payload.get('produto', '')}",
        f"- Objetivo da campanha: {payload.get('objetivo', '')}",
        f"- Canal de conversão: {payload.get('canal_conversao', '')}",
        "",
        "## Batalha Estratégica",
        "",
        str(payload.get("batalha", "")),
        "",
        "## Problemas Priorizados",
        "",
        "| Problema | Impacto | Voz do cliente | Funil |",
        "| --- | --- | --- | --- |",
    ]
    for problem in payload.get("problemas", []):
        if isinstance(problem, dict):
            lines.append(
                f"| {problem.get('nome', '')} | {problem.get('impacto', '')} | "
                f"{problem.get('voz_cliente', '')} | {problem.get('funil', '')} |"
            )

    lines.extend([
        "",
        "## Personas E Papéis De Decisão",
        "",
        "| Persona | Papel | Dores | Objeções | Provas | CTA |",
        "| --- | --- | --- | --- | --- | --- |",
    ])
    for persona in payload.get("personas", []):
        if isinstance(persona, dict):
            lines.append(
                f"| {persona.get('nome', '')} | {persona.get('papel', '')} | "
                f"{list_text(persona.get('dores'))} | {list_text(persona.get('objecoes'))} | "
                f"{list_text(persona.get('provas'))} | {persona.get('cta', '')} |"
            )

    # Novos blocos (omitidos silenciosamente se ausentes — backwards compat)
    lines.extend(render_champion(payload))
    lines.extend(render_jtbd(payload))
    lines.extend(render_forces(payload))

    narrative = payload.get("narrativa", {})
    if not isinstance(narrative, dict):
        narrative = {}
    lines.extend([
        "",
        "## Proposta De Valor E Mecanismo",
        "",
        str(payload.get("proposta_valor", "")),
        "",
        "## Inimigo / Status Quo",
        "",
        str(payload.get("inimigo", "")),
        "",
        "## Narrativa Central",
        "",
        f"- Contexto: {narrative.get('contexto', '')}",
        f"- Tensão: {narrative.get('tensao', '')}",
        f"- Inimigo: {narrative.get('inimigo', '')}",
        f"- Nova crença: {narrative.get('nova_crenca', '')}",
        f"- Mecanismo: {narrative.get('mecanismo', '')}",
        f"- Prova: {narrative.get('prova', '')}",
        f"- Convite: {narrative.get('convite', '')}",
        "",
        "## Tradução Para Ativos",
        "",
        "| Ativo | Direção |",
        "| --- | --- |",
        "| DCC/DEOC | Transformar tese, persona, dor e provas em documento estratégico. |",
        "| LP | Usar batalha, promessa, prova e objeções na sequência de seções. |",
        "| Criativos | Derivar hooks a partir de inimigo, tensão e nova crença. |",
        "| Plano de mídia | Separar públicos e mensagens por persona/funil. |",
        "| Comercial | Usar objeções e provas na qualificação. |",
        "| Tracking | Codificar persona, hook, dor, ângulo e stage. |",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build UCM thesis markdown from JSON.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--audit", action="store_true",
                        help="Apenas valida o JSON e emite warnings sobre Champion-tipo, JTBD core e Forces of Progress.")
    args = parser.parse_args()

    payload = load_payload(args.input_json)

    if args.audit:
        warnings = audit_payload(payload)
        if not warnings:
            print("[OK] Tese passa nos checks de Champion-tipo, JTBD core (Ulwick) e Forces of Progress.")
            return
        print(f"[AUDIT] {len(warnings)} warning(s):")
        for w in warnings:
            print(f"  - {w}")
        sys.exit(1)

    if not args.md_path:
        parser.error("--md PATH é obrigatório quando não está em --audit.")

    args.md_path.parent.mkdir(parents=True, exist_ok=True)
    args.md_path.write_text(build_markdown(payload), encoding="utf-8")


if __name__ == "__main__":
    main()
