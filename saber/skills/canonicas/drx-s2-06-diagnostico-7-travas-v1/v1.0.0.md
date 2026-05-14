---
slug: drx-s2-06-diagnostico-7-travas-v1
description: "name: Diagnóstico das 7 Travas (Orquestrador)"
name: Diagnóstico das 7 Travas (Orquestrador)
status: draft-v1

---

# Diagnóstico das 7 Travas — Orquestrador

## Descrição
Orquestra o diagnóstico completo das 7 travas do sistema de receita do cliente, coordenando a execução das 7 skills individuais (Trava 1 a Trava 7), decidindo a ordem adequada e consolidando as saídas em uma visão única de sistema.

Ativar quando o consultor quiser conduzir o diagnóstico completo das travas de uma vez, ou quando for preciso reorientar uma execução parcial em andamento.

## Quando Usar
- Triggers: "diagnóstico das 7 travas", "rodar todas as travas", "diagnosticar travas do cliente", "consolidar travas", "visão geral das travas"
- **NÃO usar quando:**
  1. O Master Contexto ainda não foi gerado — sem ele, nenhuma trava tem insumo mínimo
  2. O consultor quer rodar uma única trava específica — nesse caso, use diretamente a skill `drx-s2-NN-trava-X-*`
  3. O Mapeamento de Fluxo de Receita não existe — a Trava 1 depende do funil mapeado

## Inputs Necessários
1. **context/business.md** — modelo de negócio, revenue streams, capacidade
2. **context/gtm.md** — canais, funil, ICP, ciclo de vendas, mercado
3. **context/constraints.md** — restrições, UDEs, diagnóstico de trava
   *(ler apenas o(s) arquivo(s) relevante(s) para esta skill — ver tabela acima)*
4. **Mapeamento do Fluxo de Receita** (output de `drx-s2-05-fluxo-receita-v1`) — para dimensionar cada trava no funil
5. **Análise de Funil CRM** (se disponível) — dados quantitativos de conversão

## Processo de Execução

### 1. Determinar a ordem de execução
A ordem recomendada inverte o funil (da trava mais próxima do resultado até a mais distante), pois cada trava resolvida melhora o sinal da próxima:

```
Trava 1 (Retenção) → Trava 2 (Decisão) → Trava 3 (Compromisso) →
Trava 4 (Qualificação) → Trava 5 (Interesse) → Trava 6 (Atenção) → Trava 7 (Exposição)
```

Exceções:
- **Negócio em early stage / baixo volume:** começar por Trava 6-7 (Exposição/Atenção) — sem topo, não há o que analisar embaixo
- **Negócio maduro com churn alto:** reforçar Trava 1 primeiro — retenção é prioridade absoluta

### 2. Executar cada trava sequencialmente
Para cada trava (1 a 7):
1. Invocar a skill correspondente (`drx-s2-07-trava-1-retencao-v1` ... `drx-s2-13-trava-7-exposicao-v1`)
2. Coletar os outputs esperados: severidade (alta/média/baixa), evidência quantitativa, hipóteses de causa
3. Validar com o consultor antes de avançar para a próxima

### 3. Consolidar saídas
Ao final das 7 execuções, montar uma tabela-resumo:

| Trava | Nome | Severidade | Evidência principal | Hipótese de causa | Input para CRT |
|---|---|---|---|---|---|
| 1 | Retenção | [alta/média/baixa] | [métrica] | [hipótese] | [sim/não] |
| ... | ... | ... | ... | ... | ... |

### 4. Identificar a trava dominante (candidata)
Regra: a **trava de maior severidade com maior impacto financeiro no fluxo de receita** é candidata a trava dominante do sistema. Não declarar dominante ainda — isso é feito na CRT (Semana 3).

## Outputs Esperados
- 7 documentos individuais por trava (um por skill executada)
- Tabela consolidada de severidade e evidências
- Lista priorizada de travas candidatas à trava dominante

## Riscos
- ⚠️ Executar todas as 7 travas sem validar entre elas pode gerar inconsistência quando uma trava alimenta dados da outra
- ⚠️ Não usar esta orquestração como substituto da CRT — a trava dominante é confirmada lá, não aqui
