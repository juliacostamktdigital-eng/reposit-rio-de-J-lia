---
skill: briefing-intake
owner: coordenador
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

Recebimento, validação e estruturação de briefings vindos do Gerente ou diretamente do cliente. Transforma pedidos vagos em especificações acionáveis para os agentes especialistas.

## Quando usar

- Ao receber uma demanda nova do Gerente ou do cliente
- Antes de qualquer delegação de tarefa

## Quando NÃO usar

- Tarefas simples e repetitivas já documentadas em SOP (use direto o SOP)

## Inputs esperados

- `raw_request` — pedido bruto do Gerente ou cliente
- `requester` — quem pediu (gerente ou cliente)
- `urgency` — nível de urgência (baixa | média | alta | crítica)
- `context` — contexto disponível sobre o cliente ou campanha

## Output esperado

Briefing estruturado pronto para ser encaminhado ao agente correto, com: objetivo, entregável esperado, prazo, contexto, restrições.

## Agentes que usam esta skill

- `owner`: coordenador
- `consumers`: todos os agentes especialistas (recebem o output)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
