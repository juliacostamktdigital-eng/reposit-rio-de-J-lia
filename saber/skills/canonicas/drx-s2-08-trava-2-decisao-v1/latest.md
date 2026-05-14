---
slug: drx-s2-08-trava-2-decisao-v1
name: drx-s2-08-trava-2-decisao-v1
description: "Conduz o diagnóstico completo da Trava 2 em modo Copilot: a IA lidera a coleta, processa os dados fornecidos pelo consultor, constrói a linha do tempo de conversão, propõe scores por dimensão com justificativa e redige a consolidação cau..."
---

# Skill: Diagnóstico de Trava 2 — Decisão (DR-X)

## Descrição
Conduz o diagnóstico completo da Trava 2 em modo Copilot: a IA lidera a coleta, processa os dados fornecidos pelo consultor, constrói a linha do tempo de conversão, propõe scores por dimensão com justificativa e redige a consolidação causal. O consultor fornece dados do CRM, relata observações de campo (mystery shopping) e valida os outputs em cada etapa.

## Quando Usar
- Triggers: "Rodar diagnóstico Trava 2", "Diagnosticar decisão", "Analisar Trava 2", "Diagnóstico de decisão para [cliente]"
- **Pré-requisito:** Arquivos `context/` do cliente com status `[VALIDADO]` devem estar disponíveis
- **NÃO usar** se os arquivos `context/` não existirem — executar `skill-pipeline-extracao` primeiro

---

## Inputs de Partida

Antes de perguntar qualquer coisa ao consultor, **ler os arquivos `context/`** do cliente e extrair:
- Modelos de venda ativos — `context/gtm.md`
- Ciclo médio de vendas e entrega já declarado — `context/gtm.md`
- UDEs relacionadas a propostas abertas, follow-up, "vou pensar", ciclos longos — `context/constraints.md`
- Canais de aquisição e time comercial — `context/gtm.md`

Registrar internamente o que já se sabe e **não coletar novamente o que já está nos arquivos `context/`**.

---

## Processo de Execução

### Step 0 — Leitura do Contexto

1. Ler os arquivos `context/business.md`, `context/gtm.md` e `context/constraints.md`
2. Mapear:
   - Quais modelos de venda estão ativos (`context/gtm.md`)
   - O que já foi capturado sobre ciclo de vendas e fechamento (`context/gtm.md`)
   - UDEs que apontam sintomas da Trava 2 (`context/constraints.md`)
3. Apresentar resumo ao consultor antes de pedir novos dados:

> *"Com base nos arquivos context/, já sei que: [resumo do ciclo de vendas, UDEs relevantes, canais ativos]. Vou precisar de dados adicionais para completar o diagnóstico. Seguindo para o Step 1."*

---

### Step 1 — Camada Analítica (Dados de Conversão)

Solicitar **em uma única mensagem batch** os dados necessários para a análise de decisão. Adaptar ao que já está disponível no Master Contexto.

**Perguntar de uma vez:**
> *Preciso dos seguintes dados para construir a linha do tempo de decisão e calcular a taxa de conversão. Forneça o que tiver — dado parcial é melhor que nada:*
>
> *1. Total de propostas enviadas nos últimos 6–12 meses (por canal, se possível)*
> *2. Taxa de fechamento atual (ou estimativa: "fechamos ~X% das propostas")*
> *3. Tempo médio até o fechamento, desde o primeiro contato (ou percepção: "leva em média X semanas")*
> *4. Principais motivos de perda registrados — ou os mais frequentes na percepção do time*
> *5. Distribuição dos resultados por canal (ex: 70% fecharmos via indicação, 30% via outbound)*
> *6. Volume atual de propostas em aberto sem resposta (pipeline travado)*

**Após receber os dados:**

Construir e apresentar a Linha do Tempo de Decisão:

```
| Canal | Proposta Enviada | Tempo Médio p/ Decisão | Taxa de Fechamento | Status Predominante |
```

Calcular:
- **Tempo médio de decisão** por canal (se disponível)
- **% de propostas que não decidem** (travadas em aberto)
- **Taxa de conversão geral** — comparar com benchmarks típicos do setor quando possível

**Interpretação:**
- Ciclo > 30 dias com alta variância → forte indício de trava
- Pipeline inflado (muitas propostas sem desfecho) → decisão pode ser a restrição
- Motivos de perda concentrados em "vou pensar" / "sem retorno" → confirma Trava 2

Apresentar resultados e perguntar: *"Esses números fazem sentido com o que você observa? Alguma correção antes de avançar?"*

---

### Step 2 — Camada Experiencial (Observações de Campo)

Com base nos modelos de venda ativos identificados no Step 0, perguntar **em uma única mensagem batch** sobre o que o consultor observou ou tem evidências. Incluir apenas os modelos relevantes para aquele cliente.

**Se Inside Sales ativo:**
> *Sobre o processo de fechamento em Inside Sales:*
> - *O consultor realizou algum cliente oculto (mystery shopping) no processo de proposta/fechamento? Se sim, o que observou?*
> - *A proposta enviada tem: clareza do valor, personalização para a dor do cliente, prazo explícito para decisão e chamada clara para ação?*
> - *Existe follow-up estruturado após o envio da proposta? Com cadência definida (D+1, D+3, D+7)?*
> - *O vendedor pede decisão de forma ativa, ou apenas envia a proposta e aguarda?*
> - *Como objeções são tratadas — existe script ou depende do improviso?*

**Se Vendas Online ativo:**
> *Sobre a jornada de conversão online:*
> - *A página de checkout ou oferta tem provas sociais, garantias, escassez ou urgência explícita?*
> - *Quantas etapas e campos o checkout/formulário de compra tem?*
> - *Existe recuperação de carrinho abandonado ou remarketing ativo para quem não decidiu?*

**Se PDV ativo:**
> *Sobre a experiência de conversão no ponto de venda:*
> - *O atendente faz convite explícito à compra com argumento de valor?*
> - *Existe incentivo de fechamento (condição especial, prazo, benefício imediato para decidir agora)?*
> - *Como o vendedor responde a objeções — existe roteiro ou improviso?*

Aguardar as respostas antes de prosseguir para o scoring.

---

### Step 3 — Scoring por Dimensão (A a E)

Com base nos dados do Step 1 e nas observações do Step 2, propor score para cada dimensão usando o gabarito abaixo. **A IA propõe — o consultor valida.** Nunca pedir ao consultor que atribua as notas.

**Gabarito de referência** (`context/context-trava-2-decisao.md`):

| Nota | A) Taxa de Conversão | B) Tempo Médio de Decisão | C) Estrutura da Proposta | D) Follow-up | E) Urgência |
|---|---|---|---|---|---|
| 0 | Inexistente | Excessivamente longo | Inexistente | Inexistente | Inexistente |
| 1 | Muito abaixo da média | Longo e variável | Genérica | Eventual | Implícita |
| 2 | Abaixo do aceitável | Inconsistente | Pouco personalizada | Irregular | Ocasional |
| 3 | Média de mercado | Previsível | Clara e direcionada | Estruturado básico | Explícita |
| 4 | Acima da média | Curto e previsível | Personalizada com prova | Cadência definida | Estruturada |
| 5 | Altamente eficiente | Otimizado e controlado | Estruturada para fechamento | Governado com métricas | Parte central da arquitetura |

**Regra:** nota > 3 exige evidência formal citada na justificativa.

Apresentar tabela completa com proposta de score, justificativa e evidência que sustenta cada nota. Perguntar: *"Concorda com os scores propostos? Algum ajuste antes de calcular o total?"*

---

### Step 4 — Consolidação Causal

Com o scoring validado, redigir a hipótese causal no formato obrigatório:

> *"A empresa opera sob a política implícita de ___, o que ___, reduzindo conversão e limitando o Throughput."*

**Orientação:** identificar a política organizacional (não o sintoma operacional) que explica por que a decisão não acontece. Exemplos: "evitar pressão de fechamento para não parecer agressiva", "tratar o envio da proposta como fim do processo", "não estabelecer prazo ou condição que crie urgência real".

Apresentar a hipótese para o consultor e aguardar validação ou ajuste.

---

### Step 5 — Determinação Preliminar

Aplicar os três critérios de governância:

1. Score total ≤ 15?
2. A conversão limita o crescimento mais do que a geração de leads (pipeline infla sem converter)?
3. Resolver decisão aumentaria o Throughput mais do que intensificar aquisição?

Declarar explicitamente: **"Trava 2 é / não é potencial governante"**, com o raciocínio que sustenta a decisão.

Registrar que a validação final é feita na CRT.

---

## Regras Operacionais

- **Nunca perguntar um dado de cada vez** — todas as perguntas de uma mesma camada vão em uma única mensagem
- **Nunca delegar o scoring ao consultor** — a IA propõe com justificativa, o consultor confirma ou ajusta
- **Nunca avançar de step sem apresentar resultado e receber confirmação** do consultor
- **Sempre ler os arquivos `context/` antes de perguntar qualquer coisa** — não coletar o que já está disponível
- **Dados parciais são aceitos** — calcular com o disponível e registrar limitações explicitamente no output
- **Mystery shopping não é pré-requisito para rodar o skill** — se não foi realizado, pontuar as dimensões correspondentes de forma conservadora e registrar como dado não confirmado

---

## Fallbacks

| Situação | O que fazer |
|---|---|
| Sem dados de propostas no CRM | Usar percepção declarada como proxy. Limitar score Dimensão A ao máximo 2. Registrar como fragilidade estrutural. |
| Mystery shopping não realizado | Perguntar ao consultor o que observou no processo normal. Pontuar Dim C e E conservadoramente. Registrar como "não confirmado por observação direta". |
| Sem motivos de perda mapeados | Registrar como fragilidade estrutural. Pontuar Dim A com base na taxa de fechamento disponível. |
| Histórico < 6 meses | Calcular com o disponível. Registrar limitação. |
| Modelo de venda não aplicável | Pular seção experiencial correspondente. Registrar motivo. |
| Consultor não souber responder sobre proposta/follow-up | Pontuar as dimensões correspondentes (C, D, E) como 0–1 e registrar como dado não confirmado. |

---

## Formato de Saída Obrigatório

```markdown
# Diagnóstico Trava 2 — Decisão: [Nome do Cliente]

> **Status:** `[AGUARDANDO VALIDAÇÃO DO CONSULTOR]`
> **Data:** [data de execução]
> **Fontes:** context/business.md + context/gtm.md + context/constraints.md + dados fornecidos pelo consultor em [data]
> **Limitações registradas:** [listar dados ausentes ou estimados]

---

## Pergunta Estruturante

*"O sistema conduz naturalmente à decisão ou empurra o cliente indefinidamente?"*

**Resposta com base no diagnóstico:** [resposta em 2–3 linhas]

---

## Análise de Conversão

### Linha do Tempo de Decisão

| Canal | Tempo Médio até Decisão | Taxa de Fechamento | Propostas em Aberto | Status Predominante |
|---|---|---|---|---|
| [canal] | | | | |

### Interpretação
- **Tempo médio geral:** [X dias/semanas] — método: [real / estimado]
- **% de propostas sem desfecho:** [X]%
- **Principal motivo de perda:** [dado ou "não mapeado"]
- **Sinal de trava:** [sim/não — justificativa]

---

## Matriz de Decisão

| Elemento | Existe? | Qualidade | Evidência | Impacto na Decisão |
|---|---|---|---|---|
| Clareza da Proposta | | | | |
| Prazo / Deadline | | | | |
| Follow-up Estruturado | | | | |
| Resolução de Objeções | | | | |
| Chamada Clara para Ação | | | | |

---

## Score da Trava 2

| Dimensão | Score (0–5) | Justificativa | Evidência |
|---|---|---|---|
| A) Taxa de Conversão | | | |
| B) Tempo Médio de Decisão | | | |
| C) Estrutura da Proposta | | | |
| D) Follow-up Estruturado | | | |
| E) Arquitetura de Urgência | | | |
| **Total (0–25)** | | | |

**Faixa:** [0–10 / 11–15 / 16–20 / 21–25] — [interpretação]

---

## Consolidação Causal

*"A empresa opera sob a política implícita de ___, o que ___, reduzindo conversão e limitando o Throughput."*

---

## Determinação Preliminar

- Score ≤ 15? [Sim / Não]
- Conversão limita crescimento mais que geração de leads? [Sim / Não — justificativa]
- Resolver decisão aumenta Throughput mais que aquisição? [Sim / Não — justificativa]

**Trava 2 é / não é potencial governante.** Validação final na CRT.
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/trava-2-decisao.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
