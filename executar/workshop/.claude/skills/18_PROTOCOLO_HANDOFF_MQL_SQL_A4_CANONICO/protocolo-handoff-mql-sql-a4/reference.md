# Referência — Protocolo A-4 ↔ playbook 18

Canônico: `18_PROTOCOLO_HANDOFF_MQL_SQL_A4_CANONICO.md`.

## Passos ↔ JSON

| Passo | Conteúdo | Chaves principais |
|-------|-----------|-------------------|
| 1 | Lead correto | `lead_correto.*` |
| 2 | MQL e SQL | `mql.*`, `sql.*` |
| 3 | Aceite/rejeição | `aceitacao_rejeicao.*`, `motivos_rejeicao[]` |
| 4 | SLA | `sla.*` |
| 5 | Rotina / KPIs / thresholds / ações | `rotina.*`, `rotina.kpis[]` |
| 6 | Rastro e auditoria | `evidencia_auditavel.*`; execução via `auditoria-aderencia-handoff-a4` |

## Saídas do playbook ↔ estrutura

| Saída | JSON |
|-------|------|
| Definição MQL/SQL passa/não passa | `mql`, `sql` |
| Critérios aceitação/rejeição + motivos | `aceitacao_rejeicao` |
| Campos mínimos CRM handoff | `crm_campos[]` |
| SLA + redistribuição | `sla` |
| Cadência + KPIs + thresholds + ação | `rotina` |
| Evidências mínimas | `evidencia_auditavel` + campos `evidencia_minima` em MQL/SQL |

## Componentes críticos (iteração)

Playbook: critério objetivo vs rótulo subjetivo; motivos de rejeição para melhoria; SLA com enforcement; rotina **decisória**; loop de ajuste Mkt a partir do dado de handoff.

## Auditoria (`--audit`)

Verifica o **DoD** do playbook no JSON: meta e links; lead correto; blocos MQL/SQL completos; ≥2 motivos de rejeição com código e label; ≥2 campos CRM; SLA (tempo 1º contato, responsável, redistribuição); ≥2 KPIs com thresholds e **ação se vermelho**; registro de decisões descrito; concordância Mkt+Vendas quando aplicável.

## Relação com playbook 07

Operacional de CRM/pipeline/handoff continua no **07**; este JSON documenta o **contrato A-4** que o 07 deve conseguir executar. Use `meta.link_crm_sla_07` para amarrar.
