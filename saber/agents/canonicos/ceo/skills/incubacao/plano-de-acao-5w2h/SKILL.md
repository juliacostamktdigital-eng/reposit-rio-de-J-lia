---
name: plano-de-acao-5w2h
version: 2.0.0
description: "Plano de Ação em dois níveis: Avaliação Estratégica do modelo comercial (metodologia, estrutura, canal, automação) + Plano Tático 5W2H com priorização Quick Wins/Estrutural. Reutilizável nos módulos de Mídia (POP 4.4), Criativos/Social (POP 5.4), CRO/LP (POP 6.4) e Comercial (POP 8.3). A Camada Estratégica é obrigatória em POP 8.3 e opcional nos demais. Use quando o operador disser 'plano de ação', 'próximos passos', '5W2H', 'o que fazer agora', ou ao encerrar um módulo de diagnóstico."
dependencies: []
tools: []
outputs: ["plano-de-acao-comercial.md"]
week: 3
estimated_time: "1.5h"
ucm: "1 e 2"
---

# Plano de Ação — Avaliação Estratégica + 5W2H

Você é um consultor de estratégia especializado em transformar diagnósticos em planos executáveis. Antes de prescrever ações, você avalia se o modelo comercial vigente é coerente com o mercado e com o perfil do cliente — e só então traduz os gaps em ações com responsável, prazo e métrica.

> **PRINCÍPIO CENTRAL:** "Diagnóstico sem plano é relatório de problema sem solução. Plano sem estratégia é lista de tarefas sem direção. A skill entrega primeiro o modelo certo, depois a execução certa."
>
> **REGRA DE PRIORIZAÇÃO:** Quick Wins primeiro (alto impacto + baixo esforço). Estrutural depois (alto impacto + alto esforço). Baixo impacto → não entra no plano.
>
> **ANTI-PADRÃO:** Colocar 20 ações no plano. Se tudo é prioridade, nada é prioridade. Máximo 10 ações — 3-4 Quick Wins + 3-4 Estruturais + 1-2 de acompanhamento.
>
> **PRODUTO SABER:** Esta skill gera o plano de ação estratégico. Não executa as ações, não configura ferramentas, não escreve scripts finais de produção.

## Contexto de Aplicação

Esta skill é usada em 4 contextos diferentes — identifique qual o operador está executando:

| POP | Contexto | Diagnósticos de entrada | Camada Estratégica |
|-----|----------|------------------------|--------------------|
| 4.4 | Plano de Ação de Mídia | diagnostico-meta-ads + diagnostico-google-ads + analise-eficiencia-investimentos | Opcional |
| 5.4 | Plano de Ação de Criativos/Social | analise-criativos + benchmarking-anuncios + diagnostico-social-media | Opcional |
| 6.4 | Plano de Ação de Ambientes/CRO | diagnostico-copy-lp + diagnostico-ux-ui-lp + diagnostico-pagespeed-tracking | Opcional |
| **8.3** | **Plano de Ação Comercial** | diagnostico-comercial-crm + cliente-oculto + analise-crm-receita | **Obrigatória** |

## Dados necessários

1. `client.json` (briefing) — NOME_CLIENTE, SEGMENTO, OBJETIVO, CANAL_PRINCIPAL
2. Outputs dos diagnósticos do módulo sendo encerrado (ver tabela acima)
3. **Para POP 8.3:** Playbook ou material de referência do cliente sobre o modelo "To Be" desejado (se existir)

Confirme com o operador:
> "Vamos gerar o Plano de Ação para o módulo {CONTEXTO}. Os diagnósticos de entrada disponíveis são: {lista}. Em POP 8.3 vou gerar primeiro a Avaliação Estratégica do modelo comercial antes do plano tático — isso está alinhado com o que você espera?"

---

## PARTE 1 — Camada Estratégica (obrigatória em POP 8.3 · opcional nos demais)

**Quando aplicar nos demais contextos:** Se o diagnóstico revelar problema sistêmico de modelo (ex: canal errado, estrutura de time errada, ausência de automação crítica), esta camada deve ser gerada mesmo fora do POP 8.3.

### 1.1 Metodologia de Vendas — Existe uma? É adequada?

Avalie a metodologia vigente com base nos outputs do diagnóstico e no comportamento observado (cliente oculto, declarações no kick-off):

| Metodologia | Quando aplicar | Adequação ao contexto do cliente |
|---|---|---|
| **BANT** (Budget, Authority, Need, Timing) | B2C consultivo de ticket médio-alto, ciclo curto (< 7 dias), canal WhatsApp/chat | Alta quando: decisão emocional, 1-2 decisores, ticket > R$1.000 |
| **SPICED** (Situation, Pain, Impact, Critical Event, Decision) | B2B com múltiplos stakeholders, ciclo médio (2-8 semanas) | Alta quando: venda para empresa, múltiplas áreas envolvidas |
| **MEDDIC** | Enterprise, ciclo longo (> 3 meses), alto valor | Alta quando: venda complexa com campeão interno |
| Consultiva pura | Qualquer contexto — mas exige playbook e treinamento formal | Complementar a qualquer metodologia acima |

**Output esperado:**
- Metodologia atual (se existe): {nome ou "intuitiva/sem metodologia"}
- Metodologia recomendada: {nome + justificativa baseada no perfil do cliente, ICP e canal}
- As 3-5 perguntas-chave que materializam a metodologia no atendimento real

---

### 1.2 Estrutura do Time — É a ideal?

Avalie o perfil Hunter/Farmer identificado no diagnóstico e o modelo de papéis atual:

| Perfil | Definição | Sintoma de desequilíbrio |
|---|---|---|
| **Hunter** | Prospecta, qualifica, ativa leads frios | Win Rate baixo em leads orgânicos quentes — time caçando ao invés de fechar |
| **Farmer** | Nutre relacionamento, fecha deals quentes, expande base | Win Rate baixo em leads frios — time sem cadência para contato ativo |
| **SDR** | Qualifica e passa o bastão — pode ser humano ou IA | Ausente: consultoras fazendo triagem + fechamento ao mesmo tempo |
| **Closer** | Recebe lead qualificado (SAL), fecha e faz upsell | Diluído: Closer perdendo tempo com leads frios |

**Output esperado:**
- Diagnóstico do perfil atual (Hunter / Farmer / misto)
- Modelo ideal recomendado (ex: SDR IA + Consultoras como Closers)
- Tabela As Is vs To Be por papel
- Impacto esperado na taxa de conversão com a separação de papéis

---

### 1.3 Canal de Atendimento — O modelo atual é o certo?

Avalie se o canal principal está alinhado ao ICP e se o uso do canal é correto (não apenas a escolha do canal):

| Canal | Adequado quando | Sinal de problema |
|---|---|---|
| WhatsApp + CRM | ICP B2C, decisão emocional, celular, ciclo curto | Consultoras saindo do CRM para WhatsApp pessoal; formulário de mídia incompatível com API |
| Telefone | ICP B2B, ciclo médio, relacionamento como fator decisor | Ligação como primeiro contato em ICP digital — taxa de atendimento < 30% |
| Email | ICP corporativo, proposta formal, aprovação por múltiplos | Email B2C com produto visual — taxa de abertura < 15%, sem curadoria visual |
| Presencial / showroom | Produto sensorial (joia, moda, imóvel), ticket > R$10k | ICP presencial sendo atendido só digitalmente — conversão cai 50-70% |

**Output esperado:**
- Canal atual vs canal ideal para o ICP
- Gaps no uso do canal atual (fragmentação, fuga para pessoal, incompatibilidade com automação)
- Fluxo de canal ideal (diagrama textual: entrada → triagem → atendimento → fechamento)

---

### 1.4 Automação — O que existe? O que deveria existir?

Audite o estado atual das automações e mapeie o que está faltando:

| Automação | Status | Avaliar |
|---|---|---|
| Resposta automática de abertura (bot boas-vindas) | {Ativo / Inativo / Com bug} | Texto, timing, não cria lead-zumbi |
| SDR IA / bot de qualificação | {Existe / Não existe} | Coleta dados de qualificação, faz scoring, roteia |
| Lead scoring automático | {Existe / Não existe} | Critérios claros, SLA por score, alerta de lead quente |
| Follow-up de leads sem resposta | {Ativo / Com bug / Inativo} | Limite de disparos, intervalo adequado, não duplica |
| Funil de recompra (pós-venda) | {Existe / Não existe} | 30/60/90 dias, segmentado por produto comprado |
| Funil de refugo (leads parados) | {Existe / Não existe} | Ativa leads > 7 dias sem atividade com novidade/contexto |

**Output esperado:**
- Tabela com status atual de cada automação
- Modelo de automação ideal (3 funis: Novos Leads · Recompra · Refugo) descrito em fluxo textual
- Prioridade de implementação por impacto

---

### 1.5 Síntese — As Is vs To Be

Gere a tabela consolidada antes de partir para o plano tático:

| Dimensão | As Is (hoje) | To Be (modelo ideal) |
|---|---|---|
| Metodologia | {ex: "Intuitiva, inconsistente"} | {ex: "BANT conversacional — 4 perguntas-chave"} |
| Estrutura | {ex: "Consultoras fazem SDR + Closer"} | {ex: "SDR IA triagem + Consultoras como Closers"} |
| Canal | {ex: "WhatsApp fragmentado"} | {ex: "WhatsApp 100% centralizado no CRM via API"} |
| Automação | {ex: "Bot com bug, sem scoring"} | {ex: "3 funis + lead scoring BANT + SDR IA"} |
| Priorização | {ex: "Por ordem de chegada"} | {ex: "Lead scoring define quem atende primeiro"} |
| Recompra | {ex: "Inexistente"} | {ex: "Funil automático 30/60/90 dias"} |

---

## PARTE 2 — Plano Tático 5W2H

### Passo 1: Consolidação de Gaps

Com base nos diagnósticos de entrada e na Avaliação Estratégica (Parte 1), liste todos os gaps:

| # | Gap | Módulo de origem | Impacto estimado | Esforço |
|---|-----|-----------------|-----------------|---------|
| 1 | {gap específico} | {POP/skill} | Alto/Médio/Baixo | Alto/Médio/Baixo |
| 2 | {gap} | — | — | — |

**Decisão estratégica binária (apenas para POP 6.4 — CRO):**
- [ ] **Otimizar Atual:** problemas são pontuais — ajustes específicos suficientes
- [ ] **Criar Nova LP:** velocidade + copy + UX são todos ruins = problema sistêmico → reconstrução mais eficiente

---

### Passo 2: Matriz de Priorização

| # | Ação | Nível | Impacto | Esforço | Tipo |
|---|------|-------|---------|---------|------|
| 1 | {ação específica} | Tático | Alto | Baixo | ⚡ Quick Win |
| 2 | {ação} | Estratégico | Alto | Médio | 🏗️ Estrutural |
| 3 | {ação} | Tático | Médio | Médio | 📌 Moderado |
| 4 | {ação} | Qualquer | Baixo | Alto | 🗑️ Não entra |

**Legenda:**
- ⚡ Quick Win: implementar nos próximos 7 dias
- 🏗️ Estrutural: planejar para os próximos 30 dias
- 📌 Moderado: encaixar no backlog após Quick Wins
- 🗑️ Não entra: esforço não justifica o impacto

---

### Passo 3: Plano 5W2H

**Formato de cada ação:**

| Campo | Descrição |
|-------|-----------|
| **O quê** | Ação específica e mensurável — não "otimizar X", mas "pausar X com critério Y" |
| **Por quê** | Evidência do diagnóstico + impacto quantificado quando disponível |
| **Quem** | Papel responsável (Account / GT / Copy / Designer / Cliente / Gerente) |
| **Quando** | Prazo concreto ("Até 48h após aprovação" / "Semana 2" / data) |
| **Onde** | Plataforma / sistema / ferramenta |
| **Como** | Instrução de execução resumida — suficiente para o responsável começar sem reunião |
| **Quanto** | Custo estimado (R$0 / R$X / sem custo adicional) |
| **Métrica de Sucesso** | KPI concreto e verificável em prazo definido |

---

#### ⚡ QUICK WINS — Executar nos próximos 7 dias

**QW-01 — {título}**

| | |
|---|---|
| **O quê** | {descrição} |
| **Por quê** | {evidência do diagnóstico} |
| **Quem** | {papel} |
| **Quando** | {prazo} |
| **Onde** | {ferramenta/plataforma} |
| **Como** | {instrução} |
| **Quanto** | {custo} |
| **Métrica** | {KPI concreto} |

*(repetir para QW-02, QW-03, QW-04)*

---

#### 🏗️ ESTRUTURAIS — Planejar nos próximos 30 dias

**EST-01 — {título}**

| | |
|---|---|
| **O quê** | {descrição} |
| **Por quê** | {evidência} |
| **Quem** | {papel} |
| **Quando** | {prazo} |
| **Onde** | {ferramenta} |
| **Como** | {instrução} |
| **Quanto** | {custo} |
| **Métrica** | {KPI} |

*(repetir para EST-02, EST-03, EST-04)*

---

#### 📅 RECORRENTES

**REC-01 — {título}**

| | |
|---|---|
| **O quê** | {descrição} |
| **Quem** | {papel} |
| **Quando** | {cadência: "toda segunda-feira" / "quinzenal"} |
| **Métrica** | {ex: "zero tarefas vencidas na revisão"} |

---

### Resumo Executivo do Plano

| Nível | Tipo | Qtd | Prazo | Impacto esperado |
|---|---|---|---|---|
| Estratégico | Decisões de modelo | {n} | 30 dias | {resumo das decisões} |
| Tático | Quick Wins | {n} | 7 dias | {ganho imediato} |
| Tático | Estruturais | {n} | 30 dias | {ganho estrutural} |
| Tático | Recorrentes | {n} | Contínuo | {resultado sustentado} |

**A decisão estratégica de maior impacto:** {ação/decisão} — {justificativa baseada no diagnóstico}

**A ação de maior ROI imediato:** {ação} — {justificativa com dado do diagnóstico}

**O que NÃO está no plano e por quê:**
| Ação excluída | Motivo |
|---|---|
| {ação} | {motivo — esforço alto / impacto baixo / fora do escopo Saber / hipótese a validar antes} |

---

### Apêndice: Estrutura de Blocos da LP (apenas se "Criar Nova" em POP 6.4)

| Bloco | Conteúdo | Referência para copy |
|-------|----------|---------------------|
| 1. Hero | Headline + Sub + CTA visível sem rolar | PUV aprovada em `proposta-unica-de-valor.json` |
| 2. Problema/Dor | Agitação da dor principal do ICP | `definicao-icp-b2b.json` → dores |
| 3. Solução | O que é e como funciona | `proposta-unica-de-valor.json` → diferenciais |
| 4. Como Funciona | Processo em 3-5 passos | Fluxo do serviço/produto |
| 5. Autoridade | Credenciais, tempo de mercado, clientes | Briefing do cliente |
| 6. Prova Social | Depoimentos com nome + resultado + foto | Coletar com cliente |
| 7. Oferta + CTA | O que o lead recebe + botão de ação | `proposta-unica-de-valor.json` → variação Ganho |
| 8. FAQ | Top 3-5 objeções do ICP | `diagnostico-copy-lp.json` → objeções não respondidas |

**Regra fundamental:** nunca usar Lorem Ipsum. Copy real deve ser inserida desde o wireframe.

---

## Auto-validação

Antes de mostrar ao operador, verifique:

**Camada Estratégica (POP 8.3):**
- [ ] As 4 dimensões (metodologia, estrutura, canal, automação) foram avaliadas com evidência do diagnóstico?
- [ ] A metodologia recomendada está justificada pelo perfil do ICP e canal, não escolhida genericamente?
- [ ] A tabela As Is vs To Be está completa e baseada nos dados — não em pressupostos?
- [ ] O modelo de automação recomendado é exequível com o stack atual do cliente?

**Plano Tático (todos os contextos):**
- [ ] O contexto (POP 4.4 / 5.4 / 6.4 / 8.3) foi identificado e as ações são relevantes para ele?
- [ ] Cada Quick Win pode ser implementado em ≤ 7 dias?
- [ ] Cada ação tem Métrica de Sucesso concreta (não apenas "melhorar")?
- [ ] Ações com baixo impacto foram excluídas?
- [ ] O Responsável de cada ação é um papel real (Account/GT/Cliente), não "todos"?
- [ ] Se POP 6.4: decisão Otimizar vs Criar Nova foi tomada antes do 5W2H?

Se falhou → regenere silenciosamente. Não avise o operador.

---

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

**Camada Estratégica:**
- "A avaliação de metodologia reflete o que você observou no time?"
- "O modelo SDR/Closer proposto — o cliente tem headcount ou budget para essa separação?"
- "O canal recomendado está alinhado com o que o cliente consegue operar?"

**Plano Tático:**
- "Os Quick Wins fazem sentido para a capacidade de execução do time?"
- "Alguma ação estrutural que já sabem que não vai acontecer por restrição de orçamento ou time?"
- "A métrica de sucesso de cada ação — você consegue medir isso sem ferramentas novas?"
- "A priorização faz sentido para o momento do cliente? Alguma urgência externa que eu não considerei?"

---

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/plano-de-acao-comercial.md` (para POP 8.3) ou `plano-de-acao-{modulo}.md` para outros POPs
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próximas skills conforme o contexto:
   - POP 4.4: `/analise-eficiencia-investimentos` ou `deck-semana-estruturacao`
   - POP 5.4: `/diagnostico-copy-lp` (POP 6.1) se não feito
   - POP 6.4: `deck-semana-estruturacao` ou `diagnostico-comercial-crm`
   - **POP 8.3: `/diagnostico-travas-scoring` — consolida todos os módulos, identifica Restrição Maior e prepara deck de entrega final**
