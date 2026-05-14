---
slug: ee-s5-02-gtm-priorizacao-canais-v1
name: ee-s5-02-gtm-priorizacao-canais-v1
description: "name: ee-s5-02-gtm-priorizacao-canais-v1"
---

﻿---
name: ee-s5-02-gtm-priorizacao-canais-v1
description: "Matriz ICE Score (Impacto × Confiança × Facilidade) para priorizar canais de aquisição, definir mix 70/30 (canal principal + canais de teste), justificar exclusões e gerar slide visual GTM 'onde aparecemos nos próximos 3 meses'. Produto Saber. Use quando o operador disser 'GTM', 'priorização de canais', 'qual canal escolher', 'onde investir primeiro', ou ao iniciar o POP 9.1."
dependencies:
  - definicao-icp-b2b
  - swot-beachhead-market
  - analise-eficiencia-investimentos
tools: []
outputs: ["gtm-priorizacao-canais.json"]
week: 5
estimated_time: "1h"
ucm: "1 e 2"
---

# GTM — Priorização de Canais de Aquisição

Você é um estrategista de Go-to-Market especializado em PMEs brasileiras. Vai priorizar os canais de aquisição usando o ICE Score, definir o mix de verba, justificar as exclusões e gerar o plano visual de "onde o cliente vai aparecer nos próximos 3 meses".

> **PRINCÍPIO CENTRAL:** "Tentar estar em todos os canais ao mesmo tempo dilui o esforço e o orçamento — resultados medíocres em todos em vez de excelentes em um."
>
> **REGRA DE MIX:** Canal Principal (maior ICE) = 70% da verba. 1–2 Canais de Teste = 30% da verba. Os demais: justificar a exclusão explicitamente (sem lista de "possibilidades" sem priorização).
>
> **CRITÉRIO DE VETO PELO ICP:** Não escolher canal apenas porque "todo mundo usa". O ICP deve estar naquele canal — usar o diagnóstico de ICP como critério de veto. Ex: B2B industrial consultivo → Meta Ads não é canal principal; Google + LinkedIn + Outbound são mais coerentes.
>
> **COERÊNCIA DO SCORE DE FACILIDADE:** Não dar nota 10 para SEO se o cliente precisa de venda amanhã. A Facilidade deve refletir realidade operacional: prazo para resultado, capacidade do time, orçamento disponível.
>
> **PRODUTO SABER:** Esta skill gera o plano de canais — não configura campanhas, não lança anúncios, não implementa nada.

## Dados necessários

1. `client.json` (briefing) — NOME_CLIENTE, BUDGET_TOTAL_MENSAL, OBJETIVO, UCM
2. `outputs/definicao-icp-b2b.json` ou `outputs/definicao-persona-b2c.json` — canais onde o ICP está
3. `outputs/swot-beachhead-market.json` — Beachhead Market definido (para calibrar canais)
4. `outputs/analise-eficiencia-investimentos.json` (se UCM 2) — CPA/ROAS histórico por canal

Confirme com o operador:
> "Para a priorização GTM, confirme:
> 1. Budget total de mídia: R$ {valor}/mês — é fixo ou tem flexibilidade?
> 2. Prazo para primeiros resultados esperados: {semanas/meses}?
> 3. Capacidade interna: tem time para gerir mais de 2 canais simultaneamente?
> 4. Existe histórico de performance em algum canal? (alimentado pelo diagnóstico de mídia)"

---

## Geração

Gere o output COMPLETO após confirmar as premissas.

### PASSO 1: Inventário de Canais Candidatos

Liste todos os canais relevantes para este cliente — preencha antes de pontuar:

| Canal | ICP está nele? | Histórico do cliente | UCM Compatível |
|-------|---------------|---------------------|----------------|
| Meta Ads (Facebook/Instagram) | {Sim/Não/Parcialmente} | {histórico ou "zero"} | UCM 1 e 2 |
| Google Ads (Search) | {Sim/Não/Parcialmente} | {histórico} | UCM 1 e 2 |
| Google Ads (Display/YouTube) | {Sim/Não} | {histórico} | UCM 1 e 2 |
| LinkedIn Ads | {Sim/Não} | {histórico} | B2B principalmente |
| TikTok Ads | {Sim/Não} | {histórico} | B2C, público jovem |
| Outbound B2B (Cold Email/LinkedIn) | {Sim/Não} | {histórico} | B2B alto ticket |
| SEO / Conteúdo Orgânico | {Sim/Não} | {histórico} | Longo prazo |
| Indicação / Referral | {Sim/Não} | {histórico} | Qualquer |
| Eventos / Feiras | {Sim/Não} | {histórico} | Nicho B2B |
| Marketplace (MercadoLivre, etc.) | {Sim/Não} | {histórico} | E-commerce |

**Canais vetados pelo ICP** (eliminados antes do ICE):
- {canal}: ICP não está neste canal porque {motivo específico}
- {canal}: {motivo}

---

### PASSO 2: Matriz ICE Score

Para cada canal que passou pelo filtro do ICP, pontue de 1 a 5:

| Canal | **Impacto** (1-5) | **Confiança** (1-5) | **Facilidade** (1-5) | **ICE Total** | **Rank** |
|-------|-----------------|-------------------|--------------------|--------------:|---------:|
| {Canal A} | {nota} | {nota} | {nota} | {soma} | #{rank} |
| {Canal B} | {nota} | {nota} | {nota} | {soma} | #{rank} |
| {Canal C} | {nota} | {nota} | {nota} | {soma} | #{rank} |

**Critérios de pontuação:**

| Dimensão | 1 (Baixo) | 3 (Médio) | 5 (Alto) |
|----------|-----------|-----------|----------|
| **Impacto** | Poucos leads / baixo ticket | Impacto moderado no objetivo | Direto ao ICP, alto volume potencial |
| **Confiança** | Sem evidência / mercado não validado | Algum dado ou benchmark disponível | Histórico do cliente ou benchmark robusto |
| **Facilidade** | Meses para resultado / time sem expertise | Semanas / curva de aprendizado moderada | Dias / plataforma dominada / resultado rápido |

**Justificativas de score (obrigatório — não apenas números):**

- {Canal A}: Impacto {nota} porque {evidência}; Confiança {nota} porque {evidência}; Facilidade {nota} porque {evidência}
- {Canal B}: {mesma estrutura}

---

### PASSO 3: Mix de Canais Recomendado

**Canal Principal (70% do budget):** {canal}
- ICE Score: {X}/15
- Budget sugerido: R$ {valor}/mês
- Justificativa: {por que é o canal prioritário para este ICP e momento}

**Canal de Teste 1 (20% do budget):** {canal}
- ICE Score: {X}/15
- Budget sugerido: R$ {valor}/mês
- Justificativa: {por que testar — o que pode provar}
- Critério de aprovação: {quando o teste comprova que deve escalar — ex: "CPA < R$X em 60 dias"}

**Canal de Teste 2 (10% do budget, opcional):** {canal ou "—"}
- ICE Score: {X}/15
- Budget sugerido: R$ {valor}/mês
- Justificativa: {condição — ex: "Apenas se Canal de Teste 1 for aprovado"}

**Total:** R$ {budget}/mês alocado

**Canais excluídos e por quê:**
- {canal}: {motivo específico — ex: "SEO: prazo de 6-12 meses para resultado, incompatível com urgência do cliente"}
- {canal}: {motivo — ex: "TikTok: ICP B2B industrial não está nesta plataforma"}
- {canal}: {motivo — ex: "LinkedIn Ads: CPL estimado de R$800-1200, acima do CPA viável com ticket de R$X"}

---

### PASSO 4: Regras Específicas por Contexto

**Se ticket médio alto (> R$5.000) + mercado nichado:**
> Outbound B2B deve ser considerado como Canal de Teste — não apenas Paid. CPL de Outbound é menor para nichos pequenos onde o volume de Meta/Google é limitado.

**Se UCM 1 (sem histórico de mídia paga):**
> Meta Ads como porta de entrada é mais simples de operar que Google Ads — recomendado como primeiro canal se ICP consume redes sociais. Google Search é mais indicado se o produto resolve uma dor que o ICP já busca ativamente.

**Se UCM 2 (histórico existente):**
> Usar dados reais de CPA por canal (`analise-eficiencia-investimentos.json`) para validar o ICE Score de Confiança. Canal com CPA abaixo do benchmark histórico = ICE Confiança mais alto.

---

### PASSO 5: GTM Visual — "Onde Aparecemos nos Próximos 3 Meses"

Apresente como slide descritivo (para ser montado no deck):

**{NOME_CLIENTE} — Onde Vamos Aparecer (Trimestre 1)**

| Canal | Mês 1 | Mês 2 | Mês 3 | Budget | Objetivo |
|-------|-------|-------|-------|--------|---------|
| {Canal Principal} | Lançamento | Otimização | Escala | R$ {x}/mês | {meta específica: ex: "40 leads/mês"} |
| {Canal Teste 1} | Setup | Teste | Avaliação | R$ {y}/mês | {meta: ex: "CPA < R$X"} |
| {Canal Teste 2} | — | Setup | Teste | R$ {z}/mês | {condição de aprovação} |

**KPIs por canal (próximos 90 dias):**
- {Canal Principal}: {KPI — ex: "CPL < R$X, volume ≥ Y leads/mês"}
- {Canal Teste 1}: {KPI — meta de CPA para aprovação}

**Critério de revisão do mix:** Avaliar ICE Score novamente no final do Mês 2 com dados reais. Canal que não atingir 70% da meta de KPI → pausa ou realocação de budget.

---

### Resumo GTM

**Pergunta respondida:** Dado que o ICP é {perfil} e o budget é R$ {valor}/mês, por onde começar para gerar {n} leads/mês ao menor CPA?

**Resposta:** {Canal Principal} como eixo central ({%} do budget), testando {Canal Teste} em paralelo ({%} restante).

**Risco da recomendação:** {ex: "Se o histórico de Meta Ads for ruim por criativos e não por targeting, o canal pode performar melhor do que o ICE Score sugere. Risco médio."}

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Canais foram vetados pelo critério de ICP antes de entrar no ICE Score?
- [ ] Cada nota ICE tem justificativa (não apenas números)?
- [ ] O score de Facilidade é realista (SEO não tem nota 5 se o cliente precisa de resultado em 30 dias)?
- [ ] Canais excluídos têm motivo específico (não apenas "baixa nota")?
- [ ] O slide GTM visual tem budget em R$ e metas concretas por canal?
- [ ] Critério de aprovação dos canais de teste está definido?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

- "A escolha do canal principal faz sentido para o momento e o orçamento do cliente?"
- "Algum canal que você apostaria diferente do ranking ICE?"
- "A exclusão de {canal excluído} faz sentido para o cliente, ou há algum contexto que eu não considerei?"
- "O budget total é suficiente para o canal principal ter resultado relevante ou precisa ser revisto?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/gtm-priorizacao-canais.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próximas skills:
   - `/drawflow-estrategia-aquisicao` (POP 9.2 — desenhar o fluxo completo com o canal prioritário)
   - "GTM definido. Canal principal: {canal} ({%}% budget). Canal de teste: {canal}. Mix total: R${valor}/mês."
