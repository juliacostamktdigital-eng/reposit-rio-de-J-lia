# Análise de CRM & Receita — Alisson Joias

> **Data de geração:** 07/05/2026
> **CRM:** Kommo
> **Período analisado:** Jan/2025 – Jan/2026
> **Fontes:** CSV Acompanhamento Mensal (Jan/2025–Jan/2026) · Screenshots CRM Kommo 28/04/2026 (3 leads individuais) · Kick-Off 05/02/2026 (Tier 2 — contexto)
> Dados não executáveis por ausência de export de deals individuais sinalizados como `[não disponível]`.

---

## Limitação Estrutural dos Dados

O CSV disponível é um **tracker de funil agregado por mês** — não um export de negócios fechados por cliente. Isso impede as análises que dependem de granularidade individual:

| Análise | Status |
|---|---|
| Concentração de receita 80/20 | `[não disponível]` — sem export por cliente |
| Win Rate por segmento de cliente | `[não disponível]` — sem campo de segmento preenchido |
| LTV por cliente | `[não disponível]` — sem histórico de compras individuais |
| Top 20% de clientes | `[não disponível]` — sem base ordenada por receita |

**O que É possível analisar com os inputs disponíveis:** canal orgânico vs Meta Ads, ticket médio e tendência, sazonalidade.

---

## CHECK 0 — Qualidade dos Dados: **BAIXA**

| Critério | Status | Observação |
|---|---|---|
| Valor de contrato preenchido ≥ 80% dos deals | ❌ | CSV tem faturamento agregado, não por deal. Screenshots de CRM confirmam campo `Venda = R$1` (placeholder) em Walker Campos |
| Canal de origem registrado por deal | ⚠️ | Separação orgânico/pago disponível apenas como totais mensais no CSV |
| Segmento/perfil do cliente registrado | ❌ | Nenhum campo de segmento visível nos inputs disponíveis |
| Total do export bate com faturamento declarado (± 10%) | ✅ | CSV 2025: R$9.128.485 total · Kick-off: "R$700K–R$1M/mês" → compatível |

**Confiabilidade:** Baixa para análise por segmento e concentração. Média para análise temporal e de canal.

---

## Análise 3 — Receita por Canal de Origem

**Metodologia:** Orgânico = Visão Geral – Meta Ads Leads. Jan/2025–Dez/2025: 100% orgânico (% Share de mídia = 0,00% no CSV). Jan/2026: 98,75% orgânico por receita.

| Canal | Período | Leads | Vendas | Win Rate (L→V) | Receita gerada |
|---|---|---|---|---|---|
| **Orgânico** | Jan/25–Jan/26 | 8.943 | 2.762 | **30,9%** | R$9.128.485 (2025) |
| **Meta Ads — Total** | Jan/25–Jan/26 | 682 | 2 | **0,29%** | R$7.805 |

### Detalhamento Meta Ads

| Campanha | Investimento total | Leads | Vendas | ROAS | CPA |
|---|---|---|---|---|---|
| Meta Ads — Leads (Jan/25–Jan/26) | R$1.917,62 | 682 | 2 | 8,20x (jan/26) | R$475,88 |
| Meta Ads — Engajamento | R$1.058,54 | — | — | — | — |
| Meta Ads — Venda | R$37,72 | — | 0 | 0x | — |
| **Total Meta Ads** | **R$2.976,16** | **682** | **2** | — | — |

> **Histórico de conversão Meta Ads:**
> Jan/2025: 72 leads, R$149,84 investido → **0 vendas**
> Fev/2025: 6 leads, R$53,43 → **0 vendas**
> Abr/2025: 0 leads qualificados → **0 vendas**
> Dez/2025: 235 leads, R$614,00 → **0 vendas**
> Jan/2026: 369 leads, R$951,75 → **2 vendas** (primeiras conversões desde o início das campanhas)

### Achados Principais

**Win Rate orgânico (30,9%) vs Meta Ads (0,29%) — diferença de 105x.**

A diferença não indica que Meta Ads é inviável — indica que os leads têm natureza distinta e o processo de atendimento não está calibrado para cada tipo:

- **Orgânico:** lead inicia conversa pelo Instagram (inbound quente, alta intenção de compra). Processo comercial atual foi construído para atender exatamente esse perfil.
- **Meta Ads:** lead preenche formulário sem iniciar conversa no WhatsApp (inbound frio). Gera o problema da "janela de 24 horas" identificado no kick-off — a consultora precisa enviar template para iniciar contato, o que a Meta cobra e limita.

O ROAS de 8,20x no único mês com conversão (jan/2026) confirma que quando o Meta Ads gera venda, o valor é positivo. O gargalo está na taxa de conversão, não no ticket do lead que compra.

---

## Análise 4 — Ticket Médio e LTV

### Ticket Médio — Série Histórica

| Mês | Ticket Médio | Vendas | Faturamento |
|---|---|---|---|
| Jan/2025 | R$3.334,94 | 201 | R$670.322,74 |
| Fev/2025 | R$3.336,04 | 178 | R$593.814,53 |
| Mar/2025 | R$3.141,24 | 225 | R$706.779,56 |
| Abr/2025 | R$3.434,14 | 210 | R$721.168,46 |
| Mai/2025 | R$3.284,05 | 263 | R$863.704,25 |
| Jun/2025 | R$3.131,91 | 239 | R$748.525,71 |
| Jul/2025 | R$3.228,53 | 218 | R$703.820,45 |
| Ago/2025 | R$3.259,76 | 242 | R$788.862,96 |
| Set/2025 | R$3.647,56 | 194 | R$707.625,69 |
| Out/2025 | R$4.104,50 | 191 | R$783.959,36 |
| Nov/2025 | R$3.983,70 | 294 | R$1.171.207,33 |
| Dez/2025 | R$3.735,72 | 179 | R$668.693,96 |
| Jan/2026 | R$4.812,50 | 130 | R$625.625,12 |

| Métrica | Valor | Referência | Status |
|---|---|---|---|
| Ticket médio anual 2025 (ponderado) | R$3.465,38 | — | — |
| Ticket médio H1/2025 | R$3.277,22 | — | Base |
| Ticket médio H2/2025 | R$3.659,63 | — | +11,7% vs H1 |
| Ticket médio Jan/2026 | R$4.812,50 | — | +46,9% vs H1 · pico da série |
| Ticket declarado no kick-off (fev/2026) | R$4.318,00 | — | ⚠️ Divergência +7,6% vs CSV |
| Ticket declarado jan/2026 (kick-off) | R$4.472,00 | — | ⚠️ Divergência +7,6% vs CSV |
| LTV médio | `[não disponível]` | — | Sem histórico por cliente |

**Divergência ticket declarado vs real:** Kick-off (05/02/2026) citou R$4.472 para janeiro. CSV mostra R$4.812,50. Diferença de R$340 (7,6%) — abaixo do limiar de 15% para divergência crítica. Provável causa: kick-off usou dado preliminar ou média de período diferente.

**Tendência:** Alta sistemática confirmada. H2/2025 +11,7% vs H1 em ticket médio, jan/2026 +46,9% vs H1. Padrão consistente com rebrand de premium positioning concluído ~jan/2025 e aceleração ao longo do ano.

### LTV e Churn

| Métrica | Status |
|---|---|
| LTV por cliente | `[não disponível]` — sem export com histórico por cliente |
| Churn estimado | `[não disponível]` — sem base de clientes individuais |
| Proxy LTV/CPA (1 compra) | CPA Meta Ads jan/26: R$475,88 · Ticket médio: R$3.902,50 → razão 8,2x (acima do mínimo de 3x) |

---

## Análise 5 — Sazonalidade e Tendência

### Receita por Trimestre — 2025

| Trimestre | Receita | % do Ano | Vs. Trimestre Anterior | Observação |
|---|---|---|---|---|
| Q1/2025 (Jan–Mar) | R$1.970.916,83 | 21,6% | — | Base do ano — fev fraco (R$593.815) |
| Q2/2025 (Abr–Jun) | R$2.333.398,42 | 25,6% | +18,4% | Dia das Mães puxa (mai = R$863.704) |
| Q3/2025 (Jul–Set) | R$2.200.309,10 | 24,1% | -5,7% | Baixa sazonalidade jul/ago |
| Q4/2025 (Out–Dez) | R$2.623.859,65 | 28,7% | +19,3% | Black Friday domina (nov = R$1.171.207) |
| **Total 2025** | **R$9.128.485,00** | **100%** | — | — |

### Picos e Vales

**Meses de maior receita:**
- **Novembro/2025 → R$1.171.207** (12,8% do faturamento anual em 1 mês) — Black Friday
- **Maio/2025 → R$863.704** (9,5% do ano) — Dia das Mães

> Novembro + Maio = **22,3% do faturamento anual** (R$2.034.911 de R$9.128.485).

**Meses de menor receita:**
- **Fevereiro/2025 → R$593.815** — pós-festas, sem gatilho sazonal para joalheria
- **Dezembro/2025 → R$668.694** — ressaca do Black Friday (-43% vs novembro). Alisson declarou no kick-off: *"ressaca pesada em dezembro"* — confirmado nos dados.

### Anomalia — Outubro/2025

Outubro apresenta o maior volume de leads do ano (1.325 — +77% vs média mensal de 746) com o menor Win Rate (14,4%) e simultaneamente o maior ticket médio até aquele momento (R$4.105). Leads de qualidade menor entraram no funil mas quem comprou foi o perfil premium. Sem dado de origem dos leads, causa não identificável.

---

## Análise 1 e 2 — `[não disponível]`

### Concentração de Receita (80/20)

`[não disponível]` — Sem export de negócios fechados por cliente. CSV registra apenas totais mensais agregados. Impossível identificar Top 20% de clientes ou concentração por cliente individual.

### Receita por Segmento de Cliente

`[não disponível]` — Campo de segmento não observado no CRM (nenhum dos 3 leads visíveis nos screenshots tem segmento preenchido).

**Amostra CRM — 3 leads visíveis em 28/04/2026** (insuficiente para análise estatística):

| Lead | Etapa | Ticket CRM | Produto | Observação |
|---|---|---|---|---|
| Lúcia Mãe do Benício | Primeira Contato | R$1.750 | Aliança | — |
| Walker Campos | Orçamento | R$1 | Aliança + Pulseiras | **Placeholder — campo não preenchido** |
| Douglas Barros | **GANHO** (25/04/2026) | R$2.459 | Cordão 18k | Consultora: Débora Eduarda |

---

## Cruzamento: ICP Declarado vs Cliente Real

| Dimensão | ICP Declarado (Tier 2) | Cliente Real Observado | Alinhamento |
|---|---|---|---|
| Perfil | Empreendedor celebrando conquista, busca status/qualidade | Indeterminado (3 leads visíveis, sem dado de perfil) | ⚠️ Indeterminado |
| Ticket esperado | Premium — abaixo da Vivara, acima do mercado | R$1.750–R$2.459 (2 leads com valor; ambos abaixo da média de R$3.465) | ⚠️ Indeterminado |
| Canal de entrada | Instagram orgânico (principal) | Confirmado pelo Win Rate orgânico dominante | ✅ |

> **Limitação:** 3 leads não são representativos. Para avaliar alinhamento ICP vs cliente real, necessário export completo de deals fechados com campo de produto, valor e origem.

---

## Resumo Estratégico

**Cliente que mais vale (com dados disponíveis):**
> Canal: Orgânico (Instagram)
> Win Rate: 30,9% vs 0,29% do Meta Ads
> Ticket médio jan/2026: R$4.812 — em alta sistemática

**Top 3 achados:**

1. **Meta Ads converte 105x menos que orgânico** — 682 leads, 2 vendas em ~14 meses de campanhas. O problema é de processo de atendimento para lead frio, não de mídia. Quando converte, o ROAS é de 8,2x.

2. **Ticket médio em tendência de alta confirmada** — +11,7% H1→H2/2025, pico de R$4.812 em jan/2026. Rebrand premium está gerando impacto mensurável nos dados.

3. **Sazonalidade concentrada** — Novembro e Maio = 22,3% do faturamento anual. Estratégia de alocação de budget de mídia paga deve priorizar esses dois meses para maximizar retorno.

---

## Para Completar Esta Análise

As análises de maior valor estratégico (concentração 80/20, Win Rate por segmento, LTV) requerem:

> **Export do CRM Kommo:** Negócios → Filtrar por Status = Ganho + Período = últimos 12 meses → Exportar CSV
>
> **Campos obrigatórios no export:**
> - Data de fechamento
> - Valor (campo Venda)
> - Consultora responsável
> - Origem/canal do lead
> - Produto ou categoria
> - ID ou nome do cliente (para análise de recorrência e LTV)

---

## Limitações desta Análise

- **Dado agregado:** CSV registra totais mensais, não deals individuais. Análises 1 (80/20), 2 (segmento) e LTV não executáveis.
- **Meta Ads parcial:** Campanhas iniciadas em dez/2025, apenas jan/2026 com conversão — amostra de 1 mês com resultado, insuficiente para análise de tendência de canal pago.
- **Amostra CRM:** Apenas 3 leads visíveis nos screenshots de CRM — insuficiente para qualquer inferência sobre perfil de cliente ou segmento.
- **Cruzamento ICP vs real:** Indeterminado pela ausência de export com campo de segmento.
