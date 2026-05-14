---
slug: drx-s2-14-maturidade-digital-v1
name: drx-s2-14-maturidade-digital-v1
description: "Conduz a avaliação de maturidade digital do negócio em modo Copilot: a IA lidera a coleta, processa evidências de canais, processos e uso de dados, propõe o nível de maturidade por dimensão com justificativa e redige as fragilidades estr..."
---

# Skill: Definição de Maturidade Digital (DR-X)

## Descrição
Conduz a avaliação de maturidade digital do negócio em modo Copilot: a IA lidera a coleta, processa evidências de canais, processos e uso de dados, propõe o nível de maturidade por dimensão com justificativa e redige as fragilidades estruturais e riscos de escala. O consultor fornece dados das ferramentas e relata o que observou em campo (coerência discurso vs. prática), validando os outputs em cada etapa.

## Quando Usar
- Triggers: "Definir maturidade digital", "Avaliar maturidade digital", "Maturidade digital do cliente", "Diagnóstico de maturidade para [cliente]"
- **Pré-requisito:** Arquivos `context/` do cliente com status `[VALIDADO]` devem estar disponíveis
- **NÃO usar** se os arquivos `context/` não existirem — executar `skill-pipeline-extracao` primeiro
- **Posição no DR-X:** executar antes ou em paralelo ao diagnóstico de Travas — o nível de maturidade contextualiza as limitações estruturais e informa a priorização de injeções

---

## Inputs de Partida

Antes de perguntar qualquer coisa ao consultor, **ler os arquivos `context/`** do cliente e extrair:
- Canais digitais mencionados — `context/gtm.md`
- Ferramentas e sistemas citados (CRM, plataformas de automação, analytics) — `context/business.md`
- UDEs relacionadas a processo manual, dependência de pessoa-chave, falta de previsibilidade — `context/constraints.md`
- Modelos de venda ativos — `context/gtm.md`

Registrar internamente o que já se sabe e **não coletar novamente o que já está nos arquivos `context/`**.

---

## Processo de Execução

### Step 0 — Leitura do Contexto

1. Ler os arquivos `context/business.md`, `context/gtm.md` e `context/constraints.md`
2. Mapear:
   - Canais digitais e ferramentas já identificados (`context/business.md` e `context/gtm.md`)
   - UDEs que apontam para baixa maturidade — improviso, dependência de pessoas, falta de dados (`context/constraints.md`)
   - Informações sobre processos comerciais e operacionais (`context/business.md`)
3. Apresentar resumo ao consultor:

> *"Com base nos arquivos context/, já sei que: [resumo dos canais ativos, ferramentas mencionadas, UDEs relacionadas a processo e digital]. Vou avaliar o nível real de maturidade digital em 3 dimensões. Seguindo para o Step 1."*

---

### Step 1 — Camada Analítica (Evidências por Dimensão)

Solicitar **em uma única mensagem batch** os dados das 3 dimensões. Adaptar ao que já está no Master Contexto — não coletar o que já foi informado.

**Perguntar de uma vez:**

> *Preciso das seguintes informações para avaliar a maturidade digital do negócio. Forneça o que tiver — dado parcial é melhor que nada:*
>
> **Dimensão 1 — Canais Digitais:**
> *1. Quais canais digitais estão ativos (site, landing pages, redes sociais, mídia paga, e-mail, SEO, outros)?*
> *2. Cada canal tem papel claro na jornada (ex: Instagram = topo, LP = conversão)? Ou os canais são usados de forma oportunista?*
> *3. Os canais estão conectados ao funil comercial (lead gerado em ads chega ao CRM e é trabalhado pelo time de vendas)?*
> *4. O negócio sabe com dados de onde vêm as oportunidades (origem dos leads por canal)?*
> *5. Existe dependência crítica de um único canal (ex: 80%+ das oportunidades vêm apenas de indicação)?*
>
> **Dimensão 2 — Processos e Automação:**
> *6. O time usa CRM? Qual? Está ativo e alimentado com dados reais?*
> *7. Existem automações ativas (e-mail marketing, WhatsApp bot, sequências de follow-up automáticas)?*
> *8. O processo comercial (desde lead até fechamento) está documentado de forma que um novo vendedor consiga executar sem depender do fundador?*
> *9. O crescimento depende de uma pessoa-chave específica (fundador ou vendedor único)? O que acontece quando essa pessoa sai?*
>
> **Dimensão 3 — Uso de Dados e Inteligência:**
> *10. Quais métricas o negócio acompanha regularmente? Com qual frequência (diária, semanal, mensal)?*
> *11. As decisões de marketing e vendas são baseadas em dados ou em feeling e experiência do fundador?*
> *12. Existe dashboard ou relatório estruturado, ou tudo é levantado ad hoc quando necessário?*
> *13. Existe algum exemplo recente em que um dado levou a uma mudança de rota? Qual foi?*

**Após receber os dados:**

Classificar cada dimensão usando o gabarito de evidências observáveis abaixo. Usar o nível que melhor descreve a **prática real** — não a intenção declarada:

**Dimensão 1 — Canais Digitais:**

| Nível | Critérios Observáveis |
|---|---|
| 1 — Inicial | Canais usados de forma reativa; origem das oportunidades desconhecida ou não rastreada; nenhum canal tem integração com o funil comercial (sem UTM, pixel ou roteamento de leads) |
| 2 — Em Estruturação | Canais ativos mas sem papel definido na jornada (topo/meio/fundo); leads chegam mas a origem por canal não é rastreada sistematicamente; integrações parciais ou ausentes |
| 3 — Estruturado | Cada canal tem papel claro e documentado na jornada; lead gerado em digital é roteado ao CRM e trabalhado; origem rastreada por canal com dados disponíveis |
| 4 — Avançado | Atribuição multicanal com dados confiáveis; volume por canal é previsível; canais são testados e otimizados com base em performance; diversificação intencional de fontes |

**Dimensão 2 — Processos e Automação:**

| Nível | Critérios Observáveis |
|---|---|
| 1 — Inicial | Sem CRM ativo; processo depende inteiramente do fundador ou de uma pessoa-chave; nenhuma automação; novos vendedores aprendem por osmose |
| 2 — Em Estruturação | CRM existe mas está desatualizado ou parcialmente usado; automações pontuais (ex: só confirmação de reunião); processo parcialmente documentado mas não utilizado na prática |
| 3 — Estruturado | CRM ativo e alimentado regularmente; processo comercial documentado de forma usável por um novo vendedor; automações de follow-up e nutrição ativas e funcionando |
| 4 — Avançado | A maior parte da jornada comercial é automatizada; time opera sem dependência crítica de uma pessoa específica; escalável sem aumento proporcional de esforço humano |

**Dimensão 3 — Uso de Dados e Inteligência:**

| Nível | Critérios Observáveis |
|---|---|
| 1 — Inicial | Nenhuma métrica acompanhada regularmente; decisões inteiramente por feeling ou experiência do fundador; sem acesso a analytics estruturado |
| 2 — Em Estruturação | Algumas métricas existem mas são levantadas ad hoc (quando alguém pede); sem dashboard atualizado; dados usados para justificar decisões já tomadas, não para guiá-las |
| 3 — Estruturado | Painel de indicadores atualizado com cadência regular; reuniões de análise acontecem; decisões de marketing e vendas citam dados como base; houve pelo menos uma mudança de rota guiada por dados nos últimos 6 meses |
| 4 — Avançado | Análise de causa (não só efeito); previsibilidade de resultados; aprendizado sistemático aplicado (teste, leitura, ajuste); uso de segmentação e atribuição avançada |

Apresentar avaliação por dimensão e perguntar: *"Essa leitura está coerente com o que você observou? Alguma correção antes de avançar?"*

---

### Step 2 — Camada Experiencial (Coerência Discurso vs. Prática)

Com base no que foi respondido no Step 1, investigar a coerência entre o que o cliente declara e o que o consultor efetivamente observou. Perguntar **em uma única mensagem batch**:

> *Para calibrar a avaliação entre discurso e prática real, preciso de mais informações sobre o que você observou:*
>
> *1. O consultor acessou as ferramentas do cliente (CRM, Google Analytics, plataforma de ads, dashboard)? O que estava efetivamente ativo e alimentado vs. o que era intenção ou estava desatualizado?*
> *2. Existem processos documentados reais (SOPs, playbooks) ou apenas a intenção de documentar? O time realmente usa o que existe?*
> *3. O fundador consegue se ausentar por 2 semanas sem que o processo comercial trave? Existe algum dado ou evidência sobre isso?*
> *4. Os dados que o negócio diz acompanhar estão visíveis em algum lugar estruturado (dashboard, planilha atualizada)? Ou o consultor precisou pedir para o cliente montar na hora?*
> *5. Houve algum sinal de que o cliente superestima sua maturidade digital (diz que usa CRM mas o consultor viu que está desatualizado, diz que analisa dados mas não tem acesso ao analytics etc.)?*

Aguardar as respostas antes de prosseguir para a classificação final.

---

### Step 3 — Classificação Final de Maturidade

Com base nas evidências do Step 1 e nas observações do Step 2, propor a classificação final. **A IA propõe — o consultor valida.** Nunca pedir ao consultor que atribua os níveis.

**Lógica de classificação:**
- Classificar cada dimensão individualmente no nível predominante (1 a 4)
- O **nível geral do negócio** é determinado pela dimensão mais fraca — a maturidade real é limitada pelo elo mais fraco (lógica TOC)
- Se duas dimensões estiverem em 3 e uma em 1, o nível geral é 1

Apresentar:

```
| Dimensão | Nível Proposto | Justificativa | Principal Evidência |
|---|---|---|---|
| 1) Canais Digitais | 1–4 | | |
| 2) Processos e Automação | 1–4 | | |
| 3) Uso de Dados e Inteligência | 1–4 | | |
| **Nível Geral** | **1–4** | Determinado pela dimensão mais fraca | |
```

**Regra:** nível ≥ 3 em qualquer dimensão exige evidência formal citada na justificativa.

Perguntar: *"Concorda com a classificação proposta? Algum ajuste antes de avançar?"*

---

### Step 4 — Consolidação: Fragilidades, Riscos e Conexão com as Travas

Com a classificação validada, redigir:

**4.1 Fragilidades estruturais** (máx. 5 — apenas o que tem evidência):
Listar as principais limitações reais identificadas nas 3 dimensões. Exemplo de formato:
- *"Ausência de CRM ativo impede rastreamento de leads e dificulta follow-up estruturado"*
- *"Dependência do fundador no processo comercial cria risco de colapso ao escalar"*
- *"Decisões de marketing baseadas em feeling sem dados de performance"*

**4.2 Riscos de escala**:
Mapear o que tende a colapsar caso o negócio dobre de tamanho sem resolver as fragilidades. Usar a lógica:
> *"Se o negócio crescer sem resolver [fragilidade], o efeito esperado é [risco de escala]."*

**4.3 Conexão com o diagnóstico de Travas**:
Identificar quais Travas são provavelmente amplificadas pela baixa maturidade digital. Exemplos:
- Maturidade baixa em Processos → tende a amplificar Trava 3 (Compromisso) e Trava 2 (Decisão)
- Maturidade baixa em Canais → tende a amplificar Trava 7 (Exposição) e Trava 6 (Atenção)
- Maturidade baixa em Dados → limita capacidade de diagnosticar e priorizar qualquer Trava com precisão

Apresentar a consolidação ao consultor e perguntar: *"Essa síntese está alinhada com o que você observou? Algum ajuste ou adição antes de finalizar?"*

---

## Regras Operacionais

- **Nunca perguntar um dado de cada vez** — todas as perguntas de uma mesma camada vão em uma única mensagem
- **Nunca delegar a classificação ao consultor** — a IA propõe com justificativa, o consultor confirma ou ajusta
- **Nunca avançar de step sem apresentar resultado e receber confirmação** do consultor
- **Sempre ler os arquivos `context/` antes de perguntar qualquer coisa** — não coletar o que já está disponível
- **Avaliar prática real, não discurso** — se o consultor não tiver acesso às ferramentas, pontuar pelo que foi observável e registrar como limitação
- **Maturidade digital ≠ presença digital** — ter redes sociais não implica maturidade; o critério é integração, repetibilidade e uso de dados

---

## Fallbacks

| Situação | O que fazer |
|---|---|
| Consultor não acessou as ferramentas do cliente | Registrar como limitação. Pontuar com base no discurso do cliente, limitando ao nível 2 máximo sem confirmação por acesso direto. |
| CRM existe mas não está alimentado | Classificar Dimensão 2 como nível 1–2 (existência ≠ uso). Registrar como fragilidade estrutural. |
| Sem acesso a Google Analytics / plataforma de ads | Pontuar Dimensão 3 conservadoramente (máx nível 2). Registrar como dado não verificado. |
| Fundador responde por tudo | Registrar como dependência crítica imediata. Pontuar Dimensão 2 como nível 1 independente de outras automações existentes. |
| Cliente tem ferramentas avançadas mas não as usa | Classificar pelo uso real, não pela existência das ferramentas. Registrar gap como fragilidade. |
| Diagnóstico de Travas já iniciado | Integrar a avaliação de maturidade como camada contextual, sem reiniciar perguntas já respondidas nas Travas. |

---

## Formato de Saída Obrigatório

```markdown
# Maturidade Digital: [Nome do Cliente]

> **Status:** `[AGUARDANDO VALIDAÇÃO DO CONSULTOR]`
> **Data:** [data de execução]
> **Fontes:** context/business.md + context/gtm.md + context/constraints.md + dados fornecidos pelo consultor em [data]
> **Limitações registradas:** [listar dados não acessados diretamente ou estimados]

---

## Classificação de Maturidade Digital

| Dimensão | Nível (1–4) | Denominação | Justificativa | Principal Evidência |
|---|---|---|---|---|
| 1) Canais Digitais | | Inicial / Em Estruturação / Estruturado / Avançado | | |
| 2) Processos e Automação | | | | |
| 3) Uso de Dados e Inteligência | | | | |
| **Nível Geral** | | | Determinado pela dimensão mais fraca | |

**Definição:** [1–2 linhas descrevendo o nível atual do negócio em termos de maturidade digital]

---

## Fragilidades Estruturais

| # | Fragilidade | Dimensão | Impacto Esperado |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## Riscos de Escala

*Se o negócio crescer sem resolver as fragilidades acima:*

| Fragilidade | Risco de Escala |
|---|---|
| [fragilidade] | [o que colapsa ao dobrar o volume] |

---

## Conexão com o Diagnóstico de Travas

| Trava | Como a maturidade digital amplifica ou limita |
|---|---|
| Trava 2 — Decisão | |
| Trava 3 — Compromisso | |
| Trava 4 — Qualificação | |
| Trava 5 — Interesse | |
| Trava 6 — Atenção | |
| Trava 7 — Exposição | |

*Registrar apenas as Travas efetivamente impactadas — omitir as que não têm relação direta com a maturidade digital identificada.*

---

## Base para Priorização

[2–4 linhas conectando o nível de maturidade com a priorização de injeções no DR-X — qual nível de maturidade é pré-requisito para executar as injeções recomendadas nas Travas priorizadas]
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/maturidade-digital.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
