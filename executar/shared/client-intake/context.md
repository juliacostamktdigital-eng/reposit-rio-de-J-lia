---
skill: client-intake
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

Coleta estruturada de informações essenciais sobre um novo cliente antes do início da operação. Garante que todos os agentes partam do mesmo entendimento do contexto, objetivos e restrições do cliente.

## Quando usar

- Primeiro contato operacional com um cliente novo
- Retomada de cliente após hiato de mais de 60 dias
- Mudança significativa de escopo ou produto do cliente

## Quando NÃO usar

- Cliente já ativo com contexto documentado e atualizado
- Reunião de rotina sem mudança de escopo

## Inputs esperados

- `client_name` — nome da empresa ou pessoa
- `contact_name` — nome do responsável pelo contato
- `segment` — b2b, b2c ou b2b2c
- `product_description` — o que o cliente vende
- `main_goal` — objetivo principal da contratação da V4
- `current_channels` — canais digitais já em uso
- `monthly_budget` — investimento mensal disponível
- `timeline` — prazo esperado para primeiros resultados

## Output esperado

Documento estruturado de intake com todas as informações coletadas, pronto para ser consumido pelos agentes especialistas. Formato: Markdown com seções nomeadas.

## Agentes que usam esta skill

- `consumers`: gerente, coordenador, copywriter, designer

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
