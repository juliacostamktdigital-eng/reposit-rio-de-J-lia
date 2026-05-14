# Referência — Funil unificado A-2 ↔ playbook 17

Canônico: `17_FUNIL_UNIFICADO_CONVERSOES_A2_CANONICO.md`.

## Modo simples vs avançado (passo 0)

Decisão **antes** do passo 1. Não há "default neutro" — declare e justifique.

| Critério | Simples (lead-centric) | Avançado (opportunity-centric) |
|----------|------------------------|--------------------------------|
| Segmento típico | B2C, PME, SaaS PLG self-serve | B2B mid-market / enterprise |
| Ticket médio (BRL) | < R$ 30k | ≥ R$ 30k |
| Ciclo de venda | < 30 dias | ≥ 30 dias |
| Decisor | 1 pessoa (ou casal) | Comitê ≥ 3 stakeholders |
| Unidade do funil | Lead | Opportunity / Buying Group |
| Framework | AIDA / clássico | Forrester B2B Revenue Waterfall 2021 + Bowtie WbD |
| Etapas pós-venda | Cliente, retenção (opcional) | Onboarding → Expansão → Advocacia (simétrico ao pré) |

### Exemplos modo simples (3)
1. **DTC de cosmético** — ticket R$ 180, ciclo < 1h, decisão individual, funil Visitante → Lead → Cliente → Recomprador.
2. **Curso digital R$ 1.997** — checkout direto, decisor único, funil Visitante → Lead → Aluno → Renovação.
3. **SaaS PLG R$ 99/mo self-serve** — trial sem SDR, comitê de 1 (head de marketing solo), funil Visitante → Trial → Pago → Expansão.

### Exemplos modo avançado (3)
1. **ERP industrial R$ 200k/ano** — comitê de TI + Operações + Diretor Financeiro + procurement, ciclo 4–9 meses, RFP formal. Bowtie completo.
2. **Consultoria estratégica R$ 80k/projeto** — Champion (gerente) + Economic Buyer (CFO) + 2 influencers, ciclo 2–4 meses, opportunity-centric.
3. **Plataforma martech R$ 50k/ano** — Champion (Head Mkt) + IT Security + Legal + CFO, ciclo 3–6 meses, RPM Forrester aplicado.

## Conversion rates de referência (benchmarks 2024–2026)

Use como base de calibragem das faixas verde/amarelo/vermelho. Ajuste por segmento e maturidade.

| Transição | Faixa de referência | Verde | Amarelo | Vermelho | Fonte |
|-----------|--------------------|-------|---------|----------|-------|
| Lead → MQL | 25–35% | ≥ 35% | 25–34% | < 12% | SmartBug 2024, Forrester |
| MQL → SQL | 13–25% | ≥ 25% | 13–24% | < 6% | SmartBug, Pedowitz Group 2024 |
| SQL → Opportunity | 50–60% | ≥ 60% | 50–59% | < 25% | Forrester B2B Revenue Waterfall 2021 |
| Opportunity → Closed Won | 20–30% | ≥ 30% | 20–29% | < 10% | B2B SaaS médio 2024 |
| Lead Acceptance Rate (SDR aceita MQL) | 42% médio | ≥ 50% | 30–49% | < 20% | SmartBug 2024 |
| Customer → Retained 90d | 75–90% (B2B SaaS) | ≥ 90% | 75–89% | < 60% | Winning by Design Bowtie |

**Regra**: vermelho = < 50% da faixa baixa. Sem benchmark explícito, não declare "está bom".

### Fontes citadas
- **SmartBug Media** — *2024 B2B Conversion Rate Benchmarks*.
- **Pedowitz Group** — *Lead Management Maturity Model* + *Handoff is a System Event*.
- **Forrester** — *B2B Revenue Waterfall 2021* (opportunity-centric, buying group de 13 stakeholders + 9 influenciadores externos, RPM V1–V13 + CR0–CR4).
- **Winning by Design** — *Bowtie Funnel*, *Pirate Funnel*, *SaaS Revenue Operating Model*.

## SLA Mkt+Vendas (template obrigatório)

Sem isso, o funil é pôster. Documento curto, escrito, assinado por ambas as áreas.

```
SLA MARKETING ↔ VENDAS — vNN — assinado em DD/MM/AAAA

1. DEFINIÇÃO MQL (acordada)
   Lead que: <critério explícito ex: cargo in [CMO, Head Mkt, Diretor Mkt]
   AND empresa size ≥ 50 funcionários
   AND lead_score ≥ 70 (regra detalhada em scoring rule §5)>.

2. DEFINIÇÃO SQL (acordada)
   MQL aceito por SDR + reunião agendada (status=meeting_booked) + BANT/MEDDIC parcial confirmado.

3. TEMPO DE ACEITE (Lead Acceptance SLA)
   SDR aceita ou devolve MQL em ≤ 24h úteis após handoff automatizado do CRM.
   Se passar de 24h sem ação → reabre alerta + escala pra gerente comercial.

4. PROCEDIMENTO DE DEVOLUÇÃO / DESCARTE / REQUALIFICAÇÃO
   - Devolução com motivo padronizado (lista fechada: out_of_icp, sem_budget, sem_timing, dado_invalido).
   - Devolvido com motivo "sem_timing" volta pro nurturing de Mkt (workflow X).
   - Devolvido com motivo "out_of_icp" exclui do funil + alimenta exclusion audience nas plataformas.
   - Requalificação só se houver evento novo (job change, sinal de intenção, novo cargo).

5. OWNERSHIP
   Owner Mkt: <pessoa>.
   Owner Vendas: <pessoa>.
   Owner Funil (governança end-to-end): <pessoa>.

6. CADÊNCIA DE REVISÃO
   Quinzenal nos 90 primeiros dias; mensal depois.
```

## Automação CRM concreta (não descrição teórica)

### State machine (exemplo HubSpot / RD Station / Pipedrive)

```
[lead_new] --(form_submit OU lead_score≥70)--> [mql]
[mql] --(SDR_accept OU 24h timeout)--> [sal_accepted | sal_returned]
[sal_accepted] --(meeting_booked)--> [sql]
[sql] --(proposal_sent)--> [opportunity]
[opportunity] --(contract_signed)--> [closed_won]
[opportunity] --(reason_lost)--> [closed_lost]
```

Cada transição é **system event** (Pedowitz Group): regra automatizada dispara a mudança no instante em que o critério é atingido. SDR/AE não decide se promove — sistema promove e ele só executa próxima ação.

### Scoring rule (exemplo observável)

```
lead_score = 0
+ 30 se cargo in [CMO, Head Mkt, Diretor Mkt, VP Mkt]
+ 20 se empresa size ≥ 50 funcionários
+ 15 se baixou material de fundo de funil (case, benchmark, ROI calc)
+ 10 se segmento in [SaaS, e-commerce, fintech]
+ 5 por evento de engajamento últimos 14d (cap em +20)

THRESHOLD MQL: lead_score ≥ 70 + cargo válido + empresa válida.
```

### Webhook OUT por mudança de stage

Cada transição emite `POST` pra endpoint N8N / GTM Server / BI:

```json
{
  "event_id": "uuid-v4",
  "event_name": "MQL",
  "timestamp": "ISO-8601",
  "lead_id": "crm-internal-id",
  "previous_stage": "lead_new",
  "new_stage": "mql",
  "scoring_at_transition": 78,
  "user_data": {"em": "sha256...", "ph": "sha256..."}
}
```

Webhook alimenta tracking server-side (CAPI Meta, Enhanced Conversions Google) + BI + auditoria de funil.

## Eventos canônicos do funil

A skill `tracking-engineer` (TE) e `instrumentation-engineer` (IE) só configuram tags se A-2 declarou os eventos abaixo.

| Evento (PascalCase) | Origem | Quem dispara | Etapa |
|---------------------|--------|--------------|-------|
| `PageView` | Front | GTM Web | Visitante |
| `Lead` | Front | GTM Web (form submit) | Lead |
| `MQL` | Server (N8N) | Webhook CRM | MQL |
| `NOICP` | Front | GTM Web (form submit anti-ICP) | Excluído |
| `LeadAccepted` | Server (N8N) | Webhook CRM (SDR aceita) | SAL |
| `LeadQualified` | Server (N8N) | Webhook CRM (BANT confirmado) | SQL |
| `Opportunity` | Server (N8N) | Webhook CRM (proposta enviada) | Opportunity |
| `DealWon` | Server (N8N) | Webhook CRM (contrato assinado) | Closed Won |
| `CustomerRetained90d` | Server (N8N) | Cron CRM (90d pós-won, sem churn) | Retenção (Bowtie pós) |

**Regra**: eventos server-side carregam `event_id` (UUID v4) + hash SHA-256 (email lowercase trimado, phone E.164) pra dedup CAPI.

## Buying group (Forrester 2021) — modo avançado

Comitê de compra B2B enterprise:

- **13 stakeholders internos**: Champion, Economic Buyer, Decision Maker, Influencer (×3), User (×3), Ratifier, Initiator, Gatekeeper, Coach.
- **9 influenciadores externos**: analistas (Gartner, Forrester), peers, comunidade, reviews (G2), parceiros, integradores, consultores, mídia, redes sociais.

Modo avançado **exige** mapear pelo menos: Champion + Economic Buyer + 1 User + 1 Influencer interno.

### Bowtie pós-venda (Winning by Design)

Etapas simétricas ao pré-venda:

```
Pré-venda:   Awareness → Education → Selection → Commitment
Pós-venda:   Onboarding → Impact (Value Delivery) → Expansion → Advocacy
```

Modo avançado **exige** declarar pelo menos Onboarding e Impact com fonte da verdade e KPIs.

### RPM (Revenue Performance Model) — V1–V13 + CR0–CR4

Forrester 2021 substitui o funil clássico por waterfall de volumes (V1 awareness → V13 advocacy) e conversion rates (CR0 inquiry-to-MQL → CR4 won-to-expand).

Modo avançado declara pelo menos:
- `rpm_volumes`: V1, V5 (MQL), V8 (Opp), V11 (Won), V13 (Expansion).
- `rpm_conversion_rates`: CR0–CR4 com benchmarks calibrados.

## Passo a passo (playbook) ↔ JSON

| Passo | Seção implícita | Campos principais no JSON |
|-------|------------------|---------------------------|
| 0 Modo | Gate inicial | `modo`, `criterios_modo` |
| 1 Objetivo do funil | Passo 1 | `objetivo.conversao_final_que_importa`, `objetivo.lead_correto_definicao` |
| 2 AS IS | Passo 2 | `as_is.marketing`, `as_is.vendas`, `as_is.ferramentas_resumo`, `as_is.lacunas` |
| 3 TO BE / vocabulário | Passo 3 | `to_be.notas_alinhamento`, nomes em `etapas[].nome` |
| 4 Por etapa | Passo 4 | `etapas[]`: `definicao_passa`, `evidencia_minima`, `taxa_aceitavel`, `fonte_da_verdade`, `campos_minimos`, `handoff_protocolo_ref` |
| 5 Eventos tracking | Passo 5 | `eventos_tracking[]`, `eventos_canonicos[]` |
| 6 Coerência operação | Passo 6 | `coerencia_operacao` |
| 7 Automação CRM | Passo 7 | `automacao_crm` |
| 8 SLA | Passo 9 | `sla_mkt_vendas` |
| 9 Benchmarks | Passo 4 (faixas) | `benchmarks_referencia` |
| Avançado | Buying group / Bowtie | `buying_group`, `bowtie_etapas_posvenda`, `rpm_volumes`, `rpm_conversion_rates` |

## Saídas do playbook ↔ estrutura

| Saída canônica | Onde no JSON |
|----------------|--------------|
| Modo escolhido + critério | `modo`, `criterios_modo` |
| Etapas nome + definição | `etapas[].nome`, `definicao_passa` |
| Evento de conversão por etapa | `etapas[].conversao_evento` (+ `eventos_tracking` agregado) |
| Taxa aceitável (faixas) | `etapas[].taxa_aceitavel.{verde,amarelo,vermelho,fonte_benchmark}` + `benchmarks_referencia` |
| Fonte da verdade | `etapas[].fonte_da_verdade` |
| Campos mínimos | `etapas[].campos_minimos[]` |
| Handoffs | `etapas[].handoff_protocolo_ref`, `meta.link_protocolo_handoff` |
| SLA Mkt+Vendas | `sla_mkt_vendas` |
| Automação CRM | `automacao_crm` |
| Eventos canônicos pra TE/IE | `eventos_canonicos[]` |
| Buying group (avançado) | `buying_group` |
| Bowtie pós-venda (avançado) | `bowtie_etapas_posvenda[]` |
| RPM volumes / CR (avançado) | `rpm_volumes`, `rpm_conversion_rates` |

## Componentes críticos (iteração)

Conforme playbook: definições operacionais vs nome cosmético; **uma** fonte da verdade; poucos campos essenciais; alinhamento Plano de Mídia; funil cabível na operação; **handoff é system event, não judgment call**.

## Gerenciado (playbook § final)

- **KPIs:** % leads com status válido; % campos mínimos preenchidos; tempo de ciclo por etapa; lead acceptance rate (SLA-bound).
- **Vermelho:** discrepância entre fontes ou etapa sem dono.
- **Amarelo:** muitas etapas, baixa adesão de dados.
- **Verde:** rastreio mínimo e aderência.
- **Cadência:** quinzenal até estabilizar; mensal depois; mudanças no change log.

Campos `gerenciado` no JSON espelham isso; preencher `dono_funil` quando a lacuna "Dono" do canônico for fechada.

## Auditoria (`--audit`)

O script verifica preenchimento mínimo para o DoD: meta, modo declarado, objetivo, AS IS, ≥2 etapas com bloco completo, eventos de tracking, eventos canônicos, SLA Mkt+Vendas, automação CRM, benchmarks por etapa, coerência operacional, backlog não vazio. No modo avançado, exige adicionalmente buying group (≥4 papéis) + bowtie pós-venda (≥2 etapas) + RPM (volumes + CRs).

Avisos extras: detecção automática de modo cruzando `criterios_modo` (warning se modo declarado diverge do detectado); SLA ausente, automação só descritiva (sem state machine + scoring + webhook), benchmarks ausentes, modo avançado sem buying group.

Itens listados são **lacunas** até preencher ou justificar em notas (fora do escopo do script).
