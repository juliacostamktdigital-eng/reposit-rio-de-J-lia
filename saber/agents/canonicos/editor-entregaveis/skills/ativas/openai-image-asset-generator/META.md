# META - openai-image-asset-generator
**Status:** ativa
**Atualizado:** 2026-04-27
**Fonte:** agente:codex

## Papel

Gerar assets visuais para decks, landing pages, criativos e fundos usando OpenAI Images API.

## Dependencias

- `OPENAI_IMAGE_API_KEY` no ambiente (Paperclip: preferir no adapter env; evita forçar Codex em modo API)
- ou `OPENAI_API_KEY` (CLI / legado)
- Node.js com `fetch`, `FormData` e `Blob`

## Seguranca

Nao versionar `.env` com chave real.

## Promocao global

Candidata a global apos primeiro piloto com assets em entrega real.
