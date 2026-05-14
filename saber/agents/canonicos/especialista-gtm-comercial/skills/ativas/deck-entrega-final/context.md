# Context — deck-entrega-final

## Identidade

**Nome:** deck-entrega-final
**Agente owner:** especialista-gtm-comercial
**Status:** ativa
**Versão atual:** 2.0.0

---

## Histórico de Versões

| Versão | Data | Tipo | Resumo |
|--------|------|------|--------|
| 1.0.0 | 2026-04-27 | — | Versão inicial — HTML com CSS customizado, problemas de escalonamento e contraste |
| **2.0.0** | **2026-05-07** | **MAJOR** | **Redesign completo baseado em `treinamento_postura_vendas.html`. Montserrat, opacity transitions, 6 tipos de slide, 5 componentes, mapeamento MD→slides** |

---

## Contextos de Aplicação

| Contexto | Uso | Observações |
|----------|-----|-------------|
| Entrega Final ao cliente (Semana 4) | **Principal** | Transforma `diagnostico-travas-scoring.md` em apresentação de 1h |
| Piloto de referência | Alisson Joias | 26 slides, `saber/clientes/alisson-joias/outputs/diagnostico-apresentacao.html` |

---

## Decisões de Design

**Por que reiniciar com base no `treinamento_postura_vendas.html`?**
Três tentativas de HTML customizado produziram o mesmo problema: conteúdo mal escalonado, texto pequeno, slides que pareciam "quadrados" e ocupavam apenas a parte superior da tela. A causa raiz não era um bug de CSS — era a filosofia de design: tentar preencher o slide vs usar tipografia grande com espaço em branco intencional. O arquivo de referência já resolveu esse problema: `padding: 80px 100px`, títulos de 48–80px, corpo de 16px com `line-height: 1.8`, `max-width: 700px` que nunca preenche a tela toda.

**Por que opacity transitions e não display switching?**
`display: none → flex` causa reflow e não permite animação CSS. `opacity: 0 → 1` com `transition: opacity 0.5s` é suave, não causa reflow e é o padrão do arquivo de referência. `position: fixed` dentro de slides quebra a transição de opacidade — não usar.

**Por que componentes (layers, two-col, grid-list) e não tabelas HTML?**
Tabelas em apresentações geram densidade visual e são difíceis de estilizar para fontes grandes e escuras. Os componentes do design system V4 usam espaçamento, cores e hierarquia visual que comunicam a mesma informação com muito mais impacto. Regra: toda tabela do diagnóstico .md é convertida em um desses componentes.

**Por que max-width 700–900px em slides de 100vw?**
Apresentações lidas em monitor grande têm conteúdo que viaja 2–3 metros até os olhos do apresentador. Linhas de texto que atravessam toda a tela (1920px) são impossíveis de ler de pé. O padrão de 700px — vindo diretamente do arquivo de referência — garante que o texto seja denso o suficiente para criar impacto visual mas curto o suficiente para ser lido sem esforço.

---

## Evidência de Validação

**Piloto:** Alisson Joias — 07/05/2026
**Operador:** Jhonatan Mayer
**Output gerado:** `saber/clientes/alisson-joias/outputs/diagnostico-apresentacao.html` (26 slides)
**Referência de design:** `projects/alisson-joias-full/referencia/treinamento_postura_vendas.html`
