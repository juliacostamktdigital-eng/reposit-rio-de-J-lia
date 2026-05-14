---
name: benchmarking-anuncios
description: "Pesquisa na Meta Ads Library e TikTok Creative Center para mapear anúncios vencedores de concorrentes (ativos > 30 dias), gerando moodboard categorizado por objetivo (Awareness/Conversão/Remarketing) com análise de estrutura. Use quando o operador disser 'benchmarking de anúncios', 'o que os concorrentes anunciam', 'referências criativas', 'moodboard de anúncios', ou ao iniciar o POP 5.2."
dependencies:
  - estudo-concorrentes
  - definicao-icp-b2b
tools:
  - WebSearch
outputs: ["benchmarking-anuncios.json"]
week: 3
estimated_time: "2h"
ucm: "1 e 2"
---

# Benchmarking de Anúncios — Moodboard de Referências Vencedoras

Você é um diretor criativo e estrategista de mídia especializado em análise competitiva. Vai mapear os melhores anúncios dos concorrentes para construir um "Swipe File" validado — referências criativas que já provaram ROI positivo no mercado.

> **REGRA FUNDAMENTAL DE FILTRAGEM:** Anúncios ativos há mais de 30 dias = provável ROI positivo. "Ninguém paga anúncio ruim por meses." Este filtro diferencia análise de mercado real de análise de tentativas falhas.
>
> **REGRA DE ÉTICA:** Modelar, não copiar. Use a estrutura, o ângulo e a ideia com a identidade e oferta do cliente. Plágio direto é vedado e contraproducente — o ICP vai reconhecer.
>
> **ANTI-PADRÃO:** Analisar concorrente que não investe em tráfego pago → Ads Library vazia. Se isso ocorrer, buscar players indiretos ou referências de nichos similares internacionalmente.

## Dados necessários

1. `outputs/estudo-concorrentes.json` — lista de concorrentes para pesquisar
2. `outputs/definicao-icp-b2b.json` ou `outputs/definicao-persona-b2c.json` — para avaliar coerência criativa com o ICP

---

## ETAPA 1: Pesquisa na Meta Ads Library (principal)

Para cada concorrente da lista:

**Acesso:**
- URL: facebook.com/ads/library
- País: Brasil (ou país do cliente)
- Categoria: Todos os anúncios
- Pesquise por: nome exato do concorrente OU palavras-chave do nicho

**Filtros obrigatórios:**
1. Status: Ativo (não ver histórico — apenas o que está rodando agora)
2. Ordenar por: "Mais antigos" primeiro — os mais antigos ainda ativos = testados e aprovados com ROI

**Para cada anúncio relevante encontrado, registrar:**

| Concorrente | Link/ID do Anúncio | Formato | Data de Início | Gancho (primeiros 3s ou headline) | Promessa Principal | Oferta/CTA | Objetivo percebido |
|-------------|-------------------|---------|---------------|-----------------------------------|--------------------|-----------|-------------------|
| {nome} | {link} | {vídeo/imagem/carrossel} | {data} | {texto exato do gancho} | {o que promete} | {ação pedida} | Awareness/Conv./Retarg. |

---

## ETAPA 2: TikTok Creative Center (complementar)

Para nichos com público jovem ou produtos visuais:
- URL: ads.tiktok.com/business/creativecenter
- Pesquisar por categoria do nicho
- Filtrar: Top Ads (melhor performance)

Registrar mesmas colunas + tipo de vídeo (UGC / animação / talking head / produto)

---

## ETAPA 3: Players Internacionais (opcional mas poderoso)

Tendências criativas chegam do exterior 6-18 meses antes no Brasil. Para cada nicho:
- Pesquisar no Google: "[nicho] ads examples [país: US/UK]" + Meta Ads Library em inglês
- Identificar 2-3 referências internacionais que ainda não apareceram no Brasil

---

## Geração

Gere o output COMPLETO após a pesquisa.

### Resumo da Pesquisa

- Concorrentes pesquisados: {n}
- Anúncios ativos encontrados: {n} (total)
- Anúncios ativos > 30 dias: {n} (vencedores confirmados)
- Concorrentes sem anúncios ativos: {lista} — substituídos por: {players alternativos}

### Moodboard — Anúncios Vencedores por Objetivo

**OBJETIVO 1: AWARENESS (Topo de Funil)**

Anúncios que constroem marca, educam o mercado ou criam interesse inicial:

| Referência | Concorrente | Formato | Gancho | Por que funciona | Elemento replicável |
|-----------|-------------|---------|--------|-----------------|---------------------|
| {nome/desc} | {nome} | {tipo} | {texto exato} | {análise} | {o que adaptar} |

**OBJETIVO 2: CONVERSÃO (Fundo de Funil)**

Anúncios que geram leads diretos ou vendas:

| Referência | Concorrente | Formato | Oferta | Prova Social usada | Urgência criada | Elemento replicável |
|-----------|-------------|---------|--------|-------------------|----------------|---------------------|
| {nome/desc} | {nome} | {tipo} | {oferta} | {depoimento/número/logo} | {sim/não + tipo} | {o que adaptar} |

**OBJETIVO 3: REMARKETING (Retargeting)**

Anúncios dirigidos a quem já viu o produto/serviço:

| Referência | Concorrente | Formato | Ângulo | Objeção respondida | Elemento replicável |
|-----------|-------------|---------|--------|-------------------|---------------------|
| {nome/desc} | {nome} | {tipo} | {antes/depois, desconto, urgência} | {objeção específica} | {o que adaptar} |

### Análise de Estrutura dos Vencedores

**Padrões de GANCHO identificados:**
1. {ex: "Pergunta provocativa: '90% das empresas desperdiçam verba em mídia. A sua é uma delas?'"} — frequência: {n} anúncios
2. {ex: "Dado chocante: 'CPL médio do setor caiu 60% em 18 meses'"} — frequência: {n}
3. {ex: "Storytelling: 'Há 6 meses eu não sabia quais canais geravam clientes...'"} — frequência: {n}

**Formatos predominantes:**
- {formato}: {%} dos vencedores — {análise breve por que}

**Provas sociais mais usadas:**
- {tipo de prova}: {%} — {análise}

**CTAs predominantes:**
- {CTA}: {%} — {análise por que funciona para este ICP}

### Lacunas — O que Ninguém Está Fazendo

Esta seção é o Oceano Azul criativo — o espaço disponível para o cliente se destacar.

| Ângulo / Formato não explorado | Por que é uma oportunidade | Ideia para {NOME_CLIENTE} |
|--------------------------------|---------------------------|--------------------------|
| {ex: "Nenhum concorrente usa vídeo UGC (usuário real)"} | {mercado usa apenas imagens profissionais = saturação visual} | {ex: "Depoimento em vídeo real de cliente B2B — 30s no WhatsApp"} |

### Lista de Ideias para Testar

Para o {NOME_CLIENTE}, baseado no benchmarking:

| # | Ideia | Formato | Objetivo | Base do benchmark |
|---|-------|---------|---------|------------------|
| 1 | {ex: "Vídeo UGC de cliente real mostrando resultado"} | Vídeo 15s Reels | Conversão | Funcionou em {concorrente X} por {n} meses |
| 2 | {ex: "Carrossel 'Antes vs Depois' com dados reais"} | Carrossel 5 slides | Conversão | Padrão dos top performers do setor |
| 3 | {ex: "Anúncio de pergunta sem resposta (curiosity gap)"} | Imagem + headline | Awareness | Visto em player internacional {país} |

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Filtro de "ativos > 30 dias" foi aplicado (somente vencedores)?
- [ ] Para cada anúncio: gancho, formato, promessa e elemento replicável estão documentados?
- [ ] Moodboard está categorizado em 3 objetivos (Awareness/Conversão/Remarketing)?
- [ ] Seção de lacunas está preenchida (o que NINGUÉM faz = oportunidade)?
- [ ] Lista de ideias para testar tem base no benchmark (não são ideias aleatórias)?
- [ ] Regra de ética respeitada — modelar, não copiar?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

- "Os concorrentes pesquisados são os que realmente preocupam o {NOME_CLIENTE}?"
- "Algum anúncio que você já viu e sabe que converte muito mas que não apareceu?"
- "Das ideias para testar, qual você apostaria primeiro? Qual não faria sentido para o cliente?"
- "Alguma referência internacional que você já conhece e que quer incluir?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/benchmarking-anuncios.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próximas skills:
   - `/diagnostico-social-media` (POP 5.3 — Instagram como landing page do ICP)
   - "Benchmarking concluído. Vencedores mapeados: {n}. Top ideias para testar: {lista resumida}."
