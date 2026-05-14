---
name: retro-otimizacao-campanhas-por-dados
description: Cruza mídia, backup leads, CRM match, UTMs parseadas e feedback comercial para descobrir quais campanhas, criativos, hooks, personas, dores e ângulos geram MQL, SQL, vendas e lead ruim. Use em retro-otimização, debrief, rebrief, leitura N3 ou decisão de mídia/copy/criativo baseada em qualidade.
---

# Retro Otimização Campanhas Por Dados

## Quando Usar

Use depois que campanha já gerou leads e existe base mínima de mídia + leads + CRM.

Use para responder:

- qual campanha trouxe mais MQLs;
- qual criativo trouxe MQLs mais baratos;
- qual hook trouxe SQLs;
- qual formato trouxe lead ruim;
- qual persona avança mais;
- qual dor gera conversa comercial melhor;
- qual canal gera lead barato mas sem fit;
- qual campanha tem problema de SLA.

## Inputs

- export de mídia;
- backup leads;
- CRM match;
- UTMs parseadas;
- feedback comercial;
- qualidade de dados validada.

## Workflow

1. Valide se a base é confiável com `auditoria-qualidade-dados-growth`.
2. Defina grãos de análise:
   - campanha;
   - criativo;
   - formato;
   - hook;
   - persona;
   - dor;
   - ângulo.
3. Calcule métricas:
   - spend;
   - leads;
   - MQL;
   - SQL;
   - venda;
   - CPL;
   - CPMQL;
   - CPSQL;
   - receita;
   - CAC;
   - taxa de desqualificação.
4. Separe lead barato de lead qualificado.
5. Classifique padrões:
   - vencedor;
   - promissor;
   - caro mas qualificado;
   - barato mas ruim;
   - inconclusivo;
   - tracking insuficiente.
6. Gere recomendações para mídia, copy, criativo, LP e vendas.
7. Transforme aprendizados em rebrief para próximo ciclo.

## Output Esperado

- análise por campanha/criativo/atributo;
- hipóteses aprendidas;
- recomendações;
- cortes ou reforços justificados;
- rebrief para próximo ciclo.

Use `templates/analise-retro-otimizacao.md`.
Use `templates/analytics-ready.csv` com o script para sumarizar performance.

## Script Utilitário

```bash
python3 scripts/analyze_retro_optimization.py templates/analytics-ready.csv --group-by creative_id --md /tmp/retro.md --csv /tmp/retro.csv
```

## Definition Of Done

- A análise declara limites de qualidade dos dados.
- Decisões não usam CPL isolado.
- Recomendações conectam mídia, criativo, LP e vendas.
- Aprendizados viram hipóteses para próximo ciclo.
