---
name: gestao-ekyte-tags
description: Aplica etiquetas padronizadas em tarefas do Ekyte em lote respeitando o Playbook de Tags da Colli&Co. Resolve IDs, faz merge seguro com tags existentes (nunca sobrescreve), preview obrigatório, aplica em paralelo.
user-invocable: true
---

# /gestao-ekyte-tags — Aplicar tags em tarefas Ekyte

**Regra de ouro:** `update_task_tags` **SUBSTITUI** a lista inteira de tags da task. Por isso esta skill **sempre** lê as tags atuais e envia o conjunto completo (atuais + novas).

## Pré-requisitos

- MCP `ekyte-oficial` (`api.ekyte.com/mcp`) ativo — endpoint Streamable HTTP POST `/mcp` (não SSE); token de API no config; autentica a empresa Colli (companyId 3597)
- Parâmetros corretos: `taskId` é integer; `tags` é array de `{ctcTaskId: int, tagId: int}`
- IDs das tasks a taguear (fornecidos, ou skill lista por filtro via `list_tasks`)
- **Nunca** usar `list_tasks` sem filtro de projeto/workspace — dá timeout

## Dois modos

### Modo ROTINA

Toda tarefa de rotina recorrente leva **exatamente 2 tags**: tag da rotina + tag da semana do ano.

**Tags de rotina** (IDs fixos):

| Rotina | Tag | ID |
|---|---|---|
| Sprint Growth | `SPRINT GROWTH` | 250506 |
| Weekly Expansão | `WEEKLY EXPANSÃO` | 250507 |
| Alinhamento Comitê | `ALINHAMENTO COMITÊ` | 250508 |
| Quality Control | `QUALITY CONTROL` | 250509 |
| Ação Gerencial | `AÇÃO GERENCIAL` | 250510 |
| WAR | `WAR` | 250511 |

**Tag de semana:** formato `SEMANA NN` — maiúsculo, zero-padded (`SEMANA 01` … `SEMANA 52`).

### Modo TIPO (entregável)

| Gatilho | Tag | ID |
|---|---|---|
| sigla `[LP]` | `LANDING PAGE` | 90834 |
| sigla `[CA]` | `Criativo Ads` | 79390 |
| criativo em vídeo | `criativo em vídeo` | 228775 |

## Fluxo para cada task

1. **Resolver IDs** das tags-alvo (usar cache acima)
2. **Ler tags atuais:** `get_detailed_task(taskId)` → extrair lista existente
3. **Merge:** `conjunto_final = tags_atuais ∪ tags_novas` (dedupe por ID)
4. **Preview obrigatório** — aguardar "ok"
5. **Aplicar:** `update_task_tags(taskId, tags)` em paralelo
6. **Relatório:** ✅ aplicadas / ⏭️ já tinham / ❌ falhas

## Guardrails

1. **Nunca aplicar sem merge** — sempre `get_detailed_task` antes
2. **Preview sempre**, mesmo em lote
3. **Tag inexistente = parar e reportar** (não criar tag nova)
4. **Modo ROTINA = exatamente 2 tags** (rotina + semana)
5. **Idempotência:** rodar 2× não duplica nem apaga
