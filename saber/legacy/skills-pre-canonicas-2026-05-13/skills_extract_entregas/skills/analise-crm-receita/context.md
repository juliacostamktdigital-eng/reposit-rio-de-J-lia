# Context — analise-crm-receita

## Identidade

**Nome:** analise-crm-receita
**Status:** ativa
**Versão atual:** 1.1.0

---

## Histórico de Versões

| Versão | Data | Tipo | Resumo |
|--------|------|------|--------|
| 1.0.0 | 2026-01-01 | — | Versão inicial — output JSON, sem checks de qualidade |
| **1.1.0** | **2026-05-07** | **MINOR** | **Output .md, CHECK 0 + CHECK 0.5 obrigatórios, cobertura explícita de análises não executáveis** |

---

## Contextos de Aplicação

| Contexto | Uso | Observações |
|----------|-----|-------------|
| POP Semana 4 — Consolidação | **Principal** | Fornece Win Rate, ticket médio e concentração de receita para `/diagnostico-travas-scoring` |
| Diagnóstico de ICP real vs declarado | **Suplementar** | Cruza output de `/definicao-icp-b2b` com dados reais do CRM |

---

## Decisões de Design

**Por que CHECK 0 antes das análises?**
Em PMEs, dados de CRM são frequentemente mal preenchidos (campos em branco, valores placeholder de R$1, segmentos inconsistentes). Iniciar análises sem auditoria de qualidade gera conclusões baseadas em dados ruins — que o consultor vai defender diante do cliente sem saber que a base era falha.

**Por que CHECK 0.5 (distorção oculta)?**
O CHECK 0 detecta ausências óbvias. O CHECK 0.5 detecta dados que parecem completos mas estão distorcidos — como Omie exportando apenas NFs sem funil, ou inativos de 3 anos contaminando o Win Rate. Esta camada de verificação foi adicionada após o piloto Alisson Joias, onde o Win Rate de Meta Ads (0,29%) só foi confirmado após identificar que o export incluía leads de 14 meses sem distinção de data.

**Por que análises não executáveis devem aparecer no .md?**
O operador precisa saber o que não foi possível analisar e por quê — para coletar os dados na próxima rodada. Um .md que silencia análises não executáveis parece completo mas esconde buracos que o cliente vai perguntar na apresentação.

**Por que output .md e não .json?**
O output é um documento consultivo lido por humano (operador + cliente). JSON era adequado para consumo por outras skills, mas o `.md` com tabelas e seções narrativas é mais adequado para revisão e entrega direta.

---

## Evidência de Validação

**Piloto:** Alisson Joias — 07/05/2026
**Operador:** Jhonatan Mayer
**Output gerado:** `saber/clientes/alisson-joias/outputs/analise-crm-receita.md`
