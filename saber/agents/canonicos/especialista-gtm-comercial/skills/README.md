# Skills — Especialista GTM e Comercial
**Status:** v1
**Atualizado:** 2026-04-27
**Fonte:** agente:codex

---

## Como o Paperclip entrega skills

As skills sao ativadas na aba **Skills** do agente no Paperclip e vinculadas ao `CODEX_HOME/skills/` no proximo run.

## Skills esperadas no Paperclip

| Skill | Obrigatoria? | Fonte canonica | Quando usar |
|---|---|---|---|
| `diagnostico-comercial-crm` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/diagnostico-comercial-crm/SKILL.md` | T26 — processo comercial |
| `analise-crm-receita` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/analise-crm-receita/SKILL.md` | Receita, segmento, LTV, win rate |
| `cliente-oculto` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/cliente-oculto/SKILL.md` | T27 — cliente oculto comercial |
| `gtm-priorizacao-canais` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/gtm-priorizacao-canais/SKILL.md` | T29 — matriz GTM |
| `drawflow-estrategia-aquisicao` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/drawflow-estrategia-aquisicao/SKILL.md` | T30 — fluxo AEMR/aquisicao |
| `diagnostico-travas-scoring` | Opcional | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/diagnostico-travas-scoring/SKILL.md` | Gargalo maior / restricao |
| `forecast-midia-3-meses` | Secundaria | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/forecast-midia-3-meses/SKILL.md` | Validar premissas comerciais do forecast |
| `xlsx` | Opcional | `empresa/skills/gerais/xlsx/SKILL.md` | Export CRM/receita |
| `github-gerenciamento` | Opcional | `empresa/skills/gerais/github-gerenciamento/SKILL.md` | Commit/PR quando solicitado |

## Regras

- Nao usar skills de deck neste agente.
- Nao alterar CRM.
- Nao decidir precificacao final sem CEO/humano.

