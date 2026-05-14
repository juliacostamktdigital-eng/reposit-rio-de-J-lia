# HTML Slide Build Spec

## Contrato

Entrada:

```text
source/deck.json
```

Saida principal:

```text
index.html
```

Export opcional:

```text
exports/deck.pptx
```

## Estrutura recomendada

```html
<main class="deck" data-aspect-ratio="16:9">
  <section class="slide slide--hero" data-slide-id="s01">
    ...
  </section>
</main>
```

## CSS minimo

```css
:root {
  --v4-red: #E50914;
  --v4-black: #1A1814;
  --v4-white: #FFFFFF;
  --v4-gray: #464646;
  --v4-yellow: #FFDD00;
  --slide-w: min(100vw, calc(100vh * 16 / 9));
  --slide-h: calc(var(--slide-w) * 9 / 16);
}

.slide {
  width: var(--slide-w);
  height: var(--slide-h);
  aspect-ratio: 16 / 9;
  background: var(--v4-black);
  color: var(--v4-white);
}
```

## Navegacao

- Setas esquerda/direita alternam slides.
- Indicador discreto de slide atual.
- Impressao/export deve preservar um slide por pagina quando possivel.

## Preparacao para PPTX

- Cada slide deve ter `data-slide-id`.
- Componentes devem ter classes previsiveis.
- Textos devem estar em elementos HTML reais.
- Tabelas devem usar `<table>` quando forem tabelas.
- Metricas devem usar blocos identificaveis.

## QA tecnico

- Abrir sem erro no browser.
- Sem overflow visual em viewport desktop comum.
- Conteudo legivel em 16:9.
- Sem dependencia remota obrigatoria.
- Sem cores proibidas fora de contexto.
