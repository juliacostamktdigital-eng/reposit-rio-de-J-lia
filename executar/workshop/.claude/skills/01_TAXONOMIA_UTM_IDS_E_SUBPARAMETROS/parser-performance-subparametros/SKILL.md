---
name: parser-performance-subparametros
description: Parseia UTMs, IDs v4 e subparâmetros de campanhas para transformar exports de mídia, leads e CRM em tabela analisável por campanha, criativo, formato, hook, persona, dor, ângulo, etapa e qualidade comercial. Use em leitura de performance, planilha de testes, debrief, retro-otimização ou quando houver CSV com UTMs.
---

# Parser Performance Subparâmetros

## Quando Usar

Use quando precisar:

- transformar exports com UTMs em dimensões analisáveis;
- agrupar performance por formato, hook, persona, dor, ângulo e etapa;
- cruzar mídia, lead, MQL, SQL, oportunidade e venda;
- detectar `unknown_source`, `creative_id` vazio ou UTM malformada;
- preparar base para planilha de testes, debrief N3 ou retro-otimização.

Não use para gerar UTMs novas. Para isso, use `gerador-taxonomia-utm-ids`.
Não use para QA de lead teste. Para isso, use `qa-tracking-utm-crm`.

## Inputs Necessários

- CSV de mídia, leads, CRM ou backup com pelo menos parte dos campos:
  - `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`;
  - `v4_client_id`, `v4_campaign_id`, `v4_adgroup_id`, `v4_creative_id`, `v4_test_id`;
  - campos comerciais como MQL/SQL, receita, feedback e status.
- Dicionário de dados quando houver.
- Contexto do período/campanha.

Se só houver nomes de plataforma, tente extrair IDs pelo prefixo. Se não houver IDs, marque como lacuna crítica.

## Workflow

1. Identifique o grão da base: linha por lead, por criativo, por campanha, por dia ou por evento.
2. Normalize cabeçalhos e valores sem alterar o arquivo original.
3. Extraia IDs:
   - primeiro dos campos `v4_*`;
   - depois dos campos UTM;
   - por último dos nomes visíveis, se existirem.
4. Parseie `utm_campaign`:
   - `campaign_id`, `typ`, `obj`, `mov`, `slug`, `coh`, `seg`, `per`.
5. Parseie `utm_content`:
   - `creative_id`, `fmt`, `hook`, `per`, `slug`, `dor`, `ang`, `stage`, `ver`.
6. Parseie `utm_term`:
   - social: `adgroup_id`, `pub`, `temp`, `pos`, `slug`, `plc`, `geo`;
   - search: `adgroup_id`, `kw`, `match`, `temp`, `slug`, `geo`.
7. Gere campos analíticos padronizados.
8. Calcule flags de qualidade:
   - origem desconhecida;
   - ID faltante;
   - UTM malformada;
   - divergência entre `v4_*` e UTM;
   - campo comercial ausente.
9. Produza tabela pronta para análise e resumo de problemas.

## Output Esperado

Produza:

- tabela parseada;
- campos analíticos padronizados;
- relatório de qualidade dos dados;
- alertas de tracking;
- sugestões de correção de taxonomia;
- agrupamentos recomendados para leitura.

Use `templates/performance-export.csv` como exemplo de entrada.
Use `templates/relatorio-parser.md` como modelo de saída.

## Script Utilitário

Para parsear um CSV:

```bash
python scripts/parse_subparams.py templates/performance-export.csv --csv /tmp/performance-parsed.csv --md /tmp/parser-report.md
```

O script preserva o CSV original e cria um novo arquivo com dimensões parseadas.

## Definition Of Done

- IDs principais foram extraídos ou marcados como ausentes.
- `utm_campaign`, `utm_content` e `utm_term` foram parseadas.
- Tabela final permite agrupar por campanha, ad group, criativo, formato, hook, persona, dor, ângulo, etapa e versão.
- Campos de qualidade comercial foram preservados.
- Lacunas e divergências foram listadas.
- O output pode alimentar debrief, planilha de testes e próximo ciclo.

## Armadilhas

- Sobrescrever o export original.
- Parsear valores malformados sem alertar.
- Confiar em `utm_source` quando `creative_id` está vazio.
- Agrupar por nome de campanha quando existe ID.
- Ignorar divergência entre `v4_*` e UTM.
- Misturar first-touch e last-touch sem declarar a regra.

## Referências

- Playbook canônico: `assets/canonicos/01_TAXONOMIA_UTM_IDS_E_SUBPARAMETROS.md`
- Detalhamento: `reference.md`
- Exemplo CSV: `templates/performance-export.csv`
- Template: `templates/relatorio-parser.md`
