---
skill: ci-cd-pipeline
owner: dev-infra-deploy
latest: v1.0.0
status: active
segment:
  - b2b
  - b2c
  - b2b2c
tier:
  - scale
  - enterprise
software:
  - api
specialization:
  - saas
  - ecom
  - inside-sales
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Montagem de pipeline de CI/CD (Integração Contínua / Deploy Contínuo) para automatizar o processo de build, teste e deploy de aplicações, reduzindo erros manuais e tempo de entrega.

## Quando usar

- Cliente com desenvolvimento ativo (updates frequentes)
- Time com múltiplos desenvolvedores
- Necessidade de ambiente de staging antes de produção

## Quando NÃO usar

- Sites estáticos simples que fazem deploy manual (use direto Vercel/Netlify)
- Tier `starter` ou `growth` sem desenvolvimento ativo

## Inputs esperados

- `repository` — repositório do código (GitHub, GitLab, Bitbucket)
- `stack` — linguagem e framework
- `environments` — staging | produção | ambos
- `deploy_target` — Vercel | servidor VPS | outro
- `test_coverage` — há testes automatizados? (define se CI tem etapa de teste)

## Output esperado

Pipeline configurado e documentado com: branch strategy, workflow de CI/CD, ambientes configurados e processo de rollback.

## Agentes que usam esta skill

- `owner`: dev-infra-deploy
- `consumers`: dev-frontend (usa o pipeline para fazer deploys)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial com GitHub Actions |
