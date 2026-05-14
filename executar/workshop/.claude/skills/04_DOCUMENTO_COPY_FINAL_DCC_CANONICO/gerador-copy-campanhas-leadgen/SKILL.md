---
name: gerador-copy-campanhas-leadgen
description: Gera copies de anúncios para campanhas de leadgen mantendo coerência com persona, etapa de funil, formato, promessa, prova, objeção, CTA e tracking. Use ao criar textos para Meta Ads, Google Ads, LinkedIn Ads, variações de headlines, descrições, primary text, CTAs e atributos para utm_content.
---

# Gerador Copy Campanhas Leadgen

## Quando Usar

Use quando já existir estratégia mínima de comunicação e for necessário transformar ângulos em copies publicáveis ou revisáveis.

Situações típicas:

- gerar variações de anúncios a partir do DEOC/DCC;
- transformar biblioteca de hooks em matriz de anúncios;
- criar copies para plano de mídia;
- padronizar textos com `creative_id` e atributos de tracking;
- gerar variações controladas por persona, etapa, hook ou formato;
- preparar insumos para briefing criativo e QA.

Não use para inventar estratégia do zero. Se faltarem ângulos, hooks, provas ou claims seguros, use `biblioteca-angulos-hooks-copy` primeiro.

## Inputs Necessários

- DEOC/DCC ou biblioteca de ângulos;
- plano de mídia;
- taxonomia UTM;
- persona;
- etapa de funil;
- formato;
- oferta;
- CTA;
- promessa;
- prova;
- objeção atacada;
- claims permitidos/proibidos;
- `creative_id` ou regra para gerar IDs.

## Workflow

1. Identifique a hipótese criativa:
   - persona;
   - dor;
   - ângulo;
   - hook;
   - promessa;
   - prova;
   - objeção.
2. Escolha o formato:
   - estático;
   - vídeo;
   - carrossel;
   - texto search;
   - imagem + headline;
   - LinkedIn single image/document.
3. Defina a etapa de funil:
   - TOFU: tensão, dor, diagnóstico, nova crença;
   - MOFU: mecanismo, prova, comparação, objeção;
   - BOFU: oferta, urgência, CTA, risco reduzido.
4. Gere variações controladas:
   - não mude persona, dor e promessa na mesma variação;
   - declare qual variável muda;
   - preserve prova e claim seguro.
5. Preencha campos obrigatórios:
   - `creative_id`;
   - persona;
   - etapa;
   - formato;
   - hook;
   - texto principal;
   - headline;
   - descrição;
   - CTA;
   - prova usada;
   - objeção atacada;
   - `utm_content` ou atributos previstos;
   - variação.
6. Revise claims proibidos e riscos de comunicação.
7. Entregue matriz pronta para mídia, criativo, tracking e leitura de performance.

## Output Esperado

- matriz de copies por anúncio;
- variações de texto principal;
- headlines;
- descrições;
- CTAs;
- prova e objeção por copy;
- `utm_content_attrs`;
- hipótese e variável testada;
- riscos e observações de QA.

Use `templates/copy-anuncio.md` para uma entrega editorial.
Use `templates/copy-anuncios.json` com o script para gerar CSV/Markdown.

## Script Utilitário

```bash
python3 scripts/build_ad_copy_matrix.py templates/copy-anuncios.json --csv /tmp/copies.csv --md /tmp/copies.md
```

O script expande briefs de anúncios em uma matriz normalizada e monta atributos de `utm_content`.

## Definition Of Done

- Cada copy tem hipótese clara.
- Cada variação muda uma variável principal.
- A promessa é sustentada por prova.
- Claims proibidos foram evitados.
- CTA é coerente com etapa e oferta.
- `utm_content_attrs` permite leitura por formato, persona, hook, dor, ângulo, etapa e versão.
- O output pode ir para mídia, briefing criativo ou QA sem retrabalho estrutural.

## Cuidados

- Não criar copy sem prova.
- Não gerar variações que misturam muitas mudanças.
- Não usar superlativos absolutos sem base.
- Não prometer resultado financeiro sem recorte/fonte.
- Não perder conexão com LP/oferta.
