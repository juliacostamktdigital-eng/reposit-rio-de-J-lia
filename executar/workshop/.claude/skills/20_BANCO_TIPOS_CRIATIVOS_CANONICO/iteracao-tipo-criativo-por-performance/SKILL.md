---
name: iteracao-tipo-criativo-por-performance
description: Análise pós-campanha por tipo de criativo — dados, impacto, veredito (manter/alterar/descontinuar), mudanças sugeridas no banco, novas variações e entradas de change log — playbook 20 § Gerenciado (KPI impacto por tipo; iteração tipo→mudança→resultado). Alimenta `banco-tipos-criativos` e o próximo `selecao-pack-criativo-ciclo`.
---

# Iteração de tipo de criativo por performance

## Fonte canônica

Playbook **`20_BANCO_TIPOS_CRIATIVOS_CANONICO.md`**:

- **Quando usar:** inclui **iterar receita** com especialistas (workshop); esta skill adiciona o laço **dados → decisão → registro**.
- **Componentes críticos:** variações que testam **hipóteses**; evidência (benchmark no tipo; aqui **evidência de performance**).
- **Passo 4 (catálogo):** versionar mudanças com **change log** (o que mudou no tipo e por quê) — saída desta skill deve **espelhar** em `change_log_catalogo` / histórico do tipo no **`banco-tipos-criativos`**.
- **§ Gerenciado:** KPIs **impacto por tipo**; **taxa de iteração** (tipo → mudança → resultado); **change log por tipo** + vínculo com campanhas.

## Propósito

Traduzir **performance observada** (mídia, criativo, vendas quando couber) em **decisões explícitas** sobre cada `tipo_id` e em **patch** revisível para o catálogo (template, hipótese, variações, DoD).

## Quando usar

- Após janela mínima de leitura do ciclo (cadência **mensal** por canal/segmento ou **após ciclo relevante**, playbook).
- Quando há **debrief**, export de ads manager, planilha de testes ou relatório com **atribuição por creative_id / tipo**.
- Ante de montar o **próximo pack** (`selecao-pack-criativo-ciclo`).

## Quando não usar

- Sem **identificação** do tipo ou criativo nos dados (não inventar performance por tipo).
- Amostra tão pequena que o veredito seria ruído — registrar como **inconclusivo** em vez de “alterar”.

## Entradas / saídas (inventário)

**Inputs:** performance por tipo, criativos usados, métricas, feedback comercial, debriefs.

**Outputs:** recomendações **manter / alterar / descontinuar** (e variantes: pausar, expandir), **change log** sugerido, **novas variações** / hipóteses para próximo teste.

## Dependências

- **`banco-tipos-criativos`** — tipos e versões atuais.
- Opcional: **`selecao-pack-criativo-ciclo`** (pack que gerou o teste), exports de mídia, CRM.

## Workflow

1. Carregar `meta` com período, links ao banco e fontes de dados.
2. Por tipo exercitado no período, preencher `analise[]`: métricas, baseline/esperado, **veredito**, evidência curta.
3. Para **alterar** ou **expandir**: preencher `mudanca_proposta` (campos do banco afetados), `novas_variacoes_sugeridas`, `nova_hipotese`.
4. Gerar linhas `change_log_sugerido[]` prontas para colar em `banco-tipos.json` → `change_log_catalogo`.
5. Atualizar `tipos[].campanhas_onde_usado` e versão do tipo no banco após aprovação humana.

```bash
python3 scripts/evaluate_iteracao_tipos.py --write-default templates/iteracao-tipos.json
python3 scripts/evaluate_iteracao_tipos.py templates/iteracao-tipos.json --md ./iteracao-tipos-consolidado.md
python3 scripts/evaluate_iteracao_tipos.py templates/iteracao-tipos.json --audit
python3 scripts/evaluate_iteracao_tipos.py templates/iteracao-tipos.json --summary
```

## Definition of Done (por linha em `analise[]`)

`tipo_id`, `veredito`, `evidencia_resumida` e **métrica primária** ou marcação explícita **inconclusivo** com motivo; se `alterar|descontinuar|expandir`, `mudanca_proposta` ou risco registrado.

## Artefatos

- `reference.md`
- `templates/changelog-tipo-criativo.md` (ficha por tipo / ciclo)
- `templates/iteracao-tipos.json`
- `scripts/evaluate_iteracao_tipos.py`
