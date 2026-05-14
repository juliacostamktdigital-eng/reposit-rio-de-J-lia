# Agentes Canonicos
**Status:** v1
**Atualizado:** 2026-04-25
**Fonte:** agente:codex

---

## Fonte oficial

Este diretorio guarda os prompts autorais ativos da iniciativa Agentizacao Saber.

Edite estes arquivos quando quiser iterar o comportamento dos Agentes. Depois, sincronize o conteudo para a instancia Paperclip por UI, API ou script operacional.

## Prompts ativos

| Agente | Arquivo | Status |
|---|---|---|
| Bibliotecario projetos | `bibliotecario-projetos/AGENTS.md` | canonico-v0 |
| CEO | `ceo/AGENTS.md` | canonico-v1 com roteamento para Redacao e Editor |
| Briefador | `briefador/AGENTS.md` | canonico-v1 com handoff para Redacao e Editor |
| Inteligencia Brain | `inteligencia-brain/AGENTS.md` | canonico-v1 com `outputType: inteligencia` e `outputType: plano-roi` |
| Redacao e Voz do Cliente | `redacao-voz-cliente/AGENTS.md` | canonico-v1 |
| Editor de Entregaveis | `editor-entregaveis/AGENTS.md` | canonico-v1 |
| Analista de Mercado e Benchmark | `analista-mercado-benchmark/AGENTS.md` | canonico-v0 |
| Estrategista de Posicionamento | `estrategista-posicionamento/AGENTS.md` | canonico-v0 |
| Gestor de Trafego e Midia Paga | `gestor-trafego-midia-paga/AGENTS.md` | canonico-v0 |
| Diretor Criativo e Presenca Digital | `diretor-criativo-presenca/AGENTS.md` | canonico-v0 |
| Analista CRO e Landing Page | `analista-cro-lp/AGENTS.md` | canonico-v0 |
| Especialista GTM e Comercial | `especialista-gtm-comercial/AGENTS.md` | canonico-v0 |

## Skills por agente

Cada agente canonico passa a manter copia local de skills neste formato:

- `skills/README.md` -> contrato do agente no Paperclip
- `skills/ativas/<skill-slug>/SKILL.md` -> copia local de skills ativas
- `skills/ativas/<skill-slug>/META.md` -> origem, owner e status da skill local
- `skills/incubacao/<skill-slug>/...` -> skills candidatas em teste
- `skills/CHECKLIST-PROMOCAO-PARA-GLOBAL.md` -> gate de promocao para `empresa/skills/`

Regra de fonte de verdade:

- Durante incubacao local: fonte primaria no agente canonico.
- Depois de promover: fonte primaria no catalogo global `empresa/skills/`.
