# SABER — skills

**Versionamento:** ao alterar uma skill, siga o padrão imutável `v{X.Y.Z}.md` + `latest.md` + `CHANGELOG.md`, com **uma PR por skill** — ver **[`VERSIONAMENTO.md`](VERSIONAMENTO.md)** (alinhado ao exemplo `executar/shared/client-intake/` e a [`executar/_meta/versioning.md`](../../executar/_meta/versioning.md)).

Skills no padrão Paperclip: cada skill é uma pasta com **`SKILL.md`** (frontmatter YAML `name` + `description`). Em produção, `SKILL.md` deve permanecer **par** com `latest.md` após cada versão aprovada (detalhes em `VERSIONAMENTO.md`).

## Coordenação

| Pasta | Função |
|-------|--------|
| [`paperclip/`](paperclip/SKILL.md) | API Paperclip: heartbeats, checkout, comentários, approvals, rotinas. Inclui `references/`. |

## Transversais (secção 5 do planejamento)

| Pasta | Função |
|-------|--------|
| [`saber_bpmn_context/`](saber_bpmn_context/SKILL.md) | Resumo da etapa a partir do bundle BPMN |
| [`saber_context_pack_validate/`](saber_context_pack_validate/SKILL.md) | Validação do pacote mínimo do pedido |
| [`saber_run_artifact_version/`](saber_run_artifact_version/SKILL.md) | Versionamento de artefatos no issue |
| [`saber_gate_comment_templates/`](saber_gate_comment_templates/SKILL.md) | Modelos de comentário para gate B3 |

## MVP OPS recomendado (secção 2.1)

| Pasta | Função |
|-------|--------|
| [`saber_session_extract/`](saber_session_extract/SKILL.md) | Extrato pós-sessão a partir de transcrição/notas |
| [`saber_gc_client_pack/`](saber_gc_client_pack/SKILL.md) | Pacote cliente GC + análise de desvios (agregado) |

## GTM — funil comercial (secção 3; fora do quadro OPS)

`gtm_lead_brief`, `gtm_spiced_extract`, `gtm_call_quality_score`, `gtm_commercial_package`, `gtm_deck_roi_draft`, `gtm_post_call_sales`, `gtm_followup_sequence`, `gtm_contract_draft`, `gtm_contract_consistency_check`, `gtm_handoff_manifest`.

## OPS — pool Paperclip (secção 4)

- **GC:** `ops_gc_kit`, `ops_gc_deviation_analysis`, `ops_dmd_reminders`
- **KO:** `ops_project_scaffold`, `ops_kickoff_prep`, `ops_post_kickoff_extract`, `ops_backlog_merge_suggest`
- **CX:** `ops_context_compiler`, `ops_context_diff`, `ops_canonical_publish`
- **BM:** `ops_research_grid`, `ops_benchmark_draft`, `ops_claim_coverage_check`, `ops_benchmark_refine`
- **DG:** `ops_pop_evidence_run`, `ops_diag_package_v1`, `ops_csat_trigger`
- **PS:** `ops_solution_hypotheses`, `ops_implementation_design`, `ops_pricing_package`, `ops_client_proposal_deck`
- **N:** `ops_contract_generate`, `ops_esign_monitor`
- **H2:** `ops_compile_handoff_executar`, `ops_notebooklm_handoff`

## Manutenção em lote

O script [`_generate_domain_skills.mjs`](_generate_domain_skills.mjs) regenera as skills de **domínio** (não altera `paperclip/`). `node _generate_domain_skills.mjs` a partir desta pasta.

## Referências

- Planejamento: `V4OS Colli&Co/Plans/Execution/saber-tobe-bpmn-app/Paperclip-planejamento-skills.md`
- Dados da jornada: `V4OS Colli&Co/src/data/saber-bpmn.bundle.json`
- Upstream Paperclip: [paperclipai/paperclip](https://github.com/paperclipai/paperclip)
