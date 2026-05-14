---
name: setup-backup-leads-utms
description: Cria estrutura de planilha backup de leads e UTMs para preservar lead_id, first/last-touch, IDs v4, parâmetros parseados, match CRM, mídia exportada e tabela analytics ready. Use ao configurar fonte de verdade, fallback de CRM, tracking N2 ou base de análise pós-campanha.
---

# Setup Backup Leads UTMs

## Quando Usar

Use sempre que um cliente tiver captação de leads. A planilha backup é obrigatória mesmo quando o CRM parece confiável.

Use especialmente para:

- criar backup de leads;
- preservar UTMs e IDs;
- estruturar abas de auditoria;
- preparar match CRM;
- criar base analytics ready;
- evitar perda de dados por falha de integração.

## Abas Obrigatórias

1. `00_README`
2. `01_RAW_LEADS`
3. `02_ATTRIBUTION`
4. `03_PARSED_PARAMS`
5. `04_CRM_MATCH`
6. `05_MEDIA_EXPORT`
7. `06_ANALYTICS_READY`
8. `07_PIVOTS`

## Workflow

1. Defina `client_id`, período, dono e links de referência.
2. Crie a planilha com o nome `backup_leads_{client_id}_{ano_mes}`.
3. Monte abas e colunas canônicas.
4. Defina regra de `lead_id`:
   - ideal: UUID na conversão;
   - aceitável v1: hash por email normalizado, telefone normalizado e data.
5. Garanta first-touch e last-touch.
6. Prepare campos de match CRM.
7. Prepare tabela `06_ANALYTICS_READY` com 1 linha por `lead_id`.
8. Documente origem, cadência, dono e observações de qualidade.

## Output Esperado

- estrutura de abas;
- dicionário de colunas;
- CSVs vazios por aba;
- regras de `lead_id`;
- checklist N2;
- base pronta para análise posterior.

Use `templates/backup-leads.md` para setup manual.
Use `templates/backup-leads.json` com o script para gerar arquivos base.

## Script Utilitário

```bash
python3 scripts/build_backup_leads_schema.py templates/backup-leads.json --out /tmp/backup-leads
```

## Definition Of Done

- Todas as abas canônicas existem.
- UTMs first e last são preservadas.
- IDs v4 estão na atribuição.
- CRM match tem método e confiança.
- Analytics ready permite leitura por lead, campanha, criativo, MQL e SQL.
