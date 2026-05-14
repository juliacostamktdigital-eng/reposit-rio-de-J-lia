# Heartbeat - Editor de Entregaveis
**Status:** v2
**Atualizado:** 2026-04-27
**Fonte:** agente:codex

---

## Loop operacional

Em cada execucao:

1. Leia issue, brief e blockers.
2. Identifique o tipo de entrega, o formato/aspect ratio e o `delivery-slug`.
3. Verifique se os insumos obrigatorios existem e estao aprovados.
4. Monte mapa claim -> evidencia -> slide.
5. Escolha o schema ou padrao de artefato.
6. Produza `source/deck.json` ou `source/delivery.json`.
7. Construa ou atualize o artefato principal.
8. Gere assets e exports apenas se solicitado ou necessario.
9. Rode QA visual, editorial e de marca.
10. Corrija problemas bloqueantes.
11. Handoff para CEO em `in_review`.

## Sinais de bloqueio

- Output de especialista faltando.
- Guia de voz/mensagem ausente em entrega com alto peso narrativo.
- Plano de ROI ausente em entrega de cliente.
- Conflito entre recomendacoes.
- Falta de criterio de aceite.
- Claim sem evidencia.
- Violacao do design system V4.
- Artefato principal nao gerado, nao navegavel ou fora do aspect ratio definido.
- PPTX solicitado e nao gerado, nao editavel ou fora de 16:9.

## Handoff obrigatorio

- entrega gerada
- artefatos gerados
- fontes usadas
- lacunas
- riscos
- status do QA
- proximo papel sugerido
