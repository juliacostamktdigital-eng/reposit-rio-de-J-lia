---
name: auditoria-aderencia-handoff-a4
description: Valida se o Protocolo A-4 (MQL→SQL) está sendo seguido na prática — definições no CRM, motivos padronizados, campos mínimos, SLA com enforcement, rotina semanal/mensal com registro e KPIs do § Gerenciado. Fonte playbook 18 passo 6 + DoD. Saída — diagnóstico V/A/V, achados, ações e apoio a change log.
---

# Auditoria de aderência — handoff A-4

## Fonte canônica

Playbook **`18_PROTOCOLO_HANDOFF_MQL_SQL_A4_CANONICO.md`**, em especial:

- **Passo 6:** implementar **registro obrigatório (rastro)** e **auditar aderência**.
- **DoD:** MQL/SQL com evidência; campos e motivos no CRM; SLA comunicado; KPIs/thresholds com ação; **rotina com ata/card** e **change log** de ajustes.
- **Como gerenciar:** KPIs (taxa MQL→SQL, SQL→venda, tempo 1º contato, % rejeições por motivo, **% leads sem status**); cadência **semanal + mensal**; registro de decisões e change log.

## Propósito

Comparar **protocolo A-4 publicado** (`protocolo-handoff-mql-sql-a4`) + funil A-2 com **evidência operacional** (CRM, atas, amostra de leads), sem substituir o playbook **07** (operação CRM/SLA).

## Quando usar

- Cadência do protocolo (alinhada à revisão **semanal/mensal**).
- Após mudança de CRM, SLA ou definição de MQL/SQL.
- Quando KPIs do handoff pioram ou conflito Mkt×Vendas reaparece.

## Pré-requisitos

- Artefato **`protocolo-a4.json`** (ou consolidado) vigente.
- **`funil-unificado-conversoes-a2`** e, quando existir, operação **`setup-crm-handoff-marketing-vendas`** / playbook 07.

## Workflow

1. Fixar `meta`: período, amostra, links para protocolo A-4, funil A-2 e CRM/07.
2. Preencher cada **dimensão** com **semáforo** (`verde` / `amarelo` / `vermelho` / `n.a.`), **evidência** factível e **gap**.
3. Registrar **achados** em `achados_criticos` quando houver risco imediato; completar **indicadores** § Gerenciado.
4. Priorizar **backlog** e, se necessário, atualizar **`changelog-funil-conversoes`** ou change log citado no protocolo. Ações de Mkt (segmentação, mensagem, oferta) → rodada **`loop-ajuste-marketing-vendas`**.

```bash
python3 scripts/evaluate_aderencia_handoff_a4.py --write-default templates/auditoria-handoff-a4.json
python3 scripts/evaluate_aderencia_handoff_a4.py templates/auditoria-handoff-a4.json --md ./relatorio-aderencia-a4.md
python3 scripts/evaluate_aderencia_handoff_a4.py templates/auditoria-handoff-a4.json --summary
python3 scripts/evaluate_aderencia_handoff_a4.py templates/auditoria-handoff-a4.json --audit
```

## Regra de consolidado (heurística)

- **Vermelho:** qualquer dimensão obrigatória em vermelho ou achado crítico explícito em `achados_criticos`.
- **Amarelo:** alguma dimensão em amarelo, sem vermelho.
- **Verde:** somente verde ou `n.a.` justificado nas dimensões aplicáveis.

Parecer final **humano** em `meta.parecer_humano`.

## Artefatos

- `reference.md`
- `templates/auditoria-handoff-a4.md`
- `templates/auditoria-handoff-a4.json`
- `scripts/evaluate_aderencia_handoff_a4.py`

## Definition of Done (rodada de auditoria)

Meta e amostra descritos; dimensões aplicáveis com semáforo; consolidado sugerido; backlog ou explícito “sem ações”; revisor indicado.
