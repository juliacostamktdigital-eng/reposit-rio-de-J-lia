---
skill: report-consolidado
owner: coordenador
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

Coleta e consolidação dos status e resultados de todos os agentes especialistas em um único relatório coerente para o Gerente. Elimina a necessidade do Gerente de consultar cada agente individualmente.

## Quando usar

- Antes de toda reunião de resultado do Gerente com o cliente
- Relatório semanal de andamento da conta
- Quando o Gerente solicita visão geral da operação

## Quando NÃO usar

- Relatório tático específico de um canal (→ deixar para o agente especialista)

## Inputs esperados

- `status_trafego` — update do Gestor de Tráfego
- `status_copy` — update do Copywriter
- `status_projeto` — update do Gestor de Projeto
- `status_dev` — update do Dev Frontend / Infra (se aplicável)
- `period` — período coberto pelo relatório

## Output esperado

Documento consolidado com: visão geral da operação, status por área, alertas e riscos, próximos passos prioritários.

## Agentes que usam esta skill

- `owner`: coordenador
- `consumers`: gerente (recebe o output)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
