---
name: qa-go-live-meta-ads
description: Valida go/no-go antes de ativar verba em Meta Ads com base no playbook 15 — conta, pixel/eventos, públicos e temperatura, IDs e taxonomia, UTMs e v4_*, criativos, orçamento, checklist pré go-live, subtipos (lead nativo, conversão site, engajamento) e anti-padrões. Entrada típica — campanhas em rascunho, artefatos de setup, URLs e planilha growth. Saída — relatório Markdown, gaps bloqueadores e recomendação revisada por humano.
---

# QA go-live — Meta Ads

## Fonte canônica

Playbook **`15_SETUP_CAMPANHAS_META_ADS_CANONICO.md`**, em especial seções **1** (perguntas que a conta precisa responder), **3** (inputs), **4** (conta), **5** (eventos), **6–8** (públicos e estrutura — referência para checagens de temperatura/exclusões), **10–12** (nomenclatura, criativos, orçamento), **13** (checklist antes do go-live), **14** (N2), **16** (anti-padrões).

## Princípio

Este QA é **validação**, não criação de campanha. A decisão final é sempre **humana**; o script resume gaps e anti-padrões para evitar ativar verba sem aprendizado confiável (Seção 1).

## Quando usar

- Imediatamente antes de sair de rascunho / ativar orçamento em campanhas Meta.
- Após alterações relevantes em pixel, evento de otimização, URLs, públicos ou estrutura.

## Dependências (artefatos esperados)

- **`setup-campanhas-meta-ads`** — `estrutura-campanha-meta` preenchido e, se aplicável, script `--audit` sem bloqueadores críticos.
- **`setup-meta-lead-nativo`**, **`setup-meta-conversao-site`** — checklists específicos quando o subtipo for usado (Seção 14).
- **`gerador-taxonomia-utm-ids`**, **`contrato-dados-marketing-crm`**, planilha growth/backup, plano de mídia, DEOC.

## Workflow

1. Reunir evidências (prints, IDs, URL com UTMs, teste de evento, lead de teste).
2. Preencher **`templates/checklist-go-live-meta.md`** ou o **JSON** com `ok` / `gap` / `n.a.` por item (`n.a.` só quando o item não se aplica ao conjunto de campanhas em revisão).
3. Marcar **anti-padrões** da Seção 16 como detectados ou não.
4. Ajustar **subtipos** (`lead_nativo_aplicavel`, `conversao_site_aplicavel`, `engajamento_aplicavel`) e confirmar se o checklist da subskill correspondente foi atendido.
5. Gerar relatório:

```bash
python3 scripts/evaluate_qa_go_live_meta.py --write-default templates/checklist-go-live-meta.json
python3 scripts/evaluate_qa_go_live_meta.py templates/checklist-go-live-meta.json --md ./relatorio-qa-go-live-meta.md
python3 scripts/evaluate_qa_go_live_meta.py templates/checklist-go-live-meta.json --summary
```

6. **Não** aprovar go-live com item Seção 13 em `gap` ou anti-padrão detectado sem plano de correção documentado.

## Outputs

- Relatório Markdown com contagem por grupo, lista de gaps, anti-padrões acionados e sugestão automática (`pronto` / `nao_pronto` / `incompleto`).
- Campos livres para `gaps_bloqueadores` e `acoes_corretivas` no JSON.

## Artefatos

- `reference.md` — mapa item ↔ seção do canônico.
- `templates/checklist-go-live-meta.md`
- `templates/checklist-go-live-meta.json`
- `scripts/evaluate_qa_go_live_meta.py`

## Definition of Done (para o processo de QA)

Todos os itens aplicáveis da Seção 13 com `ok`; complementos N2 relevantes (`v4_*`, públicos padrão, subtipos) atendidos; nenhum anti-padrão da Seção 16 marcado como detectado sem mitigação; revisão humana registrada em `meta`.
