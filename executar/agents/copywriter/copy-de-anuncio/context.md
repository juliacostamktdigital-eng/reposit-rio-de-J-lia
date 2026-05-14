---
skill: copy-de-anuncio
owner: copywriter
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
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

Escrita do copy completo de anúncios pagos (Meta Ads e Google Ads), incluindo texto principal, headline, descrição e CTA, adaptado por formato, plataforma e nicho.

## Quando usar

- Criação de novos anúncios para qualquer plataforma paga
- Revisão de copies com baixo CTR ou taxa de conversão
- A/B test de variações de mensagem

## Inputs esperados

- `briefing` — documento de briefing do Coordenador
- `platform` — Meta | Google | ambos
- `format` — imagem | carrossel | vídeo | texto (Google)
- `hook` — hook escolhido (output de `hook-generation`)
- `objective` — o que o anúncio precisa fazer (clique, lead, venda)
- `client_intake` — contexto do cliente (tom, restrições)

## Output esperado

Copy completo formatado por plataforma com: texto principal, headline, descrição, CTA e variações para teste.

## Agentes que usam esta skill

- `owner`: copywriter
- `consumers`: gestor-de-trafego (usa para criar anúncios), designer (usa para compor criativos)

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial com templates Meta e Google por nicho |
