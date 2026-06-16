---
name: gestao-ekyte-rename-tasks
description: Renomeia títulos de múltiplas tarefas Ekyte em lote via find-replace. Ideal para operações repetitivas como trocar sigla [WEB] → [P&P] em 3+ tasks.
user-invocable: true
---

# /gestao-ekyte-rename-tasks — Renomear tasks Ekyte em lote

## Quando usar

✅ 3+ tasks para renomear
✅ Operações find-replace repetitivas em lote
❌ 1-2 tasks (mais rápido na UI)
❌ Edições complexas (responsáveis, prazos, fases)

## Arquitetura de MCPs

| Servidor | Função |
|---|---|
| `ekyte-oficial` | **Escrita** — `update_task`, responsáveis, fases, comentários |
| `ekyte` (n8n) | **Leitura** — insights, performance, BI |

Caminho primário: `mcp__ekyte-oficial__update_task`. PATCH REST como fallback.

## Modos de uso

**Opção 1 — IDs explícitos:**
```
Renomeia tasks (IDs: 9342321, 9342322):
- Substitui: [WEB] → [P&P]
```

**Opção 2 — Filtro por projeto/workspace:**
```
No projeto "Sprint Junho 26 VLoca", renomeia:
- Substitui: [CA] → [KV]
```

## Operações suportadas

- Find-replace simples: `[WEB]` → `[P&P]`
- Múltiplas substituições sequenciais
- Case-sensitive
- Exemplos: remover prefixo, alterar [NN], expandir nomes curtos

## Output

Relatório com contagem de sucessos/falhas, IDs processados e motivos de erro.

## Pré-requisitos

- **Primário:** MCP `ekyte-oficial` ativo
- **Fallback:** Token Ekyte em `clientes/_skill-ekyte/.env`
  - Obtido via F12 no navegador, filtrando requisições `api.ekyte` e copiando JWT do header `Authorization`

## Limitações

- Sem validação prévia de títulos
- Sem undo automático
- Sem garantia de idempotência em execuções repetidas
