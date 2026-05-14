---
skill: sprint-planning
owner: gestor-de-projeto
latest: v1.1.0
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
  - api
specialization: []
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Planejamento do ciclo de trabalho (sprint de 1–2 semanas) com tasks definidas, responsáveis, dependências e prazos. Garante que a equipe saiba o que fazer, em que ordem e até quando.

## Quando usar

- Início de cada sprint/semana
- Após reunião de resultado com novos direcionamentos
- Quando há mudança de prioridade do cliente

## Inputs esperados

- `strategy_doc` — documento de estratégia do Gerente
- `backlog` — lista de pendências e novas demandas
- `team_capacity` — disponibilidade estimada de cada agente
- `sprint_duration` — 1 semana | 2 semanas
- `client_deadline` — algum prazo externo que precisa ser respeitado

## Output esperado

Plano de sprint com: lista de tasks priorizadas, responsável por task, prazo, dependências e critério de conclusão.

## Agentes que usam esta skill

- `owner`: gestor-de-projeto
- `consumers`: todos os agentes (recebem suas tasks do sprint)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.1.0 | 2026-04-06 | latest | Modelo quinzenal alinhado ao BPMN FWO 1 com gate de aprovação Copy→Design→Gerente→Cliente |
| v1.0.0 | 2026-04-06 | — | Versão inicial |
