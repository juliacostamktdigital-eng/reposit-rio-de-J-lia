---
name: delivery-format-briefing
description: Use ao produzir briefs que podem virar entregaveis finais para definir tipo de artefato, formato/aspect ratio, canal, exports, assets necessarios e proximo executor.
---

# Delivery Format Briefing

## Quando usar

Use em todo brief que mencione deck, landing page, criativo, imagem, documento, handoff visual, apresentacao, proposta, asset ou entrega final.

## Objetivo

Evitar que o `editor-entregaveis` receba uma task ambigua. O brief deve dizer qual formato a entrega precisa ter antes do builder iniciar.

## Workflow

1. Leia a demanda e identifique o artefato esperado.
2. Classifique o `delivery type`.
3. Defina o artefato principal.
4. Defina formato/aspect ratio.
5. Defina canal e modo de iteracao.
6. Liste exports obrigatorios.
7. Liste assets visuais necessarios.
8. Se algum item estiver indefinido, marque `TBD` e coloque em riscos/perguntas.

## Campos obrigatorios no brief

```markdown
## Delivery format contract

- Delivery type:
- Primary artifact:
- Format/aspect ratio:
- Target channel:
- Visual system:
- Required exports:
- Required image assets:
- Iteration mode:
```

## Guia rapido

- Slides iteraveis: `html-slide-deck`, `index.html`, `16:9`, `HTML-first`.
- PowerPoint formal: `pptx-export`, `exports/deck.pptx`, `16:9`, `HTML-first + export`.
- Landing page: `landing-page`, `landing/index.html`, `responsive`, `code-first`.
- Criativo feed: `static-creative`, `creatives/<name>.html`, `1:1` ou `4:5`, `static image-first`.
- Stories/Reels: `static-creative`, `creatives/<name>.html`, `9:16`, `static image-first`.
- Pack de assets: `image-asset-pack`, `assets/generated/`, formato por asset, `asset-first`.

## Regra

O Briefador define o contrato de formato, mas nao executa a entrega.
