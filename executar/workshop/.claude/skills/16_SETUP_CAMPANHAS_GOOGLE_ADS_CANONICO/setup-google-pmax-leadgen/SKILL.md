---
name: setup-google-pmax-leadgen
description: Estrutura Performance Max para leadgen com conversão validada — pré-requisitos do playbook 16, 2–5 asset groups, assets (texto/imagem/vídeo), audience signals sem sobrecarga, guardrails (URL expansion, brand controls, metas de conversão) e checklist go-live PMax. Conservadora no início; não substitui Search quando falta sinal ou assets. Use após `setup-campanhas-google-ads` e alinhamento DEOC; antes do ar, `qa-go-live-google-ads` quando existir.
---

# Setup Google Ads — Performance Max (leadgen)

## Fonte canônica

Playbook **`16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md`**, **Seções 8–9** (PMax e assets), **10** (nomenclatura, exemplo PMax), **12** (orçamento; oscilação PMax), **13** (PMax só se maduro), **14** (go-live PMax), **17** (evitar PMax sem asset ou sem signal). Legado: **`12-estrutura-campanhas-google-ads-pmax.md`**.

## Princípio

PMax **expande** além de Search quando há **conversão confiável**, **assets suficientes**, **sinais de audiência** e **verba para aprendizado**. Sinais orientam o algoritmo — não são targeting fixo. **Não sobrecarregar** sinais: priorizar os mais fortes (Seção 8).

## Dependências

- **`setup-campanhas-google-ads`** — conta, conversões, GTM/`v4_*`, backup.
- **`gerador-taxonomia-utm-ids`**, **`contrato-dados-marketing-crm`**, **`qa-lp-ponto-conversao`**.
- Opcional forte: **`setup-google-search-leadgen`** quando Search já alimenta intenção e dados.

## Quando usar / quando não usar (Seção 8)

| Usar | Não usar (ou adiar) |
| --- | --- |
| Conversão bem configurada e validada | Conversão ou LP instáveis |
| Assets minimamente decentes e briefing/DEOC | Sem asset utilizável |
| Lista/sinal de audiência relevante | Sem sinal mínimo na conta |
| Budget para aprendizado + objetivo de expansão | Budget muito baixo |
| | Necessidade de **controle granular imediato** só por PMax |

## Workflow

1. Preencher **gate de pré-requisitos** (Seção 8 — “quando usar” vs “quando evitar”). Se algum gate falhar, só prossiga com **`excecao_risco_aceita`** e **`excecao_nota`** explícita — o canônico desaconselha.
2. Definir **uma campanha PMax aquisição** (ou mais se o plano exigir) com `campaign_id` e nomenclatura §10.
3. Montar **2 a 5 asset groups** (§8): oferta principal; persona/segmento; dor/caso de uso — evitar excesso no início.
4. Por asset group, mapear **assets §9**: headlines curtas/longas, descrições, imagens (quadrada/horizontal/vertical quando possível), logo; **vídeo próprio** preferencial (evitar só auto-gerado).
5. Definir **audience signals** (§8): Customer Match, visitantes, leads/MQL, termos alta intenção, URLs referência, in-market, GA4 — poucos e fortes.
6. Documentar **guardrails**: URL expansion, brand controls, metas de conversão, lance (legado 12 + §12 canônico).
7. Preencher template MD/JSON e gerar:

```bash
python3 scripts/build_google_pmax.py templates/estrutura-campanha-google-pmax.json --md ./pmax-leadgen.md
python3 scripts/build_google_pmax.py templates/estrutura-campanha-google-pmax.json --audit
```

8. Atualizar **`estrutura-campanha-google.json`** com `escopo.pmax: true` e link para este artefato.

## Outputs

- Blueprint PMax: asset groups, inventário de assets, sinais, guardrails e checklist §14 específico.

## Artefatos

- `reference.md`
- `templates/estrutura-campanha-google-pmax.md`
- `templates/estrutura-campanha-google-pmax.json`
- `scripts/build_google_pmax.py`

## Definition of Done

Pré-requisitos explícitos; 2+ asset groups coerentes; assets mínimos por grupo; ≥1 audience signal documentado; URL expansion e brand controls registrados; lead/conversão testável com rastreio; hipótese e leitura na planilha growth; sem violar §17 (PMax sem asset ou sem signal).
