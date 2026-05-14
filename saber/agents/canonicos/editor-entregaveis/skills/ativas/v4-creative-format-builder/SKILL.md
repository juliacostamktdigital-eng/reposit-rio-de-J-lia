---
name: v4-creative-format-builder
description: Use para construir criativos visuais em HTML/CSS nos formatos 16:9, 9:16, 1:1, 4:5 e 1.91:1, prontos para review e export PNG/JPG.
---

# V4 Creative Format Builder

## Quando usar

Use quando a entrega for criativo estatico, variação visual de campanha, card social, story, thumbnail, banner ou mock visual.

## Formatos suportados

- `16:9` - apresentacao, YouTube, banners horizontais.
- `9:16` - stories, reels, shorts.
- `1:1` - feed quadrado.
- `4:5` - feed vertical.
- `1.91:1` - ads/link preview.

## Workflow

1. Leia contrato de formato e copy aprovada.
2. Defina um frame por formato.
3. Crie `source/delivery.json`.
4. Construa `creatives/<format>.html`.
5. Use `openai-image-asset-generator` para fundo, textura, cutout, objeto ou icone quando necessario.
6. Prepare exports em `exports/` quando solicitado.
7. Rode QA visual.

## Regras

- Cada formato precisa preservar a ideia central sem apenas esticar layout.
- Texto deve caber no frame sem corte.
- Criativo de ads precisa ser legivel em scan rapido.
- Nao use imagem gerada para representar pessoa real sem autorizacao.
- Nao use logos ou marcas de terceiros sem fonte aprovada.

## Output bundle

```text
projetos/<slug>/entregaveis/<delivery-slug>/
  creatives/16x9.html
  creatives/9x16.html
  creatives/1x1.html
  assets/generated/
  exports/
  source/delivery.json
  qa/qa-report.md
```
