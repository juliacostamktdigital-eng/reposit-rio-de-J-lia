# Referência Do Setup Backup Leads UTMs

Fonte normativa: `assets/canonicos/09_CONTRATO_DADOS_MKT_CRM_BACKUP_UTMS_CANONICO.md`.

## Princípio

Todo cliente deve ter uma planilha backup padronizada. Ela não substitui o CRM; ela protege a operação contra perda de UTMs, falha de integração, mudança de campos do cliente e divergência entre mídia e CRM.

## Nome Da Planilha

```text
backup_leads_{client_id}_{ano_mes}
```

Exemplo:

```text
backup_leads_cli-hs-prevent_2026-05
```

## Abas

### 00_README

Contexto operacional:

- cliente;
- período;
- dono;
- origem dos dados;
- link da LP;
- link CRM;
- link plano de mídia;
- link taxonomia UTM;
- data da última atualização;
- observações de qualidade.

### 01_RAW_LEADS

Registro bruto de todo lead capturado.

Colunas mínimas:

- `raw_row_id`;
- `captured_at`;
- `source_form`;
- `landing_page_url`;
- `conversion_url`;
- `thank_you_url`;
- `ip_hash`;
- `user_agent`;
- `name`;
- `email`;
- `phone`;
- `company`;
- `role`;
- `segment`;
- `message`;
- `consent_lgpd`;
- `raw_payload`.

### 02_ATTRIBUTION

Origem e IDs.

Colunas mínimas:

- `lead_id`;
- `raw_row_id`;
- `client_id`;
- `first_utm_source`;
- `first_utm_medium`;
- `first_utm_campaign`;
- `first_utm_content`;
- `first_utm_term`;
- `first_landing_page_url`;
- `first_seen_at`;
- `last_utm_source`;
- `last_utm_medium`;
- `last_utm_campaign`;
- `last_utm_content`;
- `last_utm_term`;
- `last_landing_page_url`;
- `last_seen_at`;
- `v4_campaign_id`;
- `v4_adgroup_id`;
- `v4_creative_id`;
- `v4_test_id`.

### 03_PARSED_PARAMS

Campos já quebrados para análise: campanha, conjunto, criativo, formato, persona, hook, dor, ângulo, stage, versão, placement, geo, keyword e match type.

### 04_CRM_MATCH

Resultado do cruzamento com CRM.

Valores permitidos para `match_method`:

- `lead_id`;
- `email`;
- `phone`;
- `email_phone`;
- `crm_native`;
- `manual`;
- `no_match`.

Valores permitidos para `match_confidence`:

- `high`;
- `medium`;
- `low`;
- `none`.

### 05_MEDIA_EXPORT

Export da plataforma de mídia por data, origem, campanha, conjunto, criativo, investimento, impressões, cliques e conversões.

### 06_ANALYTICS_READY

Grão recomendado: 1 linha por `lead_id`.

Campos essenciais:

- origem;
- IDs;
- atributos parseados;
- status de funil;
- flags `is_mql`, `is_sql`, `is_opportunity`, `is_won`;
- `deal_value`;
- `feedback_quality`;
- `speed_to_lead_minutes`.

### 07_PIVOTS

Visões recomendadas:

- leads por campanha;
- MQL por campanha;
- MQL por criativo;
- MQL por formato;
- MQL por hook;
- SQL por criativo;
- vendas por campanha;
- taxa de fonte desconhecida;
- leads sem match CRM;
- leads sem atendimento.

## Critério N2

- planilha backup padronizada;
- UTMs chegam na conversão;
- IDs chegam na planilha;
- CRM recebe origem ou existe match confiável;
- first-touch e last-touch são preservados;
- dicionário de dados existe;
- teste ponta a ponta existe;
- análise pós-campanha é possível.
