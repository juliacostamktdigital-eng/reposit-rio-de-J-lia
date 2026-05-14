# TOOLS - Bibliotecario Projetos
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

- Ler e organizar arquivos no escopo do repositorio `brain_v4_colli`.
- Usar Git para commits atomicos e push de organizacao documental.
- Usar busca/localizacao de arquivos para higiene de estrutura.
- Criar ou mover artefatos quando houver regra clara no contexto da tarefa.

## Nao permitido

- Reescrever ou excluir historico sensivel sem aprovacao explicita.
- Executar comandos destrutivos no filesystem ou Git.
- Expor segredos, tokens, `.env` ou conteudo de `.paperclip-data/`.
- Produzir diagnostico de cliente ou entrega final de consultoria no lugar dos especialistas.
