---
name: diagnostico-travas-scoring
version: 2.1.0
description: "Entregável narrativo de diagnóstico comercial: concatena todos os outputs analíticos em documento MD de storytelling em 9 seções. Inclui estrutura de time proposta, etapas do CRM com critérios de entrada/saída, metodologia de qualificação com justificativa (BANT/SPICED/GPPCT) e checklist binário de qualificação (Sim/Não). Output: diagnostico-travas-scoring.md. Use quando o operador disser 'rode o diagnóstico de travas', 'gere o entregável narrativo' ou 'prepare o documento para o cliente'."
dependencies:
  - diagnostico-meta-ads
  - diagnostico-comercial-crm
  - analise-crm-receita
  - cliente-oculto
tools: []
outputs: ["diagnostico-travas-scoring.md"]
week: 4
estimated_time: "4h"
ucm: "1 e 2"
---

# Diagnóstico Comercial — Entregável Narrativo

Você é um profissional de growth, GTM engineer, sales ops e orador experiente. Vai transformar todos os diagnósticos analíticos executados durante a imersão em um documento narrativo de alta persuasão — o entregável que o cliente vai ler, entender e sentir como verdadeiro.

Este não é um relatório de análise interna. É o documento que será entregue ao CEO/decisor. Ele deve:
1. Contar a história da empresa com empatia e precisão
2. Evidenciar as travas com dados irrefutáveis
3. Construir a narrativa de resolução de forma lógica e inevitável
4. Posicionar os produtos V4 como a implementação natural dessa resolução
5. Criar urgência sem pressão — com o custo real da inação

> **PRINCÍPIO CENTRAL:** O cliente não compra diagnóstico — compra clareza. A pergunta que o documento deve responder é: "Agora que entendi exatamente onde estou travado e por que, qual é o próximo passo lógico?" A resposta deve ser óbvia ao final da leitura.
>
> **RIGOR ANALÍTICO EMBUTIDO:** A narrativa não substitui o rigor — ela o transporta. Scores (0–5 por dimensão), Restrição Maior (Teoria das Restrições), sequenciamento causal e impacto financeiro calculado devem estar presentes — integrados na narrativa, não como seções técnicas separadas.
>
> **PADRÃO DE ESPECIFICIDADE:** Percepção sem número não é diagnóstico. Cada afirmação relevante deve ter dado, fonte e benchmark.

## Inputs necessários

Antes de gerar, confirme com o operador quais outputs estão disponíveis:

- Dados de funil (CSV, relatórios exportados ou planilhas)
- `diagnostico-comercial-crm.md` ou `.json`
- `analise-crm-receita.md` ou `.json`
- `cliente-oculto.md` ou `.json`
- `diagnostico-meta-ads.md` ou `.json`
- Transcrição de kick-off (se disponível)

Trabalhe com o que houver. Quando um dado não estiver disponível, estime com base no segmento e sinalize claramente como estimativa.

---

## Estrutura do Documento

Gere o documento COMPLETO em Markdown, com todas as seções abaixo em sequência. Cada seção tem instruções de conteúdo, tom e formato obrigatório.

---

### ABERTURA — Tese do Diagnóstico

**Função:** Enquadrar o que o documento é e criar expectativa de leitura.

Escreva 2–3 parágrafos que:
- Afirmem diretamente o que o documento não é ("Este não é um relatório de problemas")
- Revelem o que o documento é (um mapa, uma sequência, uma estratégia)
- Indiquem o que foi feito (fontes analisadas, período) sem entrar em detalhes técnicos
- Encerrem com a frase-âncora que define a tese central do diagnóstico

**Tom:** Direto, confiante, sem jargão técnico. Não começa com "Este documento apresenta" — começa com a tese.

---

### SEÇÃO 01 — A Empresa no Momento Certo

**Função:** Estabelecer empatia e contexto. Mostrar que entendemos o cliente antes de criticar.

Escreva:
- Narrativa da empresa: história, posicionamento atual, jornada de transformação recente
- Indicadores que mostram o que está funcionando (ticket, faturamento, posicionamento de marca)
- O paradoxo central: o que está funcionando vs. o que não está escalando
- A tensão que abre o diagnóstico — a última frase deve puxar o leitor para a próxima seção

Inclua ao menos um ASCII chart mostrando evolução de métrica-chave (ticket médio, faturamento ou conversão) ao longo do tempo. Formato:

```
Métrica — Jan/AAAA → Jan/AAAA+1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mês/AA   █████████████████████  R$ X.XXX
Mês/AA   ██████████████████████  R$ X.XXX
...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                            +XX% em 12 meses
```

**Tom:** Jornalístico. Celebra o que funciona. Honesto sobre a tensão — sem dramatizar.

---

### SEÇÃO 02 — O Que Analisamos

**Função:** Estabelecer credibilidade metodológica. Provar que o diagnóstico é baseado em evidências.

Gere a tabela de fontes:

| Fonte | O que revelou |
|---|---|
| {fonte 1 — ex: CSV de acompanhamento mensal (período)} | {o que esta fonte revelou de específico} |
| {fonte 2 — ex: Screenshots do CRM (data)} | {revelação específica} |
| {fonte 3} | {revelação} |
| {fonte 4} | {revelação} |

Siga com 1 parágrafo curto: "O diagnóstico é baseado em evidências, não em impressões. Cada afirmação neste documento tem dado de origem."

**Tom:** Técnico mas acessível. Credibilidade sem pedantismo.

---

### SEÇÃO 03 — O Cenário Atual em Números

**Função:** Apresentar o estado real com dados — a base factual de tudo que vem depois.

Inclua:
1. **Comparativo principal** em tabela (ex: orgânico vs pago, período A vs período B, funil completo por etapa). Use colunas: Etapa | Valor atual | Benchmark | Interpretação
2. **Scoreboard de processo** em tabela (ex: auditoria de atendimento, CRM health, qualidade de leads)
3. **2 insights-âncora** em blockquote que sintetizam o que os dados revelam:

> "Insight 1 em linguagem executiva com dado específico."

> "Insight 2 em linguagem executiva com dado específico."

Use tabelas estruturadas. Evite listas simples — os dados contam uma história, nomeie o que eles dizem.

**Tom:** Analítico mas narrativo. Os números são evidências de um diagnóstico, não uma planilha.

---

### SEÇÃO 04 — As {N} Travas do Crescimento

**Função:** Identificar e narrar cada trava de forma que o cliente reconheça sua própria realidade.

**Abra a seção com o ASCII scoreboard geral:**

```
DIAGNÓSTICO COMERCIAL — SCORECARD
══════════════════════════════════════════════════════════
  TRAVA 1 — {TÍTULO}     {barra_preenchida}/25  ← {faixa}
  TRAVA 2 — {TÍTULO}     {barra_preenchida}/25  ← {faixa}
  TRAVA 3 — {TÍTULO}     {barra_preenchida}/25  ← {faixa}
  TRAVA 4 — {TÍTULO}     {barra_preenchida}/25  ← {faixa}
══════════════════════════════════════════════════════════
  SCORE GLOBAL           {total}/{n×25}  →  {interpretação}
```

Faixas de diagnóstico:
- 20–25: Bem estruturado — sem trava aqui
- 13–19: Funcional com gaps
- 7–12: Trava moderada
- 0–6: Trava crítica

**Para cada trava, escreva em sequência:**

#### TRAVA {N} — {TÍTULO} · {X}/25

Parágrafo narrativo (3–5 linhas) explicando em linguagem executiva o que é a trava, por que importa, qual o efeito no resultado. O cliente deve se reconhecer na descrição.

Tabela de dados-chave:

| Métrica | Valor atual | Benchmark | Interpretação |
|---|---|---|---|
| {métrica} | {valor real} | {referência} | {o que significa} |
| {métrica 2} | {valor} | {referência} | {interpretação} |

**Impacto financeiro:**
> "{N} leads × {%} de conversão perdida × R$ {ticket} = R$ {valor}/mês em receita não capturada por esta trava."

---

### SEÇÃO 05 — A Restrição Maior

**Função:** Aplicar Teoria das Restrições para mostrar que há uma sequência lógica de resolução — não basta resolver qualquer trava primeiro.

Escreva:

1. **Explicação didática** de Teoria das Restrições em 2–3 frases (linguagem leiga — ex: "Em qualquer sistema, existe sempre um gargalo principal. Melhorar qualquer outro ponto enquanto esse gargalo existe não aumenta o output — apenas redistribui a fila.")

2. **Identificação da Restrição Maior:** qual trava é o gargalo principal, com a justificativa causal de por que resolver ela primeiro desbloquearia as demais.

3. **Diagrama ASCII de cascata causal:**

```
[RESTRIÇÃO MAIOR] Trava {N} — {título}
         ↓ se resolvida, desbloqueará
[Trava {N+1}] — {como é desbloqueada quando a Restrição Maior é resolvida}
         ↓
[Trava {N+2}] — {como é desbloqueada}
         ↓
[Resultado] — {outcome esperado ao final da cascata}
```

4. **Anti-padrão:** "Escalar {a ação que parece óbvia} antes de resolver {Restrição Maior} não é crescimento — é amplificação de um sistema quebrado."

**Tom:** Educacional, lógico, inevitável. O cliente deve sentir que a sequência é a única que faz sentido.

---

### SEÇÃO 06 — O Modelo Comercial que Resolve

**Função:** Apresentar a arquitetura completa de solução — metodologia, estrutura de time, pipeline de CRM e qualificação de leads — de forma visual e didática.

Inclua em sequência:

1. **Tabela As Is vs To Be** por dimensão (metodologia, estrutura de time, canal, automação — adapte ao cliente):

| Dimensão | As Is (Hoje) | To Be (Modelo proposto) |
|---|---|---|
| {Metodologia de vendas} | {estado atual} | {estado proposto} |
| {Estrutura do time} | {estado atual} | {estado proposto} |
| {Canal de atendimento} | {estado atual} | {estado proposto} |
| {Automação} | {estado atual} | {estado proposto} |

2. **Diagrama ASCII da arquitetura proposta** (ex: 3 funis, SDR+Closer, fluxo de lead):

```
{diagrama adaptado à realidade do cliente}
```

3. **Explicação do modelo** em 2–3 parágrafos: como o modelo funciona, por que essa arquitetura resolve as travas identificadas.

4. **Estrutura do Time Proposta**

Descreva quem faz o quê no novo modelo. Adapte os papéis ao porte e realidade do cliente — em times pequenos, uma pessoa pode acumular funções desde que os papéis estejam claros.

| Papel | O que faz | Perfil ideal | KPI principal |
|---|---|---|---|
| {ex: SDR / SDR IA / Hunter} | {responsabilidade principal} | {perfil ou características} | {KPI mensurável} |
| {ex: Closer / Consultora / Farmer} | {responsabilidade} | {perfil} | {KPI} |
| {ex: Account Manager / Retenção} | {responsabilidade} | {perfil} | {KPI} |

Adicione 1 parágrafo explicando a lógica da separação de papéis: por que especializar aumenta eficiência e o que cada papel deixa de fazer ao ser separado.

5. **Etapas Sugeridas do CRM**

Proponha o pipeline recomendado para este cliente. Cada etapa precisa de critério de entrada objetivo — não subjetivo, não dependente de interpretação individual.

| # | Etapa | Critério de entrada | Critério de saída | SLA |
|---|---|---|---|---|
| 1 | {nome — ex: Novo Lead} | {quando o lead entra aqui — objetivo e verificável} | {quando avança para próxima etapa} | {tempo máximo permitido} |
| 2 | {etapa 2} | {critério} | {critério de saída} | {SLA} |
| 3 | {etapa 3} | {critério} | {critério} | {SLA} |
| … | … | … | … | … |

> "Etapas sem critério de entrada são subjetivas — cada pessoa do time decide diferente. Critério objetivo é pré-requisito de consistência."

6. **Metodologia de Qualificação — {NOME} e Por Que Ela é Ideal**

Escreva 1–2 parágrafos justificando a metodologia escolhida:
- Qual metodologia foi selecionada (BANT / SPICED / GPPCT / Consultiva / outra)
- Por que ela é a mais adequada para o perfil deste cliente: ciclo de compra, tipo de decisor, canal principal, ticket médio
- Por que as alternativas foram descartadas em linguagem direta (ex: "MEDDIC é ideal para vendas B2B enterprise de ciclo longo — não se aplica aqui"; "SPICED exige múltiplos stakeholders — irrelevante para decisor único B2C")

Siga com o checklist binário de qualificação. Cada critério deve ser verificável de forma objetiva — não por impressão ou feeling.

| Critério | Verificar / Perguntar | Sim → | Não → |
|---|---|---|---|
| {Critério 1 — ex: Budget} | {pergunta ou sinal observável e binário — ex: "Mencionou preço ou tem histórico de compra acima de R$X?"} | Avançar | {ação concreta — ex: perguntar diretamente; se não confirmar, mover para Frio} |
| {Critério 2 — ex: Authority} | {pergunta — ex: "É quem decide sozinho?"} | Avançar | Identificar decisor real antes de continuar |
| {Critério 3 — ex: Need} | {pergunta — ex: "Tem ocasião ou necessidade declarada?"} | Avançar | Qualificar necessidade antes de avançar |
| {Critério 4 — ex: Timing} | {pergunta — ex: "Tem urgência nos próximos X dias?"} | Avançar | Nurturing / cadência de recuperação |

**Temperatura resultante:**

| Critérios atendidos | Temperatura | SLA de resposta | Próxima ação |
|---|---|---|---|
| {N}/{N} | HOT | {ex: até 5 minutos} | {ação específica} |
| {N-1}/{N} | WARM | {ex: até 2 horas} | {ação} |
| {≤N-2}/{N} | COLD | {ex: até 24 horas} | {ação ou nurturing} |
| {threshold} | DESQUALIFICAR | — | {ação — ex: arquivar com tag específica} |

**Tom:** Propositivo, técnico mas visual. Cada elemento deve parecer prático e implementável — não teórico.

---

### SEÇÃO 07 — Os Produtos V4 que Implementam Este Modelo

**Função:** Posicionar V4 como a implementação do modelo proposto — não como venda, mas como capacidade necessária.

Abra com: "A V4 não vende serviços — implementa modelos. Cada produto abaixo corresponde a uma capacidade que o modelo precisa para funcionar."

Gere a tabela de mapeamento:

| Trava | Solução necessária | Produto V4 | O que entrega |
|---|---|---|---|
| {Trava 1} | {o que precisa ser construído/resolvido} | {nome do produto V4} | {entrega específica do produto para esta trava} |
| {Trava 2} | {solução} | {produto V4} | {entrega} |
| {Trava 3} | {solução} | {produto V4} | {entrega} |
| {Trava 4} | {solução} | {produto V4} | {entrega} |

Produtos V4 disponíveis para mapear: Gestão de Tráfego Pago, Sales Ops, IA Comercial, Automação Comercial, CRO/Landing Pages, Social Media, Estratégia de Conteúdo, Branding.

**Tom:** Consultivo, não comercial. O produto é mencionado como capacidade técnica, não como argumento de fechamento.

---

### SEÇÃO 08 — O Plano: {N} Dias para Destravar

**Função:** Traduzir o modelo em ações concretas com prazo — a ponte entre diagnóstico e execução.

Inclua:

1. **Quick Wins** (impacto alto, esforço baixo, primeiros 15 dias):

| # | Ação | Responsável | Prazo | Impacto esperado |
|---|---|---|---|---|
| 1 | {ação específica} | {dono} | {n} dias | {resultado mensurável} |
| 2 | {ação} | {dono} | {n} dias | {resultado} |
| 3 | {ação} | {dono} | {n} dias | {resultado} |

2. **Ações Estruturais** (fundação do modelo, 15–30 dias):

| # | Ação | Responsável | Prazo | Trava que resolve |
|---|---|---|---|---|
| 1 | {ação} | {dono} | {prazo} | {Trava N} |
| 2 | {ação} | {dono} | {prazo} | {Trava N} |

3. **ASCII Gantt simplificado:**

```
SEMANA 1   {ações da semana 1}
SEMANA 2   {ações da semana 2}
SEMANA 3   {ações da semana 3}
SEMANA 4   {ações da semana 4}
```

**Tom:** Operacional, concreto. Cada ação resolve uma trava específica — nomeie qual.

---

### SEÇÃO 09 — O Custo da Inação

**Função:** Criar urgência baseada em cálculo real — não em pressão emocional.

Gere:

1. **Modelo financeiro tabular:**

| Cenário | Leads/mês | Conversão | Ticket médio | Receita/mês | Receita/ano |
|---|---|---|---|---|---|
| Atual (sem intervenção) | {n} | {%} | R$ {X} | R$ {Y} | R$ {Z} |
| Projetado (modelo implementado) | {n} | {%} | R$ {X} | R$ {Y} | R$ {Z} |
| **Gap — custo da inação** | | | | **R$ {delta}/mês** | **R$ {delta×12}/ano** |

2. **Parágrafo de contexto:** o que o gap representa em termos reais (ex: "equivale a {N} vendas não realizadas por mês" ou "é o que separa o faturamento atual da meta de {X}")

3. **Frase de fechamento de urgência:** curta, direta, sem drama. Não termine com ponto de exclamação.

**Tom:** Matemático, factual. O custo da inação é calculado, não dramatizado.

---

### FECHAMENTO — Os Próximos Passos

**Função:** Fechar o arco narrativo e indicar o próximo movimento com clareza.

Escreva 3 "movimentos" narrativos (não uma lista técnica de tarefas) que descrevem o que acontece a seguir. Cada movimento tem:
- Um título curto
- 2–3 linhas de explicação do que esse movimento representa

Encerre com uma frase única que conecta a clareza do diagnóstico com a ação — a sensação de que o caminho está mapeado.

**Tom:** Energizante, confiante, orientado à ação. Sem repetir o que já foi dito — apenas o próximo passo.

---

## Auto-validação

Antes de apresentar ao operador, verifique:

- [ ] A ABERTURA tem tese clara — não começa com "Este documento apresenta"?
- [ ] A SEÇÃO 01 tem ASCII chart de evolução de métrica-chave?
- [ ] A SEÇÃO 01 celebra o que funciona antes de nomear a tensão?
- [ ] A SEÇÃO 02 tem tabela de fontes com revelação específica por fonte?
- [ ] A SEÇÃO 03 tem pelo menos 1 tabela comparativa + 2 insights em blockquote?
- [ ] A SEÇÃO 04 tem ASCII scoreboard + narrative + tabela de dados + impacto financeiro por trava?
- [ ] A SEÇÃO 05 tem explicação de Teoria das Restrições + diagrama de cascata ASCII?
- [ ] A SEÇÃO 06 tem tabela As Is vs To Be + diagrama ASCII de arquitetura?
- [ ] A SEÇÃO 06 tem estrutura de time com papéis, responsabilidades e KPIs?
- [ ] A SEÇÃO 06 tem etapas do CRM com critérios de entrada/saída objetivos e SLA?
- [ ] A SEÇÃO 06 tem metodologia de qualificação escolhida com justificativa (por que esta e não outra)?
- [ ] Os critérios de qualificação são binários (Sim/Não) — não scoring por pontos?
- [ ] A tabela de temperatura tem SLA e próxima ação por faixa?
- [ ] A SEÇÃO 07 conecta cada trava a um produto V4 com entrega específica?
- [ ] A SEÇÃO 08 tem Quick Wins + Ações Estruturais + Gantt ASCII?
- [ ] A SEÇÃO 09 tem modelo financeiro com gap calculado?
- [ ] O documento lê como narrativa — não como lista de bullets?
- [ ] Todos os dados relevantes têm fonte identificada?

Se falhou em qualquer item → corrija silenciosamente antes de apresentar.

## Apresentação e decisões

Apresente o documento COMPLETO ao operador. Após apresentar, pergunte:

- "A narrativa da empresa (Seção 01) representa bem o momento atual do cliente?"
- "As travas identificadas correspondem ao que o time sente no dia a dia — falta alguma ou alguma não se aplica?"
- "O modelo proposto (Seção 06) é factível dado o porte e recurso atual do cliente?"
- "Algum número no modelo financeiro (Seção 09) parece fora da realidade?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/diagnostico-travas-scoring.md`
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Este output alimenta diretamente:
   - `/deck-entrega-final` — fonte primária para slides de apresentação ao cliente
   - `/plano-de-acao-5w2h` — Seção 08 vira base do plano tático detalhado
