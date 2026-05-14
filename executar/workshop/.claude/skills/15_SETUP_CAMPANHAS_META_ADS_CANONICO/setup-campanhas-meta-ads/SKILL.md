---
name: setup-campanhas-meta-ads
description: Prepara conta Meta Ads, pixel/CAPI, públicos por temperatura, estrutura campanha/conjunto/anúncio, nomenclatura alinhada à taxonomia, UTMs, hipóteses e checklist pré go-live conforme playbook 15. Use após DEOC, plano de mídia, LP, contrato de dados e taxonomia; antes de ativar verba. Subtipos lead nativo, conversão site e engajamento exigem checklists complementares quando aplicáveis.
---

# Setup de campanhas Meta Ads

## Fonte canônica

Playbook **`15_SETUP_CAMPANHAS_META_ADS_CANONICO.md`** (consolida estrutura Meta, lead nativo, conversão e engajamento).

## Princípio (Seção 1)

Setup **não é execução** — é preparação para aprendizado confiável. Antes do ar, a conta precisa responder às perguntas do canônico (conta, pixel, públicos, IDs, estrutura de teste, hipótese, leitura, backup, contrato de dados).

## Dependências recomendadas (inventário)

Antes de go-live, alinhar com:

- **`gerador-taxonomia-utm-ids`** — padrão `campaign_id`, `adgroup_id`, `creative_id` e UTMs.
- **`contrato-dados-marketing-crm`** — origem do lead, campos, backup.
- **`qa-lp-ponto-conversao`** — LP/formulário consistente com promessa e conversão.
- **`setup-meta-lead-nativo`**, **`setup-meta-conversao-site`** e **`setup-meta-engajamento-remarketing`** — checklists complementares por subtipo quando o plano usar formulário nativo, conversão no site ou aquecimento/remarketing.

## Inputs obrigatórios (Seção 3)

DEOC; plano de mídia; LP/ponto de conversão; contrato de dados; taxonomia UTM/IDs; criativos (aprovados ou fila final); planilha backup; planilha de testes growth; CRM/SLA; matriz de testes (o que varia / constante); definição de lead correto e follow-up por tipo; acessos BM, conta de anúncios, pixel, página, Instagram, domínio.

## Workflow

1. Preencha **checklist de conta** (Seção 4) em `templates/estrutura-campanha-meta.md` ou no JSON.
2. Valide **eventos e pixel** (Seção 5): profundidade de otimização vs volume.
3. Defina **públicos** frios/mornos/quentes e **exclusões** (Seções 6–7).
4. Monte **estrutura inicial** (Seção 8) respeitando temperatura e orçamento.
5. Escolha **tipo de campanha** por objetivo (Seção 9): construção de público, captação de leads (nativo/LP/WhatsApp), conversão, engajamento.
6. Aplique **nomenclatura** da taxonomia (Seção 10).
7. Planeje **3–5 criativos** por conjunto com `creative_id` e hipótese (Seção 11).
8. Defina **orçamento** CBO vs ABO e regras de aprendizado (Seção 12).
9. Preencha **checklist pré go-live** (Seção 13) e critérios **N2** (Seção 14).
10. Gere documento consolidado: `python3 scripts/build_setup_meta.py templates/estrutura-campanha-meta.json --md ./setup-meta.md`
11. Subtipos: `setup-meta-lead-nativo`, `setup-meta-conversao-site` e `setup-meta-engajamento-remarketing` quando aplicável. Antes de ativar verba, rode **`qa-go-live-meta-ads`** (`scripts/evaluate_qa_go_live_meta.py` + `checklist-go-live-meta.json`).

## Reforço operacional por subtipo

- **Lead nativo:** formulario, perguntas de qualificacao, SLA, integracao CRM/backup e qualidade comercial antes de ativar.
- **Conversao no site:** LP, evento, pixel/CAPI, UTMs e volume precisam estar confiaveis antes de otimizar.
- **Engajamento/remarketing:** usar apenas com funcao clara no funil, regra de criacao/uso do publico aquecido, janelas, exclusoes e campanha seguinte definida.

## Outputs

- Estrutura de campanhas/conjuntos/anúncios com IDs e nomes.
- Registro de públicos, exclusões, hipóteses e matriz de testes.
- Evidência de testes de pixel, backup, CRM e checklists por subtipo conforme N2.

## Artefatos

- `reference.md` — resumo fiel ao canônico (seções 1–16).
- `templates/estrutura-campanha-meta.md`
- `templates/estrutura-campanha-meta.json`
- `scripts/build_setup_meta.py`

## Scripts

```bash
python3 scripts/build_setup_meta.py templates/estrutura-campanha-meta.json --md ./setup-meta-saida.md
python3 scripts/build_setup_meta.py templates/estrutura-campanha-meta.json --audit
```

## Definition of Done (N2 — Seção 14)

Conta, pixel e eventos configurados; públicos padrão criados; estrutura coerente com objetivo e temperatura; IDs e nomes corretos; UTMs e campos de versão aplicados; planilha backup com lead teste; hipótese e leitura registradas; subtipos com checklist específico quando usados (lead nativo, conversão site, engajamento/remarketing); checklist pré go-live preenchido.
