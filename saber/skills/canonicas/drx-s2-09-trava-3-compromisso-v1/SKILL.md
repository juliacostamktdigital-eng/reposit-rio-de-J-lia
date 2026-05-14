---
slug: drx-s2-09-trava-3-compromisso-v1
name: drx-s2-09-trava-3-compromisso-v1
description: "Conduz o diagnóstico completo da Trava 3 em modo Copilot: a IA lidera a coleta, processa os dados fornecidos pelo consultor, constrói a linha do tempo de compromisso, identifica onde o funil vaza antes da decisão, propõe scores por dimen..."
---

# Skill: Diagnóstico de Trava 3 — Compromisso (DR-X)

## Descrição
Conduz o diagnóstico completo da Trava 3 em modo Copilot: a IA lidera a coleta, processa os dados fornecidos pelo consultor, constrói a linha do tempo de compromisso, identifica onde o funil vaza antes da decisão, propõe scores por dimensão com justificativa e redige a consolidação causal. O consultor fornece dados de agendamento e no-show, relata observações de campo e valida os outputs em cada etapa.

## Quando Usar
- Triggers: "Rodar diagnóstico Trava 3", "Diagnosticar compromisso", "Analisar Trava 3", "Diagnóstico de compromisso para [cliente]"
- **Pré-requisito:** Arquivos `context/` do cliente com status `[VALIDADO]` devem estar disponíveis
- **NÃO usar** se os arquivos `context/` não existirem — executar `skill-pipeline-extracao` primeiro

---

## Inputs de Partida

Antes de perguntar qualquer coisa ao consultor, **ler os arquivos `context/`** do cliente e extrair:
- Modelos de venda ativos — `context/gtm.md`
- Ciclo médio de vendas e entrega já declarado — `context/gtm.md`
- UDEs relacionadas a no-show, "lead que sumiu", dificuldade de agendamento, follow-up excessivo — `context/constraints.md`
- Gargalos operacionais relacionados a triagem e primeiro contato — `context/constraints.md`

Registrar internamente o que já se sabe e **não coletar novamente o que já está nos arquivos `context/`**.

---

## Processo de Execução

### Step 0 — Leitura do Contexto

1. Ler os arquivos `context/business.md`, `context/gtm.md` e `context/constraints.md`
2. Mapear:
   - Quais modelos de venda estão ativos (`context/gtm.md`)
   - O que já foi capturado sobre ciclo de atendimento e responsividade (`context/gtm.md`)
   - UDEs que apontam sintomas da Trava 3 — no-show, leads frios, follow improdutivo (`context/constraints.md`)
3. Apresentar resumo ao consultor:

> *"Com base nos arquivos context/, já sei que: [resumo de ciclo de contato, gargalos de triagem, UDEs relevantes]. Vou precisar de dados adicionais para completar o diagnóstico. Seguindo para o Step 1."*

---

### Step 1 — Camada Analítica (Dados de Compromisso)

Solicitar **em uma única mensagem batch** os dados necessários para a análise. Adaptar ao que já está disponível no Master Contexto.

**Perguntar de uma vez:**
> *Preciso dos seguintes dados para construir a linha do tempo de compromisso e identificar onde o funil vaza antes da decisão. Forneça o que tiver disponível:*
>
> *1. Volume de leads contatados e qualificados nos últimos 6–12 meses (ou estimativa)*
> *2. Agendamentos marcados vs. agendamentos realizados — taxa de no-show estimada*
> *3. Tempo médio entre o lead entrar e o primeiro contato do time (em horas ou dias)*
> *4. Número médio de tentativas de follow-up necessárias para conseguir um agendamento*
> *5. Canal com melhor e pior taxa de comparecimento (se houver mais de um canal)*
> *6. O que acontece com leads que somem após qualificação — existe tentativa de recuperação?*

**Após receber os dados:**

Construir e apresentar a Linha do Tempo de Compromisso:

```
| Etapa | Volume | % que Avança | Tempo Médio | Observação |
| Lead entra → 1º contato | | | | |
| 1º contato → Agendamento | | | | |
| Agendamento → Comparecimento | | | | |
```

Calcular:
- **Taxa de no-show** por canal (se disponível)
- **Ponto de maior vazamento** no funil pré-decisão
- **Esforço de follow** (tentativas médias) vs. resultado obtido

**Interpretação:**
- Taxa de no-show > 30% → forte indício de Trava 3
- Muitas tentativas de follow para poucos avanços → compromisso travado
- Queda entre qualificação e agendamento → problema na proposta do próximo passo

Apresentar resultados e perguntar: *"Esses números fazem sentido com o que você observa? Alguma correção antes de avançar?"*

---

### Step 2 — Camada Experiencial (Observações de Campo)

Com base nos modelos de venda ativos identificados no Step 0, perguntar **em uma única mensagem batch** sobre o que o consultor observou. Incluir apenas os modelos relevantes para aquele cliente.

**Se Inside Sales ativo:**
> *Sobre o processo de agendamento e compromisso em Inside Sales:*
> - *O consultor simulou ser um lead (cliente oculto) e entrou em contato? O que observou no primeiro atendimento?*
> - *O consultor pede agendamento com data e hora definidas, ou deixa vago ("qualquer dia da semana")?*
> - *Existe mensagem de confirmação enviada após o agendamento? E lembrete no D-1 ou D-0?*
> - *Quando um lead não aparece, existe rotina de recuperação? Como funciona?*
> - *O primeiro contato cria clareza do próximo passo e do benefício de avançar?*

**Se Vendas Online ativo:**
> *Sobre microcompromissos na jornada digital:*
> - *O formulário de cadastro/lead tem fricção excessiva (muitos campos, informações prematuras)?*
> - *Existe benefício explícito e imediato para o lead agir agora (por que preencher, por que agendar)?*
> - *Há sistema de recuperação para abandono de formulário ou carrinho (e-mail, WhatsApp, retargeting)?*
> - *O CTA da página é claro sobre o que vai acontecer depois do clique?*

**Se PDV ativo:**
> *Sobre compromisso no ponto de venda:*
> - *O vendedor tenta agendar retorno ou oferece reserva ao final de uma visita sem compra?*
> - *Existe follow-up estruturado pós-visita para leads que não compraram na hora?*
> - *O cliente sai da loja sabendo o próximo passo?*

Aguardar as respostas antes de prosseguir para o scoring.

---

### Step 3 — Scoring por Dimensão (A a E)

Com base nos dados do Step 1 e nas observações do Step 2, propor score para cada dimensão usando o gabarito abaixo. **A IA propõe — o consultor valida.** Nunca pedir ao consultor que atribua as notas.

**Gabarito de referência** (`context/context-trava-3-compromisso.md`):

| Nota | A) Tempo 1º Contato | B) Conversão Agendamento | C) Comparecimento | D) Follow-up | E) Arquitetura Compromisso |
|---|---|---|---|---|---|
| 0 | Sem contato / tardio | Ninguém avança | No-show dominante | Inexistente | Inexistente; cliente solto |
| 1 | Muito lento / inconsistente | Muito baixo; exceções | Muito alto no-show | Eventual; sem padrão | Confusa; exige esforço |
| 2 | Lento; melhora em canais | Baixo; esforço alto | Alto; recuperação fraca | Irregular; repetitivo | Parcial; falhas na instrução |
| 3 | Adequado e previsível | Aceitável; padrão básico | Nível aceitável | Cadência básica aplicada | Clara; confirmação mínima |
| 4 | Rápido e consistente | Bom; processo estável | Baixo no-show; recuperação | Cadência com intenção | Estruturada; fricção reduzida |
| 5 | Otimizado com SLA/controle | Excelente; alta conversão | Mínimo; recuperação eficaz | Governado com métricas | Desenhada para compromisso |

**Regra:** nota > 3 exige evidência formal citada na justificativa.

Apresentar tabela completa com proposta de score, justificativa e evidência que sustenta cada nota. Perguntar: *"Concorda com os scores propostos? Algum ajuste antes de calcular o total?"*

---

### Step 4 — Consolidação Causal

Com o scoring validado, redigir a hipótese causal no formato obrigatório:

> *"A empresa opera sob a política implícita de ___, o que gera ___, bloqueando o avanço do cliente para a decisão."*

**Orientação:** identificar a política organizacional que explica por que o compromisso não é obtido. Exemplos: "tratar o follow-up como obrigação e não como condução", "não criar clareza do próximo passo no primeiro contato", "aceitar agendamentos vagos sem confirmação estruturada".

Apresentar a hipótese para o consultor e aguardar validação ou ajuste.

---

### Step 5 — Determinação Preliminar

Aplicar os três critérios de governância:

1. Score total ≤ 15?
2. A maior perda do funil ocorre entre qualificação/interesse e a decisão (pré-proposta)?
3. Resolver compromisso aumentaria o Throughput mais do que ajustar proposta ou aquisição?

Declarar explicitamente: **"Trava 3 é / não é potencial governante"**, com o raciocínio que sustenta a decisão.

Registrar que a validação final é feita na CRT.

---

## Regras Operacionais

- **Nunca perguntar um dado de cada vez** — todas as perguntas de uma mesma camada vão em uma única mensagem
- **Nunca delegar o scoring ao consultor** — a IA propõe com justificativa, o consultor confirma ou ajusta
- **Nunca avançar de step sem apresentar resultado e receber confirmação** do consultor
- **Sempre ler os arquivos `context/` antes de perguntar qualquer coisa** — não coletar o que já está disponível
- **Dados parciais são aceitos** — calcular com o disponível e registrar limitações explicitamente
- **Mystery shopping não é pré-requisito** — se não foi realizado, pontuar conservadoramente e registrar como dado não confirmado

---

## Fallbacks

| Situação | O que fazer |
|---|---|
| Sem dados de agendamento/no-show no CRM | Usar percepção declarada ("a maioria não aparece", "precisamos de 5 tentativas") como proxy. Anotar como estimativa. |
| Mystery shopping não realizado | Perguntar ao consultor o que observa no processo normal. Pontuar Dim E conservadoramente. Registrar como "não confirmado por observação direta". |
| Sem dados de no-show | Registrar como fragilidade estrutural. Limitar Dim C ao máximo 2. |
| Histórico < 6 meses | Calcular com o disponível. Registrar limitação. |
| Modelo de venda não aplicável ao cliente | Pular seção experiencial correspondente. Registrar motivo. |
| Consultor não souber responder sobre agendamento ou follow-up | Pontuar as dimensões correspondentes (A, B, D, E) como 0–1 e registrar como dado não confirmado. |

---

## Formato de Saída Obrigatório

```markdown
# Diagnóstico Trava 3 — Compromisso: [Nome do Cliente]

> **Status:** `[AGUARDANDO VALIDAÇÃO DO CONSULTOR]`
> **Data:** [data de execução]
> **Fontes:** context/business.md + context/gtm.md + context/constraints.md + dados fornecidos pelo consultor em [data]
> **Limitações registradas:** [listar dados ausentes ou estimados]

---

## Pergunta Estruturante

*"O sistema transforma intenção em presença/ação, ou vive de perseguição?"*

**Resposta com base no diagnóstico:** [resposta em 2–3 linhas]

---

## Linha do Tempo de Compromisso

| Etapa | Volume | % que Avança | Tempo Médio | Principal Causa de Perda |
|---|---|---|---|---|
| Lead entra → 1º contato | | | | |
| 1º contato → Agendamento | | | | |
| Agendamento → Comparecimento | | | | |

**Ponto de maior vazamento:** [etapa + justificativa]
**Taxa de no-show estimada:** [X]% — método: [real / estimado]
**Tentativas de follow por agendamento:** [X] tentativas em média

---

## Score da Trava 3

| Dimensão | Score (0–5) | Justificativa | Evidência |
|---|---|---|---|
| A) Tempo até Primeiro Contato | | | |
| B) Conversão para Agendamento/Ação | | | |
| C) Taxa de Comparecimento (no-show) | | | |
| D) Cadência e Qualidade de Follow-up | | | |
| E) Arquitetura do Compromisso | | | |
| **Total (0–25)** | | | |

**Faixa:** [0–10 / 11–15 / 16–20 / 21–25] — [interpretação]

---

## Consolidação Causal

*"A empresa opera sob a política implícita de ___, o que gera ___, bloqueando o avanço do cliente para a decisão."*

---

## Determinação Preliminar

- Score ≤ 15? [Sim / Não]
- Maior perda do funil ocorre antes da decisão (pré-proposta)? [Sim / Não — justificativa]
- Resolver compromisso aumenta Throughput mais que ajustar proposta ou aquisição? [Sim / Não — justificativa]

**Trava 3 é / não é potencial governante.** Validação final na CRT.
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/trava-3-compromisso.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
