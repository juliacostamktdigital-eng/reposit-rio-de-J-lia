---
name: protocolo-handoff-mql-sql-a4
description: Define e documenta o Protocolo de Handoff A-4 (MQL→SQL) com critérios passa/não passa, evidência, motivos de rejeição padronizados, campos CRM, SLA, KPIs/thresholds e rotina de revisão — alinhado ao playbook 18 e complementar ao CRM/SLA (07). Gera consolidado Markdown e auditoria de DoD.
---

# Protocolo de handoff MQL/SQL (A-4)

## Fonte canônica

Playbook **`18_PROTOCOLO_HANDOFF_MQL_SQL_A4_CANONICO.md`**. Relação explícita com **`07_CRM_HANDOFF_SLA_MARKETING_VENDAS_CANONICO.md`**: o 18 é o recorte **A-4** (definições, critérios, DoD); o 07 permanece o consolidado operacional de CRM e SLA.

## Propósito (1 frase)

Operar handoffs **Marketing → Vendas** (principalmente **MQL → SQL**) com **critérios, evidência e cadência**, fechando o loop sem “guerra de lead”.

## Quando usar / quando não

**Usar** quando houver handoff Mkt→Vendas, conflito recorrente sobre qualidade de lead ou etapas MQL/SQL ambíguas. **Não usar** como cerimônia sem consequência (playbook: sem mudança com significado não fecha Gerenciado).

## Entradas

Funil unificado (A-2); DEOC; plano de mídia; capacidade e SLA comercial; benchmark (§ Entradas).

## Dependências de skills

- **`funil-unificado-conversoes-a2`** — etapas, fonte da verdade, campos mínimos base.
- **`jornada-lead-raci`** — touchpoints e RACI por etapa (playbook 19); recomendado **antes** de fechar SLA/handoffs operacionais.
- **`setup-crm-handoff-marketing-vendas`** ou equivalente do **playbook 07** — operação CRM/SLA.
- **`benchmark-campo-batalha-gtm`** ou benchmark próprio para thresholds.

## Workflow (6 passos do canônico)

1. Fixar lead “correto” (ICP + **anti-ICP** operando).
2. Definir **MQL** e **SQL** no vocabulário do funil: condição de entrada + **evidência mínima**.
3. Critérios de aceitação/rejeição e **motivos padronizados** no CRM.
4. **SLA**, responsáveis e redistribuição quando estourar.
5. Rotina de revisão: **KPIs**, thresholds V/A/V e **ação** quando piora.
6. Registro obrigatório (rastro) e plano de **auditoria de aderência** (`auditoria-aderencia-handoff-a4`).

Preencher **`templates/protocolo-a4.json`** e gerar o consolidado:

```bash
python3 scripts/build_protocolo_a4.py --write-default templates/protocolo-a4.json
python3 scripts/build_protocolo_a4.py templates/protocolo-a4.json --md ./protocolo-a4-consolidado.md
python3 scripts/build_protocolo_a4.py templates/protocolo-a4.json --audit
```

Quem preferir prosa pode espelhar em **`templates/protocolo-a4.md`** e transcrever para o JSON.

## Saídas (protocolo v1)

Definições MQL/SQL; critérios e motivos; campos CRM; SLA; cadência; evidências mínimas — conforme § Saídas do playbook.

## Definition of Done (playbook)

MQL e SQL com passa/não passa + evidência; campos e motivos padronizados; SLA comunicado com exceção; KPIs/thresholds + ação por faixa; rotina com registro (ata/card) e change log de ajustes.

## Gerenciamento (§ Gerenciado)

KPIs típicos: taxa MQL→SQL; SQL→venda; tempo 1º contato; % rejeições por motivo; % leads sem status. Cadência: **semanal** operacional + **mensual** estrutural. Registro: atas/cards + change log (segmentação, mensagem, processo).

**Loop de ajuste na prática:** use **`loop-ajuste-marketing-vendas`** nas revisões para transformar leitura de KPI em ações (segmentação, mensagem, oferta, processo) com rastro — playbook 18, passo 5 e componentes críticos.

## Artefatos

- `reference.md`
- `templates/protocolo-a4.md`
- `templates/protocolo-a4.json`
- `scripts/build_protocolo_a4.py`
