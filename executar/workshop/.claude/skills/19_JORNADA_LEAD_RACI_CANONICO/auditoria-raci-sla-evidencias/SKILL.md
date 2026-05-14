---
name: auditoria-raci-sla-evidencias
description: Audita aderência à jornada/RACI em operação — donos por etapa, handoffs com responsável, evidência mínima no CRM, SLA com enforcement e ação quando estoura — com diagnóstico verde/amarelo/vermelho do playbook 19 § Gerenciado. Complementa `jornada-lead-raci` com evidências de CRM e A-4.
---

# Auditoria — RACI, SLA e evidências

## Fonte canônica

Playbook **`19_JORNADA_LEAD_RACI_CANONICO.md`**, seção **Como gerenciar (Gerenciado)**:

- **KPIs:** % etapas com dono; % violações de SLA; % etapas sem evidência mínima.
- **Thresholds:** vermelho — etapas sem dono; handoff sem responsável; lead “sumindo”; amarelo — dono sem evidência; SLA estoura sem ação; verde — dono + evidência + ação definida quando estoura.
- **Cadência:** mensal ou ao trocar estrutura do time; **change log do RACI** obrigatório para mudanças de papel.

## Propósito

Verificar se o artefato **`jornada-lead-raci`** (e o que foi acordado no funil A-2 e protocolo A-4) **bate com a prática**: rastro mínimo, donos reais e SLA com consequência.

## Quando usar

- Cadência **mensal** ou após mudança de time/handoff.
- Junto ou após **`auditoria-aderencia-handoff-a4`** quando o sintoma for “ninguém é dono” ou lead some.
- Antes de registrar mudanças no **`changelog-raci-jornada`** (use a auditoria para embasar o "antes/depois").

## Pré-requisitos

- **`jornada-lead-raci.json`** (ou consolidado) como referência.
- Acesso a amostra CRM / relatórios de SLA / atas de handoff.

## Workflow

1. Referenciar `meta` com links ao artefato RACI, funil A-2 e protocolo A-4.
2. Preencher **KPIs quantitativos** quando disponíveis (% dono, % violações SLA, % sem evidência).
3. Avaliar cada **dimensão** com semáforo + evidência.
4. Registrar **achados críticos**, **backlog** e próxima revisão.
5. Se houver alteração de RACI/evidência/SLA no artefato, abrir entrada em **`changelog-raci-jornada`** e alinhar `versao_artefato` em **`jornada-lead-raci`**.

```bash
python3 scripts/evaluate_auditoria_raci.py --write-default templates/auditoria-raci.json
python3 scripts/evaluate_auditoria_raci.py templates/auditoria-raci.json --md ./relatorio-auditoria-raci.md
python3 scripts/evaluate_auditoria_raci.py templates/auditoria-raci.json --summary
python3 scripts/evaluate_auditoria_raci.py templates/auditoria-raci.json --audit
```

## Consolidado (heurística)

- **Vermelho** se dimensão crítica em vermelho **ou** `achados_criticos` preenchido.
- **Amarelo** se houver amarelo e nenhum vermelho.
- **Verde** se apenas verde/`n.a.` aplicável.
- **Incompleto** se dimensão obrigatória sem semáforo.

Parecer humano em `meta.parecer_humano`.

## Artefatos

- `reference.md`
- `templates/auditoria-raci.md`
- `templates/auditoria-raci.json`
- `scripts/evaluate_auditoria_raci.py`

## Definition of Done (rodada)

Meta e período descritos; KPIs ou justificativa “não medido”; dimensões preenchidas; consolidado sugerido; backlog ou explícito “sem ação corretiva nesta rodada”.
