# Referência — QA go-live Google Ads ↔ playbook 16

Canônico: `16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md`.

## Mapa por grupo de checklist

| Grupo no JSON | Seções do playbook | Conteúdo |
|---------------|---------------------|----------|
| `principio` | §1 | Intenção, conversão, qualidade de sinal; base de conta/tag; fragmentação; URLs/assets; UTMs/backup; hipótese e leitura. |
| `conta` | §4 | Conta, faturamento, permissões, auto-tagging, GA4, GTM/tag, remarketing, Customer Match, enhanced conversions. |
| `conversoes` | §5 | Profundidade vs volume, secundárias, importação offline planejada. |
| `gtm_dados` | §6 | gclid, gbraid/wbraid, UTMs, v4_*, hidden, backup, CRM, lead teste obrigatório. |
| `nomenclatura` | §10 | campaign_id, adgroup_id, creative_id nos nomes. |
| `negativas` | §11 | Lista inicial, cadência de revisão. |
| `orcamento` | §12 | Aprendizado, evitar mudança diária sem evidência, lance/objetivo documentado. |
| `go_live` | §14 | Lista explícita pré ar (conversões, enhanced, UTMs, backup, CRM, Search/PMax/Display condicional, URLs, orçamento/datas, hipótese, change log). |
| `n2` | §15 | DoD N2 operacional (pode sobrepor tematicamente §14 — ambos devem fechar antes do parecer). |
| `anti_padroes` | §17 | Detectado = sinal vermelho no veredito até haver mitigação documentada. |

## Subtipos (`subtipos` no JSON)

| Chave | Alinhamento | Quando `aplicavel: true` |
|-------|-------------|---------------------------|
| `search` | §7 | Há campanhas Search no go-live. |
| `pmax` | §§8–9 | Há PMax no go-live. |
| `display` | §9 (Display) | Há Display/remarketing no go-live. |

Se `aplicavel: true` e `checklist_subskill_ok: false`, o veredito é **não pronto** (bloqueio de subskill).

## Status no JSON

- `ok` — atendido.
- `gap` — não atendido / bloqueador.
- `n.a.` — fora do escopo do conjunto em revisão (ex.: sem PMax → itens PMax específicos em §14 podem ser `n.a.`).

Aliases aceitos pelo script: `sim`, `s`, `não`, `nao`, `fail`, `falha` (normalizados para `ok` / `gap` / `na`).
