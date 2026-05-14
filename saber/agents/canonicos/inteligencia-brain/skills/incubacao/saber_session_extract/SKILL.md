---
name: saber_session_extract
description: >
  Extrai de transcrição ou notas: objetivos, decisões, riscos, próximos passos e perguntas abertas, com referência a timestamp/turno quando existir. MVP OPS — eficiência consultor.
---

# saber_session_extract

## Entrada

Transcrição ou notas brutas (issue, anexo ou documento).

## Saída

1. **Objetivos** acordados
2. **Decisões** (bullet, quem/decisão)
3. **Riscos** e dependências
4. **Próximos passos** acionáveis
5. **Abertos** / perguntas
6. Quando houver tempo ou turno na fonte, cite entre parênteses.

## Notas

Rascunho para revisão humana; não substitui POP nem evidências formais.

## Coordenação Paperclip

Quando o run estiver no **pool OPS** acoplado ao Paperclip: use a skill `paperclip` (ficheiro `paperclip/SKILL.md` nesta pasta) para checkout, comentários, anexos, status e header `X-Paperclip-Run-Id`. Trabalho de **domínio** (texto, análise, rascunhos) faz-se aqui; **governança do quadro** faz-se via API Paperclip conforme essa skill.

## Dados e processo canônicos

- No monorepo V4OS Colli&Co: `src/data/saber-bpmn.bundle.json` (jornada, estágios, tipos A/S/H/M).
- Planejamento: `V4OS Colli&Co/Plans/Execution/saber-tobe-bpmn-app/Paperclip-planejamento-skills.md`.

## Tipos de passo (A / S / H / M)

Alinhar saídas ao painel do bundle (`task_types`) e às colunas do issue (Briefing → Execução → **Aprovar entrega** quando for gate humano).
