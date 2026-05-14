---
skill: checklist-entrega-assets
owner: designer
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

Protocolo de entrega de assets visuais com checklist de qualidade, organização de arquivos, nomeação padronizada e especificações técnicas por destino (plataforma de anúncio, dev, cliente).

## Quando usar

- Ao finalizar qualquer conjunto de assets
- Antes de qualquer entrega ao Coordenador, Dev ou Gestor de Tráfego

## Inputs esperados

- `assets_produced` — lista de peças produzidas
- `destination` — para quem vai: gestor-de-trafego | dev-frontend | cliente
- `platforms` — plataformas de destino

## Output esperado

Pasta de assets organizada com nomeação padronizada, formatos corretos por plataforma e checklist de qualidade assinado.

## Agentes que usam esta skill

- `owner`: designer
- `consumers`: gestor-de-trafego (recebe assets), dev-frontend (recebe assets)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
