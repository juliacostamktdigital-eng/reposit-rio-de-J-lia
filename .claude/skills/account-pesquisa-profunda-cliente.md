---
name: account-pesquisa-profunda-cliente
description: Monta Knowledge Base acionável via Deep Research estruturado no Gemini — gera prompts prontos para pesquisa de posicionamento, mercado, produto, concorrentes e consumidor.
user-invocable: true
---

# /account-pesquisa-profunda-cliente — Deep Research do cliente

Monta KB acionável através de Deep Research estruturado, gerando insumos para copy, criativos, campanhas e landing pages.

## Gate obrigatório (BLOQUEANTE)

Só roda se a pasta do cliente já contiver:
- Formulário de kickoff preenchido
- Transcrição de reunião de vendas

Sem esses dois documentos, a skill para e pede os dados.

## Fluxo

**Passo 1:** Identificar cliente; validar caminho em `clientes/<cliente>/docs/pesquisa-profunda/`

**Passo 2:** Varredura de dados internos — kickoff, calls, CRM, links, propostas

**Passo 3:** Consolidar resumo `[DADOS INTERNOS CONSOLIDADOS]` em `00-briefing-pesquisa.md`

**Passo 4:** Entregar **5 prompts prontos** em blocos copiáveis:
- **DR-1:** Cliente, posicionamento digital e região
- **DR-2:** Produto, serviço e setor
- **DR-3:** Consumidor e demanda
- **DR-4:** Concorrência
- **Perplexity:** Busca social (opcional)

## Regra crítica de filesystem

Sempre usar **caminhos absolutos**. Nunca caminhos relativos nem `cd` em comandos Bash.

## Saídas estruturadas

- Prompts em `prompts/dr-1-*.md` até `dr-4-*.md`
- Outputs brutos em `bruto/gemini/dr-0N-output.md`
- Sínteses em `01-cliente-posicionamento-digital.md`, `02-mercado-setor-*.md`, `03-produto-*.md`, `04-concorrentes.md`, `06-consumidor.md`
- Fontes em `07-fontes-e-evidencias.md`

## Princípios

- Separar rigorosamente FATO / INFERÊNCIA / LACUNA
- Não inventar dados
- Priorizar material interno
- Prompts copiáveis diretamente no chat (zero atrito)
