---
slug: drx-s2-12-trava-6-atencao-v1
name: drx-s2-12-trava-6-atencao-v1
description: "Conduz o diagnóstico completo da Trava 6 em modo Copilot: a IA lidera a coleta, processa dados de performance de campanhas e criativos, analisa o nível de diferenciação vs. concorrentes, propõe scores por dimensão com justificativa e red..."
---

# Skill: Diagnóstico de Trava 6 — Atenção (DR-X)

## Descrição
Conduz o diagnóstico completo da Trava 6 em modo Copilot: a IA lidera a coleta, processa dados de performance de campanhas e criativos, analisa o nível de diferenciação vs. concorrentes, propõe scores por dimensão com justificativa e redige a consolidação causal. O consultor fornece dados das plataformas de mídia e relata o que observou na análise de criativos e comunicação, validando os outputs em cada etapa.

## Quando Usar
- Triggers: "Rodar diagnóstico Trava 6", "Diagnosticar atenção", "Analisar Trava 6", "Diagnóstico de atenção para [cliente]"
- **Pré-requisito:** Arquivos `context/` do cliente com status `[VALIDADO]` devem estar disponíveis
- **NÃO usar** se os arquivos `context/` não existirem — executar `skill-pipeline-extracao` primeiro

---

## Inputs de Partida

Antes de perguntar qualquer coisa ao consultor, **ler os arquivos `context/`** do cliente e extrair:
- Modelos de venda ativos — `context/gtm.md`
- Canais de aquisição ativos e orçamento de marketing mencionado — `context/gtm.md`
- UDEs relacionadas a baixo CTR, custo por lead alto, criativos genéricos, baixo retorno de campanhas, invisibilidade da marca — `context/constraints.md`
- Informações sobre o time de marketing ou gestão de tráfego — `context/business.md`

Registrar internamente o que já se sabe e **não coletar novamente o que já está nos arquivos `context/`**.

---

## Processo de Execução

### Step 0 — Leitura do Contexto

1. Ler os arquivos `context/business.md`, `context/gtm.md` e `context/constraints.md`
2. Mapear:
   - Quais canais de aquisição estão ativos (`context/gtm.md`)
   - O que já foi capturado sobre performance de marketing e criativos (`context/gtm.md`)
   - UDEs que apontam fraqueza na captura de atenção (`context/constraints.md`)
3. Apresentar resumo ao consultor:

> *"Com base nos arquivos context/, já sei que: [resumo dos canais ativos, orçamento, UDEs sobre performance]. Vou analisar a capacidade do sistema de capturar atenção. Seguindo para o Step 1."*

---

### Step 1 — Camada Analítica (Performance de Atenção)

Solicitar **em uma única mensagem batch** os dados de performance. Adaptar ao que já está no Master Contexto.

**Perguntar de uma vez:**
> *Preciso dos seguintes dados para avaliar a capacidade do sistema de capturar atenção. Forneça o que tiver disponível:*
>
> *1. CTR médio das campanhas ativas nos últimos 3–6 meses (por canal: Meta Ads, Google Ads, LinkedIn etc.)*
> *2. Taxa de visualização de vídeos, se aplicável: percentual que assiste até 3s, 25%, 50%*
> *3. CPM médio e custo por clique nos principais canais*
> *4. Engajamento orgânico nas redes: curtidas, comentários, compartilhamentos médios por post*
> *5. Existe algum benchmark de referência para o setor (CTR esperado, CPM médio do segmento)?*
> *6. Qual foi o anúncio ou criativo com melhor performance nos últimos 3 meses? Por que acreditam que funcionou?*

**Após receber os dados:**

Identificar campanhas com maior e menor performance e classificar a performance geral:
- **CTR < 1% em tráfego pago** → tendência de fraqueza de atenção (varia por canal e setor)
- **CPM alto + engajamento baixo** → criativos não interrompem o padrão do público
- **Melhor peça = única que funciona** → ausência de sistema de captura de atenção
- **Sem dados de performance** → ausência de mídia estruturada; registrar como fragilidade estrutural

Apresentar análise e perguntar: *"Essa leitura faz sentido com o que você observa? Alguma correção antes de avançar?"*

---

### Step 2 — Camada Experiencial (Análise de Criativos e Diferenciação)

Com base nos modelos de venda ativos identificados no Step 0, perguntar **em uma única mensagem batch**. Incluir apenas os modelos relevantes.

**Se Inside Sales ativo:**
> *Sobre a primeira abordagem ativa (outbound / cold outreach):*
> - *A primeira mensagem de abordagem (e-mail, WhatsApp, LinkedIn) gera resposta ou tende a ser ignorada?*
> - *Existe personalização real (referência à dor específica do prospect) ou é uma mensagem padrão enviada para todos?*
> - *A primeira linha / assunto da mensagem é diferente do que os concorrentes enviam?*
> - *Qual a taxa de resposta ao primeiro contato ativo — tem algum dado ou estimativa?*

**Se Vendas Online ativo:**
> *Sobre criativos e anúncios pagos:*
> - *O consultor analisou os anúncios ativos do cliente — qual o nível de diferenciação visual e de copy em relação aos concorrentes?*
> - *Os criativos têm headline que interrompe o padrão (chama atenção nos primeiros 2–3 segundos) ou são genéricos?*
> - *O consultor comparou os anúncios do cliente com os de 3–5 concorrentes principais (via biblioteca de anúncios do Meta / Google)? O que observou?*
> - *Qual a promessa principal dos anúncios — é específica e diferenciada ou poderia ser de qualquer empresa do setor?*

**Se PDV ativo:**
> *Sobre a atenção física no ponto de venda:*
> - *A fachada e a comunicação visual externa da loja chamam atenção em relação aos concorrentes próximos?*
> - *A promessa visual é clara e diferenciada, ou segue o padrão genérico do setor?*

Aguardar as respostas antes de prosseguir para o scoring.

---

### Step 3 — Scoring por Dimensão (A a E)

Com base nos dados do Step 1 e nas observações do Step 2, propor score para cada dimensão usando o gabarito abaixo. **A IA propõe — o consultor valida.** Nunca pedir ao consultor que atribua as notas.

**Gabarito de referência** (`context/context-trava-6-atencao.md`):

| Nota | A) CTR / Resposta | B) Diferenciação | C) Clareza da Promessa | D) Força de Interrupção | E) Competitividade |
|---|---|---|---|---|---|
| 0 | Inexistente | Genérico | Confusa | Invisível | Muito inferior |
| 1 | Muito abaixo | Quase igual | Vaga | Fraca | Inferior |
| 2 | Abaixo aceitável | Leve | Pouco específica | Limitada | Semelhante |
| 3 | Aceitável | Moderada | Clara | Adequada | Competitivo |
| 4 | Acima da média | Clara | Muito clara | Forte | Acima da média |
| 5 | Altamente eficiente | Altamente distinta | Impossível ignorar | Altamente impactante | Dominante |

**Regra:** nota > 3 exige evidência formal citada na justificativa.

Apresentar tabela completa com proposta de score, justificativa e evidência que sustenta cada nota. Perguntar: *"Concorda com os scores propostos? Algum ajuste antes de calcular o total?"*

---

### Step 4 — Consolidação Causal

Com o scoring validado, redigir a hipótese causal no formato obrigatório:

> *"A empresa opera sob a política implícita de ___, o que gera comunicação pouco diferenciada e baixa captura de atenção, limitando o volume e qualidade de entrada no funil."*

**Orientação:** identificar a política que explica a fraqueza de atenção. Exemplos: "imitar o padrão de comunicação dos concorrentes para parecer legítima", "evitar posicionamento forte para não polarizar", "priorizar segurança criativa sobre diferenciação".

Apresentar a hipótese para o consultor e aguardar validação ou ajuste.

---

### Step 5 — Determinação Preliminar

Aplicar os três critérios de governância:

1. Score total ≤ 15?
2. Baixa atenção limita diretamente a geração de oportunidades (melhorar decisão ou retenção não resolve o volume)?
3. Resolver atenção aumentaria significativamente a entrada no funil?

Declarar explicitamente: **"Trava 6 é / não é potencial governante"**, com o raciocínio que sustenta a decisão.

Registrar que a validação final é feita na CRT.

---

## Regras Operacionais

- **Nunca perguntar um dado de cada vez** — todas as perguntas de uma mesma camada vão em uma única mensagem
- **Nunca delegar o scoring ao consultor** — a IA propõe com justificativa, o consultor confirma ou ajusta
- **Nunca avançar de step sem apresentar resultado e receber confirmação** do consultor
- **Sempre ler os arquivos `context/` antes de perguntar qualquer coisa** — não coletar o que já está disponível
- **Ausência de dados de ads não bloqueia o diagnóstico** — registrar como fragilidade estrutural e focar na análise qualitativa dos criativos e mensagens

---

## Fallbacks

| Situação | O que fazer |
|---|---|
| Sem dados de CTR / anúncios pagos | Registrar como fragilidade estrutural. Pontuar Dim A com base na percepção do consultor (máx 2). Focar análise na qualidade dos criativos e no canal predominante. |
| Análise de concorrentes não realizada | Pontuar Dim B e E conservadoramente. Registrar como "não confirmado por análise direta". |
| Sem mídia paga ativa | Adaptar análise para o canal ativo (outbound, orgânico, PDV). Não pontuar dimensões de ads se o canal não for usado. |
| Canal principal é outbound sem digital | Focar Dim A na taxa de resposta ao cold outreach. Adaptar Dim B ao nível de personalização das mensagens. |
| Modelo de venda não aplicável | Pular seção experiencial correspondente. Registrar motivo. |
| Consultor não souber descrever os criativos | Pontuar Dim B, C e D como 0–1 e registrar como dado não confirmado. |

---

## Formato de Saída Obrigatório

```markdown
# Diagnóstico Trava 6 — Atenção: [Nome do Cliente]

> **Status:** `[AGUARDANDO VALIDAÇÃO DO CONSULTOR]`
> **Data:** [data de execução]
> **Fontes:** context/business.md + context/gtm.md + context/constraints.md + dados fornecidos pelo consultor em [data]
> **Limitações registradas:** [listar dados ausentes ou estimados]

---

## Pergunta Estruturante

*"A comunicação interrompe e prende ou é apenas mais uma peça no feed?"*

**Resposta com base no diagnóstico:** [resposta em 2–3 linhas]

---

## Análise de Performance de Atenção

| Canal | CTR Médio | CPM | Engajamento | Benchmark Referência | Avaliação |
|---|---|---|---|---|---|
| [canal] | | | | | Fraco / Aceitável / Forte |

**Melhor criativo / peça identificada:** [descrição]
**Principal sinal de fraqueza de atenção:** [dado ou percepção]

---

## Painel Comparativo (vs. Concorrentes)

| Elemento | Cliente | Concorrente 1 | Concorrente 2 | Diferenciação |
|---|---|---|---|---|
| Headline / Abertura | | | | Baixa / Média / Alta |
| Promessa Principal | | | | |
| Visual / Formato | | | | |
| Gatilho de Atenção | | | | |

*[Preencher com o disponível — registrar "não analisado" quando ausente]*

---

## Score da Trava 6

| Dimensão | Score (0–5) | Justificativa | Evidência |
|---|---|---|---|
| A) CTR / Taxa de Resposta Inicial | | | |
| B) Diferenciação vs. Concorrência | | | |
| C) Clareza da Promessa | | | |
| D) Força de Interrupção de Padrão | | | |
| E) Competitividade Geral | | | |
| **Total (0–25)** | | | |

**Faixa:** [0–10 / 11–15 / 16–20 / 21–25] — [interpretação]

---

## Consolidação Causal

*"A empresa opera sob a política implícita de ___, o que gera comunicação pouco diferenciada e baixa captura de atenção, limitando o volume e qualidade de entrada no funil."*

---

## Determinação Preliminar

- Score ≤ 15? [Sim / Não]
- Baixa atenção limita geração de oportunidades (melhorar decisão não resolve volume)? [Sim / Não — justificativa]
- Resolver atenção aumenta significativamente o topo do funil? [Sim / Não — justificativa]

**Trava 6 é / não é potencial governante.** Validação final na CRT.
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/trava-6-atencao.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
