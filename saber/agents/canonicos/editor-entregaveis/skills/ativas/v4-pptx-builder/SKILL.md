---
name: v4-pptx-builder
description: Use quando for necessario exportar decks PowerPoint editaveis em 16:9 a partir de source/deck.json ou do HTML visual final, mantendo design V4.
---

# V4 PPTX Builder

## Quando usar

Use apenas quando a task pedir PPTX, quando o handoff exigir PowerPoint editavel, ou quando a revisao final precisar desse formato.

## Objetivo

Gerar `exports/deck.pptx` editavel, em 16:9, com componentes V4, sem transformar o deck inteiro em imagem.

## Workflow

1. Leia `source/deck.json`.
2. Leia `v4-slide-design-system`.
3. Configure apresentacao 16:9.
4. Defina tema, masters e componentes reutilizaveis.
5. Gere cada slide conforme `component`.
6. Salve `exports/deck.pptx` no output bundle.
7. Se possivel, gere render para QA.
8. Passe para `v4-slide-qa-gate`.

## Regras tecnicas

- O PPTX final precisa ser editavel.
- Texto deve entrar como texto, nao como imagem.
- Tabelas devem ser objetos editaveis sempre que possivel.
- Imagens so para assets, logos, screenshots ou elementos visuais reais.
- Em PptxGenJS, usar `pptx.layout = "LAYOUT_16x9"` ou layout custom equivalente.
- Usar slide masters para barra, logo e padroes repetidos quando possivel.
- Manter `source/deck.json` como fonte reprodutivel do deck.

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

- Consulte `references/PPTX-BUILD-SPEC.md` para contrato tecnico.
