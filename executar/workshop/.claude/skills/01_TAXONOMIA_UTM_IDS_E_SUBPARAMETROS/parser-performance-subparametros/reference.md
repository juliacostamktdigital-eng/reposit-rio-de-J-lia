# Referência Do Parser De Subparâmetros

Fonte normativa: `assets/canonicos/01_TAXONOMIA_UTM_IDS_E_SUBPARAMETROS.md`.

## Objetivo

Converter UTMs e parâmetros `v4_*` em dimensões analíticas para responder:

- qual campanha trouxe mais MQLs;
- qual criativo trouxe MQLs mais baratos;
- qual hook trouxe SQLs;
- qual formato trouxe lead ruim;
- qual persona avança mais;
- qual dor gera conversa comercial melhor;
- qual canal gera lead barato, mas sem fit;
- qual percentual de leads está sem origem ou sem match.

## Prioridade De Extração

Quando houver campos duplicados, use esta ordem:

1. Campos próprios `v4_*`.
2. IDs no início de `utm_campaign`, `utm_content`, `utm_term`.
3. Nomes visíveis da plataforma.
4. Campos manuais do CRM/planilha.

Se houver divergência entre `v4_*` e UTM, marque flag. Não escolha silenciosamente sem registrar.

## Campos De Entrada Esperados

UTMs:

- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_content`
- `utm_term`

IDs:

- `v4_client_id`
- `v4_campaign_id`
- `v4_adgroup_id`
- `v4_creative_id`
- `v4_test_id`

Comerciais:

- `lead_status`
- `mql_status`
- `sql_status`
- `opportunity_status`
- `deal_status`
- `disqualification_reason`
- `sales_owner`
- `first_contact_at`
- `speed_to_lead_minutes`
- `feedback_quality`
- `deal_value`

Mídia:

- `spend`
- `impressions`
- `clicks`
- `leads`
- `cpl`
- `campaign_name`
- `adgroup_name`
- `creative_name`

## Parsing De `utm_campaign`

Formato:

```text
{campaign_id}__typ-{tipo_campanha}__obj-{objetivo}__mov-{movimento}__slug-{slug}__coh-{cohort}__seg-{segmento}__per-{periodo}
```

Campos derivados:

- `campaign_id`
- `tipo_campanha`
- `objetivo`
- `movimento`
- `campaign_slug`
- `cohort`
- `segmento`
- `periodo`

## Parsing De `utm_content`

Formato:

```text
{creative_id}__fmt-{formato}__hook-{hook}__per-{persona}__slug-{slug}__dor-{dor}__ang-{angulo}__stage-{etapa}__ver-{versao}
```

Campos derivados:

- `creative_id`
- `formato`
- `hook`
- `persona`
- `creative_slug`
- `dor`
- `angulo`
- `etapa_funil`
- `versao`

## Parsing De `utm_term`

Social:

```text
{adgroup_id}__pub-{publico}__temp-{temperatura}__pos-{posicionamento}__slug-{slug}__plc-{placement}__geo-{geo}
```

Search:

```text
{adgroup_id}__kw-{keyword_slug}__match-{tipo_match}__temp-{temperatura}__slug-{slug}__geo-{geo}
```

Campos derivados:

- `adgroup_id`
- `publico`
- `keyword`
- `match_type`
- `temperatura`
- `posicionamento`
- `adgroup_slug`
- `placement`
- `geo`

## Flags De Qualidade

Crie flags booleanas ou valores `ok/erro` para:

- `missing_campaign_id`
- `missing_adgroup_id`
- `missing_creative_id`
- `missing_test_id`
- `malformed_utm_campaign`
- `malformed_utm_content`
- `malformed_utm_term`
- `v4_campaign_mismatch`
- `v4_adgroup_mismatch`
- `v4_creative_mismatch`
- `unknown_source`
- `missing_commercial_feedback`

## Métricas De Qualidade

Calcule quando possível:

- `unknown_source_rate`
- `creative_id_fill_rate`
- `campaign_id_fill_rate`
- `crm_feedback_rate`
- `utm_malformed_rate`
- `v4_mismatch_rate`

## Regras De Interpretação

- Se `creative_id` está ausente, não conclua performance por criativo.
- Se `campaign_id` diverge entre `v4_campaign_id` e `utm_campaign`, marque risco de match.
- Se `utm_content` está malformada, não agrupe por hook/dor/persona sem revisão.
- Se feedback comercial falta, sinalize que leitura é mídia/conversão, não qualidade.
- Se first-touch e last-touch estiverem misturados, declare qual campo foi usado.

## Saída Analytics Ready

Grão ideal para leadgen:

```text
1 linha por lead_id
```

Campos recomendados:

- IDs: `lead_id`, `client_id`, `campaign_id`, `adgroup_id`, `creative_id`, `test_id`.
- Origem: `source`, `medium`.
- Campanha: `cohort`, `segmento`, `tipo_campanha`, `movimento`, `periodo`.
- Público: `publico`, `temperatura`, `posicionamento`, `keyword`, `match_type`.
- Criativo: `formato`, `persona`, `hook`, `creative_slug`, `dor`, `angulo`, `etapa_funil`, `versao`.
- Funil: `lead_status`, `is_mql`, `is_sql`, `is_opportunity`, `is_won`.
- Comercial: `deal_value`, `disqualification_reason`, `feedback_quality`, `speed_to_lead_minutes`.
- Qualidade: flags de missing/malformed/mismatch.
