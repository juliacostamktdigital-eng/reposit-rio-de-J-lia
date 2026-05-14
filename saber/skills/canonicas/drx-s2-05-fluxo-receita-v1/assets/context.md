# Contexto: Mapeamento do Fluxo de Receita — DR-X

> Referência para o consultor durante execução. Contém conceitos, critérios de interpretação e lógica TOC aplicada ao diagnóstico.

---

## O que é Fluxo de Receita

O fluxo de receita é o caminho que o dinheiro percorre desde a geração de demanda até o reconhecimento de receita. Inclui todos os processos comerciais, operacionais e financeiros que impactam o caixa e o throughput.

**Mapear o fluxo serve para:**
- Identificar onde o sistema perde dinheiro (alta saída de leads/pedidos)
- Identificar onde o dinheiro fica travado (tempo alto entre etapas)
- Identificar qual etapa limita o resultado global (restrição)

---

## Etapas Típicas do Fluxo

| Etapa | O que acontece | O que pode travar |
|---|---|---|
| Geração de demanda | Leads entram no sistema | Volume insuficiente, qualidade ruim |
| Qualificação | Leads são filtrados | Sem critérios, CAC alto |
| Venda | Proposta e fechamento | Ciclo longo, baixa conversão |
| Entrega | Produto/serviço entregue | Gargalo operacional, retrabalho |
| Faturamento | Nota emitida | Atraso burocrático |
| Recebimento | Dinheiro entra no caixa | Inadimplência, prazo longo |

---

## Lógica TOC aplicada ao Fluxo

**Throughput** = taxa na qual o sistema gera dinheiro através das vendas.

**Perguntas estruturantes durante o mapeamento:**
- Onde o dinheiro fica parado mais tempo?
- Qual etapa, se melhorada, destravaria o sistema inteiro?
- O problema é falta de demanda ou incapacidade de conversão/entrega?
- O fluxo cresce de forma linear ou aos trancos?

**Ponto de acúmulo = candidato a restrição.** Onde leads, pedidos ou tarefas se acumulam aguardando processamento é onde a restrição provavelmente está.

---

## Dependências — o que observar

| Tipo | Exemplos de impacto |
|---|---|
| Entre pessoas | Aprovação de um gestor trava toda a etapa |
| Entre áreas | Comercial fecha, operacional não tem capacidade |
| Entre sistemas | CRM não integrado com faturamento gera retrabalho |

---

## Saída esperada do diagnóstico

Ao final do mapeamento, o consultor deve ter:
1. Fluxo documentado como **realmente acontece** — não como deveria ser
2. Pelo menos 1 ponto de acúmulo ou gargalo identificado com evidência
3. Hipóteses iniciais de restrição para validação na CRT
