---
name: analise-feedback-comercial-growth
description: Analisa feedback comercial de leads para separar problema de lead, promessa, oferta, SLA, tracking ou processo de vendas, usando CRM, motivos de desqualificação, lead quality, speed-to-lead, MQL/SQL e feedback notes. Use em leitura semanal/quinzenal, debrief N3, revisão de campanhas ou rebrief para copy, mídia e oferta.
---

# Análise Feedback Comercial Growth

## Quando Usar

Use quando marketing precisa entender se a campanha gerou demanda ruim, demanda boa não atendida, promessa desalinhada ou gargalo comercial.

Situações típicas:

- leads baratos não viram MQL;
- MQLs não viram SQL;
- vendas rejeita leads;
- motivo de perda se repete;
- speed-to-lead está alto;
- criativo gera lead caro mas qualificado;
- copy/oferta precisa ser ajustada por objeções reais;
- debrief precisa incluir qualidade comercial.

## Inputs Necessários

- export CRM;
- `lead_id`;
- `campaign_id`;
- `creative_id`;
- `test_id`;
- MQL/SQL/oportunidade/venda;
- `disqualification_reason`;
- `lead_quality`;
- `speed_to_lead_minutes`;
- `feedback_notes`;
- campanha/criativo/promessa;
- SLA esperado;
- critérios MQL/SQL.

## Workflow

1. Agrupe por campanha, criativo e teste.
2. Calcule:
   - leads;
   - MQLs;
   - SQLs;
   - oportunidades;
   - vendas;
   - taxa MQL;
   - taxa SQL;
   - speed-to-lead médio;
   - distribuição de qualidade;
   - motivos de desqualificação.
3. Classifique o problema provável:
   - lead ruim;
   - promessa desalinhada;
   - oferta errada;
   - SLA/comercial;
   - tracking/dados;
   - hipótese inconclusiva.
4. Leia feedback notes para objeções recorrentes.
5. Conecte achados com decisões:
   - ajustar público;
   - ajustar promessa;
   - ajustar LP/oferta;
   - revisar SLA;
   - revisar critérios MQL/SQL;
   - escalar criativo qualificado;
   - matar criativo com baixa qualidade;
   - gerar rebrief.
6. Devolva aprendizados para copy, mídia, DEOC e próximo ciclo.

## Output Esperado

- diagnóstico de qualidade comercial;
- tabela por campanha/criativo;
- motivos recorrentes;
- objeções e feedback notes;
- classificação de gargalo;
- recomendações de rebrief;
- campos para debrief N3.

Use `templates/relatorio-feedback-comercial.md` para relatório.
Use `templates/feedback-comercial.csv` com o script para gerar análise.

## Script Utilitário

```bash
python3 scripts/analyze_sales_feedback.py templates/feedback-comercial.csv --md /tmp/feedback-comercial.md --csv /tmp/feedback-comercial-analise.csv
```

O script consolida feedback por campanha/criativo e recomenda diagnóstico preliminar.

## Definition Of Done

- Qualidade comercial foi analisada junto com mídia/funil.
- Motivos de desqualificação foram agrupados.
- SLA foi considerado antes de culpar mídia.
- Objeções recorrentes viraram insumo de copy/oferta.
- Recomendações indicam qual alavanca revisar.
- Aprendizado pode entrar no debrief N3.

## Cuidados

- Não aceitar "lead ruim" sem motivo fechado.
- Não otimizar mídia sem ouvir vendas.
- Não culpar copy se SLA estourou.
- Não ignorar criativo caro que gera SQL.
- Não usar feedback notes sem normalizar padrões.
