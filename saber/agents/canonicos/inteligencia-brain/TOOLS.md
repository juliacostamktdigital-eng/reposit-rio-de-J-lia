# TOOLS - Inteligencia Brain
**Status:** v1
**Atualizado:** 2026-04-25
**Fonte:** agente:codex

---

## Como o Paperclip trabalha com skills

As skills deste agente sao ativadas na aba **Skills** do Paperclip. No run seguinte, o Paperclip vincula as skills ativas ao ambiente `CODEX_HOME/skills/`.

Este arquivo define contrato de uso de ferramentas e limites operacionais. O catalogo de skills esperadas vive em `./skills/README.md`.

## Skills ativas esperadas

- Consulte `./skills/README.md` para lista canonica de skills obrigatorias, opcionais e candidatas.
- Se uma skill esperada nao estiver disponivel no run, registre a lacuna na issue e siga com extracao/sintese factual sem assumir capacidades ausentes.

## Permitido

- Ler issue e variaveis de rotina (`mode`, `outputType`, `anchorDir`, `pathsJson`, `contextSubdir`).
- Ler arquivos explicitamente indicados em `pathsJson` (modo targeted).
- Criar/atualizar `inteligencia.md` e `plano-de-roi.md` no escopo permitido.
- Versionar historico do Plano de ROI e fechar issue apos execucao concluida.

## Nao permitido

- Escrever copy final, guia de voz ou consolidar entregavel final.
- Reorganizar estrutura do repositorio fora dos outputs permitidos.
- Inventar dados de stakeholder, faturamento, metas, SPICED ou claims.
- Expor segredos, tokens ou dados sensiveis.
