# Context — diagnostico-travas-scoring

## Identidade

**Nome:** diagnostico-travas-scoring
**Agente owner:** especialista-gtm-comercial
**Status:** ativa
**Versão atual:** 2.0.0

---

## Histórico de Versões

| Versão | Data | Tipo de mudança | Resumo |
|--------|------|-----------------|--------|
| 1.0.0 | 2026-04-27 | — | Versão inicial — formato analítico interno (Pergunta → Dados → Score → Consolidação Causal). Output: JSON |
| 2.0.0 | 2026-05-07 | MAJOR | Reformulação para entregável narrativo de 9 seções. Storytelling persuasivo para entrega ao cliente. ASCII charts, diagramas de cascata, modelo financeiro de inação, mapeamento de produtos V4. Output: MD |
| **2.1.0** | **2026-05-07** | **MINOR** | **Seção 06 expandida: estrutura de time proposta, etapas do CRM com critérios objetivos de entrada/saída, metodologia de qualificação com justificativa explícita (BANT/SPICED/GPPCT), checklist binário Sim/Não substituindo scoring por pontos** |

---

## Contextos de Aplicação

| Contexto | Uso | Observações |
|----------|-----|-------------|
| POP Semana 4 — Consolidação | **Principal** | Concatena todos os diagnósticos das semanas anteriores |
| Entrega Final ao cliente | **Documento base** | Fonte primária para `/deck-entrega-final` |
| Pré-plano de ação | **Obrigatório** | Seção 08 alimenta `/plano-de-acao-5w2h` |

---

## Decisões de Design

**Por que formato narrativo e não analítico?**
O formato analítico (v1.0.0) foi validado internamente mas rejeitado como entregável ao cliente — percebido como "relatório técnico", não como diagnóstico que o CEO consegue apropriar. A mudança para narrativa resolve: o cliente lê, entende e sente como verdadeiro, sem precisar de mediação do consultor para interpretar.

**Por que 9 seções nessa ordem?**
A sequência segue o arco narrativo persuasivo: empatia (Seção 01) → credibilidade (02) → realidade (03) → problema (04) → causa raiz (05) → solução (06) → implementação (07) → plano (08) → urgência (09). Inverter a ordem (ex: começar com problemas antes de empatia) reduz a receptividade do cliente.

**Por que o rigor analítico permanece embutido?**
Narrativa sem dados é impressão. O diagnóstico precisa de scores, Restrição Maior e impacto financeiro — mas integrados na história, não como seções técnicas separadas que interrompem o fluxo de leitura.

**Por que checklist binário e não scoring por pontos?**
Scoring (0-10 por critério, total 0-40) exige calibração — "quanto vale Budget forte? 8 ou 9?" — o que cria inconsistência entre atendentes. Binário elimina ambiguidade: ou tem ou não tem. A temperatura resultante (HOT/WARM/COLD) é derivada do número de critérios atendidos, não de uma soma ponderada. Para times sem treinamento formal em metodologia de vendas, binário é mais aderente à prática real.

**Por que justificar a escolha da metodologia no próprio documento?**
O cliente precisa entender não apenas o que fazer, mas por que aquele framework e não outro. A justificativa explícita de "por que BANT e não SPICED" serve dois propósitos: (1) demonstra domínio consultivo, e (2) aumenta a adoção — time que entende o motivo segue com mais rigor do que time que apenas executa.

**Por que critérios de entrada/saída do CRM precisam ser objetivos?**
Critérios subjetivos ("lead qualificado", "cliente em negociação") criam funis diferentes para cada vendedor — impossível mensurar ou gerenciar. Critério objetivo ("enviou orçamento por escrito") é verificável por qualquer pessoa, permite SLA e permite diagnóstico de pipeline real.

**Por que incluir produtos V4 no diagnóstico?**
O momento de maior receptividade para posicionar solução é após a narrativa de resolução (Seção 06), quando o cliente já aceita o modelo proposto. Inserir V4 como "implementadores do modelo" — não como vendedores — é a diferença entre consultoria e pitch.

**Por que ASCII e não imagens?**
O output é Markdown. ASCII charts, diagramas e Gantts são renderizáveis em qualquer leitor de MD, versionáveis em git, e conversíveis para slides via `/deck-entrega-final`. Dependência de imagens externas cria fricção na geração e na manutenção.

**Por que output .md e não .json?**
v1.0.0 gerava JSON para consumo interno por outras skills. Em v2.0.0 o output é o próprio documento de entrega — lido por humano, não por máquina. Skills que precisam de dados estruturados (ex: metadados de travas) devem extrair do MD ou de outputs analíticos anteriores.

---

## Evidência de Validação

**Piloto:** Alisson Joias — 07/05/2026
**Operador:** Jhonatan Mayer
**Inputs utilizados:** CSV de acompanhamento (13 meses), Screenshots CRM Kommo, Transcrição Kick-Off, Auditoria de Cliente Oculto
**Output gerado:** `clientes/alisson-joias/outputs/diagnostico-travas-scoring.md`
**Feedback:** Output v1 (analítico) percebido como "muito técnico para entrega ao cliente". Output v2 (narrativo) aprovado.

---

## Dependências

- `diagnostico-comercial-crm` — perfil Hunter/Farmer, gaps de processo, estado do CRM
- `analise-crm-receita` — funil por etapa, Win Rate, ticket médio, sazonalidade
- `cliente-oculto` — nota de atendimento por critério, pontos críticos e fortes
- `diagnostico-meta-ads` — CPL, taxa de conversão pago, volume e qualidade de leads pagos

## Próximas Skills (ordem de uso)

1. `/deck-entrega-final` — transforma o MD narrativo em slides de apresentação
2. `/plano-de-acao-5w2h` — aprofunda a Seção 08 em plano tático detalhado com 5W2H
