# Referência — Auditoria RACI/SLA ↔ playbook 19 § Gerenciado

## Dimensões sugeridas (`dimensoes[]`)

| ID | Foco | Threshold no canônico |
|----|------|------------------------|
| ar-01 | **% etapas com dono** (Accountable claro na prática) | KPI: % etapas com dono |
| ar-02 | **Handoffs** com responsável definido e assumido | Vermelho: handoff sem responsável |
| ar-03 | **Lead “sumindo”** / rotas sem accountable | Vermelho |
| ar-04 | **Evidência mínima** no CRM vs matriz RACI | Amarelo: dono sem evidência; KPI % sem evidência |
| ar-05 | **SLA:** violações e **ação** quando estoura | Amarelo: SLA estoura sem ação; verde: ação definida |
| ar-06 | **Change log RACI** atualizado quando papel muda | Registro obrigatório § Gerenciado |

## KPIs no JSON (`kpis_medidos`)

Espelham o canônico:

- `pct_etapas_com_dono`
- `pct_violacoes_sla`
- `pct_etapas_sem_evidencia_minima`

Valores podem ser “n/d” com nota até haver extração do CRM.

## Entradas (inventário)

RACI; CRM; SLA; registros de atendimento; funil; protocolo A-4 — alinhado ao **`03_INVENTARIO_SKILLS_POR_PLAYBOOK.md`**.

## Relação com outras skills

| Skill | Papel |
|-------|--------|
| `jornada-lead-raci` | Referência “como deveria ser” |
| `protocolo-handoff-mql-sql-a4` | SLA e responsáveis no handoff |
| `auditoria-aderencia-handoff-a4` | Pode cruzar com RACI em etapas MQL/SQL |
| `changelog-raci-jornada` | Registrar correções estruturais de papel (`render_changelog_raci.py` + templates) |
