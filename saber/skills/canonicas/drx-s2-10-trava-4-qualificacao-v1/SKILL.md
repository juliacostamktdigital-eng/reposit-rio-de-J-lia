---
slug: drx-s2-10-trava-4-qualificacao-v1
name: drx-s2-10-trava-4-qualificacao-v1
description: "Conduz o diagnóstico completo da Trava 4 em modo Copilot: a IA lidera a coleta, compara o ICP declarado com o perfil real dos leads e clientes, constrói a Matriz ICP vs Realidade, propõe scores por dimensão com justificativa e redige a c..."
---

# Skill: Diagnóstico de Trava 4 — Qualificação (DR-X)

## Descrição
Conduz o diagnóstico completo da Trava 4 em modo Copilot: a IA lidera a coleta, compara o ICP declarado com o perfil real dos leads e clientes, constrói a Matriz ICP vs Realidade, propõe scores por dimensão com justificativa e redige a consolidação causal. O consultor fornece os dados de perfil, relata observações do processo de qualificação e valida os outputs em cada etapa.

## Quando Usar
- Triggers: "Rodar diagnóstico Trava 4", "Diagnosticar qualificação", "Analisar Trava 4", "Diagnóstico de qualificação para [cliente]"
- **Pré-requisito:** Arquivos `context/` do cliente com status `[VALIDADO]` devem estar disponíveis
- **NÃO usar** se os arquivos `context/` não existirem — executar `skill-pipeline-extracao` primeiro

---

## Inputs de Partida

Antes de perguntar qualquer coisa ao consultor, **ler os arquivos `context/`** do cliente e extrair:
- ICP declarado pelo cliente — `context/gtm.md`
- Fluxos de receita e perfil dos clientes reais — `context/business.md`
- UDEs relacionadas a qualidade de leads, conversão baixa, reclamações do time comercial — `context/constraints.md`
- Canais de aquisição e origem dos leads — `context/gtm.md`

Registrar internamente o que já se sabe e **não coletar novamente o que já está nos arquivos `context/`**.

---

## Processo de Execução

### Step 0 — Leitura do Contexto

1. Ler os arquivos `context/business.md`, `context/gtm.md` e `context/constraints.md`
2. Mapear:
   - ICP já declarado (`context/gtm.md`)
   - Perfil dos clientes reais já identificado (`context/business.md`)
   - UDEs que apontam desalinhamento entre público atraído e cliente ideal (`context/constraints.md`)
3. Apresentar resumo ao consultor:

> *"Com base nos arquivos context/, já sei que: [resumo do ICP declarado, perfil dos clientes reais, UDEs relevantes sobre qualidade de leads]. Vou verificar o alinhamento entre ICP e realidade. Seguindo para o Step 1."*

---

### Step 1 — Camada Analítica (Coerência ICP vs Realidade)

Solicitar **em uma única mensagem batch** os dados necessários. Adaptar ao que já está disponível no Master Contexto — especialmente o ICP, que provavelmente já foi capturado.

**Perguntar de uma vez:**
> *Preciso verificar o alinhamento entre o cliente ideal declarado e o que o sistema realmente atrai e fecha. Forneça o que tiver:*
>
> *1. Existe ICP documentado formalmente? Se sim, quais são os critérios principais (segmento, porte, dor, orçamento, cargo do decisor)?*
> *2. Perfil predominante dos leads gerados nos últimos 6–12 meses — existem divergências óbvias em relação ao ICP?*
> *3. Perfil dos clientes que efetivamente fecharam: segmento, porte, ticket médio real*
> *4. % aproximado de leads que são desqualificados ou descartados antes de proposta*
> *5. Existem critérios formais de desqualificação — o time sabe quando recusar um lead?*
> *6. O time comercial reclama da qualidade dos leads? Qual a principal queixa?*

**Após receber os dados:**

Construir e apresentar a Matriz ICP vs Realidade:

```
| Critério | ICP Declarado | Leads Gerados | Clientes Fechados | Alinhamento |
| Segmento | | | | Alto/Médio/Baixo |
| Porte | | | | |
| Dor Principal | | | | |
| Ticket | | | | |
| Cargo Decisor | | | | |
```

**Interpretação:**
- ICP inexistente → fragilidade estrutural imediata; Dimensão A = 0
- Grande divergência entre leads gerados e ICP → Trava 4 provável
- Clientes fechados com ticket abaixo do ICP → sistema atrai quem não pode pagar
- Alta desqualificação necessária → custo operacional desnecessário

Apresentar a análise e perguntar: *"Essa comparação faz sentido? Alguma correção antes de avançar?"*

---

### Step 2 — Camada Experiencial (Observações de Campo)

Com base nos modelos de venda ativos identificados no Step 0, perguntar **em uma única mensagem batch** sobre o que o consultor observou. Incluir apenas os modelos relevantes para aquele cliente.

**Se Inside Sales ativo:**
> *Sobre o processo de qualificação em Inside Sales:*
> - *O consultor simulou ser um lead claramente fora do ICP (cliente oculto)? O que aconteceu — foi desqualificado ou o processo seguiu normalmente?*
> - *O vendedor faz perguntas estruturadas de qualificação antes de enviar proposta (dor, orçamento, prazo, decisor)?*
> - *Existe autonomia do vendedor para recusar educadamente um lead que claramente não tem perfil?*
> - *Existe roteiro ou script de qualificação, ou cada vendedor qualifica do seu jeito?*

**Se Vendas Online ativo:**
> *Sobre a qualificação na jornada digital:*
> - *Os anúncios e a landing page usam linguagem, imagens e promessas que atraem o ICP — ou são genéricos e atraem qualquer público?*
> - *O formulário de entrada tem campos que qualificam o lead antes do contato (ex: faturamento, número de funcionários, cargo)?*
> - *O público das campanhas está segmentado pelo perfil do ICP ou é amplo e indiscriminado?*

**Se PDV ativo:**
> *Sobre qualificação no ponto de venda:*
> - *O perfil predominante de quem entra na loja condiz com o cliente ideal?*
> - *A comunicação visual da fachada e dos materiais internos atrai o segmento certo?*

Aguardar as respostas antes de prosseguir para o scoring.

---

### Step 3 — Scoring por Dimensão (A a E)

Com base nos dados do Step 1 e nas observações do Step 2, propor score para cada dimensão usando o gabarito abaixo. **A IA propõe — o consultor valida.** Nunca pedir ao consultor que atribua as notas.

**Gabarito de referência** (`context/context-trava-4-qualificacao.md`):

| Nota | A) ICP Documentado | B) ICP vs Leads | C) ICP vs Clientes | D) Processo Qualificação | E) Desqualificação |
|---|---|---|---|---|---|
| 0 | Inexistente | Totalmente desalinhado | Não são ICP | Inexistente | Nunca desqualifica |
| 1 | Vago | Majoritariamente desalinhado | Grande divergência | Improvisado | Raramente |
| 2 | Parcial | Parcialmente desalinhado | Divergência relevante | Básico | Depende do vendedor |
| 3 | Claro; pouco usado | Alinhamento aceitável | Alinhamento parcial | Estruturado | Ocorre quando evidente |
| 4 | Claro e utilizado | Bom alinhamento | Bom alinhamento | Estruturado com roteiro | Critério claro |
| 5 | Governante e revisado | Alto alinhamento consistente | Total coerência estratégica | Estruturado e mensurado | Critério claro e estratégico |

**Regra:** nota > 3 exige evidência formal citada na justificativa.

Apresentar tabela completa com proposta de score, justificativa e evidência que sustenta cada nota. Perguntar: *"Concorda com os scores propostos? Algum ajuste antes de calcular o total?"*

---

### Step 4 — Consolidação Causal

Com o scoring validado, redigir a hipótese causal no formato obrigatório:

> *"A empresa opera sob a política implícita de ___, o que gera atração e priorização de perfis desalinhados, reduzindo a eficiência do Throughput."*

**Orientação:** identificar a política organizacional que explica o desalinhamento. Exemplos: "priorizar volume de leads em vez de qualidade", "evitar desqualificar para não perder oportunidade", "não definir formalmente quem não é cliente ideal".

Apresentar a hipótese para o consultor e aguardar validação ou ajuste.

---

### Step 5 — Determinação Preliminar

Aplicar os três critérios de governância:

1. Score total ≤ 15?
2. Grande parte do esforço comercial é gasto com leads desalinhados (conversão limitada por fit, não por proposta)?
3. Ajustar ICP aumentaria o Throughput mais do que otimizar decisão ou compromisso?

Declarar explicitamente: **"Trava 4 é / não é potencial governante"**, com o raciocínio que sustenta a decisão.

Registrar que a validação final é feita na CRT.

---

## Regras Operacionais

- **Nunca perguntar um dado de cada vez** — todas as perguntas de uma mesma camada vão em uma única mensagem
- **Nunca delegar o scoring ao consultor** — a IA propõe com justificativa, o consultor confirma ou ajusta
- **Nunca avançar de step sem apresentar resultado e receber confirmação** do consultor
- **Sempre ler os arquivos `context/` antes de perguntar qualquer coisa** — o ICP declarado provavelmente já está no contexto
- **ICP inexistente não bloqueia o diagnóstico** — registrar como fragilidade estrutural (Dim A = 0) e continuar com o que for observável
- **Mystery shopping não é pré-requisito** — se não foi realizado, pontuar Dim E conservadoramente e registrar como dado não confirmado

---

## Fallbacks

| Situação | O que fazer |
|---|---|
| ICP inexistente | Registrar como fragilidade estrutural imediata. Dim A = 0. Calcular demais dimensões com base na percepção do consultor sobre perfil de leads e clientes. |
| Sem dados de perfil de leads no CRM | Usar percepção declarada ("a maioria dos leads não tem orçamento") como proxy. Anotar como estimativa. |
| Mystery shopping não realizado | Pontuar Dim D e E conservadoramente. Registrar como "não confirmado por observação direta". |
| Time comercial sem critério de desqualificação | Registrar como evidência direta de Trava 4. Pontuar Dim E = 0 ou 1. |
| Modelo de venda não aplicável | Pular seção experiencial correspondente. Registrar motivo. |
| Consultor não souber descrever o processo de qualificação | Pontuar Dim D como 0–1 e registrar como dado não confirmado. |

---

## Formato de Saída Obrigatório

```markdown
# Diagnóstico Trava 4 — Qualificação: [Nome do Cliente]

> **Status:** `[AGUARDANDO VALIDAÇÃO DO CONSULTOR]`
> **Data:** [data de execução]
> **Fontes:** context/business.md + context/gtm.md + context/constraints.md + dados fornecidos pelo consultor em [data]
> **Limitações registradas:** [listar dados ausentes ou estimados]

---

## Pergunta Estruturante

*"O sistema atrai quem pode e quer comprar, ou quem apenas interage?"*

**Resposta com base no diagnóstico:** [resposta em 2–3 linhas]

---

## Matriz ICP vs Realidade

| Critério | ICP Declarado | Leads Gerados | Clientes Fechados | Alinhamento |
|---|---|---|---|---|
| Segmento | | | | Alto / Médio / Baixo |
| Porte | | | | |
| Dor Principal | | | | |
| Ticket | | | | |
| Cargo Decisor | | | | |

**ICP documentado formalmente:** [Sim / Não / Parcial]
**Principal divergência identificada:** [descrição]
**Taxa de desqualificação praticada:** [X]% ou "não mapeada"

---

## Score da Trava 4

| Dimensão | Score (0–5) | Justificativa | Evidência |
|---|---|---|---|
| A) ICP Documentado e Claro | | | |
| B) Alinhamento ICP vs Leads | | | |
| C) Alinhamento ICP vs Clientes Fechados | | | |
| D) Processo de Qualificação | | | |
| E) Capacidade de Desqualificar | | | |
| **Total (0–25)** | | | |

**Faixa:** [0–10 / 11–15 / 16–20 / 21–25] — [interpretação]

---

## Consolidação Causal

*"A empresa opera sob a política implícita de ___, o que gera atração e priorização de perfis desalinhados, reduzindo a eficiência do Throughput."*

---

## Determinação Preliminar

- Score ≤ 15? [Sim / Não]
- Esforço comercial concentrado em leads desalinhados? [Sim / Não — justificativa]
- Ajustar ICP aumenta Throughput mais que otimizar decisão/compromisso? [Sim / Não — justificativa]

**Trava 4 é / não é potencial governante.** Validação final na CRT.
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/trava-4-qualificacao.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
