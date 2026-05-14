---
name: gerador-taxonomia-utm-ids
description: Gera IDs canônicos, nomes de campanha/ad group/criativo, UTMs completas e parâmetros v4 para campanhas de leadgen. Aplica lowercase enforçado, hífen como separador, regra de imutabilidade de IDs antigos quando versionar criativos (`crv-x` original preservado mesmo após `crv-x-v2` publicado), cap de 150 chars em utm_campaign, e exige canonical tag SEO na LP de destino. É insumo upstream do contrato-dados-marketing-crm (IDs gerados aqui viram chaves do dicionário) e do instrumentation-engineer (taxonomia consumida pelo measurement plan). Use antes de setup Meta Ads, Google Ads, LP, plano de mídia, briefing criativo, tracking, CRM ou quando o usuário pedir nomenclatura, UTMs, campaign_id, creative_id, adgroup_id ou URLs parametrizadas.
---

# Gerador Taxonomia UTM IDs

## Quando Usar

Use quando precisar criar:

- `client_id`, `campaign_id`, `adgroup_id`, `creative_id` e `test_id`;
- nomes visíveis para campanha, conjunto/ad group e criativo;
- `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`;
- parâmetros `v4_*`;
- URLs finais parametrizadas;
- tabela de UTMs para mídia, LP, CRM e planilha de testes.

Nao use para auditar tracking depois do go-live. Para isso, use a futura skill `qa-tracking-utm-crm`.

## Inputs Necessários

- Cliente e slug do cliente.
- Ano/mês e sequenciais desejados.
- Canal e tipo de mídia.
- Tipo de campanha, objetivo, movimento, cohort, segmento e período.
- Público/ad group: público, temperatura, posicionamento, keyword/match quando Search, placement e geo.
- Criativo: formato, hook, persona, slug, dor, ângulo, etapa e versão.
- Teste: hipótese ou `test_id`.
- URL base da LP ou ponto de conversão.

Se algum valor estiver solto ou com acento/espaço, normalize para slug antes de gerar.

## Workflow

1. Confirme o escopo: uma campanha, vários criativos, Search, social, LP, WhatsApp ou outro ponto.
2. Normalize todos os valores:
   - minúsculas;
   - sem acentos;
   - sem espaços;
   - `-` entre palavras;
   - valores curtos e estáveis.
3. Gere IDs:
   - `cli-{slug_cliente}`;
   - `cmp-{cliente}-{ano}{mes}-{sequencial}`;
   - `adg-{cliente}-{ano}{mes}-{sequencial}`;
   - `crv-{cliente}-{ano}{mes}-{sequencial}`;
   - `tst-{cliente}-{ano}{mes}-{sequencial}`.
4. Monte nomes visíveis:
   - campanha: `{campaign_id} | {tipo_campanha} | {objetivo} | {movimento} | {slug}`;
   - ad group: `{adgroup_id} | {publico} | {temperatura} | {posicionamento} | {slug}`;
   - criativo: `{creative_id} | {formato} | {hook} | {persona} | {slug} | {versao}`.
5. Monte UTMs:
   - `utm_campaign` com campanha, tipo, objetivo, movimento, slug, cohort, segmento e período;
   - `utm_content` com criativo, formato, hook, persona, slug, dor, ângulo, etapa e versão;
   - `utm_term` social ou search conforme o caso.
6. Adicione parâmetros `v4_client_id`, `v4_campaign_id`, `v4_adgroup_id`, `v4_creative_id`, `v4_test_id`.
7. **Validador de canonical tag SEO na LP de destino:** toda URL com UTM gerada nesta skill deve apontar pra LP que tenha `<link rel="canonical" href="https://lp-base-sem-utm">` no `<head>`. Sem canonical, o Google Search indexa cada UTM como página duplicada e mata SEO da LP. Alerte o operador a validar antes de subir campanha.
8. **Versionamento de criativo com imutabilidade:** quando criativo é iterado (ex: nova headline), o ID antigo `crv-headline-a` permanece **imutável** e é criado um novo `crv-headline-a-v2`. Nunca renomeie nem reaproveite ID v1 — preserva histórico analítico longitudinal. Mesma regra vale pra `cmp-` e `adg-`.
9. Gere URL final e tabela para planilha.
10. Valide se IDs e nomes são curtos, parseáveis e coerentes com plano de mídia/briefing.

## Output Esperado

Produza:

- IDs canônicos;
- nomes visíveis;
- UTMs completas;
- parâmetros customizados;
- URL final;
- tabela por campanha/ad group/criativo;
- observações de risco se algum campo estiver genérico, longo ou ausente.

Use `templates/url-utm.md` para documentação manual.
Use `templates/campanha-utm.json` com o script para gerar outputs em lote.

## Script Utilitário

Para gerar CSV e Markdown a partir de JSON:

```bash
python scripts/generate_utm_matrix.py templates/campanha-utm.json --csv /tmp/utm.csv --md /tmp/utm.md
```

O script normaliza valores, monta IDs, nomes, UTMs e URLs. Revise o output antes de publicar campanhas.

## Definition Of Done

- Toda campanha tem `campaign_id`.
- Todo ad group/conjunto tem `adgroup_id`.
- Todo criativo tem `creative_id`.
- Toda URL tem UTMs completas e parâmetros `v4_*`.
- Nomes visíveis têm ID + 3 a 5 dimensões humanas.
- Campos são parseáveis por `__` e `chave-valor`.
- Valores genéricos ou longos foram corrigidos.
- **`utm_campaign` ≤ 150 chars** — alguns relatórios (Looker Studio, GA4 Explorations, GSC) cortam em 100/150. Se estourar, abreviar (`aquisicao`→`aq`, `conversao`→`cv`, `prospeccao`→`pp`, `remarketing`→`rmkt`).
- **LP de destino tem `<link rel="canonical">` apontando pra URL base sem UTMs** (ou alerta explícito ao operador caso não verificável).
- **Versionamento preserva ID antigo**: ao iterar criativo, novo ID `*-v2`, `*-v3` é gerado; o original permanece imutável.

## Referências Cruzadas

- **Upstream desta skill**: nada (esta é fonte de verdade pra IDs e UTMs).
- **Downstream consumido**:
  - `contrato-dados-marketing-crm` (skill irmã workshop) — IDs gerados aqui (`cmp-`, `adg-`, `crv-`, `tst-`) viram chaves do dicionário de dados e do contrato URL → form → backup → CRM.
  - `instrumentation-engineer` (skill global) — taxonomia consumida pelo measurement plan e pelos `dataLayer.push()`.

## Armadilhas

- Criar nomes enormes para análise que deveria estar nos subparâmetros.
- Usar acentos, espaços, maiúsculas ou frases.
- Misturar campanha, ad group e criativo no mesmo campo.
- Publicar criativo sem `creative_id`.
- Criar UTM sem `v4_*` quando CRM/planilha pode receber campos próprios.
- Usar valores livres demais que impedem agrupamento.

## Referências

- Playbook canônico: `assets/canonicos/01_TAXONOMIA_UTM_IDS_E_SUBPARAMETROS.md`
- Detalhamento: `reference.md`
- Template: `templates/url-utm.md`
- Schema: `templates/campanha-utm.json`
