# CHANGELOG — deck-entrega-final

---

## [2.0.0] — 2026-05-07 — MAJOR

**Contexto:** Três iterações de apresentação HTML para Alisson Joias revelaram que o design anterior (baseado em CSS customizado do zero) produzia slides com conteúdo mal escalonado, texto pequeno, contraste ruim e layout que ocupava apenas a parte superior da tela. O operador Jhonatan Mayer solicitou descarte completo das diretrizes anteriores e reinício baseado no arquivo de referência `projects/alisson-joias-full/referencia/treinamento_postura_vendas.html`, que é o design system oficial V4.

**O que mudou:**

### Adicionado
- **Template base obrigatório:** `treinamento_postura_vendas.html` — não reinventar design
- 6 tipos de slide documentados com HTML de referência: `slide-cover`, `slide-section`, `slide-content`, `slide-content-alt`, `slide-quote`, `slide-close`
- 5 componentes de conteúdo documentados: `layers` (sequência/hierarquia), `two-col` (comparação), `grid-list` (grade de itens), `callout` (insight destacado), `big-number` (métrica de impacto)
- Tabela de mapeamento MD → Slides (seção do diagnóstico → tipo de slide → componente)
- Checklist de auto-validação (10 itens) antes de salvar
- Paleta de cores completa da referência (`--v4-red`, `--v4-black`, `--v4-dark`, etc.)
- Especificação tipográfica completa: cover 80px/900, slide title 48px/900, body 16px/400, tag 10px/700
- Layout: `padding: 80px 100px`, max-width 700–900px, opacity transitions (não display switching)
- Regras de ritmo narrativo: slides de section a cada 4–5 slides, quotes a cada 6–7
- Output piloto: 26 slides para Alisson Joias

### Modificado
- Princípio de design: de "preencher o slide" para "conteúdo máx 700–900px — espaço em branco é intencional"
- Navegação: dots laterais + botões prev/next circulares na base + teclas ← → Espaço + progress bar topo 2px

### Removido
- Todas as diretrizes anteriores de layout e componentes customizados
- Uso de `display: none/flex` para transição de slides (substituído por `opacity`)
- Qualquer uso de `position: fixed` dentro de slides

---

## [1.0.0] — 2026-04-27

Versão inicial. Geração de HTML navegável com CSS customizado. Diretrizes sem referência ao design system V4. Output com problemas de escalonamento, contraste e tipografia.
