---
name: monitor-maturidade-handoff-executar
description: Consolida histórico de handoffs operacionais EXECUTAR medindo tempo até pacote completo, completude, pendências, desvios venda vs. Growth Class, severidade, retrabalho no planning e risco de churn M0. Use em governança de onboarding, revisão mensal, feedback a vendas/Growth Class ou auditoria N2/N3 do handoff.
---

# Monitor Maturidade Handoff Executar

## Quando Usar

Use quando precisar medir se o processo de handoff escala sem degradar qualidade nem gerar recoleta de contexto no planning.

Situações típicas:

- retrospectiva de handoffs por período;
- risco recorrente de desalinhamento pós-venda;
- churn ou insatisfação M0 ligada a expectativa;
- priorizar melhorias em roteiro de vendas ou Growth Class;
- auditar evolução N2 → N3 do handoff.

## Inputs

- histórico de handoffs (datas, completude, pendências);
- métricas de desvio (quantidade, severidade);
- indicadores de retrabalho no planning;
- notas de risco churn M0 quando existirem.

## Métricas De Referência

Alinhar ao playbook `11`:

- tempo fechamento → pacote de handoff completo;
- completude do pacote;
- número de pendências por handoff;
- número de desvios venda vs. Growth Class;
- severidade média ou máxima dos desvios;
- retrabalho no planning por falta de contexto;
- churn ou risco M0 associado a desalinhamento inicial.

## Workflow

1. Colete registros objetivos por conta/ciclo (não opinião solta).
2. Calcule médias, distribuições e outliers (tempo, pendências, desvios).
3. Separe handoffs completos vs. incompletos e motivos.
4. Identifique padrões problemáticos (ex.: mesmo tipo de promessa mal explicada).
5. Produza recomendações para vendas, Growth Class e operação.
6. Classifique maturidade do processo em N2 ou N3 conforme critérios em `reference.md`.

## Output Esperado

- relatório de maturidade;
- painel resumido de KPIs;
- padrões e feedback acionável;
- gaps para atingir N3.

Use `templates/relatorio-handoff-n3.md`.
Use `templates/handoff-historico.json` com o script para agregar indicadores.

## Script Utilitário

```bash
python3 scripts/aggregate_handoff_maturity.py templates/handoff-historico.json --md /tmp/relatorio-handoff.md --csv /tmp/relatorio-handoff.csv
```

## Definition Of Done

- Métricas foram calculadas a partir de dados rastreáveis.
- Padrões citados têm exemplo ou contagem.
- Recomendações apontam dono sugerido (vendas, GC, ops).
- Nível N2/N3 do processo está justificado.
