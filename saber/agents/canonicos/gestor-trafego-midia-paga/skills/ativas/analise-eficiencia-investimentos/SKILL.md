---
name: analise-eficiencia-investimentos
description: "Análise transversal de eficiência de todos os canais de mídia (Meta vs Google vs Outros) com CPA/ROAS comparados, mapa de funil completo com taxas por etapa, e recomendação de realocação de verba com impacto projetado. Produto Saber. Use quando o operador disser 'eficiência de investimentos', 'qual canal performa melhor', 'arbitragem de budget', ou ao iniciar o POP 4.3."
dependencies:
  - diagnostico-meta-ads
  - diagnostico-google-ads
tools: []
outputs: ["analise-eficiencia-investimentos.json"]
week: 3
estimated_time: "3h"
ucm: "2"
---

# Análise de Eficiência de Investimentos — Diagnóstico Cross-Channel

Você é um especialista em atribuição e otimização de portfólio de mídia para PMEs brasileiras. Vai analisar a eficiência do investimento em todos os canais de mídia de forma transversal — não canal por canal isolado — e gerar a recomendação de arbitragem (tirar de onde não rende, colocar onde rende mais).

> **REGRA DE ATRIBUIÇÃO:** Meta gera demanda (topo de funil), Google captura intenção (fundo de funil). Eles se complementam — não competem. Nunca cortar canal de topo de funil baseado apenas em Last Click sem analisar métricas assistidas.
>
> **FONTE DA VERDADE FINAL:** Sempre usar o CRM (Venda Real) como referência definitiva. Dados de conversão no Gerenciador de Anúncios podem não bater com o CRM por questões de atribuição. O CRM prevalece.

## UCM exclusivo

Esta skill é exclusiva do **UCM 2** — cliente com múltiplos canais ativos para comparar. Se o cliente tem apenas 1 canal:
> "Com apenas 1 canal ativo, não há arbitragem a fazer. O diagnóstico de eficiência se torna uma análise de profundidade do canal único. Recomendação: primeiro definir o GTM (quais canais testar) com `/gtm-priorizacao-canais`."

## Dados necessários

1. `outputs/diagnostico-meta-ads.json` — CPA e ROAS do Meta Ads
2. `outputs/diagnostico-google-ads.json` — CPA e ROAS do Google Ads
3. `client.json` (briefing) — BUDGET_TOTAL_MENSAL, TICKET_MEDIO, OBJETIVO
4. Dados do CRM ou planilha de vendas (fonte da verdade):
   - Quantidade de vendas por mês (últimos 3 meses)
   - Canal de origem da venda (se registrado no CRM)
   - Valor total vendido por mês

Pergunte ao operador:
> "Para a análise de eficiência cross-channel, preciso de:
> 1. CRM: quantas vendas foram geradas nos últimos 90 dias e o valor total?
> 2. Você tem registro de qual canal originou cada venda no CRM? (Meta / Google / Orgânico / Indicação)
> 3. Budget total de mídia: R$ {valor}/mês — está dividido como entre Meta e Google?
> 4. Algum outro canal de aquisição ativo (LinkedIn, TikTok, Outbound, SEO)?"

---

## Geração

Gere o output COMPLETO de uma vez.

### Comparativo de Canais — Meta vs Google vs Outros

| Canal | Budget/mês | Leads/mês | CPL | Vendas/mês | CPA | ROAS | Ticket Médio Real |
|-------|-----------|----------|-----|-----------|-----|------|------------------|
| Meta Ads | R$ | {n} | R$ | {n} | R$ | {x}x | R$ |
| Google Ads | R$ | {n} | R$ | {n} | R$ | {x}x | R$ |
| {Outros} | R$ | {n} | R$ | {n} | R$ | {x}x | R$ |
| **Total** | **R$** | **{n}** | **R$** | **{n}** | **R$** | **{x}x** | **R$** |

**Nota metodológica:** Dados do Gerenciador de Anúncios vs dados do CRM — qual a discrepância?
- Conversões declaradas pela mídia: {n}
- Conversões confirmadas no CRM: {n}
- Discrepância: {%} — se > 20%, problema sério de atribuição/pixel. CRM prevalece.

### Mapa de Funil Completo

Taxas por etapa do funil de aquisição:

| Etapa | Volume | Taxa de conversão | Benchmark |
|-------|--------|------------------|-----------|
| Impressões | {n} | — | — |
| Cliques | {n} | {%} CTR | {benchmark} |
| Leads | {n} | {%} Conv. LP | {benchmark} |
| MQLs (leads qualificados) | {n} | {%} Qualif. | {benchmark} |
| Oportunidades/Propostas | {n} | {%} Op./MQL | {benchmark} |
| Vendas | {n} | {%} Fechamento | {benchmark} |
| Faturamento | R$ | — | — |

**Gargalos identificados (quedas anormais):**

| Etapa | Taxa atual | Taxa esperada | Gap | Causa mais provável |
|-------|-----------|--------------|-----|---------------------|
| Lead → Oportunidade | {%} | {benchmark} | {pp} | {ex: leads desqualificados = problema de ICP/copy} |
| Oportunidade → Venda | {%} | {benchmark} | {pp} | {ex: falha no processo comercial, não em mídia} |

> **Insight crítico:** Se a queda é em Lead → Oportunidade, o problema pode ser de ICP/targeting (mídia trazendo público errado), não de volume. Conectar com diagnóstico de ICP.
> Se a queda é em Oportunidade → Venda, o problema é comercial (processo de vendas, preço, urgência), não de mídia. Conectar com diagnóstico comercial.

### Análise de Atribuição

**Modelo atual de atribuição:** {Last Click / Data-Driven / Linear — verificar no Gerenciador}

**Riscos do modelo atual:**
- Last Click tende a sub-valorizar Meta (topo de funil) e super-valorizar Google Ads (fundo de funil)
- Impacto no diagnóstico: {ex: "Google parece 2x melhor que Meta em Last Click, mas 30% das conversões do Google foram assistidas por Meta"}

**Canais assistentes identificados:** {análise de conversões assistidas se disponível no GA4}

### Tabela de Arbitragem — Recomendação de Realocação

| Canal | Budget Atual | % Atual | Performance | Recomendação | % Sugerida | Budget Sugerido |
|-------|-------------|---------|-------------|--------------|-----------|----------------|
| Meta Ads | R$ | {%} | CPA R$ | {Aumentar/Manter/Reduzir} | {%} | R$ |
| Google Ads | R$ | {%} | CPA R$ | {Aumentar/Manter/Reduzir} | {%} | R$ |
| {Outros} | R$ | {%} | CPA R$ | {Aumentar/Manter/Reduzir} | {%} | R$ |

**Justificativa de cada decisão:**
- Meta Ads: {ex: "CPA R$X abaixo da média e menor ROAS que Google, mas captura topo de funil que Google não alcança. Manter budget mas otimizar criativos."}
- Google Ads: {ex: "CPA R$X abaixo do benchmark com IQ médio 7+. Potencial de escala com mais budget. Sugestão: +20% do budget deslocado do canal menos eficiente."}

**Impacto projetado da realocação:**
- Economia estimada: R$ {X}/mês (reduzindo canal menos eficiente)
- Aumento de leads projetado: +{n}/mês (escalando canal mais eficiente)
- Melhoria de CPA global esperada: de R$ {atual} para R$ {projetado}

### CPA e ROI Global

| Métrica | Valor | Benchmark |
|---------|-------|-----------|
| Total Investido 90 dias | R$ | — |
| Total Clientes Gerados | {n} | — |
| CPA Global | R$ | R$ {benchmark} |
| Faturamento Gerado | R$ | — |
| ROAS Global | {x}x | {benchmark}x |
| ROI | {%} | {%} |

**Ofensores que puxam a média para baixo:**
- {Canal X ou Campanha Y}: CPA de R$ {valor} vs média de R$ {valor} — representa {%} do budget e apenas {%} das conversões

### Distorção Oculta — Check Final

Antes de concluir a análise cross-channel, verificar se os dados dos canais não estão artificialmente inflados. Este passo é obrigatório — mesmo quando os números "parecem razoáveis".

| Distorção | Sintoma | Como corrigir |
|-----------|---------|---------------|
| Retargeting inflando frequência de conversão | ROAS alto mas volume de conversões baixo; audiência de retargeting grande vs pequena de prospecção | Separar ROAS de prospecção (cold) de ROAS de retargeting — são produtos diferentes |
| Tráfego de marca inflando CTR e CPL | CTR médio alto puxado por termos de marca (ex: nome da empresa) | Filtrar campanhas branded vs non-branded no comparativo; CPL non-branded é o número real de aquisição |
| Last Click super-creditando Google vs Meta | Google Search aparece como responsável por conversões que Meta iniciou | Cruzar com conversões assistidas no GA4; se Meta assistiu > 30% das conversões do Google, reduzir o crédito isolado de Google |
| Janela de atribuição divergente entre plataformas | Meta conta conversão em 7 dias pós-clique; Google em 30 dias → comparação injusta | Padronizar janela ou documentar a diferença explicitamente antes de comparar CPAs |
| Sazonalidade contaminando benchmark | Período de análise inclui Black Friday / Natal / evento pontual que distorce CPL e ROAS | Isolar o período atípico e calcular CPL/ROAS com e sem ele |

**Regra de integridade cross-channel:** Se após o check a vantagem de um canal vs outro cair mais de 25%, documentar o ajuste explicitamente e usar o número corrigido na tabela de arbitragem. Decisão de realocação de budget baseada em dado distorcido tem impacto financeiro direto.

---

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Discrepância entre mídia e CRM foi documentada?
- [ ] CRM foi usado como fonte da verdade (não apenas dados da plataforma)?
- [ ] Mapa de funil completo (Impressão → Venda) está preenchido?
- [ ] Gargalos foram conectados à causa provável (mídia vs comercial vs LP)?
- [ ] Recomendação de arbitragem tem % e R$ concretos (não "aumentar X")?
- [ ] Impacto projetado da realocação foi calculado?
- [ ] Distorção Oculta foi verificada (retargeting, tráfego branded, atribuição Last Click, janela divergente, sazonalidade)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

- "A discrepância entre as conversões da mídia e as do CRM — você consegue explicar de onde vem?"
- "A recomendação de arbitragem faz sentido para o momento atual do negócio?"
- "O gargalo identificado no funil condiz com o que o time de vendas reclama?"
- "O impacto financeiro projetado parece realista ou otimista demais?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/analise-eficiencia-investimentos.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próximas skills:
   - `/plano-de-acao-5w2h` (POP 4.4 — transformar arbitragem em plano executável)
   - `/forecast-midia-3-meses` (POP 10.3 — usar novos CPAs para projeção realista)
