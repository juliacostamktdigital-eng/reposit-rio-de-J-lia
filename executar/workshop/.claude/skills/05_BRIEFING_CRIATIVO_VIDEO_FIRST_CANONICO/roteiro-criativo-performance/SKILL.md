---
name: roteiro-criativo-performance
description: Gera roteiros de performance para vídeos, UGC, founder, demo, motion, screen-record, estáticos e carrosséis a partir de brief criativo, hipótese, persona, hook, prova, CTA, direção visual e tracking. Use após briefing-criativo-video-first quando precisar de roteiro por cena, textos em tela, legenda/copy ou carrossel slide a slide.
---

# Roteiro Criativo Performance

## Quando Usar

Use quando o brief criativo já existe e precisa virar peça executável para produção, gravação, motion, design ou mídia.

Situações típicas:

- transformar brief em roteiro video-first;
- criar UGC, founder, demo, motion ou screen-record;
- adaptar uma hipótese para formatos diferentes;
- escrever texto em tela e legenda/copy;
- montar carrossel slide a slide;
- gerar variações controladas sem perder ID e tracking.

Não use para redefinir a estratégia do criativo. Se faltarem hipótese, persona, promessa, prova ou tracking, volte para `briefing-criativo-video-first`.

## Inputs Necessários

- brief criativo;
- **`selecao-pack-criativo-ciclo`** (linha do pack: tipo_id, hipótese, critério de leitura) quando produção vier em lote;
- formato;
- duração;
- persona;
- hook;
- dor/desejo;
- ângulo;
- promessa;
- mecanismo;
- prova;
- CTA;
- direção visual;
- claims permitidos/proibidos;
- restrições de marca;
- `creative_id`;
- `utm_content` previsto.

## Workflow

1. Confirme a hipótese e a variável testada.
2. Escolha o tipo de roteiro:
   - video-roteirizado;
   - UGC;
   - founder;
   - demo;
   - motion;
   - screen-record;
   - depoimento;
   - prova social;
   - estático;
   - carrossel.
3. Estruture a narrativa:
   - hook inicial;
   - contexto;
   - tensão;
   - mecanismo;
   - prova;
   - CTA.
4. Para vídeo curto, use blocos de tempo:
   - 0-3s: hook;
   - 3-10s: dor/tensão;
   - 10-20s: mecanismo/prova;
   - 20-30s: CTA.
5. Para carrossel, documente cada slide:
   - função narrativa;
   - texto principal;
   - prova ou exemplo;
   - visual sugerido;
   - CTA/transição;
   - atributo de análise.
6. Escreva:
   - fala/narração;
   - textos em tela;
   - direção visual por cena;
   - legenda/copy do anúncio;
   - observações de edição.
7. Valide:
   - promessa não saiu do brief;
   - prova não foi inventada;
   - CTA está claro;
   - claims são seguros;
   - tracking e versão continuam presentes.

## Output Esperado

- roteiro por cena/bloco de tempo;
- texto em tela;
- direção visual;
- orientação de captação/edição;
- legenda/copy do anúncio;
- carrossel slide a slide quando aplicável;
- variações controladas;
- QA flags de produção.

Use `templates/roteiro-video.md` para vídeo.
Use `templates/carrossel-slide-a-slide.md` para carrossel.
Use `templates/roteiro-criativo.json` com o script para gerar Markdown/CSV.

## Script Utilitário

```bash
python3 scripts/build_creative_script.py templates/roteiro-criativo.json --md /tmp/roteiros.md --csv /tmp/roteiros.csv
```

O script transforma briefs estruturados em roteiros por cena e matriz de produção.

## Definition Of Done

- Roteiro tem hook nos primeiros segundos ou primeiro slide.
- Cada bloco tem função narrativa.
- Prova e promessa estão preservadas.
- CTA aparece no final.
- Textos em tela e direção visual estão claros.
- Variações não misturam múltiplas mudanças.
- `creative_id` e `utm_content` permanecem vinculados.

## Cuidados

- Não inventar prova.
- Não adicionar promessa fora do brief.
- Não remover objeção atacada.
- Não criar roteiro bonito mas impossível de produzir.
- Não esconder pendências de asset, prova, edição ou aprovação.
