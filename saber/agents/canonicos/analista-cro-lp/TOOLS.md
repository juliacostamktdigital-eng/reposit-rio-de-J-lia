# TOOLS - analista-cro-lp
**Status:** v1
**Atualizado:** 2026-04-27
**Fonte:** agente:codex

---

## Como o Paperclip trabalha com skills

As skills deste agente sao ativadas na aba **Skills** do Paperclip. No run seguinte, o Paperclip vincula as skills ativas ao ambiente `CODEX_HOME/skills/`.

Consulte `./skills/README.md` para lista canonica de skills obrigatorias, opcionais e candidatas.

## Permitido

- Ler arquivos explicitamente indicados na issue ou no brief.
- Ler `projetos/<slug>/plano-de-roi.md` e outputs predecessores quando relevantes.
- Criar/editar arquivos apenas nos paths de output combinados para a task.
- Usar skills ativas vinculadas ao agente.
- Usar Git/GitHub apenas quando a issue pedir persistencia, commit ou PR.

## Nao permitido

- Ler o monorepo inteiro sem necessidade.
- Usar skills de deck como dependencia deste agente de dominio.
- Alterar Plano de ROI, decks finais, CRM, campanhas, automacoes ou arquivos fora do escopo.
- Rodar comandos destrutivos.
- Expor secrets, tokens ou dados sensiveis.
