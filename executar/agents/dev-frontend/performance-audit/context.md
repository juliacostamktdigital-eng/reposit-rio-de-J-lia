---
skill: performance-audit
owner: dev-frontend
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
specialization: []
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Auditoria de performance técnica de páginas do cliente com foco em Core Web Vitals, velocidade de carregamento e impacto na taxa de conversão.

## Quando usar

- Landing page com taxa de conversão abaixo do esperado
- Antes de qualquer campanha de grande volume de tráfego
- Auditoria mensal de páginas ativas

## Inputs esperados

- `page_url` — URL da página a auditar
- `device_focus` — mobile | desktop | ambos
- `current_conversion_rate` — taxa atual (se disponível)

## Output esperado

Relatório de performance com score atual, problemas identificados por prioridade e plano de ação com estimativa de impacto.

## Agentes que usam esta skill

- `owner`: dev-frontend
- `consumers`: gestor-de-trafego (recebe para justificar baixa conversão), coordenador

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
