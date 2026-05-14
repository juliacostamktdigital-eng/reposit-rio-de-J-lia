# Skills — Inteligencia Brain
**Status:** v1
**Atualizado:** 2026-04-25
**Fonte:** agente:codex

---

## Como o Paperclip entrega skills

As skills sao ativadas na aba **Skills** do agente no Paperclip e vinculadas ao `CODEX_HOME/skills/` no proximo run.

O Inteligencia Brain deve usar skills apenas para extracao, sintese e validacao de contexto. Ele nao escreve copy final nem consolida entregaveis.

## Estrutura local por agente

- `skills/ativas/` guarda copias locais das skills ativas deste agente.
- `skills/incubacao/` guarda skills candidatas em teste ou adaptacao.
- Cada skill local deve conter `SKILL.md` e `META.md`.
- Promocao para catalogo global segue `skills/CHECKLIST-PROMOCAO-PARA-GLOBAL.md`.
- O catalogo global publicado continua em `empresa/skills/`.

## Skills esperadas no Paperclip

| Skill | Obrigatoria? | Fonte canonica | Quando usar |
|---|---|---|---|
| `paperclip` | Sim | Paperclip company library | Ler issue, fechar run e operar rotina |
| `saber_session_extract` | Candidata | `empresa/skills/saber/skills/legacy/paperclip_genericas/saber_session_extract/SKILL.md` | Extrair informacoes de sessoes/calls antes de atualizar inteligencia ou Plano de ROI |
| `gtm_spiced_extract` | Candidata | `empresa/skills/saber/skills/legacy/paperclip_genericas/gtm_spiced_extract/SKILL.md` | Extrair SPICED quando a fonte vier de vendas |
| `ops_post_kickoff_extract` | Candidata | `empresa/skills/saber/skills/legacy/paperclip_genericas/ops_post_kickoff_extract/SKILL.md` | Extrair desvios e aprendizados de kickoff |
| `ops_context_diff` | Candidata | `empresa/skills/saber/skills/legacy/paperclip_genericas/ops_context_diff/SKILL.md` | Comparar nova fonte com contexto anterior e marcar conflitos |
| `saber_run_artifact_version` | Candidata | `empresa/skills/saber/skills/legacy/paperclip_genericas/saber_run_artifact_version/SKILL.md` | Apoiar versionamento de `plano-de-roi.md` |

## Backlog de skills a criar/adaptar

| Skill desejada | Motivo |
|---|---|
| `plano-roi-iterate` | Criar/iterar Plano de ROI com schema EP-07 |
| `plano-roi-completeness-check` | Validar gate minimo antes de liberar especialistas |
| `context-conflict-register` | Padronizar registro de conflitos entre versoes |

## Regra

Se a task pedir voz, copy, deck ou entrega final, o Brain apenas atualiza contexto e recomenda handoff para Redacao ou Editor.
