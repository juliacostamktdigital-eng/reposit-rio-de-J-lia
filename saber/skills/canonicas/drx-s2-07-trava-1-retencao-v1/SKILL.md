---
slug: drx-s2-07-trava-1-retencao-v1
name: drx-s2-07-trava-1-retencao-v1
description: "Conduz o diagnóstico completo da Trava 1 em modo Copilot: a IA lidera a coleta, processa os dados fornecidos pelo consultor, calcula LTV e cohort, propõe scores por dimensão com justificativa e redige a consolidação causal. O consultor f..."
---

# Skill: Diagnóstico de Trava 1 — Retenção (DR-X)

## Descrição
Conduz o diagnóstico completo da Trava 1 em modo Copilot: a IA lidera a coleta, processa os dados fornecidos pelo consultor, calcula LTV e cohort, propõe scores por dimensão com justificativa e redige a consolidação causal. O consultor fornece dados, responde perguntas sobre o que observou em campo e valida os outputs em cada etapa.

## Quando Usar
- Triggers: "Rodar diagnóstico Trava 1", "Diagnosticar retenção", "Analisar Trava 1", "Diagnóstico de retenção para [cliente]"
- **Pré-requisito:** Arquivos `context/` do cliente com status `[VALIDADO]` devem estar disponíveis
- **NÃO usar** se os arquivos `context/` não existirem — executar `skill-pipeline-extracao` primeiro

---

## Inputs de Partida

Antes de perguntar qualquer coisa ao consultor, **ler os arquivos `context/`** do cliente e extrair:
- Modelos de venda ativos — `context/gtm.md`
- Retenção e Continuidade (sinais já mapeados) — `context/constraints.md`
- UDEs relacionadas a churn, pós-venda ou dependência de aquisição — `context/constraints.md`
- Fluxos de receita (para identificar quais têm potencial de recorrência) — `context/business.md`

Registrar internamente o que já se sabe e **não coletar novamente o que já está nos arquivos `context/`**.

---

## Processo de Execução

### Step 0 — Leitura do Contexto

1. Ler os arquivos `context/business.md`, `context/gtm.md` e `context/constraints.md`
2. Mapear:
   - Quais modelos de venda estão ativos (`context/gtm.md`)
   - O que já foi capturado sobre retenção (`context/constraints.md`)
   - UDEs que apontam para sintomas da Trava 1 (`context/constraints.md`)
3. Apresentar ao consultor um resumo curto do que já se sabe sobre retenção, antes de pedir novos dados:

> *"Com base nos arquivos context/, já sei que: [resumo]. Vou precisar de dados adicionais para completar o diagnóstico. Seguindo para o Step 1."*

---

### Step 1 — Camada Analítica (Dados Econômicos)

Solicitar **em uma única mensagem batch** os dados necessários para a análise econômica. Adaptar a pergunta ao que já está disponível no Master Contexto — não pedir o que já foi informado.

**Perguntar de uma vez:**
> *Preciso dos seguintes dados para calcular LTV, cohort e % de receita recorrente. Pode fornecer o que tiver disponível — dado parcial é melhor do que nada, e registro as limitações:*
>
> *1. Base de clientes dos últimos 12 meses (pode ser colada em tabela, descrita em texto ou estimada). Idealmente: cliente, data de aquisição, receita total, produto e canal.*
> *2. Ticket médio por produto/serviço (se não tiver receita por cliente)*
> *3. Frequência média de compra por cliente*
> *4. Tempo médio de permanência (meses que um cliente típico fica ativo)*
> *5. CAC médio (custo de aquisição por cliente)*
> *6. % aproximado da receita que vem de clientes que já compraram antes (vs. novos)*

**Após receber os dados:**

Executar os seguintes cálculos e apresentar resultados antes de avançar:

**Cohort de Retenção** (se base de clientes disponível):
```
| Mês de Aquisição | Clientes Iniciais | Ativos após 3m | Ativos após 6m | Ativos após 12m |
```
Se não for possível construir o cohort: registrar como fragilidade estrutural e limitar score da Dimensão A ao máximo 2.

**LTV:**
- Se receita por cliente disponível: `LTV = receita total gerada / nº de clientes no período`
- Se não: `LTV = Ticket Médio × Frequência de Compra × Tempo de Permanência`
- Anotar qual metodologia foi usada e por quê

**Interpretação LTV vs CAC:**
- LTV ≤ CAC → retenção crítica ⚠️
- LTV < 3× CAC → risco estrutural
- LTV > 3× CAC → saudável

**% Receita Recorrente:** calcular proporção da receita vinda da base existente vs. novos clientes, por produto/serviço quando possível.

Apresentar todos os resultados e perguntar: *"Esses números fazem sentido com o que você observa? Alguma correção antes de avançar?"*

---

### Step 2 — Camada Experiencial (Observações de Campo)

Com base nos modelos de venda ativos identificados no Step 0, perguntar **em uma única mensagem batch** sobre o que o consultor observou ou tem evidências. Incluir apenas os modelos relevantes para aquele cliente.

**Se Inside Sales ativo:**
> *Sobre o processo pós-venda em Inside Sales:*
> - *Existe onboarding estruturado após o fechamento? Como é?*
> - *Existe reunião de acompanhamento definida? Com que frequência?*
> - *Após 30 dias, há contato proativo da empresa com o cliente?*
> - *Existe algum processo formal para reativar clientes inativos?*
> - *O cliente sabe qual é o próximo passo após a compra?*

**Se Vendas Online ativo:**
> *Sobre a jornada pós-compra online:*
> - *Existe comunicação automática após a compra (e-mail, SMS, WhatsApp)?*
> - *Existe oferta de recompra ou expansão no pós-venda?*
> - *Há remarketing ativo para a base de clientes existente?*

**Se PDV ativo:**
> *Sobre a experiência de loja:*
> - *É feito cadastro do cliente no momento da compra?*
> - *Existe convite explícito para retorno ou programa de fidelização?*
> - *Há comunicação futura com clientes que já compraram?*

Aguardar as respostas antes de prosseguir para o scoring.

---

### Step 3 — Scoring por Dimensão (A a E)

Com base nos dados do Step 1 e nas observações do Step 2, propor score para cada dimensão usando o gabarito abaixo. **A IA propõe — o consultor valida.** Nunca pedir ao consultor que atribua as notas.

**Gabarito de referência** (`context/context-trava-1-retencao.md`):

| Nota | A) Dados Estruturados | B) Receita Recorrente | C) Jornada Pós-Venda | D) Política de Continuidade | E) Expansão |
|---|---|---|---|---|---|
| 0 | Inexistente | Inexistente | Inexistente | Inexistente | Inexistente |
| 1 | Fragmentado | Residual | Reativa | Improviso | Ocasional |
| 2 | Básico sem segmentação | Instável | Pontual | Intenção não formalizada | Pontual |
| 3 | Consistente ≥ 6 meses | Parcialmente previsível | Definida | Documentada parcialmente | Estruturada básica |
| 4 | Segmentado com coorte | Consistente | Padronizada | Aplicada consistentemente | Estruturada com métricas |
| 5 | Monitorado continuamente | Pilar central | Governada | Política governante | Integrada à estratégia central |

**Regra:** nota > 3 exige evidência formal citada na justificativa.

Apresentar tabela completa com proposta de score, justificativa e evidência que sustenta cada nota. Perguntar: *"Concorda com os scores propostos? Algum ajuste antes de calcular o total?"*

---

### Step 4 — Consolidação Causal

Com o scoring validado, redigir a hipótese causal no formato obrigatório:

> *"A empresa opera sob a política implícita de ___, gerando ___, limitando o crescimento cumulativo."*

**Orientação:** identificar a política organizacional (não o sintoma operacional) que explica por que a retenção não existe. Exemplos de política implícita: "priorizar volume de novas vendas sobre relacionamento com a base", "tratar cada venda como evento isolado sem continuidade planejada", "ausência de responsável formal pelo pós-venda".

Apresentar a hipótese para o consultor e aguardar validação ou ajuste.

---

### Step 5 — Determinação Preliminar

Aplicar os três critérios de governância:

1. Score total ≤ 15?
2. LTV calculado limita o crescimento (LTV ≤ 3× CAC ou não sustenta operação sem aquisição constante)?
3. Resolver retenção aumentaria o Throughput mais do que intensificar aquisição?

Declarar explicitamente: **"Trava 1 é / não é potencial governante"**, com o raciocínio que sustenta a decisão.

Registrar que a validação final é feita na CRT.

---

## Regras Operacionais

- **Nunca perguntar um dado de cada vez** — todas as perguntas de uma mesma camada vão em uma única mensagem
- **Nunca delegar o scoring ao consultor** — a IA propõe com justificativa, o consultor confirma ou ajusta
- **Nunca avançar de step sem apresentar resultado e receber confirmação** do consultor
- **Sempre ler os arquivos `context/` antes de perguntar qualquer coisa** — não coletar o que já está disponível
- **Dados parciais são aceitos** — calcular com o disponível e registrar limitações explicitamente no output
- **Não fazer cálculos implícitos** — mostrar o raciocínio matemático antes de apresentar o resultado final

---

## Fallbacks

| Situação | O que fazer |
|---|---|
| Cohort impossível de construir | Limitar score Dimensão A ao máximo 2. Registrar como fragilidade estrutural no output. |
| CAC não disponível | Calcular LTV normalmente. Registrar ausência do CAC na interpretação — não fazer comparação LTV vs CAC. |
| Sem dados de recompra | Usar frequência declarada como proxy. Anotar estimativa no output. |
| Histórico < 6 meses | Registrar limitação. Calcular com o disponível. Limitar score Dimensão A ao máximo 2. |
| Modelo de venda não aplicável ao cliente | Pular seção experiencial correspondente. Registrar motivo. |
| Consultor não souber responder sobre pós-venda | Pontuar a dimensão correspondente como 0–1 e registrar como dado não confirmado. |

---

## Formato de Saída Obrigatório

```markdown
# Diagnóstico Trava 1 — Retenção: [Nome do Cliente]

> **Status:** `[AGUARDANDO VALIDAÇÃO DO CONSULTOR]`
> **Data:** [data de execução]
> **Fontes:** context/business.md + context/gtm.md + context/constraints.md + dados fornecidos pelo consultor em [data]
> **Limitações registradas:** [listar dados ausentes ou estimados]

---

## Pergunta Estruturante

*"Se a empresa parar de adquirir novos clientes por 90 dias, o faturamento se sustenta?"*

**Resposta com base no diagnóstico:** [Não / Parcialmente / Sim — justificativa em 2–3 linhas]

---

## Análise Econômica

### Cohort de Retenção
[Tabela ou nota de fragilidade estrutural se não foi possível construir]

### LTV vs CAC
- **LTV calculado:** R$ [valor] — método: [real / estimado]
- **CAC médio:** R$ [valor] / [não disponível]
- **Relação LTV/CAC:** [X]× → [interpretação: crítico / risco / saudável]

### Receita Recorrente
- **% da receita vinda da base:** [X]%
- **Análise por produto:** [descrição]

---

## Scorecard de Retenção por Produto

| Produto | Receita Recorrente (%) | Recompra (%) | Permanência Média | LTV | Obs. |
|---|---|---|---|---|---|
| [produto] | | | | | |

---

## Score da Trava 1

| Dimensão | Score (0–5) | Justificativa | Evidência |
|---|---|---|---|
| A) Dados Estruturados de Retenção | | | |
| B) Receita Recorrente Relevante | | | |
| C) Jornada Formal de Pós-Venda | | | |
| D) Política Clara de Continuidade | | | |
| E) Estratégia Ativa de Expansão | | | |
| **Total (0–25)** | | | |

**Faixa:** [0–10 / 11–15 / 16–20 / 21–25] — [interpretação]

---

## Consolidação Causal

*"A empresa opera sob a política implícita de ___, gerando ___, limitando o crescimento cumulativo."*

---

## Determinação Preliminar

- Score ≤ 15? [Sim / Não]
- LTV limita crescimento? [Sim / Não — justificativa]
- Resolver retenção aumenta Throughput mais que aquisição? [Sim / Não — justificativa]

**Trava 1 é / não é potencial governante.** Validação final na CRT.
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/trava-1-retencao.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
