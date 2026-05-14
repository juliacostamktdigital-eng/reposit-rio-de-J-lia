# Mapa De LP / Ponto De Conversão

## 1. Contexto

- Cliente:
- Campanha:
- Tipo de ponto de conversão:
- Persona:
- Etapa do funil:
- Oferta:
- Promessa:
- CTA principal:
- Próximo passo comercial:

## 2. Mapa De Seções

| Ordem | Seção | Objetivo | Título | Subtítulo | Conteúdo | Prova/asset | CTA | Evento | Tracking |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Hero |  |  |  |  |  |  | `lp_view` |  |
| 2 | Problema e tensão |  |  |  |  |  |  |  |  |
| 3 | Solução/mecanismo |  |  |  |  |  |  |  |  |
| 4 | Benefícios |  |  |  |  |  |  |  |  |
| 5 | Provas |  |  |  |  |  |  |  |  |
| 6 | Objeções/FAQ |  |  |  |  |  |  |  |  |
| 7 | Formulário/CTA final |  |  |  |  |  |  | `form_start`, `form_submit` |  |
| 8 | Thank you |  |  |  |  |  |  | `thank_you_view` |  |

## 3. Formulário

### Campos Visíveis

| Campo | Obrigatório? | Objetivo | Observação |
| --- | --- | --- | --- |
| nome | sim | identificação |  |
| email | sim | contato |  |
| telefone | sim | contato |  |
| empresa | sim | fit |  |
| cargo | sim | fit/persona |  |
| segmento | sim | fit |  |
| principal desafio | sim | qualificação |  |
| consentimento LGPD | sim | compliance |  |

### Campos Ocultos

| Campo | Fonte | Regra |
| --- | --- | --- |
| `utm_source` | URL/cookie | capturar |
| `utm_medium` | URL/cookie | capturar |
| `utm_campaign` | URL/cookie | capturar |
| `utm_content` | URL/cookie | capturar |
| `utm_term` | URL/cookie | capturar |
| `v4_campaign_id` | URL/cookie | capturar |
| `v4_adgroup_id` | URL/cookie | capturar |
| `v4_creative_id` | URL/cookie | capturar |
| `v4_test_id` | URL/cookie | capturar |
| `first_touch_*` | storage | preservar |
| `last_touch_*` | conversão atual | atualizar |

## 4. Eventos

| Evento | Gatilho | Destino | Observação |
| --- | --- | --- | --- |
| `page_view` | carregamento | analytics |  |
| `lp_view` | LP carregada | analytics |  |
| `form_start` | início do formulário | analytics |  |
| `form_submit` | envio | analytics/CRM |  |
| `lead_created` | lead criado | CRM/backup |  |
| `thank_you_view` | obrigado | analytics |  |

## 5. Checklist N2

| Critério | Status | Evidência | Gap |
| --- | --- | --- | --- |
| Promessa coerente com anúncio |  |  |  |
| CTA funciona |  |  |  |
| Formulário funciona |  |  |  |
| Campos ocultos capturam UTMs |  |  |  |
| Evento configurado |  |  |  |
| CRM recebe origem |  |  |  |
| Backup recebe lead |  |  |  |
| Mobile-first |  |  |  |
| LGPD/política ok |  |  |  |
