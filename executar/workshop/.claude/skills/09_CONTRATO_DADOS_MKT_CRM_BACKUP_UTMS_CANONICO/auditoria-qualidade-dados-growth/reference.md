# Referência Da Auditoria De Qualidade De Dados Growth

Fonte normativa: `assets/canonicos/09_CONTRATO_DADOS_MKT_CRM_BACKUP_UTMS_CANONICO.md`.

## Princípio

Não existe análise N3 confiável se a base não preserva origem, IDs, match CRM e qualidade comercial. Antes de otimizar mídia ou criativo, a operação deve saber se os dados sustentam a conclusão.

## Métricas

### `unknown_source_rate`

Percentual de leads sem origem útil.

Sinais:

- `source` vazio;
- `source` como `unknown`;
- ausência de `utm_source`;
- conversões sem first/last-touch.

### `crm_match_rate`

Percentual de leads do backup com match no CRM.

Sinais válidos:

- `match_confidence` como `high` ou `medium`;
- `crm_contact_id` preenchido;
- `crm_deal_id` preenchido.

### `creative_id_fill_rate`

Percentual de leads com `creative_id` ou `v4_creative_id` preenchido.

### `mql_feedback_rate`

Percentual de MQLs com feedback comercial útil.

Feedback útil inclui:

- `feedback_quality`;
- `feedback_notes`;
- `disqualification_reason`;
- `lost_reason`.

### `lead_id_duplicate_rate`

Percentual de registros duplicados por `lead_id`.

## Decisão De Confiabilidade

### Confiável

- origem desconhecida menor que 10%;
- match CRM maior que 90%;
- creative ID maior que 95%;
- feedback MQL maior que 80%;
- duplicidade baixa.

### Confiável Com Ressalvas

Use quando há alertas moderados, mas a análise ainda pode ser feita com limites declarados.

### Não Confiável

Use quando a base não sustenta leitura por campanha, criativo, MQL/SQL ou feedback comercial.

## Plano Corretivo

Cada gap deve ter:

- fonte;
- impacto;
- severidade;
- dono;
- ação;
- prazo;
- critério de aceite.
