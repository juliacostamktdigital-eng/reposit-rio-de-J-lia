# Dicionário De Dados Marketing -> CRM

Schema versão **v2** — 8 camadas + 22 campos por classe LGPD + Consent Mode v2 granular + dedup CAPI.

## Fluxo (8 Camadas)

1. **URL** — UTMs + click-IDs chegam na LP.
2. **Cookie/storage browser** — first-party cookies (mn_first_*, mn_last_*, _fbp, _fbc), TTL 90-365 dias.
3. **Form hidden** — snapshot do estado da camada 2 + 4 sinais Consent Mode v2 no submit.
4. **dataLayer** — `window.dataLayer.push()`, fonte da verdade pra GTM/CAPI/dedup. `event_id` UUID v4 nasce aqui.
5. **Backup planilha** — Google Sheets / Supabase / fallback.
6. **CRM** — RD Station / HubSpot / Pipedrive / Bitrix. Match primária por `cf_lead_id`.
7. **Servidor CAPI** — Stape / Cloud Run / N8N. Dispara Meta CAPI + Google Ads ECfL/OCI. EMQ ≥ 7,0.
8. **Base analítica** — BigQuery / Looker Studio / Metabase.

## Dicionário De 22 Campos Por Classe LGPD

### Classe `pii-bruto` (3 campos)

| Campo | Tipo | Origem | Regra | Exemplo | Destino permitido |
|---|---|---|---|---|---|
| `email_raw` | string | form | trim | `pessoa@empresa.com` | CRM, backup |
| `phone_raw` | string | form | conforme digitado | `(11) 99999-9999` | CRM, backup |
| `nome_raw` | string | form | trim | `Maria Silva` | CRM, backup |

### Classe `pii-hash` (5 campos)

| Campo | Tipo | Origem | Regra | Exemplo | Destino permitido |
|---|---|---|---|---|---|
| `email_sha256` | string (64 hex) | transform front | lowercase → trim → SHA-256 (Gmail: remove `.`) | `8b94...` | Meta CAPI, Google Ads ECfL/OCI, dataLayer |
| `phone_e164` | string | transform front | E.164 (`+5511999999999`) | `+5511999998888` | CRM, backup |
| `phone_sha256` | string (64 hex) | transform front | E.164 → SHA-256 | `c3a1...` | Meta CAPI, Google Ads ECfL |
| `first_name_sha256` | string (64 hex) | transform front | lowercase → trim → SHA-256 | `e2b1...` | Meta CAPI |
| `user_id` | string (64 hex) | transform front | sha256(email lowercased) | `8b94...` | GA4 User-ID, dataLayer |

### Classe `id-tecnico` (5 campos)

| Campo | Tipo | Origem | Regra | Exemplo | Notas |
|---|---|---|---|---|---|
| `event_id` | UUID v4 | front (submit) | mesmo UUID em pixel + CAPI | `8c6f4b2a-...` | **chave dedup CAPI** |
| `session_id` | string | front (storage) | TTL 30min | `sess_abc123` | analytics |
| `client_id` | string | GA4 cookie `_ga` | gerado GA4 | `1234567890.1234567890` | GA4 User-ID join |
| `lead_id` | UUID v4 | front (submit) | único por lead | `7a3e...` | match interno |
| `cf_lead_id` | UUID v4 | front (submit) | custom field CRM | `7a3e...` | **match key primária CRM** |

### Classe `metadata-marketing` (12 campos lógicos: 8 click-IDs + 4 first-touch + 4 last-touch)

| Campo | Tipo | Origem | Quando enviar |
|---|---|---|---|
| `gclid` | string | URL → cookie `mn_gclid` | sempre |
| `fbclid` | string | URL → cookie `mn_fbclid` | sempre |
| `wbraid` | string | URL → cookie `mn_wbraid` | iOS 14+ Google Ads web |
| `gbraid` | string | URL → cookie `mn_gbraid` | iOS 14+ Google Ads app |
| `fbp` | string | cookie `_fbp` (Pixel) | sempre (Meta CAPI) |
| `fbc` | string | cookie `_fbc` (do `fbclid`) | quando houve `fbclid` |
| `ttclid` | string | URL → cookie | TikTok Ads |
| `li_fat_id` | string | URL → cookie | LinkedIn Ads |
| `first_touch_source` / `_medium` / `_campaign` / `_timestamp` | string / int | URL → cookie | write-once |
| `last_touch_source` / `_medium` / `_campaign` / `_timestamp` | string / int | URL → cookie | update on conversion |

### Classe `consent` (4 campos — Consent Mode v2 granular ANPD)

| Campo | Tipo | Origem | Controla |
|---|---|---|---|
| `consent_analytics` | bool | banner LGPD | GA4, Clarity (`analytics_storage`) |
| `consent_ads` | bool | banner LGPD | pixels remarketing (`ad_storage`) |
| `consent_ad_user_data` | bool | banner LGPD CMv2 | envio dados pra Meta/Google (`ad_user_data`) |
| `consent_ad_personalization` | bool | banner LGPD CMv2 | personalização Custom Audiences (`ad_personalization`) |

## Hashing Canônico

- **email**: `lowercase → trim → SHA-256 hex` (64 chars). Gmail: remover `.` antes do `@`.
- **phone**: normalizar pra E.164 (`+5511999999999`) → `SHA-256 hex`.
- **encoding default**: hex lowercase. Meta CAPI e Google Ads ECfL/OCI exigem hex.
- **regra inviolável**: PII raw nunca sai pra Meta/Google/TikTok/LinkedIn.

## Match Key E Dedup

- **Match key primária CRM**: `cf_lead_id` (UUID v4 custom field).
- **Fallback**: `email_sha256`.
- **Sem nenhuma**: tag `dedupe-pendente` no CRM, revisão manual.
- **Dedup CAPI**: mesmo `event_id` UUID v4 em pixel browser e CAPI server. Mesmo `event_name`, `event_time` ±5min. Sem isso, Meta conta em duplicidade.

## LGPD Compliance

- **Banner com 4 categorias granulares** (ANPD): necessário, funcional, analytics, marketing.
- **4 sinais Consent Mode v2**: `analytics_storage`, `ad_storage`, `ad_user_data`, `ad_personalization`.
- **Modeled conversions**: quando usuário recusa, Google/Meta entram em estimativa (ao invés de sumir o dado).

## Regras

- First-touch: write-once em cookie + form hidden + dataLayer + backup + CRM.
- Last-touch: update on conversion em cookie + form hidden + dataLayer + backup + CRM.
- Dedupe: `cf_lead_id` no CRM; `event_id` no CAPI.
- Match CRM: primária `cf_lead_id`, fallback `email_sha256`, tag `dedupe-pendente` se faltar.
- Feedback comercial: motivo de perda + receita + status MQL/SQL no CRM.
- Fonte da verdade: dataLayer (camada 4) é a fonte normativa pra GTM/CAPI; CRM é fonte da verdade pra qualidade comercial.

## Critérios N2

- [ ] Backup padronizado.
- [ ] UTMs chegam na conversão.
- [ ] IDs chegam na planilha.
- [ ] CRM recebe origem ou match confiável.
- [ ] First-touch preservado.
- [ ] Last-touch preservado.
- [ ] Dicionário existe.
- [ ] Teste ponta a ponta existe.
- [ ] Análise pós-campanha possível.

## Critérios N3 (adicionais à v2)

- [ ] CAPI server-side ativo (camada 7).
- [ ] EMQ Meta ≥ 7,0.
- [ ] Dedup CAPI verificado (mesmo `event_id` pixel + server).
- [ ] Banner LGPD com 4 categorias granulares ativo.
- [ ] 4 sinais Consent Mode v2 propagados pra dataLayer.
- [ ] Hashing canônico declarado e implementado.

## Referências Cruzadas

- **Upstream**: `gerador-taxonomia-utm-ids` (IDs canônicos), `instrumentation-engineer` (measurement plan + dataLayer snippets).
- **Downstream**: `tracking-engineer` (config GTM + CAPI), `qa-tracking-utm-crm` (audit pós go-live).
