# SABER — skills e agents (processo separado)

Este diretório guarda **apenas** o processo **SABER** (jornada To Be × Paperclip): agents, skills e organograma **não** seguem o modelo de `executar/agents/` (processo **Executar**).

## O que vai aqui

| Pasta | Conteúdo |
|-------|----------|
| `saber/agents/` | Definições de agentes específicos do SABER (organograma próprio) |
| `saber/skills/` | Skills de **coordenação** (ex.: integração Paperclip) e de **domínio** SABER (OPS, GC, KO, …) |
| `saber/_meta/` | Notas de planejamento, premissas e referências (não substitui o catálogo evolutivo no doc de produto) |

## Relação com o resto do repo

- **`../executar/agents/`** e **`../executar/shared/`** = processo **Executar** (assessoria mkt/vendas; hierarquia em `../executar/_meta/agents.md`).
- **`saber/`** = processo operacional SABER orquestrado no **Paperclip** (pool OPS), com gates, runs e artefatos próprios.

## MVP (recorte)

Validação mínima descrita no planejamento: skill `paperclip` + **1 ou 2** skills de domínio OPS (`saber_session_extract`, `saber_gc_client_pack`) + templates de issue humanos. Em `skills/` existe ainda o **catálogo evolutivo** completo (GTM + OPS por fase + transversais), conforme o documento de planejamento — ativar no agente só o subconjunto do piloto.

## Referências

- **Versionamento de skills nesta pasta:** [`saber/skills/VERSIONAMENTO.md`](skills/VERSIONAMENTO.md) — padrão `v*.*.*.md` + `latest.md`, PR obrigatória por skill (referência Executar: `executar/_meta/versioning.md`, exemplo `executar/shared/client-intake/`).
- Paperclip: [paperclipai/paperclip](https://github.com/paperclipai/paperclip) — control plane, `skills/paperclip/SKILL.md`.
- Detalhes de dúvidas abertas (D1–D7), tipos A/S/H/M e ordem de construção: ver `saber/_meta/README.md`.
