# Context — plano-de-acao-5w2h

## Identidade

**Nome:** plano-de-acao-5w2h
**Agente owner:** ceo
**Status:** incubação
**Versão atual:** 2.0.0

---

## Histórico de Versões

| Versão | Data | Tipo de mudança | Resumo |
|--------|------|-----------------|--------|
| 1.0.0 | 2026-04-25 | — | Versão inicial — plano tático 5W2H puro |
| **2.0.0** | **2026-05-07** | **MAJOR** | **Adição de Camada Estratégica obrigatória em POP 8.3: avaliação de metodologia (BANT/SPICED/MEDDIC), estrutura de time (Hunter/Farmer/SDR/Closer), canal de atendimento e automação. Tabela As Is vs To Be como pré-requisito do plano tático.** |

---

## Contextos de Aplicação

| POP | Módulo | Camada Estratégica |
|-----|--------|-------------------|
| 4.4 | Mídia | Opcional |
| 5.4 | Criativos/Social | Opcional |
| 6.4 | CRO/LP | Opcional |
| 8.3 | Comercial | **Obrigatória** |

---

## Decisões de Design

**Por que duas camadas?**
O plano tático (5W2H) prescreve ações dentro do modelo atual. Sem antes avaliar se o modelo (metodologia, estrutura, canal, automação) é o correto, o risco é executar bem a coisa errada. A separação "estratégia → tática" evita esse anti-padrão.

**Por que obrigatório só em POP 8.3?**
O processo comercial tem mais variáveis de modelo (perfil de time, metodologia, canal, automação) do que os outros módulos. Mídia e CRO têm gargalos mais localizados onde o plano tático já é suficiente. Em POP 8.3, ignorar o modelo é ignorar a causa raiz.

**Por que BANT e não SPICED ou MEDDIC?**
BANT é adequado para o perfil majoritário dos clientes V4 Saber: B2C ou B2B de ciclo curto, canal WhatsApp, decisão 1-2 pessoas. SPICED e MEDDIC são mapeados na skill mas não são o default — o operador escolhe com base no diagnóstico.

---

## Evidência de Validação

**Piloto:** Alisson Joias — 07/05/2026
**Operador:** Jhonatan Mayer
**Diagnósticos de entrada:** diagnostico-comercial-crm · cliente-oculto · analise-crm-receita
**Output gerado:** `clientes/alisson-joias/outputs/plano-de-acao-comercial.md`
**Feedback do operador:** Output v1 (tático puro) rejeitado por ser "lista de tarefas" sem dimensão estratégica. Output v2 (duas camadas) aprovado.

---

## Dependências

- `diagnostico-comercial-crm` — fornece perfil Hunter/Farmer, gaps de CRM, LRT, processo declarado vs real
- `cliente-oculto` — fornece nota de atendimento por critério (C1-C7), pontos críticos e fortes
- `analise-crm-receita` — fornece Win Rate por canal, ticket médio, sazonalidade (opcional mas recomendado em POP 8.3)

## Próxima skill (POP 8.3)

`diagnostico-travas-scoring` — consolida outputs de todos os módulos, identifica Restrição Maior (sequência causal), pontua dimensões 0-5 e prepara o deck de entrega final.
