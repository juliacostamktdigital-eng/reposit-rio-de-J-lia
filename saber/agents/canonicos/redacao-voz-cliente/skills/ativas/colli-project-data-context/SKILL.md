---
name: colli-project-data-context
description: "Monta contexto operacional de projeto usando MCPs Colli: BigQuery Calls, BigQuery WhatsApp Groups e Cockpit/Strapi. Use quando precisar entender um cliente/projeto antes de briefing, copy, diagnóstico, handoff ou priorização. Resolve project_document_id, ticker, grupo WhatsApp, status, fase, LT, health score, calls recentes e atividade de WhatsApp com segurança."
dependencies: []
outputs: ["project-data-context.md"]
estimated_time: "15-30min"
---

# Colli Project Data Context

Use esta skill para montar um contexto factual de projeto antes de escrever brief, copy, diagnóstico ou recomendação. Ela não substitui julgamento estratégico; ela reduz redescoberta e evita trabalhar com contexto solto.

## Fontes MCP esperadas

MCPs configurados no Codex:

- `n8n-bigquery-calls`
- `n8n-bigquery-whatsapp-groups`
- `cockpit`

Se as tools MCP não estiverem disponíveis no runtime, pare e informe que falta configurar MCP no `CODEX_HOME` do Paperclip. Não use token literal na resposta. Não invente dados.

## Regra de segurança

- Prefira dados agregados e metadados.
- Não abra transcrição ou texto de WhatsApp por padrão.
- Só use evidência textual quando a tarefa exigir prova concreta.
- Não exponha telefone, e-mail, nome de participante, mensagem privada ou transcrição longa no output final.
- Quando usar texto sensível, sintetize e cite apenas trechos curtos indispensáveis.

## Pegadinha dos MCPs n8n

As tools n8n exigem que vários campos "opcionais" sejam enviados como string vazia. Ao chamar uma tool, preencha todos os campos listados no contrato. Exemplo: se não filtrar `project_ticker`, envie `"project_ticker": ""`.

## Fluxo padrão

### 1. Resolver identidade do projeto

Use `localize_project` primeiro. Pode estar disponível tanto no MCP de calls quanto no MCP de WhatsApp.

Quando tiver ticker/nome:

```json
{
  "search_text": "TICKER ou nome",
  "project_document_id": "",
  "project_name": "",
  "integration_slug": "",
  "only_with_integrations": "",
  "limit": "5"
}
```

Quando quiser priorizar projetos com WhatsApp:

```json
{
  "search_text": "",
  "project_document_id": "",
  "project_name": "",
  "integration_slug": "whatsapp",
  "only_with_integrations": "true",
  "limit": "5"
}
```

Capture:

- `project_document_id`
- `calls_project_document_id`
- `project_ticker`
- `project_name`
- `statuses`
- `phase`
- `board`
- `project_start_date`
- `whatsapp_group_id`
- `whatsapp_group_ids_csv`
- `integrations_json`

Se houver múltiplos candidatos, não chute. Liste os candidatos e peça confirmação ou use contexto da issue para desambiguar.

### 2. Consultar Cockpit

Use `cockpit_get_project` quando tiver `project_document_id`:

```json
{
  "documentId": "PROJECT_DOCUMENT_ID",
  "populate": ""
}
```

Use `cockpit_project_health_score` para score atual:

```json
{
  "documentId": "PROJECT_DOCUMENT_ID"
}
```

Use `cockpit_query_history` quando a pergunta envolver evolução temporal:

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

Capture:

- status, categoria, board, fase
- `projectStartDate`, `lt`, `churnDate`, `concludedDate`
- `algorithm_flag`
- `algorithm_health_avg_score`
- indicadores relevantes do health score

### 3. Consultar calls

Comece por resumo, últimos 30 a 60 dias:

```json
{
  "mode": "summary",
  "output_format": "compact",
  "project_document_id": "PROJECT_DOCUMENT_ID",
  "project_ticker": "",
  "project_tickers_csv": "",
  "call_types_csv": "",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "search_text": "",
  "require_transcription": "",
  "require_url": "",
  "include_transcription_excerpt": "",
  "include_invitees": "",
  "limit": "10"
}
```

Depois use `by_type` para entender composição:

```json
{
  "mode": "by_type",
  "output_format": "compact",
  "project_document_id": "PROJECT_DOCUMENT_ID",
  "project_ticker": "",
  "project_tickers_csv": "",
  "call_types_csv": "",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "search_text": "",
  "require_transcription": "",
  "require_url": "",
  "include_transcription_excerpt": "",
  "include_invitees": "",
  "limit": "20"
}
```

Se precisar de reuniões específicas, use `details` sem transcrição primeiro:

```json
{
  "mode": "details",
  "output_format": "compact",
  "project_document_id": "PROJECT_DOCUMENT_ID",
  "project_ticker": "",
  "project_tickers_csv": "",
  "call_types_csv": "Kick Off,Checkin,Alinhamento,Reunião de vendas",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "search_text": "",
  "require_transcription": "",
  "require_url": "",
  "include_transcription_excerpt": "",
  "include_invitees": "",
  "limit": "10"
}
```

Só use `include_transcription_excerpt: "true"` quando precisar de evidência de voz, objeção, promessa ou alinhamento.

### 4. Consultar WhatsApp

Comece por resumo do grupo:

```json
{
  "mode": "summary",
  "id_group": "WHATSAPP_GROUP_ID",
  "client_documentid": "",
  "search_name": "",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "limit": "10"
}
```

Use atividade por dia para detectar picos/quedas:

```json
{
  "id_group": "WHATSAPP_GROUP_ID",
  "client_documentid": "",
  "search_name": "",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "limit": "60"
}
```

Não use `whatsapp_buscar_mensagens_queryon` com `include_text=true` para contexto geral. Para contexto geral, use resumo, status, volume e atividade.

## Output recomendado

Entregue um bloco compacto:

```markdown
## Contexto de Dados do Projeto

**Projeto:** ...
**IDs:** project_document_id=..., ticker=..., whatsapp_group_id=...
**Status operacional:** ...
**Cockpit:** flag=..., health=..., LT=..., fase=...
**Calls recentes:** ...
**WhatsApp:** ...
**Sinais relevantes:** ...
**Lacunas:** ...
**Fontes consultadas:** MCP/tool + filtros principais
```

## Quando parar

Pare e peça confirmação quando:

- `localize_project` retornar mais de um candidato plausível.
- não houver `project_document_id` e o ticker também estiver ausente.
- a pergunta exigir evidência textual sensível sem autorização clara.
- uma tool falhar por schema ou timeout depois de uma tentativa corrigida.
