---
name: setup-meta-conversao-site
description: Configura campanhas Meta com otimização para conversão no site (LP/evento no domínio) quando pixel/CAPI, evento e LP estão validados e há sinal suficiente para o algoritmo, conforme playbook 15 (subtipo venda/conversão). Use após setup base da conta, QA de LP e definição de evento no funil; não substitui lead nativo quando o tracking é instável. Exige checklist específico N2 além do setup genérico.
---

# Setup Meta Ads — Conversão no site

## Fonte canônica

Playbook **`15_SETUP_CAMPANHAS_META_ADS_CANONICO.md`**, seções **1** (pré-requisitos gerais), **4–5** (conta, pixel/CAPI, eventos e regra de profundidade), **6–8** (públicos, inclusão visitantes LP/site), **9** (“Venda/conversão”), **13** (go-live), **14** (N2 com subtipo), **16** (evitar conversão sem evento validado). Legado: **`assets/legacy/merge/skills/10-2-meta-conversao.md`**.

## Princípio

Conversão no site só faz sentido quando o **evento é confiável**, a **LP está pronta** e **pixel/CAPI preservam sinal** para otimização (Seção 9). Sem validação de evento, o canônico classifica como armadilha (Seção 16). A **profundidade do evento de otimização** deve seguir a Seção 5: o mais profundo possível **sem matar volume**.

## Dependências

- **`setup-campanhas-meta-ads`** — estrutura campanha/conjunto/anúncio, públicos, nomenclatura, checklist geral.
- **`gerador-taxonomia-utm-ids`** — IDs e UTMs na URL final.
- **`contrato-dados-marketing-crm`** — quando a conversão gera lead (ex.: envio de formulário na LP).
- **`qa-lp-ponto-conversao`** — LP e ponto de conversão alinhados à promessa e ao evento.
- Funil unificado — **fonte da verdade** do nome e significado do evento.

## Quando usar / quando não usar

| Usar | Não usar |
| --- | --- |
| Objetivo é ação **no site** (lead na LP, agendamento, compra etc.) com evento disparado de forma estável | Evento/pixel instável ou LP incompleta → tratar com lead nativo ou tráfego até estabilizar tracking |
| Evento **validado** (testes em Events Manager / fluxo real) e hipótese de volume compatível com o evento escolhido | “Subir conversão” só pelo nome da campanha, sem prova de evento |

## Workflow

1. Confirmar **pré-requisitos** da Seção 9: evento validado; volume e valor do ciclo **justificam** a otimização (se volume for baixo, documentar uso de evento mais raso conforme Seção 5).
2. Amarrar **evento de otimização** ao funil (nome técnico + definição comercial) e registrar **justificativa** profundidade vs volume.
3. Conferir **pixel + CAPI** (quando aplicável), testes e priorização de eventos na conta.
4. Fixar **URLs finais** (LP, obrigado/thank-you se impactar medição), **UTMs** e consistência com o contrato de dados.
5. Planejar **públicos** (ex.: visitantes LP/site 30D no canônico) e **exclusões** (ex.: remarketing sem excluir convertidos — Seção 16).
6. Preencher **matriz de testes** e **3–5 criativos** por conjunto com hipótese (Seções 11–12).
7. Executar **teste ponta a ponta**: disparo do evento visível para a Meta; se a conversão for lead em formulário LP, validar **backup** e **CRM/handoff** como no setup geral N2.
8. Gerar consolidado:

```bash
python3 scripts/build_meta_conversao_site.py templates/meta-conversao-site.json --md ./conversao-site-saida.md
python3 scripts/build_meta_conversao_site.py templates/meta-conversao-site.json --audit
```

9. No artefato de **`setup-campanhas-meta-ads`**, marcar subtipo **conversão site** como aplicável.

## Outputs

- Registro do evento, URLs, pixel/CAPI, testes, matriz de testes e checklist **específico** de conversão no site para N2.

## Artefatos

- `reference.md` — trechos e regras do playbook 15 + síntese 10-2.
- `templates/meta-conversao-site.md`
- `templates/meta-conversao-site.json`
- `scripts/build_meta_conversao_site.py`

## Definition of Done (N2 para este subtipo)

Evento validado e documentado; pixel/eventos testados; LP e UTMs coerentes; teste de conversão (e lead backup/CRM quando o evento for captura na LP); matriz e hipótese registradas; itens do go-live geral **mais** este checklist preenchido (Seção 14: subtipos com checklist específico).
