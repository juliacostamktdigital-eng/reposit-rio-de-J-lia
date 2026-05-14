# Protocolos de Agentes — Como Ler e Escrever neste Cerebro
**Status:** v1 — Fundamento
**Atualizado:** 2026-04-16
**Fonte:** humano (Luis Santos)

---

## Proposito

Este documento define as regras obrigatorias para qualquer agente semi-autonomo que interaja com este repositorio.
Leia este arquivo antes de qualquer acao de leitura ou escrita.

---

## Principio Fundamental

> **Este repositorio e a memoria persistente da operacao Colli & Co.**
> Agentes leem daqui para ter contexto. Agentes escrevem aqui para persistir conhecimento novo.
> Conhecimento operacional novo deve ir para `projetos/` (cliente) ou `areas/` (funcao), salvo excecao explicita.

**Obrigatorio tambem:** `07-CONTEXT-SECURITY.md` — escopo micro/meso/macro, diretorios de risco e commits.

---

## 1. Regras de Leitura

### 1.1 Ordem de leitura

Ao iniciar uma sessao neste cerebro, leia nesta ordem:

```
1. CLAUDE.md / AGENTS.md              ← contexto rapido (obrigatorio)
2. empresa/contexto/06-AGENT-PROTOCOLS.md   ← este arquivo (obrigatorio)
3. empresa/contexto/07-CONTEXT-SECURITY.md  ← escopo e commits (obrigatorio)
4. empresa/contexto/05-VOCABULARY.md ← termos que voce vai usar (obrigatorio)
5. Documentos relevantes para a tarefa (condicional)
6. projetos/ ou areas/ relevantes (condicional — dados vivos)
```

### 1.1b Caminhos no terminal (evitar `../empresa` errado)

Neste repositorio, **caminhos escritos na documentacao** (incluindo este arquivo, `CLAUDE.md`, skills) sao **sempre relativos à raiz git do cerebro** — a pasta que contem `empresa/`, `projetos/`, `areas/` e `AGENTS.md`.

| Onde o Paperclip (ou o teu shell) abre o `cwd` | Como chegar a `empresa/contexto/06-AGENT-PROTOCOLS.md` |
|------------------------------------------------|--------------------------------------------------------|
| Raiz do repo (`brain_v4_colli/`) | `empresa/contexto/06-AGENT-PROTOCOLS.md` |
| Pasta de **projeto** `projetos/<slug>/` | `../../empresa/contexto/06-AGENT-PROTOCOLS.md` |
| Workspace so do agente (ex.: `.paperclip-data/.../workspaces/<agentId>`) | Nao assumas relativo ao repo: usa **`git rev-parse --show-toplevel`** no repositorio do cerebro (ou a variavel de ambiente **`COLLI_BRAIN_ROOT`** quando definida) e prefixa os paths da doc com esse root. |

**Erro comum:** com `cwd` em `projetos/prado-...`, usar `../empresa/...` — isso aponta para `projetos/empresa/`, que **nao existe**. Sao **dois** niveis ate a raiz: `../../empresa/...`.

**Paths legados:** qualquer referencia a `v4 os/saber/` ou `.paperclip-data/.../v4 os/` esta **obsoleta**; o cerebro canónico e este repo (`brain_v4_colli`). Skills em Paperclip ficam em `areas/iniciativas/agentizacao_saber/workstation/paperclip/skills/` — nao procures skills dentro de `v4 os/saber/`.

### 1.2 Hierarquia de confianca de fontes

| Fonte | Confianca | Observacao |
|-------|-----------|------------|
| ADR em `empresa/contexto/06-AGENT-PROTOCOLS.md` | Maxima | Decisao explicita e registrada |
| Arquivos em `empresa/contexto/01-` a `05-` | Alta | Fundamentos validados por humano |
| Arquivos em `projetos/` e `areas/` | Media | Dado operacional — pode estar desatualizado |
| Fichas em `empresa/produtos/` | Alta | Fonte primaria de produto — mantida por humano |
| Material fora de `brain_v4_colli/` | Variavel | So se o humano apontar o path; declare a fonte |
| Inferencia propria do agente | Baixa | Sempre declare: "inferencia — nao validado" |

### 1.3 Quando declarar lacuna

Se a informacao que voce precisa **nao existe neste repositorio**, declare explicitamente:

```
> **Lacuna:** [descricao do que nao foi encontrado] — informacao nao disponivel neste cerebro.
```

Nunca invente dados. Nunca assuma que algo e verdade so porque parece razoavel.

---

## 2. Regras de Escrita

### 2.1 Taxonomia de projetos — distincao critica

Este cerebro tem **tres tipos distintos de projeto**. Confundir os tipos e um erro frequente:

| Tipo | Pasta | O que e | Exemplos |
|------|-------|---------|---------|
| **Cliente em operacao** | `projetos/<slug>.md` | Empresa externa contratante da Colli & Co que esta sendo atendida ativamente por um squad | acme-industrias, restaurante-xyz |
| **Iniciativa interna** | `areas/iniciativas/<nome>.md` | Programa estrategico interno que envolve multiplas areas funcionais da Colli & Co | V4 AI OS, Agentizacao do Saber, novo produto SWAS |
| **Estado de area** | `areas/<area>/estado-atual.md` | Situacao corrente de uma area funcional especifica | saude do pipeline de vendas, metricas de CS |

**Regra de decisao rapida:**
- "Estamos entregando servico para esse cliente?" → `projetos/`
- "E um projeto interno nosso que envolve mais de uma area?" → `areas/iniciativas/`
- "E o estado ou playbook de uma area especifica?" → `areas/<area>/`

### 2.2 Onde cada tipo de dado vai

| O que voce descobriu | Onde escrever |
|---------------------|---------------|
| Contexto de cliente ativo (externo) | `projetos/<slug-cliente>.md` |
| Projeto interno transversal (cross-area) | `areas/iniciativas/<nome>.md` |
| Estado ou playbook de uma area funcional | `areas/<area>/estado-atual.md` ou `areas/<area>/playbooks/` |
| Nova decisao tecnica importante | Adicionar ADR em `empresa/contexto/06-AGENT-PROTOCOLS.md` |
| Novo produto identificado (ficha) | **Nao** criar sozinho em `empresa/produtos/` — sinalizar lacuna ao humano |
| Correcao de fundamento em `01-` a `05-` | Protocolo de revisao abaixo + `07-CONTEXT-SECURITY.md` |

### 2.2 Formato obrigatorio para `projetos/<slug>.md`

Use o template em `projetos/_TEMPLATE.md`. Campos minimos:

```markdown
# [Nome do contexto]
**Atualizado:** YYYY-MM-DD HH:MM (horario de Brasilia)
**Fonte:** agente:[nome-do-agente] | sistema:[nome-do-sistema]
**Proxima revisao:** YYYY-MM-DD
**Confianca:** [alta | media | baixa]

---

## Resumo
## Detalhes
## Lacunas
```

### 2.3 Protocolo de revisao de fundamentos (`empresa/contexto/01-` a `05-`)

Arquivos nesta faixa sao **Fundamentos** — mudam raramente.
Para atualiza-los:

1. Confirme que a tarefa e **macro** ou explicitamente autorizada (ver `07-CONTEXT-SECURITY.md`)
2. Identifique o que esta desatualizado
3. Escreva nota de revisao no proprio arquivo:
   ```
   > **Nota de revisao [YYYY-MM-DD]:** [o que mudou e por que]
   ```
4. Atualize o conteudo
5. Atualize o campo `**Atualizado:**` no cabecalho

**Nunca delete conteudo de fundamentos silenciosamente.**
Se algo ficou obsoleto, marque como `deprecated` e anote o motivo.

### 2.4 O que NUNCA escrever neste cerebro

- Dados pessoais de colaboradores (salario, avaliacao individual, historico de desligamento)
- Dados confidenciais de clientes (contratos, valores, informacoes sigilosas de negocio)
- Secrets, tokens de API, senhas
- Codigo-fonte executavel (este cerebro e documentacao, nao codigo)

---

## 3. Convencoes de nomenclatura

### `projetos/`

```
projetos/acme-industrias.md
projetos/cliente-xyz-2026.md
```

### `areas/`

```
areas/vendas/estado-atual.md
areas/marketing/playbooks/campanha-meta.md
```

- Use kebab-case nos slugs de arquivo quando possivel
- Nao use acentos ou caracteres especiais no nome do arquivo

---

## 4. Identificacao do Agente

Todo agente que escreve neste cerebro deve se identificar no campo `**Fonte:**`.

Exemplos validos:
- `agente:sdr-ia`
- `agente:roi-plan`
- `agente:claude-code`
- `agente:copilot-flows`
- `sistema:ekyte`
- `sistema:bigquery-job`
- `humano:luis-santos`

---

## 5. ADRs — Architecture Decision Records

Registre aqui decisoes tecnicas tomadas por agentes ou validadas por humanos.
Nunca delete uma ADR — se a decisao mudou, crie uma nova e marque a anterior como REVISADA.

### ADR-005 — Cerebro como fonte de verdade de contexto

- **Status:** Decidido (2026-04-15); **Atualizado** com ADR-008 (paths)
- **Decisao:** Este repositorio (`brain_v4_colli/`) e a fonte de verdade de contexto para todos os agentes semi-autonomos da Colli & Co.
- **Contexto:** Agentes que nao tem contexto persistente tomam decisoes ruins ou repetem trabalho ja feito. A solucao e um cerebro em markdown, versionavel e legivel por qualquer ferramenta.
- **Consequencia:** Todo agente deve ler `CLAUDE.md` ou `AGENTS.md` ao iniciar. Conhecimento operacional novo relevante vai para `projetos/` e `areas/`. Decisoes tecnicas novas devem gerar ADR aqui.

### ADR-006 — Operacao mutavel, fundamentos com protocolo

- **Status:** REVISADA (2026-04-15) — substitui redacao anterior sobre `streams/` e `docs/`
- **Decisao:** `projetos/` e `areas/` podem ser atualizados com frequencia por agentes, dentro do escopo da tarefa (`07-CONTEXT-SECURITY.md`). Arquivos em `empresa/contexto/01-` a `05-` exigem nota de revisao e cabecalho atualizado; mudancas grandes exigem intencao macro.
- **Contexto:** Precisamos de velocidade nos dados operacionais mas estabilidade nos fundamentos.
- **Consequencia:** Agentes podem escrever em `projetos/` e `areas/` quando o escopo permitir. Mudancas em fundamentos devem ser sinalizadas para revisao humana.

### ADR-007 — Nenhum dado sensivel de colaboradores ou clientes no cerebro

- **Status:** Decidido (2026-04-15)
- **Decisao:** Dados pessoais de colaboradores (salarios, avaliacoes) e dados confidenciais de clientes (contratos, valores) nao entram neste repositorio.
- **Contexto:** Este cerebro pode ser acessado por multiplos agentes com diferentes niveis de acesso. Vazamento de dados sensiveis e inaceitavel.
- **Consequencia:** Agentes que precisam desses dados devem acessar os sistemas de origem (v4-synk-rh, CRM) diretamente via API autorizada, nunca replicar para aqui.

### ADR-008 — Paths canonicos deste repositorio

- **Status:** Decidido (2026-04-15)
- **Decisao:** A estrutura oficial e `empresa/contexto/` (fundamentos + protocolos), `projetos/` (clientes), `areas/` (funcoes), `empresa/produtos/` (fichas). Nomes legados `docs/` e `streams/` nao correspondem a pastas neste repo.
- **Contexto:** Documentacao inicial descrevia uma arvore generica; a implementacao em `brain_v4_colli/` usa nomes diferentes.
- **Consequencia:** Toda documentacao interna deve usar estes paths; agentes nao devem criar `docs/` ou `streams/` aqui sem decisao explicita de reorganizacao.

---

## 6. Checklist de Sessao para Agentes

Antes de executar qualquer tarefa neste cerebro:

- [ ] Li `CLAUDE.md` ou `AGENTS.md`
- [ ] Li `06-AGENT-PROTOCOLS.md` e `07-CONTEXT-SECURITY.md`
- [ ] Sei qual vocabulario usar (`05-VOCABULARY.md`)
- [ ] Identifiquei onde vou escrever (se tiver output) e se o escopo e micro/meso/macro
- [ ] Nao vou inventar dados — declararei lacunas quando necessario
- [ ] Nao vou escrever dados sensiveis de colaboradores ou clientes

---

## 7. Fluxo de Sessao Tipica

1. Inicio da sessao
2. Ler `CLAUDE.md` ou `AGENTS.md`
3. Ler documentos em `empresa/contexto/` pertinentes a tarefa
4. Ler `projetos/` ou `areas/` quando precisar de estado vivo
5. Executar tarefa (limites de escopo: `07-CONTEXT-SECURITY.md`)
6. Persistir saida em `projetos/` ou `areas/` quando aplicavel
7. (Opcional) Atualizar fundamentos apenas com escopo macro e nota de revisao
8. Fim
