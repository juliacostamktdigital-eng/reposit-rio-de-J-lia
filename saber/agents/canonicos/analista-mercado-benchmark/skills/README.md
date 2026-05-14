# Skills — Analista de Mercado e Benchmark
**Status:** v1
**Atualizado:** 2026-04-27
**Fonte:** agente:codex

---

## Como o Paperclip entrega skills

As skills sao ativadas na aba **Skills** do agente no Paperclip e vinculadas ao `CODEX_HOME/skills/` no proximo run.

Este arquivo declara o contrato canonico de skills para o Analista de Mercado e Benchmark. A fonte primaria das skills promovidas continua em `empresa/skills/`.

## Skills esperadas no Paperclip

| Skill | Obrigatoria? | Fonte canonica | Quando usar |
|---|---|---|---|
| `sizing-mercado-tam-sam-som` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/sizing-mercado-tam-sam-som/SKILL.md` | T05 — TAM/SAM/SOM |
| `estudo-concorrentes` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/estudo-concorrentes/SKILL.md` | T06/T11 — concorrentes e comparativos |
| `definicao-icp-b2b` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/definicao-icp-b2b/SKILL.md` | T07 — ICP B2B |
| `definicao-persona-b2c` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/definicao-persona-b2c/SKILL.md` | T09 — Persona B2C |
| `swot-beachhead-market` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/swot-beachhead-market/SKILL.md` | Beachhead e segmento prioritario |
| `xlsx` | Opcional | `empresa/skills/gerais/xlsx/SKILL.md` | Planilhas e dados tabulares |
| `pdf` | Opcional | `empresa/skills/gerais/pdf/SKILL.md` | Relatorios e materiais em PDF |
| `github-gerenciamento` | Opcional | `empresa/skills/gerais/github-gerenciamento/SKILL.md` | Commit/PR quando solicitado |

## Regras

- Nao usar skills de deck neste agente.
- Nao usar PUV como output final; encaminhar para `estrategista-posicionamento`.
- Nao inventar fonte externa sem citar origem e incerteza.

