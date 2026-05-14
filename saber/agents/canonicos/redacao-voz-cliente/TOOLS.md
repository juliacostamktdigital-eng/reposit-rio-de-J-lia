# TOOLS - Redacao e Voz do Cliente
**Status:** v1
**Atualizado:** 2026-04-25
**Fonte:** agente:codex

---

## Como o Paperclip trabalha com skills

As skills deste agente sao ativadas na aba **Skills** do Paperclip. No run seguinte, o Paperclip vincula as skills ativas ao ambiente `CODEX_HOME/skills/`.

Este arquivo define contrato de uso de ferramentas e limites operacionais. O catalogo de skills esperadas vive em `./skills/README.md`.

## Skills ativas esperadas

- Consulte `./skills/README.md` para lista canonica de skills obrigatorias, opcionais e candidatas.
- Se uma skill esperada nao estiver disponivel no run, registre a lacuna na issue e siga sem assumir a existencia da skill.

## Permitido

- Ler arquivos explicitamente indicados na issue/brief.
- Usar busca textual dentro do escopo do cliente para localizar termos de voz e mensagem.
- Criar/editar arquivos em `projetos/<slug>/context/copy/` quando a task pedir artefato persistente.
- Criar documento de issue quando o Paperclip pedir output sem arquivo.

## Nao permitido

- Ler o monorepo inteiro sem necessidade.
- Usar fontes externas sem autorizacao explicita.
- Alterar Plano de ROI.
- Alterar decks finais ou arquivos de implementacao sem task especifica.
- Rodar comandos destrutivos.
- Expor secrets, tokens ou dados sensiveis.
