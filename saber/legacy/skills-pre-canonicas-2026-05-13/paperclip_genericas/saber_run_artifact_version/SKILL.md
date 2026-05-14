---
name: saber_run_artifact_version
description: >
  Convenção de versionamento de artefatos anexados ao issue e comentários pós-run. Use após cada run ou re-run pós-reprovação.
---

# saber_run_artifact_version

## Convenção

- Versão semântica leve: `v0.1`, `v0.2`, … até aprovação.
- Toda entrega em comentário: título com versão + data (ISO).
- Reprovação: incrementar minor; mencionar o comentário que motivou a revisão.

## Instruções

1. Detectar última versão no thread.
2. Propor próxima versão e nome sugerido do anexo (slug + ticker).
3. Lembrar `X-Paperclip-Run-Id` em mutações.

## Saída

Texto curto para colar no topo do comentário com artefato.

## Coordenação Paperclip

Quando o run estiver no **pool OPS** acoplado ao Paperclip: use a skill `paperclip` (ficheiro `paperclip/SKILL.md` nesta pasta) para checkout, comentários, anexos, status e header `X-Paperclip-Run-Id`. Trabalho de **domínio** (texto, análise, rascunhos) faz-se aqui; **governança do quadro** faz-se via API Paperclip conforme essa skill.

## Dados e processo canônicos

- No monorepo V4OS Colli&Co: `src/data/saber-bpmn.bundle.json` (jornada, estágios, tipos A/S/H/M).
- Planejamento: `V4OS Colli&Co/Plans/Execution/saber-tobe-bpmn-app/Paperclip-planejamento-skills.md`.

## Tipos de passo (A / S / H / M)

Alinhar saídas ao painel do bundle (`task_types`) e às colunas do issue (Briefing → Execução → **Aprovar entrega** quando for gate humano).
