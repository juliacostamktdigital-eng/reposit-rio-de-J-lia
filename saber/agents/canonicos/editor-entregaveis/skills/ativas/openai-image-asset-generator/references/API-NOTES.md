# API Notes

## Endpoints usados

- `POST /v1/images/generations` - gera imagem por prompt.
- `POST /v1/images/edits` - edita imagem com prompt e, opcionalmente, mascara.
- `POST /v1/files` - upload de JSONL para batch.
- `POST /v1/batches` - cria batch assincrono.
- `GET /v1/batches/{id}` - consulta status.
- `GET /v1/files/{id}/content` - baixa resultado.

## Modelo

O script usa `OPENAI_IMAGE_MODEL` ou `--model`, com default `gpt-image-2`.

## Batch

A referencia oficial da Batch API lista `/v1/responses` entre os endpoints suportados. Por isso `batch-prepare` gera JSONL para `/v1/responses` usando ferramenta de imagem, em vez de assumir batch direto para `/v1/images/generations`.

## Tamanhos

Presets sugeridos:

- `16:9` -> `1536x864`
- `9:16` -> `864x1536`
- `1:1` -> `1024x1024`
- `4:5` -> `1024x1280`
- `1.91:1` -> `1536x804`

Se a API recusar um tamanho, rode novamente com `--size auto` ou outro tamanho suportado.
