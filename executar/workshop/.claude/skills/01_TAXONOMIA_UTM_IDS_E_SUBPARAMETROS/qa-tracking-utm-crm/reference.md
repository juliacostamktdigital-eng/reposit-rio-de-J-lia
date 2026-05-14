# Referência Do QA Tracking UTM CRM

Fonte normativa: `assets/canonicos/01_TAXONOMIA_UTM_IDS_E_SUBPARAMETROS.md`.

## Objetivo

Garantir que a origem do lead seja preservada desde a URL até a base analítica, permitindo otimizar por MQL, SQL, oportunidade e venda, não apenas por CPL.

## Cadeia De Validação Em 5 Saltos

A validação **não tem 3 saltos, tem 5**. Cada salto pode silenciosamente sobrescrever ou descartar parte da origem — o trabalho do QA é identificar **exatamente em qual salto** o first-touch se perde.

```text
[1] URL com UTMs/IDs/click IDs
        |
        v
[2] LP (browser/cookie/session/dataLayer)
        |
        v
[3] Form / WhatsApp / ponto de conversão (campos ocultos)
        |
        v
[4] Planilha backup (Sheets/N8N/webhook)
        |
        v
[5] CRM (HubSpot/RD/Pipedrive/Salesforce)
        |
        v
(análise: BI / dashboard / planilha de testes)
```

### Falhas típicas por salto

| Salto | Falha típica | Sintoma |
| --- | --- | --- |
| 1→2 | Redirect 302 com `Location` sem query string; CDN/proxy reescrevendo URL | UTMs somem antes da LP renderizar |
| 2→3 | GTM/dataLayer carrega depois do `submit`; SPA com hash routing perdendo querystring | Campos ocultos vazios mesmo com UTM na URL |
| 3→4 | Webhook trunca payload; integração só mapeia `utm_source`/`utm_medium`; backup só recebe email | `creative_id`, `gclid`, `fbclid` perdidos |
| 4→5 | CRM tem property mas não há mapping no integrador; CRM sobrescreve first-touch a cada conversão | First-touch vira last-touch silenciosamente |
| 5→análise | Export do CRM não traz `creative_id`/`adgroup_id`; BI agrega só por `utm_source` | Decisão sobe sem granularidade de criativo |

## Campos Obrigatórios

### UTMs

- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_content`
- `utm_term`

### IDs `v4_*`

- `v4_client_id`
- `v4_campaign_id`
- `v4_adgroup_id`
- `v4_creative_id`
- `v4_test_id`

### Click IDs (2025-2026)

Capture **todos** os click IDs do canal. Cookies de browser caem com ITP/ETP, restauração de iOS 14+ e modo sem cookies → click ID na URL é a fonte mais confiável.

| Click ID | Plataforma | Quando aparece | Cookie correspondente | Onde usar |
| --- | --- | --- | --- | --- |
| `gclid` | Google Ads | Search/Display/YT clássico, com cookies disponíveis | `_gcl_aw` | Conversion Linker, GA4, Offline Conversion Import |
| `gbraid` | Google Ads | Tráfego iOS 14+ vindo de **app** (YouTube, Discover) sem IDFA | `_gcl_gb` | Enhanced Conversions for Web, EC for Leads |
| `wbraid` | Google Ads | Tráfego iOS 14+ vindo de **web** sem cookies disponíveis | `_gcl_aw` (parcial) | Enhanced Conversions, Modeled Conversions |
| `fbclid` | Meta (FB/IG) | Click em ad orgânico/pago em qualquer device | `_fbc` (derivado) | CAPI, Advanced Matching, dedup |
| `_fbp` | Meta (browser) | Definido pelo Pixel no primeiro pageview | cookie `_fbp` | CAPI obrigatório (user_data) |
| `_fbc` | Meta (browser) | Definido pelo Pixel quando `fbclid` presente | cookie `_fbc` | CAPI obrigatório (user_data) |
| `ttclid` | TikTok Ads | Click em ad TikTok | cookie `_ttp` (derivado) | TikTok Events API |
| `li_fat_id` | LinkedIn Ads | Click em ad LinkedIn | cookie `li_fat_id` | LinkedIn Conversions API |
| `msclkid` | Microsoft/Bing Ads | Click em ad Bing | cookie `_uetmsclkid` | UET, Offline Conversions |

Regra: para cada lead, no CRM o **mesmo registro** deve carregar `gclid` **OU** `gbraid` **OU** `wbraid` (Google) e `fbclid` + `_fbp` + `_fbc` (Meta) quando origem permitir. Cruzamento `utm × gclid × fbclid × wbraid × gbraid` é o que permite reconciliação Plataforma ↔ CRM.

### Convenção De Lead Teste

Todo lead teste **obrigatoriamente**:

- email padrão: `qa+<timestamp-iso8601>@<dominio-cliente>.com`
  - exemplo: `qa+20260504T1530-001@cliente.com`
  - permite filtro regex `^qa\+\d` em qualquer ferramenta;
- payload contém flag `is_test: true` (campo oculto no form, hidden field no payload, propriedade booleana no CRM);
- regra de exclusão automática configurada **antes** do teste em:
  - Custom Audiences / Lookalikes (Meta) — exclude `is_test=true`;
  - Customer Match (Google) — exclude segment;
  - dashboards de performance (BI/Looker/Sheets) — filtro `WHERE is_test = false`;
  - Conversions API (Meta/Google) — não dispara evento de venda real para lead teste, ou dispara em `test_event_code` separado.

Sem essas três coisas, lead teste polui Lookalike, infla CTR, distorce custo por aquisição e contamina modelos de bidding. **Não execute QA sem o lead teste seguir a convenção.**

### Campos CRM/backup mínimos

- `lead_id`
- `created_at`
- `client_id`
- `campaign_id`
- `adgroup_id`
- `creative_id`
- `test_id`
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
- `is_test` (boolean)
- click IDs persistidos (`gclid`, `gbraid`, `wbraid`, `fbclid`, `_fbp`, `_fbc`, `ttclid`, `li_fat_id`, `msclkid`) quando origem permitir

## Regras First-Touch E Last-Touch

First-touch:

- gravar uma vez;
- não sobrescrever em nova visita;
- preservar primeira origem relevante;
- conter `first_utm_source`, `first_utm_medium`, `first_utm_campaign`, `first_utm_content`, `first_utm_term`, `first_conversion_at`.

Last-touch:

- atualizar em nova conversão relevante;
- registrar última origem antes da conversão;
- conter `last_utm_source`, `last_utm_medium`, `last_utm_campaign`, `last_utm_content`, `last_utm_term`, `last_conversion_at`.

## Verificação De Dedup CAPI (Meta)

CAPI server-side **complementa** o pixel browser, não substitui. Se browser e server enviam o mesmo evento sem chave de dedup, Meta conta 2× e o EMQ degrada.

### Requisitos

1. **`event_id` UUID v4**, gerado **uma vez** na origem (browser, antes do submit), e enviado **igual** em:
   - `fbq('track', 'Lead', {...}, {eventID: '<uuid>'})` no browser;
   - payload do CAPI server-side (`event_id: '<uuid>'`) — N8N/Stape/Cloud Run/GTM Server.
2. **`event_name` idêntico** nos dois lados (`Lead` ≠ `lead` ≠ `LeadSubmit`).
3. **`event_time` próximo** (delta < 60s).
4. **`user_data` consistente** (email/phone hashed SHA-256, mesma normalização).

### Como verificar

1. Abrir Meta Events Manager → Test Events → adicionar `test_event_code`.
2. Submeter lead teste com convenção `qa+timestamp@dominio` + `is_test=true`.
3. Aguardar até 60s.
4. Procurar dois eventos `Lead` com mesmo `event_id`.
5. Coluna **"Deduplicated"** deve estar **`Yes`** para o par.
6. Se ambos chegam mas não deduplicam: `event_id` divergente, `event_name` divergente, ou delta de tempo > 60s.
7. Se só browser chega: CAPI server não está disparando.
8. Se só server chega: pixel browser não está disparando ou está bloqueado.

EMQ ≥ 7,0 é meta de done para CAPI saudável (mesmo critério usado pela skill `tracking-engineer`).

## Decisão Formal Codificada

A decisão **não é opinião**. É decisão escrita com código de classificação por gap + plano de correção operacionalizável.

### Códigos de classificação

Formato: `<severidade>-N<numero>` onde número é sequencial dentro do QA.

- `bloqueador-N1`, `bloqueador-N2`, … — impede go-live, match ou leitura confiável de origem.
- `alto-N1`, … — gera risco de falso aprendizado em mídia (otimização cega, lookalike contaminada).
- `medio-N1`, … — afeta completude; pode ser aceito temporariamente com risco escrito.
- `baixo-N1`, … — melhoria de governança/padronização.

### Plano de correção por código

Para cada código, registrar **obrigatório**:

- **dono** (nome real, não "TI" / "marketing");
- **esforço estimado** (em horas ou pontos);
- **bloqueia go-live**: `sim` / `não`;
- **mitigação interina** (se `bloqueia=não`, qual o workaround até a correção definitiva);
- **prazo** (data ou sprint).

### Decisão final

| Decisão | Critério |
| --- | --- |
| `go` | zero gaps; ou só `baixo-N*` com plano e dono |
| `go-com-risco` | zero `bloqueador-N*`; ≤2 `alto-N*` com mitigação documentada e aceite escrito do operador |
| `no-go` | ≥1 `bloqueador-N*`; ou `alto-N*` sem mitigação possível |
| `retestar` | correção foi feita; evidência inconclusiva; ambiente errado; ou dados chegaram atrasados/duplicados |

## Dark Traffic CRM ↔ Plataforma

Premissa: **CRM tem leads que plataforma de mídia não tem**. Não é bug, é dark traffic. Inclui:

- WhatsApp direto (link `wa.me/...` sem UTM, indicação no perfil de Instagram orgânico);
- ligação telefônica (número exibido no anúncio mas não rastreado por call tracking);
- indicação boca-a-boca / member-get-member;
- walk-in (loja física);
- inbound orgânico (SEO, blog, email).

Sem quantificar dark traffic, **CAC de mídia paga fica subestimado** (você atribui leads que vieram orgânicos à campanha) ou **superestimado** (você ignora leads que campanha originou mas perderam UTM no caminho).

### Método de quantificação

1. **Universo CRM**: total de leads no período (ex: últimos 30 dias).
2. **Universo plataformas**: soma de leads/conversões reportadas em Meta + Google + outros (deduplicado por click ID quando possível).
3. **Gap absoluto**: `leads_crm - leads_plataforma`.
4. **Gap percentual**: `gap_absoluto / leads_crm`.
5. **Cohort do gap**: dos leads do CRM **sem** click ID/UTM, quantos têm:
   - origem `whatsapp` direta no CRM?
   - origem `phone` direta?
   - origem `referral`?
   - origem `organic`/`direct` (sem campanha)?
6. **Decisão**: gap < 15% é saudável (mídia paga responde por maioria do volume rastreável). Gap > 40% indica ou (a) tracking quebrado em algum salto, ou (b) negócio rodando muito por canais não rastreáveis — em ambos os casos, a leitura de CAC de mídia paga precisa ressalva escrita.

Anotar `dark_traffic_gap` no JSON de QA com os 4 números (CRM, Meta, Google, gap %).

## Severidade

- `bloqueador`: impede go-live, match ou leitura confiável.
- `alto`: pode gerar falso aprendizado ou perda relevante de origem.
- `medio`: afeta completude, mas pode ser aceito temporariamente.
- `baixo`: melhoria de governança ou padronização.

## Falsos Positivos Comuns

- A plataforma mostra lead, mas CRM não tem origem.
- A URL tem UTM, mas campos ocultos não capturam.
- A planilha recebe `utm_source`, mas não recebe `creative_id`.
- First-touch funciona em uma visita, mas é sobrescrito em retorno.
- Last-touch nunca atualiza.
- Dedupe junta leads diferentes por telefone incompleto.
- Export de CRM não contém campos necessários para análise.
- `event_id` divergente entre pixel browser e CAPI server (Meta conta 2×).
- Lead teste sem convenção `qa+timestamp` poluindo Lookalike.

## Critério N2

Tracking está N2 quando:

- toda campanha tem ID;
- todo criativo tem ID;
- toda URL tem UTM conforme;
- todo lead carrega origem;
- fonte da verdade preserva os campos;
- existe teste ponta a ponta registrado nos 5 saltos;
- click IDs do canal são persistidos quando origem permite;
- dedup CAPI verificado quando há pixel + server.

## Critério N3

Tracking está N3 quando:

- campos são usados para decisão;
- performance é agrupada por atributos de criativo;
- qualidade comercial retroalimenta o próximo ciclo;
- aprendizados existem por cohort/segmento;
- padrão é revisado quando gera ruído ou falso aprendizado;
- dark traffic é quantificado e CAC tem ressalva quando gap > 40%.
