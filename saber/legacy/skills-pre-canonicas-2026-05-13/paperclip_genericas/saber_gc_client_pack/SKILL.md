---
name: saber_gc_client_pack
description: >
  Pacote cliente pós-handoff OPS: comunicação ao cliente (convite, DMD, próximos passos) e relatório curto desvios promessa × expectativa. Agrega GC.02 + GC.05 num único run; GC.04 fora se ASR manual.
---

# saber_gc_client_pack

## Entrada

Manifest/handoff resumido, ROI, transcrição ou notas da GC, instruções do Coord.

## Saída

**(a)** Texto ao cliente (tom profissional, pt-BR) com convite/links/DMD e próximos passos.
**(b)** Relatório interno curto: promessa (vendas) vs briefing/ROI; riscos de handoff; hipóteses marcadas como tal.

## Gate

Saída **não** é oficial para cliente sem aprovação no quadro (gate S).

## Coordenação Paperclip

Quando o run estiver no **pool OPS** acoplado ao Paperclip: use a skill `paperclip` (ficheiro `paperclip/SKILL.md` nesta pasta) para checkout, comentários, anexos, status e header `X-Paperclip-Run-Id`. Trabalho de **domínio** (texto, análise, rascunhos) faz-se aqui; **governança do quadro** faz-se via API Paperclip conforme essa skill.

## Dados e processo canônicos

- No monorepo V4OS Colli&Co: `src/data/saber-bpmn.bundle.json` (jornada, estágios, tipos A/S/H/M).
- Planejamento: `V4OS Colli&Co/Plans/Execution/saber-tobe-bpmn-app/Paperclip-planejamento-skills.md`.

## Tipos de passo (A / S / H / M)

Alinhar saídas ao painel do bundle (`task_types`) e às colunas do issue (Briefing → Execução → **Aprovar entrega** quando for gate humano).
