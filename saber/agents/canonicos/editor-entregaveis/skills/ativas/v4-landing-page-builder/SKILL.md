---
name: v4-landing-page-builder
description: Use para construir landing pages responsivas como entregaveis finais do Saber, aplicando V4/client brand, hierarquia de conversao, HTML/CSS/JS e QA visual.
---

# V4 Landing Page Builder

## Quando usar

Use quando o contrato de entrega pedir `landing-page` ou uma pagina web responsiva como artefato final.

## Objetivo

Construir `landing/index.html` com experiencia visual final, responsiva e pronta para iteracao.

## Workflow

1. Leia brief, copy aprovada e contrato de formato.
2. Defina a acao principal da pagina.
3. Monte `source/delivery.json`.
4. Crie `landing/index.html` com CSS local.
5. Use assets V4/client brand e assets gerados quando necessario.
6. Garanta responsividade desktop/mobile.
7. Rode QA visual.

## Regras

- Landing page nao e deck verticalizado; precisa ter fluxo de conversao.
- Hero deve deixar claro oferta, prova ou decisao.
- CTA principal deve ser consistente.
- Nao invente claims de performance.
- Nao usar imagem gerada como prova real.
- Assets gerados devem ser decorativos, conceituais ou explicitamente marcados.

## Output bundle

```text
projetos/<slug>/entregaveis/<delivery-slug>/
  landing/index.html
  source/delivery.json
  assets/generated/
  exports/
  qa/qa-report.md
  README.md
```
