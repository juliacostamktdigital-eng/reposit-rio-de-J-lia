---
name: setup-campanhas-google-ads
description: Prepara conta Google Ads, GTM/tag/GA4, conversões, UTMs e v4_*, estrutura Search/PMax/Display, negativas, nomenclatura e checklist pré go-live conforme playbook 16. Use após DEOC, plano de mídia, LP e taxonomia; antes de ativar verba. Conservadora com PMax no início — exige conversão validada e backup. Subskills Search, PMax e Display complementam o detalhe operacional; `qa-go-live-google-ads` valida go/no-go antes do ar.
---

# Setup de campanhas Google Ads

## Fonte canônica

Playbook **`16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md`** (consolida Search, PMax e Display).

## Princípio (Seção 1)

Google Ads depende de **intenção**, **conversão** e **qualidade de sinal**. Setup não é execução: antes da mídia, a operação precisa garantir conta/faturamento, tag/GA4/GTM, conversões, públicos/listas, estrutura sem fragmentação excessiva, alinhamento termos/URLs/assets à oferta, UTMs/IDs e backup + CRM.

## Dependências recomendadas (inventário)

- **`gerador-taxonomia-utm-ids`** — `campaign_id`, `adgroup_id`, `creative_id`, UTMs e parâmetros `v4_*`.
- **`contrato-dados-marketing-crm`** — campos hidden, planilha backup, conciliação.
- **`qa-lp-ponto-conversao`** — LP e formulário com submissão testada (Seção 6: não publicar sem lead teste).

## Inputs obrigatórios (Seção 3)

DEOC; plano de mídia; LP; contrato de dados; taxonomia; planilha backup; CRM/SLA; keywords/temas de busca; negativas iniciais; assets (texto/imagem/vídeo) quando PMax/YouTube/Display; acessos Google Ads, GA4, GTM, Search Console quando aplicável.

## PMax (posicionamento do canônico)

Seção 8: **evitar PMax no início** se conversão não validada, LP sem preservação de dados, assets insuficientes, budget baixo demais, necessidade de controle granular imediato ou ausência de sinais mínimos. Skill principal registra decisão; detalhe operacional: **`setup-google-pmax-leadgen`**.

## Workflow

1. Preencha **checklist de conta** (Seção 4) no template MD ou JSON.
2. Defina **conversões** e regra de profundidade vs volume (Seção 5).
3. Valide **GTM e parâmetros** (Seção 6): `gclid`, `gbraid`/`wbraid` quando aplicável, UTMs, `v4_*`, hidden fields, backup, CRM.
4. Documente **Search** (Seção 7), **PMax** (Seções 8–9) e/ou **Display** (Seção 9) conforme o plano — sem misturar marca e não-marca na mesma leitura.
5. Prepare **negativas** iniciais e cadência de revisão (Seção 11).
6. Aplique **nomenclatura** (Seção 10).
7. Defina **orçamento e aprendizado** (Seção 12); evitar mudanças diárias sem evidência.
8. Escolha **estrutura inicial** mínima ou madura (Seção 13).
9. Preencha **pré go-live** (Seção 14) e critérios **N2** (Seção 15).
10. Gere consolidado:

```bash
python3 scripts/build_setup_google.py templates/estrutura-campanha-google.json --md ./setup-google.md
python3 scripts/build_setup_google.py templates/estrutura-campanha-google.json --audit
```

11. Para **Search**: `setup-google-search-leadgen`. Para **PMax**: `setup-google-pmax-leadgen` (`build_google_pmax.py`). Para **Display/remarketing**: `setup-google-display-remarketing` (`build_google_display.py`). Antes do ar: **`qa-go-live-google-ads`** (`evaluate_qa_go_live_google.py`).

## Outputs

- Estrutura documentada (Search/PMax/Display aplicáveis), conversões, UTMs/IDs, negativas, hipóteses e evidência de lead teste (backup/CRM).

## Artefatos

- `reference.md` — resumo fiel ao canônico (seções 1–17).
- `templates/estrutura-campanha-google.md`
- `templates/estrutura-campanha-google.json`
- `scripts/build_setup_google.py`

## Definition of Done (N2 — Seção 15)

Conta e faturamento prontos; GTM/tag/conversões funcionando; UTMs e IDs aplicados; estrutura Search/PMax/Display documentada conforme escopo; públicos/listas/sinais configurados; planilha backup com lead teste; hipótese e critério de leitura registrados.
