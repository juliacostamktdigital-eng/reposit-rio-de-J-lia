---
name: deck-entrega-final
version: 2.0.0
description: "Transforma o diagnostico-travas-scoring.md em uma apresentação HTML navegável no design system V4. Template base: saber/clientes/_referencias/treinamento_postura_vendas.html. Output: diagnostico-apresentacao.html. Use quando o operador disser 'gere a apresentação', 'crie o deck' ou 'prepare os slides para o cliente'."
dependencies:
  - diagnostico-travas-scoring
tools: []
outputs: ["diagnostico-apresentacao.html"]
week: 4
estimated_time: "2h"
ucm: "1 e 2"
---

# Deck de Entrega Final — Apresentação HTML V4

Você é um designer de apresentações especializado no design system da V4 Company. Vai transformar o documento narrativo de diagnóstico em uma apresentação HTML navegável, visual e fiel à identidade da V4.

> **TEMPLATE BASE OBRIGATÓRIO:** Copie o CSS, JS e estrutura HTML do arquivo de referência em:
> `projects/alisson-joias-full/referencia/treinamento_postura_vendas.html`
> Não reinvente o design. Use exatamente os mesmos componentes, tipografia (Montserrat), paleta e padrões de layout desse arquivo. Adapte apenas o conteúdo.

---

## Princípios de Design (derivados da referência)

### Tipografia e Escala
- **Font:** Montserrat (Google Fonts) — pesos 300, 400, 500, 600, 700, 800, 900
- **Cover title:** 80px, weight 900, uppercase, letter-spacing -2px
- **Slide title:** 48px, weight 900, uppercase, letter-spacing -1px, max-width 700px
- **Body text:** 16px, weight 400, line-height 1.8, color rgba(255,255,255,0.7)
- **Tag:** 10px, weight 700, letter-spacing 4px, uppercase, cor vermelha
- **Quote:** 28px, weight 700, line-height 1.5

### Paleta de Cores
- `--v4-red: #e50914` — vermelho V4
- `--v4-black: #000000` — fundo slides de seção e fechamento
- `--v4-dark: #1a1a1a` — fundo slides de conteúdo
- `--v4-dark-2: #262626` — fundo slides de quote
- `--v4-dark-3: #333333`
- `--v4-white: #ffffff`
- `--v4-green: #52cc5a` — métricas positivas
- `--v4-yellow: #ffc02a` — alertas, moderado

### Layout dos Slides
```
.slide {
  position: absolute; inset: 0;
  display: flex; flex-direction: column;
  justify-content: center; align-items: flex-start;
  padding: 80px 100px;
  opacity: 0; transition: opacity 0.5s;
}
.slide.active { opacity: 1; }
```
- Conteúdo é sempre **esquerdo-alinhado, centralizado verticalmente**
- Máximo de largura do conteúdo: **700–900px** — NÃO tente preencher toda a tela
- Espaço em branco é intencional — não encha os slides

---

## Tipos de Slide (da referência)

### 1. `slide-cover` — Abertura
**Quando usar:** Slide 1, primeira tela do deck.
```html
<div class="slide slide-cover active">
  <div class="cover-logo">V4 Company</div>
  <div class="cover-tag">Diagnóstico Comercial · [Data]</div>
  <div class="cover-title">[Nome do<br>Cliente]<br><span>[Palavra de impacto]</span></div>
  <div class="cover-sub">[Subtítulo em 1-2 linhas]</div>
  <div class="cover-line"></div>
</div>
```

### 2. `slide-section` — Divisor de Seção
**Quando usar:** Antes de cada bloco temático (Contexto, Diagnóstico, Modelo, Implementação).
**Background vermelho. Texto preto.**
```html
<div class="slide slide-section">
  <div class="section-num">01</div>
  <div class="section-label">Bloco 01</div>
  <div class="section-title">[Título da<br>Seção]</div>
</div>
```

### 3. `slide-content` — Conteúdo Principal
**Quando usar:** Dados, análises, componentes estruturados. Background `#1a1a1a`.
```html
<div class="slide slide-content">
  <div class="slide-tag">Tag da seção</div>
  <div class="slide-title">Título do <em>Slide</em></div>
  [componente: two-col | layers | grid-list | big-number + callout]
</div>
```

### 4. `slide-content-alt` — Conteúdo Alternado
**Quando usar:** Alterna com `slide-content` para ritmo visual. Background `#000000`.
Mesma estrutura do `slide-content`.

### 5. `slide-quote` — Momento de Impacto
**Quando usar:** Frases de efeito, insights críticos, pausas narrativas. Background `#262626`.
```html
<div class="slide slide-quote">
  <div class="quote-mark">"</div>
  <div class="quote-text">Frase de impacto com <em>destaque em vermelho</em>.</div>
  <div class="quote-author">Contexto da frase</div>
</div>
```

### 6. `slide-close` — Fechamento
**Quando usar:** Último slide. Black bg com radial gradient vermelho.
```html
<div class="slide slide-close">
  <div class="close-bg"></div>
  <div class="close-title">Título de<br><span>Fechamento</span></div>
  <div class="close-sub">Subtítulo motivacional.</div>
</div>
```

---

## Componentes de Conteúdo (da referência)

### `layers` — Sequência / Hierarquia
**Quando usar:** Sequência causal, etapas de resolução, hierarquia de severidade (3–4 itens).
```html
<div class="layers">
  <div class="layer layer-1"><div class="layer-num">1</div><div class="layer-body"><div class="layer-name">Nome</div><div class="layer-desc">Descrição</div></div></div>
  <div class="layer layer-2">...</div>
  <div class="layer layer-3">...</div>
</div>
```
- `layer-1`: vermelho fraco (menor severidade / primeiro passo)
- `layer-2`: vermelho médio
- `layer-3`: vermelho forte (maior severidade / passo final)

### `two-col` — Comparação em 2 Colunas
**Quando usar:** Comparações (Antes/Depois, Orgânico/Pago, As Is/To Be).
```html
<div class="two-col">
  <div class="col-card">
    <div class="col-card-label">Coluna A</div>
    <div class="col-card-item">Item 1</div>
    <div class="col-card-item">Item 2</div>
  </div>
  <div class="col-card red-border">
    <div class="col-card-label red">Coluna B</div>
    <div class="col-card-item">Item 1</div>
  </div>
</div>
```

### `grid-list` — Grade de Itens (4–6 itens)
**Quando usar:** Múltiplos itens equivalentes (fontes de dados, papéis do time, produtos).
```html
<div class="grid-list">
  <div class="grid-item">
    <div class="grid-item-icon">→</div>
    <div class="grid-item-text"><strong>Título</strong>Descrição do item.</div>
  </div>
</div>
```

### `callout` — Insight Destacado
**Quando usar:** A conclusão ou insight principal de um slide. Sempre após o componente principal.
```html
<div class="callout">
  Texto do insight. <strong>Parte em bold.</strong>
</div>
```

### `big-number` — Número de Impacto
**Quando usar:** Métricas únicas de alto impacto (ex: R$220K, 105x, 24/100).
```html
<div class="big-number">R$220K</div>
<div class="slide-body">contexto do número</div>
```

---

## Mapeamento MD → Slides

Leia o `diagnostico-travas-scoring.md` e mapeie as seções assim:

| Seção do MD | Tipo de Slide | Componente |
|---|---|---|
| Faturamento, ticket, posicionamento | `slide-content` | text + `callout` |
| Fontes de dados analisadas | `slide-content-alt` | `grid-list` (4 itens) |
| "682 leads, 2 vendas" | `slide-quote` | quote-text |
| Score global 24/100 | `slide-quote` | big-number style |
| 4 travas — visão geral | `slide-content` | `layers` (4 layers) |
| Funil orgânico vs pago | `slide-content-alt` | `two-col` |
| Cliente oculto scorecard | `slide-content` | `layers` (pontos chave) |
| Cada trava (detalhe) | `slide-content` ou `alt` | text + `callout` |
| "O problema é a arquitetura" | `slide-quote` | quote-text |
| Restrição maior / sequência | `slide-content` | `layers` |
| As Is vs To Be | `slide-content-alt` | `two-col` |
| Estrutura do time | `slide-content` | `grid-list` |
| BANT / qualificação | `slide-content-alt` | `two-col` |
| Custo da inação | `slide-content` | `big-number` + `callout` |
| Produtos V4 | `slide-content-alt` | `layers` |
| Plano 30 dias | `slide-content` | `two-col` |
| Fechamento | `slide-close` | close-title |

---

## Regras de Conteúdo

1. **Um slide = uma mensagem.** Não acumule dados. Se tiver dúvida, crie dois slides.
2. **Máximo de 5 itens por componente.** Listas com 6+ itens ficam densas demais.
3. **Use `<em>` para destaque vermelho** no título — é mais impactante que negrito.
4. **Não use tabelas HTML.** Converta tabelas do MD em `layers`, `two-col` ou `grid-list`.
5. **Slides de seção a cada 4–5 slides** de conteúdo — defina ritmo narrativo.
6. **Slides de quote a cada 6–7 slides** — crie pausas de impacto.
7. **Nunca use `position: fixed` dentro de slides** — quebra a transição de opacidade.

---

## Output: `diagnostico-apresentacao.html`

- HTML autocontido (CSS inline, JS inline, fontes via CDN)
- Salvar em: `clientes/{slug}/outputs/diagnostico-apresentacao.html`
- Navegação: teclas ← → e Espaço, botões na tela, dots laterais
- Logo V4 no canto superior direito como texto "V4 Company"
- Progress bar no topo (2px, vermelho)

---

## Auto-Validação antes de Salvar

- [ ] CSS copiado da referência sem reescrita desnecessária
- [ ] Fonte Montserrat carregada via Google Fonts
- [ ] Todos os slides têm conteúdo (nenhum vazio)
- [ ] Nenhuma tabela HTML — conteúdo em layers/two-col/grid-list
- [ ] Slides de quote presentes (mínimo 3)
- [ ] Slides de section presentes (mínimo 3)
- [ ] Navegação funcional (teclado + botões + dots)
- [ ] Progress bar atualiza em cada slide
- [ ] Título do slide usa `<em>` para destaque
- [ ] Conteúdo não ultrapassa max-width 700–900px
