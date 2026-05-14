---
name: banco-tipos-criativos
description: Mantém catálogo versionável de tipos de criativo (receitas) com taxonomia formato × temperatura × objetivo de funil, template, variações A/B/C, DoD, referências de benchmark e change log — playbook 20. Insumo obrigatório para pack de produção (`selecao-pack-criativo-ciclo`) e briefing/roteiro.
---

# Banco de tipos de criativo

## Fonte canônica

Playbook **`20_BANCO_TIPOS_CRIATIVOS_CANONICO.md`**:

- **Propósito:** manter banco versionável de receitas para não reinventar do zero e orientar primeira leva por **função no funil**.
- **Passos:** taxonomia mínima → 10–30 tipos base → por tipo: mecanismo, template, variações, refs → **versionar** com change log → catálogo como insumo do **Pack de Produção** (`assets/canonicos/templates/pack-producao.md` + skill **`selecao-pack-criativo-ciclo`**).
- **DoD (catálogo “pronto”):** taxonomia definida; **10+** tipos com template completo e **≥1 referência** cada; change log de alterações.
- **Gerenciado:** KPIs (tipos usados por campanha; impacto por tipo; taxa iteração); cadência **mensal** por canal/segmento e após ciclos; **change log por tipo** + **link para campanhas** onde foi usado.

Template oficial espelhado: `templates/tipo-criativo.md` (alinhado a `assets/canonicos/templates/tipo-criativo.md`).

## Quando usar / quando não

**Usar** na primeira leva, workshops de iteração de receita, ou ao formalizar aprendizados em tipos reutilizáveis. **Não usar** como galeria sem hipótese, template enxuto e DoD (contra-indicação explícita do playbook).

## Entradas / saídas

Conforme canônico: benchmark, plano de mídia, DEOC, empacotamento de oferta → **catálogo** (tipos + taxonomia + histórico de mudanças).

## Dependências

- Downstream: **`selecao-pack-criativo-ciclo`**, **`briefing-criativo-video-first`**, **`roteiro-criativo-performance`**, **`setup-campanhas-meta-ads`** (e equivalentes Google).
- Opcional: **`iteracao-tipo-criativo-por-performance`** após ciclos com dados (§ Gerenciado playbook 20).

## Workflow

1. Declarar taxonomia mínima em `taxonomia` (formato × temperatura × objetivo).
2. Cadastrar tipos em `tipos[]` (um registro = uma receita); usar `templates/tipo-criativo.md` para revisão humana ou espelhar campos no JSON.
3. A cada mudança relevante em um tipo, adicionar linha em `change_log_catalogo[]` (**o que mudou no tipo e por quê**).
4. Preencher `campanhas_onde_usado` / links quando o tipo sair do papel (§ Gerenciado).
5. Auditar aderência ao DoD antes de declarar catálogo “operacional”; em seguida **`selecao-pack-criativo-ciclo`** para montar o pack do ciclo.

```bash
python3 scripts/build_banco_tipos.py --write-default templates/banco-tipos.json
python3 scripts/build_banco_tipos.py templates/banco-tipos.json --md ./banco-tipos-consolidado.md
python3 scripts/build_banco_tipos.py templates/banco-tipos.json --audit
python3 scripts/build_banco_tipos.py templates/banco-tipos.json --summary
```

## Definition of Done (tipo)

`id`, `nome`, `formato`, `temperatura`, `objetivo_funil`, `hipotese`, `componentes_obrigatorios` (lista não vazia), **≥1** `referencias_benchmark`, `variacoes` com A/B/C preenchidas, `dod_checklist` objetivo.

## Definition of Done (catálogo — playbook)

Taxonomia preenchida; **≥10** tipos em `ativo` ou equivalente com DoD do tipo; **≥1** entrada de change log após primeira versão estável (ou registro explícito “baseline v1”).

## Artefatos

- `reference.md`
- `templates/tipo-criativo.md`
- `templates/banco-tipos.md`
- `templates/banco-tipos.json`
- `scripts/build_banco_tipos.py`
