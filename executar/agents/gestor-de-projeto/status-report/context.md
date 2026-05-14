---
skill: status-report
owner: gestor-de-projeto
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
  - manual
specialization: []
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Relatório de andamento das entregas do sprint para o Coordenador. Registra o que foi concluído, o que está em andamento, o que está atrasado e quais são os riscos para os próximos dias.

## Quando usar

- Check-in de meio de sprint (D+3 ou D+4)
- Sempre que solicitado pelo Coordenador
- Antes do relatório consolidado que o Coordenador envia ao Gerente

## Inputs esperados

- `sprint_plan` — documento do sprint atual
- `tasks_status` — atualização de cada agente sobre suas tasks

## Output esperado

Relatório de status com semáforo visual por task e por área, riscos e próximas ações.

## Agentes que usam esta skill

- `owner`: gestor-de-projeto
- `consumers`: coordenador (inclui no report-consolidado)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
