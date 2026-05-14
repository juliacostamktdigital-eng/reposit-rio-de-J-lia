---
name: saber_bpmn_context
description: >
  Injeta trecho do processo BPMN/jornada relevante à etapa do pedido (GC, KO, CX, …). Use no pré-run ou quando o orquestrador precisar do que é permitido na etapa.
---

# saber_bpmn_context

## Escopo

Orquestrador ou agente carrega o **estágio OPS ou vendas** atual (ex.: `gc`, `ko`, `bm`) e produz um resumo operacional: objetivos da fase, entradas/saídas esperadas do bundle, e restrições para o run.

## Instruções

1. Identificar `stage_id` do issue (rótulo, template ou metadado).
2. Ler em `saber-bpmn.bundle.json` o objeto `stages.<stage_id>` (título, inputs, outputs, gateway, steps).
3. Entregar markdown curto: título da fase, lista de passos com IDs (ex. GC.02), e nota de **gate humano** quando o passo for tipo revisão (`s`/`S`).

## Saída

Bloco markdown pronto para colar na descrição do issue, em documento `plan`, ou no contexto do run.

## Coordenação Paperclip

Quando o run estiver no **pool OPS** acoplado ao Paperclip: use a skill `paperclip` (ficheiro `paperclip/SKILL.md` nesta pasta) para checkout, comentários, anexos, status e header `X-Paperclip-Run-Id`. Trabalho de **domínio** (texto, análise, rascunhos) faz-se aqui; **governança do quadro** faz-se via API Paperclip conforme essa skill.

## Dados e processo canônicos

- No monorepo V4OS Colli&Co: `src/data/saber-bpmn.bundle.json` (jornada, estágios, tipos A/S/H/M).
- Planejamento: `V4OS Colli&Co/Plans/Execution/saber-tobe-bpmn-app/Paperclip-planejamento-skills.md`.

## Tipos de passo (A / S / H / M)

Alinhar saídas ao painel do bundle (`task_types`) e às colunas do issue (Briefing → Execução → **Aprovar entrega** quando for gate humano).
