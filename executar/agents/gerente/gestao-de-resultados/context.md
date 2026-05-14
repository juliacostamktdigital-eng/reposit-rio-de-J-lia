---
skill: gestao-de-resultados
owner: gerente
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
  - api
specialization: []
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Leitura periódica dos KPIs da conta, diagnóstico de desvios e geração de recomendações de ajuste para o ciclo seguinte. É a skill central da reunião de resultado com o cliente.

## Quando usar

- Reunião semanal ou quinzenal de resultado
- Relatório mensal da conta
- Qualquer momento em que o cliente pede "como estamos indo?"

## Quando NÃO usar

- Análise tática de campanha específica (→ `gestor-de-trafego/analise-de-performance`)
- Diagnóstico inicial sem histórico de dados (→ `estrategia-comercial`)

## Inputs esperados

- `kpis_report` — dados de performance do período (pode vir de API de analytics, planilha ou relatório manual)
- `meta_target` — metas acordadas no início do ciclo
- `period` — período analisado
- `qualitative_notes` — observações do coordenador ou dos agentes especialistas

## Output esperado

Dashboard narrativo: visão do período, análise de cada KPI vs. meta, diagnóstico de causa-raiz dos desvios, recomendações priorizadas e próximos passos.

## Agentes que usam esta skill

- `owner`: gerente
- `consumers`: coordenador (alimenta com dados), cliente (recebe o output)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
