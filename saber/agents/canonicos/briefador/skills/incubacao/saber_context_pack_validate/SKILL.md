---
name: saber_context_pack_validate
description: >
  Valida pacote mínimo do pedido (ticker, links, refs POP) antes de run B2 pesado. Use na coluna Preparação ou checklist do issue.
---

# saber_context_pack_validate

## Pacote mínimo

Verificar presença e formato razoável de:

- `ticker` (código projeto Saber)
- Links: grupo/chat, pasta Drive ou equivalente, gravação/transcrição se houver
- Instruções do Coord / operador
- Referências POP ou IDs de passos quando a etapa exigir

## Instruções

1. Listar campos obrigatórios do template do issue.
2. Para cada um, OK / ausente / ambíguo.
3. Se faltar algo crítico: não iniciar síntese pesada; pedir completar no comentário (via skill `paperclip`).

## Saída

Checklist tabular + uma frase de **go/no-go** para o run.

## Coordenação Paperclip

Quando o run estiver no **pool OPS** acoplado ao Paperclip: use a skill `paperclip` (ficheiro `paperclip/SKILL.md` nesta pasta) para checkout, comentários, anexos, status e header `X-Paperclip-Run-Id`. Trabalho de **domínio** (texto, análise, rascunhos) faz-se aqui; **governança do quadro** faz-se via API Paperclip conforme essa skill.

## Dados e processo canônicos

- No monorepo V4OS Colli&Co: `src/data/saber-bpmn.bundle.json` (jornada, estágios, tipos A/S/H/M).
- Planejamento: `V4OS Colli&Co/Plans/Execution/saber-tobe-bpmn-app/Paperclip-planejamento-skills.md`.

## Tipos de passo (A / S / H / M)

Alinhar saídas ao painel do bundle (`task_types`) e às colunas do issue (Briefing → Execução → **Aprovar entrega** quando for gate humano).
