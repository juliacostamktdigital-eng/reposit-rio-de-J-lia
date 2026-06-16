---
name: outra-notebooklm-cadastrar
description: Cadastra ou atualiza links de NotebookLM para múltiplos clientes existentes de uma vez — processa lista colada, valida pastas, atualiza CLAUDE.md de cada cliente.
user-invocable: true
---

# /outra-notebooklm-cadastrar — Cadastro em massa de NotebookLM

Registra ou atualiza notebooks de vários clientes de uma vez, sem reexecutar `/novo-cliente`.

## Quando usar

- `/outra-notebooklm-cadastrar` diretamente
- "cadastrar notebooks dos clientes"
- "colar uma lista de links de NotebookLM"
- Atualizar NotebookLM de cliente já existente
- Vários links para organizar simultaneamente

## Fluxo

**Etapa 1 — Solicitar dados**
Pedir lista em formato flexível (`:`, `-` ou `=` como separadores), uma entrada por linha:
```
VLoca - https://notebooklm.google.com/notebook/abc123/...
FiveCred: https://notebooklm.google.com/notebook/def456/...
```

**Etapa 2 — Processar linha por linha**

- Normalizar nome: lowercase, sem acentos, hífens (não underscore), só `a-z`, `0-9`, `-`
- Extrair ID: string após `/notebook/` até `/`, `?` ou fim da URL
- Validar pasta: verificar `clientes/<nome-normalizado>/` — se ausente, marcar como pulado
- Atualizar `CLAUDE.md`: substituir bloco `## NotebookLM` existente ou inserir novo após primeiro `# `

**Etapa 3 — Relatório final**

```
✓ Cadastrados (novos blocos)
↻ Atualizados (links modificados)
⊘ Pulados (pastas inexistentes)
✗ Erros (URLs malformadas, IDs inválidos)
```

## Bloco a inserir no CLAUDE.md

```markdown
## NotebookLM
- **Link:** [URL completa]
- **Notebook ID:** [ID extraído]
```

## Cenários especiais

- **Duplicatas:** processar última ocorrência da lista
- CLAUDE.md ausente: criar com título cliente + bloco NotebookLM
- Lista vazia: avisar e mostrar formato esperado
- Pasta inexistente: marcar como pulado, não criar
