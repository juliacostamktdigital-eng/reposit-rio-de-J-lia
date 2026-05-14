---
name: loop-ajuste-marketing-vendas
description: Opera o loop de ajuste Mkt↔Vendas do Protocolo A-4 — a partir de KPIs de handoff, rejeições, SLA e feedback comercial, define hipóteses e plano de ação (segmentação, mensagem, oferta ou processo) com responsáveis e registro em ata/change log (playbook 18 passo 5 + componentes críticos + Gerenciado).
---

# Loop de ajuste — Marketing e Vendas (A-4)

## Fonte canônica

Playbook **`18_PROTOCOLO_HANDOFF_MQL_SQL_A4_CANONICO.md`**:

- **Passo 5:** rotina de revisão com KPIs (taxas + tempo), **thresholds V/A/V** e **o que muda quando piora (ação definida)**.
- **Componentes críticos:** *Rotina decisória (o que muda quando a taxa piora) vs leitura de número*; **Loop de ajuste** — *Marketing muda segmentação/mensagem/oferta com base no dado de handoff*.
- **Como gerenciar:** KPIs do handoff; **registro obrigatório** — ata/card com decisões + **change log** (segmentação, mensagem, processo).

## Propósito

Transformar **sinais** (rejeições, atrasos, taxas ruins, feedback de vendas) em **mudanças explícitas** com dono, prazo e rastro — sem confundir com redefinição do protocolo inteiro (isso é `protocolo-handoff-mql-sql-a4`).

## Quando usar

- Revisão **semanal (operacional)** ou **mensal (estrutural)** alinhada ao A-4.
- Após **`auditoria-aderencia-handoff-a4`** com gaps ou semáforo amarelo/vermelho.
- Quando um **motivo de rejeição** domina ou SLA de 1º contato reincide.

## Entradas

KPIs MQL→SQL, SQL→venda, speed-to-lead, motivos padronizados, feedback qualitativo de vendas; links ao protocolo A-4 e plano de mídia (§ Entradas do 18, via operação).

## Dependências

- **`protocolo-handoff-mql-sql-a4`** (thresholds e ações-base por faixa).
- **`funil-unificado-conversoes-a2`**, **`setup-crm-handoff-marketing-vendas`** / 07.
- Opcional: **`changelog-funil-conversoes`** ou change log citado no protocolo para registrar mudanças estruturais.

## Workflow

1. **Leitura:** preencher `leitura_kpis[]` com valor e **faixa** (verde/amarelo/vermelho) vs threshold do protocolo.
2. **Qualitativo:** resumir rejeições por motivo, SLA e **feedback vendas** (`sinais_qualitativos`).
3. **Hipóteses:** listar causas prováveis com nível de confiança.
4. **Plano:** ações em `plano_acao[]` (segmentação, mensagem, oferta, processo comercial, CRM/outro) com responsável e prazo.
5. **Registro:** ata/card + entrada no change log; próxima revisão.

```bash
python3 scripts/build_loop_ajuste_a4.py --write-default templates/loop-ajuste-a4.json
python3 scripts/build_loop_ajuste_a4.py templates/loop-ajuste-a4.json --md ./loop-ajuste-consolidado.md
python3 scripts/build_loop_ajuste_a4.py templates/loop-ajuste-a4.json --audit
```

## Outputs

Plano de ação por faixa, responsáveis, mudanças a registrar e links de evidência — alinhado ao inventário e às saídas esperadas do ciclo A-4.

## Definition of Done (rodada)

Leitura de KPIs fechada; pelo menos uma ação priorizada **se** houver faixa amarela ou vermelha (ou registro explícito de “sem ação — manutenção”); decisão registrada em `registro`.

## Artefatos

- `reference.md`
- `templates/loop-ajuste-a4.md`
- `templates/loop-ajuste-a4.json`
- `scripts/build_loop_ajuste_a4.py`
