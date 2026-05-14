# Referência Do Simulador De Cenários Mídia Funil

Fonte normativa: `assets/canonicos/03_PLANO_DE_MIDIA_CANONICO.md`.

## Papel Da Skill

O simulador verifica se uma tese de mídia é financeiramente e operacionalmente plausível. Ele conecta orçamento, CPL, conversões de funil, ticket, receita, CAC e ROAS antes de virar promessa de campanha.

## Cenários Obrigatórios

### Pessimista

Representa atrito real:

- CPL acima do planejado;
- menor taxa lead -> MQL;
- menor taxa MQL -> SQL;
- menor taxa de venda;
- possível SLA pior;
- volume comercial aquém da meta.

### Provável

Representa expectativa realista:

- premissas baseadas em histórico ou benchmark;
- conversões compatíveis com qualidade esperada;
- volume dentro da capacidade comercial;
- risco ainda explícito.

### Otimista

Representa upside justificável:

- CPL melhor que benchmark;
- taxas melhores por oferta, criativo, audiência ou SLA;
- deve ter explicação, não apenas desejo;
- não pode ser o único cenário que sustenta a promessa.

## Fórmulas

```text
leads = investimento / CPL
MQLs = leads * taxa_lead_para_mql
CPMQL = investimento / MQLs
SQLs = MQLs * taxa_mql_para_sql
CPSQL = investimento / SQLs
oportunidades = SQLs * taxa_sql_para_oportunidade
custo_oportunidade = investimento / oportunidades
vendas = oportunidades * taxa_oportunidade_para_venda
receita = vendas * ticket_medio
ROAS = receita / investimento
CAC = investimento / vendas
```

Quando não houver etapa de oportunidade, use:

```text
vendas = SQLs * taxa_sql_para_venda
```

## Campos De Entrada

- `cenario`;
- `budget`;
- `cpl`;
- `taxa_lead_mql`;
- `taxa_mql_sql`;
- `taxa_sql_opp`;
- `taxa_opp_venda`;
- `taxa_sql_venda`;
- `ticket_medio`;
- `meta_leads`;
- `meta_mqls`;
- `meta_sqls`;
- `meta_vendas`;
- `meta_receita`;
- `roas_alvo`;
- `cac_maximo`;
- `capacidade_atendimento`;
- `fonte_premissas`.

## Alertas

### Meta Improvável

Emitir quando apenas o cenário otimista bate a meta principal.

### Budget Insuficiente

Emitir quando nenhum cenário bate meta de vendas, receita ou MQL.

### Capacidade Comercial

Emitir quando leads simulados superam a capacidade de atendimento.

### CAC Inviável

Emitir quando CAC simulado passa do limite máximo ou da margem suportável.

### ROAS Baixo

Emitir quando ROAS fica abaixo do alvo.

### Premissa Fraca

Emitir quando taxa de conversão ou CPL não tem fonte, histórico ou benchmark.

## Sensibilidade Recomendada

Sempre que possível, diga qual variável mais move o resultado:

- CPL;
- taxa lead -> MQL;
- taxa MQL -> SQL;
- taxa final de venda;
- ticket médio;
- budget.

Heurística simples:

- se leads são suficientes, mas MQLs não, gargalo é qualidade/captura;
- se MQLs são suficientes, mas SQLs não, gargalo é qualificação/comercial;
- se SQLs são suficientes, mas vendas não, gargalo é venda/oferta/proposta;
- se vendas existem, mas CAC/ROAS falham, gargalo é unit economics.

## Decisões Recomendadas

- manter plano;
- aumentar budget;
- reduzir meta;
- revisar CPL/canal;
- revisar oferta/LP/formulário;
- melhorar SLA/handoff;
- recalibrar ticket/receita;
- bloquear promessa até obter dados reais.
