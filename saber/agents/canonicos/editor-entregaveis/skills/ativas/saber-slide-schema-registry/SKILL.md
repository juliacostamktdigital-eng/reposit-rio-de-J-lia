---
name: saber-slide-schema-registry
description: Use para escolher e aplicar o formato canonico de decks Saber em HTML 16:9, definindo sequencia de slides, componentes, densidade e payload esperado em source/deck.json.
---

# Saber Slide Schema Registry

## Quando usar

Use apos o intake e o mapa de evidencias, antes de gerar `source/deck.json`.

## Objetivo

Escolher o formato de entrega e converter conteudo aprovado em uma sequencia de slides com papel narrativo, componente visual e criterio de conteudo.

## Workflow

1. Identifique o tipo de deck vindo do intake.
2. Abra `references/SLIDE-SCHEMAS.md`.
3. Escolha o schema mais proximo.
4. Ajuste quantidade de slides conforme densidade real, sem perder a narrativa.
5. Para cada slide, defina:
   - `id`
   - `role`
   - `title`
   - `section`
   - `component`
   - `claim_ids`
   - `content`
   - `notes`
6. Gere ou atualize `source/deck.json`.

## Regras

- Um slide precisa ter um papel claro: contexto, diagnostico, insight, decisao, plano ou handoff.
- Nao use slide como deposito de texto.
- Use tabelas apenas quando comparacao for mais importante que persuasao.
- Use metric cards para numeros que mudam decisao.
- Use flow quando a decisao depende de sequencia operacional.
- Use matriz quando ha trade-off.

## Saida minima em `source/deck.json`

```json
{
  "meta": {
    "project": "<slug>",
    "delivery": "<delivery-slug>",
    "format": "html",
    "aspectRatio": "16:9",
    "brand": "V4 Company",
    "optionalExports": ["pptx"]
  },
  "slides": [
    {
      "id": "s01",
      "role": "executive-opening",
      "section": "ABERTURA",
      "title": "...",
      "component": "hero-statement",
      "claimIds": [],
      "content": {}
    }
  ]
}
```

## Referencias

- Consulte `references/SLIDE-SCHEMAS.md` para schemas canonicos.
