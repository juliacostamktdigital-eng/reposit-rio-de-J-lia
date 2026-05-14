# Context — ee-s4-diagnostico-comercial

## Identidade

**Nome:** ee-s4-diagnostico-comercial
**Status:** ativa
**Versão atual:** 1.2.0

---

## Histórico de Versões

| Versão | Data | Tipo | Resumo |
|--------|------|------|--------|
| 1.0.0 | 2026-01-01 | — | Versão inicial — funil + objeções + qualificação + plano de ação. Output JSON |
| 1.1.0 | 2026-05-07 | MINOR | Escopo redefinido como diagnóstico puro. Removidos: objeções, qualificação, plano de ação. Output .md. Benchmarks com refs inline |
| **1.2.0** | **2026-05-07** | **MINOR** | **Hierarquia de fontes Tier 1/Tier 2. Kick-off/briefing não geram conclusões diagnósticas. Hunter/Farmer exige dado quantitativo** |

---

## Contextos de Aplicação

| Contexto | Uso | Observações |
|----------|-----|-------------|
| POP Semana 4 — início | **Principal** | Primeira skill diagnóstica da semana — alimenta `/analise-crm-receita` e `/ee-s4-cliente-oculto` |
| Input para `/diagnostico-travas-scoring` | **Obrigatório** | Score de processo (dimensão T2) depende deste output |

---

## Decisões de Design

**Por que hierarquia Tier 1 / Tier 2?**
Diagnóstico baseado em percepção do gestor sobre o próprio processo tem viés sistemático: o gestor descreve o processo ideal, não o real. Dados de CRM, transcrições reais e cliente oculto mostram o que realmente acontece. A hierarquia formaliza essa distinção — tornando obrigatório citar a fonte e marcar quando só há Tier 2 disponível.

**Por que Hunter/Farmer exige dado quantitativo?**
A distinção Hunter (prospecção ativa) / Farmer (gestão de carteira) era frequentemente classificada por perfil declarado do vendedor ou percepção do gestor — fontes Tier 2 que raramente correspondiam aos dados reais. A regra de exigir Win Rate por canal de origem ou por consultora força o diagnóstico a se basear em comportamento observado, não em autopercepção.

**Por que o plano de ação foi removido?**
O plano de ação pertence a `/plano-de-acao-5w2h`. Manter os dois no mesmo documento criava confusão de escopo e output denso — o cliente via diagnóstico e plano misturados, sem a clareza de "aqui está o problema, aqui está o que faremos". Separar gera dois documentos distintos com funções distintas.

---

## Evidência de Validação

**Piloto:** Alisson Joias — 07/05/2026
**Operador:** Jhonatan Mayer
**Output gerado:** `saber/clientes/alisson-joias/outputs/ee-s4-diagnostico-comercial.md`
