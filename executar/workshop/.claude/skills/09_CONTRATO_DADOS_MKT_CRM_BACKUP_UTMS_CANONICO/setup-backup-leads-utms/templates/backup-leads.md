# Setup Backup Leads UTMs

## Identificação

- Cliente:
- Client ID:
- Período:
- Dono:
- Link LP:
- Link CRM:
- Link plano de mídia:
- Link taxonomia UTM:
- Última atualização:

## Planilha

Nome:

```text
backup_leads_{client_id}_{ano_mes}
```

## Abas

| Aba | Objetivo | Status | Observações |
| --- | --- | --- | --- |
| `00_README` | Contexto operacional |  |  |
| `01_RAW_LEADS` | Registro bruto de leads |  |  |
| `02_ATTRIBUTION` | Origem e IDs |  |  |
| `03_PARSED_PARAMS` | UTMs e IDs parseados |  |  |
| `04_CRM_MATCH` | Match e status CRM |  |  |
| `05_MEDIA_EXPORT` | Export de mídia |  |  |
| `06_ANALYTICS_READY` | Base pronta para análise |  |  |
| `07_PIVOTS` | Visões recomendadas |  |  |

## Regras

- Lead ID:
- First-touch:
- Last-touch:
- Dedupe:
- Match CRM:
- Cadência de atualização:
- Fonte da verdade:

## Checklist N2

- [ ] Backup padronizado.
- [ ] UTMs chegam na conversão.
- [ ] IDs chegam na planilha.
- [ ] CRM recebe origem ou match confiável.
- [ ] First-touch e last-touch preservados.
- [ ] Dicionário de dados existe.
- [ ] Teste ponta a ponta existe.
- [ ] Análise pós-campanha possível.
