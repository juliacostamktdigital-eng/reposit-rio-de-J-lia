---
slug: design-system-pro
name: design-system-pro
description: >
  Cria design systems profissionais completos para Figma a partir de screenshots de referência, logo e tipografia fornecidos pelo usuário. Use esta skill SEMPRE que o usuário mencionar "design system", "design tokens", "styleguide", "style guide", "sistema de design", "tokens de design", "shadcn", "componentes UI", ou quando o usuário enviar uma imagem de referência visual (de Dribbble, Behance, Pinterest, Figma, etc.) e quiser transformá-la em um sistema de design. Também acione quando o usuário pedir para "extrair cores", "criar paleta a partir de uma imagem", "montar um tema", ou "exportar para Figma". A skill cobre o fluxo completo: o usuário entrega print de referência + logo + tipografia → análise visual → extração de tokens → preview HTML para aprovação → exportação direta para o Figma. Mesmo que o usuário só envie uma imagem e diga "quero algo assim", assuma que ele quer o design system completo e use esta skill.
---

# Design System PRO

Skill para criar design systems profissionais com saída para o Figma. O usuário entrega os insumos (print de referência, logo e tipografia) e recebe um design system completo exportado diretamente para o Figma.

## Idioma

Todas as interações com o usuário devem ser em **Português (BR)**. Código e nomes de variáveis/tokens permanecem em inglês (padrão da indústria).

---

## Fluxo Principal

```
INSUMOS DO USUÁRIO          PROCESSAMENTO              SAÍDA
─────────────────          ──────────────              ─────
1. Print de referência  →  Análise visual          →  Preview HTML
2. Logo (arquivo)       →  Extração de tokens         (aprovação)
3. Tipografia (nome)    →  Geração do sistema      →  FIGMA
```

### Os 3 insumos obrigatórios

Antes de iniciar qualquer trabalho, colete do usuário:

1. **Print de referência** — Screenshot ou imagem de inspiração (Dribbble, Behance, Pinterest, site, app, etc.). É a referência visual principal de onde serão extraídos cores, espaçamento, raios e estilo geral.

2. **Logo** — Arquivo da logo da marca (PNG, SVG, ou qualquer formato de imagem). Será usada para extrair cores da marca caso não estejam evidentes no print, e será incluída no design system do Figma.

3. **Tipografia** — Nome da(s) fonte(s) que o projeto usa. O usuário informa diretamente (ex: "Inter", "Poppins", "Montserrat + Lora"). Não tente adivinhar pela imagem — peça explicitamente.

Se o usuário não fornecer algum dos 3, pergunte antes de prosseguir:

> "Para montar o design system, preciso de 3 coisas:
> 1. **Print de referência** — uma imagem/screenshot com o visual que você quer seguir
> 2. **Logo** — o arquivo da logo da marca
> 3. **Tipografia** — o nome da(s) fonte(s) do projeto
>
> O que está faltando?"

---

## Fase 1: Coleta e Análise

### Passo 1: Receber e Validar Insumos

Confirme que tem os 3 insumos. Resuma o que recebeu para o usuário confirmar:

> "Recebi tudo:
> - **Referência:** [descreva brevemente a imagem]
> - **Logo:** [nome do arquivo]
> - **Tipografia:** [nome(s) da(s) fonte(s)]
>
> Vou analisar e montar o design system. Pode confirmar?"

### Passo 2: Análise Visual da Referência

Olhe para a imagem de referência e extraia:

**Cores (a partir do print + logo):**
- Cor primária/marca → identifique a partir da logo e do print. Gere escala completa (50-900)
- Cor secundária (se presente) → gere escala completa (50-900)
- Cores neutras/cinzas → gere escala completa (50-900)
- Cores semânticas: success (verde), error (vermelho), warning (amarelo/laranja), info (azul)
- Cores de fundo, superfície, borda

**Estilo Visual (a partir do print):**
- Ritmo de espaçamento (apertado, normal, relaxado)
- Estilo de border-radius (reto 0px, levemente arredondado 4-6px, arredondado 8-12px, pílula 999px)
- Estilo de sombra (nenhuma, sutil, proeminente)
- Tom geral (minimalista, corporativo, ousado, amigável, elegante, etc.)

**Tipografia (a partir do insumo do usuário):**
- Fonte principal: a que o usuário informou
- Definir escala tipográfica: h1 a h6 (tamanhos + pesos), body (regular, small, xs), labels
- Se o usuário informou 2 fontes: definir qual é para headings e qual para body

Quando as cores não forem claramente visíveis, faça inferências razoáveis. Garanta contraste WCAG 4.5:1 para texto. Gere escalas harmoniosas usando teoria de cores.

### Passo 3: Apresentar Resumo do Design

Antes de gerar o preview, apresente um resumo rápido para alinhamento:

- **Cor primária:** [hex e nome descritivo]
- **Cor secundária:** [hex, se houver]
- **Fonte principal:** [nome]
- **Fonte secundária:** [nome, se houver]
- **Estilo:** [ex: "Moderno minimalista", "Corporativo elegante"]
- **Border radius:** [ex: "Arredondado 8px"]
- **Sombras:** [ex: "Sutis, com blur leve"]
- **Sensação geral:** [descrição em 1 linha]

---

## Fase 2: Preview para Aprovação

### Passo 4: Gerar Preview HTML

Gere um **arquivo HTML standalone** (`design-system-preview.html`) visualmente polido e profissional. Esse é o artefato que o usuário vai avaliar antes de exportar para o Figma.

O HTML deve ser **auto-contido** (CSS inline, sem dependências externas exceto Google Fonts) e incluir:

**Seção 1 — Identidade**
- Logo exibida (se for imagem acessível)
- Nome do projeto / marca
- Fontes utilizadas

**Seção 2 — Paleta de Cores**
- Escala primária (50-900) como swatches com hex
- Escala secundária (se houver)
- Escala de neutros (50-900)
- Cores semânticas (success, warning, error, info) com swatches

**Seção 3 — Tipografia**
- Escala tipográfica completa (H1 a H6, body, small, label)
- Cada nível com: nome, tamanho, peso, e texto de exemplo

**Seção 4 — Espaçamento e Raios**
- Exemplos visuais de border-radius
- Exemplos de sombras aplicadas em cards

**Seção 5 — Componentes Base**
- Botões (primary, secondary, outline, ghost, destructive) em diferentes tamanhos
- Cards com conteúdo exemplo
- Badges / Tags
- Alertas (info, success, warning, error)
- Inputs e form elements básicos

**Seção 6 — Dark Mode**
- Toggle funcional para alternar entre light e dark
- Todo o preview deve funcionar nos dois modos

**Qualidade visual:** O preview deve parecer um styleguide profissional. Use grid limpo, espaçamento generoso, hierarquia visual clara. O usuário vai decidir se aprova baseado nesse preview, então capriche.

### Passo 5: Apresentar para Aprovação

Salve o HTML no diretório de outputs e apresente ao usuário:

> "Aqui está o preview do seu design system. Revise as cores, tipografia e componentes. Se estiver tudo certo, eu exporto direto para o Figma. Se quiser ajustes, me diga o que mudar."

- **Se aprovar** → prossiga para a Fase 3 (Exportação Figma)
- **Se pedir ajustes** → faça as alterações, gere novo HTML, apresente novamente
- **Itere quantas vezes for necessário** até o usuário aprovar

---

## Fase 3: Exportação para Figma

Após aprovação do preview, exporte o design system completo para o Figma.

### Passo 6: Verificar Método de Exportação

**Opção A — MCP do Figma conectado:**
Se o MCP do Figma (`mcp.figma.com`) estiver disponível nas ferramentas, use-o diretamente:
- `create_design_system_rules` para criar as regras do design system
- Outras ferramentas do MCP conforme necessário

**Opção B — Script Figma Plugin API (padrão):**
Se o MCP não estiver conectado, gere um script JavaScript completo para a Figma Plugin API. Consulte `references/figma-export.md` para o template e padrões.

### Passo 7: Gerar Exportação Figma

O script/exportação deve criar no Figma:

**1. Color Styles** (organizados hierarquicamente com `/`):
```
Primary/50, Primary/100, ..., Primary/900
Secondary/50, Secondary/100, ..., Secondary/900  (se houver)
Neutral/50, Neutral/100, ..., Neutral/900
Semantic/Success, Semantic/Warning, Semantic/Error, Semantic/Info
Surface/Background, Surface/Card, Surface/Muted
Border/Default, Border/Input
```

**2. Text Styles:**
```
Heading/H1, Heading/H2, Heading/H3, Heading/H4, Heading/H5, Heading/H6
Body/Large, Body/Regular, Body/Small, Body/XSmall
Label/Large, Label/Regular
```
Cada text style com: font family (a tipografia informada), size, weight, line-height.

**3. Effect Styles** (sombras):
```
Shadow/SM, Shadow/MD, Shadow/LG, Shadow/XL
```

**4. Variables (Design Tokens):**
- Coleção "Design Tokens" com modos Light e Dark
- Variáveis de cor para: background, foreground, primary, secondary, muted, accent, destructive, border, input, ring, success, warning, info (e seus foregrounds)
- Variável de número para border-radius

**5. Logo:**
- Incluir instrução para o usuário importar a logo manualmente no Figma (a Plugin API não importa arquivos externos diretamente)

### Passo 8: Entregar ao Usuário

Se usou script (Opção B), entregue o arquivo `.js` e as instruções de uso:

> "Seu design system está pronto para o Figma! Aqui está o script:
>
> **Como usar:**
> 1. Abra o Figma Desktop
> 2. No arquivo de destino, vá em **Plugins > Development > New Plugin**
> 3. Selecione 'Figma design' e 'Empty'
> 4. Cole o conteúdo do script no arquivo `code.ts`
> 5. Execute o plugin
>
> O script vai criar automaticamente: [X] color styles, [X] text styles, [X] effect styles e [X] variables com modos Light/Dark."

---

## Prompt 2: Desenvolvimento de Componentes

Após o design system base estar no Figma, o usuário pode pedir componentes adicionais. Cada componente segue este fluxo:

### Fluxo do Componente

1. **Verificar no shadcn** — Busque se existe no registry do shadcn. Se existir, use como referência de estrutura e variantes.

2. **Definir variantes** — Mapeie todas as variantes do componente:
   - Tamanhos (sm, md, lg)
   - Estilos (default, outline, ghost, destructive)
   - Estados (default, hover, focus, disabled, loading)

3. **Gerar Preview HTML** — Adicione o componente ao preview HTML com showcase de todas as variantes.

4. **Aprovação** — Mostre ao usuário, colete feedback.

5. **Exportar para Figma** — Gere o script que cria o componente como Figma component com variantes (usando component properties).

**Componentes comuns:**
- Layout: Card, Separator, Tabs, Accordion
- Forms: Button, Input, Select, Checkbox, Radio, Switch, Textarea
- Feedback: Alert, Toast, Progress, Skeleton, Badge
- Overlay: Dialog, Drawer, Popover, Tooltip, Dropdown Menu
- Navigation: Navigation Menu, Breadcrumb, Pagination
- Data: Table, Avatar, Calendar

---

## Prompt 3: Desenvolvimento de Páginas

Constrói layouts de páginas completas para o Figma baseados em screenshots.

### Fluxo da Página

1. **Receber screenshot** — O usuário sobe o print da página que quer recriar.

2. **Análise visual** — Identifique:
   - Estrutura de layout (colunas, sidebar, header, footer)
   - Seções da página (nomear cada bloco)
   - Componentes usados em cada seção

3. **Mapear para componentes do design system** — Priorize usar componentes que já existem no design system. Liste quais componentes novos precisam ser criados.

4. **Gerar Preview HTML** — Crie a página completa em HTML standalone usando os tokens do design system. Inclua responsividade.

5. **Aprovação** — Apresente ao usuário.

6. **Exportar para Figma** — Gere frames e layouts no Figma usando auto-layout, os color/text styles criados, e os componentes existentes.

---

## Referências

- `references/globals-template.md` — Template completo do CSS com variáveis (útil para o preview HTML)
- `references/figma-export.md` — Templates e padrões para scripts da Figma Plugin API
- `references/styleguide-layout.md` — Templates de layout para styleguide (caso o usuário queira versão Next.js também)

---

## Dicas para Resultados Melhores

- **Extraia cores da logo** quando o print de referência não tiver cores de marca claras — a logo é a fonte mais confiável da identidade visual
- **Gere escalas harmoniosas** usando teoria de cores (análogos, complementares, triádicos)
- **Garanta acessibilidade** com contraste WCAG 4.5:1 para texto e 3:1 para elementos gráficos
- **O preview é o momento da verdade** — invista tempo para deixá-lo visualmente impecável, porque é o que o usuário vai avaliar
- **Não adivinhe a tipografia** — sempre peça ao usuário. Fontes são decisões de marca
- **Dark mode não é opcional** — gere sempre as duas versões (light + dark) dos tokens
- **Organização hierárquica no Figma** — use `/` para criar subgrupos (ex: `Primary/500`) que facilitam a navegação
