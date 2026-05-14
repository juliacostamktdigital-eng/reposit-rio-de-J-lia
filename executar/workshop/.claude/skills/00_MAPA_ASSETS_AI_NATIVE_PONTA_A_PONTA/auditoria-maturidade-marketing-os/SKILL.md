---
name: auditoria-maturidade-marketing-os
description: Audita a maturidade N1/N2/N3 do Marketing OS por componente, verificando evidencias, donos, dados, execucao, cadencia e aprendizado. Use quando o usuario pedir auditoria de conta, diagnostico de maturidade, health check operacional, N2/N3, gaps, falso positivo de implementacao ou readiness antes de go-live/proximo ciclo.
---

# Auditoria Maturidade Marketing OS

## Quando Usar

Use para avaliar se uma conta esta pronta, implementada ou gerenciada:

- antes de iniciar planning ou pacote v1;
- antes de go-live;
- depois de um ciclo de campanha;
- quando resultado ruim pode ser demanda, conversao, oferta, tracking ou vendas;
- quando ha duvida se a conta esta em N1, N2 ou N3;
- quando o time precisa priorizar gaps com evidencia.

Nao use para:

- criar todos os assets faltantes;
- substituir auditorias especialistas de Meta, Google, CRM, LP ou tracking;
- dar nota sem evidencias verificaveis.

## Inputs Necessarios

- Inventario de assets do cliente ou mapa gerado por `mapa-assets-cliente-ai-native`.
- Evidencias: links, prints, arquivos, planilhas, CRM, exports, logs, checklists.
- Dados de midia, LP, tracking, CRM e qualidade comercial.
- Donos por componente e cadencias existentes.
- Historico de decisoes, backlog, debriefs e changelog.

Se a evidencia nao existir, classifique como ausente. Nao aceite "esta no grupo", "esta combinado" ou "o time sabe" como evidencia.

## Modelo De Maturidade

- `N1 - existe/rascunho`: ha intencao, arquivo solto, setup parcial ou processo informal.
- `N2 - implementado/auditavel`: assets obrigatorios existem, donos claros, dados minimos preservados, evidencia de execucao e processo auditavel.
- `N3 - gerenciado`: dados lidos em cadencia, decisoes registradas, hipoteses no backlog, aprendizados alimentam proximo ciclo e padroes sao canonizados.

## Workflow

1. Defina o escopo da auditoria: conta inteira, pre-go-live, componente especifico ou pos-ciclo.
2. Liste os componentes avaliados:
   - handoff e discovery;
   - diagnostico e pacote v1;
   - benchmark/DEOC/oferta;
   - midia;
   - criativo e LP;
   - tracking/dados;
   - CRM/SLA/vendas;
   - testes/performance;
   - debrief/aprendizado;
   - governanca e versionamento.
3. Para cada componente, verifique criterios N2 e N3 em `reference.md`.
4. Atribua status: `N0`, `N1`, `N2`, `N3` ou `bloqueado`.
5. Registre evidencia, lacuna, risco, dono e proxima acao.
6. Marque falsos positivos:
   - asset existe, mas nao e usado;
   - setup existe, mas nao tem lead teste;
   - dado existe, mas nao fecha com CRM;
   - campanha roda, mas nao ha hipotese;
   - relatorio existe, mas nao ha decisao.
7. Gere score e prioridades.
8. Recomende proximo nivel de maturidade com menor conjunto de acoes necessario.

## Output Esperado

Produza:

- sumario executivo da maturidade;
- score geral e por componente;
- tabela N0/N1/N2/N3 com evidencia;
- falsos positivos e riscos;
- bloqueadores antes de go-live ou proximo ciclo;
- backlog priorizado;
- recomendacao de decisao: seguir, seguir com risco aceito, pausar, corrigir ou replanejar.

Use `templates/checklist-n2-n3.md` para auditoria em Markdown.
Use `templates/auditoria-maturidade.json` para entrada do script de score.

## Script Utilitario

Para gerar score de maturidade a partir de JSON:

```bash
python scripts/score_maturity.py templates/auditoria-maturidade.json --md /tmp/auditoria-maturidade.md --csv /tmp/auditoria-maturidade.csv
```

O script nao substitui julgamento especializado. Ele padroniza score, severidade e agrupamento dos achados.

## Definition Of Done

- Todos os componentes do escopo foram avaliados.
- Cada nota tem evidencia ou lacuna explicita.
- Falsos positivos foram chamados pelo nome.
- Bloqueadores foram separados de melhorias.
- Existe recomendacao clara de decisao.
- Proximas acoes tem dono, prioridade e criterio de pronto.

## Armadilhas

- Confundir documento criado com processo implementado.
- Confundir dashboard com gestao.
- Aceitar N3 sem decisao registrada.
- Dar nota alta para tracking sem lead teste ponta a ponta.
- Avaliar midia sem qualidade comercial.
- Tratar ausencia de evidencia como "provavelmente ok".

## Referencias

- Playbook canonico: `assets/canonicos/00_MAPA_ASSETS_AI_NATIVE_PONTA_A_PONTA.md`
- Detalhamento: `reference.md`
- Template: `templates/checklist-n2-n3.md`
- Schema: `templates/auditoria-maturidade.json`
