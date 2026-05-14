---
name: setup-google-search-leadgen
description: Estrutura campanhas Google Search para leadgen por demanda ativa — taxonomia não-marca/marca/concorrentes, clusters de grupos (problema, solução, comparativo, persona), keywords com match types, negativas desde o dia 1, RSAs e URLs com UTMs, alinhado ao playbook 16 (Seção 7) e legado 11. Use após setup base `setup-campanhas-google-ads` ou em paralelo à documentação de conta/conversões; antes do go-live use `qa-go-live-google-ads` quando existir.
---

# Setup Google Ads — Search (leadgen / demanda ativa)

## Fonte canônica

Playbook **`16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md`**, **Seção 7** (estrutura Search), com apoio das Seções **5–6** (conversões, GTM/`v4_*`), **10** (nomenclatura), **11** (negativas), **12** (orçamento), **13** (mínimo leadgen), **14** (go-live Search), **17** (evitar Search sem negativas; marca vs não-marca). Legado: **`assets/legacy/merge/skills/11-estrutura-campanhas-google-ads-search.md`**.

## Princípio

Search captura **intenção explícita**. A estrutura deve separar **leitura** entre não-marca, marca e concorrentes; clusterizar ad groups por tema; usar **frase/exata** no início; **negativas desde o dia 1**; e manter anúncio → LP → conversão rastreável.

## Dependências

- **`setup-campanhas-google-ads`** — conta, conversões, GTM, escopo geral.
- **`gerador-taxonomia-utm-ids`**, **`contrato-dados-marketing-crm`**, **`qa-lp-ponto-conversao`**.

## Quando usar / quando não usar

| Usar | Não usar |
| --- | --- |
| Há demanda de busca configurável (problema, solução, categoria, marca, concorrente se permitido) | Objetivo é só “testar Google” sem lista de intenção nem LP |
| Plano de mídia e DEOC definem oferta, claims e destino | Substituir DEOC ou definir ICP do zero só nesta skill |

## Workflow

1. Confirmar **“quando usar Search”** (Seção 7): tipo de demanda ativa que justifica o canal.
2. Definir **campanhas por intenção**: não-marca (grupos 00–03), marca separada, concorrentes só se permitido/estratégico com **copy e compliance** anotados.
3. **Clusterizar ad groups** por intenção; evitar misturar intenções opostas no mesmo grupo.
4. Montar **keywords**: alta intenção; **frase/exata** inicialmente; ampla só com conversão e negativas maduras (documentar estágio).
5. Montar **lista inicial de negativas** (Seção 11) e **cadência** de revisão de termos de busca (primeira semana + cadência semanal inicial).
6. Definir **RSAs** (headlines/descrições/paths) alinhados ao DEOC; conferir mínimos e coerência com URL final.
7. Registrar **orçamento/lances** (Seção 12) e hipótese na planilha growth.
8. Preencher `templates/estrutura-campanha-google-search.md` ou o JSON e gerar:

```bash
python3 scripts/build_google_search.py templates/estrutura-campanha-google-search.json --md ./search-leadgen.md
python3 scripts/build_google_search.py templates/estrutura-campanha-google-search.json --audit
```

9. Marcar no JSON mestre `estrutura-campanha-google.json` o escopo **Search** e link para este artefato, se aplicável.

## Outputs

- Blueprint Search: campanhas, grupos, keywords, negativas, RSAs, URLs, leitura marca/não-marca e checklist específico pré go-live.

## Artefatos

- `reference.md`
- `templates/estrutura-campanha-google-search.md`
- `templates/estrutura-campanha-google-search.json`
- `scripts/build_google_search.py`

## Definition of Done

Campanhas por intenção definidas; grupos clusterizados; keywords + match policy documentados; negativas iniciais + rotina de search terms; RSAs com guardrails; URL final e rastreio coerentes com Seções 6 e 14 (Search conferido).
