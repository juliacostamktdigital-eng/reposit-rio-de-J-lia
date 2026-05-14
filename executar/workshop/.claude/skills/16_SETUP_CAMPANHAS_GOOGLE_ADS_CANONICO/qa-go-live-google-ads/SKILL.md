---
name: qa-go-live-google-ads
description: Valida go/no-go antes de ativar verba em Google Ads com base no playbook 16 — princípio (intenção, conversão, sinal), conta/tag/GA4, conversões, GTM e v4_*, nomenclatura, negativas, orçamento, checklist pré go-live (§14), critério N2 (§15), subtipos Search/PMax/Display e anti-padrões (§17). Entrada típica — campanhas em rascunho, artefatos de setup, URLs e planilha growth. Saída — relatório Markdown, gaps bloqueadores e recomendação revisada por humano.
---

# QA go-live — Google Ads

## Fonte canônica

Playbook **`16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md`**, em especial **§1** (princípio), **§§4–6** (conta, conversões, GTM/parâmetros), **§§10–12** (nomenclatura, negativas, orçamento), **§14** (checklist antes do go-live), **§15** (N2), **§17** (anti-padrões). **§§7–9** entram via subtipos e itens condicionais do checklist §14.

## Princípio

Este QA é **validação**, não criação de campanha. A decisão final é **humana**; o script resume gaps e anti-padrões para evitar ativar verba sem conversão testada, sem backup/CRM e sem controle mínimo de Search/PMax/Display.

## Quando usar

- Imediatamente antes de sair de rascunho / ativar orçamento.
- Após mudanças relevantes em conversões, GTM, URLs, negativas, assets, audience signals ou estrutura.

## Dependências (artefatos esperados)

- **`setup-campanhas-google-ads`** — template principal preenchido; `build_setup_google.py --audit` sem bloqueadores críticos quando usado.
- **`setup-google-search-leadgen`**, **`setup-google-pmax-leadgen`**, **`setup-google-display-remarketing`** — quando o subtipo for usado, marcar subtipo aplicável e confirmar checklist da subskill.
- **`gerador-taxonomia-utm-ids`**, **`contrato-dados-marketing-crm`**, **`qa-lp-ponto-conversao`**, planilha growth/backup, plano de mídia, DEOC.

## Workflow

1. Reunir evidências (conversão testada, lead teste no backup, URLs finais, IDs nos nomes, política de negativas).
2. Preencher **`templates/checklist-go-live-google.md`** ou o **JSON** com `ok` / `gap` / `n.a.` por item (`n.a.` só quando não se aplica ao escopo em revisão — ex.: sem Search → itens Search em `n.a.`).
3. Marcar **anti-padrões** da **§17** como detectados ou não.
4. Ajustar **subtipos** (`search`, `pmax`, `display`): se `aplicavel: true`, exige `checklist_subskill_ok: true`.
5. Gerar relatório:

```bash
python3 scripts/evaluate_qa_go_live_google.py --write-default templates/checklist-go-live-google.json
python3 scripts/evaluate_qa_go_live_google.py templates/checklist-go-live-google.json --md ./relatorio-qa-go-live-google.md
python3 scripts/evaluate_qa_go_live_google.py templates/checklist-go-live-google.json --summary
```

6. **Não** aprovar go-live com item **§14** ou **§15** aplicável em `gap`, nem anti-padrão **§17** detectado sem plano documentado.

## Outputs

- Relatório Markdown com contagem por grupo, gaps, anti-padrões acionados veredito sugerido (`pronto` / `nao_pronto` / `incompleto`).
- Campos livres para `gaps_bloqueadores_livre` e `acoes_corretivas` no JSON.

## Artefatos

- `reference.md` — mapa item ↔ seção do canônico.
- `templates/checklist-go-live-google.md`
- `templates/checklist-go-live-google.json`
- `scripts/evaluate_qa_go_live_google.py`

## Definition of Done (processo de QA)

Itens aplicáveis da **§14** e **§15** com `ok`; subtipos coerentes (subskill com `checklist_subskill_ok` quando `aplicavel`); nenhum anti-padrão **§17** detectado sem mitigação; `decisao_humana` preenchida em `meta`.
