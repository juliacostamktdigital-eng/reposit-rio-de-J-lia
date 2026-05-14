# Seguranca de Contexto, Escopo e Commits — Brain V4 Colli
**Status:** v1 — Fundamento
**Atualizado:** 2026-04-15
**Fonte:** humano (Luis Santos)

---

## Proposito

Impedir que tarefas **pequenas** ou sessoes **mal delimitadas** corrompam **fundamentos globais** do cerebro, misturem repositorios, ou gerem commits dificeis de auditar. Este arquivo e **obrigatorio** junto com `06-AGENT-PROTOCOLS.md` antes de qualquer escrita ou commit.

---

## 1. Niveis de escopo de tarefa

| Nivel | Descricao | Onde pode escrever (padrao) |
|-------|-----------|------------------------------|
| **Micro** | Ajuste pontual: um arquivo, um cliente, um playbook, correcao cirurgica | Somente paths **explicitamente** pedidos pelo humano ou listados no ticket |
| **Meso** | Uma area funcional (ex.: vendas): varios arquivos sob `areas/<area>/` | `areas/<area>/` e, se necessario, `projetos/` ligados ao escopo |
| **Macro** | Reorganizacao do cerebro, novo padrao global, ADR, mudanca de invariantes | `empresa/contexto/`, indices (`CLAUDE.md`, `AGENTS.md`), com **revisao humana** implícita |

**Regra de ouro:** em tarefa **micro**, e **proibido** alterar `empresa/contexto/*` (exceto se o pedido citar arquivo concreto **e** o conteudo for estritamente sobre esse pedido), `CLAUDE.md`, `AGENTS.md`, `empresa/produtos/*`, ou pastas **fora** de `brain_v4_colli/`.

---

## 2. Classificacao de diretorios (risco)

| Risco | Pastas | Comportamento obrigatorio |
|-------|--------|-------------------------|
| **Alto — contexto global** | `empresa/contexto/` | Mudanca so com intencao declarada (macro), nota de revisao quando aplicavel (`00-DOC-STANDARDS.md`), sem "limpeza" nao solicitada |
| **Alto — fonte humana** | `empresa/produtos/` | **Nao** deletar nem reescrever fichas; correcoes minimas apenas se o humano pedir arquivo especifico |
| **Medio — indices** | `CLAUDE.md`, `AGENTS.md`, `empresa/MAPA.md`, `areas/*/MAPA.md` | Atualizar apenas quando a estrutura realmente mudou; nunca em passagem de uma task micro nao relacionada |
| **Baixo — operacao** | `projetos/`, `areas/<area>/` (exceto MAPA se nao for o foco) | Local padrao para persistir contexto vivo; preferir aqui em tasks micro/meso |

---

## 3. Commits (quando este cerebro estiver versionado em Git)

1. **Um assunto por commit** — nao misturar "fix tier no template" com "reescrita do vocabulario" e "patch no app X" fora de `brain_v4_colli/`.
2. **Escopo do path no corpo da mensagem** se o diff for grande: ex. `brain_v4_colli/areas/vendas/ apenas`.
3. **Nunca** commitar: secrets, tokens, dados sensiveis de clientes ou colaboradores (ja vedado em `06-AGENT-PROTOCOLS.md`).
4. **Monorepo:** se `brain_v4_colli` for subpasta de um repo maior, preferir commits que toquem **somente** arquivos sob `brain_v4_colli/`; se precisar cruzar para outro projeto, **commit separado** ou explicitamente justificado.
5. **Mensagem clara em portugues ou ingles** (consistente com o time), imperativo ou descritivo, com o **porque** quando nao for obvio.

---

## 4. Anti-padroes (falhas de seguranca de contexto)

- Expandir sozinho o escopo: "aproveitei e reorganizei `empresa/contexto/`".
- Padronizar nomenclatura em massa sem pedido.
- Copiar para ca colunas de planilha, contratos ou dumps de CRM "para referencia".
- Assumir que `docs/` ou `streams/` existem neste repo (paths canonicos estao em `00-DOC-STANDARDS.md`).
- Editar `00-DOC-STANDARDS.md` ou `06-AGENT-PROTOCOLS.md` em uma task que era "atualizar um projeto cliente".

---

## 5. Checklist antes de finalizar sessao com mudancas

- [ ] Todos os arquivos alterados estao **dentro do escopo** acordado (micro/meso/macro)?
- [ ] Nenhum arquivo **alto risco** foi tocado sem necessidade?
- [ ] Cabecalhos `**Atualizado:**` / `**Fonte:**` atualizados onde a regra do cerebro exige?
- [ ] Commit(s) separados por assunto (se aplicavel)?
- [ ] Lacunas e inferencias marcadas quando nao ha certeza?

---

## 6. Precedencia

Em duvida entre "melhorar o cerebro todo" e "cumprir o pedido minimo", vale **o pedido minimo** ate haver revisao humana ou task macro explicita.
