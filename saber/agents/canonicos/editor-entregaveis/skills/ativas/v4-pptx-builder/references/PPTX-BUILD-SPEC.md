# PPTX Build Spec

## Contrato

Entrada:

```text
source/deck.json
```

Saida opcional:

```text
exports/deck.pptx
qa/qa-report.md
```

## `deck.json`

Campos obrigatorios:

- `meta.project`
- `meta.delivery`
- `meta.aspectRatio`
- `meta.brand`
- `slides[]`

Campos obrigatorios por slide:

- `id`
- `role`
- `section`
- `title`
- `component`
- `content`

Campos recomendados:

- `claimIds`
- `speakerNotes`
- `sourceRefs`

## Build com PptxGenJS

Padrao recomendado:

```javascript
import pptxgen from "pptxgenjs";

const pptx = new pptxgen();
pptx.layout = "LAYOUT_16x9";
pptx.author = "V4 Company";
pptx.company = "V4 Company";
pptx.subject = "Saber deliverable";
pptx.theme = {
  headFontFace: "Arial Black",
  bodyFontFace: "Calibri",
  lang: "pt-BR"
};
```

## Componentes minimos

O builder deve suportar:

- `hero-statement`
- `executive-summary`
- `metric-grid`
- `diagnosis-cards`
- `evidence-table`
- `funnel-flow`
- `priority-matrix`
- `roadmap-5w2h`
- `decision-slide`
- `handoff-slide`

## Verificacoes pos-build

- Arquivo existe e tem tamanho maior que zero.
- Deck usa 16:9.
- Slides possuem logo V4.
- Texto principal e editavel.
- Nao ha texto fora da area visivel.
- Numero de slides bate com `deck.json`.
