---
skill: meta-ads-setup
owner: gestor-de-trafego
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
software:
  - mcp
  - api
specialization:
  - ecom
  - inside-sales
  - local-business
  - infoproduto
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Configuração completa de campanhas no Meta Ads Manager (Facebook e Instagram). Cobre estrutura de conta, campanhas, conjuntos de anúncios e anúncios para qualquer objetivo de negócio.

## Quando usar

- Criação de nova conta de anúncios para cliente
- Setup de nova campanha do zero
- Reestruturação de conta com performance degradada

## Quando NÃO usar

- Otimizações pontuais em campanhas ativas (→ `analise-de-performance`)
- Campanhas exclusivas Google (→ `google-ads-setup`)

## Inputs esperados

- `objective` — objetivo de negócio (leads, vendas, reconhecimento, tráfego)
- `budget_monthly` — orçamento mensal disponível para Meta
- `target_audience` — descrição do público-alvo
- `product_description` — o que está sendo anunciado
- `landing_page_url` — URL de destino dos anúncios
- `specialization` — nicho: ecom | inside-sales | local-business | infoproduto
- `pixel_id` — ID do Meta Pixel instalado na página

## Output esperado

Estrutura de campanha configurada e ativa no Meta Ads Manager, com documentação da estrutura (campanhas > conjuntos > anúncios) e link de acesso ao gerenciador.

## Agentes que usam esta skill

- `owner`: gestor-de-trafego
- `consumers`: coordenador (valida antes de subir)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial com estrutura para ecom, leads e local |
