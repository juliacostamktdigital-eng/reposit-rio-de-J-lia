# Convenções de Versionamento

> Sistema: Semantic Versioning adaptado para skills de agentes

---

## Formato

```
v{MAJOR}.{MINOR}.{PATCH}
```

| Campo | Quando incrementar |
|-------|--------------------|
| `MAJOR` | Mudança de comportamento incompatível — o agente age de forma diferente, outputs mudam estrutura, premissas são invertidas |
| `MINOR` | Nova capacidade, novo parâmetro, nova condição adicionada sem quebrar o que já existe |
| `PATCH` | Correção de texto, ajuste de tom, clarificação de instrução sem mudar comportamento |

### Exemplos práticos

| Situação | Versão anterior | Nova versão |
|----------|----------------|-------------|
| Skill de copy reescrita com nova estrutura de output | v1.3.2 | v2.0.0 |
| Adição de suporte a segmento `saas` que antes não existia | v1.3.2 | v1.4.0 |
| Correção de typo nas instruções | v1.3.2 | v1.3.3 |
| Adição de exemplo de uso sem mudar instrução | v1.3.2 | v1.3.3 |

---

## Estrutura de arquivos por skill

```
{skill-name}/
├── context.md      ← metadados + propósito + índice
├── v1.0.0.md       ← conteúdo imutável (nunca edite versões antigas)
├── v1.1.0.md       ← nova versão
├── latest.md       ← sempre igual ao conteúdo da última versão
└── CHANGELOG.md    ← histórico cronológico
```

### Regras de imutabilidade

- **Arquivos `v{X}.Y.Z.md` são imutáveis** após publicação. Se precisar corrigir, crie um `PATCH` novo.
- **`latest.md` é mutável** — sempre sobrescrito com o conteúdo da versão mais recente.
- **`context.md` é vivo** — atualizado a cada nova versão nos campos `latest` e `updated`.

---

## Template: `context.md` de uma skill

```markdown
---
skill: nome-da-skill
owner: nome-do-agente          # agente responsável pela skill
latest: v1.0.0                 # versão atual em produção
status: active                 # active | draft | deprecated
segment:
  - b2b                        # b2b | b2c | b2b2c
tier:
  - growth                     # starter | growth | scale | enterprise
software:
  - mcp                        # mcp | api | manual
specialization:
  - ecom                       # ecom | inside-sales | local-business | saas | infoproduto
created: 2026-04-06
updated: 2026-04-06
---

## Propósito

[O que esta skill faz e por que existe]

## Quando usar

[Situações concretas em que esta skill deve ser ativada]

## Quando NÃO usar

[Situações em que outra skill ou agente é mais adequado]

## Inputs esperados

- `input_1` — descrição
- `input_2` — descrição

## Output esperado

[Formato e estrutura do resultado]

## Agentes que usam esta skill

- `owner`: [agente principal]
- `consumers`: [outros agentes que consomem]

## Versões disponíveis

| Versão | Data | Status | Resumo |
|--------|------|--------|--------|
| v1.0.0 | 2026-04-06 | latest | Versão inicial |
```

---

## Template: `CHANGELOG.md` de uma skill

```markdown
# CHANGELOG — {skill-name}

## [v1.1.0] — 2026-04-06
### Adicionado
- Suporte ao segmento `saas`

### Alterado
- Tom ajustado para abordagem consultiva

---

## [v1.0.0] — 2026-04-06
### Inicial
- Versão de lançamento
```

---

## Status de uma skill

| Status | Significado |
|--------|-------------|
| `active` | Em uso em produção |
| `draft` | Em desenvolvimento, não usar em produção |
| `deprecated` | Substituída por versão mais nova ou outra skill — não criar novas instâncias |

---

## Depreciação

1. Mude `status` para `deprecated` no `context.md`
2. Adicione no topo do `latest.md` e do `context.md`:
   ```
   > ⚠️ DEPRECATED — Use [nova-skill](../nova-skill/context.md) em vez desta.
   ```
3. Mantenha os arquivos por pelo menos 2 ciclos de revisão antes de deletar

---

## Ciclo de revisão

Recomendado revisar o status de todas as skills a cada **30 dias**. Critérios:
- Skills sem uso por 60 dias → candidatas a `deprecated`
- Skills com 3+ patches em sequência → candidatas a `MINOR` consolidado
- Skills com mudança de premissa de negócio → `MAJOR` obrigatório

---

## Governança Git: pull request por skill

Alterações em skills **não** devem ser integradas por commits diretos na branch principal sem passar por revisão.

1. **Uma pull request por skill** — cada PR trata de uma única skill (ou de um conjunto mínimo coerente, ex.: migração mecânica documentada), com título e descrição que identifiquem o nome da skill e a versão nova (ex.: `v1.2.0`).
2. **Sem reescrita de histórico versionado** — a PR adiciona o novo `v{X.Y.Z}.md`, atualiza `latest.md`, `context.md` e `CHANGELOG.md` conforme as regras deste documento; não edita ficheiros `v*.*.*.md` já publicados.
3. **Aprovação humana** — merge só após aprovação explícita (donos de processo / revisores designados), em linha com a política de branch protection do repositório.

Skills do processo **SABER** (`saber/skills/`) seguem o mesmo princípio; ver também [`saber/skills/VERSIONAMENTO.md`](../../saber/skills/VERSIONAMENTO.md) para o alinhamento com `SKILL.md` Paperclip.
