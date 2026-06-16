---
name: ekyte-refresh
description: Atualiza o cache local da skill ekyte-task — re-busca workspaces fixos, projetos do trimestre vigente para cada cliente, tipos de tarefa do workflow "Padrão Colli&Co (Oficial)", e regenera o cache de fluxos (fases por tipo) via MCP oficial. Use quando a Julia rodar /ekyte-refresh, disser que entrou cliente novo, projeto novo, que mudou fluxo/fase de algum tipo, ou que o cache parece desatualizado.
user-invocable: true
---

# /ekyte-refresh — Atualizar cache do ekyte

Re-popula `clientes/_skill-ekyte/cache.md` puxando dados frescos da MCP `ekyte`. Roda em <2 minutos.

## Quando usar

- `/ekyte-refresh` (invocação direta)
- "atualiza o cache do ekyte"
- "entrou cliente novo, atualiza"
- "projeto Q3/2026 começou, atualiza"
- Cache com mais de 30 dias

## Pré-requisitos

- MCP `ekyte` configurada
- Arquivo `clientes/_skill-ekyte/cache.md` existente

## Fluxo

### 1) Confirmar trimestre vigente

Calcular trimestre atual com base na data de hoje:
- Jan/Fev/Mar → Q1
- Abr/Mai/Jun → Q2
- Jul/Ago/Set → Q3
- Out/Nov/Dez → Q4

Mostrar: "Vou atualizar o cache pro **Q2/2026**. Confirma?"

### 2) Workspaces

Os workspaces fixos não mudam (já estão hardcoded no cache). Pular esta etapa, a menos que a Julia mencione cliente novo. Nesse caso:
- Perguntar nome do cliente novo
- Chamar `ekyte.listar_workspaces_tool({"name_list_workspaces": "<nome>", "squad_id_list_workspaces": "", "situation_id_list_workspaces": "1"})`
- Confirmar qual é o ID certo (pode vir múltiplos)
- Adicionar ao cache

### 3) Projetos do trimestre vigente para cada workspace

Para cada workspace no cache:
- Chamar `ekyte.listar_projetos_tool` com:
  - `workspace_id_list_projects`: ID do workspace
  - `created_from_list_projects`: data 90 dias antes do início do trimestre (margem)
  - `created_to_list_projects`: data de hoje
- Filtrar projetos cujo nome contém `Q2/2026` (ou trimestre vigente)
- Salvar `project_id` no cache

Se um workspace não tiver projeto do trimestre: avisar ("VLoca não tem projeto Q2/2026 — quer que eu pule ou tem nome diferente?")

### 4) Tipos de tarefa

Chamar `ekyte.listar_tipos_de_tarefas_tool({"name_type_task": "", "parameters1_Value": "3535"})` (workflow Padrão Colli&Co Oficial).

Filtrar tipos cujo nome casa o regex `^\[\d+\]\[([A-Z]+)\]`.

Atualizar a tabela do cache com qualquer tipo novo. **Não remover** entradas existentes.

### 4.5) Fluxos por tipo (regenerar `flows.md`)

Regenera `clientes/_skill-ekyte/flows.md` — as fases reais de cada tipo (com `phaseId`) + dicionário `nome da fase → phaseId`.

Se o script Python estiver disponível:
```bash
python ".claude/skills/ekyte-refresh/scripts/fetch_flows.py"
```

Precisa do MCP `ekyte-oficial` configurado. Se faltar, pular esta etapa.

### 5) Salvar e reportar

Atualizar `clientes/_skill-ekyte/cache.md`:
- Atualizar campo "Última atualização total" no topo
- Reescrever as seções que mudaram

Reportar:
```
✅ Cache atualizado:
  - <N> workspaces
  - <N> projetos Q2/2026 descobertos
  - <M> tipos de tarefa (<+X> novos)
  - flows.md regenerado (<T> tipos, <P> fases distintas)
```

## O que NÃO fazer

- Não rodar refresh sem confirmação do trimestre.
- Não criar workspaces, projetos ou tipos. Skill é read-only no ekyte.
- Não apagar entradas do cache automaticamente.
