# CHANGELOG — diagnostico-travas-scoring

---

## [2.1.0] — 2026-05-07 — MINOR

**Contexto:** Após revisão do output piloto (Alisson Joias), operador Jhonatan Mayer identificou três elementos presentes nas referências de entrega que estavam ausentes na Seção 06 do documento: estrutura de time, pipeline de CRM com critérios objetivos, e justificativa explícita da metodologia de qualificação. Adicionalmente, o modelo de scoring por pontos (BANT 0-40pts) foi substituído por checklist binário — mais simples e operacional para o perfil de times dos clientes Saber.

**O que mudou:**

### Adicionado
- **Estrutura do Time Proposta** (sub-item 4 da Seção 06): tabela com papel / o que faz / perfil ideal / KPI principal + parágrafo sobre lógica da separação de papéis
- **Etapas Sugeridas do CRM** (sub-item 5 da Seção 06): tabela com etapa / critério de entrada / critério de saída / SLA + nota sobre objetividade dos critérios
- **Metodologia de Qualificação com justificativa** (sub-item 6 da Seção 06): 1–2 parágrafos explicando por que a metodologia escolhida (BANT/SPICED/GPPCT/outra) é a mais adequada + por que alternativas foram descartadas
- Checklist binário de qualificação (Sim/Não por critério + ação para cada resposta)
- Tabela de temperatura resultante (HOT/WARM/COLD/DESQUALIFICAR com SLA e próxima ação)
- 6 novos itens na checklist de auto-validação cobrindo os elementos adicionados

### Modificado
- Função da Seção 06: de "apresentar arquitetura de solução" para "apresentar arquitetura completa — metodologia, time, CRM e qualificação"
- Tom da Seção 06: de "elegante, não complexa" para "prático e implementável — não teórico"
- Tabela de framework-chave (item 4 v2.0.0): substituída por estrutura de time + CRM + qualificação (itens 4, 5, 6 v2.1.0)
- Description no frontmatter: atualizada para refletir os novos elementos
- estimated_time: mantido em 4h (complexidade semelhante)

### Não modificado
- Seções 01–05 e 07–09: sem alteração
- Lógica de scores (0–5 por dimensão) e faixas de diagnóstico
- Scorecard ASCII da Seção 04
- Diagrama de cascata causal da Seção 05
- Mapeamento de produtos V4 (Seção 07)
- Plano de 30 dias (Seção 08)
- Custo da inação (Seção 09)

**Evidência de validação:** `clientes/alisson-joias/outputs/diagnostico-travas-scoring.md` — output piloto de referência (a ser atualizado com os novos elementos)

---

## [2.0.0] — 2026-05-07 — MAJOR

**Contexto:** Piloto com Alisson Joias revelou que o output analítico (v1.0.0) não era adequado como entregável ao cliente — o formato de Pergunta Estruturante → Dados → Score → Consolidação Causal é apropriado para uso interno, mas não para leitura pelo CEO/decisor. Operador Jhonatan Mayer solicitou reformulação completa para formato narrativo persuasivo, à semelhança dos materiais de referência de entrega de diagnóstico.

**O que mudou:**

### Adicionado
- **Estrutura narrativa em 9 seções** (obrigatória — não há modo alternativo em v2.0.0):
  - ABERTURA: tese do diagnóstico
  - SEÇÃO 01: A Empresa no Momento Certo (brand story + paradoxo + ASCII chart)
  - SEÇÃO 02: O Que Analisamos (tabela de fontes + credibilidade metodológica)
  - SEÇÃO 03: Cenário Atual em Números (tabelas comparativas + insights-âncora)
  - SEÇÃO 04: As Travas do Crescimento (scoreboard ASCII + narrative + dados + impacto por trava)
  - SEÇÃO 05: A Restrição Maior (explicação didática de TOC + diagrama de cascata ASCII)
  - SEÇÃO 06: O Modelo Comercial que Resolve (As Is vs To Be + arquitetura ASCII)
  - SEÇÃO 07: Os Produtos V4 que Implementam Este Modelo (mapeamento trava → solução → produto)
  - SEÇÃO 08: O Plano N Dias para Destravar (Quick Wins + Estruturais + Gantt ASCII)
  - SEÇÃO 09: O Custo da Inação (modelo financeiro tabular com gap calculado)
  - FECHAMENTO: Os Próximos Passos (3 movimentos narrativos)
- ASCII scoreboard de travas com barras de progresso e faixas de diagnóstico
- ASCII diagrama de cascata causal (Restrição Maior → desbloqueio sequencial)
- ASCII Gantt de 30 dias
- Mapeamento explícito de produtos V4 por trava
- Modelo financeiro de custo da inação (cenário atual vs projetado com gap)
- Instruções de tom por seção (jornalístico / analítico / educacional / propositivo)
- Checklist de auto-validação narrativa (12 itens)

### Modificado
- Output: de `diagnostico-travas-scoring.json` para `diagnostico-travas-scoring.md`
- Estimated_time: de 3h para 4h (documento mais extenso)
- Princípio Central: inclui "o cliente não compra diagnóstico — compra clareza"
- Dependencies: adicionados `analise-crm-receita` e `cliente-oculto`
- Perguntas de apresentação: adaptadas para validação da narrativa (não apenas dos dados)
- Finalização: próximas skills agora explicitam `/deck-entrega-final` e `/plano-de-acao-5w2h`

### Não modificado
- Rigor analítico: scores (0–5 por dimensão), Restrição Maior, sequenciamento causal e impacto financeiro permanecem obrigatórios — integrados na narrativa
- Faixas de diagnóstico: 0–6 crítico / 7–12 moderado / 13–19 funcional / 20–25 bem estruturado
- Teoria das Restrições como princípio de sequenciamento

**Breaking change:** Output não é mais JSON — é um documento Markdown narrativo de 9 seções. Sistemas ou skills que esperavam JSON de `diagnostico-travas-scoring` precisam ser atualizados.

**Evidência de validação:** `clientes/alisson-joias/outputs/diagnostico-travas-scoring.md` (07/05/2026)

---

## [1.0.0] — 2026-04-27

Versão inicial. Formato analítico interno:
- Estrutura por trava: Pergunta Estruturante → Resposta Direta → Dados Tabulados → Análise por Canal → Score 0–5 por dimensão → Mapa Competitivo → Consolidação Causal → Determinação Preliminar
- Consolidação: Resumo de scores → Restrição Maior → Sequenciamento Causal → Impacto Financeiro → Próximos Passos
- Output: `diagnostico-travas-scoring.json`
- Usado como input para `/deck-entrega-final` e `/plano-de-acao-5w2h`
