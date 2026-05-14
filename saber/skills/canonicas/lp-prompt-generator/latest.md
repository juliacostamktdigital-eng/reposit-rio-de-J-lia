---
slug: lp-prompt-generator
name: lp-prompt-generator
description: Gera prompts ultra-detalhados e otimizados para criar Landing Pages de produto físico/e-commerce com foco em captura de leads, estilo Bold/Alto Impacto. Use SEMPRE que o usuário mencionar "gerar prompt de LP", "prompt para landing page", "quero criar uma LP", "montar prompt de página de vendas", "preciso de um prompt para landing page", "prompt para Claude Design", ou quando o usuário fornecer briefing de produto + copy + design system e quiser um prompt pronto para colar em outra sessão do Claude. Acione também quando o usuário disser "me ajuda a montar o prompt", "como faço o prompt da minha LP", "gera o prompt completo". O output desta skill é SEMPRE um bloco de prompt otimizado — não a LP em si.
---

# LP Prompt Generator — Produto Físico + Captura de Leads

Esta skill **não cria a Landing Page**. Ela gera um **prompt completo e otimizado** para ser colado no Claude (Design ou qualquer sessão), que então criará a LP com máxima qualidade.

A regra número um: **o prompt gerado deve ser tão específico que o Claude receptor não precise adivinhar nada**. Tudo que for ambíguo no briefing vira pergunta antes de gerar.

---

## Quando usar esta skill

- Usuário tem briefing de produto físico / e-commerce
- Usuário quer capturar leads (email, WhatsApp, contato)
- Usuário tem copy pronta (headline, benefícios, CTAs)
- Usuário tem design system (logo, paleta, tipografia)
- Usuário quer o prompt para colar em outra sessão Claude

---

## Workflow

### Etapa 1 — Coletar o briefing completo

Peça **tudo de uma vez**, em bloco único. Nunca faça perguntas separadas.

> "Para gerar um prompt que entregue uma LP de alto impacto sem precisar de ajustes, preciso de três blocos de informação. Me passa o que tiver:
>
> **[PRODUTO]**
> - Nome do produto e categoria
> - O que ele faz / resolve (seja específico — evite "melhora sua vida")
> - Público-alvo ideal (quem compra, faixa etária, contexto de uso)
> - Diferenciais reais (por que é melhor que concorrentes — número, velocidade, material, garantia…)
> - Preço ou faixa de preço (ajuda a posicionar o tom)
>
> **[COPY]**
> - Headline principal (a frase mais importante da página)
> - Subheadline ou argumento de reforço
> - 3 a 6 benefícios principais (pode ser lista)
> - Texto ou proposta do formulário de captura (ex: "Receba desconto de lançamento")
> - CTA principal (ex: "Quero garantir o meu", "Receber oferta exclusiva")
> - Depoimentos disponíveis (nome + cargo/contexto + citação específica)
>
> **[DESIGN SYSTEM]**
> - Cores primárias (hex ou nome)
> - Fonte(s) usadas
> - Logo disponível? (sim/não — se sim, descreva o estilo: minimalista, serif, símbolo…)
> - Referências de sites ou marcas que gosta visualmente
> - Alguma regra de identidade que o Claude deve respeitar"

Se o usuário não tiver algum item, **marque como `[PLACEHOLDER]`** no prompt gerado e instrua o Claude receptor a preencher de forma coerente com o restante.

---

### Etapa 2 — Validar antes de gerar

Antes de montar o prompt, faça este checklist internamente:

- [ ] Produto está claro o suficiente para uma LP específica (não genérica)?
- [ ] Há pelo menos 1 diferencial verificável (número, prazo, material, exclusividade)?
- [ ] O objetivo de captura de leads está claro (tipo de formulário, incentivo)?
- [ ] Existe paleta de cores definida?
- [ ] A headline fornecida é específica ou poderia servir pra qualquer produto?

Se a headline for genérica ("Transforme sua rotina"), **avise o usuário e sugira uma versão mais específica** antes de continuar.

---

### Etapa 3 — Montar o prompt otimizado

O prompt gerado deve seguir **exatamente esta estrutura**. Copie, preencha e entregue:

---

```
# PROMPT PARA LANDING PAGE — [NOME DO PRODUTO]

## CONTEXTO E OBJETIVO
Crie uma Landing Page de alta conversão para captura de leads do produto [NOME].
Estilo visual: Bold / Alto Impacto — tipografia grande, contraste forte, hierarquia clara, zero elementos decorativos sem função.
Output: HTML + Tailwind single-file, mobile-first, pronto para publicar.

---

## PRODUTO
- **Nome**: [nome]
- **Categoria**: [categoria]
- **O que resolve**: [descrição objetiva do problema e solução — 2 linhas max]
- **Público-alvo**: [quem é, contexto de uso]
- **Diferenciais**: [lista com bullet points — verificáveis, sem "qualidade" ou "excelência"]
- **Preço**: [valor ou "a revelar no formulário"]

---

## COPY FORNECIDA (use sem alterar, exceto onde marcado como [adaptar])

### Hero
- **Headline**: [headline exata]
- **Subheadline**: [subheadline exata]
- **CTA primário**: [texto exato do botão]

### Benefícios / Features
[lista exata dos benefícios fornecidos]

### Formulário de Captura
- **Proposta de valor**: [o que o usuário ganha ao deixar o contato]
- **Campos**: [nome, email, whatsapp — o que for]
- **CTA do formulário**: [texto exato]

### Depoimentos
[depoimento 1: nome + contexto + citação]
[depoimento 2: nome + contexto + citação]
[depoimento 3: nome + contexto + citação]
Se não houver depoimentos reais, crie 3 plausíveis para o nicho e marque como [PLACEHOLDER — substituir por reais].

---

## DESIGN SYSTEM

### Paleta
- **Primária**: [hex]
- **Secundária**: [hex ou "derivar da primária"]
- **Fundo**: [hex ou "preto / branco / neutro escuro"]
- **Texto**: [hex]
- **Destaque / CTA**: [hex — geralmente a cor de maior contraste]

### Tipografia
- **Display (headlines)**: [fonte — geralmente bold, condensada ou slab]
- **Body**: [fonte — leitura fácil]
- Fonte do Google Fonts. Importe via link no head.

### Logo
[descrição do logo ou "sem logo — usar nome tipográfico"]

### Regras de identidade
[lista de regras que devem ser respeitadas — bordas, ícones, espaçamento, etc.]

---

## ESTRUTURA OBRIGATÓRIA DA LP

Implemente exatamente estas seções, nesta ordem:

1. **Navbar** — logo/nome + CTA âncora. Sem menu completo.
2. **Hero** — headline grande (≥64px desktop), subheadline, CTA primário, visual de impacto (produto em destaque ou composição tipográfica bold — sem blob abstrato, sem gradiente roxo/azul, sem stock photo genérico).
3. **Prova social rápida** — 3 números ou selos de credibilidade do produto (ex: "4.9★ avaliação", "3.000 unidades vendidas", "Garantia de 30 dias").
4. **Benefícios** — 3 a 6 cards bold. Cada card: ícone semântico (Lucide) + título curto + 1 frase de benefício real.
5. **Produto em detalhe** — seção com foto/mockup grande do produto + lista de especificações ou diferenciais técnicos.
6. **Formulário de captura** — seção destacada com proposta de valor clara + formulário simples (nome + email/whatsapp) + CTA. Fundo de cor primária ou dark.
7. **Depoimentos** — 3 cards com nome, contexto/cargo, citação específica (não vazia).
8. **FAQ** — 5 perguntas que eliminam objeções reais do nicho (não genéricas).
9. **CTA final** — bloco de fechamento com headline de urgência/escassez plausível + botão grande.
10. **Footer** — nome da marca, links mínimos (política de privacidade, contato), redes sociais se houver.

---

## REGRAS DE IMPLEMENTAÇÃO

### Visual Bold / Alto Impacto
- Headlines do hero em peso 800-900, tamanho ≥64px desktop / ≥40px mobile
- Contraste forte: nunca texto cinza médio sobre fundo branco
- Uso de cor primária de forma agressiva (botões, destaques, backgrounds de seção)
- Seções alternando fundo claro/escuro para ritmo visual
- Zero gradiente roxo→azul aleatório
- Zero blob SVG decorativo

### Técnico
- HTML + Tailwind CDN, single-file
- tailwind.config com cores customizadas (nunca blue-600 puro)
- Google Fonts importada no head
- Lucide via CDN — lucide.createIcons() no final do body
- Mobile-first — breakpoints sm/md/lg
- Navbar com hamburger menu em mobile (toggle JS)
- Smooth scroll em âncoras
- Formulário com validação básica de JS (campo obrigatório)
- Zero lorem ipsum
- Zero console.log
- Alt text descritivo em todas as imagens
- Contraste WCAG AA mínimo

### Imagens
- Hero: mockup real do produto (use placeholder descritivo: `https://placehold.co/800x600?text=Foto+Produto`) ou composição tipográfica sem imagem
- Produto em detalhe: placeholder com instrução clara de troca
- Nenhum stock photo de "pessoa feliz genérica"

---

## PLACEHOLDERS PARA SUBSTITUIÇÃO
Ao finalizar, liste todos os elementos que precisam ser trocados pelo cliente:
- [ ] Foto real do produto no hero
- [ ] Foto(s) do produto na seção de detalhes
- [ ] Logo em alta resolução
- [ ] Depoimentos reais (se foram criados como placeholder)
- [ ] Link real do formulário (webhook, Mailchimp, etc.)
- [ ] Links de redes sociais
- [ ] Política de privacidade

---

## O QUE NUNCA FAZER
- Headlines genéricas ("A solução ideal para você")
- CTA "Saiba mais"
- Depoimentos: "Excelente!" sem mais contexto
- Features: Rápido / Seguro / Confiável sem contexto real
- Gradiente roxo-azul no hero
- Navbar com 7+ links
- Footer institucional gigante
```

---

### Etapa 4 — Entregar o prompt

Entregue o prompt em **bloco de código Markdown** para facilitar a cópia. Depois do bloco:

1. Resumo em 3 linhas do que foi preenchido vs. o que ficou como placeholder
2. Aviso sobre qualquer decisão criativa tomada (ex: "Criei 3 depoimentos placeholder pois não foram fornecidos")
3. Instrução direta: **"Cole esse prompt em uma nova conversa no Claude para gerar sua LP."**

---

## Anti-padrões desta skill

Nunca:
- Gerar a LP diretamente (a skill gera o prompt, não a página)
- Fazer perguntas uma por uma (sempre em bloco único)
- Aceitar headline genérica sem alertar o usuário
- Pular o design system — cores e fontes são obrigatórias no prompt
- Inventar um nicho ou produto sem dados do usuário
- Gerar prompt sem a seção de formulário de captura (é o objetivo central da LP)
