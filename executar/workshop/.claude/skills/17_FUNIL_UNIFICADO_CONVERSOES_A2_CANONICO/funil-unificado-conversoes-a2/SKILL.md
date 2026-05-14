---
name: funil-unificado-conversoes-a2
description: Desenha o Funil Unificado (A-2) em **modo simples (lead-centric, B2C/PME/SaaS PLG)** ou **modo avançado (opportunity/buying-group, Forrester B2B Revenue Waterfall 2021 + Bowtie Winning by Design)** com etapas, definições únicas Marketing+Vendas, eventos, fonte da verdade, campos mínimos, handoffs, conversion rates de referência (Lead→MQL ~30%, MQL→SQL 13-25%, SQL→Won 20-30% B2B SaaS) e backlog — antes do contrato de dados, CRM/SLA e setup de campanhas. Entrega obrigatória: SLA Mkt↔Vendas escrito + automação CRM concreta (state machine, scoring rule, webhook). Fonte playbook 17.
---

# Funil unificado — conversões (A-2)

## Fonte canônica

Playbook **`17_FUNIL_UNIFICADO_CONVERSOES_A2_CANONICO.md`** (e legado `04-funil-unificado-a2.md` alinhado ao mesmo conteúdo).

## Propósito (1 frase)

Definir o fluxo end-to-end do lead (geração → venda/drop) com **vocabulário único** e **fonte da verdade** por etapa, para tracking, CRM e otimização não competirem entre áreas.

## Quando usar / quando não

**Usar** antes de fechar Plano de Mídia, antes de implementar tracking/CRM como fonte da verdade, ou quando há definições conflitantes entre áreas. **Não usar** para redesenhar organograma — foco é fluxo, definições e evidência (§ “Quando usar”).

## Entradas

Plano de mídia; DEOC; AS IS (comercial, time, ferramentas); benchmark de conversão por etapa; objetivo de conversão e “lead correto” (§ Entradas).

## Dependências recomendadas

- **`benchmark-campo-batalha-gtm`** ou materiais de benchmark do segmento (faixas por etapa).
- **`contrato-dados-marketing-crm`** — aplicado **depois** que o funil v1 existir.
- **`protocolo-handoff-mql-sql-a4`** — vincular `link_protocolo_handoff` / artefato A-4 quando existir (playbook 18).
- **`jornada-lead-raci`** — donos R/A/C/I e touchpoints por etapa (playbook 19); complementa governança pós-definição do funil.

## Workflow (passos 1–7 do canônico + extensões 2026)

0. **Escolha de modo** (gate antes do passo 1):
   - **Simples (lead-centric)** — B2C, PME, SaaS PLG self-serve, Mkt e Vendas mesma pessoa/time. Etapas: Visitante → Lead → Cliente → Retenção/Upsell.
   - **Avançado (opportunity-centric)** — B2B enterprise, ciclo >30d, ticket >R$10k, comitê de compra. Use Forrester B2B Revenue Waterfall 2021 (Opportunity como unidade, não Lead) + Bowtie Winning by Design (pré-venda + pós-venda simétricos: Awareness/Education/Selection → Onboarding/Expansion/Advocacy). Buying group: 13 stakeholders + 9 influenciadores externos.
   - Critério: ticket + ciclo + tipo de decisor. Documente a escolha — não há "default neutro".
1. Objetivo do funil: conversão final que importa + definição de lead correto.
2. AS IS Marketing e Vendas: origem, atendimento, perdas e sumiço de lead.
3. TO BE: etapas propostas e **um nome/Definição por etapa** alinhados entre áreas.
4. Por etapa: critério "passou", evidência mínima, faixa verde/amarelo/vermelho (com fonte — usar **Conversion Rates de Referência** abaixo), **uma** fonte da verdade, campos mínimos com regra de preenchimento; handoffs.
5. Eventos de tracking necessários para sustentar o funil (entrada pra `tracking-engineer` / IE).
6. Coerência com capacidade do time e ciclo (funil operável).
7. **Automação CRM concreta** (não descrição teórica) por handoff:
   - State machine no CRM (HubSpot Workflow / RD Automation / Pipedrive Workflow) com estados e transições nomeadas
   - Scoring rule (regra observável: ex "lead_score ≥ 70 + cargo in (CMO, Head Marketing) → MQL")
   - Webhook OUT por mudança de stage (pra alimentar tracking server-side e BI)
8. **Handoff é system event, não judgment call** (Pedowitz Group). Regra automatizada no CRM dispara mudança de status no instante em que critério é atingido. SDR/AE não decide se promove — sistema promove e SDR só executa próxima ação. Sem isso, funil é pôster.
9. Publicar artefato + **SLA Mkt↔Vendas escrito** (definição MQL/SQL, tempo de aceite, procedimento de devolução/descarte/requalificação) + **backlog** (campos, integrações, treino, adoção).

## Conversion Rates de Referência (benchmarks 2024-2026, B2B SaaS típico)

Use como semáforo amarelo/vermelho na faixa por etapa, ajustando por segmento:

| Transição | Faixa de referência | Fonte |
|-----------|--------------------|-------|
| Lead → MQL | 25-35% | Forrester / SmartBug |
| MQL → SQL | 13-25% | SmartBug, Pedowitz Group |
| SQL → Opportunity | 50-60% | Forrester B2B Revenue Waterfall |
| Opportunity → Closed Won | 20-30% | B2B SaaS médio |
| Lead Acceptance Rate (SDR aceita MQL) | 42% médio | SmartBug |

Vermelho: <50% da faixa baixa. Amarelo: dentro/abaixo da faixa. Verde: ≥faixa alta. Sem benchmark calibrado, não declare "está bom".

Em paralelo, preencher **`templates/funil-unificado-a2.json`** (recomendado) e gerar o Markdown de leitura:

```bash
python3 scripts/build_funil_unificado_a2.py templates/funil-unificado-a2.json --md ./funil-unificado-a2-consolidado.md
python3 scripts/build_funil_unificado_a2.py templates/funil-unificado-a2.json --audit
```

Quem preferir editar em prosa pode usar **`templates/funil-unificado-a2.md`** como espelho das seções e depois transcrever para o JSON.

## Outputs (funil v1)

Etapas com definição; evento que "conta"; taxas aceitáveis (faixas calibradas com benchmarks 2024-2026); fonte da verdade; campos mínimos; pontos de handoff ligados ao protocolo — conforme § Saídas do playbook.

**Outputs obrigatórios adicionais:**
- **Modo escolhido** (simples / avançado) com critério documentado.
- **SLA Mkt↔Vendas escrito** — definição MQL/SQL/SAL/Opportunity acordada, tempo de aceite SLA-bound (ex: 24h úteis), procedimento de devolução/descarte/requalificação. Sem isso, funil é pôster.
- **Automação CRM concreta** — state machine no CRM (HubSpot/RD/Pipedrive), scoring rule observável, webhook OUT por mudança de stage. NÃO descrição teórica.

## Definition of Done (playbook)

Etapas nomeadas e definidas com acordo Mkt+Vendas; fonte da verdade **uma por etapa**; campos mínimos com definição; handoffs identificados; backlog priorizado (§ DoD).

## Gerenciamento contínuo

KPIs sugeridos, thresholds e cadência quinzenal→mensal estão no JSON (`gerenciado`) e no `reference.md`. **Change log** obrigatório para mudanças: skill **`changelog-funil-conversoes`**. **Rodadas de governança:** após publicar o A-2, usar **`auditoria-funil-fontes-verdade`** na cadência do § Gerenciado (playbook 17).

## Artefatos

- `reference.md` — mapa § playbook ↔ campos do template.
- `templates/funil-unificado-a2.md`
- `templates/funil-unificado-a2.json`
- `scripts/build_funil_unificado_a2.py`

## Skill irmã

- **`tracking-engineer`** — funil A-2 define quais eventos canônicos a IE/TE precisam instrumentar (Lead, MQL, SQL, Opportunity, Won). Funil é o *measurement plan*; TE é o *tagging plan*. Sem A-2 acordado, TE recusa configurar tags de qualificação (gera dado tecnicamente correto e business inutilizável).
