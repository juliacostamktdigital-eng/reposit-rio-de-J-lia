---
name: colli-voice-of-customer-mcp
description: "Extrai voz do cliente, dores, objeções, claims e linguagem real usando MCPs Colli de Calls e WhatsApp. Use para copy, guia de voz, revisão de mensagem, proposta de valor, LP, anúncios, e-mails, scripts e narrativas. Prioriza evidência mínima, proteção de PII e síntese acionável."
dependencies:
  - colli-project-data-context
outputs: ["voice-of-customer.md"]
estimated_time: "20-45min"
---

# Colli Voice of Customer MCP

Use esta skill quando a tarefa exigir voz real do cliente para copy, narrativa, guia de redação, anúncio, landing page, proposta comercial ou revisão de mensagem. O objetivo é capturar linguagem, tensão, objeções e evidências sem despejar dados sensíveis.

## Fontes MCP esperadas

- `n8n-bigquery-calls`
- `n8n-bigquery-whatsapp-groups`
- opcional: `cockpit`, para status/risco/contexto operacional

Se as tools MCP não estiverem disponíveis, informe que falta configurar MCP no `CODEX_HOME` do Paperclip. Não use tokens literais nem faça improviso com credenciais.

## Princípios

- Voz do cliente não é transcrição bruta. É síntese de padrões com evidências mínimas.
- Texto sensível só entra quando melhora a decisão de copy.
- Não inclua telefone, e-mail, ID pessoal, nome de remetente, URL privada ou transcrição longa no output.
- Diferencie fato observado, inferência e recomendação.
- Nunca transforme reclamação isolada em promessa comercial.

## Pegadinha dos MCPs n8n

Ao chamar tools n8n, envie campos não usados como `""`. O schema pode exigir campos que parecem opcionais.

## Fluxo padrão

### 1. Comece pelo contexto do projeto

Se ainda não houver `project_document_id`, `project_ticker` e `whatsapp_group_id`, use a skill `colli-project-data-context` primeiro.

Dados mínimos:

- `project_document_id`
- `project_ticker`
- `project_name`
- `whatsapp_group_id`, se existir
- objetivo da peça de copy
- público alvo ou segmento

### 2. Buscar calls com valor de voz

Prefira estes tipos:

- `Kick Off`
- `Reunião de vendas`
- `Reuniao de vendas`
- `Checkin`
- `Alinhamento`
- `Acompanhamento Comercial`
- `Estruturacao Estrategica`

Primeiro liste detalhes sem transcrição:

```json
{
  "mode": "details",
  "output_format": "compact",
  "project_document_id": "PROJECT_DOCUMENT_ID",
  "project_ticker": "",
  "project_tickers_csv": "",
  "call_types_csv": "Kick Off,Reunião de vendas,Reuniao de vendas,Checkin,Alinhamento,Acompanhamento Comercial,Estruturacao Estrategica",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "search_text": "",
  "require_transcription": "true",
  "require_url": "",
  "include_transcription_excerpt": "",
  "include_invitees": "",
  "limit": "10"
}
```

Depois abra trechos só das calls mais relevantes:

```json
{
  "mode": "details",
  "output_format": "evidence",
  "project_document_id": "PROJECT_DOCUMENT_ID",
  "project_ticker": "",
  "project_tickers_csv": "",
  "call_types_csv": "Kick Off,Reunião de vendas,Reuniao de vendas,Checkin,Alinhamento,Acompanhamento Comercial,Estruturacao Estrategica",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "search_text": "dor OU objeção OU meta OU problema específico",
  "require_transcription": "true",
  "require_url": "",
  "include_transcription_excerpt": "true",
  "include_invitees": "",
  "limit": "5"
}
```

Procure:

- palavras usadas pelo cliente para descrever o problema
- antes/depois desejado
- objeções de compra
- concorrentes ou alternativas citadas
- métricas, metas e prazos
- medos, frustrações e riscos percebidos
- frases que podem virar headline, subheadline, bullets ou prova

### 3. Buscar WhatsApp com cuidado

Comece pelo agregado:

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

Para picos de atividade:

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

Só busque mensagens com texto quando houver uma hipótese clara:

```json
{
  "id_group": "WHATSAPP_GROUP_ID",
  "client_documentid": "",
  "search_name": "",
  "search_text": "termo de dor, objeção, entrega ou resultado",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "include_text": "true",
  "include_sender_name": "",
  "limit": "10"
}
```

Use `include_sender_name: "true"` apenas se a identidade funcional do interlocutor for essencial. Em geral, não é.

### 4. Separar evidências por função de copy

Classifique achados em:

- **Linguagem literal:** termos recorrentes e frases curtas.
- **Dores:** problemas que o cliente sente ou verbaliza.
- **Objeções:** motivos para não comprar, não aprovar ou hesitar.
- **Desejos:** resultado desejado em linguagem do cliente.
- **Provas:** números, fatos, eventos, entregas ou comparação antes/depois.
- **Promessas seguras:** claims sustentáveis pelas fontes.
- **Riscos de promessa:** claims que parecem fortes, mas não têm evidência suficiente.
- **Tom:** formal, direto, técnico, ansioso, pragmático, aspiracional etc.

## Output recomendado

```markdown
## Voice of Customer

**Projeto:** ...
**Objetivo de copy:** ...
**Período analisado:** ...

### Linguagem do cliente
- ...

### Dores e tensões
- ...

### Objeções
- ...

### Claims seguros
- ...

### Claims proibidos ou frágeis
- ...

### Frases úteis para copy
- "..." — uso sugerido: headline/bullet/CTA

### Tom recomendado
...

### Implicações para a peça
...

### Fontes consultadas
- MCP/tool + filtros principais, sem tokens
```

## Regras para copy final

- Não use aspas diretas se o trecho contiver PII ou contexto privado.
- Não cite nomes de pessoas.
- Não use uma frase isolada como verdade universal.
- Se a evidência vem de WhatsApp, trate como sinal qualitativo, não prova estatística.
- Se a evidência vem de transcrição, valide se é cliente, time Colli ou terceiro falando antes de atribuir voz ao cliente.

## Quando escalar

Recomende envolver `briefador` quando faltar objetivo, público ou contexto operacional. Recomende envolver `estrategista-posicionamento` quando houver conflito de promessa, segmento ou diferenciação. Recomende envolver `editor-entregaveis` quando o output precisar virar deck/documento final.
