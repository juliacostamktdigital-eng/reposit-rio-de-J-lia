# CHANGELOG — plano-de-acao-5w2h

---

## [2.0.0] — 2026-05-07 — MAJOR

**Contexto:** Piloto com Alisson Joias revelou que o output tático puro (v1.0.0) era percebido como "lista de tarefas" — prescreve ações dentro do modelo vigente sem questionar se o modelo é o correto. Operador Jhonatan Mayer solicitou adição de dimensão estratégica antes do plano tático.

**O que mudou:**

### Adicionado
- **Parte 1 — Camada Estratégica** (obrigatória em POP 8.3, opcional nos demais):
  - 1.1 Avaliação de Metodologia de Vendas (BANT / SPICED / MEDDIC / Consultiva)
  - 1.2 Avaliação de Estrutura do Time (Hunter / Farmer / SDR / Closer)
  - 1.3 Avaliação de Canal de Atendimento (WhatsApp / Telefone / Email / Presencial)
  - 1.4 Auditoria de Automação (estado atual + modelo de 3 funis)
  - 1.5 Tabela As Is vs To Be consolidada por dimensão
- Coluna "Camada Estratégica" na tabela de Contexto de Aplicação
- Perguntas de apresentação específicas para a camada estratégica
- Checklist de auto-validação da camada estratégica (4 itens)
- Output renomeado para `plano-de-acao-comercial.md` em POP 8.3

### Modificado
- Finalização POP 8.3: próxima skill agora é `/diagnostico-travas-scoring` (antes: `/gtm-priorizacao-canais`)
- Princípio Central atualizado: inclui "modelo certo antes de execução certa"
- Matriz de Priorização: adicionada coluna "Nível" (Estratégico / Tático) para diferenciar ações

### Não modificado
- Parte 2 (Plano Tático 5W2H): estrutura, formatos e lógica de Quick Wins / Estrutural / Recorrentes mantidos intactos
- Contextos POP 4.4, 5.4 e 6.4: sem alteração de comportamento

**Breaking change:** Output em POP 8.3 agora tem duas partes — operadores que esperavam apenas o 5W2H receberão a Avaliação Estratégica primeiro.

**Evidência de validação:** `clientes/alisson-joias/outputs/plano-de-acao-comercial.md` (07/05/2026)

---

## [1.0.0] — 2026-04-25

Versão inicial. Plano tático 5W2H puro:
- Consolidação de gaps dos diagnósticos
- Matriz de priorização (Quick Win / Estrutural / Moderado / Não entra)
- Plano 5W2H por ação (O quê / Por quê / Quem / Quando / Onde / Como / Quanto / Métrica)
- Resumo executivo
- Apêndice de estrutura de blocos de LP (POP 6.4)
- 4 contextos de aplicação (POP 4.4 / 5.4 / 6.4 / 8.3)
