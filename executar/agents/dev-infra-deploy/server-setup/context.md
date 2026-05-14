---
skill: server-setup
owner: dev-infra-deploy
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
  - saas
  - inside-sales
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Configuração completa de ambiente de produção para hospedar as aplicações e páginas do cliente. Inclui servidor, domínio, SSL, DNS e configurações de segurança básicas.

## Quando usar

- Novo cliente com necessidade de hospedagem
- Migração de ambiente existente
- Setup de ambiente de staging

## Quando NÃO usar

- Deploy em plataformas managed como Shopify ou Webflow (não requer configuração de servidor)
- Tier `starter` com solução de LP builder simples

## Inputs esperados

- `application_type` — landing page | WordPress | Next.js | e-commerce | API
- `expected_traffic` — volume de visitas esperado (para dimensionamento)
- `domain` — domínio a configurar
- `ssl_required` — sim (padrão) | não
- `budget_infra` — orçamento mensal para infraestrutura

## Output esperado

Ambiente configurado e documentado: URL acessível, SSL ativo, DNS propagado, acesso seguro entregue ao Coordenador.

## Agentes que usam esta skill

- `owner`: dev-infra-deploy
- `consumers`: dev-frontend (usa o ambiente para deploy)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
