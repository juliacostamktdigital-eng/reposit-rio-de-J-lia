# Referência TAM / SAM / SOM

Fonte normativa: `assets/canonicos/12_BENCHMARK_MERCADO_TAM_SAM_SOM_CANONICO.md` (seção 6.2).

## Erros Comuns (evitar)

- usar SAM como SOM;
- inventar participação de mercado sem base;
- ignorar capacidade operacional;
- ignorar budget e CPL na captura aquisitável;
- começar sizing sem contexto mínimo de segmento e ticket.

## Tabela Obrigatória SOM

| Variável | Valor | Fonte |
| --- | --- | --- |
| Capacidade operacional | clientes/projetos/mês | cliente/operação |
| Budget mensal de aquisição | R$/mês | cliente/operação |
| CPL ou custo de oportunidade estimado | R$ | histórico/benchmark |
| Leads/mês possíveis | budget / CPL | cálculo |
| Taxa de conversão estimada | % | histórico/benchmark |
| Clientes/mês capturáveis | min(capacidade, leads × conversão) | cálculo |
| Faturamento potencial/mês | clientes × ticket | cálculo |
| SOM anual | faturamento/mês × 12 | cálculo |

## N2 (benchmark global)

Para o pacote institucional completo, N2 exige TAM/SAM/SOM com fontes ou premissas explícitas, SOM limitado por capacidade e budget, e incertezas documentadas (ver playbook seção 10.2).

## Relação Com Outras Skills

- `benchmark-campo-batalha-gtm` fornece contexto e benchmarks de CPL/comportamento;
- `posicionamento-competitivo-beachhead` usa sizing para escolher recorte inicial;
- `plano-midia-leadgen` e `simulador-cenarios-midia-funil` consome premissas de conversão e budget.
