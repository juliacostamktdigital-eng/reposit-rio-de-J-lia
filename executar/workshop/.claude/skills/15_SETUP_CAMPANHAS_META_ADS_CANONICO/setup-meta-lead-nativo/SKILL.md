---
name: setup-meta-lead-nativo
description: Configura captação via formulário nativo (Instant Forms / Lead Ads) na Meta com perguntas de qualificação, SLA de follow-up, integração CRM/backup e rastreio de origem, em alinhamento ao playbook 15 (subtipo captação de leads). Use quando o destino for formulário nativo; após DEOC, contrato de dados e setup base de campanhas quando existir. Não substitui conversão no site nem WhatsApp como destino—cada um tem fricção e tracking diferentes.
---

# Setup Meta Ads — Lead nativo (formulário na Meta)

## Fonte canônica

Playbook **`15_SETUP_CAMPANHAS_META_ADS_CANONICO.md`**, seções **5** (eventos leadgen), **8–9** (estrutura e tipo “Captação de leads”), **13** (go-live — campos/perguntas lead nativo), **14** (N2 — checklist por subtipo), **16** (evitar lead nativo sem SLA ou sem perguntas mínimas). Contexto legado: **`assets/legacy/merge/skills/10-1-meta-lead-nativo.md`**.

## Princípio

Lead nativo reduz dependência de LP mas **exige** perguntas/qualificação equilibradas com volume, **SLA de atendimento acordado antes de ativar**, planilha backup e caminho CRM auditável. Sem isso, CPL baixo vira ruído (cf. canônico seção 16).

## Dependências

- **`setup-campanhas-meta-ads`** — conta, públicos, estrutura campanha/conjunto/anúncio, nomenclatura, pré go-live genérico.
- **`gerador-taxonomia-utm-ids`** — `campaign_id`, `adgroup_id`, `creative_id` preservados na operação e, quando possível, no CRM.
- **`contrato-dados-marketing-crm`** — campos, origem, backup.
- Protocolo de handoff / funil (ex. skills do playbook 17–18 quando existirem) — critérios MQL e perguntas alinhadas.

## Quando usar / quando não usar

| Usar | Não usar |
| --- | --- |
| Destino é formulário Instant Lead; LP ainda imatura ou hipótese valida contato rápido | Objetivo é otimizar evento **no site** com pixel/CAPI confiável → `setup-meta-conversao-site` |
| CRM/SLA e backup já definidos ou em definição fechada no mesmo sprint | **Sem** SLA de follow-up por escrito |
| Oferta e mensagem aprovadas (DEOC / guardrails) | Substituir estratégia de MQL por apenas “volume cego” sem qualificação |

## Workflow

1. Confirmar **pré-requisitos** da seção “Captação de leads” (oferta clara, CRM/SLA, backup ativo, SLA aceito **antes** de ativar nativo).
2. Desenhar o **Lead Form**: introdução, campos padrão e custom, perguntas de qualificação ligadas a MQL/handoff, privacidade, tela de obrigado / próximo passo.
3. Definir **integração** (CRM, webhook, Zapier, Leads Center, CSV) e **prova** com lead de teste em CRM **e** backup.
4. Alinhar **eventos** (Seção 5): `Lead` no envio; evolução para MQL/offline quando houver volume — sem prometer otimização mais profunda sem dados.
5. Revisar **públicos** (remarketing “formulário aberto sem envio” no canônico) e exclusões, em conjunto com a estrutura da skill principal de setup.
6. Registrar **matriz de testes** (criativo/ângulo vs público; não tudo ao mesmo tempo).
7. Preencher **`templates/meta-lead-nativo.md`** ou o JSON e gerar o consolidado:

```bash
python3 scripts/build_meta_lead_nativo.py templates/meta-lead-nativo.json --md ./lead-nativo-saida.md
python3 scripts/build_meta_lead_nativo.py templates/meta-lead-nativo.json --audit
```

8. Marcar no artefato principal de setup (`estrutura-campanha-meta.json`) o subtipo **Lead formulário nativo** como aplicável.

## Outputs

- Especificação do formulário nativo (campos, perguntas, intenção comercial).
- Registro de integração, SLA, teste ponta a ponta e checklist específico N2 para lead nativo.

## Artefatos

- `reference.md` — regras e citações do playbook 15 + legado 10-1.
- `templates/meta-lead-nativo.md` — preenchimento manual.
- `templates/meta-lead-nativo.json` — fonte para script.
- `scripts/build_meta_lead_nativo.py` — Markdown + auditoria.

## Definition of Done (N2 para este subtipo)

SLA e backup validados; formulário com perguntas/campos conferidos; integração testada com lead real de teste; origem (`campaign_id` / UTMs / campos de contrato) documentada; matriz de testes registrada; itens do canônico seção 13 “campos e perguntas do lead nativo conferidos” atendidos.
