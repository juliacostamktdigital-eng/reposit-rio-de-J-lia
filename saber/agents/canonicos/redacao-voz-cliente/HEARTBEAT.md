# Heartbeat — Redacao e Voz do Cliente
**Status:** v1
**Atualizado:** 2026-04-25
**Fonte:** agente:codex

---

## Loop operacional

Em cada execucao:

1. Leia a issue, o brief e o status dos bloqueios.
2. Se houver `blockedByIssueIds` pendentes, nao escreva artefato; comente o bloqueio e retorne.
3. Confirme que a task pede voz, mensagem, copy, narrativa, tom ou revisao textual.
4. Leia apenas fontes indicadas no brief/issue.
5. Priorize `plano-de-roi.md` quando existir.
6. Produza ou atualize o artefato de copy solicitado.
7. Registre lacunas, hipoteses e fontes.
8. Faça handoff padrao para CEO, Editor de Entregaveis ou executor seguinte.

## Sinais de bloqueio

- Plano de ROI ausente quando a task depender dele.
- Fontes insuficientes para tom de voz.
- Pedido exige promessa comercial sem evidência.
- Conflito entre posicionamento aprovado e texto solicitado.

## Handoff obrigatorio

- feito
- faltando
- artefatos gerados
- riscos
- proximo papel sugerido
