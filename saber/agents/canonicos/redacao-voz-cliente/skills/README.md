# Skills — Redacao e Voz do Cliente
**Status:** v1
**Atualizado:** 2026-04-25
**Fonte:** agente:codex

---

## Como o Paperclip entrega skills

As skills sao ativadas na aba **Skills** do agente no Paperclip e vinculadas ao `CODEX_HOME/skills/` no proximo run.

Este arquivo declara o contrato canonico de skills para Redacao. O conteudo das skills continua nos diretorios de origem.

## Estrutura local por agente

- `skills/ativas/` guarda copias locais das skills ativas deste agente.
- `skills/incubacao/` guarda skills candidatas em teste ou adaptacao.
- Cada skill local deve conter `SKILL.md` e `META.md`.
- Promocao para catalogo global segue `skills/CHECKLIST-PROMOCAO-PARA-GLOBAL.md`.
- O catalogo global publicado continua em `empresa/skills/`.

## Skills esperadas no Paperclip

| Skill | Obrigatoria? | Fonte canonica | Quando usar |
|---|---|---|---|
| `diagnostico-copy-lp` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/diagnostico-copy-lp/SKILL.md` | Avaliar promessa, clareza, CTA, message match e copy de LP |
| `proposta-unica-de-valor` | Sim | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/proposta-unica-de-valor/SKILL.md` | Apoiar mensagens centrais, PUV e variações de valor |
| `analise-criativos` | Opcional | `empresa/skills/saber/skills/skills_extract_entregas/skills/v4-diagnostico-planejamento/analise-criativos/SKILL.md` | Avaliar copy/mensagem de criativos junto ao contexto visual |
| `crafting-positioning` | Candidata | `empresa/skills/gtm-strategist-skills-master/.claude/skills/crafting-positioning/SKILL.md` | Adaptar frameworks de posicionamento e mensagem |
| `building-communication-engine` | Candidata | `empresa/skills/gtm-strategist-skills-master/.claude/skills/building-communication-engine/SKILL.md` | Criar sistema de mensagem/canais quando fizer sentido |
| `preparing-launch-assets` | Candidata | `empresa/skills/gtm-strategist-skills-master/.claude/skills/preparing-launch-assets/SKILL.md` | Adaptar blocos de copy para assets e campanha |
| `executar/agents/copywriter` | Referencia | `empresa/skills/executar/agents/copywriter/context.md` | Contexto de papel para copywriter na operacao Executar |

## Backlog de skills a criar/adaptar

| Skill desejada | Motivo |
|---|---|
| `manual-copy-saber` | Criar manual de copy por cliente com tom, pilares, exemplos e limites |
| `voz-cliente-extract` | Extrair voz do cliente de calls, site, redes e materiais existentes |
| `mensagem-por-canal` | Adaptar mensagem para deck, LP, criativo, WhatsApp e proposta |
| `claim-evidence-check` | Checar se promessas e claims possuem fonte/prova |
| `copy-style-regression` | Comparar novo texto contra guia de voz/mensagem |

## Regras de uso

- Nao usar skill de copy para inventar promessa.
- Quando `diagnostico-copy-lp` apontar problema de mensagem, produzir recomendacao em `voz-e-mensagem.md` ou `revisao-copy-<artefato>.md`.
- Skills GTM externas/localizadas em `gtm-strategist-skills-master` sao candidatas: adaptar antes de virar obrigatorio no Paperclip.
