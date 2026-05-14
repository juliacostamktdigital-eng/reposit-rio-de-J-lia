---
name: colli-executive-cockpit-context
description: "Consulta contexto executivo do Cockpit/Strapi via MCP: health score, flag, status, fase, LT, datas, histórico e snapshot de projetos. Use para priorização, decisão de CEO, briefing executivo, risco de conta, contexto antes de delegar tarefas e leitura de carteira."
dependencies: []
outputs: ["executive-cockpit-context.md"]
estimated_time: "10-25min"
---

# Colli Executive Cockpit Context

Use esta skill para obter contexto executivo e operacional do Cockpit antes de decidir prioridade, delegação, risco ou narrativa. Ela é especialmente útil para CEO, Briefador e Redação quando precisam entender saúde do cliente e estágio do projeto.

## Fonte MCP esperada

- `cockpit`

Se a tool MCP não estiver disponível, informe que falta configurar o MCP Cockpit no `CODEX_HOME` do Paperclip. Não use token literal nem faça chamadas manuais com credencial na conversa.

## O que buscar

- status do projeto
- categoria, produto, board e fase
- início do projeto, LT, churn/conclusão se houver
- flag do cliente (`Safe`, `Care`, `Critical`, `Danger`)
- health score atual e histórico
- indicadores ativos relevantes
- coordenador/squad quando necessário

## Fluxo padrão por projeto

### 1. Obter cadastro do projeto

Quando tiver `project_document_id`:

```json
{
  "documentId": "PROJECT_DOCUMENT_ID",
  "populate": ""
}
```

Capture:

- `name`
- `ticker`
- `statuses`
- `category`
- `product`
- `board`
- `phase`
- `projectStartDate`
- `lt`
- `churnDate`
- `concludedDate`

### 2. Obter health score atual

```json
{
  "documentId": "PROJECT_DOCUMENT_ID"
}
```

Capture:

- score atual
- flag
- indicadores críticos
- campos manuais relevantes
- lacunas de dado

### 3. Obter histórico quando houver pergunta temporal

Use para perguntas como "piorou?", "está em risco há quanto tempo?", "qual tendência?".

```json
{
  "startDate": "YYYY-MM-DD",
  "endDate": "YYYY-MM-DD",
  "columns": ["algorithm_health_avg_score", "algorithm_flag"],
  "timezone": "America/Sao_Paulo",
  "granularity": "weekly",
  "projectDocumentIds": ["PROJECT_DOCUMENT_ID"],
  "filterByStatus": "",
  "filterByCategory": "",
  "filterBySquad": "",
  "filterByUser": "",
  "filter": null,
  "page": 1,
  "pageSize": 50,
  "includeMetricTimestamps": false,
  "parseTypes": true
}
```

### 4. Buscar carteira ou comparativos

Use `cockpit_query_table` para listas de projetos por status, squad, categoria ou faixa de health score.

Exemplo: projetos em danger:

```json
{
  "page": 1,
  "pageSize": 50,
  "sortBy": "name",
  "sortOrder": "asc",
  "search": "",
  "healthScoreBand": "",
  "filterByUser": "",
  "filterByCategory": "",
  "filterByStatus": "active",
  "filterBySquad": "",
  "filters": [
    {
      "column": "algorithm_flag",
      "operator": "eq",
      "value": "Danger"
    }
  ],
  "fetchAllPages": false,
  "maxPages": 3,
  "applyColumnFiltersOnClient": true,
  "validateFilterColumns": true
}
```

Exemplo: faixa de health score:

```json
{
  "page": 1,
  "pageSize": 100,
  "sortBy": "name",
  "sortOrder": "asc",
  "search": "",
  "healthScoreBand": "danger",
  "filterByUser": "",
  "filterByCategory": "",
  "filterByStatus": "active",
  "filterBySquad": "",
  "filters": [],
  "fetchAllPages": true,
  "maxPages": 10,
  "applyColumnFiltersOnClient": true,
  "validateFilterColumns": true
}
```

## Cuidados de carga

- Não combine `fetchAllPages` com filtros pesados na API se não precisar.
- Para filtros de coluna que causam timeout/500, use `applyColumnFiltersOnClient: true`.
- Com `fetchAllPages`, use `sortBy` apenas `name` ou `createdAt`.
- Não ordene por métrica em busca ampla.
- Mantenha `pageSize` razoável.

## Interpretação executiva

Classifique o contexto em:

- **Estado:** ativo, finalizado, churned, onboarding, ongoing etc.
- **Risco:** seguro, atenção, crítico, danger.
- **Tendência:** melhorando, estável, piorando, inconclusiva.
- **Causa provável:** separar dado observado de hipótese.
- **Ação recomendada:** briefing, investigação, contato, revisão de promessa, handoff, pausa.

Não confunda health score com verdade final. Trate como sinal operacional que precisa ser combinado com calls, WhatsApp e contexto da issue.

## Output recomendado

```markdown
## Contexto Executivo Cockpit

**Projeto:** ...
**Status/Fase:** ...
**LT e datas:** ...
**Health/Flag:** ...
**Tendência:** ...
**Sinais críticos:** ...
**Leitura executiva:** ...
**Implicação para a tarefa:** ...
**Fontes consultadas:** MCP/tool + filtros principais
```

## Quando usar junto com outras skills

- Use `colli-project-data-context` quando precisar juntar Cockpit com Calls e WhatsApp.
- Use `colli-voice-of-customer-mcp` quando o contexto executivo precisar virar copy, guia de voz ou mensagem.
- Use esta skill isolada quando a pergunta for de priorização, saúde de carteira, risco ou decisão de delegação.
