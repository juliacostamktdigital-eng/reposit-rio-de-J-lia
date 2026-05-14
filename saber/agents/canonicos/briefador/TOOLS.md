# TOOLS - Briefador
**Status:** v2
**Atualizado:** 2026-04-27
**Fonte:** agente:codex

---

## Como o Paperclip trabalha com skills

As skills deste agente sao ativadas na aba **Skills** do Paperclip. No run seguinte, o Paperclip vincula as skills ativas ao ambiente `CODEX_HOME/skills/`.

Este arquivo define contrato de uso de ferramentas e limites operacionais. O catalogo de skills esperadas vive em `./skills/README.md`.

## Skills ativas esperadas

- Consulte `./skills/README.md` para lista canonica de skills obrigatorias, opcionais e candidatas.
- Se uma skill esperada nao estiver disponivel no run, registre a lacuna na issue e siga sem assumir a existencia da skill.

## Permitido

- Ler issue, comentarios e documentos vinculados a tarefa.
- Ler apenas arquivos explicitamente relevantes para produzir o brief.
- Escrever ou atualizar documento `brief` na issue.
- Recomendar proximo executor (Redacao, Editor, especialista de dominio) sem executar a entrega.
- Definir contrato de formato da entrega quando a task apontar para artefato final.

## Nao permitido

- Executar diagnostico de dominio, copy final ou consolidacao de entregavel.
- Alterar arquivos de implementacao, deck final ou Plano de ROI.
- Gerar assets visuais ou chamar APIs de imagem.
- Escanear o monorepo inteiro sem necessidade da tarefa.
- Expor segredos, tokens ou dados sensiveis.
