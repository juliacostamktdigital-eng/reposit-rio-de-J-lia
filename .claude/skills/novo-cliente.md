---
name: novo-cliente
description: Cria a pasta completa de um novo cliente no workspace — detecta raiz, copia template, cria links.md, CLAUDE.md e AGENTS.md. Ponto de entrada obrigatório antes de qualquer outra skill de cliente.
user-invocable: true
---

# /novo-cliente — Criar estrutura de pasta de cliente

Fluxo de 8 passos para criar pasta de cliente completa e pronta para uso.

## Passo 1 — Localizar raiz de clientes

Detectar em ordem:
1. `clientes/`
2. `builders-hub/clientes/`
3. `CLIENTES V4/`
4. `squads/[squad]/clientes/`

## Passo 2 — Nomear cliente

Converter para `lowercase-com-hifens` sem acentos. Verificar se já existe (se sim, ir para `/contexto`).

## Passo 3 — Encontrar template

Buscar em:
- `bases/_template/_template-cliente`
- `builders-hub/bases/_template/_template-cliente`
- `[raiz-clientes]/_template`

Se não encontrar, criar estrutura mínima manualmente.

## Passo 4 — Criar estrutura

Copiar template e garantir pastas: `calls/`, `checkins/`, `docs/`, `campanhas/`. Criar `.env` se necessário.

## Passo 5 — Coletar links

Solicitar: NotebookLM, Google Drive, site e links adicionais em formato "descrição - URL".

## Passo 6 — Escrever `links.md`

Documentar recursos com seções: bases, drives, web, outros. Itens não informados recebem `-`.

## Passo 7 — Criar `CLAUDE.md` e `AGENTS.md`

Escrever documentação referenciando `links.md`, incluir instruções sobre NotebookLM se aplicável.

## Passo 8 — Confirmar

Exibir estrutura final e orientar próximos passos:
- Adicionar dados do cliente
- Rodar `/contexto` para gerar Mission Control
- Preencher `.env`
- Rodar `/outra-notebooklm-cadastrar` se tiver notebook
- Rodar `/ekyte-refresh` se workspace for novo
