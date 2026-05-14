---
slug: drx-s2-13-trava-7-exposicao-v1
name: drx-s2-13-trava-7-exposicao-v1
description: "Conduz o diagnóstico completo da Trava 7 em modo Copilot: a IA lidera a coleta, processa dados de alcance, frequência e share of voice, compara a presença do cliente vs. concorrentes, propõe scores por dimensão com justificativa e redige..."
---

# Skill: Diagnóstico de Trava 7 — Exposição (DR-X)

## Descrição
Conduz o diagnóstico completo da Trava 7 em modo Copilot: a IA lidera a coleta, processa dados de alcance, frequência e share of voice, compara a presença do cliente vs. concorrentes, propõe scores por dimensão com justificativa e redige a consolidação causal. O consultor fornece dados das plataformas e relata o que observou sobre presença no mercado, validando os outputs em cada etapa.

## Quando Usar
- Triggers: "Rodar diagnóstico Trava 7", "Diagnosticar exposição", "Analisar Trava 7", "Diagnóstico de exposição para [cliente]"
- **Pré-requisito:** Arquivos `context/` do cliente com status `[VALIDADO]` devem estar disponíveis
- **NÃO usar** se os arquivos `context/` não existirem — executar `skill-pipeline-extracao` primeiro

---

## Inputs de Partida

Antes de perguntar qualquer coisa ao consultor, **ler os arquivos `context/`** do cliente e extrair:
- Modelos de venda ativos — `context/gtm.md`
- Canais de aquisição ativos e orçamento de marketing mencionado — `context/gtm.md`
- UDEs relacionadas a invisibilidade digital, dependência de indicação, volume baixo de leads, "zero exposição" — `context/constraints.md`
- Informações sobre frequência de publicação ou ausência de atividade nos canais — `context/gtm.md`

Registrar internamente o que já se sabe e **não coletar novamente o que já está nos arquivos `context/`**.

---

## Processo de Execução

### Step 0 — Leitura do Contexto

1. Ler os arquivos `context/business.md`, `context/gtm.md` e `context/constraints.md`
2. Mapear:
   - Quais canais estão ativos e com que frequência declarada (`context/gtm.md`)
   - O que já foi capturado sobre presença de mercado e geração de leads (`context/gtm.md`)
   - UDEs que apontam exposição insuficiente — baixo volume de entrada, dependência de indicação (`context/constraints.md`)
3. Apresentar resumo ao consultor:

> *"Com base nos arquivos context/, já sei que: [resumo dos canais ativos, orçamento, frequência declarada, UDEs sobre visibilidade]. Vou analisar se a exposição é suficiente para sustentar crescimento. Seguindo para o Step 1."*

---

### Step 1 — Camada Analítica (Alcance e Frequência)

Solicitar **em uma única mensagem batch** os dados de presença e volume. Adaptar ao que já está no Master Contexto.

**Perguntar de uma vez:**
> *Preciso dos seguintes dados para avaliar se a exposição do negócio é suficiente para alimentar o funil. Forneça o que tiver:*
>
> *1. Alcance mensal médio nos últimos 6 meses (por canal: Meta, Google, LinkedIn, Instagram etc.) e impressões totais*
> *2. Frequência média de anúncios pagos e investimento mensal em mídia por canal*
> *3. Volume de tráfego total (orgânico + pago) e leads gerados por mês*
> *4. Frequência de publicação orgânica por canal (ex: "postamos 3x por semana no Instagram")*
> *5. Principal fonte de origem dos leads atualmente (indicação, orgânico, ads, outbound, Yokogawa etc.)*
> *6. Comparação percebida com concorrentes — a empresa acredita estar mais visível, similar ou menos visível que os principais concorrentes?*

**Após receber os dados:**

Classificar a exposição atual:

| Nível | Critério |
|---|---|
| Insuficiente | Alcance < 5% do mercado estimado; frequência esporádica; dependência de indicação > 70% |
| Básica | Presença existente mas inconsistente; sem cobertura de canais estratégicos |
| Consistente | Frequência regular; múltiplos canais; geração de leads previsível |
| Dominante | Alto alcance; frequência estratégica; share of voice superior ao mercado |

Apresentar análise e perguntar: *"Essa leitura faz sentido com o que você observa? Alguma correção antes de avançar?"*

---

### Step 2 — Camada Experiencial (Presença Real no Mercado)

Com base nos modelos de venda ativos identificados no Step 0, perguntar **em uma única mensagem batch**. Incluir apenas os modelos relevantes.

**Se Inside Sales ativo:**
> *Sobre geração ativa de oportunidades (outbound):*
> - *Existe prospecção ativa outbound com sequência definida (cadência de e-mail, WhatsApp, LinkedIn)?*
> - *Qual o volume de contatos ativos por semana e qual é a taxa de resposta estimada?*
> - *Existe base de prospecção segmentada pelo ICP, ou a abordagem é genérica / pontual?*

**Se Vendas Online ativo:**
> *Sobre presença digital e consistência de exposição:*
> - *O consultor verificou a biblioteca de anúncios do cliente — quantos anúncios estão ativos? Há quanto tempo estão no ar (consistência vs. campanhas pontuais)?*
> - *Comparando com 3–5 concorrentes principais: a empresa está mais visível, similar ou menos visível em canais pagos?*
> - *A presença orgânica (posts, stories, conteúdo) é consistente (rotina definida) ou reativa (só posta quando tem algo para vender / evento específico)?*
> - *O SEO orgânico gera tráfego relevante, ou a empresa é invisível nas buscas do ICP?*

**Se PDV ativo:**
> *Sobre presença física e territorial:*
> - *A localização tem fluxo de pessoas adequado para o ICP?*
> - *A sinalização externa é visível e comunicativa a partir da via pública?*
> - *Existe presença territorial além do ponto fixo (feiras, eventos, parcerias locais)?*

Aguardar as respostas antes de prosseguir para o scoring.

---

### Step 3 — Scoring por Dimensão (A a E)

Com base nos dados do Step 1 e nas observações do Step 2, propor score para cada dimensão usando o gabarito abaixo. **A IA propõe — o consultor valida.** Nunca pedir ao consultor que atribua as notas.

**Gabarito de referência** (`context/context-trava-7-exposicao.md`):

| Nota | A) Alcance Mensal | B) Frequência e Consistência | C) Share of Voice | D) Diversidade de Canais | E) Regularidade Estratégica |
|---|---|---|---|---|---|
| 0 | Quase inexistente | Inexistente | Invisível | Canal único | Reativa |
| 1 | Muito baixo | Esporádica | Muito inferior | Quase inexistente | Ocasional |
| 2 | Baixo | Irregular | Inferior | Limitado | Inconsistente |
| 3 | Aceitável | Consistente básica | Similar | Adequado | Planejada básica |
| 4 | Alto | Consistente estratégica | Superior | Bem distribuído | Planejada e executada |
| 5 | Dominante | Altamente estruturada | Dominante | Estrategicamente multicanal | Planejada e otimizada |

**Regra:** nota > 3 exige evidência formal citada na justificativa.

Apresentar tabela completa com proposta de score, justificativa e evidência que sustenta cada nota. Perguntar: *"Concorda com os scores propostos? Algum ajuste antes de calcular o total?"*

---

### Step 4 — Consolidação Causal

Com o scoring validado, redigir a hipótese causal no formato obrigatório:

> *"A empresa opera sob a política implícita de ___, o que gera baixa presença no mercado e limita o volume de entrada no funil."*

**Orientação:** identificar a política organizacional que explica a exposição insuficiente. Exemplos: "confiar exclusivamente em indicação orgânica como canal de aquisição", "evitar investimento constante em mídia para controlar custo", "comunicar apenas quando há algo específico para vender, em vez de construir presença contínua".

Apresentar a hipótese para o consultor e aguardar validação ou ajuste.

---

### Step 5 — Determinação Preliminar

Aplicar os três critérios de governância:

1. Score total ≤ 15?
2. O funil é pequeno por falta de alcance (não por baixa conversão) — melhorar decisão não resolve o volume?
3. Aumentar exposição aumentaria diretamente a entrada no funil e o Throughput?

Declarar explicitamente: **"Trava 7 é / não é potencial governante"**, com o raciocínio que sustenta a decisão.

Registrar que a validação final é feita na CRT.

---

## Regras Operacionais

- **Nunca perguntar um dado de cada vez** — todas as perguntas de uma mesma camada vão em uma única mensagem
- **Nunca delegar o scoring ao consultor** — a IA propõe com justificativa, o consultor confirma ou ajusta
- **Nunca avançar de step sem apresentar resultado e receber confirmação** do consultor
- **Sempre ler os arquivos `context/` antes de perguntar qualquer coisa** — não coletar o que já está disponível
- **Ausência de mídia paga não bloqueia o diagnóstico** — registrar como dado relevante e analisar os canais que existem (orgânico, outbound, PDV)
- **Distinguir Trava 6 (atenção) de Trava 7 (exposição):** exposição = volume e frequência de presença no mercado; atenção = capacidade de interromper o padrão quando presente

---

## Fallbacks

| Situação | O que fazer |
|---|---|
| Sem investimento em mídia paga | Registrar como dado estrutural relevante. Analisar presença orgânica e outbound. Adaptar scoring ao canal predominante. |
| Sem dados de analytics (alcance, impressões) | Pontuar Dim A com base na percepção do consultor (máx 2). Registrar como fragilidade estrutural. |
| Análise de concorrentes não realizada | Pontuar Dim C conservadoramente. Registrar como "não confirmado por análise direta". |
| Empresa depende 100% de indicação | Registrar como evidência primária de Trava 7. Pontuar Dim B, D e E em 0–1. |
| Modelo de venda não aplicável | Pular seção experiencial correspondente. Registrar motivo. |
| Consultor não souber descrever a presença no mercado | Pontuar Dim B, C e E como 0–1 e registrar como dado não confirmado. |

---

## Formato de Saída Obrigatório

```markdown
# Diagnóstico Trava 7 — Exposição: [Nome do Cliente]

> **Status:** `[AGUARDANDO VALIDAÇÃO DO CONSULTOR]`
> **Data:** [data de execução]
> **Fontes:** context/business.md + context/gtm.md + context/constraints.md + dados fornecidos pelo consultor em [data]
> **Limitações registradas:** [listar dados ausentes ou estimados]

---

## Pergunta Estruturante

*"O mercado vê essa empresa com frequência estratégica ou apenas ocasionalmente?"*

**Resposta com base no diagnóstico:** [resposta em 2–3 linhas]

---

## Análise de Alcance e Frequência

| Canal | Alcance Mensal | Investimento | Frequência | Nível de Exposição |
|---|---|---|---|---|
| [canal] | | | | Insuficiente / Básica / Consistente / Dominante |

**Principal fonte de origem dos leads:** [indicação / orgânico / ads / outbound]
**% estimado de leads por indicação:** [X]% — [interpretação: dependência / equilibrado / diversificado]

---

## Mapa de Exposição Competitiva

| Canal | Cliente | Concorrente 1 | Concorrente 2 | Presença Relativa |
|---|---|---|---|---|
| Meta Ads | | | | Muito Inferior / Inferior / Similar / Superior / Dominante |
| Google Ads | | | | |
| Instagram Orgânico | | | | |
| Outbound | | | | |
| [outros canais relevantes] | | | | |

*[Preencher com o disponível — registrar "não analisado" quando ausente]*

---

## Score da Trava 7

| Dimensão | Score (0–5) | Justificativa | Evidência |
|---|---|---|---|
| A) Alcance Mensal | | | |
| B) Frequência e Consistência | | | |
| C) Share of Voice vs. Concorrentes | | | |
| D) Diversidade de Canais | | | |
| E) Regularidade Estratégica | | | |
| **Total (0–25)** | | | |

**Faixa:** [0–10 / 11–15 / 16–20 / 21–25] — [interpretação]

---

## Consolidação Causal

*"A empresa opera sob a política implícita de ___, o que gera baixa presença no mercado e limita o volume de entrada no funil."*

---

## Determinação Preliminar

- Score ≤ 15? [Sim / Não]
- Funil pequeno por falta de alcance (não por baixa conversão)? [Sim / Não — justificativa]
- Aumentar exposição aumenta diretamente entrada e Throughput? [Sim / Não — justificativa]

**Trava 7 é / não é potencial governante.** Validação final na CRT.
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/trava-7-exposicao.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
