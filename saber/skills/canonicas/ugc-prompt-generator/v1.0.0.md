---
slug: ugc-prompt-generator
name: ugc-prompt-generator
description: Gera prompts ultra-detalhados e cinematográficos para criar vídeos UGC (User Generated Content) realistas com IAs generativas de vídeo como Sora, Veo, Runway, Kling e Pika. Use SEMPRE que o usuário mencionar "prompt UGC", "vídeo UGC", "gerar UGC", "UGC realista", "vídeo de usuário", "conteúdo orgânico", "review de produto em vídeo", "unboxing UGC", "depoimento em vídeo", "testimunho", "vídeo autêntico de produto", "ugc sem parecer IA", "ugc natural", ou quando o usuário fornecer um produto/serviço e quiser um prompt para criar vídeo de usuário real. Acione também quando o usuário disser "quero um vídeo que pareça gravado por um usuário real", "como faço um UGC com IA", "prompt para vídeo orgânico", "simular unboxing", "criar depoimento falso realista". O output desta skill é SEMPRE um bloco de prompt otimizado para IA de vídeo — não o vídeo em si.
---

# UGC Prompt Generator — Vídeos Realistas Sem Parecer IA

## O que é UGC e por que o realismo importa

UGC (User Generated Content) é conteúdo criado por usuários reais — reviews, unboxings, depoimentos, "dia com meu produto", tutoriais casuais. O que torna o UGC eficaz é a **autenticidade percebida**: câmera imperfeita, ambiente bagunçado, iluminação natural inconsistente, pausas naturais na fala, micro-expressões reais.

IAs de vídeo tendem a produzir conteúdo *perfeito demais* — luz uniforme, movimentos suaves, cenário limpo, expressões neutras. Esses elementos destroem a credibilidade do UGC. Esta skill ensina a escrever prompts que combatem exatamente isso.

---

## Processo de criação do prompt

### Passo 1 — Coletar informações do usuário

Antes de gerar o prompt, identifique:

1. **Produto/Serviço**: O que está sendo mostrado? (ex: suplemento, skincare, app, roupa)
2. **Formato do UGC**: Qual tipo de vídeo?
   - Unboxing / primeiro uso
   - Review / depoimento falado
   - "Dia com o produto" / rotina
   - Tutorial rápido / how-to
   - Antes e depois
   - Reação ao resultado
3. **Persona do criador**: Quem está gravando?
   - Idade aproximada, gênero, estilo (universitária, mãe de 30 anos, atleta, executivo)
4. **Ambiente/Contexto**: Onde está gravando?
   - Quarto, banheiro, cozinha, academia, escritório, carro
5. **Tom emocional**: Como a pessoa se sente?
   - Animada / surpresa / aliviada / satisfeita / casual / incrédula
6. **Plataforma de destino**: TikTok, Reels, YouTube Shorts, Story?
7. **Duração aproximada**: 15s, 30s, 60s?
8. **IA de vídeo alvo**: Sora, Veo, Runway, Kling, Pika, Luma?

Se o usuário não fornecer todos, **assuma defaults razoáveis e informe** no prompt gerado.

---

### Passo 2 — Aplicar os 7 Pilares do UGC Realista

Para cada prompt gerado, incorpore obrigatoriamente estes elementos:

#### 🎥 Pilar 1 — Câmera imperfeita
- Handheld shake leve e orgânico (não estabilizado)
- Foco que ajusta levemente no início do plano
- Ângulo ligeiramente torto (1–3 graus)
- Aproximação/afastamento casual da câmera
- Dedos aparecendo brevemente no canto do frame
- Self-mode (frontal), câmera levemente abaixo dos olhos

**Frase-chave para o prompt**: `"handheld smartphone footage, slight natural camera shake, selfie angle, slightly off-center framing, casual reframing mid-shot"`

#### 💡 Pilar 2 — Iluminação natural e imperfeita
- Luz de janela lateral (não ring light)
- Sombras visíveis no rosto
- Mudança sutil de luminosidade (nuvens passando)
- Overexposição leve em uma parte do frame
- Ausência de luz de preenchimento artificial

**Frase-chave**: `"natural window lighting, slight overexposure on one side, no ring light, visible soft shadows, ambient room lighting"`

#### 🏠 Pilar 3 — Ambiente autêntico
- Fundo levemente bagunçado (cama desarrumada, coisas na prateleira, pôster na parede)
- Objetos do cotidiano visíveis (copos d'água, capas de celular, livros)
- Ruído de fundo leve (AC, rua, música baixa)
- Nenhum backdrop ou cenário "montado"

**Frase-chave**: `"lived-in bedroom background, unmade bed, everyday objects visible on shelves, natural ambient noise atmosphere"`

#### 🗣️ Pilar 4 — Performance humana autêntica
- Micro-pausas antes de responder
- Olhar que desvia brevemente (memória, pensamento)
- Sorriso que não começa perfeito
- Gestos com as mãos não coreografados
- Toque no cabelo, rosto, ou produto de forma natural
- Balbucio ou correção de frase (sem exagero)

**Frase-chave**: `"authentic human expressions, natural micro-pauses, genuine smile building slowly, unscripted hand gestures, occasional glance away"`

#### 📱 Pilar 5 — Linguagem visual de smartphone
- Proporção 9:16 ou 4:5
- Compressão de vídeo leve (não 4K "cinema")
- Abertura f/1.8 simulada — desfoque leve de fundo
- Saturação ligeiramente elevada (modo retrato do iPhone/Samsung)
- Grain digital sutil

**Frase-chave**: `"shot on smartphone, portrait mode, slight digital grain, warm color grading, 9:16 vertical format, compressed video look"`

#### ⏱️ Pilar 6 — Edição orgânica
- Cortes diretos sem transição fancy
- Um ou dois jump cuts intenzionais
- Texto na tela em fonte simples (CapCut style)
- Duração de plano variável (2s, 5s, 3s — não uniforme)
- Sem música dramática — áudio ambiente ou trending sound baixo

**Frase-chave**: `"direct cuts, intentional jump cut, no fancy transitions, casual editing style, variable shot lengths"`

#### 🎭 Pilar 7 — Especificidade da persona
- Roupa casual e real (pijama, camiseta simples, moletom)
- Cabelo não perfeitamente penteado
- Unhas sem manicure perfeita (ou esmalte descascando)
- Skin texture visível — sem filtro de pele suavizante
- Jóias ou acessórios cotidianos (argola simples, cordão)

**Frase-chave**: `"wearing casual everyday clothes, natural skin texture, no beauty filter, hair slightly messy, authentic everyday appearance"`

---

### Passo 3 — Estrutura do Prompt Gerado

O prompt final deve seguir este formato:

```
[SCENE SETUP]
[PERSON DESCRIPTION]
[ENVIRONMENT DESCRIPTION]
[ACTION SEQUENCE]
[CAMERA BEHAVIOR]
[LIGHTING]
[AUDIO ATMOSPHERE]
[TECHNICAL SPECS]
[NEGATIVE PROMPT / O QUE EVITAR]
```

---

### Passo 4 — Template de Prompt (preencher por caso)

```
A [IDADE]-year-old [GÊNERO] [PERSONA CASUAL], wearing [ROUPA COTIDIANA],
sitting/standing in their [AMBIENTE REAL] with [DETALHES DE FUNDO].

They are holding a [PRODUTO] and [AÇÃO PRINCIPAL — ex: opening it for the first time /
talking directly to camera / showing results on skin].

[SEQUÊNCIA DE AÇÃO ESPECÍFICA DO FORMATO]:
- Shot 1: [descrição do plano]
- Shot 2: [descrição do plano]
- Shot 3: [descrição do plano]

Camera: handheld smartphone footage, selfie front-facing angle slightly below eye level,
slight natural camera shake, occasional casual reframing, 9:16 vertical format.

Lighting: natural window light coming from [LADO], soft shadows on face,
no ring light, slight overexposure on one side, warm ambient tone.

Performance: authentic expressions, genuine [EMOÇÃO] building naturally,
natural micro-pauses before speaking, unscripted hand gestures,
occasional glance down at product, natural skin texture visible.

Technical: shot on smartphone (iPhone/Samsung portrait mode look),
slight digital grain, compressed video quality, warm slightly saturated colors,
no cinematic color grading.

Audio atmosphere: [RUÍDO DE FUNDO AMBIENTE] barely audible in background.

DO NOT include: ring light reflections, perfect symmetrical lighting,
studio-quality footage, overly smooth camera movement, beauty skin filters,
perfect hair/makeup, artificial backdrop, dramatic music, fancy transitions.
```

---

## Formatos específicos por tipo de UGC

### 🎁 Unboxing
Sequência: reação ao pacote → abertura com dificuldade real → primeiro contato com produto → reação ao cheiro/textura/aparência → mostra para câmera → lê embalagem em voz alta.

Adicionar: sons de fita arranhando, papelão amassando, "nossa, veio mais rápido do que eu esperava".

### 💬 Depoimento / Review
Sequência: olha direto para câmera → introduz o produto casualmente → conta experiência pessoal específica → mostra o produto sendo usado → dá opinião sincera (com uma ressalva pequena para parecer real) → call to action casual.

Adicionar: uma pausa de pensamento no meio, uma hesitação como "tipo... como eu explico..." antes de um ponto importante.

### 🌅 Rotina / "Day with"
Sequência: manhã com o produto → plano do produto em close durante uso → reação durante o dia → resultado no final do dia.

Adicionar: luz de manhã (quente e suave), cabelo ainda bagunçado, café na mão.

### 📊 Antes e Depois
Sequência: narração do problema antes → show do uso do produto → resultado depois → câmera aproximando do resultado.

Adicionar: iluminação idêntica nos dois planos (para parecer comparação honesta), mesma roupa, mesmo ângulo.

---

## Exemplos de Prompts Prontos

### Exemplo 1 — Skincare (Serum)

```
A 28-year-old Brazilian woman with natural curly hair, slightly messy, wearing a white
oversized t-shirt, sitting cross-legged on an unmade bed in a cozy bedroom.
Behind her: bookshelf with plants, fairy lights slightly blurred,
clothes on a chair in the background.

She's holding a small amber glass serum bottle, examining it with genuine curiosity.

Shot 1 (4s): She looks at camera casually — "então, comprei esse sérum há três semanas
e resolvi filmar minha reação agora que deu pra ver resultado." Slight laugh, touches hair.
Shot 2 (3s): Close-up of her applying a few drops to her palm, then pressing gently to face.
Shot 3 (5s): Looks at camera again, genuinely smiling — "eu juro que não esperava isso,
minha pele tava descamando muito e agora..." — tilts face slightly to show skin texture.
Shot 4 (3s): Shows bottle to camera, reads brand name casually, "vou deixar no link da bio."

Camera: handheld front-facing smartphone, slight wobble, 9:16, slightly below eye level.
Lighting: soft natural morning window light from the left, warm, slight overexposure on right side of face.
Performance: genuine expressions, real skin texture visible, no beauty filter, natural micro-pauses.
Technical: iPhone portrait mode look, warm saturation, slight digital grain.
Background audio: faint street sounds from outside window.

AVOID: ring light, studio lighting, perfect skin smoothing, dramatic music, fancy cuts.
```

### Exemplo 2 — Suplemento / Proteína

```
A 24-year-old athletic man with short hair, post-workout look (slight sweat,
red cheeks), wearing a plain gray gym shirt, standing in a small apartment kitchen.
Background: protein shaker on counter, sneakers on floor, fridge with magnets.

He's holding a black protein powder bag.

Shot 1 (3s): Pours scoop into shaker while talking — "cara, testei esse negócio
por 30 dias antes de falar qualquer coisa."
Shot 2 (4s): Shakes the bottle, glances at it — "o sabor eu achei que ia ser horrível
tipo os outros que tomei..." — pauses, smirks.
Shot 3 (5s): Takes a sip, genuine reaction — slightly surprised expression — "mas
tá surpreendentemente bom. Tipo... achei que ia ser mais doce."
Shot 4 (3s): Shows bag to camera sideways — "vou deixar o desconto nos comentários."

Camera: handheld, slight shake from post-workout energy, phone tilted 2 degrees, selfie mode.
Lighting: overhead kitchen light with window light mixing, slightly harsh but real.
Performance: natural post-workout energy, genuine taste reaction, unperfect smile.
Technical: Samsung camera look, slightly cooler tones, real skin texture.
Audio: refrigerator hum barely audible.

AVOID: gym background, perfect lighting setup, scripted-sounding delivery.
```

---

## Customizações por Plataforma

| Plataforma | Duração ideal | Ritmo | Estética |
|---|---|---|---|
| TikTok | 15–30s | Rápido, direto | Bright, saturado |
| Instagram Reels | 30–60s | Médio | Warm, lifestyle |
| YouTube Shorts | 45–60s | Médio-lento | Mais informativo |
| Stories | 15s | Muito rápido | Casual extremo |

---

## Output final obrigatório

Sempre entregue:
1. **Prompt principal** (em inglês — IAs de vídeo respondem melhor)
2. **Tradução/resumo em português** do que o prompt vai gerar
3. **Sugestão de negative prompt** (o que a IA deve EVITAR)
4. **Adaptações por IA**: como ajustar para Sora vs Runway vs Kling se relevante
5. **Dica de pós-produção**: o que fazer depois de gerar o vídeo para aumentar realismo (adicionar caption CapCut-style, corte jump cut, som de trending)
