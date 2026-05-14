---
name: gtm_followup_sequence
description: >
  Sequência de e-mails/mensagens em rascunho a partir de objeções e contexto. Funil GTM.
---

# gtm_followup_sequence

## Mapeamento: P.08a

## Saída

2–4 mensagens com assunto, corpo, CTA; tom alinhado à marca.

## Coordenação Paperclip

Quando o run estiver no **pool OPS** acoplado ao Paperclip: use a skill `paperclip` (ficheiro `paperclip/SKILL.md` nesta pasta) para checkout, comentários, anexos, status e header `X-Paperclip-Run-Id`. Trabalho de **domínio** (texto, análise, rascunhos) faz-se aqui; **governança do quadro** faz-se via API Paperclip conforme essa skill.

## Dados e processo canônicos

- No monorepo V4OS Colli&Co: `src/data/saber-bpmn.bundle.json` (jornada, estágios, tipos A/S/H/M).
- Planejamento: `V4OS Colli&Co/Plans/Execution/saber-tobe-bpmn-app/Paperclip-planejamento-skills.md`.

## Tipos de passo (A / S / H / M)

Alinhar saídas ao painel do bundle (`task_types`) e às colunas do issue (Briefing → Execução → **Aprovar entrega** quando for gate humano).
