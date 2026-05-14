---
slug: coringa-sx-01-pipeline-extracao-v1
name: coringa-sx-01-pipeline-extracao-v1
description: "Executa o fluxo completo de extração de dados qualitativos de uma ou mais fontes (transcrição de Kickoff, Formulário Diagnóstico, Reunião de Vendas) e os transforma nos **arquivos de contexto do cliente** (`context/business.md`, `context..."
---

# Skill: Pipeline Base de Extração de Contexto (DR-X)

## Descrição
Executa o fluxo completo de extração de dados qualitativos de uma ou mais fontes (transcrição de Kickoff, Formulário Diagnóstico, Reunião de Vendas) e os transforma nos **arquivos de contexto do cliente** (`context/business.md`, `context/gtm.md`, `context/constraints.md`, `context/stakeholders.md`). Consolida informações ruidosas e complexas (múltiplas linhas de receita, restrições, UDEs e inteligência de relacionamento) em dados estruturados prontos para análise DR-X.

## Quando Usar
- Triggers: "Rodar pipeline de extração", "Extrair contexto base novo cliente", "Aplicar skill de extração", "Gerar contexto", "Analisar transcrição do kickoff", "Processar reunião de vendas"
- **Sempre** como ponto de partida (Fase 0) antes de qualquer outra skill (TAM SAM SOM, Fluxo de Receita)
- NÃO usar quando os arquivos de `context/` já existem e estão com status `[VALIDADO]` — nesse caso, usar como revisão crítica

## Inputs Necessários
- Um ou mais arquivos (TXT, MD, PDF, DOCX) ou conteúdo colado diretamente no chat
- **Não solicitar nenhum dado adicional antes de ler** — Claude lê primeiro e confirma ambiguidades depois

---

## Processo de Execução

### Step 0: Leitura e Triagem das Fontes
1. Leia todos os arquivos ou conteúdo fornecido.
2. Para cada input, registre em raciocínio interno: **quem enviou** (cliente, consultor ou terceiro) e **como chegou** (proativamente pelo cliente, solicitado pela equipe, encaminhado com alguma mensagem). A *forma* de chegada do material é inteligência de relacionamento tão importante quanto o conteúdo. Ex: um briefing enviado pelo próprio cliente antes da reunião, com mensagem exigindo que a equipe estude a empresa com antecedência, revela muito sobre o perfil de engajamento.
3. Se houver **mais de uma fonte**, identifique conflitos entre elas em dados críticos (ex: ticket médio diferente no formulário vs. na transcrição).
4. Se encontrar conflito em dado crítico: **pare e apresente o conflito ao consultor** antes de prosseguir. Pergunte qual fonte deve ser tratada como verdade absoluta para aquele dado.
5. Identifique quem é o **consultor** e quem é o **cliente** pelo contexto do documento. Se ambíguo, confirme antes de prosseguir.

### Step 1: O "Rastreador" (Leitura Bruta)
1. Varra o documento ignorando ruído (conversas paralelas, piadas, explicações teóricas).
2. Registre os dados factuais em buckets explícitos — estes ficam no seu raciocínio, **não são exibidos** ao consultor, a menos que haja gaps críticos (ver ponto 3).
   - **Produto/ICP:** O que vendem e para quem.
   - **Receita:** Tickets médios, formas de monetização, múltiplos fluxos de venda (B2B, licitações, B2C).
   - **Travas (UDEs):** Dores, reclamações, atrasos no funil, sintomas de churn ou falha de retenção.
   - **Objetivos:** Prazos e metas declarados.
   - **Stakeholders / Relacionamento:** Quem são os decisores, influenciadores e operacionais. Como cada input chegou (enviado pelo cliente, pelo consultor, por terceiro). Sinais comportamentais de confiança, ruptura ou expectativa — o que a *forma* de chegada do material revela sobre a pessoa. Histórico com agências ou fornecedores anteriores.
3. **Se houver gaps críticos** — qualquer um dos itens abaixo ausente ou muito incerto — exiba os buckets parciais e liste os gaps antes de avançar para o Step 2:
   - Ticket médio (ao menos estimado)
   - ICP definido (segmento, porte, geografia)
   - Horizonte estratégico
   - Pelo menos uma UDE ou restrição identificada
   - Modelo de monetização

### Step 2: O "Sintetizador" (Lógica de Negócios)
1. Com os buckets mapeados, cruze as categorias e estruture os dados com foco no método DR-X (TOC, Throughput, Restrições).
2. Se houver mais de uma fonte de receita, **liste todas** — nunca apenas a principal.
3. Verifique a presença dos cinco itens abaixo. Qualquer ausência ou incerteza vira uma **pergunta direta ao consultor** no Step 2.5:
   - Ticket médio (ao menos estimado)
   - ICP definido (segmento, porte, geografia)
   - Horizonte estratégico
   - Pelo menos uma UDE / restrição identificada
   - Modelo de monetização

### Step 2.5: Resolução de Gaps (Diálogo com o Consultor)
1. Se houver qualquer gap ou incerteza identificado no Step 2, **faça todas as perguntas de uma vez** — uma lista numerada, clara e direta.
2. Aguarde as respostas antes de gerar o documento.
3. Incorpore as respostas ao Master Contexto.
4. Se o consultor não souber responder alguma pergunta, registre como `[Não confirmado]` no campo correspondente e liste na seção Pontos de Dúvida do output.
5. Se não houver nenhum gap, pule este step e vá direto ao Step 3.

### Step 3: Geração e Salvamento dos Arquivos de Contexto

1. Gere os quatro arquivos de contexto seguindo os formatos de saída abaixo, com as respostas do consultor incorporadas.
2. Salve em: `[pasta-do-projeto-aberto]/clientes/[nome-do-cliente]/`
   - `context/business.md` — modelo de negócio, revenue streams, capacidade operacional
   - `context/gtm.md` — canais, funil, ICP, ciclo de vendas, retenção, mercado, concorrência
   - `context/constraints.md` — restrições operacionais, UDEs, diagnóstico de trava dominante
   - `context/stakeholders.md` — mapa de stakeholders, perfis de engajamento, inteligência de relacionamento
   - Se o diretório não existir, crie-o (incluindo `context/`, `inputs/`, `ativos-cliente/`, `produtos/`).
3. Salve também a síntese consolidada em `inputs/sinteses/master-contexto.md` (se múltiplas fontes foram processadas) com status `[AGUARDANDO VALIDAÇÃO FINAL DO CONSULTOR]`.
4. Se não tiver permissão de escrita, exiba o conteúdo no chat para o consultor salvar manualmente.

### Step 4: Atualização dos Arquivos de Governança

Toda rodada da `sx-01` toca obrigatoriamente os arquivos abaixo (criando se não existem, atualizando se existem):

1. **`cliente.md`** — preencher/complementar com dados extraídos (CNPJ, setor, stakeholders cliente + V4, site).
2. **`STATUS.md` (raiz do cliente)** — atualizar:
   - Fase ativa (S1 / S2 / etc.)
   - Status (resumo de uma linha sobre o estado atual)
   - Risco principal
   - Próximo movimento
   - Tabela de Context Files com status atual de cada um
3. **`MAPA.md`** — atualizar três blocos:
   - **Estado atual** — fase em execução, maior risco, próximo passo
   - **Últimos inputs relevantes** — adicionar linha com a data da rodada e o que foi processado
   - **Decisões recentes** — adicionar uma linha resumida para cada conflito resolvido nesta rodada (apontando para `DECISIONS.md`)
4. **`DECISIONS.md`** — registrar:
   - Cada **conflito entre fontes** resolvido nesta rodada como uma decisão Dx (com decisão, motivo, impacto, fontes)
   - Cada **questão remanescente** como item em "Questões Abertas"
5. **`produtos/<Produto Ativo>/produto.md`** — preencher/atualizar o campo `Objetivo` a partir do master-contexto. Atualizar campo `Fase ativa` se mudou.
6. **`produtos/<Produto Ativo>/STATUS.md`** — atualizar:
   - `Fase atual` e `Próxima fase`
   - `Última ação` (registrar a rodada da sx-01 com data)
   - Síntese da fase concluída (se aplicável)
   - Tabela de Entregáveis em curso
   - Bloqueios e pendências

Esses arquivos garantem que o rastro da rodada fique visível em todos os níveis de governança.

---

## 🛑 Regra de Ouro (Trava de Validação)

**NÃO inicie automaticamente outras skills** (Sizing, Diagnóstico de Trava, etc.) após concluir este passo. Sua execução termina ao entregar os arquivos de contexto.

**NÃO faça perguntas parciais ou progressivas.** Todas as dúvidas devem ser consolidadas e feitas de uma vez no Step 2.5 — nunca uma pergunta de cada vez ao longo do processo.

**Após o Step 2.5**, não interrompa mais. Incorpore as respostas e gere o documento final.

---

## Formatos de Saída Obrigatórios

### context/business.md

```markdown
# Context: Business — [Nome do Cliente]

> **Status de Validação:** `[AGUARDANDO VALIDAÇÃO FINAL DO CONSULTOR]`
> **Fontes consultadas:** [Lista dos arquivos utilizados]
> **Participantes identificados:** [Lista com papéis: Consultor / Cliente]
>
> *Nota:* NENHUM Sizing ou Diagnóstico deve ser feito automaticamente sem que o Consultor altere este status para `[VALIDADO]`.

---

### Pontos de Dúvida Remanescentes
*[Liste apenas o que o consultor não soube responder. Se nenhum: "Todos os gaps foram resolvidos pelo consultor".]*
- [ ] [Campo: dado que ficou como `[Não confirmado]`...]

---

### 1. Visão Geral do Negócio
- **Problema de Negócio Resolvido:** [Contexto claro do que o cliente resolve para seus clientes]
- **ICP Ideal (Perfil do Cliente):** [Características demográficas e firmográficas]
- **Meta Principal do Sistema (TOC):** [Onde querem chegar — objetivo declarado]
- **Horizonte Estratégico Declarado:** [Prazo. Se não informado: "Não declarado — ver Pontos de Dúvida"]

### 2. Visão de Revenue Streams (Arquitetura de Receita)
| Fluxo de Receita | Modelo de Monetização | Ticket Médio Estimado | Representatividade |
| :--- | :--- | :--- | :--- |
| [Ex: B2B Corporativo] | [Ex: SaaS recorrente] | [Ex: R$ 2.500/ano] | [Ex: Core / Secundário] |

### 3. Capacidade Operacional
- **Capacidade de entrega atual:** [...]
- **Gargalos operacionais identificados:** [...]
- **Equipe / estrutura comercial:** [...]
```

---

### context/gtm.md

```markdown
# Context: GTM — [Nome do Cliente]

> **Status de Validação:** `[AGUARDANDO VALIDAÇÃO FINAL DO CONSULTOR]`

---

### 3. Dinâmica de Go-to-Market

- **Canais de Aquisição:** [...]
- **Ciclo Médio de Vendas:** [...]
- **Funil CRM (se disponível):** [...]

### 4. Retenção e Continuidade
- **Modelo de Pós-Venda existente:** [Inexistente / Reativo / Estruturado]
- **Sinais de Churn ou LTV baixo:** [...]

### 5. Mercado e Concorrência
- **Estimativa de TAM/SAM/SOM (se disponível):** [...]
- **Principais concorrentes identificados:** [...]
```

---

### context/constraints.md

```markdown
# Context: Constraints — [Nome do Cliente]

> **Status de Validação:** `[AGUARDANDO VALIDAÇÃO FINAL DO CONSULTOR]`

---

### Restrições Operacionais
- [Restrição 1 — extraída literalmente da fonte]
- [Restrição 2...]

### UDEs (Efeitos Indesejados / Sintomas de Trava)
- [UDE 1 — extraído literalmente]
- [UDE 2...]

### Diagnóstico Preliminar de Trava Dominante
- [Se identificável na extração: hipótese de trava dominante com justificativa]
```

---

> **Próximo passo:** Consultor, revise os campos marcados como `[Não confirmado]`. Quando corretos, altere o status para **`[VALIDADO]`** em cada arquivo — só então as demais skills podem ser executadas.
