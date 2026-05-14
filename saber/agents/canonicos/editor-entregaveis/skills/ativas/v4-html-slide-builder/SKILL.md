---
name: v4-html-slide-builder
description: Use para construir decks HTML visuais 16:9 como entrega final iteravel do Saber, aplicando design V4, navegacao entre slides, responsividade controlada e estrutura exportavel para PPTX.
---

# V4 HTML Slide Builder

## Quando usar

Use depois que `source/deck.json` estiver estruturado e o design system V4 estiver definido. Esta e a skill principal de build para o inicio do processo Saber.

## Objetivo

Gerar `index.html` como deck visual final, 16:9, navegavel, revisavel e pronto para iteracao. O HTML deve ser bom o suficiente para ser entregue e tambem estruturado o bastante para virar PPTX depois.

## Workflow

1. Leia `source/deck.json`.
2. Leia `v4-slide-design-system`.
3. Crie ou atualize `index.html`.
4. Estruture cada slide como um frame 16:9.
5. Aplique componentes V4 conforme `component`.
6. Garanta navegacao por teclado e/ou controles discretos.
7. Garanta que textos, tabelas e blocos sejam editaveis no codigo.
8. Registre assets e dependencias locais.
9. Passe para `v4-slide-qa-gate`.

## Regras de layout

- Cada slide deve ter proporcao 16:9 fixa.
- O deck pode ocupar a viewport, mas o conteudo interno nao pode depender de zoom manual.
- Use CSS tokens para cores, tipografia, spacing e componentes.
- Preserve uma estrutura semantica facil de converter para PPTX.
- Nao use imagem full-slide para texto.
- Nao dependa de CDN externa sem necessidade.
- O HTML precisa abrir localmente ou via servidor simples.

## Output bundle

```text
projetos/<slug>/entregaveis/<delivery-slug>/
  index.html
  source/deck.json
  exports/deck.pptx
  qa/qa-report.md
  README.md
```

## Referencias

- Consulte `references/HTML-SLIDE-BUILD-SPEC.md` para estrutura recomendada.
