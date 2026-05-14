---
slug: drx-s2-05-fluxo-receita-v1
name: drx-s2-05-fluxo-receita-v1
description: "Conduz o mapeamento completo do fluxo de receita em modo Copilot: a IA lidera a coleta estruturada das etapas do fluxo, identifica dependências, analisa gargalos e propõe hipóteses iniciais de restrição sob a lente TOC. O consultor descr..."
---

# Skill: Mapeamento do Fluxo de Receita (DR-X)

## Descrição
Conduz o mapeamento completo do fluxo de receita em modo Copilot: a IA lidera a coleta estruturada das etapas do fluxo, identifica dependências, analisa gargalos e propõe hipóteses iniciais de restrição sob a lente TOC. O consultor descreve como o processo acontece na prática, responde perguntas sobre o que observou em campo e valida os outputs em cada etapa.

## Quando Usar
- Triggers: "Mapear fluxo de receita", "Mapeamento do fluxo", "Analisar fluxo de caixa", "Identificar gargalos do fluxo", "Fluxo de receita para [cliente]"
- **Pré-requisito:** Arquivos `context/` do cliente com status `[VALIDADO]` devem estar disponíveis
- **NÃO usar** se os arquivos `context/` não existirem — executar `skill-pipeline-extracao` primeiro
- **Posição no DR-X:** executa após extração de contexto e antes (ou em paralelo) com diagnósticos de Trava

---

## Inputs de Partida

Antes de perguntar qualquer coisa ao consultor, **ler os arquivos `context/`** do cliente e extrair:
- Fluxos de receita ativos (`context/business.md` — Revenue Streams)
- Time comercial e responsabilidades declaradas (`context/gtm.md`)
- Ciclo de vendas e entrega já mapeado (`context/gtm.md`)
- Restrições operacionais e gargalos já identificados (`context/constraints.md`)
- UDEs relacionadas a funil, conversão, entrega ou faturamento

Registrar internamente o que já se sabe e **não coletar novamente o que já está nos arquivos `context/`**.

---

## Processo de Execução

### Step 0 — Leitura do Contexto

1. Ler os arquivos `context/business.md`, `context/gtm.md` e `context/constraints.md`
2. Mapear:
   - Quais fluxos de receita estão ativos e qual é o principal (por representatividade) — `context/business.md`
   - Ciclo de vendas e entrega já declarado — `context/gtm.md`
   - Gargalos e UDEs já capturados que se relacionam ao fluxo — `context/constraints.md`
3. Apresentar ao consultor um resumo curto do que já se sabe antes de pedir novos dados:

> *"Com base nos arquivos context/, já sei que: [resumo dos fluxos ativos, ciclo estimado, gargalos já identificados]. Vou mapear o fluxo em detalhe por fluxo de receita. Seguindo para o Step 1."*

---

### Step 1 — Definição do Fluxo por Receita

Para cada fluxo de receita identificado no Step 0, perguntar em **uma única mensagem batch** como o dinheiro percorre o sistema. Priorizar os fluxos de maior representatividade — se houver mais de 3 fluxos, perguntar primeiro sobre os dois principais e tratar os demais como variação.

**Perguntar de uma vez:**

> *Para cada fluxo de receita ativo, preciso entender como o processo acontece na prática — não como deveria ser, mas como realmente é. Pode descrever:*
>
> *[Para cada fluxo identificado no Master Contexto]:*
>
> **[Nome do fluxo]:**
> - *Onde começa o processo? (ex: lead entra, cliente liga, vendedor prospecta)*
> - *Quem qualifica o lead ou oportunidade e com qual critério?*
> - *Como é feita a proposta/orçamento? Quem faz? Em quanto tempo?*
> - *Quem aprova internamente antes de enviar ao cliente?*
> - *Após o fechamento, o que acontece até a entrega? Quais etapas e responsáveis?*
> - *Como é feito o faturamento (emissão de nota)? Há atraso comum nessa etapa?*
> - *Em quanto tempo o dinheiro entra no caixa após a entrega?*

**Após receber os dados:**

Montar o fluxo como uma sequência de etapas para cada receita ativa, no formato:

```
Etapa → Responsável → Tempo médio → Critério de passagem
```

Apresentar o mapa rascunho e perguntar: *"Esse mapa reflete como acontece na prática? Alguma etapa faltou ou está errada?"*

---

### Step 2 — Dependências e Pontos de Espera

Com o fluxo rascunhado validado, perguntar em **uma única mensagem batch** sobre as dependências que podem travar o fluxo:

> *Agora preciso entender o que cria espera ou bloqueio entre as etapas. Para o fluxo de [principal receita]:*
>
> - *Existe alguma etapa que depende exclusivamente de uma pessoa — se ela não age, o fluxo para?*
> - *Há alguma aprovação interna que costuma atrasar o processo? De quem depende?*
> - *Existe etapa onde leads ou pedidos ficam "esperando" antes de avançar? Qual e por quanto tempo?*
> - *Há retrabalho recorrente em alguma parte do processo? (ex: proposta que volta, entrega que precisa ser refeita)*
> - *CRM/sistema atual ([sistema identificado nos arquivos context/]) cobre todas as etapas ou há partes fora do sistema?*
> - *O time comercial e o time de entrega têm capacidade equilibrada — ou um acelera mais que o outro aguenta?*

Aguardar as respostas antes de prosseguir para análise.

---

### Step 3 — Análise de Gargalos e Perdas

Com base nos Steps 1 e 2, a IA identifica e propõe os gargalos. **A IA propõe — o consultor valida.** Nunca pedir ao consultor que liste os gargalos por conta própria.

Para cada etapa do fluxo, avaliar e apresentar:

| Etapa | Tempo médio | Taxa de conversão (se declarada) | Capacidade máxima | Risco de acúmulo | Hipótese de gargalo |
|---|---|---|---|---|---|
| [etapa] | | | | Alto / Médio / Baixo | [sim/não — justificativa] |

**Critério de identificação de gargalo:** etapa onde pedidos/leads se acumulam aguardando processamento, onde a capacidade é menor que a demanda, ou onde o responsável é único e insubstituível.

Apresentar tabela e perguntar: *"Essa análise reflete o que você observa? Alguma etapa foi subestimada ou superestimada como gargalo?"*

---

### Step 4 — Visão Sistêmica (TOC) e Hipóteses de Restrição

Com o mapa e análise de gargalos validados, a IA responde as quatro perguntas estruturantes e propõe hipóteses de restrição:

**Perguntas estruturantes respondidas pela IA:**

1. *Onde o sistema perde dinheiro?* — etapas com maior saída de oportunidades (churn de funil)
2. *Onde o dinheiro fica travado?* — etapas com maior tempo médio entre início e conclusão
3. *Qual etapa limita o resultado global?* — candidato a restrição principal
4. *O fluxo cresce linear ou aos trancos?* — avaliação de previsibilidade

**Declarar explicitamente** a hipótese de restrição principal:

> *"Com base no mapeamento, a hipótese de restrição principal é: [etapa / pessoa / capacidade]. O fluxo desacelera nesse ponto porque [raciocínio]. Isso limita o throughput porque [impacto sistêmico]. Validação final na CRT."*

Apresentar para confirmação do consultor antes de gerar o output final.

---

## Regras Operacionais

- **Nunca perguntar uma etapa de cada vez** — todas as perguntas de uma mesma camada vão em uma única mensagem
- **Nunca pedir ao consultor que identifique os gargalos** — a IA propõe com justificativa, o consultor confirma ou ajusta
- **Nunca avançar de step sem apresentar resultado e receber confirmação** do consultor
- **Sempre ler os arquivos `context/` antes de perguntar qualquer coisa** — não coletar o que já está disponível
- **Mapear o fluxo como realmente acontece** — não como deveria ser; se o consultor descrever o processo ideal, pedir que descreva o que ocorre na prática
- **Múltiplos fluxos:** se o cliente tiver mais de 3 fluxos ativos, tratar os dois principais em detalhe e registrar os demais como variações no output
- **Não fazer afirmações implícitas sobre gargalos** — mostrar o raciocínio antes de declarar a hipótese

---

## Fallbacks

| Situação | O que fazer |
|---|---|
| Consultor não sabe o tempo médio de uma etapa | Registrar como "não mapeado" — não estimar sem base. Registrar como fragilidade estrutural. |
| Taxa de conversão não disponível | Registrar ausência. Usar percepção declarada como proxy ("a maioria fecha", "poucos viram proposta"). Anotar como estimativa. |
| CRM não cobre todo o fluxo | Registrar etapas fora do sistema como ponto de risco. Não usar ausência de dados no sistema como indicador de baixo volume. |
| Fluxo muito informal / sem etapas definidas | Registrar como sintoma de fragilidade. Construir o mapa a partir do que o consultor descreve — mesmo que seja apenas "liga, faz proposta, fecha". |
| Múltiplos responsáveis por mesma etapa sem clareza | Registrar como dependência de pessoa não formalizada — candidato a ponto de espera. |
| Cliente tem fluxo diferente por canal (online vs. presencial vs. indicação) | Perguntar sobre o canal principal e registrar os demais como variações. Não mapear todos com o mesmo nível de detalhe. |

---

## Formato de Saída Obrigatório

```markdown
# Mapeamento do Fluxo de Receita: [Nome do Cliente]

> **Status:** `[AGUARDANDO VALIDAÇÃO DO CONSULTOR]`
> **Data:** [data de execução]
> **Fontes:** context/business.md + context/gtm.md + context/constraints.md + descrição do consultor em [data]
> **Limitações registradas:** [listar etapas sem dados, estimativas usadas]

---

## Fluxos de Receita Mapeados

[Listar fluxos cobertos e fluxos tratados como variação]

---

## Mapa do Fluxo — [Nome do Fluxo Principal]

| Etapa | Responsável | Tempo Médio | Critério de Passagem |
|---|---|---|---|
| Geração de demanda | | | |
| Qualificação | | | |
| Proposta / Orçamento | | | |
| Fechamento | | | |
| Entrega | | | |
| Faturamento | | | |
| Recebimento | | | |

*[Repetir tabela para cada fluxo mapeado em detalhe]*

---

## Dependências Identificadas

| Tipo | Descrição | Impacto no Fluxo |
|---|---|---|
| Entre pessoas | | |
| Entre áreas | | |
| Entre sistemas | | |

**Pontos de espera críticos:**
- [Etapa] — [motivo do bloqueio] — [tempo típico de espera]

---

## Análise de Gargalos

| Etapa | Risco de Acúmulo | Capacidade | Principal Fragilidade |
|---|---|---|---|
| [etapa] | Alto / Médio / Baixo | [dado ou "não mapeado"] | [descrição] |

---

## Visão Sistêmica (TOC)

- **Onde o sistema perde dinheiro:** [etapa + raciocínio]
- **Onde o dinheiro fica travado:** [etapa + tempo estimado]
- **Etapa que limita o resultado global:** [candidato a restrição]
- **Fluxo cresce:** [linear / aos trancos — justificativa]

---

## Hipótese de Restrição Principal

*"O fluxo é limitado por [etapa / pessoa / capacidade], porque [raciocínio], impactando o throughput ao [consequência sistêmica]."*

**Validação final:** CRT.

---

## Pontos de Atenção para a CRT

- [ ] [Item que requer aprofundamento na análise de restrições]
- [ ] [Item que pode ser descartado se confirmado]
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/fluxo-receita.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
