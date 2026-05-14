---
skill: meeting-notes
owner: shared
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
specialization: []
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Registro padronizado de reuniões com cliente ou internas. Garante rastreabilidade de decisões, alinhamentos e próximos passos.

## Quando usar

- Qualquer reunião com cliente (estratégica, de alinhamento, de resultado)
- Reuniões internas com decisões que afetam a operação
- Calls de onboarding ou kickoff

## Quando NÃO usar

- Conversas informais sem decisões ou ações
- Trocas de mensagem em chat

## Inputs esperados

- `meeting_type` — tipo de reunião (estratégica, alinhamento, resultado, kickoff)
- `participants` — lista de participantes e papéis
- `date` — data e hora
- `duration` — duração aproximada
- `raw_notes` — anotações brutas ou transcrição

## Output esperado

Documento estruturado de ata com: contexto, pontos discutidos, decisões tomadas, próximos passos com responsáveis e prazos.

## Agentes que usam esta skill

- `consumers`: gerente, coordenador, gestor-de-projeto

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
