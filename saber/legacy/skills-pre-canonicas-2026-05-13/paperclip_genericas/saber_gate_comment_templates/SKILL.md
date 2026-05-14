---
name: saber_gate_comment_templates
description: >
  Textos mínimos para aprovar ou reprovar com rastreio ao gate B3. Use para humanos no quadro ou agente assistente de comentário.
---

# saber_gate_comment_templates

## Aprovar (exemplo)

"Aprovo entrega **vX.Y** para envio ao cliente. Gate B3 OK. Próximo passo: …"

## Reprovar (exemplo)

"Reprovo **vX.Y**: ajustar [ponto]. Ref: comentário [link/id]. Manter em revisão."

## Instruções

Substituir colchetes; sempre referenciar versão do artefato e próxima ação clara.

## Coordenação Paperclip

Quando o run estiver no **pool OPS** acoplado ao Paperclip: use a skill `paperclip` (ficheiro `paperclip/SKILL.md` nesta pasta) para checkout, comentários, anexos, status e header `X-Paperclip-Run-Id`. Trabalho de **domínio** (texto, análise, rascunhos) faz-se aqui; **governança do quadro** faz-se via API Paperclip conforme essa skill.

## Dados e processo canônicos

- No monorepo V4OS Colli&Co: `src/data/saber-bpmn.bundle.json` (jornada, estágios, tipos A/S/H/M).
- Planejamento: `V4OS Colli&Co/Plans/Execution/saber-tobe-bpmn-app/Paperclip-planejamento-skills.md`.

## Tipos de passo (A / S / H / M)

Alinhar saídas ao painel do bundle (`task_types`) e às colunas do issue (Briefing → Execução → **Aprovar entrega** quando for gate humano).
