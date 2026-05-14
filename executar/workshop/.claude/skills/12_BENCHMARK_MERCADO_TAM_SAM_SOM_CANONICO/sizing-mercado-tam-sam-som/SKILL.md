---
name: sizing-mercado-tam-sam-som
description: Dimensiona TAM, SAM e SOM com fontes, filtros, premissas e tabela de capacidade vs. budget, calculando leads/mês, clientes capturáveis e receita obtível antes de DEOC e plano de mídia. Use após contexto de mercado e handoff, quando precisar número defendável de oportunidade real e teto de captura.
---

# Sizing Mercado TAM SAM SOM

## Quando Usar

Use quando o time precisar separar **mercado total**, **mercado atendível** e **captura viável** com capacidade e budget atuais.

Não confundir SAM com SOM nem assumir captura sem teto operacional ou financeiro.

## Princípio Canônico

```text
SOM = menor valor entre potencial de mercado, capacidade operacional e aquisição viável com budget atual.
```

Na prática, o script calcula o vínculo **budget → leads → conversão → clientes/mês**, limitado pela **capacidade operacional**, e projeta receita mensal e anual a partir do ticket.

## TAM

Deve conter:

- valor em BRL ou USD;
- escopo geográfico;
- fonte;
- ano da fonte;
- método usado;
- intervalo de incerteza, se estimado.

## SAM

Deve conter:

- filtros aplicados (geografia, nicho, ICP, produto, canal);
- justificativa dos filtros;
- fontes ou premissas;
- valor final;
- exclusões explícitas.

## SOM

Registrar a **tabela obrigatória** (variável, valor, fonte) e os campos calculados quando houver inputs numéricos.

## Inputs Operacionais

- segmento e geografia;
- ticket médio ou faixa;
- fontes de mercado para TAM/SAM;
- capacidade operacional (clientes/projetos por mês);
- budget mensal de aquisição;
- CPL ou custo de oportunidade estimado;
- taxa de conversão estimada (lead → cliente).

## Workflow

1. Documente TAM com fonte e método.
2. Derive SAM aplicando filtros e exclusões com justificativa.
3. Preencha variáveis de SOM (capacidade, budget, CPL, conversão, ticket).
4. Execute o script ou calcule manualmente a tabela.
5. Declare incertezas e cenários (conservador/provável) se necessário.

## Output Esperado

- bloco TAM/SAM/SOM com premissas;
- tabela SOM preenchida;
- valores calculados: leads/mês, clientes/mês, faturamento/mês, SOM anual;
- notas sobre limites do modelo.

Use `templates/tam-sam-som.md`.
Use `templates/tam-sam-som.json` com o script para recalcular e gerar Markdown.

## Script Utilitário

```bash
python3 scripts/calculate_tam_sam_som.py templates/tam-sam-som.json --md /tmp/tam-sam-som.md --csv /tmp/tam-sam-som-tabela.csv
```

## Definition Of Done

- TAM e SAM têm fonte ou premissa explícita.
- SOM considera capacidade **e** budget, não só tamanho de mercado.
- Nenhuma linha crítica do playbook foi omitida sem marcar N/A justificado.
- Números sensíveis têm intervalo ou cenário quando aplicável.
