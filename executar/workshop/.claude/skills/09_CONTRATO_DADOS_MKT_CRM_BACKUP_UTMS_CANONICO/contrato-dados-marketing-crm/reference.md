# Referência Do Contrato De Dados Marketing CRM

Fonte normativa: `assets/canonicos/09_CONTRATO_DADOS_MKT_CRM_BACKUP_UTMS_CANONICO.md`.

Schema versão: **v2** (8 camadas + dicionário de 22 campos por classe LGPD + dedup CAPI + Consent Mode v2 granular). Compatível com payloads v1 (6 camadas) — auditor mantém leitura sem quebrar.

## Princípio

Tracking só é útil quando permite responder:

```text
qual campanha, conjunto e criativo geraram leads que avançaram no funil?
```

Para isso, a operação precisa de contrato entre mídia, LP/formulário/WhatsApp, dataLayer, planilha backup, CRM, servidor CAPI, planilha de testes e dashboard/debrief.

## 8 Camadas Detalhadas

A v2 expande as 6 camadas v1 com **dataLayer (camada 4)** e **Servidor CAPI (camada 7)**. A regra de propagação é simples: cada campo nasce em uma camada, é gravado nas seguintes via cookie/cache/payload, e nunca é regenerado nas camadas a jusante (o downstream confia no upstream).

### Camada 1 — URL

Transporta UTMs (`utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`) + click-IDs (`gclid`, `fbclid`, `wbraid`, `gbraid`, `ttclid`, `li_fat_id`, `msclkid`) até a LP.

Risco: se a pessoa navegar dentro do site e converter depois, a URL inicial se perde — por isso o snapshot vai imediatamente pra camada 2.

### Camada 2 — Cookie / Storage Browser

Preserva o estado da camada 1 em first-party cookies (sugestão: prefixo `mn_` ou `_v4_`):

- first-touch: gravar uma vez (write-once) — `mn_first_utm_*`, `mn_first_gclid` etc. TTL longo (180-365 dias).
- last-touch: atualizar a cada visita relevante — `mn_last_utm_*`, `mn_last_gclid`. TTL 90-180 dias.
- click-IDs também espelhados como `_fbp` (Meta browser ID, gerado pelo pixel) e `_fbc` (Meta click ID, derivado de `fbclid`).

### Camada 3 — Form Hidden

Snapshot do estado da camada 2 no momento do submit. Campos hidden mínimos:

- `first_utm_*`, `last_utm_*`;
- `gclid`, `fbclid`, `wbraid`, `gbraid`, `ttclid`, `li_fat_id`;
- `_fbp`, `_fbc`;
- IDs canônicos da taxonomia (`v4_client_id` / `v4_campaign_id` / `v4_adgroup_id` / `v4_creative_id` / `v4_test_id`);
- `event_id` (UUID v4 gerado no submit), `cf_lead_id` (UUID v4 gerado no submit);
- `event_time` (unix timestamp);
- URL da LP, referrer, user-agent (opcional — muitas plataformas já capturam);
- 4 sinais Consent Mode v2 (`consent_analytics`, `consent_ads`, `consent_ad_user_data`, `consent_ad_personalization`).

### Camada 4 — dataLayer (NOVA na v2)

`window.dataLayer.push({...})` é a **fonte da verdade** pra GTM, GA4, Meta Pixel + CAPI dedup, Google Ads ECfL/OCI, Clarity etc. O `event_id` UUID v4 vai aqui e é o mesmo UUID enviado server-side via CAPI — **sem isso, não há dedup**.

Estrutura mínima:

```js
window.dataLayer.push({
  event: "lead_submit",
  event_id: "<uuid v4>",
  event_time: 1714838400,
  user_data: {
    email_sha256: "<hash>",
    phone_sha256: "<hash>",
    fbp: "<_fbp value>",
    fbc: "<_fbc value>"
  },
  marketing: {
    first_touch: {...},
    last_touch: {...},
    gclid: "...", fbclid: "..."
  },
  consent: {
    analytics: true, ads: true,
    ad_user_data: true, ad_personalization: true
  },
  ids: {
    cf_lead_id: "<uuid v4>",
    v4_creative_id: "crv-..."
  }
});
```

Princípio Avo: **se o evento nasce com semântica errada na camada 4, todas as camadas downstream herdam o erro**. Qualidade do dataLayer é não-negociável.

### Camada 5 — Backup Planilha

Google Sheets / Supabase / fallback. Sempre existe. Não substitui o CRM; é o cinto de segurança quando webhook falha. Recebe o mesmo payload do submit, com timestamp e status `recebido`.

### Camada 6 — CRM

RD Station / HubSpot / Pipedrive / Bitrix / Salesforce. Recebe payload via webhook ou integração nativa. Armazena origem, status, avanço comercial, feedback, receita, motivo de perda/desqualificação.

Match no CRM:

- `cf_lead_id` (UUID custom field) é a **match key primária** — nunca colide.
- `email_sha256` é fallback quando `cf_lead_id` falha (formulário antigo, integração legada).
- Se ambos faltarem → criar lead com tag `dedupe-pendente` pra revisão manual.

### Camada 7 — Servidor CAPI (NOVA na v2)

Server-Side GTM (Stape, Cloud Run) ou N8N consome o evento `lead_submit` da camada 4 (via tag GTM web → endpoint server) e dispara:

- Meta CAPI (Conversions API) com `event_id` igual ao do pixel browser → **dedup**.
- Google Ads ECfL (Enhanced Conversions for Leads) com email/phone hash.
- Google Ads OCI (Offline Conversion Import) quando o lead vira MQL/SQL no CRM (precisa de `gclid` original ou `gbraid`/`wbraid`).
- TikTok Events API, LinkedIn CAPI, Pinterest CAPI conforme escopo.

EMQ (Event Match Quality) Meta meta de done: ≥ 7,0.

### Camada 8 — Base Analítica

BigQuery / Looker Studio / Metabase. Cruza:

- mídia (Meta/Google/TikTok/LinkedIn export);
- leads do CRM;
- backup planilha;
- UTMs parseadas;
- qualidade comercial (MQL/SQL/win/loss).

Entrega análise pós-campanha por criativo, campanha, conjunto, ICP.

## Dicionário De 22 Campos Por Classe LGPD

A classe LGPD define o que pode ser enviado pra cada destino. PII bruto **nunca** chega em Meta/Google/TikTok — sempre em hash canônico.

### Classe `pii-bruto` (3 campos)

| Campo | Tipo | Origem | Regra | Exemplo | Destino permitido |
|---|---|---|---|---|---|
| `email_raw` | string | form | trim, lowercase opcional | `pessoa@empresa.com` | CRM, backup |
| `phone_raw` | string | form | conforme digitado | `(11) 99999-9999` | CRM, backup |
| `nome_raw` | string | form | trim, capitalização preservada | `Maria Silva` | CRM, backup |

### Classe `pii-hash` (5 campos)

| Campo | Tipo | Origem | Regra de geração | Exemplo | Destino permitido |
|---|---|---|---|---|---|
| `email_sha256` | string (64 hex) | transform front | lowercase → trim → SHA-256 hex (Gmail: remove `.` antes do `@`) | `8b94...` | Meta CAPI, Google Ads ECfL/OCI, dataLayer |
| `phone_e164` | string | transform front | E.164 (`+5511999999999`, sem máscara) | `+5511999998888` | CRM, backup, transformar antes de hash |
| `phone_sha256` | string (64 hex) | transform front | E.164 → SHA-256 hex | `c3a1...` | Meta CAPI, Google Ads ECfL |
| `first_name_sha256` | string (64 hex) | transform front | lowercase → trim → SHA-256 hex | `e2b1...` | Meta CAPI (advanced match) |
| `user_id` | string (64 hex) | transform front | sha256(email lowercased) | `8b94...` | GA4 User-ID, dataLayer |

### Classe `id-tecnico` (5 campos)

| Campo | Tipo | Origem | Regra | Exemplo | Notas |
|---|---|---|---|---|---|
| `event_id` | UUID v4 | front (gerado no submit) | mesmo UUID em pixel browser E CAPI server | `8c6f4b2a-...` | **chave de dedup CAPI** |
| `session_id` | string | front (storage) | TTL 30min | `sess_abc123` | analytics |
| `client_id` | string | GA4 cookie `_ga` | gerado pelo GA4 | `1234567890.1234567890` | GA4 User-ID join |
| `lead_id` | UUID v4 | front (gerado no submit) | único por lead | `7a3e...` | match interno |
| `cf_lead_id` | UUID v4 | front (gerado no submit) | custom field CRM | `7a3e...` | **match key primária CRM** |

`lead_id` e `cf_lead_id` podem ser o **mesmo UUID** — convenção é manter um campo distinto pro custom field do CRM pra deixar explícito que é a match key primária.

### Classe `metadata-marketing` (12 campos lógicos)

Click-IDs (8 campos):

| Campo | Tipo | Origem | Quando enviar | Notas |
|---|---|---|---|---|
| `gclid` | string | URL → cookie `mn_gclid` | sempre que presente | Google Ads padrão |
| `fbclid` | string | URL → cookie `mn_fbclid` | sempre que presente | Meta padrão |
| `wbraid` | string | URL → cookie `mn_wbraid` | iOS 14+ Google Ads web | substitui `gclid` quando ATT bloqueia |
| `gbraid` | string | URL → cookie `mn_gbraid` | iOS 14+ Google Ads app | substitui `gclid` quando ATT bloqueia |
| `fbp` | string | cookie `_fbp` (Pixel gera) | sempre (Meta CAPI) | identificador browser Meta |
| `fbc` | string | cookie `_fbc` (Pixel grava do `fbclid`) | sempre que houve `fbclid` | identificador click Meta |
| `ttclid` | string | URL → cookie | TikTok Ads | TikTok Events API |
| `li_fat_id` | string | URL → cookie | LinkedIn Ads | LinkedIn CAPI |

First/last touch (8 campos):

| Campo | Regra | Exemplo |
|---|---|---|
| `first_touch_source` | write-once cookie | `linkedin` |
| `first_touch_medium` | write-once cookie | `cpc` |
| `first_touch_campaign` | write-once cookie | `cmp-cli001-2026q2-leadgen-001` |
| `first_touch_timestamp` | write-once cookie | `1714838400` |
| `last_touch_source` | update on conversion | `google` |
| `last_touch_medium` | update on conversion | `cpc` |
| `last_touch_campaign` | update on conversion | `cmp-cli001-2026q2-brand-002` |
| `last_touch_timestamp` | update on conversion | `1715443200` |

### Classe `consent` (4 campos — Consent Mode v2 granular ANPD)

| Campo | Tipo | Origem | Notas |
|---|---|---|---|
| `consent_analytics` | bool | banner LGPD | habilita/desabilita GA4, Clarity |
| `consent_ads` | bool | banner LGPD | habilita/desabilita pixels de remarketing |
| `consent_ad_user_data` | bool | banner LGPD (Consent Mode v2) | permite enviar dados pra Meta/Google |
| `consent_ad_personalization` | bool | banner LGPD (Consent Mode v2) | permite personalização (Custom Audiences) |

## Hashing Canônico

Pseudo-código:

```js
// Email
function hashEmail(email) {
  let normalized = email.trim().toLowerCase();
  // Gmail-only: remove ponto antes do @
  if (/@gmail\.com$/.test(normalized)) {
    const [user, domain] = normalized.split("@");
    normalized = user.replace(/\./g, "") + "@" + domain;
  }
  return sha256Hex(normalized);
}

// Phone (Brasil)
function normalizePhoneE164(phone) {
  const digits = phone.replace(/\D/g, "");
  if (digits.startsWith("55")) return "+" + digits;
  if (digits.length === 11) return "+55" + digits;  // celular DDD+9
  if (digits.length === 10) return "+55" + digits;  // fixo DDD+8
  return null; // inválido
}

function hashPhone(phone) {
  const e164 = normalizePhoneE164(phone);
  return e164 ? sha256Hex(e164) : null;
}
```

Encoding:

- **Google Ads (ECfL/OCI)** e **Meta CAPI**: SHA-256 **hex** (lowercase, 64 chars).
- **UID 2.0** (publishers programáticos): SHA-256 **base64** — não é o caso default da operação.

## Match Key E Dedup

### Match Key No CRM

- **Primária**: `cf_lead_id` (UUID v4 custom field). Nunca colide. Gerado no front no submit, enviado simultaneamente pra backup, CRM e dataLayer.
- **Fallback**: `email_sha256`. Usado quando `cf_lead_id` falha (formulário legado, integração antiga, retry sem cookie).
- **Sem nenhuma**: criar lead no CRM com tag `dedupe-pendente`. Revisão manual semanal pra reconciliar.

### Dedup CAPI

Meta CAPI deduplica eventos quando:

1. Pixel browser dispara `Lead` com `event_id = X`.
2. CAPI server dispara `Lead` com **mesmo `event_id = X`**.
3. Mesmo `event_name`, mesmo `event_time` (±5min).

**Sem `event_id` consistente, Meta conta o evento duas vezes** — duplica conversão, distorce CPL, polui Custom Audiences.

Mesmo princípio vale pra Google Ads Enhanced Conversions (matched via `gclid` + email hash + transaction_id).

## LGPD Compliance

### Banner Com 4 Categorias Granulares (ANPD)

ANPD orienta categorização granular (não basta "aceitar/recusar tudo"):

1. **Necessário** — sempre ativo (sessão, segurança, anti-fraude). Não é cookie de marketing.
2. **Funcional** — preferências do usuário (idioma, layout). Opcional.
3. **Analytics** — GA4, Clarity, heatmaps. Opcional → controla `consent_analytics`.
4. **Marketing** — pixels Meta/Google/TikTok/LinkedIn, remarketing. Opcional → controla `consent_ads`, `consent_ad_user_data`, `consent_ad_personalization`.

### 4 Sinais Consent Mode v2

Google Consent Mode v2 (obrigatório EEA, recomendado Brasil) exige 4 sinais:

| Sinal | O que controla |
|---|---|
| `analytics_storage` (=`consent_analytics`) | GA4 cookies + measurement |
| `ad_storage` (=`consent_ads`) | cookies de ads + remarketing |
| `ad_user_data` | envio de dados de usuário pra Google Ads |
| `ad_personalization` | personalização de audiências |

Quando o usuário recusa, Google Ads/GA4 entra em **modeled conversions** (estimativa) ao invés de sumir o dado.

### Regra Inviolável

**PII raw nunca sai pra plataforma de mídia**. Email/phone/nome só viajam pra Meta/Google/TikTok em SHA-256 hex (com normalização canônica). Violação = banimento da conta + multa LGPD/ANPD.

## Lead ID

Ideal: UUID v4 gerado no front no momento da conversão (`cf_lead_id`) e enviado para planilha backup, CRM, automação, thank-you page e eventos.

Aceitável na v1: hash ou dedupe por email normalizado, telefone normalizado e data.

Evitar: nome, telefone sem normalização ou identificador que muda por sistema.

## Critérios De Qualidade

Bom:

- `unknown_source_rate` menor que 10%;
- `crm_match_rate` maior que 90%;
- `creative_id_fill_rate` maior que 95%;
- `mql_feedback_rate` maior que 80%;
- `lead_id_duplicate_rate` baixo e monitorado;
- `capi_dedup_rate` maior que 95% (Meta Events Manager);
- `emq_score` Meta CAPI maior ou igual a 7,0.

Alerta:

- mais de 15% de origem desconhecida;
- leads sem `creative_id`;
- CRM sem motivo de desqualificação;
- muitos leads sem primeiro contato;
- backup e CRM divergentes;
- pixel e CAPI com `event_id` divergente (dedup quebrado);
- consent banner ausente ou só "aceitar/recusar tudo".

## Critério N2

Contrato N2 quando:

- existe planilha backup padronizada;
- UTMs chegam na conversão;
- IDs chegam na planilha;
- CRM recebe origem ou existe match confiável;
- first-touch e last-touch são preservados;
- existe dicionário de dados;
- existe teste ponta a ponta;
- análise pós-campanha é possível.

## Critério N3

Contrato N3 quando:

- dados são atualizados em cadência;
- debrief usa qualidade comercial;
- campanhas são otimizadas por MQL/SQL/venda;
- padrões de criativo são analisados;
- erros de dados viram ação corretiva;
- aprendizados alimentam DEOC/DCC, plano de mídia e briefing;
- CAPI server-side ativo com EMQ ≥ 7,0;
- Consent Mode v2 granular ativo com modeled conversions.

## Referências Cruzadas

### Upstream (consome saída de)

- **`gerador-taxonomia-utm-ids`** (skill irmã workshop) — gera os IDs canônicos `cli-`, `cmp-`, `adg-`, `crv-`, `tst-` que viram chaves do contrato em todas as 8 camadas.
- **`instrumentation-engineer`** (skill global) — entrega o measurement plan, schema versioning Snowplow-style e snippets `dataLayer.push()` que populam as camadas 2-4. Sem o measurement plan da IE, este contrato é especulação sobre o que o front realmente envia.

### Downstream (alimenta)

- **`tracking-engineer`** (skill global) — implementa as tags GTM, variáveis e gatilhos que consomem o dataLayer (camada 4) e disparam Meta CAPI / Google Ads ECfL / OCI conforme contrato. EMQ ≥ 7,0 é o done dele.
- **`qa-tracking-utm-crm`** (skill workshop) — audita ponta a ponta após go-live, valida dedup CAPI, checa `crm_match_rate`, `unknown_source_rate`, fill rate de criativo.

### Mapa Visual

```text
gerador-taxonomia-utm-ids ──> [contrato-dados-marketing-crm] ──> tracking-engineer ──> qa-tracking-utm-crm
                                          ▲
                                          │
                              instrumentation-engineer
                              (measurement plan + dataLayer)
```
