---
name: inventario-gaps-assets-marketing-os
description: Identifica lacunas sistêmicas de assets do Marketing OS além de copy, mídia e criativo, avaliando handoff, diagnóstico, tracking, CRM, SLA, QA, debrief, versionamento, automação e evidências N2/N3. Use em auditoria de conta, onboarding, readiness, go-live, revisão operacional ou quando o usuário pedir gaps, assets faltantes ou inventário transversal.
---

# Inventário Gaps Assets Marketing OS

## Quando Usar

Use para descobrir o que falta na operação antes de culpar mídia, copy ou criativo.

Situações típicas:

- onboarding de cliente;
- auditoria de operação;
- preparação de go-live;
- revisão N2/N3;
- QA transversal;
- campanha travada por ausência de asset;
- operação sem tracking, CRM, SLA, handoff ou debrief confiável.

## Inputs Necessários

- mapa de assets do cliente;
- status operacional atual;
- evidências existentes;
- auditorias anteriores;
- plano de mídia;
- DEOC/DCC;
- tracking/UTMs;
- CRM e SLA;
- planilha de testes;
- QA criativo/LP/tracking;
- debriefs e changelog.

## Workflow

1. Liste os assets existentes e faltantes.
2. Classifique cada asset por componente:
   - handoff;
   - discovery/diagnóstico;
   - estratégia/oferta;
   - mídia;
   - criativo/LP;
   - tracking/dados;
   - CRM/vendas;
   - testes/aprendizado;
   - versionamento;
   - automação.
3. Verifique evidência:
   - link;
   - arquivo;
   - planilha;
   - print;
   - responsável;
   - data de atualização.
4. Classifique status:
   - inexistente;
   - rascunho;
   - existe mas incompleto;
   - pronto N2;
   - gerenciado N3.
5. Avalie severidade:
   - crítica: bloqueia go-live, tracking, CRM ou leitura;
   - alta: prejudica resultado ou aprendizado;
   - média: cria retrabalho ou risco;
   - baixa: melhoria de escala.
6. Defina impacto:
   - produção;
   - conversão;
   - leitura;
   - vendas;
   - governança;
   - automação.
7. Priorize e indique próxima ação.
8. Encaminhe gaps acionáveis para `backlog-operacional-growth`.

## Output Esperado

- inventário de assets;
- lista de gaps;
- severidade e impacto;
- dono recomendado;
- prioridade;
- evidências faltantes;
- decisão de encaminhamento para backlog.

Use `templates/inventario-gaps-assets.md` para entrega manual.
Use `templates/gaps-assets.json` com o script para gerar CSV/Markdown.

## Script Utilitário

```bash
python3 scripts/audit_asset_gaps.py templates/gaps-assets.json --md /tmp/gaps-assets.md --csv /tmp/gaps-assets.csv
```

O script normaliza gaps, calcula score de prioridade e gera inventário priorizado.

## Definition Of Done

- Assets críticos foram verificados.
- Gaps têm severidade, impacto, dono e próxima ação.
- Evidências estão registradas.
- Gaps bloqueadores estão destacados.
- Itens acionáveis foram preparados para backlog.
- A avaliação não depende de opinião sem evidência.

## Cuidados

- Não criar uma skill para cada asset esquecido.
- Não confundir "existe arquivo" com N2.
- Não marcar N3 sem revisão, changelog e aprendizado.
- Não esconder gap crítico como pendência leve.
- Não avançar go-live com tracking/CRM sem evidência.
