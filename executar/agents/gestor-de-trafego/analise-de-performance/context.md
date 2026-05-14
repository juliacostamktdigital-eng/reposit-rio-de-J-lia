---
skill: analise-de-performance
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
  - enterprise
software:
  - api
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

Análise periódica das métricas de campanhas pagas e geração de recomendações táticas de otimização. Alimenta o relatório consolidado do Coordenador.

## Quando usar

- Análise semanal de campanhas ativas
- Diagnóstico de queda de performance
- Antes de toda reunião de resultado

## Inputs esperados

- `platform` — Meta Ads | Google Ads | ambas
- `period` — período analisado
- `campaign_data` — exportação ou leitura das métricas via API/MCP
- `goals` — metas definidas para o período

## Output esperado

Relatório de performance com: visão por campanha, diagnóstico de causa-raiz de desvios, recomendações priorizadas e próximos passos.

## Agentes que usam esta skill

- `owner`: gestor-de-trafego
- `consumers`: coordenador (recebe o output para consolidar)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial com suporte a Meta e Google |
