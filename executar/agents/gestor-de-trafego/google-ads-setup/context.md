---
skill: google-ads-setup
owner: gestor-de-trafego
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
  - local-business
  - saas
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Configuração de campanhas no Google Ads para captura de demanda existente via Search, Display e Performance Max. Complementa o tráfego de interrupção do Meta Ads com tráfego de intenção.

## Quando usar

- Cliente com budget que suporta dois canais (growth+)
- Produto com alta intenção de busca (pesquisado ativamente)
- Estratégia de funil completo (Meta topo, Google fundo)

## Quando NÃO usar

- Tier `starter` com budget insuficiente para dois canais
- Produto sem volume de busca comprovado (use Meta primeiro)

## Inputs esperados

- `keywords_research` — lista de palavras-chave e volumes de busca
- `budget_google` — orçamento mensal para Google Ads
- `landing_page_url` — página de destino
- `conversion_goal` — o que conta como conversão
- `specialization` — nicho para definir estrutura de campanha

## Output esperado

Campanhas configuradas no Google Ads com estrutura documentada, grupos de anúncios organizados por intenção e tracking de conversão ativo.

## Agentes que usam esta skill

- `owner`: gestor-de-trafego

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial com Search e Performance Max |
