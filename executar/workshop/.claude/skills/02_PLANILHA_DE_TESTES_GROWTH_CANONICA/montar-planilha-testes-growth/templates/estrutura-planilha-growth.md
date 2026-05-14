# Estrutura Da Planilha De Testes Growth

## Metadados

- Cliente:
- Cohort:
- Segmento:
- Período:
- Dono:
- Cadência:
- Link DEOC/DCC:
- Link plano de mídia:
- Link taxonomia UTM:
- Link CRM:

## Abas

| Aba | Função | Status | Observação |
| --- | --- | --- | --- |
| `00_README` | Como usar, links e glossário |  |  |
| `01_TESTES` | Hipóteses, variáveis e decisões |  |  |
| `02_CRIATIVOS` | Criativos e atributos analisáveis |  |  |
| `03_CAMPANHAS` | Estrutura de mídia e metas |  |  |
| `04_ADGROUPS` | Públicos, keywords e recortes |  |  |
| `05_LEADS_FUNIL` | Leads, UTMs e avanço comercial |  |  |
| `06_PERFORMANCE_MIDIA` | Métricas de plataforma |  |  |
| `07_PERFORMANCE_FUNIL` | Qualidade real e custos por etapa |  |  |
| `08_APRENDIZADOS` | Padrões, evidências e recomendações |  |  |

## IDs De Ligação

| ID | Onde aparece | Obrigatório? |
| --- | --- | --- |
| `test_id` | Testes, criativos, leads, performance funil, aprendizados | Sim |
| `campaign_id` | Testes, campanhas, adgroups, leads, mídia, funil | Sim |
| `adgroup_id` | Testes, adgroups, leads, mídia, funil | Sim quando há mídia paga |
| `creative_id` | Criativos, leads, mídia, funil | Sim quando há criativo |
| `lead_id` | Leads e CRM | Sim para análise por lead |

## Checklist N2

| Critério | Status | Evidência | Correção |
| --- | --- | --- | --- |
| Todo teste tem hipótese |  |  |  |
| Todo criativo tem ID |  |  |  |
| Toda campanha tem ID |  |  |  |
| Todo lead tem origem |  |  |  |
| Campanha/criativo conecta com lead |  |  |  |
| Existe decisão registrada |  |  |  |

## Gaps Encontrados

| Gap | Aba | Severidade | Impacto | Dono | Correção |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
