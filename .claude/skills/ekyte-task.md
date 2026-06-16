---
name: ekyte-task
description: Cria tarefas no Ekyte com briefing estruturado seguindo o padrão Colli&Co. Disparar quando Julia solicitar "criar/subir/abrir tarefa(s) no ekyte", fornecer demanda em texto livre ou apontar aba de planilha de demandas para subida em lote.
user-invocable: true
---

# /ekyte-task — Criar tarefas no Ekyte com briefing

Automatiza a criação de tarefas no Ekyte com briefing completo, preview obrigatório e ativação automática.

## Quando ativar

- "cria task no ekyte / sobe task / abre tarefa"
- Demanda em texto livre ("5 criativos ads pro VLoca")
- Planilha de demandas apontada para subida em lote
- `/ekyte-task` explícito

**Não usar** para consultas simples de dados — MCP base cobre direto.

## Estrutura de título

```
[NN][SIGLA][IA] TICKER | Demanda específica
```
- `NN` = quantidade em 2 dígitos (01, 09, 15)
- `SIGLA` = sigla do tipo (CA, LP, KV, PC…)
- `[IA]` = sempre; marca geração via skill
- `TICKER` = sigla CRM do cliente (FCE, ACCE, MSZB, TAWV, TECN1, FARS, SOTB)
- Demanda = parte livre e descritiva

**Exemplo:** `[09][CA][IA] ACCE | Remarketing produto X`

## Fluxo (10 passos obrigatórios)

**1. Pre-fly check** (lotes ≥3): varrer pendências, propor defaults, consolidar em 1 resposta

**2. Carregar contexto**: `cache.md`, `sla.md`, `flows.md` de `clientes/_skill-ekyte/`

**3. Identificar modo**: texto livre (Modo A) ou planilha (Modo B)

**4. Resolver workspace/projeto**: consultar cache ou MCP; bloquear workspace desconhecido sem confirmação explícita da Julia

**5. Resolver tipo/sigla**: mapear para `task_type_id`; desambiguar se múltiplos matches

**6. Chamar /ekyte-briefing**: delegar montagem da description; injeta síntese NotebookLM obrigatoriamente

**7. Calcular prazo**: SLA da tabela + sobrescrever se Julia especificar

**8. Preview obrigatório**: mostrar workspace, projeto, tipo, título, resumo de briefing, responsáveis por etapa

**9. Criar e ativar via MCP**:
- Chamar `ekyte_create_task`
- Após criação, disparar `generate-tasks` para sair de "Não planejada" → "Ativa"
- Aplicar responsáveis por etapa se pedido

**10. Atualizar cache + tags**: registrar IDs novos; aplicar tags `SPRINT GROWTH` (250506) + `SEMANA NN` + `IA` via merge

## Workspaces fixos (não criar fora sem confirmação)

| Cliente | Ticker | workspace_id |
|---|---|---|
| FiveCred | FCE | 123901 |
| VLoca (Accenture Participações) | ACCE | 118531 |
| Fares | FARS | 133704 |
| Atlantica Maquinas (SOTB) | SOTB | 54255 |
| Massimo Zanetti | MSZB | a confirmar |
| Tawá Veículos | TAWV | a confirmar |
| Tecnipool | TECN1 | a confirmar |

## Ativação: generate-tasks

Após criar task (fica "Não planejada"), disparar:
```
POST /api/v2/companies/{company_id}/projects/{project_id}/generate-tasks
Body: []   ← array vazio, NUNCA objeto
```
- HTTP 500 com body vazio = falso erro quando não há "Não planejada" restante
- HTTP 401 = token expirou; renovar via F12 no navegador

## Tags finais (sempre merge, nunca substituição)

- `SPRINT GROWTH` → tagId: 250506
- `SEMANA NN` → semana ISO vigente (zero-padded)
- `IA` em vermelho → tagId específico do cache

## Briefing: delegado à /ekyte-briefing

A `/ekyte-task` **não** monta o texto de briefing. Sempre invocar `/ekyte-briefing`, que:
- Carrega template da sigla de `clientes/_skill-ekyte/briefing-templates/`
- Consulta NotebookLM do cliente via `/cs-notebooklm-consulta-cliente`
- Devolve `briefing_ekyte_text` (texto plano formatado — sem HTML)

**Regra crítica:** sem NotebookLM cadastrado = parar antes do preview e pedir autorização explícita.

## Guardrails não-negociáveis

1. **Preview obrigatório** antes de cada criação
2. **Workspace desconhecido** = PARAR + pedir confirmação explícita
3. **Erro = parar**; não continuar lote sem aprovação
4. **NotebookLM obrigatório** em projeto novo (salvo autorização)
5. **Task nunca atrasada** ao encerrar; validar "Executar etapa até"
6. **Sem auto-inventar IDs** — tudo vem de cache ou MCP
7. **Merge de tags**, não substituição

## Modo planilha (Modo B)

- Ler URL com WebFetch; extrair colunas: sequencial, título, datas, task_type_id, email executor, descrição, Qtd Peças, Tags, Fase
- Cada linha = 1 task; pre-fly confirmar quantificação [NN] por linha
- Reusar síntese NotebookLM em 4+ tasks do mesmo cliente

## Esteira completa recomendada

```
/novo-cliente → /account-handoff → /account-pesquisa-profunda-cliente
→ /contexto → /outra-notebooklm-cadastrar → /ekyte-refresh
→ /ekyte-briefing-refresh → /ekyte-task
   → /ekyte-briefing → /cs-notebooklm-consulta-cliente
   → preview → criar → ativar → tags
```
