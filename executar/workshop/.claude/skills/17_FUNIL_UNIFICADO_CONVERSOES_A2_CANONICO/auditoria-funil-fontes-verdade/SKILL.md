---
name: auditoria-funil-fontes-verdade
description: Audita aderência do funil em operação — concordância entre fontes da verdade (CRM, planilha, plataforma), donos por etapa, eventos de tracking, campos mínimos e adoção — com diagnóstico verde/amarelo/vermelho alinhado ao playbook 17 (Gerenciado). Entrada — artefato A-2, exports, amostra de leads; saída — relatório, semáforo consolidado e backlog priorizado.
---

# Auditoria — funil e fontes da verdade

## Fonte canônica

Playbook **`17_FUNIL_UNIFICADO_CONVERSOES_A2_CANONICO.md`**, em especial:

- **Saídas (outputs):** fonte da verdade por etapa, campos mínimos, eventos.
- **Componentes críticos:** uma fonte preferencial por etapa; evitar planilha paralela; evidência auditável.
- **Como gerenciar (Gerenciado):** KPIs (% status válido, % campos mínimos, ciclo); **thresholds** vermelho / amarelo / verde; cadência quinzenal→mensal; **change log** obrigatório para mudanças.

Esta skill **não** redesenha o funil: valida se a operação e os dados batem com o **Funil unificado (A-2)** publicado.

## Quando usar

- Na cadência de governança (quinzenal até estabilizar, depois mensal — § Gerenciado).
- Quando surgem números conflitantes entre CRM, backup e plataformas de mídia.
- Antes de debrief pesado, revisão de SLA ou mudança de contrato de dados.
- Após incidente (leads sem status, perda de atribuição, “dois funis” no discurso).

## Pré-requisitos

- Artefato **`funil-unificado-conversoes-a2`** (v1 ou versão atual) com etapas e fonte da verdade declarada por etapa.
- Acesso a amostra auditável: CRM, planilha de backup/testes, relatórios de mídia quando couber.

## Workflow

1. Abrir o JSON do funil ou o consolidado `.md` e fixar **versão de referência** em `meta` / `referencia_funil`.
2. Para cada **dimensão** do template: registrar evidência, semáforo (`verde` / `amarelo` / `vermelho` / `n.a.`) e gap.
3. Preencher **etapas sem dono**, **campos mínimos** (aderência) e **eventos de tracking** na prática.
4. Gerar relatório e consolidar prioridades no **backlog**. Mudanças estruturais no funil → registrar em **`changelog-funil-conversoes`**.

```bash
python3 scripts/evaluate_auditoria_funil.py --write-default templates/auditoria-funil.json
python3 scripts/evaluate_auditoria_funil.py templates/auditoria-funil.json --md ./relatorio-auditoria-funil.md
python3 scripts/evaluate_auditoria_funil.py templates/auditoria-funil.json --summary
python3 scripts/evaluate_auditoria_funil.py templates/auditoria-funil.json --audit
```

## Regra de consolidado (derivada do § Gerenciado)

- **Vermelho** se houver discrepância material entre fontes ou etapas críticas **sem dono** com impacto operacional, ou qualquer dimensão obrigatória em vermelho.
- **Amarelo** se não houver vermelho, mas houver baixa adesão a dados/campos, excesso de etapas vs qualidade de dado, ou dimensões em amarelo.
- **Verde** se dimensões aplicáveis estão verdes (ou `n.a.` justificado) e KPIs mínimos coerentes com evidência.

O script aplica uma heurística documentada em `reference.md`; o parecer final permanece **humano**.

## Outputs

- Relatório Markdown (semáforos, contagem, backlog).
- JSON reutilizável para histórico / comparar rodadas.

## Artefatos

- `reference.md`
- `templates/auditoria-funil.md`
- `templates/auditoria-funil.json`
- `scripts/evaluate_auditoria_funil.py`

## Definition of Done (da auditoria)

Todas as dimensões aplicáveis com semáforo e evidência; amostra e período descritos; **diagnóstico global** explícito; backlog priorizado ou explícito “sem itens”; revisor humano indicado em `meta`.
