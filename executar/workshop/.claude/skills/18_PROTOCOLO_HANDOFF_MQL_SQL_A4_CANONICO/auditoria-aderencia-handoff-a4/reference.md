# Referência — Auditoria aderência A-4 ↔ playbook 18

## Âncoras

| Dimensão ID | O que valida | Onde no canônico |
|-------------|--------------|------------------|
| ad-01 | MQL/SQL no CRM alinhados a definições e evidência | Passos 2 e 6; DoD |
| ad-02 | Motivos padronizados usados nas desqualificações/rejeições | Passo 3; componentes críticos |
| ad-03 | Campos mínimos do handoff preenchidos na prática | Passo 3; DoD |
| ad-04 | SLA de 1º contato (amostra ou métrica) | Passo 4; componentes críticos |
| ad-05 | Enforcement: redistribuição/escalação quando SLA estoura | Passo 4 |
| ad-06 | Rotina **semanal** operacional com **ata/card** | Passo 5; DoD |
| ad-07 | KPIs do protocolo medidos e comparados a thresholds | Passo 5; Gerenciado |
| ad-08 | % leads **sem status** aceitável | Gerenciado (KPI explícito) |
| ad-09 | Rejeições analisáveis por **motivo** (insumo loop de ajuste) | Componentes críticos; Gerenciado |
| ad-10 | **Change log** / **atas** refletem ajustes (segmentação, mensagem, processo) | DoD; Gerenciado |

## Status no JSON

Valores: `verde`, `amarelo`, `vermelho`, `n.a.` (com justificativa em evidência). Vazio = pendente na `--audit`.

## Consolidado

Igual à skill `auditoria-funil-fontes-verdade`: pior sinal entre dimensões aplicáveis prevalece; `achados_criticos` força vermelho se preenchido.

## Inventário (inputs esperados)

CRM; funil; registros de handoff; SLA; motivos; atas/cards — conforme linha do **`03_INVENTARIO_SKILLS_POR_PLAYBOOK.md`**.
