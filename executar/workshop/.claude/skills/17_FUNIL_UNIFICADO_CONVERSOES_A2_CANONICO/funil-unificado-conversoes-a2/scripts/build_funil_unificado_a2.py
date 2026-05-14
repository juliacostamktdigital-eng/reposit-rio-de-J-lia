#!/usr/bin/env python3
"""Consolida funil unificado A-2 a partir de JSON (playbook 17) e audita DoD.

Conceitos refletidos (alinhados a SKILL.md / reference.md / template JSON):
  - Modo simples (lead-centric) vs avançado (opportunity / Forrester B2B
    Revenue Waterfall 2021 + Bowtie WbD).
  - Auto-detect de modo a partir de `criterios_modo` (ticket BRL, ciclo,
    comitê) com warning quando declarado diverge de detectado.
  - Benchmarks 2024-2026 com semáforo calibrado (verde/amarelo/vermelho).
  - SLA Mkt+Vendas como seção formal no Markdown.
  - Automação CRM concreta: state machine (Mermaid), scoring rule, webhook OUT.
  - Eventos canônicos pra TE/IE.
  - Buying group + Bowtie pós-venda + RPM (modo avançado).
  - --audit verbose com warnings de SLA, automação, benchmarks, buying group,
    eventos canônicos.
  - Backwards-compat: JSON antigo sem `modo` → assume `simples` sem erro.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

# Garante UTF-8 no stdout (necessário pra console Windows cp1252 não quebrar
# em caracteres como ≥, →, ⚠️ presentes nos avisos do audit).
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass


# ---------------------------------------------------------------------------
# helpers básicos
# ---------------------------------------------------------------------------


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def block(t: Any) -> str:
    s = "" if t is None else str(t).strip()
    return s if s else "_[preencher]_"


def is_placeholder(s: str) -> bool:
    t = s.strip().lower()
    if not t:
        return True
    if t.startswith("_[preencher]"):
        return True
    if t in ("[nome]", "yyyy-mm-dd"):
        return True
    return False


def filled(v: Any) -> bool:
    if v is None:
        return False
    if isinstance(v, bool):
        return True
    if isinstance(v, (int, float)):
        return True
    if isinstance(v, str):
        return not is_placeholder(v)
    if isinstance(v, list):
        return len(v) > 0
    if isinstance(v, dict):
        return len(v) > 0
    return bool(v)


def num(v: Any) -> float | None:
    """Tenta converter para float; aceita strings com vírgula/percentual."""
    if v is None:
        return None
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        s = v.strip().replace("%", "").replace(",", ".").replace(" ", "")
        if not s:
            return None
        try:
            return float(s)
        except ValueError:
            return None
    return None


# ---------------------------------------------------------------------------
# modo: detecção automática (simples vs avançado)
# ---------------------------------------------------------------------------


THRESHOLDS_AVANCADO = {
    "ticket_medio_brl": 30000.0,  # ≥ R$ 30k
    "ciclo_dias": 30.0,           # ≥ 30 dias
    "comite_size": 3.0,           # ≥ 3 stakeholders
}


def detectar_modo(criterios: dict[str, Any] | None) -> tuple[str, list[str]]:
    """Detecta modo a partir de critérios; retorna (modo, sinais)."""
    sinais: list[str] = []
    c = criterios or {}
    ticket = num(c.get("ticket_medio_brl"))
    ciclo = num(c.get("ciclo_dias"))
    comite = num(c.get("comite_size"))

    if ticket is not None and ticket > THRESHOLDS_AVANCADO["ticket_medio_brl"]:
        sinais.append(f"ticket_medio_brl={ticket:.0f} > R$30k")
    if ciclo is not None and ciclo > THRESHOLDS_AVANCADO["ciclo_dias"]:
        sinais.append(f"ciclo_dias={ciclo:.0f} > 30")
    if comite is not None and comite > THRESHOLDS_AVANCADO["comite_size"]:
        sinais.append(f"comite_size={comite:.0f} > 3")

    modo_detectado = "avancado" if sinais else "simples"
    return modo_detectado, sinais


def normalizar_modo(s: Any) -> str:
    if not isinstance(s, str):
        return "simples"
    t = s.strip().lower()
    if t in ("avancado", "avançado", "advanced", "opportunity", "b2b"):
        return "avancado"
    return "simples"


# ---------------------------------------------------------------------------
# benchmarks: semáforo calibrado por etapa
# ---------------------------------------------------------------------------


def parse_threshold_ref(spec: str) -> tuple[str, float] | None:
    """Parsea strings como '≥ 35%', '< 12%', '25-34%' (média), '20–29%'."""
    if not spec:
        return None
    s = spec.strip().replace("%", "").replace(",", ".").replace(" ", "")
    s = s.replace("–", "-").replace("—", "-")
    if s.startswith(("≥", ">=")):
        v = num(s.lstrip("≥>="))
        return ("gte", v) if v is not None else None
    if s.startswith(("≤", "<=")):
        v = num(s.lstrip("≤<="))
        return ("lte", v) if v is not None else None
    if s.startswith(">"):
        v = num(s.lstrip(">"))
        return ("gt", v) if v is not None else None
    if s.startswith("<"):
        v = num(s.lstrip("<"))
        return ("lt", v) if v is not None else None
    if "-" in s:
        partes = s.split("-")
        if len(partes) == 2:
            lo = num(partes[0])
            hi = num(partes[1])
            if lo is not None and hi is not None:
                return ("range", (lo + hi) / 2.0)
    v = num(s)
    return ("eq", v) if v is not None else None


def avaliar_semaforo(observado: float | None, taxa: dict[str, Any]) -> str:
    """Retorna 'verde' / 'amarelo' / 'vermelho' / '?' baseado no observado."""
    if observado is None:
        return "?"
    verde = parse_threshold_ref(str(taxa.get("verde") or ""))
    amarelo = parse_threshold_ref(str(taxa.get("amarelo") or ""))
    vermelho = parse_threshold_ref(str(taxa.get("vermelho") or ""))

    def match(rule: tuple[str, float] | None, x: float) -> bool:
        if rule is None:
            return False
        op, v = rule
        if v is None:
            return False
        if op == "gte":
            return x >= v
        if op == "lte":
            return x <= v
        if op == "gt":
            return x > v
        if op == "lt":
            return x < v
        if op == "range":
            return abs(x - v) / max(v, 1e-9) <= 0.5  # heurística broad
        if op == "eq":
            return abs(x - v) <= 0.5
        return False

    # ordem: vermelho > verde > amarelo (vermelho domina pra warning)
    if match(vermelho, observado):
        return "vermelho"
    if match(verde, observado):
        return "verde"
    if match(amarelo, observado):
        return "amarelo"
    return "?"


def emoji_semaforo(s: str) -> str:
    return {"verde": "🟢", "amarelo": "🟡", "vermelho": "🔴"}.get(s, "⚪")


# ---------------------------------------------------------------------------
# default document
# ---------------------------------------------------------------------------


def default_document() -> dict[str, Any]:
    return {
        "meta": {
            "cliente_projeto": "[Nome]",
            "versao_funil": "v1",
            "data": "YYYY-MM-DD",
            "responsavel": "",
            "link_plano_midia": "",
            "link_deoc": "",
            "link_protocolo_handoff": "",
            "link_benchmark": "",
        },
        "modo": "simples",
        "criterios_modo": {
            "ticket_medio_brl": None,
            "ciclo_dias": None,
            "comite_size": None,
            "segmento": "",
            "justificativa": "",
        },
        "concordancia": {
            "marketing_concorda": False,
            "vendas_concorda": False,
            "data_alinhamento": "",
        },
        "objetivo": {
            "conversao_final_que_importa": "",
            "lead_correto_definicao": "",
        },
        "as_is": {
            "marketing": "",
            "vendas": "",
            "ferramentas_resumo": "",
            "lacunas": "",
        },
        "to_be": {"notas_alinhamento": ""},
        "etapas": [
            {
                "ordem": 1,
                "nome": "",
                "definicao_passa": "",
                "evidencia_minima": "",
                "conversao_evento": "",
                "fonte_da_verdade": "",
                "dono_etapa": "",
                "handoff_protocolo_ref": "",
                "taxa_aceitavel": {
                    "verde": "",
                    "amarelo": "",
                    "vermelho": "",
                    "fonte_benchmark": "",
                },
                "campos_minimos": [
                    {"campo": "", "definicao_preenchimento": ""},
                ],
            },
            {
                "ordem": 2,
                "nome": "",
                "definicao_passa": "",
                "evidencia_minima": "",
                "conversao_evento": "",
                "fonte_da_verdade": "",
                "dono_etapa": "",
                "handoff_protocolo_ref": "",
                "taxa_aceitavel": {
                    "verde": "",
                    "amarelo": "",
                    "vermelho": "",
                    "fonte_benchmark": "",
                },
                "campos_minimos": [
                    {"campo": "", "definicao_preenchimento": ""},
                ],
            },
        ],
        "benchmarks_referencia": [
            {"transicao": "Lead → MQL", "verde": "≥ 35%", "amarelo": "25–34%", "vermelho": "< 12%", "fonte": "SmartBug 2024 / Forrester"},
            {"transicao": "MQL → SQL", "verde": "≥ 25%", "amarelo": "13–24%", "vermelho": "< 6%", "fonte": "SmartBug, Pedowitz Group 2024"},
            {"transicao": "SQL → Opportunity", "verde": "≥ 60%", "amarelo": "50–59%", "vermelho": "< 25%", "fonte": "Forrester B2B Revenue Waterfall 2021"},
            {"transicao": "Opportunity → Closed Won", "verde": "≥ 30%", "amarelo": "20–29%", "vermelho": "< 10%", "fonte": "B2B SaaS médio 2024"},
            {"transicao": "Lead Acceptance Rate", "verde": "≥ 50%", "amarelo": "30–49%", "vermelho": "< 20%", "fonte": "SmartBug 2024 (média 42%)"},
            {"transicao": "Customer → Retained 90d", "verde": "≥ 90%", "amarelo": "75–89%", "vermelho": "< 60%", "fonte": "Winning by Design Bowtie"},
        ],
        "sla_mkt_vendas": {
            "definicao_mql": "",
            "definicao_sql": "",
            "tempo_aceite_horas": None,
            "procedimento_devolucao": "",
            "motivos_devolucao_padronizados": [],
            "owner_marketing": "",
            "owner_vendas": "",
            "owner_funil": "",
            "cadencia_revisao": "Quinzenal nos 90 primeiros dias; mensal depois",
            "data_assinatura": "",
            "versao": "v1",
        },
        "automacao_crm": {
            "plataforma": "",
            "state_machine": [
                {"from_stage": "", "to_stage": "", "trigger": "", "regra_observavel": ""},
            ],
            "scoring_rule": {
                "definicao": "",
                "threshold_mql": "",
                "exemplos_pontos": [],
            },
            "webhook_out_stages": [],
            "endpoint_webhook": "",
        },
        "eventos_tracking": [
            {"evento": "", "etapa_relacionada": "", "nota": ""},
        ],
        "eventos_canonicos": [
            {"nome": "PageView", "origem": "front", "responsavel_disparo": "GTM Web", "etapa": "Visitante"},
            {"nome": "Lead", "origem": "front", "responsavel_disparo": "GTM Web (form submit)", "etapa": "Lead"},
            {"nome": "MQL", "origem": "server", "responsavel_disparo": "Webhook CRM via N8N", "etapa": "MQL"},
            {"nome": "NOICP", "origem": "front", "responsavel_disparo": "GTM Web (form submit anti-ICP)", "etapa": "Excluído"},
            {"nome": "LeadAccepted", "origem": "server", "responsavel_disparo": "Webhook CRM via N8N", "etapa": "SAL"},
            {"nome": "LeadQualified", "origem": "server", "responsavel_disparo": "Webhook CRM via N8N", "etapa": "SQL"},
            {"nome": "Opportunity", "origem": "server", "responsavel_disparo": "Webhook CRM via N8N", "etapa": "Opportunity"},
            {"nome": "DealWon", "origem": "server", "responsavel_disparo": "Webhook CRM via N8N", "etapa": "Closed Won"},
            {"nome": "CustomerRetained90d", "origem": "server", "responsavel_disparo": "Cron CRM via N8N", "etapa": "Retenção (Bowtie pós)"},
        ],
        "buying_group": {
            "champion": "",
            "economic_buyer": "",
            "decision_maker": "",
            "influencers_internos": [],
            "users": [],
            "ratifier": "",
            "gatekeeper": "",
            "influenciadores_externos": [],
        },
        "bowtie_etapas_posvenda": [
            {"ordem": 1, "nome": "Onboarding", "definicao_passa": "", "fonte_da_verdade": "", "kpi_principal": ""},
            {"ordem": 2, "nome": "Impact / Value Delivery", "definicao_passa": "", "fonte_da_verdade": "", "kpi_principal": ""},
            {"ordem": 3, "nome": "Expansion", "definicao_passa": "", "fonte_da_verdade": "", "kpi_principal": ""},
            {"ordem": 4, "nome": "Advocacy", "definicao_passa": "", "fonte_da_verdade": "", "kpi_principal": ""},
        ],
        "rpm_volumes": {
            "V1_awareness": None,
            "V5_mql": None,
            "V8_opportunity": None,
            "V11_won": None,
            "V13_expansion": None,
        },
        "rpm_conversion_rates": {
            "CR0_inquiry_to_mql": "",
            "CR1_mql_to_sql": "",
            "CR2_sql_to_opp": "",
            "CR3_opp_to_won": "",
            "CR4_won_to_expand": "",
        },
        "coerencia_operacao": {
            "capacidade_time": "",
            "ciclo_venda": "",
            "riscos_funil_impossivel": "",
        },
        "backlog": [
            {"item": "", "prioridade": "", "dono": ""},
        ],
        "gerenciado": {
            "kpis": [
                "% leads com status válido",
                "% campos mínimos preenchidos",
                "Tempo de ciclo por etapa",
                "Lead acceptance rate (SLA-bound)",
            ],
            "cadencia_revisao": "Quinzenal até estabilizar; mensal após",
            "dono_funil": "",
            "thresholds_resumo": "Vermelho: discrepância entre fontes ou etapa sem dono. Amarelo: muitas etapas e baixa adesão. Verde: rastreio mínimo e aderência.",
        },
    }


# ---------------------------------------------------------------------------
# render: seções markdown
# ---------------------------------------------------------------------------


def render_modo(d: dict[str, Any]) -> str:
    modo_decl = normalizar_modo(d.get("modo", "simples"))
    crit = d.get("criterios_modo") or {}
    modo_det, sinais = detectar_modo(crit)

    parts: list[str] = []
    parts.append("## 0. Modo do funil\n\n")
    parts.append(f"- **Modo declarado:** `{modo_decl}`\n")
    parts.append(f"- **Modo detectado (auto):** `{modo_det}`\n")
    if sinais:
        parts.append(f"- **Sinais de modo avançado:** {', '.join(sinais)}\n")
    if modo_decl != modo_det:
        parts.append(
            f"- ⚠️ **Divergência:** declarou `{modo_decl}` mas critérios apontam `{modo_det}`. "
            "Reavaliar antes de seguir (não há default neutro).\n"
        )
    parts.append(f"- **Segmento:** {block(crit.get('segmento'))}\n")
    parts.append(f"- **Justificativa:** {block(crit.get('justificativa'))}\n")
    parts.append("\n| Critério | Valor declarado |\n|---|---|\n")
    parts.append(f"| Ticket médio (BRL) | {block(crit.get('ticket_medio_brl'))} |\n")
    parts.append(f"| Ciclo (dias) | {block(crit.get('ciclo_dias'))} |\n")
    parts.append(f"| Comitê (stakeholders) | {block(crit.get('comite_size'))} |\n")
    parts.append("\n")
    return "".join(parts)


def render_benchmarks_globais(d: dict[str, Any]) -> str:
    bench = d.get("benchmarks_referencia") or []
    if not bench:
        return ""
    parts: list[str] = []
    parts.append("## Benchmarks 2024–2026 (faixas de referência)\n\n")
    parts.append("| Transição | Verde | Amarelo | Vermelho | Fonte |\n|---|---|---|---|---|\n")
    for b in bench:
        if not isinstance(b, dict):
            continue
        parts.append(
            f"| {block(b.get('transicao'))} | {block(b.get('verde'))} | "
            f"{block(b.get('amarelo'))} | {block(b.get('vermelho'))} | {block(b.get('fonte'))} |\n"
        )
    parts.append("\nRegra: vermelho = < 50% da faixa baixa. Sem benchmark explícito, não declarar 'está bom'.\n\n")
    return "".join(parts)


def render_etapas(d: dict[str, Any]) -> str:
    etapas = d.get("etapas") or []
    parts: list[str] = []
    parts.append("## 4. Etapas\n\n")
    for et in etapas:
        if not isinstance(et, dict):
            continue
        tax = et.get("taxa_aceitavel") or {}
        observado = num(et.get("conversion_rate_observado"))
        sem = avaliar_semaforo(observado, tax)
        emoji = emoji_semaforo(sem)

        parts.append(f"### Etapa {block(et.get('ordem'))} — {block(et.get('nome'))} {emoji}\n\n")
        parts.append(f"- **Definição de passou:** {block(et.get('definicao_passa'))}\n")
        parts.append(f"- **Evidência mínima:** {block(et.get('evidencia_minima'))}\n")
        parts.append(f"- **Evento conversão:** {block(et.get('conversao_evento'))}\n")
        parts.append(f"- **Fonte da verdade:** {block(et.get('fonte_da_verdade'))}\n")
        parts.append(f"- **Dono da etapa:** {block(et.get('dono_etapa'))}\n")
        parts.append(f"- **Handoff (protocolo):** {block(et.get('handoff_protocolo_ref'))}\n")
        if observado is not None:
            parts.append(
                f"- **Conversion rate observado:** {observado:.1f}% — semáforo: {emoji} `{sem}`\n"
            )
        parts.append("\n#### Taxas aceitáveis (calibradas)\n\n")
        parts.append(f"- 🟢 **Verde:** {block(tax.get('verde'))}\n")
        parts.append(f"- 🟡 **Amarelo:** {block(tax.get('amarelo'))}\n")
        parts.append(f"- 🔴 **Vermelho:** {block(tax.get('vermelho'))}\n")
        parts.append(f"- **Fonte faixa:** {block(tax.get('fonte_benchmark'))}\n")
        parts.append("\n#### Campos mínimos\n\n")
        for cm in et.get("campos_minimos") or []:
            if isinstance(cm, dict):
                parts.append(
                    f"- **{block(cm.get('campo'))}:** {block(cm.get('definicao_preenchimento'))}\n"
                )
        parts.append("\n")
    return "".join(parts)


def render_sla(d: dict[str, Any]) -> str:
    sla = d.get("sla_mkt_vendas") or {}
    parts: list[str] = []
    parts.append("## 8. SLA Marketing ↔ Vendas\n\n")
    parts.append(f"**Versão:** {block(sla.get('versao'))} — assinado em {block(sla.get('data_assinatura'))}\n\n")
    parts.append("### 1. Definição MQL (acordada)\n")
    parts.append(f"{block(sla.get('definicao_mql'))}\n\n")
    parts.append("### 2. Definição SQL (acordada)\n")
    parts.append(f"{block(sla.get('definicao_sql'))}\n\n")
    parts.append("### 3. Tempo de aceite (Lead Acceptance SLA)\n")
    h = sla.get("tempo_aceite_horas")
    if h is not None and num(h) is not None:
        parts.append(f"SDR aceita ou devolve em ≤ **{h}h úteis** após handoff automatizado do CRM.\n\n")
    else:
        parts.append("_[preencher: ex 24h úteis após handoff automatizado]_\n\n")
    parts.append("### 4. Procedimento de devolução / descarte / requalificação\n")
    parts.append(f"{block(sla.get('procedimento_devolucao'))}\n\n")
    motivos = sla.get("motivos_devolucao_padronizados") or []
    if motivos:
        parts.append("**Motivos padronizados (lista fechada):**\n")
        for m in motivos:
            parts.append(f"- `{m}`\n")
        parts.append("\n")
    parts.append("### 5. Ownership\n")
    parts.append(f"- **Owner Marketing:** {block(sla.get('owner_marketing'))}\n")
    parts.append(f"- **Owner Vendas:** {block(sla.get('owner_vendas'))}\n")
    parts.append(f"- **Owner Funil (governança end-to-end):** {block(sla.get('owner_funil'))}\n\n")
    parts.append("### 6. Cadência de revisão\n")
    parts.append(f"{block(sla.get('cadencia_revisao'))}\n\n")
    return "".join(parts)


def render_automacao_crm(d: dict[str, Any]) -> str:
    auto = d.get("automacao_crm") or {}
    sm = auto.get("state_machine") or []
    sm_real = [
        s
        for s in sm
        if isinstance(s, dict)
        and filled(s.get("from_stage"))
        and filled(s.get("to_stage"))
    ]
    scoring = auto.get("scoring_rule") or {}
    webhook_stages = auto.get("webhook_out_stages") or []

    parts: list[str] = []
    parts.append("## 7. Automação CRM (concreta — não descritiva)\n\n")
    parts.append(f"**Plataforma:** {block(auto.get('plataforma'))}\n\n")

    parts.append("### State machine (Mermaid)\n\n")
    if sm_real:
        parts.append("```mermaid\nstateDiagram-v2\n")
        for s in sm_real:
            f_ = str(s.get("from_stage") or "").strip()
            to = str(s.get("to_stage") or "").strip()
            trig = str(s.get("trigger") or "").strip()
            label = trig if trig else "trigger"
            parts.append(f"    {f_} --> {to}: {label}\n")
        parts.append("```\n\n")
        parts.append("**Regras observáveis (Pedowitz Group: handoff = system event, não judgment call):**\n\n")
        for s in sm_real:
            parts.append(
                f"- `{s.get('from_stage')}` → `{s.get('to_stage')}` "
                f"(trigger: {block(s.get('trigger'))}) — {block(s.get('regra_observavel'))}\n"
            )
        parts.append("\n")
    else:
        parts.append("⚠️ _State machine ausente — automação descritiva-só não cumpre DoD._\n\n")

    parts.append("### Scoring rule\n\n")
    parts.append(f"- **Definição:** {block(scoring.get('definicao'))}\n")
    parts.append(f"- **Threshold MQL:** {block(scoring.get('threshold_mql'))}\n")
    pts = scoring.get("exemplos_pontos") or []
    if pts:
        parts.append("- **Exemplos de pontos:**\n")
        for p in pts:
            parts.append(f"  - {p}\n")
    parts.append("\n")

    parts.append("### Webhook OUT por mudança de stage\n\n")
    parts.append(f"**Endpoint:** `{block(auto.get('endpoint_webhook'))}`\n\n")
    if webhook_stages:
        parts.append("**Stages que disparam webhook:**\n")
        for s in webhook_stages:
            parts.append(f"- `{s}`\n")
        parts.append("\n")
    parts.append("**Payload canônico (JSON):**\n\n")
    parts.append(
        "```json\n"
        "{\n"
        "  \"event_id\": \"uuid-v4\",\n"
        "  \"event_name\": \"<MQL|LeadAccepted|LeadQualified|Opportunity|DealWon>\",\n"
        "  \"timestamp\": \"ISO-8601\",\n"
        "  \"lead_id\": \"crm-internal-id\",\n"
        "  \"previous_stage\": \"<stage anterior>\",\n"
        "  \"new_stage\": \"<novo stage>\",\n"
        "  \"scoring_at_transition\": 0,\n"
        "  \"user_data\": {\"em\": \"sha256...\", \"ph\": \"sha256...\"}\n"
        "}\n```\n\n"
    )
    return "".join(parts)


def render_eventos_canonicos(d: dict[str, Any]) -> str:
    evs = d.get("eventos_canonicos") or []
    if not evs:
        return ""
    parts: list[str] = []
    parts.append("## Eventos canônicos do funil (input pra TE/IE)\n\n")
    parts.append("| Evento | Origem | Responsável disparo | Etapa |\n|---|---|---|---|\n")
    for e in evs:
        if not isinstance(e, dict):
            continue
        parts.append(
            f"| `{block(e.get('nome'))}` | {block(e.get('origem'))} | "
            f"{block(e.get('responsavel_disparo'))} | {block(e.get('etapa'))} |\n"
        )
    parts.append(
        "\nServer-side: `event_id` UUID v4 + hash SHA-256 (email lowercase trimado, "
        "phone E.164) pra dedup CAPI.\n\n"
    )
    return "".join(parts)


def render_avancado(d: dict[str, Any]) -> str:
    """Renderiza buying group + bowtie + RPM (modo avançado)."""
    if normalizar_modo(d.get("modo")) != "avancado":
        return ""
    parts: list[str] = []
    parts.append("## 9. Avançado — Buying Group / Bowtie / RPM\n\n")

    bg = d.get("buying_group") or {}
    parts.append("### Buying group (Forrester 2021)\n\n")
    parts.append(f"- **Champion:** {block(bg.get('champion'))}\n")
    parts.append(f"- **Economic Buyer:** {block(bg.get('economic_buyer'))}\n")
    parts.append(f"- **Decision Maker:** {block(bg.get('decision_maker'))}\n")
    parts.append(f"- **Ratifier:** {block(bg.get('ratifier'))}\n")
    parts.append(f"- **Gatekeeper:** {block(bg.get('gatekeeper'))}\n")
    infl = bg.get("influencers_internos") or []
    if infl:
        parts.append(f"- **Influencers internos:** {', '.join(str(x) for x in infl)}\n")
    users = bg.get("users") or []
    if users:
        parts.append(f"- **Users:** {', '.join(str(x) for x in users)}\n")
    ext = bg.get("influenciadores_externos") or []
    if ext:
        parts.append(f"- **Influenciadores externos:** {', '.join(str(x) for x in ext)}\n")
    parts.append("\n")

    bw = d.get("bowtie_etapas_posvenda") or []
    if bw:
        parts.append("### Bowtie pós-venda (Winning by Design)\n\n")
        parts.append("| Ordem | Etapa | Definição | Fonte da verdade | KPI |\n|---|---|---|---|---|\n")
        for e in bw:
            if not isinstance(e, dict):
                continue
            parts.append(
                f"| {block(e.get('ordem'))} | {block(e.get('nome'))} | "
                f"{block(e.get('definicao_passa'))} | {block(e.get('fonte_da_verdade'))} | "
                f"{block(e.get('kpi_principal'))} |\n"
            )
        parts.append("\n")

    rpm_v = d.get("rpm_volumes") or {}
    rpm_cr = d.get("rpm_conversion_rates") or {}
    if rpm_v or rpm_cr:
        parts.append("### RPM — Revenue Performance Model (Forrester)\n\n")
        parts.append("**Volumes:**\n")
        parts.append(f"- V1 Awareness: {block(rpm_v.get('V1_awareness'))}\n")
        parts.append(f"- V5 MQL: {block(rpm_v.get('V5_mql'))}\n")
        parts.append(f"- V8 Opportunity: {block(rpm_v.get('V8_opportunity'))}\n")
        parts.append(f"- V11 Won: {block(rpm_v.get('V11_won'))}\n")
        parts.append(f"- V13 Expansion: {block(rpm_v.get('V13_expansion'))}\n\n")
        parts.append("**Conversion rates:**\n")
        parts.append(f"- CR0 inquiry→MQL: {block(rpm_cr.get('CR0_inquiry_to_mql'))}\n")
        parts.append(f"- CR1 MQL→SQL: {block(rpm_cr.get('CR1_mql_to_sql'))}\n")
        parts.append(f"- CR2 SQL→Opp: {block(rpm_cr.get('CR2_sql_to_opp'))}\n")
        parts.append(f"- CR3 Opp→Won: {block(rpm_cr.get('CR3_opp_to_won'))}\n")
        parts.append(f"- CR4 Won→Expand: {block(rpm_cr.get('CR4_won_to_expand'))}\n\n")
    return "".join(parts)


def render_md(d: dict[str, Any]) -> str:
    m = d.get("meta") or {}
    conc = d.get("concordancia") or {}
    obj = d.get("objetivo") or {}
    as_is = d.get("as_is") or {}
    to_be = d.get("to_be") or {}
    co = d.get("coerencia_operacao") or {}
    ger = d.get("gerenciado") or {}

    parts: list[str] = []
    parts.append("# Funil unificado (A-2) — consolidado\n\n")
    parts.append("## Cabeçalho\n\n")
    parts.append(
        "| Campo | Valor |\n|---|---|\n"
        f"| Cliente/projeto | {block(m.get('cliente_projeto'))} |\n"
        f"| Versão | {block(m.get('versao_funil'))} |\n"
        f"| Data | {block(m.get('data'))} |\n"
        f"| Responsável | {block(m.get('responsavel'))} |\n"
        f"| Plano mídia | {block(m.get('link_plano_midia'))} |\n"
        f"| DEOC | {block(m.get('link_deoc'))} |\n"
        f"| Protocolo handoff | {block(m.get('link_protocolo_handoff'))} |\n"
        f"| Benchmark | {block(m.get('link_benchmark'))} |\n\n"
    )

    parts.append(render_modo(d))

    parts.append("## Concordância (DoD)\n\n")
    parts.append(
        f"- Marketing concorda: **{conc.get('marketing_concorda')}**\n"
        f"- Vendas concorda: **{conc.get('vendas_concorda')}**\n"
        f"- Data alinhamento: {block(conc.get('data_alinhamento'))}\n\n"
    )
    parts.append("## 1. Objetivo\n\n")
    parts.append(
        f"- **Conversão final que importa:** {block(obj.get('conversao_final_que_importa'))}\n"
        f"- **Lead correto:** {block(obj.get('lead_correto_definicao'))}\n\n"
    )
    parts.append("## 2. AS IS\n\n")
    parts.append(f"### Marketing\n\n{block(as_is.get('marketing'))}\n\n")
    parts.append(f"### Vendas\n\n{block(as_is.get('vendas'))}\n\n")
    parts.append(f"### Ferramentas\n\n{block(as_is.get('ferramentas_resumo'))}\n\n")
    parts.append(f"### Lacunas\n\n{block(as_is.get('lacunas'))}\n\n")
    parts.append("## 3. TO BE (vocabulário)\n\n")
    parts.append(f"{block(to_be.get('notas_alinhamento'))}\n\n")

    parts.append(render_benchmarks_globais(d))
    parts.append(render_etapas(d))

    parts.append("## 5. Eventos de tracking\n\n")
    for ev in d.get("eventos_tracking") or []:
        if isinstance(ev, dict):
            parts.append(
                f"- **{block(ev.get('evento'))}** → etapa {block(ev.get('etapa_relacionada'))} — {block(ev.get('nota'))}\n"
            )
    parts.append("\n")

    parts.append(render_eventos_canonicos(d))

    parts.append("## 6. Coerência operação\n\n")
    parts.append(f"- **Capacidade time:** {block(co.get('capacidade_time'))}\n")
    parts.append(f"- **Ciclo venda:** {block(co.get('ciclo_venda'))}\n")
    parts.append(f"- **Riscos:** {block(co.get('riscos_funil_impossivel'))}\n\n")

    parts.append(render_automacao_crm(d))
    parts.append(render_sla(d))
    parts.append(render_avancado(d))

    parts.append("## Backlog\n\n")
    for b in d.get("backlog") or []:
        if isinstance(b, dict):
            parts.append(
                f"- **{block(b.get('prioridade'))}** · {block(b.get('item'))} — dono: {block(b.get('dono'))}\n"
            )
    parts.append("\n## Gerenciado\n\n")
    for k in ger.get("kpis") or []:
        parts.append(f"- KPI: {k}\n")
    parts.append(f"\n**Cadência:** {block(ger.get('cadencia_revisao'))}\n\n")
    parts.append(f"**Dono funil:** {block(ger.get('dono_funil'))}\n\n")
    parts.append(f"**Thresholds:** {block(ger.get('thresholds_resumo'))}\n")
    return "".join(parts)


# ---------------------------------------------------------------------------
# audit
# ---------------------------------------------------------------------------


def audit(d: dict[str, Any]) -> list[str]:
    issues: list[str] = []

    # --- meta + objetivo
    m = d.get("meta") or {}
    if not filled(m.get("cliente_projeto")):
        issues.append("meta.cliente_projeto")
    obj = d.get("objetivo") or {}
    if not filled(obj.get("conversao_final_que_importa")):
        issues.append("objetivo.conversao_final_que_importa")
    if not filled(obj.get("lead_correto_definicao")):
        issues.append("objetivo.lead_correto_definicao")
    as_is = d.get("as_is") or {}
    for k in ("marketing", "vendas", "ferramentas_resumo"):
        if not filled(as_is.get(k)):
            issues.append(f"as_is.{k}")

    # --- modo declarado vs detectado
    modo_decl = normalizar_modo(d.get("modo", "simples"))
    crit = d.get("criterios_modo") or {}
    modo_det, sinais = detectar_modo(crit)
    if modo_decl != modo_det:
        if modo_decl == "simples" and modo_det == "avancado":
            issues.append(
                f"⚠️ modo: declarou 'simples' mas critérios apontam 'avancado' "
                f"({', '.join(sinais)}) — reavaliar (não há default neutro)"
            )
        elif modo_decl == "avancado" and modo_det == "simples":
            issues.append(
                "⚠️ modo: declarou 'avancado' mas critérios não indicam ticket/ciclo/comitê grandes — "
                "confirmar que é mesmo opportunity-centric ou voltar pra 'simples'"
            )

    # --- etapas
    etapas = [e for e in (d.get("etapas") or []) if isinstance(e, dict)]
    if len(etapas) < 2:
        issues.append("etapas: mínimo 2 etapas end-to-end")
    etapas_sem_benchmark = 0
    for i, et in enumerate(etapas, 1):
        pr = f"etapa[{i}]"
        for k in (
            "nome",
            "definicao_passa",
            "evidencia_minima",
            "conversao_evento",
            "fonte_da_verdade",
        ):
            if not filled(et.get(k)):
                issues.append(f"{pr}.{k}")
        tax = et.get("taxa_aceitavel") or {}
        algum_filled = any(filled(tax.get(tk)) for tk in ("verde", "amarelo", "vermelho"))
        if not algum_filled:
            etapas_sem_benchmark += 1
        for tk in ("verde", "amarelo", "vermelho", "fonte_benchmark"):
            if not filled(tax.get(tk)):
                issues.append(f"{pr}.taxa_aceitavel.{tk}")
        cms = [c for c in (et.get("campos_minimos") or []) if isinstance(c, dict)]
        real = [
            c
            for c in cms
            if filled(c.get("campo")) and filled(c.get("definicao_preenchimento"))
        ]
        if not real:
            issues.append(f"{pr}.campos_minimos (≥1 campo com nome e regra)")
    if etapas and etapas_sem_benchmark == len(etapas):
        issues.append(
            "⚠️ benchmarks: nenhuma etapa tem faixa verde/amarelo/vermelho preenchida — "
            "sem benchmark calibrado, não declare 'está bom'"
        )

    # --- handoff
    has_handoff = filled(m.get("link_protocolo_handoff")) or any(
        filled(e.get("handoff_protocolo_ref")) for e in etapas
    )
    if not has_handoff:
        issues.append("handoff: meta.link_protocolo_handoff ou etapas[].handoff_protocolo_ref")

    # --- eventos tracking + canônicos
    evs = [e for e in (d.get("eventos_tracking") or []) if isinstance(e, dict) and filled(e.get("evento"))]
    if not evs:
        issues.append("eventos_tracking: ≥1 evento nomeado")

    evs_can = [e for e in (d.get("eventos_canonicos") or []) if isinstance(e, dict) and filled(e.get("nome"))]
    canonicos_minimos = {"Lead", "MQL", "LeadQualified", "DealWon"}
    nomes_can = {str(e.get("nome")).strip() for e in evs_can}
    faltantes = canonicos_minimos - nomes_can
    if faltantes:
        issues.append(
            f"⚠️ eventos_canonicos: faltam {sorted(faltantes)} (TE/IE precisam pra instrumentar)"
        )

    # --- coerência operação
    co = d.get("coerencia_operacao") or {}
    if not filled(co.get("capacidade_time")):
        issues.append("coerencia_operacao.capacidade_time")
    if not filled(co.get("ciclo_venda")):
        issues.append("coerencia_operacao.ciclo_venda")

    # --- backlog
    backlog = [b for b in (d.get("backlog") or []) if isinstance(b, dict) and filled(b.get("item"))]
    if not backlog:
        issues.append("backlog: ≥1 item priorizado")

    # --- concordância
    conc = d.get("concordancia") or {}
    if not conc.get("marketing_concorda") or not conc.get("vendas_concorda"):
        issues.append("(aviso) concordancia: confirmar marketing_concorda e vendas_concorda no DoD")

    ger = d.get("gerenciado") or {}
    if not filled(ger.get("dono_funil")):
        issues.append("(aviso) gerenciado.dono_funil — canônico registra lacuna de dono")

    # --- SLA
    sla = d.get("sla_mkt_vendas") or {}
    sla_keys_obrigatorias = (
        "definicao_mql",
        "definicao_sql",
        "tempo_aceite_horas",
        "procedimento_devolucao",
        "owner_marketing",
        "owner_vendas",
    )
    sla_faltando = [k for k in sla_keys_obrigatorias if not filled(sla.get(k))]
    if not sla or sla_faltando:
        issues.append(
            f"⚠️ SLA Mkt+Vendas ausente/incompleto (faltam: {', '.join(sla_faltando) or 'tudo'}) — "
            "sem SLA escrito o funil é pôster"
        )

    # --- automação CRM
    auto = d.get("automacao_crm") or {}
    sm = [
        s
        for s in (auto.get("state_machine") or [])
        if isinstance(s, dict) and filled(s.get("from_stage")) and filled(s.get("to_stage"))
    ]
    scoring = auto.get("scoring_rule") or {}
    webhook = auto.get("webhook_out_stages") or []
    endpoint = auto.get("endpoint_webhook")

    falta_state = not sm
    falta_scoring = not (filled(scoring.get("definicao")) or filled(scoring.get("threshold_mql")))
    falta_webhook = not (webhook or filled(endpoint))

    if falta_state and falta_scoring and falta_webhook:
        issues.append(
            "⚠️ automação CRM descritiva-só (sem state machine, sem scoring rule, sem webhook) — "
            "DoD exige automação concreta"
        )
    else:
        if falta_state:
            issues.append("automacao_crm.state_machine ausente (Pedowitz: handoff = system event)")
        if falta_scoring:
            issues.append("automacao_crm.scoring_rule ausente (regra observável)")
        if falta_webhook:
            issues.append("automacao_crm.webhook_out_stages / endpoint_webhook ausente")

    # --- modo avançado: buying group + bowtie + RPM
    if modo_decl == "avancado":
        bg = d.get("buying_group") or {}
        papeis_chave = ("champion", "economic_buyer", "decision_maker")
        preenchidos = sum(1 for p in papeis_chave if filled(bg.get(p)))
        users = bg.get("users") or []
        infl = bg.get("influencers_internos") or []
        total_papeis = preenchidos + (1 if users else 0) + (1 if infl else 0)
        if total_papeis < 4:
            issues.append(
                "⚠️ modo avançado sem buying group Forrester (≥4 papéis: Champion + Economic Buyer + "
                "Decision Maker + 1 User/Influencer)"
            )

        bw = [e for e in (d.get("bowtie_etapas_posvenda") or []) if isinstance(e, dict) and filled(e.get("nome"))]
        bw_def = [e for e in bw if filled(e.get("fonte_da_verdade"))]
        if len(bw_def) < 2:
            issues.append(
                "⚠️ modo avançado sem Bowtie pós-venda (≥2 etapas com fonte da verdade — ex Onboarding + Impact)"
            )

        rpm_v = d.get("rpm_volumes") or {}
        rpm_cr = d.get("rpm_conversion_rates") or {}
        v_filled = sum(1 for k in ("V1_awareness", "V5_mql", "V8_opportunity", "V11_won", "V13_expansion") if filled(rpm_v.get(k)))
        cr_filled = sum(1 for k in ("CR0_inquiry_to_mql", "CR1_mql_to_sql", "CR2_sql_to_opp", "CR3_opp_to_won", "CR4_won_to_expand") if filled(rpm_cr.get(k)))
        if v_filled < 3 or cr_filled < 3:
            issues.append(
                f"⚠️ modo avançado: RPM Forrester incompleto (volumes preenchidos={v_filled}/5, "
                f"conversion rates={cr_filled}/5; mínimo 3+3)"
            )

    return issues


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description="Funil unificado A-2 (playbook 17)")
    parser.add_argument("input_json", nargs="?", type=Path)
    parser.add_argument("--md", dest="md_path", type=Path)
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--write-default", dest="out_json", type=Path)
    args = parser.parse_args()

    if args.out_json:
        args.out_json.write_text(
            json.dumps(default_document(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Escrito: {args.out_json}")
        return

    if not args.input_json:
        parser.error("informe input_json ou --write-default")

    d = load(args.input_json)
    if args.audit:
        xs = audit(d)
        print("Lacunas / avisos (funil A-2 / playbook 17):")
        if not xs:
            print("  - (nenhuma lacuna detectada)")
        for x in xs:
            print(f"  - {x}")
        return

    if args.md_path:
        args.md_path.write_text(render_md(d), encoding="utf-8")
        print(f"Escrito: {args.md_path}")
    else:
        print(render_md(d), end="")


if __name__ == "__main__":
    main()
