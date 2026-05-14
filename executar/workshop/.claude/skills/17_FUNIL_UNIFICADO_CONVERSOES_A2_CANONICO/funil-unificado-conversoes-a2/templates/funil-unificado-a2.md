# Funil unificado (A-2) — documento v1

**Cliente / projeto:**  
**Versão do funil:** v1  
**Data:**  
**Responsável (autor do doc):**  
**Link Plano de mídia:**  
**Link DEOC:**  
**Link Protocolo de handoff (A-4):**  
**Link benchmark / referências:**  

**Alinhamento explícito:** Marketing concorda ☐ | Vendas concorda ☐ | Data do alinhamento:

---

## 0. Modo (gate antes do passo 1)

| Campo | Conteúdo |
|-------|----------|
| Modo escolhido | ☐ Simples (lead-centric) ☐ Avançado (opportunity-centric / Forrester + Bowtie) |
| Ticket médio (BRL) | |
| Ciclo de venda (dias) | |
| Tamanho do comitê de compra | |
| Segmento (B2C / PME / SaaS PLG / B2B mid / B2B enterprise) | |
| Justificativa da escolha | |

> Critério rápido: ticket ≥ R$30k **e** ciclo ≥ 30d **e** comitê ≥ 3 → Avançado. Caso contrário → Simples.

---

## 1. Objetivo do funil (passo 1)

| Pergunta | Resposta |
|----------|----------|
| Qual conversão **final** importa para o negócio? | |
| O que é **lead correto** (e o que explicitamente **não** é)? | |

---

## 2. AS IS — como é hoje (passo 2)

### 2.1 Marketing (origem, canais, perdas)

### 2.2 Vendas (atendimento, etapas atuais, onde o lead "some")

### 2.3 Ferramentas (CRM, forms, tracking, planilhas paralelas)

### 2.4 Lacunas / conflitos de definição detectados

---

## 3. TO BE — vocabulário único (passo 3)

Notas de alinhamento de nomes (um termo = uma definição para Mkt + Vendas):

---

## 4. Etapas (passo 4)

Para **cada** etapa, copie o bloco.

### Etapa ___ — [nome]

| Campo | Conteúdo |
|-------|----------|
| Ordem no fluxo | |
| Definição operacional de "passou" | |
| Evidência mínima (auditável) | |
| Evento de conversão que "conta" | |
| Fonte da verdade (**um** sistema) | |
| Dono da etapa (conta) | |
| Ref. handoff no protocolo (ID/seção/link) | |
| Taxa aceitável — **Verde** | |
| Taxa aceitável — **Amarelo** | |
| Taxa aceitável — **Vermelho** | |
| Fonte da faixa (benchmark / histórico) | |

**Campos mínimos obrigatórios (CRM ou equivalente)**

| Campo | Como preencher / regra |
|-------|------------------------|
| | |
| | |

---

## 4.1 Benchmarks de referência (faixas calibradas)

| Transição | Verde | Amarelo | Vermelho | Fonte |
|-----------|-------|---------|----------|-------|
| Lead → MQL | ≥ 35% | 25–34% | < 12% | SmartBug 2024 / Forrester |
| MQL → SQL | ≥ 25% | 13–24% | < 6% | SmartBug, Pedowitz Group |
| SQL → Opportunity | ≥ 60% | 50–59% | < 25% | Forrester B2B Revenue Waterfall 2021 |
| Opportunity → Closed Won | ≥ 30% | 20–29% | < 10% | B2B SaaS médio |
| Lead Acceptance Rate | ≥ 50% | 30–49% | < 20% | SmartBug 2024 (média 42%) |
| Customer → Retained 90d | ≥ 90% | 75–89% | < 60% | Winning by Design Bowtie |

---

## 5. Eventos de tracking (passo 5)

| Evento / nome técnico | Etapa relacionada | Notas |
|----------------------|-------------------|-------|
| | | |

### 5.1 Eventos canônicos (entrada para tracking-engineer / IE)

| Evento (PascalCase) | Origem | Responsável dispara | Etapa |
|---------------------|--------|---------------------|-------|
| PageView | front | GTM Web | Visitante |
| Lead | front | GTM Web (form submit) | Lead |
| MQL | server | Webhook CRM via N8N | MQL |
| NOICP | front | GTM Web (form submit anti-ICP) | Excluído |
| LeadAccepted | server | Webhook CRM via N8N | SAL |
| LeadQualified | server | Webhook CRM via N8N | SQL |
| Opportunity | server | Webhook CRM via N8N | Opportunity |
| DealWon | server | Webhook CRM via N8N | Closed Won |
| CustomerRetained90d | server | Cron CRM via N8N | Retenção (Bowtie pós) |

---

## 6. Coerência com operação (passo 6)

| Pergunta | Resposta |
|----------|----------|
| Capacidade do time vs volume esperado | |
| Ciclo de venda típico | |
| Riscos de "funil impossível" de operar | |

---

## 7. Automação CRM (passo 7) — concreta, não descritiva

**Plataforma:**  (HubSpot / RD Station / Pipedrive / outro)

### 7.1 State machine

| from_stage | to_stage | trigger | regra observável |
|------------|----------|---------|------------------|
| | | | |

### 7.2 Scoring rule

- Definição:  
- Threshold MQL:  
- Pontos exemplo:  

### 7.3 Webhook OUT por mudança de stage

- Stages que disparam webhook:  
- Endpoint:  

> Lembrete: handoff é **system event** (Pedowitz Group). Sistema promove, SDR/AE só executa próxima ação.

---

## 8. SLA Marketing ↔ Vendas (passo 8) — escrito e assinado

| Campo | Conteúdo |
|-------|----------|
| Definição MQL acordada | |
| Definição SQL acordada | |
| Tempo de aceite (horas úteis) | |
| Procedimento de devolução / descarte / requalificação | |
| Motivos de devolução padronizados (lista fechada) | |
| Owner Marketing | |
| Owner Vendas | |
| Owner Funil (governança) | |
| Cadência de revisão | Quinzenal 90d → mensal |
| Data de assinatura | |
| Versão | v1 |

---

## 9. Backlog de implementação

| Item | Prioridade (P0–P2) | Dono |
|------|-------------------|------|
| | | |

---

## 10. Modo avançado — extensões Forrester + Bowtie (preencher só se modo = avançado)

### 10.1 Buying group (Forrester 2021: 13 stakeholders + 9 externos)

| Papel | Pessoa / cargo |
|-------|----------------|
| Champion | |
| Economic Buyer | |
| Decision Maker | |
| Influencers internos | |
| Users | |
| Ratifier | |
| Gatekeeper | |
| Influenciadores externos (analistas, peers, reviews) | |

### 10.2 Bowtie pós-venda (Winning by Design)

| Etapa | Definição "passou" | Fonte da verdade | KPI principal |
|-------|---------------------|------------------|---------------|
| Onboarding | | | |
| Impact / Value Delivery | | | |
| Expansion | | | |
| Advocacy | | | |

### 10.3 RPM (Revenue Performance Model)

**Volumes** (V1–V13 — declarar pelo menos os listados)

| Volume | Definição | Valor |
|--------|-----------|-------|
| V1 — Awareness | | |
| V5 — MQL | | |
| V8 — Opportunity | | |
| V11 — Won | | |
| V13 — Expansion | | |

**Conversion rates** (CR0–CR4)

| CR | Transição | Valor / faixa |
|----|-----------|---------------|
| CR0 | Inquiry → MQL | |
| CR1 | MQL → SQL | |
| CR2 | SQL → Opportunity | |
| CR3 | Opportunity → Won | |
| CR4 | Won → Expand | |

---

## 11. Gerenciamento contínuo (playbook)

| KPI / métrica | Meta ou notas |
|---------------|---------------|
| % leads com status válido | |
| % campos mínimos preenchidos | |
| Tempo de ciclo por etapa | |
| Lead acceptance rate (SLA-bound) | |

**Cadência de revisão:** quinzenal até estabilizar → mensal.  
**Dono do funil (métrica/governança):**  
**Thresholds resumo (V/A/V):**  

---

## 12. Histórico (opcional)

Usar `changelog-funil-conversoes` para mudanças formais após v1.
