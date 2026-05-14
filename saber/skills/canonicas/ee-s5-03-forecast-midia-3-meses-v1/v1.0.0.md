---
slug: ee-s5-03-forecast-midia-3-meses-v1
name: ee-s5-03-forecast-midia-3-meses-v1
description: "name: ee-s5-03-forecast-midia-3-meses-v1"
---

﻿---
name: ee-s5-03-forecast-midia-3-meses-v1
description: "Forecast de mídia com projeção mês a mês (M1-M3) + visão macro M4-M12, usando engenharia reversa das metas (receita → vendas → leads → budget). 3 cenários obrigatórios (Pessimista/Realista/Otimista) com ROAS e premissas explícitas. UCM 1 usa benchmark de mercado; UCM 2 usa histórico real. Produto Saber. Use quando o operador disser 'forecast', 'projeção de resultados', 'quanto volta se eu investir X', ou ao iniciar o POP 10.3."
dependencies:
  - gtm-priorizacao-canais
  - drawflow-estrategia-aquisicao
  - diagnostico-comercial-crm
tools: []
outputs: ["forecast-midia-3-meses.json"]
week: 5
estimated_time: "2h"
ucm: "1 e 2"
---

# Forecast de Mídia — Projeção 3 Meses

Você é um especialista em análise de performance e projeção financeira de marketing para PMEs brasileiras. Vai construir a engenharia reversa das metas — premissas matemáticas claras para os primeiros 90 dias de execução.

> **PRINCÍPIO CENTRAL:** "Investir sem prever o retorno gera insegurança e atrito; o cliente precisa saber 'se eu colocar X, quanto volta em Y?'"
>
> **GESTÃO DE EXPECTATIVA CRÍTICA:** "Projeção baseada em hipóteses, sujeita a variáveis de mercado — não é garantia de resultado." Deixar claro na apresentação. Nunca apresentar Forecast como promessa.
>
> **UCM 1 vs UCM 2:**
> - UCM 1 (sem histórico): usar benchmark de mercado com deságio de segurança (margem de erro de ±30%)
> - UCM 2 (com histórico): usar dados reais do `analise-eficiencia-investimentos.json` como base. Se histórico ruim (ex: CPM artificialmente baixo por sazonalidade), usar benchmark com deságio.
>
> **ENGENHARIA REVERSA:** Partir da meta de receita → quantas vendas? → quantos MQLs? → quantos leads? → qual budget necessário? Não o inverso.
>
> **PRODUTO SABER:** Esta skill gera o forecast estratégico — não é planilha de mídia operacional. Não configura campanhas nem define criativos.

## Dados necessários

1. `client.json` (briefing) — NOME_CLIENTE, TICKET_MEDIO, META_RECEITA, BUDGET_MIDIA_MENSAL, UCM
2. `outputs/gtm-priorizacao-canais.json` — canal principal e mix de budget
3. `outputs/diagnostico-comercial-crm.json` — taxas de conversão do funil comercial (Lead → Venda)
4. `outputs/analise-eficiencia-investimentos.json` (se UCM 2) — CPA/ROAS histórico

Confirme premissas com o operador:
> "Para o Forecast, preciso confirmar as premissas de negócio:
> 1. Meta de receita nos próximos 3 meses: R$ {valor} (ou meta mensal?)
> 2. Ticket médio confirmado: R$ {valor} — é valor de primeiro contrato ou LTV?
> 3. Taxa de fechamento atual: {%} de propostas viram venda?
> 4. Sazonalidade: algum mês dos próximos 3 que é tipicamente melhor ou pior para o segmento?
> 5. Budget de mídia confirmado: R$ {valor}/mês — é firme ou pode ser ajustado conforme resultado?"

---

## Geração

Gere o output COMPLETO após confirmar as premissas.

### PARTE 1: Premissas de Marketing (GT preenche)

| Premissa | Valor | Fonte | Confiança |
|----------|-------|-------|-----------|
| Budget mensal total | R$ {valor} | Definido no GTM | Alta |
| Budget Canal Principal ({canal}) | R$ {valor} ({%}%) | GTM — mix 70/30 | Alta |
| Budget Canais de Teste | R$ {valor} ({%}%) | GTM | Alta |
| CPM estimado | R$ {valor} | {Histórico / Benchmark de mercado ±{deságio}%} | {Alta/Média/Baixa} |
| CTR estimado | {%} | {Histórico / Benchmark} | {confiança} |
| CPC estimado | R$ {valor} | Calculado: CPM × CTR | Derivada |
| Taxa de Conversão LP (clique → lead) | {%} | {Histórico / Benchmark} | {confiança} |
| CPL estimado | R$ {valor} | Calculado: CPC ÷ Taxa Conv. LP | Derivada |
| Leads estimados/mês | {n} | Calculado: Budget ÷ CPL | Derivada |

**Fonte das premissas:**
- UCM 1: benchmark de mercado para {segmento} no {canal principal} — deságio de segurança de {%}% aplicado
- UCM 2: histórico real dos últimos 90 dias (`analise-eficiencia-investimentos.json`) — CPL real de R$ {valor}

**Ajuste de sazonalidade:**
- Mês {n}: {ex: "+20% CPM esperado — Black Friday/Copa" ou "Mês típico — sem ajuste"}
- Mês {n}: {ajuste ou "sem ajuste"}

---

### PARTE 2: Premissas de Vendas (Account valida)

| Premissa | Valor | Fonte |
|----------|-------|-------|
| Taxa MQL (lead qualificado / total de leads) | {%} | {CRM / estimativa ICP} |
| Taxa de Contato (leads contactados / total) | {%} | {CRM — LRT impacta diretamente} |
| Taxa Reunião / Oportunidade | {%} | {CRM} |
| Taxa de Fechamento (proposta → venda) | {%} | {CRM real / benchmark} |
| Ticket Médio | R$ {valor} | {CRM confirmado} |
| Ciclo de Venda médio | {n} dias | {CRM / informado pelo cliente} |

**Taxa de Conversão Composta (Lead → Venda):**
= Taxa MQL × Taxa Contato × Taxa Reunião × Taxa Fechamento
= {%} × {%} × {%} × {%} = **{%} de conversão Lead → Venda**

**Impacto do Lead Response Time no Forecast:**
- LRT atual: {tempo} — taxa de contato estimada: {%}%
- LRT meta (< 5min) — taxa de contato estimada: {%}%
- Diferença em vendas/mês com LRT otimizado: +{n} vendas → R$ {valor} adicional

---

### PARTE 3: Engenharia Reversa da Meta

**Meta de receita:** R$ {meta_trimestral}/trimestre

| Etapa | Cálculo | Resultado |
|-------|---------|-----------|
| Vendas necessárias | R$ {meta} ÷ R$ {ticket} | {n} vendas/trimestre |
| MQLs necessários | {n} vendas ÷ {%} fechamento | {n} MQLs/trimestre |
| Leads necessários | {n} MQLs ÷ {%} qualificação | {n} leads/trimestre |
| Leads/mês necessários | {n} ÷ 3 meses | {n} leads/mês |
| Budget necessário | {n} leads × R$ {CPL} | R$ {valor}/mês |

**Gap entre budget disponível (R$ {disponível}/mês) e budget necessário (R$ {necessário}/mês):**
- Gap: R$ {diferença}/mês
- Implicação: {se gap positivo: "O budget é suficiente para a meta. Sobra R$X para teste." / se gap negativo: "Para atingir a meta, o budget precisa ser aumentado em R$X ou a meta reduzida. Cenário Realista usa budget disponível."}

---

### PARTE 4: Projeção Mês a Mês (M1–M3)

#### Cenário REALISTA (premissas atuais)

| Métrica | Mês 1 | Mês 2 | Mês 3 | Trimestre |
|---------|-------|-------|-------|-----------|
| Budget investido | R$ | R$ | R$ | R$ |
| Impressões | {n} | {n} | {n} | {n} |
| Cliques | {n} | {n} | {n} | {n} |
| CPM | R$ | R$ | R$ | — |
| CTR | {%} | {%} | {%} | — |
| CPC | R$ | R$ | R$ | — |
| Leads gerados | {n} | {n} | {n} | {n} |
| CPL | R$ | R$ | R$ | — |
| MQLs | {n} | {n} | {n} | {n} |
| Vendas | {n} | {n} | {n} | {n} |
| **Receita gerada** | **R$** | **R$** | **R$** | **R$** |
| **ROAS** | **{x}x** | **{x}x** | **{x}x** | **{x}x** |
| **CPA (custo/venda)** | **R$** | **R$** | **R$** | **R$** |

**Nota sobre M1:** Fase de Aprendizado (Meta Ads) ou período de calibração — performance pode ser 20-30% abaixo do M2+. Isso é normal e esperado.

---

#### Cenário PESSIMISTA (CPM dobra ou conversão cai pela metade)

**Premissas alteradas:** CPM +100% / Taxa de Conv. LP ÷2 / Taxa de Fechamento -30%

| Métrica | Mês 1 | Mês 2 | Mês 3 | Trimestre |
|---------|-------|-------|-------|-----------|
| Leads gerados | {n} | {n} | {n} | {n} |
| Vendas | {n} | {n} | {n} | {n} |
| **Receita gerada** | **R$** | **R$** | **R$** | **R$** |
| **ROAS** | **{x}x** | **{x}x** | **{x}x** | **{x}x** |
| **Ponto de equilíbrio atingido?** | {Sim/Não} | {Sim/Não} | {Sim/Não} | {Sim/Não} |

**Quando o pessimista ocorre:** criativo não ressoa com o ICP, concorrência aumenta lances, sazonalidade adversa.

---

#### Cenário OTIMISTA (acertamos criativo e canal desde M1)

**Premissas alteradas:** CPL -30% / Taxa de Conv. LP ×1.5 / LRT < 5min implementado

| Métrica | Mês 1 | Mês 2 | Mês 3 | Trimestre |
|---------|-------|-------|-------|-----------|
| Leads gerados | {n} | {n} | {n} | {n} |
| Vendas | {n} | {n} | {n} | {n} |
| **Receita gerada** | **R$** | **R$** | **R$** | **R$** |
| **ROAS** | **{x}x** | **{x}x** | **{x}x** | **{x}x** |

**Quando o otimista ocorre:** histórico de criativos validados, ICP bem segmentado, processo comercial otimizado (LRT < 5min).

---

### PARTE 5: Visão Macro M4–M12

| Trimestre | Budget | Receita Projetada | ROAS | Hipótese |
|-----------|--------|-----------------|------|---------|
| T1 (M1–M3) | R$ {x}/mês | R$ {valor} | {x}x | Cenário Realista |
| T2 (M4–M6) | R$ {x}/mês | R$ {valor} | {x}x | +15% eficiência com otimização |
| T3 (M7–M9) | R$ {x}/mês | R$ {valor} | {x}x | Escala do canal validado |
| T4 (M10–M12) | R$ {x}/mês | R$ {valor} | {x}x | {sazonalidade: Black Friday / Natal} |
| **Ano total** | **R$** | **R$** | **{x}x** | — |

---

### PARTE 6: Premissas de Abandono (Critérios de Revisão)

Se estes alertas forem atingidos, revisar a estratégia antes de continuar investindo:

| Alerta | Threshold | Ação recomendada |
|--------|-----------|-----------------|
| CPL > {R$X} por 30 dias | {valor = CPL meta × 2} | Pausar e revisar targeting + criativo |
| CTR < {%} por 30 dias | {abaixo de benchmark} | Revisar criativo / headline |
| Taxa de Conversão LP < {%} | {abaixo de meta} | Auditoria de copy + UX da LP |
| 0 vendas no M1 | — | Revisar funil comercial — problema pode não ser de mídia |

---

### Resumo do Forecast

| Cenário | Investimento 3 meses | Receita projetada | ROAS | CPA |
|---------|---------------------|------------------|------|-----|
| Pessimista | R$ | R$ | {x}x | R$ |
| **Realista** | **R$** | **R$** | **{x}x** | **R$** |
| Otimista | R$ | R$ | {x}x | R$ |

**CPA sustentável:** R$ {valor} — calculado como: Ticket Médio × Margem Alvo ({%}%). Se CPA real ficar abaixo deste valor, o canal é lucrativo para escalar.

**ROAS de equilíbrio (break-even):** {x}x — abaixo disso, cada R$1 investido retorna menos de R$1 em margem.

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Premissas têm fonte documentada (histórico vs benchmark vs estimativa)?
- [ ] 3 cenários foram calculados com premissas diferentes (não apenas ajuste linear)?
- [ ] Engenharia reversa da meta foi feita (meta → leads → budget, não budget → leads → meta)?
- [ ] M1 tem nota sobre fase de aprendizado (expectativa calibrada)?
- [ ] Gestão de expectativa de "projeção ≠ garantia" está explícita?
- [ ] Critérios de abandono/revisão foram definidos?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

- "As premissas de marketing fazem sentido para o histórico que você conhece do segmento?"
- "As taxas de conversão comercial usadas — o time de vendas confirmaria esses números?"
- "O cenário pessimista ainda faz sentido investir? (se ROAS pessimista < 1x, rever budget ou meta)"
- "O gap entre budget disponível e necessário — tem possibilidade de ajustar o budget ou a meta?"
- "A projeção anual — está alinhada com o planejamento financeiro do cliente?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/forecast-midia-3-meses.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próximas skills:
   - `/deck-entrega-final` (POP 10.4 — consolidar todos os outputs na apresentação final)
   - "Forecast concluído. Cenário Realista: R${receita} em 3 meses. ROAS: {x}x. CPL: R${valor}. CPA: R${valor}."
