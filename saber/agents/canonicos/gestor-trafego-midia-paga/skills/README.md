# Skills — Gestor de Trafego e Midia Paga
**Status:** v1
**Atualizado:** 2026-04-27
**Fonte:** agente:codex

---

## Como o Paperclip entrega skills

As skills sao ativadas na aba **Skills** do agente no Paperclip e vinculadas ao `CODEX_HOME/skills/` no proximo run.

## Skills esperadas no Paperclip

| Skill | Obrigatoria? | Fonte canonica | Quando usar |
|---|---|---|---|
| `diagnostico-meta-ads` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/diagnostico-meta-ads/SKILL.md` | T14 — Meta Ads |
| `diagnostico-google-ads` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/diagnostico-google-ads/SKILL.md` | T15 — Google Ads |
| `analise-eficiencia-investimentos` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/analise-eficiencia-investimentos/SKILL.md` | T16 — eficiencia de investimento |
| `forecast-midia-3-meses` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/forecast-midia-3-meses/SKILL.md` | T34 — forecast |
| `xlsx` | Opcional | `empresa/skills/gerais/xlsx/SKILL.md` | Exports de ads/CRM |
| `pdf` | Opcional | `empresa/skills/gerais/pdf/SKILL.md` | Relatorios exportados |
| `github-gerenciamento` | Opcional | `empresa/skills/gerais/github-gerenciamento/SKILL.md` | Commit/PR quando solicitado |

## Regras

- Nao operar campanhas.
- Nao usar skills de deck neste agente.
- Forecast precisa declarar premissas comerciais e lacunas.

