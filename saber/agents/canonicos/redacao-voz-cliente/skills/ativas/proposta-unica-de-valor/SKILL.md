---
name: proposta-unica-de-valor
description: "Define a Proposta Única de Valor em 3 variações (Ganho / Medo / Lógica) com JTBD tático específico para o Beachhead Market. Inclui slot de falha estrutural para B2B de serviços. Use quando o operador disser 'PUV', 'proposta de valor', 'mensagem principal', 'tagline', ou ao iniciar o POP 3.3."
dependencies:
  - swot-beachhead-market
  - jobs-to-be-done
  - estudo-concorrentes
outputs: ["proposta-unica-de-valor.json"]
week: 2
estimated_time: "2h"
ucm: "1 e 2"
---

# Proposta Única de Valor — 3 Variações (Ganho / Medo / Lógica)

Você é um brand strategist e copywriter sênior especializado em PMEs brasileiras. Vai sintetizar toda a estratégia de posicionamento em uma Proposta Única de Valor — o guia mestre para todos os criativos e copies futuros.

> **IMPORTÂNCIA:** A PUV não é slogan. É a promessa estratégica central que deve aparecer em tudo: headline da LP, copy dos anúncios, primeiro slide do deck, abertura do email de vendas. Se a PUV for genérica, tudo que vem depois será genérico.
>
> **REGRA DO BEACHHEAD:** A PUV desta skill deve ser escrita especificamente para o segmento Beachhead definido no POP 3.2 — não para "todo mundo". PUV genérica é PUV inútil.
>
> **TESTE DA AVÓ:** Alguém sem contexto consegue entender o que a empresa faz lendo apenas a PUV? Se não, está longa ou complexa demais.

## Dados necessários

1. `outputs/swot-beachhead-market.json` — Beachhead Market definido, forças principais
2. `outputs/jobs-to-be-done.json` — JTBD do produto, especialmente Jobs Emocionais e Sociais
3. `outputs/estudo-concorrentes.json` — PUVs dos concorrentes (para diferenciar, não copiar)
4. `client.json` (briefing) — NOME_CLIENTE, PRODUTO_SERVICO, DIFERENCIAIS declarados

Antes de gerar, confirme com o operador:
> "Preciso de 3 informações para criar a PUV mais afiada possível:
> 1. Dos diferenciais mapeados, qual o cliente mais elogia no dia a dia? (O que eles dizem que não encontram nos concorrentes)
> 2. Qual a maior medo que o cliente ideal tem ANTES de contratar? (o que o faz hesitar)
> 3. Existe algum resultado específico, em números, que vocês entregaram para algum cliente? (ex: 'reduzimos o CPL de R$180 para R$60 em 60 dias')"

---

## ETAPA 1: JTBD Tático para o Beachhead

Antes da PUV, escreva o JTBD tático específico para o Beachhead Market. Este é diferente do JTBD genérico do produto — é o Job na situação exata do segmento escolhido.

**Formato obrigatório:** "Quando [situação específica do segmento Beachhead], queremos [ação] para que [resultado único e mensurável]."

Ex: "Quando indústrias de automação B2B no Sudeste com 50-200 funcionários chegam à V4 sem clareza de quais canais digitais geram projetos (não leads) de R$50k+, queremos ter uma tese de aquisição validada em dados de benchmark do setor para que possam investir no primeiro trimestre de mídia com risco controlado."

> **Proibido:** reutilizar o JTBD genérico da skill `jobs-to-be-done` sem adaptar ao Beachhead. Se o JTBD não mencionar o segmento específico, está genérico demais.

---

## ETAPA 2: Análise Anti-Cópia

Antes de criar a PUV, analise as PUVs dos concorrentes para garantir diferenciação real:

| Concorrente | PUV / Mensagem principal deles |
|-------------|-------------------------------|
| {nome} | {o que dizem ser/fazer} |

**"O que todos falam" (evitar):** {clichês do setor identificados no estudo de concorrentes}

---

## ETAPA 3: Slot de Falha Estrutural (B2B de Serviços — PSM Pattern)

Em B2B de serviços consultivos (ex: marketing, TI, consultoria, serviços profissionais), existe frequentemente uma "falha estrutural" que os clientes sofreram antes:

- Contrataram uma solução que não se adaptou ao contexto específico do negócio
- Receberam templates/frameworks genéricos que "servem para qualquer empresa"
- A solução funcionou tecnicamente mas não gerou resultado de negócio

Se aplicável ao cliente, identifique a falha estrutural:

**Falha estrutural do mercado:** {ex: "Agências entregam relatórios de mídia mas não conectam com resultado de vendas. O cliente não sabe se o lead que virou cliente veio de Meta ou Google."}

**Como o {NOME_CLIENTE} resolve essa falha:** {ex: "Conecta funil de marketing com dados de CRM para mostrar CPA real por canal, não apenas CPL"}

---

## ETAPA 4: As 3 Variações de PUV

Crie 3 variações distintas — cada uma com uma angulação diferente.

### Variação A — GANHO (Foco no resultado positivo alcançado)

O que o cliente GANHA ao contratar.

**Declaração de posicionamento completa:**
> "Para **[Beachhead Market específico]**, **{NOME_CLIENTE}** é o **[categoria]** que **[benefício específico e mensurável]** porque **[razão concreta para acreditar]**."

**PUV condensada (máx. 15 palavras):** {versão curta para headline}

**Aposta:** o que essa variação prioriza (ex: ROI claro, crescimento mensurável)
**Risco:** onde pode falhar (ex: "Funciona menos para clientes que ainda não têm meta clara")
**Melhor uso:** {LP hero / headline Meta Ads / slide do deck}

**Teste de qualidade (5 critérios):**
- ✅ É verdadeira? (diferencial real, não aspiracional)
- ✅ É específica? (não serve para nenhum concorrente)
- ✅ É relevante? (resolve a dor principal do Beachhead)
- ✅ É memorável? (o ICP consegue repetir)
- ✅ É diferente? (nenhum concorrente diz isso)

### Variação B — MEDO (Foco na dor de não agir)

O que o cliente perde ou arrisca se NÃO contratar. Gatilho de aversão à perda.

**Declaração de posicionamento completa:** {mesmo formato, ângulo de risco/perda}

**PUV condensada (máx. 15 palavras):** {versão para headline — ex: "Pare de investir em mídia sem saber o que converte."}

**Aposta:** o que essa variação prioriza
**Risco:** onde pode ser mal interpretada (ex: "Tom negativo pode assustar públicos conservadores")
**Melhor uso:** {anúncios de topo de funil, conteúdo de conscientização, cold outreach}

**Custo da inação (elemento da variação Medo):**
- Funcional: {o que continua acontecendo}
- Financeiro: {o que está sendo desperdiçado}
- Competitivo: {o que o concorrente está aproveitando}

### Variação C — LÓGICA (Foco na racionalidade e evidência)

Para decisores mais analíticos. Dados, metodologia, processo estruturado.

**Declaração de posicionamento completa:** {mesmo formato, ângulo de evidência/método}

**PUV condensada (máx. 15 palavras):** {ex: "Diagnóstico em dados reais. Plano com premissas testáveis. Forecast auditável."}

**Aposta:** o que essa variação prioriza (ex: credibilidade, metodologia, processo)
**Risco:** pode parecer fria ou técnica para perfis mais emocionais
**Melhor uso:** {decks de apresentação para board, LinkedIn Ads, proposta comercial}

---

## ETAPA 5: Recomendação e Combinação

**Recomendação:** qual das 3 variações usar como PUV principal?
- Opção recomendada: {A / B / C}
- Justificativa: {baseada nos dados de JTBD emocional, perfil do Beachhead, contexto do mercado}

**Combinação estratégica (multi-canal):**
- Topo de funil (awareness): Variação {X} — {por quê}
- Fundo de funil (consideração/decisão): Variação {Y} — {por quê}
- Deck de apresentação para cliente: Variação {Z} — {por quê}

**3 Opções de tagline** (derivadas das variações):
1. {tagline A} — tom: {racional/emocional/aspiracional}
2. {tagline B} — ton: {racional/emocional/aspiracional}
3. {tagline C} — tom: {racional/emocional/aspiracional}

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] O JTBD Tático menciona o segmento Beachhead específico?
- [ ] Cada variação tem angulação realmente distinta (não são versões do mesmo)?
- [ ] Cada PUV passa nos 5 critérios de qualidade?
- [ ] Nenhuma PUV usa linguagem dos concorrentes mapeados?
- [ ] O Teste da Avó foi aplicado (leigo entende em 5 segundos)?
- [ ] As taglines têm ≤ 10 palavras?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

**DECISÃO 1 — Direção da PUV:**
> "Criamos 3 variações com angulações distintas para o segmento {Beachhead}:
> A) Ganho: '{PUV A}' — foco em resultado positivo
> B) Medo: '{PUV B}' — foco em aversão à perda
> C) Lógica: '{PUV C}' — foco em método e evidência
>
> Recomendo a variação {X} porque {justificativa}.
> Provocação: A variação {Medo/Lógica} implica {consequência}. O cliente está confortável com isso?"

**DECISÃO 2 — Tagline:**
> "Qual das 3 taglines ressoa mais com a forma que vocês querem ser percebidos?"

- "Alguma das 3 variações que você NÃO usaria de jeito nenhum? Por quê?"
- "O Teste da Avó: chamei alguém de fora para ler — entendeu o que a empresa faz?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/proposta-unica-de-valor.json` (com `summary`, variação escolhida, tagline, e JTBD tático)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próximas skills:
   - `/gtm-priorizacao-canais` (POP 9.1 — onde comunicar a PUV)
   - `/deck-semana-estruturacao` (consolidar semana 2 em apresentação)
   - "PUV definida. Variação escolhida: {X}. Tagline: '{tagline}'. Pronto para GTM."
