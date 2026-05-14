# Skills — Bibliotecario Projetos
**Status:** v1
**Atualizado:** 2026-04-25
**Fonte:** agente:codex

---

## Como o Paperclip entrega skills

As skills sao ativadas na aba **Skills** do agente no Paperclip e vinculadas ao `CODEX_HOME/skills/` no proximo run.

O Bibliotecario usa skills de organizacao, Git e contexto. Ele nao executa diagnosticos nem entregas de cliente.

## Estrutura local por agente

- `skills/ativas/` guarda copias locais das skills ativas deste agente.
- `skills/incubacao/` guarda skills candidatas em teste ou adaptacao.
- Cada skill local deve conter `SKILL.md` e `META.md`.
- Promocao para catalogo global segue `skills/CHECKLIST-PROMOCAO-PARA-GLOBAL.md`.
- O catalogo global publicado continua em `empresa/skills/`.

## Skills esperadas no Paperclip

| Skill | Obrigatoria? | Fonte canonica | Quando usar |
|---|---|---|---|
| `paperclip` | Sim | Paperclip company library | Operar issues, rotinas e comentarios |
| `github-gerenciamento` | Opcional | `empresa/skills/gerais/github-gerenciamento/SKILL.md` | Apoiar commits/branches/PRs quando a task pedir |
| `organizar-temp-repositorio` | Sim | `empresa/skills/gerais/organizar-temp-repositorio/SKILL.md` | Higiene de arquivos soltos e estrutura de repo |
| `ops_project_scaffold` | Candidata | `empresa/skills/saber/skills/legacy/paperclip_genericas/ops_project_scaffold/SKILL.md` | Criar estrutura inicial de projeto/cliente quando aplicavel |
| `ops_canonical_publish` | Candidata | `empresa/skills/saber/skills/legacy/paperclip_genericas/ops_canonical_publish/SKILL.md` | Publicar/organizar artefatos canonicos quando houver fluxo aprovado |

## Regra

Se a task envolver conteudo de cliente ou entrega Saber, o Bibliotecario deve organizar paths e handoff, nao produzir diagnostico.
