# Referência de Design — Bold / Alto Impacto para Produto Físico

## O que significa Bold / Alto Impacto

Bold não é "colorido demais". É:
- **Hierarquia violenta**: o que é importante é obviamente maior
- **Contraste extremo**: preto sobre branco, branco sobre primária saturada
- **Tipografia como elemento visual**: headline grande o suficiente para ser arte
- **Zero ruído**: cada elemento existe por uma razão

---

## Paletas curadas para produto físico

### Dark Premium (produto premium, cosmético, moda)
- Fundo: `#0A0A0A`
- Texto: `#F5F5F5`
- Primária: `#C8A96E` (ouro)
- Destaque/CTA: `#FFFFFF`
- Acento: `#2D2D2D` (cards)

### Energy Bold (suplemento, esporte, fitness)
- Fundo: `#111111`
- Texto: `#FFFFFF`
- Primária: `#FF3D00` (laranja quente)
- Destaque/CTA: `#FF3D00`
- Acento: `#1A1A1A`

### Clean Impact (produto de saúde, skincare, bebê)
- Fundo: `#FFFFFF`
- Texto: `#111111`
- Primária: `#1A1A1A`
- Destaque/CTA: `#0057FF` (azul forte — mas customizado, não blue-600 do Tailwind)
- Acento: `#F4F4F4`

### Vivid Commerce (e-commerce geral, produto jovem)
- Fundo: `#FFFFFF`
- Texto: `#111111`
- Primária: cor do logo do usuário
- Destaque/CTA: primária com saturação máxima
- Acento: `#F7F7F7`

---

## Tipografia Bold — combinações por nicho

### Produto premium / moda / cosmético
- Display: `Playfair Display` (weight 700-900) ou `Cormorant Garamond Bold`
- Body: `Inter` ou `DM Sans`

### Esporte / fitness / suplemento
- Display: `Barlow Condensed` (weight 800) ou `Bebas Neue`
- Body: `Inter` ou `Roboto`

### Produto de saúde / bem-estar
- Display: `Sora` (weight 700) ou `Plus Jakarta Sans Bold`
- Body: `Sora` Regular ou `DM Sans`

### E-commerce geral / produto jovem
- Display: `Space Grotesk` (weight 700) ou `Outfit Bold`
- Body: `Space Grotesk` ou `Outfit`

---

## Layout do Hero para Produto Físico

### Opção 1 — Split (produto + copy lado a lado)
```
[ HEADLINE GRANDE ]  |  [  FOTO DO PRODUTO  ]
[ subheadline      ]  |  [  em destaque      ]
[ CTA PRIMÁRIO     ]  |
```
Melhor para produtos com visual forte (embalagem bonita, hardware, moda).

### Opção 2 — Centered com produto embaixo
```
        [ HEADLINE GIGANTE ]
        [ subheadline ]
        [ CTA PRIMÁRIO ]
   [ produto centralizado em destaque ]
```
Melhor para hero dark com produto em mockup ou fundo removido.

### Opção 3 — Tipográfico (sem foto no hero)
```
        [ HEADLINE EM TIPOGRAFIA GRANDE ]
        [ subtítulo com dado de prova social ]
        [ CTA ] [ badge de prova ]
```
Usar quando não há foto profissional do produto. Compensar com seção de produto imediatamente abaixo.

---

## Anti-padrões visuais (nunca no prompt gerado)

- Gradiente `from-purple-600 to-blue-500` no hero
- Blob SVG decorativo flutuando atrás do produto
- Grid de ícones Zap + Shield + Rocket para features
- Stock photo de "mulher sorrindo segurando produto"
- Background de "bolhas" ou "ondas" genéricas
- Três seções seguidas com o mesmo fundo branco sem contraste
- Texto de feature com fonte tamanho 14px perdida em card pequeno
- Botão CTA menor que o logo da navbar

---

## Ícones Lucide recomendados por tipo de benefício

Use ícones que conectam semanticamente — não os 3 mais populares:

- Entrega / Prazo: `truck`, `package`, `clock`
- Qualidade / Material: `gem`, `layers`, `shield-check`
- Resultado / Eficiência: `trending-up`, `zap` (apenas se for velocidade real), `target`
- Sustentabilidade: `leaf`, `recycle`, `globe`
- Garantia: `badge-check`, `award`, `star`
- Suporte / Atendimento: `headphones`, `message-circle`, `users`
- Personalização: `sliders`, `settings-2`, `palette`
- Exclusividade: `lock`, `key`, `crown`
