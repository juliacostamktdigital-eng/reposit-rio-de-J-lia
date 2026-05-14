---
skill: hook-generation
owner: copywriter
latest: v1.0.0
status: active
segment:
  - b2b
  - b2c
  - b2b2c
tier:
  - starter
  - growth
  - scale
  - enterprise
software:
  - manual
specialization:
  - ecom
  - inside-sales
  - local-business
  - saas
  - infoproduto
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Geração de ganchos (hooks) para os primeiros 3 segundos de anúncios em vídeo, primeiras linhas de anúncios em texto, e headlines de conteúdo orgânico. O hook é o elemento que determina se o usuário para ou passa.

## Quando usar

- Criação de novos anúncios em vídeo
- Headline de anúncio em imagem ou carrossel
- Primeira linha de copy em qualquer formato
- Títulos de landing page

## Quando NÃO usar

- Copy completo de anúncio (→ `copy-de-anuncio`)
- Assunto de e-mail (tem lógica própria dentro de `sequencia-de-email`)

## Inputs esperados

- `product_description` — o que está sendo promovido
- `target_audience` — quem vai ver (perfil, dores, desejos)
- `objective` — o que o hook precisa fazer (parar o scroll, gerar clique, despertar curiosidade)
- `tone` — tom da marca (ex: direto, descontraído, técnico, empático)
- `specialization` — nicho para calibrar os gatilhos
- `quantity` — quantas variações gerar (mínimo recomendado: 5)

## Output esperado

Lista de hooks variados por tipo (dor, curiosidade, benefício, provocação, dado), com justificativa de cada abordagem.

## Agentes que usam esta skill

- `owner`: copywriter
- `consumers`: gestor-de-trafego (usa nos anúncios), designer (usa nos criativos)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial com 5 tipos de hook e adaptação por nicho |
