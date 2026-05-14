---
name: delivery-format-router
description: Use no inicio de qualquer entrega para ler o delivery format contract do brief e escolher tipo de artefato, aspect ratio, bundle, skills de build, exports e assets necessarios.
---

# Delivery Format Router

## Quando usar

Use antes de qualquer intake especifico. Esta skill decide se a entrega e deck, landing page, criativo, image pack, documento ou custom.

## Workflow

1. Leia o `Delivery format contract` no brief.
2. Se nao existir, inferir com cuidado e registrar lacuna.
3. Defina:
   - `deliveryType`
   - `primaryArtifact`
   - `aspectRatio`
   - `targetChannel`
   - `visualSystem`
   - `requiredExports`
   - `requiredImageAssets`
   - `iterationMode`
4. Escolha a proxima skill:
   - `html-slide-deck` -> `saber-slide-intake` + `v4-html-slide-builder`
   - `pptx-export` -> `v4-html-slide-builder` + `v4-pptx-builder`
   - `landing-page` -> `v4-landing-page-builder`
   - `static-creative` -> `v4-creative-format-builder`
   - `image-asset-pack` -> `openai-image-asset-generator`
   - `document` -> skill documental apropriada, quando disponivel
5. Defina output bundle.

## Output esperado

```markdown
## Delivery route

- Delivery type:
- Primary artifact:
- Aspect ratio:
- Target channel:
- Builder skill:
- Asset skill:
- Required exports:
- Bundle path:
- Lacunas:
```

## Regra

Nao comece build visual sem aspect ratio, canal e artefato principal definidos ou explicitamente marcados como `TBD`.
