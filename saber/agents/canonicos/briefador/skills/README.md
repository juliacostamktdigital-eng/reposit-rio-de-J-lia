# Skills - Briefador
**Status:** v2
**Atualizado:** 2026-04-27
**Fonte:** agente:codex

---

## Como o Paperclip entrega skills

As skills sao ativadas na aba **Skills** do agente no Paperclip e vinculadas ao `CODEX_HOME/skills/` no proximo run.

O Briefador usa skills apenas para melhorar o brief. Ele nao executa diagnostico, copy ou entrega final.

## Estrutura local por agente

- `skills/ativas/` guarda copias locais das skills ativas deste agente.
- `skills/incubacao/` guarda skills candidatas em teste ou adaptacao.
- Cada skill local deve conter `SKILL.md` e `META.md`.
- Promocao para catalogo global segue `skills/CHECKLIST-PROMOCAO-PARA-GLOBAL.md`.
- O catalogo global publicado continua em `empresa/skills/`.

## Skills esperadas no Paperclip

| Skill | Obrigatoria? | Fonte canonica | Quando usar |
|---|---|---|---|
| `paperclip` | Sim | Paperclip company library | Ler issue, documentos e atualizar brief |
| `delivery-format-briefing` | Sim | local | Definir tipo de entrega, formato/aspect ratio, artefato principal, exports e assets antes do handoff |
| `sabatina-prd` | Opcional | `empresa/skills/gerais/sabatina-prd/SKILL.md` | Checar clareza, escopo e criterio de aceite quando a task estiver ambigua |
| `saber_context_pack_validate` | Candidata | `empresa/skills/saber/skills/legacy/paperclip_genericas/saber_context_pack_validate/SKILL.md` | Validar se o pacote de contexto esta suficiente antes de execucao |
| `ops_context_compiler` | Candidata | `empresa/skills/saber/skills/legacy/paperclip_genericas/ops_context_compiler/SKILL.md` | Compilar contexto quando a issue trouxer multiplas fontes |

## Skills que o Briefador nao deve usar como executor

| Skill | Encaminhar para |
|---|---|
| `diagnostico-copy-lp` | `redacao-voz-cliente` |
| `deck-semana-estruturacao` | `editor-entregaveis` |
| `deck-entrega-final` | `editor-entregaveis` |
| `v4-html-slide-builder` | `editor-entregaveis` |
| `openai-image-asset-generator` | `editor-entregaveis` |
| Qualquer diagnostico de Mercado/Midia/Vendas | Especialista de dominio |

## Regra

O output do Briefador e um documento `brief`. Se a skill sugerir uma entrega final, registre como recomendacao de proximo agente, nao como execucao.
