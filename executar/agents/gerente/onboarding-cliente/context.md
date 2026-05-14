---
skill: onboarding-cliente
owner: gerente
latest: v1.1.0
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

Condução do processo completo de entrada de um novo cliente na V4. Garante alinhamento de expectativas, setup das ferramentas e kick-off operacional.

## Quando usar

- Contrato assinado com novo cliente
- Reativação de cliente antigo com novo contrato

## Quando NÃO usar

- Cliente já em operação (→ use `estrategia-comercial` para revisão)

## Inputs esperados

- `client_intake` — documento de intake (`executar/shared/client-intake`)
- `contract_details` — escopo contratado, prazo de entrega de primeiros resultados
- `tier` — porte do cliente

## Output esperado

Checklist de onboarding concluído, acessos configurados, primer reunião de kick-off realizada, plano de 30 dias definido.

## Agentes que usam esta skill

- `owner`: gerente
- `consumers`: coordenador (executa os passos operacionais)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.1.0 | 2026-04-06 | latest | Fases alinhadas ao fluxo BPMN FWO (Handoff 1/2, Planning, Embarque, Encerramento) |
| v1.0.0 | 2026-04-06 | — | Versão inicial |
