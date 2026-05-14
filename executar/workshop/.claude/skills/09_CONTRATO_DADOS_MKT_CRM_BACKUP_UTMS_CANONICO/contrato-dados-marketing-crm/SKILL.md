---
name: contrato-dados-marketing-crm
description: Define contrato de dados entre mídia, LP/formulário, dataLayer, planilha backup, CRM, planilha de testes e dashboard, incluindo UTMs, IDs canônicos (cli-/cmp-/adg-/crv-/tst-), click-IDs estado-da-arte 2025-2026 (gclid/fbclid/wbraid/gbraid iOS 14+, fbp/fbc, ttclid, li_fat_id), PII com hashing canônico (email_raw + email_sha256, phone_raw + phone_e164 + phone_sha256), event_id UUID v4 (chave de dedup CAPI pixel/server), first/last-touch, lead_id, match CRM (cf_lead_id primária, email fallback), 4 sinais granulares Consent Mode v2 LGPD/ANPD (consent_analytics, consent_ads, consent_ad_user_data, consent_ad_personalization), status de funil e qualidade comercial. Consome IDs do gerador-taxonomia-utm-ids e measurement plan da instrumentation-engineer. Use antes de tracking, backup leads, integração CRM ou análise pós-campanha.
---

# Contrato Dados Marketing CRM

## Quando Usar

Use para garantir que a operação consiga responder quais campanhas, conjuntos e criativos geraram leads que avançaram no funil.

Situações típicas:

- definir dicionário de campos;
- estruturar contrato mídia -> LP -> backup -> CRM;
- preparar análise pós-campanha;
- auditar first/last-touch;
- criar fonte de verdade;
- validar N2 de dados.

## Camadas Do Contrato

1. URL (UTMs + click-IDs).
2. Browser/session storage/cookie first-party (mn_gclid, mn_fbclid, mn_wbraid, mn_gbraid, _fbp, _fbc).
3. Campos ocultos no formulário (snapshot do estado da camada 2 + LGPD signals).
4. **dataLayer** (`window.dataLayer.push()` — fonte da verdade pra GTM, Meta CAPI dedup, GA4 com event_id).
5. Planilha backup (Google Sheets / Supabase / fallback).
6. CRM (RD Station / HubSpot / Pipedrive / Bitrix etc.).
7. Servidor CAPI (SGTM Stape ou N8N — consome dataLayer + dedup por event_id).
8. Base analítica / planilha de testes / BI (BigQuery, Looker Studio, Metabase).

## Workflow

1. Liste camadas do fluxo.
2. Defina campos obrigatórios por camada (incluindo dataLayer + servidor CAPI).
3. Defina regras:
   - first-touch write-once;
   - last-touch update on conversion;
   - lead_id único (UUID v4);
   - **event_id UUID v4** (mesmo valor em pixel + CAPI server-side — chave de dedup);
   - **match key primária**: `cf_lead_id` (custom field UUID gerado no front no submit). **Fallback**: `email_sha256`. Se ambos faltarem, criar lead no CRM com tag `dedupe-pendente` pra revisão manual.
   - **hashing canônico** para PII destinada a Meta CAPI / Google Ads ECfL/OCI:
     - `email`: lowercase → trim → SHA-256 (hex pra Google Ads/Meta CAPI).
     - `phone`: normalizar pra E.164 (`+5511999999999`, sem máscara) → SHA-256.
     - **Nunca enviar `email_raw` ou `phone_raw` direto pra Meta/Google sem hash** (violação Política da Plataforma + LGPD).
   - dedupe;
   - status de funil;
   - feedback comercial.
4. Crie dicionário de dados:
   - nome;
   - tipo;
   - descrição;
   - exemplo;
   - obrigatório;
   - fonte;
   - regra de atualização;
   - **classe LGPD** (`pii-bruto` / `pii-hash` / `id-tecnico` / `metadata-marketing` / `consent`).

   **Campos obrigatórios mínimos do dicionário (estado da arte 2025-2026):**

   | Campo | Tipo | Classe LGPD | Origem | Obrigatório |
   |---|---|---|---|---|
   | `email_raw` | string | pii-bruto | form | sim (CRM) |
   | `email_sha256` | string | pii-hash | form (transform) | sim (CAPI/ECfL) |
   | `phone_raw` | string | pii-bruto | form | condicional |
   | `phone_e164` | string | pii-bruto | form (transform) | condicional |
   | `phone_sha256` | string | pii-hash | form (transform) | condicional (CAPI) |
   | `gclid` | string | id-tecnico | URL → cookie `mn_gclid` | condicional (Google Ads) |
   | `fbclid` | string | id-tecnico | URL → cookie `mn_fbclid` | condicional (Meta) |
   | `wbraid` | string | id-tecnico | URL → cookie `mn_wbraid` | condicional (iOS 14+ Google Ads) |
   | `gbraid` | string | id-tecnico | URL → cookie `mn_gbraid` | condicional (iOS 14+ Google Ads App) |
   | `fbp` | string | id-tecnico | cookie `_fbp` | sim (Meta CAPI) |
   | `fbc` | string | id-tecnico | cookie `_fbc` | sim (Meta CAPI quando há fbclid) |
   | `ttclid` | string | id-tecnico | URL | condicional (TikTok) |
   | `li_fat_id` | string | id-tecnico | URL | condicional (LinkedIn) |
   | `event_id` | UUID v4 | id-tecnico | front (gerado no submit) | sim (dedup CAPI) |
   | `event_time` | unix int | metadata-marketing | front | sim |
   | `cf_lead_id` | UUID v4 | id-tecnico | front (gerado no submit) | sim (match primária) |
   | `user_id` | string | pii-hash | sha256(email) | condicional (User-ID GA4) |
   | `first_touch_utm_source` etc. | string | metadata-marketing | URL → cookie write-once | sim |
   | `last_touch_utm_source` etc. | string | metadata-marketing | URL → cookie update on conversion | sim |
   | `consent_analytics` | bool | consent | banner LGPD | sim |
   | `consent_ads` | bool | consent | banner LGPD | sim |
   | `consent_ad_user_data` | bool | consent | banner LGPD (Consent Mode v2) | sim |
   | `consent_ad_personalization` | bool | consent | banner LGPD (Consent Mode v2) | sim |

5. Verifique critérios N2:
   - backup padronizado;
   - UTMs chegam na conversão;
   - IDs chegam na planilha;
   - CRM recebe origem ou match confiável;
   - first/last-touch preservados;
   - dicionário existe;
   - teste ponta a ponta existe;
   - análise pós-campanha é possível.

## Output Esperado

- contrato de dados;
- dicionário de campos;
- regras first/last-touch;
- regras de match;
- critérios N2/N3;
- gaps de cobertura.

Use `templates/dicionario-dados.md`.
Use `templates/contrato-dados.json` com o script de auditoria.

## Script Utilitário

```bash
python3 scripts/audit_data_contract.py templates/contrato-dados.json --md /tmp/contrato-dados.md --csv /tmp/contrato-dados.csv
```

## Definition Of Done

- Cada campo tem fonte, regra e **classe LGPD**.
- `lead_id` (UUID v4) está definido.
- `event_id` (UUID v4) está definido e é compartilhado pixel + CAPI server-side (sem isso, dedup quebra e Meta/Google contam evento em duplicidade).
- **Match key primária `cf_lead_id` definida**, com fallback `email_sha256`. Plano pra leads sem nenhuma das duas (tag `dedupe-pendente`).
- First-touch não é sobrescrito.
- Last-touch é atualizado corretamente.
- Backup e CRM preservam origem.
- **Hashing canônico aplicado** antes de qualquer envio pra Meta CAPI / Google Ads ECfL/OCI: email lowercase+trim → SHA-256 hex; phone E.164 → SHA-256 hex. PII bruto NUNCA chega na plataforma de mídia.
- **LGPD compliance**: cookie banner com 4 categorias granulares (necessário/funcional/analytics/marketing) ativo antes de go-live; 4 sinais Consent Mode v2 (`consent_analytics`, `consent_ads`, `consent_ad_user_data`, `consent_ad_personalization`) capturados e propagados pra GTM/dataLayer.
- Análise por campanha/criativo/MQL/SQL é possível.

## Referências Cruzadas

- **Upstream**:
  - `gerador-taxonomia-utm-ids` (skill irmã workshop) — fornece IDs canônicos `cli-`, `cmp-`, `adg-`, `crv-`, `tst-` que viram chaves do contrato.
  - `instrumentation-engineer` (skill global) — entrega o measurement plan e snippets `dataLayer.push()` que populam os campos das camadas 2-4. Sem o measurement plan da IE, este contrato é especulação sobre o que o front realmente envia.
- **Downstream**:
  - `tracking-engineer` (skill global) — implementa as tags GTM e variáveis que consomem o dataLayer e dispara CAPI/ECfL/OCI conforme contrato.
  - `qa-tracking-utm-crm` (skill workshop) — audita ponta a ponta após go-live.
