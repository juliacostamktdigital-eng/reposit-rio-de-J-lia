# SABER — meta (planejamento)

Notas de contexto para quem for criar agents e skills neste processo. **Não** duplica o documento de planejamento completo no repositório corporativo; serve como âncora local.

## Premissas (resumo)

- Paperclip orquestra sobretudo o **pool OPS SABER** (aprox. GC.01 → H2.07). Vendas (Q/P/C) e **Handoff h1** podem usar jobs/skills **fora** do quadro Paperclip.
- Skills em dois níveis: **coordenação** (API Paperclip, checkout, comentários, approvals) vs **domínio** (artefatos da jornada, MCPs, templates).
- **`bpmns`** (Markdown/JSON canônico) = contexto estável para o orquestrador por etapa.

## Dúvidas abertas (D1–D7) — afetam nomes, MCPs e critérios de aceite

| ID | Tema |
|----|------|
| D1 | Repositório canônico de skills / como resolver `e-show` por run |
| D2 | Template/schema do benchmark (BM) — `schema_version`; flag `schema_missing` |
| D3 | Manual de soluções + precificação (Service Cart / API) — gate `content_risk` |
| D4 | Integrações (Ekyte, Drive, Forms, e-sign, NotebookLM): MCP vs manual no MVP |
| D5 | Handoff Flow/HOPS ↔ Paperclip: webhook vs criação manual (`issue_bootstrap`) |
| D6 | Gates duplos (PS.08, N.05): regra fixa ou por produto/ticket |
| D7 | Telemetria e PII no payload do run — retention, hashing de `lead_id` |

## Tipos de passo (matriz A/S/H/M)

| Tipo | Padrão |
|------|--------|
| **A** | Domínio ou automação determinística; run com auditoria |
| **S** | Rascunho; gate humano no Paperclip |
| **H** | Sem skill de execução; checklist/comentário |
| **M** | Manual; skill opcional só como assistente |

## Ordem sugerida pós-MVP (piloto)

Ver documento de planejamento: após MVP (`paperclip` + 1–2 skills Saber), expandir com `saber_bpmn_context`, `saber_context_pack_validate`, depois fatias GC/KO, contexto, benchmark, diagnóstico, proposta, negociação, handoff Executar.

## Estrutura de skills

Catálogo em [`../skills/`](../skills/README.md): **`SKILL.md`** por pasta (estilo [Paperclip](https://github.com/paperclipai/paperclip/tree/master/skills)), mais `paperclip/references/`. Decisão D1 continua a definir registry canónico e `e-show` por run.
