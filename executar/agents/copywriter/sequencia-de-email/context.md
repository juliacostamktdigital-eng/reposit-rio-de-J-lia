---
skill: sequencia-de-email
owner: copywriter
latest: v1.0.0
status: active
segment:
  - b2b
  - b2c
  - b2b2c
tier:
  - growth
  - scale
  - enterprise
software:
  - api
specialization:
  - ecom
  - inside-sales
  - saas
  - infoproduto
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Criação de sequências de e-mail automatizadas para nutrição e conversão de leads. Cobre fluxos de boas-vindas, nutrição, reativação e carrinho abandonado.

## Quando usar

- Setup de fluxo de e-mail marketing automatizado
- Revisão de sequência com baixa taxa de abertura ou clique
- Lançamento de produto com sequência de aquecimento

## Quando NÃO usar

- E-mails transacionais (confirmação de pedido, senha, etc.) — responsabilidade do Dev
- Newsletters manuais sem automação

## Inputs esperados

- `sequence_type` — boas-vindas | nutrição | vendas | reativação | carrinho-abandonado
- `audience` — quem vai receber e em que estágio do funil está
- `product` — o que está sendo promovido ou que contexto o lead tem
- `tone` — tom da marca
- `quantity` — número de e-mails na sequência
- `platform` — Mailchimp | ActiveCampaign | HubSpot | RD Station | outro

## Output esperado

Sequência completa de e-mails com: assunto, pré-header, corpo do e-mail e CTA para cada disparo, com intervalo recomendado entre disparos.

## Agentes que usam esta skill

- `owner`: copywriter
- `consumers`: coordenador (valida), dev-frontend (integra na plataforma de e-mail)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial com 4 tipos de sequência |
