# URL Parametrizada E Nomenclatura

## Identificação

- Cliente:
- Client ID:
- Campaign ID:
- Adgroup ID:
- Creative ID:
- Test ID:
- Iteração de (se for v2/v3):
- Motivo da iteração:

## Canonical Tag SEO (LP de destino)

- URL canônica (sem UTMs):
- `<link rel="canonical">` presente no `<head>` da LP? (sim/não):
- Evidência (screenshot view-source ou cURL):

> Sem canonical, Google indexa cada UTM como duplicata e quebra SEO da LP. Validar antes do go-live.

## Nomes Visíveis

| Nível | Nome |
| --- | --- |
| Campanha |  |
| Conjunto/ad group |  |
| Criativo/anúncio |  |

## UTMs

| Parâmetro | Valor |
| --- | --- |
| `utm_source` |  |
| `utm_medium` |  |
| `utm_campaign` |  |
| `utm_content` |  |
| `utm_term` |  |
| `v4_client_id` |  |
| `v4_campaign_id` |  |
| `v4_adgroup_id` |  |
| `v4_creative_id` |  |
| `v4_test_id` |  |

## URL Final

```text

```

## Campos Para CRM / Planilha

| Campo | Valor |
| --- | --- |
| `client_id` |  |
| `campaign_id` |  |
| `adgroup_id` |  |
| `creative_id` |  |
| `test_id` |  |
| `tipo_campanha` |  |
| `objetivo` |  |
| `movimento` |  |
| `cohort` |  |
| `segmento` |  |
| `periodo` |  |
| `publico` |  |
| `temperatura` |  |
| `posicionamento` |  |
| `formato` |  |
| `persona` |  |
| `hook` |  |
| `dor` |  |
| `angulo` |  |
| `etapa_funil` |  |
| `versao` |  |

## Validações De Tamanho E Convenção

| Validação | Status | Observação |
| --- | --- | --- |
| `utm_campaign` ≤ 150 chars | | comprimento atual: |
| Lowercase enforçado em todos os valores | | |
| Hífen como separador interno (sem `_`, ` `) | | |
| Sem acentos | | |
| ID `crv-`/`cmp-`/`adg-` versionado preserva original | | (apenas se for iteração) |

## Observações De QA

- 
