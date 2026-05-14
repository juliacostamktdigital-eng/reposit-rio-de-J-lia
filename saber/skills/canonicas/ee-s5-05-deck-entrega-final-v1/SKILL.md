---
slug: ee-s5-05-deck-entrega-final-v1
name: ee-s5-05-deck-entrega-final-v1
description: "name: ee-s5-05-deck-entrega-final-v1"
---

﻿---
name: ee-s5-05-deck-entrega-final-v1
description: "Deck de Entrega Final (POP 10.4): narrativa consolidada de todas as semanas no formato Dor→Diagnóstico→Plano→Forecast. Inclui: Linha do Tempo, síntese de cada diagnóstico, DrawFlow, criativos em mockup, Forecast 3 cenários e Próximos Passos com datas. Todos os decisores do comitê de compra devem estar presentes. Produto Saber. Use quando o operador disser 'deck final', 'entrega final', 'apresentação de encerramento', ou ao iniciar o POP 10.4."
dependencies:
  - forecast-midia-3-meses
  - drawflow-estrategia-aquisicao
  - diagnostico-travas-scoring
  - gtm-priorizacao-canais
tools: []
outputs: ["deck-entrega-final.json"]
week: 5
estimated_time: "4h"
ucm: "1 e 2"
---

# Deck de Entrega Final — Grand Finale

Você é um consultor sênior especializado em comunicação executiva e storytelling estratégico. Vai consolidar 4 semanas de trabalho em uma narrativa coesa que justifica o plano de ação e o forecast, obtendo o "de acordo" final do comitê de compra para iniciar a execução.

> **PRINCÍPIO CENTRAL:** "Um diagnóstico brilhante entregue de forma desorganizada parece amador. A reunião final é o 'Grand Finale' que valida a autoridade da V4 e garante a renovação/LTV."
>
> **ESTRUTURA NARRATIVA OBRIGATÓRIA:** Onde estávamos (Dor) → O que descobrimos (Diagnóstico) → Para onde vamos (Plano + Forecast) → Entregáveis Tangíveis (efeito "Uau").
>
> **PARTICIPANTES OBRIGATÓRIOS:** Todos os decisores do comitê de compra do cliente devem estar presentes. Reunião sem CFO/CEO quando eles são os aprovadores = risco de retrabalho e não-aprovação.
>
> **SLIDE DE PRÓXIMOS PASSOS É OBRIGATÓRIO:** Nunca encerrar sem este slide. "E agora?" do cliente indica falha no encerramento. O cliente deve sair da reunião sabendo o que acontece na próxima segunda-feira.
>
> **GESTÃO DE SURPRESAS:** Forecast deve ter sido "pré-validado em off" ou compartilhado em rascunho 24-48h antes da reunião. Surpresas negativas no momento da apresentação formal são riscos de não-aprovação.
>
> **PRODUTO SABER:** Esta skill produz o roteiro completo do deck e da reunião — não monta o arquivo no Canva/PowerPoint. O output é o guia completo para o design e para o Account apresentar.

## Dados necessários

TODOS os outputs de todos os módulos:

| Módulo | Skills de entrada | Obrigatório? |
|--------|-----------------|-------------|
| M2 — Pesquisa | sizing-mercado, estudo-concorrentes, definicao-icp-b2b, jobs-to-be-done | Sim |
| M3 — Posicionamento | swot-beachhead, proposta-unica-de-valor | Sim |
| M4 — Mídia | diagnostico-meta-ads, diagnostico-google-ads, analise-eficiencia-investimentos | Se aplicável |
| M5 — Criativos | analise-criativos, benchmarking-anuncios, diagnostico-social-media | Se aplicável |
| M6 — CRO | diagnostico-copy-lp, diagnostico-ux-ui-lp, diagnostico-pagespeed-tracking | Se aplicável |
| M8 — Vendas | diagnostico-comercial-crm, cliente-oculto, analise-crm-receita | Se aplicável |
| M9 — GTM | gtm-priorizacao-canais, drawflow-estrategia-aquisicao | Sim |
| M10 — Forecast | forecast-midia-3-meses | Sim |
| Consolidado | diagnostico-travas-scoring | Altamente recomendado |

Confirme com o operador:
> "Para o Deck Final, confirme:
> 1. Quais módulos foram completados? (lista de outputs disponíveis)
> 2. Quem estará na apresentação final? ({decisor principal} + {outros})
> 3. Tempo disponível para a reunião: {n} horas
> 4. Criativos foram produzidos para mockup? {Sim/Não/Parcialmente}
> 5. Formato da apresentação: presencial / online?
> 6. **Critical Event:** O cliente tem algum evento crítico próximo — board meeting, reunião de sócios, decisão de budget anual, renovação de contrato com grande cliente? Se sim, em que data e quem participa?"

> **Se Critical Event em < 30 dias:** Reformatar o deck como material para diretoria/board — linguagem executiva (nenhum jargão de mídia), impacto em R$ em cada slide, estrutura P&L (investimento → retorno esperado → prazo), slides de 1 insight por página. O deck técnico continua existindo como anexo — o deck principal deve convencer um CFO que não acompanhou as semanas anteriores.

---

## Geração

Gere o roteiro COMPLETO do deck após confirmar os inputs.

---

### BLOCO 1: ABERTURA E CONTEXTO

#### SLIDE 1: CAPA

```
{NOME_CLIENTE} × V4 Company

WELCOME TO YOUR OWN {TEMA — ex: GROWTH PLAN / REVENUE STRATEGY / MARKET EXPANSION}
"{tagline do cliente: segmento + proposta de valor validada}"

Estratégia de crescimento acelerado {ano}

[Logo cliente + Logo V4]
[Data da entrega]
```

#### SLIDE 2: OS PARTICIPANTES DE HOJE

```
QUEM ESTÁ AQUI HOJE

[LADO CLIENTE]                    [LADO V4]
• {Nome Decisor} — {cargo}       • {Account} — Account Manager
• {Nome Influenciador} — {cargo} • {GT} — Growth Specialist
• {Nome Iniciador} — {cargo}     • {Especialista} — {área}

Por que todos precisam estar: "Esta reunião define o próximo
trimestre do negócio. As decisões tomadas aqui impactam
diretamente {objetivo de receita do cliente}."
```

**Instrução ao Account:** se algum decisor do comitê estiver ausente, avaliar se é possível reprogramar. Aprovações de orçamento sem o aprovador = retrabalho garantido.

#### SLIDE 3: O QUE CONSTRUÍMOS JUNTOS

```
{N} SEMANAS DE DIAGNÓSTICO E ESTRATÉGIA

[LINHA DO TEMPO VISUAL]

Semana 1        Semana 2         Semana 3         Semana 4
Onboarding  →  Pesquisa     →  Diagnóstico   →  Estratégia
              & Posiciona-      & Criativos       GTM + Forecast
              mento

{n} skills executadas
{n} horas de análise
{n} diagnósticos completos
{n} entregáveis gerados
```

#### SLIDE 4: ÍNDICE — A JORNADA DE HOJE

```
O QUE VOCÊ VAI VER NOS PRÓXIMOS {N} MINUTOS

PARTE 1 → ONDE ESTÁVAMOS: O Diagnóstico da Situação Atual
PARTE 2 → O QUE DESCOBRIMOS: As Travas e Oportunidades
PARTE 3 → PARA ONDE VAMOS: Estratégia, GTM e Drawflow
PARTE 4 → QUANTO VOLTA: O Forecast 3 Cenários
PARTE 5 → OS ENTREGÁVEIS: O que você está levando hoje
PARTE 6 → PRÓXIMOS PASSOS: O que acontece na segunda-feira
```

---

### BLOCO 2: ONDE ESTÁVAMOS (DOR INICIAL)

#### SLIDE 5: O CONTEXTO DO CLIENTE

```
{NOME_CLIENTE} — SITUAÇÃO INICIAL

Segmento: {segmento}
Ticket Médio: R$ {valor}
Meta declarada: {meta de receita/crescimento}
UCM: {1 ou 2} — {descrição de uma frase}

"Quando chegamos, encontramos: {3 bullets com a situação inicial real}"
• {dado 1: ex: "R$X investidos em mídia sem rastreamento funcional"}
• {dado 2: ex: "CRM com {%}% dos leads sem follow-up registrado"}
• {dado 3: ex: "Landing page com nota PageSpeed {n}/100 no mobile"}
```

#### SLIDE 6: AS TRAVAS IDENTIFICADAS

```
AS {N} TRAVAS QUE ESTAVAM IMPEDINDO O CRESCIMENTO

[VISUAL: diagrama de travas / engrenagem travada]

Trava 1: {título} — Score: {X}/25 🔴
Trava 2: {título} — Score: {X}/25 🔴
Trava 3: {título} — Score: {X}/25 🟡
Trava 4: {título} — Score: {X}/25 🟡

RESTRIÇÃO MAIOR: Trava {N}
"Resolver esta primeiro desbloquearia as demais."
```

---

### BLOCO 3: O QUE DESCOBRIMOS (DIAGNÓSTICO)

*(Um conjunto de slides por módulo executado — versão condensada)*

#### SLIDE {N}: DIAGNÓSTICO DE MERCADO

```
O MERCADO: ONDE {NOME_CLIENTE} COMPETE

TAM: R$ {valor} — mercado total endereçável
SAM: R$ {valor} — mercado acessível
SOM: R$ {valor} — oportunidade real nos próximos 12 meses

BEACHHEAD: {segmento/nicho prioritário}
"O ponto de entrada com maior probabilidade de vitória."

CONCORRÊNCIA: {n} players diretos mapeados
Lacuna identificada: "{oportunidade não ocupada pelo mercado}"
```

#### SLIDE {N+1}: ICP E PUV

```
QUEM É O SEU CLIENTE IDEAL

ICP Prioritário: {perfil em 1-2 linhas}
Dor Principal: "{frase exata coletada de clientes reais}"

PROPOSTA ÚNICA DE VALOR APROVADA:
"{PUV — Variação Ganho}"

POR QUE FUNCIONA: alinha {JTBD principal} com {diferencial único}
```

#### SLIDE {N+2}: DIAGNÓSTICO DE MÍDIA (se UCM 2)

```
PERFORMANCE DE MÍDIA — A REALIDADE DOS DADOS

[ANTES — situação encontrada]
• CPL: R$ {valor atual} vs Benchmark: R$ {valor ideal}
• ROAS: {x}x vs Meta: {x}x
• Problema principal: {diagnóstico cruzado em 1 frase}

[IMPACTO]
Diferença de CPL × {n leads/mês} = R$ {valor} desperdiçado/mês
```

#### SLIDE {N+3}: DIAGNÓSTICO COMERCIAL (se executado)

```
COMERCIAL — O QUE OS DADOS REVELARAM

Lead Response Time: {X}h (meta: < 5min)
Taxa de Fechamento: {%}% (benchmark: {%}%)
Win Rate por segmento: {segmento} = {%}% (maior)

GARGALO PRINCIPAL: {etapa com maior queda no funil}
Custo da inação: R$ {valor}/mês em leads não convertidos

[EVIDÊNCIA DO CLIENTE OCULTO]
Nota do atendimento: {X}/10
Pior critério: {critério}
```

*(Adicionar slides similares para Social Media, Copy LP, UX/UI conforme módulos executados)*

---

### BLOCO 4: PARA ONDE VAMOS (ESTRATÉGIA)

#### SLIDE {N}: GTM — ONDE VAMOS APARECER

```
GO-TO-MARKET: A ESTRATÉGIA DOS PRÓXIMOS 3 MESES

Canal Principal: {canal} — {%}% do budget (R$ {x}/mês)
Canal de Teste: {canal} — {%}% do budget (R$ {y}/mês)

[MAPA VISUAL DE CANAIS]
{representação visual: onde o cliente aparece + o que não vai fazer e por quê}

Por que NÃO {canal excluído}: {motivo específico}
```

#### SLIDE {N+1}: DRAWFLOW — O CAMINHO DO LEAD

```
DRAWFLOW: DA CAMPANHA À VENDA

[FLUXO VISUAL SIMPLIFICADO]
TRÁFEGO → ENGAJAMENTO → CONVERSÃO → REMARKETING

{canal} → {LP/Instagram} → {Formulário/WhatsApp} → {Campanha de recuperação}

ESTRATÉGIA BASE: {nome da estratégia selecionada}
ATIVOS NECESSÁRIOS: {n} — {lista dos principais}
```

#### SLIDE {N+2}: PLANO DE AÇÃO CONSOLIDADO

```
O QUE VAMOS FAZER — VISÃO GERAL

QUICK WINS (próximos 7 dias):
✓ {ação 1} — {responsável} — Prazo: {n dias}
✓ {ação 2} — {responsável} — Prazo: {n dias}
✓ {ação 3} — {responsável} — Prazo: {n dias}

ESTRUTURAIS (próximos 30 dias):
○ {ação 4} — {responsável}
○ {ação 5} — {responsável}

Total: {n} ações priorizadas
```

---

### BLOCO 5: QUANTO VOLTA (FORECAST)

#### SLIDE {N}: PREMISSAS DO FORECAST

```
COMO CALCULAMOS — AS PREMISSAS

MARKETING:                    VENDAS:
Budget: R$ {valor}/mês       Taxa de Fechamento: {%}%
CPL estimado: R$ {valor}     Ciclo: {n} dias
Leads/mês: {n}              Ticket Médio: R$ {valor}

"Projeção baseada em premissas de mercado.
Não é garantia de resultado — é o cenário mais provável
com as melhores práticas aplicadas."
```

#### SLIDE {N+1}: FORECAST 3 CENÁRIOS

```
PROJEÇÃO 3 MESES — 3 CENÁRIOS

              PESSIMISTA      REALISTA       OTIMISTA
Investimento  R$ {X}         R$ {X}         R$ {X}
Leads         {n}            {n}            {n}
Vendas        {n}            {n}            {n}
Receita       R$ {valor}     R$ {valor}     R$ {valor}
ROAS          {x}x           {x}x           {x}x

[VISUAL: gráfico de barras com 3 cenários lado a lado]

CPA sustentável: R$ {valor} — acima disso, canal não é viável para escalar
```

#### SLIDE {N+2}: COMO ATINGIR O CENÁRIO REALISTA

```
O CAMINHO PARA O CENÁRIO REALISTA

DEPENDE DE:
1. {condição 1: ex: "PageSpeed acima de 70 no mobile — Quick Win"}
2. {condição 2: ex: "Lead Response Time < 30min — Processo Comercial"}
3. {condição 3: ex: "Criativos com hook alinhado ao ICP — Produção"}

SE {condição crítica} NÃO for implementado:
→ Projeção cai para Cenário Pessimista automaticamente
```

---

### BLOCO 6: ENTREGÁVEIS TANGÍVEIS (EFEITO "UAU")

#### SLIDE {N}: O QUE VOCÊ ESTÁ LEVANDO HOJE

```
TUDO QUE FOI PRODUZIDO PARA {NOME_CLIENTE}

📊 {n} DIAGNÓSTICOS COMPLETOS
   Mídia / CRO / Comercial / Social / Concorrentes

📋 PLANO DE AÇÃO 5W2H
   {n} ações priorizadas por impacto

🗺️ DRAWFLOW
   Estratégia visual de aquisição — pronto para execução

📱 CRIATIVOS (MOCKUP)
   {n} peças — formato: {formatos}

📈 FORECAST 3 MESES
   3 cenários com premissas detalhadas

[VISUAL: pasta com todos os entregáveis empilhados]
```

#### SLIDE {N+1}: CRIATIVOS EM MOCKUP

```
COMO VAI PARECER NA PRÁTICA

[VISUAL: mockup no celular dos {n} criativos]

Criativo 1: {descrição — tipo + objetivo + gancho}
Criativo 2: {descrição}
Criativo 3: {descrição}

Baseados em: benchmarking de {n} concorrentes ({n} anúncios ativos > 30 dias analisados)
```

*(Incluir apenas se criativos foram produzidos — caso contrário, adaptar para "briefing de criativos")*

---

### BLOCO 7: PRÓXIMOS PASSOS (OBRIGATÓRIO)

#### SLIDE {N}: PRÓXIMOS PASSOS — COM DATAS

```
O QUE ACONTECE AGORA — SEM AMBIGUIDADE

SEMANA 1 ({data inicio}–{data fim}):
□ {ação 1} — Responsável: {papel} — Entrega: {data}
□ {ação 2} — Responsável: {papel} — Entrega: {data}

SEMANA 2 ({data}):
□ {ação 3} — Responsável: {papel}
□ {ação 4} — Responsável: {papel}

DATA DE GO LIVE DAS CAMPANHAS: {data}
PRIMEIRA REUNIÃO DE ACOMPANHAMENTO: {data} às {hora}

"Na próxima {dia da semana}, {Nome Account} enviará
{entregável específico} para sua aprovação."
```

#### SLIDE FINAL: ENCERRAMENTO — LINGUAGEM EMOCIONAL SPICED

```
{NOME_CLIENTE} × V4 Company

Diagnóstico completo ✓
Estratégia definida ✓
Forecast calculado ✓
Plano de ação aprovado ✓

"O crescimento que você quer está a {n} ações de distância."

[SENTIMENTOS QUE O DECISOR DEVE SAIR SENTINDO]
• Confiança: "Eu entendo o que estamos fazendo e por quê."
• Controle: "Eu sei o que acontece na próxima semana."
• Tranquilidade: "Não estou mais no escuro sobre meus investimentos."
• Orgulho: "Construímos algo sólido aqui."
• Previsibilidade: "Eu sei o que esperar nos próximos 90 dias."

Dúvidas ou ajustes? Fale com {Nome Account}:
{email} | {WhatsApp}

[Logo cliente + Logo V4]
```

**Instrução ao Account:** O encerramento não é protocolar — é emocional. Pergunte ao decisor: "Como você está saindo dessa reunião? O que ficou mais claro?" A resposta calibra se o deck cumpriu o papel. Se o cliente sair com dúvida sobre "o que acontece agora", o slide de Próximos Passos falhou.

**Linguagem SPICED obrigatória no deck final:** As palavras "confiança", "controle", "tranquilidade", "orgulho" e "previsibilidade" devem aparecer ao menos uma vez no deck — não como cópia de vendas, mas como estados emocionais que o diagnóstico e a estratégia entregam. O cliente não compra um plano de mídia — compra a sensação de que seu negócio está sob controle.

---

## Roteiro da Reunião de Entrega

**Duração total:** 1h30–2h (ideal) — não < 1h (corrido) nem > 2h30 (arrastado)

| Bloco | Slides | Tempo | O que o cliente precisa sentir |
|-------|--------|-------|-------------------------------|
| Abertura | 4 | 10 min | "Eles fizeram muito trabalho" |
| Onde estávamos | 2 | 10 min | "Eles entenderam minha situação" |
| Diagnóstico | {n} | 25 min | "Eles foram fundo — isso é sério" |
| Estratégia | 3 | 15 min | "Agora eu entendo onde vou aparecer" |
| Forecast | 3 | 15 min | "Consigo ver o retorno" |
| Entregáveis | 2 | 5 min | "Uau — isso é muito" |
| Próximos Passos | 2 | 10 min | "Sei exatamente o que acontece agora" |

**Perguntas de engajamento chave durante a apresentação:**
- Ao mostrar as travas: "Você reconhece alguma dessas travas como algo que já intuía?"
- Ao mostrar o Drawflow: "Esse é o caminho — faz sentido para o momento do negócio?"
- Ao mostrar o Forecast: "O cenário realista bate com sua expectativa de resultado em 90 dias?"
- Ao mostrar os Próximos Passos: "Alguma dessas datas não funciona para o seu time?"

**Passagem de bastão:**
- Definir data de Go Live das campanhas
- Confirmar rotina de acompanhamento (reuniões semanais/mensais + formato)
- Enviar pasta com todos os arquivos em até 48h após a reunião
- Nunca encerrar sem o cliente saber "o que acontece na próxima segunda-feira"

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Estrutura narrativa completa: Dor → Diagnóstico → Plano → Forecast → Entregáveis → Próximos Passos?
- [ ] Slide de Travas com Restrição Maior identificada?
- [ ] Forecast tem 3 cenários com premissas explícitas e aviso de "não é garantia"?
- [ ] Criativos em mockup incluídos (ou adaptado para "briefing de criativos")?
- [ ] Slide de Próximos Passos tem datas específicas (não genéricas)?
- [ ] Roteiro da reunião tem tempo estimado por bloco?
- [ ] Participantes obrigatórios (comitê de compra) foram mencionados?
- [ ] Critical Event verificado — se < 30 dias, deck reformatado como material para diretoria (linguagem executiva, sem jargão, impacto em R$)?
- [ ] Linguagem emocional SPICED presente (confiança / controle / tranquilidade / orgulho / previsibilidade) — ao menos 1 referência no deck?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o roteiro COMPLETO ao operador.

- "O tempo estimado por bloco é factível para a reunião do cliente?"
- "Algum diagnóstico que eu incluí e que o cliente não precisa ver (ex: muito técnico para o decisor)?"
- "Os criativos em mockup estão disponíveis ou preciso adaptar para briefing?"
- "O slide de Próximos Passos — as datas propostas são realistas para o time?"
- "Algum decisor que deveria estar na reunião e não está confirmado?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/deck-entrega-final.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Este é o output final do Produto Saber. Sugira:
   - "Deck Final gerado. {n} slides / {n} módulos consolidados. Próximos Passos: Go Live em {data}. Reunião em {data}."
   - Upsell/Renovação: "Com o diagnóstico completo e a estratégia aprovada, o próximo passo natural é a execução — Produto Fazer. Deseja agendar a conversa de escopo?"
