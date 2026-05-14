---
name: setup-google-display-remarketing
description: Estrutura campanhas Google Display com função explícita no funil — targeting, exclusões anti-ICP, placements/apps bloqueados, brand safety, frequência e janela de remarketing, criativos por formato e métrica de leitura (playbook 16 §9 Display, §14). Não é “verba sobrando”. Use com plano de mídia e DEOC; após `setup-campanhas-google-ads`; antes do ar, `qa-go-live-google-ads` quando existir.
---

# Setup Google Ads — Display e remarketing

## Fonte canônica

Playbook **`16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md`**, subseção **“Estrutura Display”** em **§9**, **§10** (nomenclatura), **§12–13** (orçamento; remarketing só com público e objetivo), **§14** (go-live Display), coerente com **§1** (intenção e sinal). Legado: **`13-estrutura-campanhas-google-ads-display.md`**.

## Princípio (§9)

Display entra quando o **plano define função clara**: alcance qualificado, remarketing, contextual, sustentação de **awareness** ou recuperação de intenção. A estrutura declara **targeting**, **exclusões anti-ICP**, **placements/apps bloqueados**, **brand safety**, **frequência**, **janela de remarketing**, **criativos por formato** e **métrica de leitura**. **Sem** exclusões, frequência e brand safety há risco de **falso aprendizado** e tráfego de baixa qualidade. **Não** usar como sobra de verba nem “barato para aparecer”.

## Dependências

- **`setup-campanhas-google-ads`** — conta, conversões quando o Display objetiva lead, listas/remarketing, UTMs.
- **`gerador-taxonomia-utm-ids`**, **`contrato-dados-marketing-crm`**, **`qa-lp-ponto-conversao`** quando houver conversão no destino.

## Quando usar / quando não usar

| Usar | Não usar |
| --- | --- |
| Plano nomeia função Display (awareness / remarketing / contextual / recuperação) | “Barato para aparecer” sem hipótese no funil |
| Existe capacidade de governar exclusões, frequência e ambientes | Zero critério de brand safety ou exclusões |
| Remarketing: há **público** e mensagem coerente (§13 mínimo) | Lista vazia e expectativa de performance |

## Workflow

1. Documentar **função no funil** e **métrica de leitura** (não só impressões).
2. Por campanha: `campaign_id`, nomenclatura §10 (`display` no tipo_campanha quando usar a taxonomia), URL final e objetivo.
3. Por grupo (ad group): `adgroup_id`, **temperatura**/audiência, targeting resumido, exclusões do grupo.
4. Registrar **exclusões globais**: anti-ICP, **placements/apps bloqueados**, tópicos/URL excluídos conforme política.
5. Registrar **brand safety** (níveis, exclusões sensíveis, listas).
6. Definir **frequência** e, em remarketing, **janela** (ex.: visitantes 30D).
7. Mapear **criativos** (`creative_id`, formato, hipótese) alinhados ao pack/DEOC.
8. Preencher templates e gerar:

```bash
python3 scripts/build_google_display.py templates/estrutura-campanha-google-display.json --md ./display-remarketing.md
python3 scripts/build_google_display.py templates/estrutura-campanha-google-display.json --audit
```

9. Marcar `escopo.display: true` em `estrutura-campanha-google.json` e link para este artefato.

## Outputs

Blueprint Display: campanhas, grupos, targeting, exclusões, brand safety, frequência, janela, criativos, pré go-live §14.

## Artefatos

- `reference.md`
- `templates/estrutura-campanha-google-display.md`
- `templates/estrutura-campanha-google-display.json`
- `scripts/build_google_display.py`

## Definition of Done

Função e métrica de leitura definidas; targeting + exclusões + brand safety documentados; frequência e janela (se remarketing); criativos com IDs; checklist §14 para Display atendido no JSON; sem tratar Display como sobra de verba.
