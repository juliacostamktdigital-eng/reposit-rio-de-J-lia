---
skill: sop-template
owner: shared
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

Geração de Procedimento Operacional Padrão (SOP) para qualquer processo recorrente da operação. Garante que processos sejam documentados, replicáveis e auditáveis.

## Quando usar

- Novo processo recorrente identificado
- Processo existente com erros frequentes por falta de documentação
- Onboarding de novo agente ou colaborador em um processo

## Quando NÃO usar

- Tarefas únicas (one-off) sem recorrência
- Processos ainda em experimentação (documente apenas após validação)

## Inputs esperados

- `process_name` — nome do processo
- `process_owner` — agente responsável pela execução
- `trigger` — o que dispara o processo
- `steps_raw` — descrição livre dos passos
- `tools_used` — ferramentas envolvidas
- `frequency` — com que frequência ocorre

## Output esperado

Documento SOP completo com objetivo, responsáveis, passo a passo numerado, critérios de qualidade e referências.

## Agentes que usam esta skill

- `consumers`: coordenador, gestor-de-projeto, dev-frontend, dev-infra-deploy, gestor-de-trafego

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
