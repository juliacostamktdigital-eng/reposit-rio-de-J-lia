---
name: auditoria-qualidade-dados-growth
description: Audita qualidade de dados de growth medindo fonte desconhecida, match CRM, preenchimento de creative_id, feedback MQL, duplicidade de lead_id e divergências entre backup, CRM e mídia. Use antes de análises N3, debrief, retro-otimização ou quando tracking parecer quebrado.
---

# Auditoria Qualidade Dados Growth

## Quando Usar

Use antes de concluir performance, premiar criativo, cortar campanha ou gerar debrief.

Use especialmente quando houver:

- origem desconhecida;
- lead sem `creative_id`;
- baixo match CRM;
- CRM sem feedback comercial;
- duplicidade de `lead_id`;
- divergência entre mídia, backup e CRM;
- muitos leads sem atendimento.

## Métricas Canônicas

- `unknown_source_rate`;
- `crm_match_rate`;
- `creative_id_fill_rate`;
- `mql_feedback_rate`;
- `lead_id_duplicate_rate`.

## Limiares

Bom:

- origem desconhecida menor que 10%;
- match CRM maior que 90%;
- creative ID preenchido maior que 95%;
- feedback MQL maior que 80%;
- duplicidade baixa e monitorada.

Alerta:

- origem desconhecida maior que 15%;
- leads sem `creative_id`;
- CRM sem motivo de desqualificação;
- backup e CRM divergentes;
- muitos leads sem primeiro contato.

## Workflow

1. Colete backup leads, CRM, mídia e dicionário de dados.
2. Valide chaves:
   - `lead_id`;
   - email;
   - telefone;
   - IDs v4;
   - creative ID.
3. Calcule métricas canônicas.
4. Classifique severidade.
5. Liste gaps por fonte.
6. Declare confiabilidade da análise:
   - confiável;
   - confiável com ressalvas;
   - não confiável.
7. Gere plano corretivo.

## Script Utilitário

```bash
python3 scripts/audit_growth_data_quality.py templates/analytics-ready.csv --md /tmp/qualidade-dados.md --csv /tmp/qualidade-dados.csv
```

## Definition Of Done

- Score de qualidade foi calculado.
- Alertas têm severidade.
- A fonte da verdade está declarada.
- Há decisão de confiabilidade.
- Gaps viraram plano corretivo.
