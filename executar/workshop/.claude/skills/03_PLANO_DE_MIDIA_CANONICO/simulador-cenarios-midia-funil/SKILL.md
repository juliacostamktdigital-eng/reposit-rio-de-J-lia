---
name: simulador-cenarios-midia-funil
description: Simula cenários pessimista, provável e otimista conectando budget, CPL, funil, ticket, receita, CAC, ROAS e capacidade comercial. Use ao planejar mídia, validar viabilidade financeira, defender budget, comparar canais, estimar MQL/SQL/vendas ou testar sensibilidade antes do go-live.
---

# Simulador Cenários Mídia Funil

## Quando Usar

Use para transformar premissas de mídia e funil em cenários claros antes de comprometer budget, meta ou promessa comercial.

Situações típicas:

- validar se um budget consegue entregar a meta;
- estimar leads, MQLs, SQLs, vendas, CAC e ROAS;
- comparar cenário pessimista/provável/otimista;
- testar sensibilidade de CPL, taxa de conversão e ticket;
- demonstrar inviabilidade de meta com premissas atuais;
- calibrar `plano-midia-leadgen`.

Não use como verdade final. Cenário é hipótese auditável, não previsão garantida.

## Inputs Necessários

- budget total ou por canal;
- CPL esperado por cenário;
- taxa lead -> MQL;
- taxa MQL -> SQL;
- taxa SQL -> oportunidade, quando aplicável;
- taxa oportunidade -> venda ou taxa SQL -> venda;
- ticket médio ou receita por venda;
- meta de leads, MQLs, SQLs, vendas ou receita;
- capacidade comercial;
- SLA/tempo de atendimento;
- benchmark/histórico usado como fonte das premissas.

## Workflow

1. Declare a meta principal e a unidade de sucesso: MQL, SQL, venda, receita, ROAS ou CAC.
2. Separe premissas por cenário:
   - pessimista: CPL maior e conversões menores;
   - provável: benchmark realista;
   - otimista: CPL e conversões melhores, mas justificáveis.
3. Calcule funil:
   - investimento -> leads;
   - leads -> MQLs;
   - MQLs -> SQLs;
   - SQLs -> oportunidades;
   - oportunidades -> vendas;
   - vendas -> receita.
4. Calcule custos:
   - CPL;
   - CPMQL;
   - CPSQL;
   - custo por oportunidade;
   - CAC;
   - ROAS.
5. Compare com metas e capacidade comercial.
6. Gere alertas:
   - volume acima da capacidade;
   - CAC maior que limite;
   - ROAS abaixo do alvo;
   - meta impossível no budget atual;
   - dependência excessiva de premissa otimista;
   - funil quebrado por baixa taxa em uma etapa.
7. Recomende decisão: manter, ajustar budget, ajustar meta, melhorar conversão, reduzir escopo, revisar canal ou bloquear promessa.

## Output Esperado

- tabela de cenários;
- premissas utilizadas;
- principais gargalos;
- alertas de inviabilidade;
- sensibilidade por variável crítica;
- recomendação executiva.

Use `templates/cenarios-midia.json` para entrada estruturada.
Use `templates/cenarios-midia.csv` como exemplo tabular.

## Script Utilitário

```bash
python3 scripts/simulate_media_funnel.py templates/cenarios-midia.json --csv /tmp/cenarios.csv --md /tmp/cenarios.md
```

O script gera CSV e Markdown com métricas calculadas por cenário e alertas básicos.

## Regras De Interpretação

- Se só o cenário otimista bate a meta, a meta não está segura.
- Se o cenário provável não cobre capacidade mínima de vendas, ajuste budget ou tese.
- Se a meta exige conversões acima do histórico sem explicação, sinalize premissa fraca.
- Se o volume de leads supera a capacidade comercial, o problema não é só mídia.
- Se ROAS parece bom com CAC ruim, revise ticket, margem e ciclo de venda.
- Se CPL melhora mas CPMQL piora, há problema de qualidade.

## Definition Of Done

- Três cenários criados.
- Fórmulas explícitas.
- Metas comparadas com resultado simulado.
- Alertas de inviabilidade listados.
- Premissas e fontes declaradas.
- Recomendação clara para plano de mídia.
