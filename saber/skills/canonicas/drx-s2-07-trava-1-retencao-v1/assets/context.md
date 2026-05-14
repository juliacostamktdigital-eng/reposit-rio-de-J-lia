# Contexto: Trava 1 — Retenção

> Referência rápida para o consultor durante execução do diagnóstico.

---

## Definição

**Retenção** = capacidade do sistema de manter clientes economicamente ativos e gerar receita recorrente ou repetida ao longo do tempo.

Venda isolada não caracteriza retenção. Retenção implica continuidade intencional.

**Trava 1 ocorre quando:**
- O sistema depende estruturalmente de aquisição constante
- Não existe política formal de continuidade
- A base não sustenta crescimento acumulativo

**Impacto no Throughput:** LTV não sustenta CAC → crescimento exige esforço exponencial de aquisição → empresa nunca acumula base.

**Pergunta estruturante:** *Se a empresa parar de adquirir novos clientes por 90 dias, o faturamento se sustenta?*

---

## Sintomas

| Tipo | Indicadores |
|---|---|
| Quantitativos | Receita recorrente irrelevante; alto % de clientes one-shot; churn elevado ou não medido; LTV próximo ou inferior ao CAC; crescimento dependente exclusivamente de novos clientes |
| Comportamentais | Pós-venda inexistente ou informal; upsell depende de iniciativa individual; cliente não sabe o próximo passo após comprar; sem rotina de acompanhamento |

---

## Referências de Cálculo

**LTV (Life Time Value):**
```
LTV = Ticket Médio × Frequência de Compra × Tempo de Permanência
```
Ou: receita total gerada por cliente no período disponível ÷ nº de clientes.

**Interpretação LTV vs CAC:**
- LTV <= CAC → **retenção crítica** — cada cliente custa mais do que gera
- LTV < 3× CAC → risco estrutural
- LTV > 3× CAC → saudável

---

## Gabarito de Pontuação — Score da Trava 1

| Score | A) Dados Estruturados | B) Receita Recorrente | C) Jornada Pós-Venda | D) Política de Continuidade | E) Expansão |
|---|---|---|---|---|---|
| 0 | Inexistente | Inexistente | Inexistente | Inexistente | Inexistente |
| 1 | Fragmentado | Residual | Reativa | Improviso | Ocasional |
| 2 | Básico sem segmentação | Instável | Pontual | Intenção não formalizada | Pontual |
| 3 | Consistente >= 6 meses | Parcialmente previsível | Definida | Documentada parcialmente | Estruturada básica |
| 4 | Segmentado com coorte | Consistente | Padronizada | Aplicada consistentemente | Estruturada com métricas |
| 5 | Monitorado continuamente | Pilar central | Governada | Política governante | Integrada à estratégia central |

**Atenção:** nota acima de 3 exige evidência formal.

## Interpretação por Faixa

| Total | Interpretação |
|---|---|
| 0–10 | Retenção inexistente. Alta probabilidade de restrição governante. |
| 11–15 | Retenção frágil. Forte dependência de aquisição. |
| 16–20 | Retenção estruturada, com lacunas. |
| 21–25 | Retenção madura e governável. |

---

## Consolidação Causal — Formato

*"A empresa opera sob a política implícita de ___, gerando ___, limitando o crescimento cumulativo."*

Evitar causas operacionais superficiais.

---

## Critério de Governância

Trava 1 é **potencial governante** quando:
- Score <= 15 **E**
- LTV limita crescimento **E**
- Resolver retenção aumenta Throughput mais do que aquisição

Validação final: CRT.
