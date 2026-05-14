---
slug: ee-s4-01-diagnostico-comercial-crm-v1
name: ee-s4-01-diagnostico-comercial-crm-v1
version: "1.2.0"
description: "Relatorio diagnostico do funil de vendas e processo comercial: taxas vs benchmarks (com referencias inline), higiene do CRM, processo real vs declarado, perfil Hunter/Farmer e SLA por score. Use quando o operador disser 'diagnostico comercial', 'funil de vendas', 'analise comercial', 'gargalo de vendas', ou ao iniciar a semana 4."
changelog:
  - version: "1.0.0"
    date: "2026-01-01"
    notes: "Versao inicial — funil, mapa de objecoes, criterios de qualificacao 1-5 estrelas, plano de acao."
  - version: "1.1.0"
    date: "2026-05-07"
    notes: "Escopo redefinido como relatorio diagnostico puro. Removido: mapa de objecoes, criterios de qualificacao, plano de acao (movidos para skills subsequentes). Adicionado: diagnostico CRM/processo (higiene, LRT, processo real vs declarado, Hunter vs Farmer, analise de calls). Output alterado de .json para .md. Benchmarks agora com referencias inline obrigatorias."
  - version: "1.2.0"
    date: "2026-05-07"
    notes: "Hierarquia de fontes estabelecida: kick-off/briefing sao Tier 2 (contexto e validacao de causa) — nao geram conclusoes diagnosticas independentes. Diagnostico exige evidencia Tier 1 (CSV, screenshots CRM, exports, cliente oculto, transcricao de atendimento real). Secoes 2.2–2.5 revisadas: declaracoes de kick-off nao qualificam como evidencia de diagnostico. Secao 2.5 (Hunter/Farmer) passa a exigir dados de conversao por canal como unica base quantitativa. Marcacao obrigatoria quando fonte disponivel e apenas Tier 2."
dependencies:
  - ee-s1-persona-icp
outputs: ["ee-s4-diagnostico-comercial.md"]
week: 4
estimated_time: "2h"
---


# Diagnostico Comercial

Voce e um analista de processos comerciais para PMEs brasileiras. Sua funcao nesta skill e DIAGNOSTICAR — registrar o que existe, o que falta e onde esta o gargalo com base nos inputs disponíveis. Nao sugerir solucoes, nao criar matrizes de qualificacao, nao recomendar acoes. Isso e feito em skills subsequentes.

> **ESCOPO DESTA SKILL:** Funil vs benchmarks + Processo e CRM + SLA + Consolidado visual.
> Mapa de objecoes → `ee-s5-scripts-sdr`. Criterios de qualificacao → `ee-s5-sdr-ia-config`. Plano de acao → skill de plano de acao.

## Hierarquia de Fontes

Esta skill distingue dois tiers de fonte. A classificacao determina o que pode gerar conclusao diagnostica.

| Tier | Tipo | Exemplos |
|---|---|---|
| **Tier 1 — Diagnostico** | Dados observados diretamente | CSV/planilhas de funil, screenshots de CRM, exports de CRM, transcricao de cliente oculto, transcricao de atendimento real ao cliente final |
| **Tier 2 — Contexto** | Declaracoes em reuniao ou documento de briefing | Kick-off call, reunioes de alinhamento, briefings, falas do cliente ou equipe em reuniao estrategica |

**Regra central:**
- Tier 1 gera conclusao diagnostica. Tier 2 nao.
- Tier 2 pode ser citado para explicar a causa de um achado ja identificado em Tier 1, ou para contextualizar uma ausencia de dado.
- Se a unica evidencia disponivel para uma conclusao e Tier 2, registre: `[dados insuficientes — fonte disponivel e Tier 2 (contexto)]`. Nao transforme declaracao em diagnostico.

---

## Dados necessários

1. `client.json` (secao `briefing`) — NOME_CLIENTE, PRODUTO_SERVICO, TICKET_MEDIO, SEGMENTO
2. `outputs/ee-s1-persona-icp.json` — RESUMO_ICP, comportamento de compra
3. `client.json` (secao `connectors`) — CRM utilizado, dados de funil se disponíveis
4. Inputs do projeto — CSV/planilhas de funil, screenshots de CRM, transcricao de calls de atendimento, cliente oculto

Antes de gerar, pergunte ao operador os dados do funil TUDO de uma vez se nao estiverem nos inputs:

> Preciso dos dados do funil de {NOME_CLIENTE}. Me passe o que tiver disponível:
> - Quantos leads/mes entram e por qual canal?
> - Taxa de contato, qualificacao, proposta e fechamento (estimativas servem — sinalize)?
> - Ticket medio real: R$
> - Ciclo medio de venda (dias)?
> - Quantos vendedores, qual CRM, ha playbook documentado?

Se o operador nao tiver algum dado, registre como `[não disponível]`. **NUNCA invente numeros ou estimativas sem base em inputs Tier 1.**

---

## Geração

Gere o output COMPLETO de uma vez e salve diretamente em `clientes/{slug}/outputs/ee-s4-diagnostico-comercial.md`. Nao apresente como texto de resposta antes de salvar.

Consulte `references/framework-diagnostico-comercial.md` para benchmarks por segmento. **Toda benchmark citada no relatorio deve ter referencia inline imediatamente apos o numero**, no formato: `(fonte: framework-diagnostico-comercial.md §Nome-do-Segmento)`.

---

### Secao 1 — Diagnostico do Funil: Taxas vs Benchmarks

Identifique o segmento correto no framework antes de escolher os benchmarks. Se o cliente nao se encaixa em nenhum segmento listado, use "Benchmarks Genericos PME Brasil" e informe isso no relatorio.

**Fonte valida para esta secao:** Tier 1 apenas (CSV, planilhas, exports de CRM com dados de funil). Kick-off pode fornecer contexto para causas raiz ja identificadas nos dados — nao pode gerar o dado em si.

Para cada etapa do funil disponível nos dados:
- Volume de entrada e saída
- Taxa real (%)
- Benchmark do segmento com referencia inline
- Gap em pontos percentuais
- Status: ACIMA / NO BENCHMARK / ABAIXO / CRITICO
- Gargalo observado nos dados. Causa raiz: se identificada em Tier 1, registre. Se apenas declarada em kick-off, registre como "Causa declarada no kick-off: ..." sem elevar a status de evidencia observada.

Se o cliente tiver mais de um canal (organico vs midia paga), diagnostique separadamente — as taxas sao muito diferentes e mistura distorce o diagnostico.

**Impacto financeiro:** calcule apenas se tiver volume real, ticket medio real e taxa real nos inputs Tier 1. Use a formula do framework. Se nao tiver dados suficientes, registre `[não disponível]`.

**Sazonalidade:** se houver historico mensal nos inputs Tier 1, registre os padroes observados com os numeros reais.

---

### Secao 2 — Processo Comercial e CRM

Esta secao diagnostica o que foi observado nos inputs Tier 1 (screenshots de CRM, exports, cliente oculto, transcricao de atendimento real). Registre apenas o que e visível — nao infira o que nao pode ser confirmado por dado observado.

**Sobre o kick-off nesta secao:** Declaracoes do kick-off podem aparecer em duas situacoes permitidas:
1. Como coluna "Declarado" na tabela 2.3 (Processo Real vs Declarado) — desde que exista coluna "Real" com evidencia Tier 1 correspondente.
2. Como nota de contexto para explicar uma causa ja identificada em Tier 1.

Nenhuma subparte desta secao pode ter o kick-off como unica fonte de uma conclusao diagnostica.

#### 2.1 Higiene do CRM

**Fonte valida:** Screenshots de CRM, exports, logs de atividade (Tier 1). Se nao disponivel, registre `[não disponível — acesso ao CRM nao concedido]` e nao preencha a tabela com dados declarados.

Para cada campo relevante visível nos inputs:
- Nome do campo
- Status observado: Preenchido sistematicamente / Inconsistente / Em branco / Nao visível nos inputs

Registre: leads com valor de ticket incorreto ou placeholder (ex: R$1), tarefas com descricao generica, leads sem evolucao de etapa.

#### 2.2 Leads Zumbi e LRT

**Fonte valida:** Screenshots ou exports do CRM mostrando leads e timestamps (Tier 1).

**Leads Zumbi:** leads visíveis nos inputs Tier 1 que estao em uma etapa sem atividade real ou sem evolucao. Registre o que foi observado. Se o CRM nao esta disponível, registre `[dados insuficientes — acesso ao CRM necessario]`. Nao use contagem de tarefas atrasadas declarada em kick-off como substituto.

**LRT (Lead Response Time):** se disponível nos inputs Tier 1 (timestamps de mensagens, logs de CRM), registre o tempo observado. Se nao disponível, registre `[não disponível]` — nao estime e nao use relato de kick-off como valor.

#### 2.3 Processo Real vs Declarado

Tabela comparando o que foi declarado em calls/briefing (Tier 2 — coluna "Declarado") com o que foi observado nos inputs Tier 1 — screenshots de CRM, cliente oculto (coluna "Real").

**Regra de inclusao:** Uma linha so existe na tabela se houver evidencia Tier 1 para a coluna "Real". Se so ha declaracao (Tier 2), a dimensao nao entra na tabela — registre abaixo dela como "Dimensoes sem evidencia observada disponivel: [lista]".

#### 2.4 Analise do Atendimento (Cliente Oculto e Atendimentos Reais)

**Fonte valida:** Transcricao de cliente oculto ou gravacao/transcricao de atendimento real ao cliente final (Tier 1). Transcricao de kick-off NAO e fonte valida para esta secao — e uma reuniao estrategica entre equipes, nao um atendimento comercial.

Se houver transcricao Tier 1 de atendimento:
- O que funcionou no atendimento (evidencia especifica do texto/gravacao)
- O que nao funcionou (evidencia especifica)
- Ciclo observado (etapas da conversa)

Se nao ha fonte Tier 1 disponível, registre `[não disponível — cliente oculto ou transcricao de atendimento real nao localizado nos inputs]`.

#### 2.5 Perfil do Time — Hunter vs Farmer

**Fonte valida:** Dados de conversao por canal (CSV/Tier 1), comportamento observado em atendimentos reais (cliente oculto/Tier 1), exports de CRM com conversao por origem de lead (Tier 1).

Declaracoes de kick-off sobre comportamento do time (ex: "consultoras com 100-200 leads", "time bom em criar tarefas") NAO sao evidencia diagnostica do perfil — sao contexto. Nao inclua como linha de evidencia na tabela.

Para cada evidencia listada, informe a fonte Tier 1:
- Evidencias de perfil Farmer (alta conversao em leads de base/canal organico — dado quantitativo)
- Evidencias de perfil Hunter (conversao em leads frios/canal pago — dado quantitativo)
- Diagnostico: qual perfil predomina com base nos dados e qual e exigido pelo mix de canais atual

Se nao ha dados de conversao por origem de lead alem do canal geral, registre `[dados insuficientes para diagnostico de perfil por canal]` e nao emita conclusao de perfil.

---

### Secao 3 — SLA de Atendimento por Score

Com base no ciclo de venda observado nos dados (nao em suposicoes):

| Score | SLA | Responsavel | Canal | Alerta se nao cumprido |
|---|---|---|---|---|
| ⭐⭐⭐⭐⭐ | X min | ... | ... | ... |
| ⭐⭐⭐⭐ | X h | ... | ... | ... |
| ⭐⭐⭐ | Regua automatica Xh | ... | ... | ... |
| ⭐⭐ / ⭐ | Nutricao passiva Xd | ... | ... | ... |

Se houver restricao tecnica conhecida que impede o cumprimento do SLA (ex: canal de entrada incompatível com resposta imediata), registre como observacao abaixo da tabela.

---

### Secao 4 — Consolidado

Tabela ASCII ou lista visual resumindo:
- O que esta funcionando (com evidencia)
- O que esta quebrado / critico (com evidencia)

Maximo de 8 itens por coluna. Sem recomendacoes — apenas o diagnostico.

---

## Auto-validacao

Antes de salvar, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Todo numero de benchmark tem referencia inline?
- [ ] Nenhum numero inventado — tudo rastreavel aos inputs ou marcado como `[não disponível]`?
- [ ] Nenhuma sugestao, recomendacao ou plano de acao (isso vai em outras skills)?
- [ ] Processo real vs declarado tem evidencia Tier 1 para a coluna "Real" em cada linha? Linhas sem Tier 1 foram removidas e listadas abaixo da tabela?
- [ ] Higiene do CRM registra apenas o que foi visível nos screenshots (Tier 1)? Se CRM nao disponivel, a secao esta marcada como `[não disponível]` sem dados declarados preenchendo a tabela?
- [ ] Impacto financeiro calculado so onde ha dados Tier 1 reais?
- [ ] Perfil Hunter/Farmer baseado exclusivamente em dados quantitativos de conversao por canal (Tier 1)? Nenhuma declaracao de kick-off foi usada como evidencia de perfil?
- [ ] Analise de atendimento (2.4) baseada exclusivamente em transcricao de cliente oculto ou atendimento real — nao em kick-off?
- [ ] Cada conclusao diagnostica tem sua fonte Tier 1 identificavel? Se a unica fonte e Tier 2, a conclusao foi substituida por `[dados insuficientes — fonte disponivel e Tier 2 (contexto)]`?

Se falhou em qualquer item → corrija antes de salvar.

## Finalização

Salve em `clientes/{slug}/outputs/ee-s4-diagnostico-comercial.md`.

Atualize `client.json`: progress.skills → completed, version++, append em history[].

Informe ao operador:
- "Diagnostico comercial salvo. Este output sera usado por: ee-s5-scripts-sdr, ee-s5-sdr-ia-config."
- Pergunte: "O diagnostico reflete o que voce observa no dia a dia? Alguma secao precisa de ajuste antes de continuar?"
- Sugira: proxima skill do dependency_graph.
