---
skill: análise-ropre-quarter-invictus
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
specialization:
  - ecom
  - inside-sales
  - local-business
  - saas
  - infoproduto
created: 2026-04-14
updated: 2026-04-14
---

## Propósito

Avaliar apresentações ROPRE do Quarter usando rubrica com 7 dimensões ponderadas. Gera nota final (0–10), classificação, pontos fortes, melhorias priorizadas por impacto e próximo passo prioritário.

O ROPRE (Resultados, Objetivos, Premissas/Riscos, Entregas, Expansão) é a reunião trimestral de prestação de contas e planejamento estratégico entre o coordenador e o cliente.

## Quando usar

- Ao receber o PDF de uma apresentação ROPRE do Quarter de um coordenador para revisão de qualidade
- Em calibração periódica dos ROPREs da equipe pelo gerente
- Na preparação de feedback estruturado pós-reunião

## Quando NÃO usar

- Para avaliar check-ins de quinzenas — use a skill de reunião de acompanhamento
- Para criar o ROPRE do zero — esta skill avalia, não gera
- Para projetos em V0 com menos de 30 dias — ajuste expectativas de D2 e D3

## Inputs esperados

- `ropre_pdf` — PDF ou texto extraído da apresentação ROPRE do Quarter
- `modelo_de_negocio` — (opcional) `ecommerce` ou `b2b-infoproduto` para adaptar os indicadores do D2

## Output esperado

Tabela de notas ponderadas por dimensão + nota final (0–10) + classificação + pontos fortes + melhorias priorizadas por impacto + checklist universal preenchido + próximo passo prioritário.

## Agentes que usam esta skill

- `owner`: coordenador
- `consumers`: gerente (validação de qualidade dos ROPREs da equipe)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-14 | latest | Versão inicial — calibrada com 7 ROPREs reais (Q1/Q2 2026) |
