# Skills — CEO
**Status:** v1
**Atualizado:** 2026-04-25
**Fonte:** agente:codex

---

## Como o Paperclip entrega skills

As skills sao gerenciadas na aba **Skills** do agente no Paperclip. Quando ativadas, o Paperclip as vincula ao `CODEX_HOME/skills/` efetivo no proximo run.

Este arquivo nao copia skills. Ele declara quais devem estar ativas e quando usar.

## Estrutura local por agente

- `skills/ativas/` guarda copias locais das skills ativas deste agente.
- `skills/incubacao/` guarda skills candidatas em teste ou adaptacao.
- Cada skill local deve conter `SKILL.md` e `META.md`.
- Promocao para catalogo global segue `skills/CHECKLIST-PROMOCAO-PARA-GLOBAL.md`.
- O catalogo global publicado continua em `empresa/skills/`.

## Skills esperadas no Paperclip

| Skill | Obrigatoria? | Fonte canonica | Quando usar |
|---|---|---|---|
| `paperclip` | Sim | Paperclip company library | Operar issues, documentos, comentarios, rotinas e API Paperclip |
| `paperclip-create-agent` | Sim | Paperclip company library | Criar/hire agentes quando faltar capacidade |
| `paperclip-create-plugin` | Opcional | Paperclip company library | Criar plugin quando a task for extensao de plataforma |
| `para-memory-files` | Sim | Paperclip company library | Memoria, planos e aprendizados metodologicos |

## Skills que o CEO deve governar, nao executar como IC

| Skill | Dono executor preferido | Observacao |
|---|---|---|
| `deck-semana-estruturacao` | `editor-entregaveis` | CEO revisa/aprova |
| `deck-entrega-final` | `editor-entregaveis` | CEO revisa/aprova |
| `plano-de-acao-5w2h` | `editor-entregaveis` | CEO governa criterios |
| `diagnostico-travas-scoring` | especialista + `editor-entregaveis` | CEO resolve conflito |
| `diagnostico-copy-lp` | `redacao-voz-cliente` | CEO nao escreve copy |

## Regra

Se uma skill de dominio ou entrega for necessaria, o CEO cria/delega task para o dono correto. O CEO so executa diretamente quando nao houver agente disponivel ou quando a task for explicitamente de governanca.
