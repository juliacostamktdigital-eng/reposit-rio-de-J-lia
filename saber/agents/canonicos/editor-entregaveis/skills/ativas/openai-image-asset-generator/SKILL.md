---
name: openai-image-asset-generator
description: >-
  Use para gerar ou editar assets visuais com OpenAI Images API: fundos, texturas,
  gradientes, pessoas/objetos recortados, icones e imagens para slides, landing pages e criativos.
---

# OpenAI Image Asset Generator

## Quando usar

Use quando uma entrega precisar de assets visuais gerados: background, textura, papel, gradiente texturizado, pessoa recortada, objeto recortado, icone, key visual, mock conceitual ou variação visual.

## Seguranca de chave

Nunca grave chave real em arquivo versionado.

**Paperclip + Codex por assinatura (recomendado):** no agente (adapter **Environment variables**), defina **`OPENAI_IMAGE_API_KEY`** — o script de imagens usa só esta. **Não** defina **`OPENAI_API_KEY`** no mesmo agente: o `codex_local` trata essa var como “auth por API” e o Codex deixa de seguir o fluxo de assinatura/login.

**CLI local / fora do Paperclip:** pode usar `OPENAI_API_KEY` ou `OPENAI_IMAGE_API_KEY`.

```bash
export OPENAI_IMAGE_API_KEY="..."   # ou OPENAI_API_KEY
```

Esta skill inclui `.env.example` apenas como template. Se criar `.env` local, ele deve ficar ignorado pelo git.

## Script principal

```bash
node scripts/openai-image-assets.mjs generate --preset slide-background --prompt "fundo premium V4 com textura de papel vermelho profundo" --aspect 16:9 --out assets/generated/bg.png
```

Comandos:

- `generate` - chama `/v1/images/generations`.
- `edit` - chama `/v1/images/edits`.
- `batch-prepare` - cria JSONL para Batch API via `/v1/responses`.
- `batch-create` - faz upload do JSONL e cria `/v1/batches`.
- `batch-status` - consulta status.
- `batch-download` - baixa outputs e extrai imagens base64 quando possivel.

## Presets

- `cutout-person` - pessoa/figura recortada com fundo transparente.
- `cutout-object` - objeto isolado com fundo transparente.
- `slide-background` - fundo 16:9 para slides/decks.
- `paper-texture` - textura de papel, grain, editorial.
- `textured-gradient` - gradiente texturizado V4/client brand.
- `icon` - icone simples, fundo transparente.
- `ad-visual` - visual de campanha sem claims factuais.

## Regras

- Nao gerar pessoa real, celebridade, cliente ou funcionario identificavel sem autorizacao.
- Nao usar imagem gerada como evidencia real.
- Nao gerar logotipo V4; use assets oficiais.
- Para cutouts, preferir `background transparent`.
- Para fundos de slide, evitar texto dentro da imagem.
- Salvar assets em `assets/generated/` dentro do bundle da entrega.

## Referencias

- Consulte `references/PROMPT-PRESETS.md` para prompts base.
- Consulte `references/API-NOTES.md` para endpoints e limites praticos.
