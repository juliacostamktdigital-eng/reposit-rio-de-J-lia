# Checklist QA Tracking UTM CRM

## 1. Contexto Do Teste

- Cliente:
- Data:
- Responsável:
- Canal:
- Campanha:
- URL testada:
- Lead teste (email): `qa+<timestamp>@<dominio>.com`
- Flag `is_test` no payload: ( ) sim ( ) não
- Exclusão em audiences/dashboards configurada antes do teste: ( ) sim ( ) não
- Decisão: `go` / `go-com-risco` / `no-go` / `retestar`

## 2. URL E Parâmetros Esperados

| Campo | Valor esperado | Encontrado na URL? |
| --- | --- | --- |
| `utm_source` |  |  |
| `utm_medium` |  |  |
| `utm_campaign` |  |  |
| `utm_content` |  |  |
| `utm_term` |  |  |
| `v4_client_id` |  |  |
| `v4_campaign_id` |  |  |
| `v4_adgroup_id` |  |  |
| `v4_creative_id` |  |  |
| `v4_test_id` |  |  |

### 2.1 Click IDs Esperados (por canal)

| Click ID | Aplicável ao canal? | Valor esperado | Encontrado na URL? |
| --- | --- | --- | --- |
| `gclid` (Google web/cookies) |  |  |  |
| `gbraid` (Google iOS app) |  |  |  |
| `wbraid` (Google iOS web) |  |  |  |
| `fbclid` (Meta) |  |  |  |
| `_fbp` (Meta cookie) |  |  |  |
| `_fbc` (Meta cookie derivado) |  |  |  |
| `ttclid` (TikTok) |  |  |  |
| `li_fat_id` (LinkedIn) |  |  |  |
| `msclkid` (Bing) |  |  |  |

## 3. Validação Por Salto (5 Saltos)

### 3.1 Salto 1 → 2: URL → LP (browser/cookie/dataLayer)

| Verificação | Status | Evidência |
| --- | --- | --- |
| LP carrega sem perder query string |  |  |
| Sem redirect 302 que descarta UTMs |  |  |
| dataLayer recebe UTMs e click IDs antes de render |  |  |
| Cookies de first-touch escritos no primeiro pageview |  |  |

### 3.2 Salto 2 → 3: LP → Form / WhatsApp / ponto de conversão

| Campo | Capturado em campo oculto? | Valor | Evidência |
| --- | --- | --- | --- |
| Campos ocultos UTM |  |  |  |
| Campos ocultos `v4_*` |  |  |  |
| Click IDs do canal |  |  |  |
| `is_test=true` |  |  |  |
| Lead ID gerado |  |  |  |
| Timestamp |  |  |  |
| Consentimento/LGPD |  |  |  |

### 3.3 Salto 3 → 4: Form → Planilha backup

| Campo | Valor esperado | Valor capturado | Status |
| --- | --- | --- | --- |
| `client_id` |  |  |  |
| `campaign_id` |  |  |  |
| `adgroup_id` |  |  |  |
| `creative_id` |  |  |  |
| `test_id` |  |  |  |
| `utm_source` |  |  |  |
| `utm_medium` |  |  |  |
| `utm_campaign` |  |  |  |
| `utm_content` |  |  |  |
| `utm_term` |  |  |  |
| `gclid` / `gbraid` / `wbraid` |  |  |  |
| `fbclid` / `_fbp` / `_fbc` |  |  |  |
| `is_test` |  |  |  |

### 3.4 Salto 4 → 5: Planilha backup → CRM

| Campo | Valor esperado | Valor capturado | Status |
| --- | --- | --- | --- |
| `lead_id` |  |  |  |
| `campaign_id` |  |  |  |
| `adgroup_id` |  |  |  |
| `creative_id` |  |  |  |
| `test_id` |  |  |  |
| `first_utm_*` |  |  |  |
| `last_utm_*` |  |  |  |
| Click IDs persistidos |  |  |  |
| `lead_status` |  |  |  |
| `sales_owner` |  |  |  |
| `is_test` |  |  |  |

### 3.5 Salto 5 → análise: CRM → BI / dashboard

| Verificação | Status | Evidência |
| --- | --- | --- |
| Export CRM contém todos os campos requeridos |  |  |
| Cruzamento `utm × gclid × fbclid × wbraid × gbraid` por linha |  |  |
| Filtro `is_test=true` aplicado em dashboards |  |  |
| Granularidade de criativo preservada |  |  |

### 3.6 Em qual salto o first-touch é sobrescrito?

- ( ) Não há sobrescrita
- ( ) Salto 1→2 (URL/LP)
- ( ) Salto 2→3 (Form)
- ( ) Salto 3→4 (Backup)
- ( ) Salto 4→5 (CRM)
- ( ) Salto 5→análise (BI)

Detalhe técnico:

## 4. Regras Críticas

| Regra | Status | Evidência | Observação |
| --- | --- | --- | --- |
| First-touch não sobrescreve |  |  |  |
| Last-touch atualiza quando deve |  |  |  |
| Dedupe de lead funciona |  |  |  |
| Evento de conversão dispara |  |  |  |
| Export permite match |  |  |  |

## 5. Verificação Dedup CAPI (Meta)

| Verificação | Status | Evidência |
| --- | --- | --- |
| `event_id` UUID v4 gerado uma vez na origem |  |  |
| `event_id` browser = `event_id` server |  |  |
| `event_name` idêntico nos dois lados |  |  |
| Delta `event_time` < 60s |  |  |
| `user_data` (email/phone hashed SHA-256) consistente |  |  |
| Meta Events Manager → Test Events → coluna "Deduplicated" = `Yes` |  |  |
| EMQ ≥ 7,0 |  |  |

## 6. Dark Traffic CRM ↔ Plataforma

| Métrica | Valor | Observação |
| --- | --- | --- |
| Leads no CRM (período) |  |  |
| Leads em Meta Ads (período) |  |  |
| Leads em Google Ads (período) |  |  |
| Leads em outras plataformas |  |  |
| Gap absoluto (CRM − plataformas) |  |  |
| **Gap percentual** |  |  |
| Cohort gap: WhatsApp direto |  |  |
| Cohort gap: telefone |  |  |
| Cohort gap: referral |  |  |
| Cohort gap: organic/direct |  |  |

Avaliação: gap < 15% saudável; gap > 40% requer ressalva escrita no CAC de mídia paga.

## 7. Gaps Codificados

| Código | Descrição | Camada/Salto | Impacto | Dono | Esforço | Bloqueia go-live | Mitigação interina | Prazo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `bloqueador-N1` |  |  |  |  |  |  |  |  |
| `alto-N1` |  |  |  |  |  |  |  |  |
| `medio-N1` |  |  |  |  |  |  |  |  |
| `baixo-N1` |  |  |  |  |  |  |  |  |

## 8. Decisão Formal Codificada

Decisão final (`go` / `go-com-risco` / `no-go` / `retestar`):

Justificativa por código:

- `bloqueador-N*`: 
- `alto-N*`: 
- `medio-N*`: 
- `baixo-N*`: 

Aceite escrito do operador (necessário para `go-com-risco`):

Condições para go-live:

- 

Reteste necessário:

- 
