---
name: selecao-pack-criativo-ciclo
description: Monta o Pack de Produção — seleção de tipos do banco canônico para primeira leva ou iteração, com quantidades, hipóteses por peça, variações A/B/C e critérios de leitura — playbook 20 passo 5. Depende de `banco-tipos-criativos`; alimenta briefing, roteiro e setup de mídia.
---

# Seleção — pack criativo por ciclo

## Fonte canônica

Playbook **`20_BANCO_TIPOS_CRIATIVOS_CANONICO.md`** e template oficial em **`assets/canonicos/templates/pack-producao.md`** (pack = criativos + ambiente de conversão + guardrails + checklist):

- **Passo 5 (pb. 20):** o catálogo de tipos é **insumo obrigatório do Pack de Produção** (primeira leva e iteração orientadas por **função no funil**).
- **Propósito do banco:** orientar seleção da primeira leva sem reinventar receitas; esta skill **operacionaliza** essa seleção dado plano de mídia, canal, etapa, orçamento e aprendizados.
- **Componentes críticos a respeitar:** objetivo por tipo (função no funil); variações que testam **hipótese**, não só estética; referências/evidência já vivem no tipo — aqui escolhe-se **o quê** produzir neste ciclo e **como medir**.

## Quando usar

- **Primeira leva** de criativos antes de briefing/produção em massa.
- **Próxima iteração** após ciclo com dados ou debrief — preferir **`iteracao-tipo-criativo-por-performance`** antes de novo pack quando houver leitura confiável.
- Alinhamento Mkt + produção: “quantas peças de qual tipo, testando o quê”.

## Quando não usar

- Sem **`banco-tipos-criativos`** mínimo utilizável (ideal: DoD do banco atendido ou exceção documentada em `meta.justificativa_sem_banco`).
- Para escolher tipo **sem** hipótese de aprendizado — voltar ao banco ou ao DEOC.

## Entradas / saídas (inventário)

**Inputs:** plano de mídia, DEOC, benchmark, **banco de tipos**, Meta/Google/etc., canal, etapa de funil, orçamento/capacidade, aprendizados.

**Outputs:** pack recomendado, **quantidade por tipo**, hipóteses, **variações** e **critérios de leitura**.

## Escopo Do Pack

O pack nao e apenas uma lista de pecas criativas. A referencia curta `executar-ai/workshop/skills/09-briefing-pack-producao-criativos-e-conversao.md` reforca que cada pack deve amarrar: canal e tipo de campanha, criativos por hipotese, ambiente de conversao minimo, tracking, guardrails e DoD. Quando o destino for LP/form/WhatsApp/agenda, registre o ambiente aqui e acione `arquitetura-lp-conversao-leadgen` ou `qa-lp-ponto-conversao` se houver risco.

## Dependências

- **Obrigatório:** **`banco-tipos-criativos`** (`banco-tipos.json` ou consolidado).
- **Recomendado entre ciclos:** **`iteracao-tipo-criativo-por-performance`** (relatório + `change_log_sugerido` aplicado ao banco).
- **Downstream:** **`briefing-criativo-video-first`**, **`roteiro-criativo-performance`**, **`setup-campanhas-meta-ads`**, `setup-campanhas-google-ads`, etc.

## Workflow

1. Fixar contexto do ciclo em `meta` (canais, etapa funil, links ao banco + plano + DEOC).
2. Do banco, **filtrar** tipos compatíveis com temperatura, formato e objetivo do plano.
3. Para cada linha em `selecao[]`: `tipo_id`, **quantidade**, **hipótese**, variações (A/B/C), **critério de leitura**, **ângulo/prova/CTA/destino** (template canônico de pack).
4. Preencher **`plano_contexto`**, **ambiente de conversão**, **guardrails** e **checklist de conformidade** (`assets/canonicos/templates/pack-producao.md`).
5. Validar **totais** vs capacidade de produção e orçamento (`totais` + soma das quantidades).
6. Exportar MD para alinhamento e, na sequência, um brief por peça (`creative_id`).

```bash
python3 scripts/build_pack_producao.py --write-default templates/pack-producao.json
python3 scripts/build_pack_producao.py templates/pack-producao.json --md ./pack-producao-consolidado.md
python3 scripts/build_pack_producao.py templates/pack-producao.json --audit
python3 scripts/build_pack_producao.py templates/pack-producao.json --summary
```

## Definition of Done (pack)

Pelo menos **uma** linha em `selecao[]` com `tipo_id`, `quantidade_pecas`, `hipotese_teste` e `criterio_leitura`; `meta.link_banco_tipos` ou `justificativa_sem_banco`; totais coerentes com soma das quantidades (ou nota); **ambiente de conversão** e **tracking mínimo** preenchidos quando o destino não for só lead nativo sem site.

## Artefatos

- `reference.md`
- `templates/pack-producao.md` (alinhado a `assets/canonicos/templates/pack-producao.md`)
- `templates/pack-producao.json`
- `scripts/build_pack_producao.py`
