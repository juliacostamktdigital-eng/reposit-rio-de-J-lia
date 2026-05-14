---
name: jornada-lead-raci
description: Mapeia jornada do lead (touchpoints, decisões) e RACI mínimo por etapa do funil — R/A/C/I, evidência mínima e validação de SLA/capacidade — para governar Funil Unificado (A-2) e Protocolo A-4. Fonte playbook 19. Saída via JSON + Markdown e auditoria de DoD.
---

# Jornada do lead + RACI

## Fonte canônica

Playbook **`19_JORNADA_LEAD_RACI_CANONICO.md`** (legado alinhado: `06-jornada-lead-raci.md`).

## Propósito (1 frase)

Mapear **touchpoints e decisões** da jornada e atribuir **responsabilidades por etapa** para garantir execução e governança do **Funil Unificado** e do **Protocolo de handoff**.

## Quando usar / quando não

**Usar** quando o lead “some” entre áreas, há múltiplos papéis (inbound/outbound/SDR/closer) ou **antes** de fechar SLA/handoffs. **Não usar** para burocracia sem impacto na operação e nos KPIs.

## Entradas e saídas

Conforme canônico: funil A-2; protocolo A-4; estrutura do time; CRM/canais → **mapa de jornada** + **RACI por etapa** + **evidência mínima** + links nos artefatos.

## Dependências

- **`funil-unificado-conversoes-a2`** — etapas e fonte da verdade.
- **`protocolo-handoff-mql-sql-a4`** — pontos de handoff e SLA.
- Opcional: **`setup-crm-handoff-marketing-vendas`** (07), **`changelog-raci-jornada`** (registro obrigatório de mudanças de RACI).

## Workflow (5 passos)

1. Listar etapas do funil e **touchpoints** relevantes por etapa.
2. Por etapa: preencher **R, A, C, I** (papéis ou nomes do time).
3. Definir **evidência mínima** (o que deve existir no CRM/registro).
4. Validar **capacidade** e **SLA** (passo 4 do canônico).
5. Publicar e linkar em funil + protocolo (`meta.link_*` + `publicacao`).

```bash
python3 scripts/build_jornada_lead_raci.py --write-default templates/jornada-lead-raci.json
python3 scripts/build_jornada_lead_raci.py templates/jornada-lead-raci.json --md ./jornada-lead-raci-consolidado.md
python3 scripts/build_jornada_lead_raci.py templates/jornada-lead-raci.json --audit
```

## Gerenciamento (§ Gerenciado do playbook)

KPIs: % etapas com dono; violações de SLA; etapas sem evidência mínima. Thresholds V/A/V e **change log do RACI** ao mudar time — referência em `reference.md`; uso operacional em **`auditoria-raci-sla-evidencias`** e **`changelog-raci-jornada`**.

## Definition of Done (playbook)

RACI para **todas** as etapas mapeadas do funil em escopo; evidência mínima por etapa; SLA compatível; links com funil e protocolo.

## Artefatos

- `reference.md`
- `templates/jornada-lead-raci.md`
- `templates/jornada-lead-raci.json`
- `scripts/build_jornada_lead_raci.py`
