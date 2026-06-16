---
name: cs-notebooklm-consulta-cliente
description: Consulta o NotebookLM de um cliente específico para extrair contexto pontual sem carregar arquivos locais no chat. Usado como subskill pela /ekyte-briefing e invocável diretamente.
user-invocable: true
---

# /cs-notebooklm-consulta-cliente — Consultar NotebookLM do cliente

Extrai contexto do cliente via NotebookLM sem precisar carregar arquivos locais no chat.

## Quando usar

- `/cs-notebooklm-consulta-cliente <cliente> "<tarefa>"`
- "consulta o NotebookLM do cliente X sobre Y"
- "puxa contexto do cliente X pra task Y"
- Economizar tokens consultando base já indexada

## Fluxo

**Passo 1:** Validar cliente e tarefa (dois inputs obrigatórios)

**Passo 2:** Verificar pasta `clientes/<cliente>/` e extrair Notebook ID do `CLAUDE.md`

**Passo 3:** Echo de proteção — confirmar cliente e tarefa antes de disparar

**Passo 4:** Decompor tarefa em até 5 perguntas fechadas e independentes. Cada pergunta inclui: "Se não encontrar, responda exatamente 'NAO ENCONTRADO'"

**Passo 5:** Disparar perguntas via MCP notebooklm em sequência (não paralelo — NotebookLM não mantém contexto entre chamadas)

**Passo 6:** Salvar artefato em `clientes/<cliente>/contexto-notebook/<YYYY-MM-DD-HHMM>-<slug>.md`

**Passo 7:** Devolver síntese + link do arquivo no chat

## Regras críticas

- Perguntas **independentes e fechadas** — máximo 5
- Se 2 perguntas consecutivas retornarem "NAO ENCONTRADO", parar
- Formato do arquivo: markdown com Tarefa, Perguntas, Respostas literais e Síntese
- Se sessão expirar: abortar e instruir re-autenticação do NotebookLM
