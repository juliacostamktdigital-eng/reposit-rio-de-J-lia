---
name: qa-tracking-utm-crm
description: Valida em 5 saltos (URL → LP → form → backup → CRM) se UTMs, IDs (gclid/fbclid/wbraid/gbraid) e v4_* preservam a origem do lead de ponta a ponta, com cruzamento utm × gclid × fbclid no CRM, verificação de dedup CAPI (event_id idêntico browser ↔ server), convenção de lead teste `qa+timestamp@dominio` + flag `is_test=true`, e decisão formal go/go-com-risco/no-go/retestar com classificação codificada. Use antes de go-live, depois de lead teste, em QA de LP/formulário/WhatsApp, setup Meta Ads, Google Ads, contrato de dados ou quando houver suspeita de tracking quebrado.
---

# QA Tracking UTM CRM

## Quando Usar

Use para validar a ponte:

```text
URL com UTMs -> LP/ponto de conversão -> formulário/WhatsApp -> planilha backup -> CRM -> análise
```

Use especialmente:

- antes de ativar verba;
- depois de criar campanha em rascunho;
- antes de considerar tracking N2;
- quando leads chegam sem origem;
- quando CRM e planilha não batem;
- quando há dúvida sobre first-touch, last-touch, `creative_id` ou dedupe.

## Inputs Necessários

- URL final com UTMs e parâmetros `v4_*`.
- Registro do lead teste na LP/formulário/WhatsApp.
- Linha da planilha backup.
- Registro do CRM.
- Campos esperados de campanha, ad group, criativo e teste.
- Evidência de evento/conversão quando houver.
- Regras de first-touch, last-touch e deduplicação.

Se algum input não existir, registre como gap. Não aprove go-live com base em suposição.

## Workflow

1. Extraia os parâmetros esperados da URL:
   - `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`;
   - `v4_client_id`, `v4_campaign_id`, `v4_adgroup_id`, `v4_creative_id`, `v4_test_id`;
   - click IDs do ecossistema: `gclid`, `gbraid`, `wbraid` (Google), `fbclid` (Meta), `msclkid` (Bing) quando aplicável.
2. Submeta o lead teste com **convenção de lead teste**: email `qa+<timestamp>@<dominio-cliente>.com` + flag `is_test=true` no payload (campo oculto), com regra de exclusão automática em audiences/relatórios. Sem isso, lead teste polui dashboard e Lookalike.
3. Compare URL vs formulário/campos ocultos (salto 1→2).
4. Compare URL → LP → formulário → planilha backup → CRM (salto a salto, **5 saltos**, não 3). Identifique exatamente em qual salto o first-touch é sobrescrito ou o ID é perdido (problema típico: redirect 302 com `Location` sem query string; tag manager carregando depois do form submit; CRM mapeando só `utm_source` e descartando `gclid`).
5. Compare planilha backup vs CRM (salto 4→5).
6. Verifique:
   - IDs preservados (utm_*, v4_*, gclid, fbclid, wbraid, gbraid);
   - first-touch não sobrescrito;
   - last-touch atualizado quando aplicável;
   - dedupe funcionando;
   - **dedup CAPI**: confirme `event_id` UUID idêntico em pixel browser e CAPI server side (Meta Events Manager → Test Events → coluna "Deduplicated" deve estar `Yes`). Sem `event_id` consistente, Meta conta 2× e EMQ degrada;
   - cruzamento `utm × gclid × fbclid × wbraid` por linha do CRM (mesmo lead deve ter os 5 campos preenchidos quando origem permite);
   - export permite cruzar lead com campanha/criativo;
   - eventos de conversão foram gerados.
7. **Dedup CRM vs plataforma** — assuma que CRM tem leads que plataforma não tem (WhatsApp direto, telefone, indicação, walk-in). Quantifique gap (% leads CRM sem origem de plataforma) e marque como "dark traffic", não ignore. Sem isso, CAC de mídia paga fica subestimado.
8. Classifique achados com **código de classificação** (não opinião):
   - `bloqueador-N1`, `bloqueador-N2`, ... — impede go-live ou leitura confiável;
   - `alto-N1`, ... — gera risco de falso aprendizado em mídia;
   - `medio-N1`, ... — exige correção mas não bloqueia se risco for aceito por escrito;
   - `baixo-N1`, ... — melhoria.
9. Decida formal escrita: `go` | `go-com-risco` | `no-go` | `retestar` com **justificativa por código** + plano de correção (**dono + esforço estimado + bloqueio go-live sim/não**) por gap. Critério: zero bloqueadores + ≤2 altos com mitigação documentada → `go-com-risco`; zero altos → `go`; ≥1 bloqueador → `no-go`.

## Output Esperado

Produza:

- checklist de QA;
- comparação esperado vs capturado;
- gaps por camada;
- decisão go/no-go;
- evidências exigidas antes do go-live;
- plano de correção com dono.

Use `templates/checklist-qa-tracking.md` para registro manual.
Use `templates/lead-test-qa.json` com o script para comparar esperado vs capturado.

## Script Utilitário

Para comparar URL esperada, backup e CRM:

```bash
python scripts/compare_tracking_capture.py templates/lead-test-qa.json --md /tmp/qa-tracking.md --csv /tmp/qa-tracking.csv
```

O script ajuda a encontrar divergências, mas a decisão final deve considerar evidências visuais, eventos e contexto operacional.

## Definition Of Done

- URL final contém UTMs, `v4_*` e click IDs do canal (gclid/fbclid/wbraid/gbraid quando aplicável).
- Campos ocultos capturam a origem (5 saltos validados).
- Planilha backup recebe todos os IDs.
- CRM recebe origem ou há match confiável via backup; cruzamento utm × gclid × fbclid disponível por lead.
- First-touch e last-touch seguem a regra.
- Lead teste foi registrado com convenção `qa+timestamp@dominio` + `is_test=true`, com evidência e exclusão de audiences confirmada.
- **Dedup CAPI verificado**: `event_id` idêntico browser ↔ server, status "Deduplicated" no Meta Events Manager.
- Gap "dark traffic" (CRM sem origem de plataforma) quantificado.
- Decisão `go`/`go-com-risco`/`no-go`/`retestar` documentada com código de classificação por gap + plano de correção (dono + esforço + bloqueio go-live).

## Armadilhas

- Validar só a URL e não o CRM.
- Aprovar tracking sem lead teste real.
- Considerar UTM ok mesmo sem `creative_id`.
- Sobrescrever first-touch.
- Não testar dedupe.
- Não verificar se export consegue cruzar lead, campanha e criativo.

## Referências

- Playbook canônico: `assets/canonicos/01_TAXONOMIA_UTM_IDS_E_SUBPARAMETROS.md`
- Detalhamento: `reference.md`
- Template: `templates/checklist-qa-tracking.md`
- Schema: `templates/lead-test-qa.json`
- **Skill irmã** `contrato-dados-marketing-crm` — define o contrato; QA testa o contrato sob carga real.
