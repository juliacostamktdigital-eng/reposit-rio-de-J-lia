# Referência — Performance Max leadgen (playbook 16 + legado 12)

Fonte: **`16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md`**. Legado: **`12-estrutura-campanhas-google-ads-pmax.md`**.

## 1. Quando usar PMax (Seção 8)

Indicado quando:

- conversão está **bem configurada**;
- há **assets suficientes**;
- há **lista/audience signal relevante**;
- há **budget para aprendizado**;
- o objetivo é **expandir além de Search**.

## 2. Quando evitar no início (Seção 8)

Evitar se:

- conversão **não** validada;
- LP/formulário **não** preserva dados;
- **não** há asset minimamente decente;
- budget **baixo demais**;
- cliente precisa de **controle granular imediato**;
- conta **sem sinais mínimos**.

## 3. Estrutura inicial — asset groups (Seção 8)

Campanha PMax 1 — aquisição principal:

- **Asset group 00:** oferta principal;
- **Asset group 01:** segmento/persona prioritária;
- **Asset group 02:** dor ou caso de uso prioritário.

Evitar **muitos** grupos no início; em geral **2 a 5** bastam.

## 4. Audience signals (Seção 8)

Usar como **sinais**, não segmentação rígida:

- Customer Match;
- visitantes do site;
- leads/MQLs;
- termos de busca de alta intenção;
- URLs de concorrentes/referências;
- in-market relevantes;
- públicos GA4.

**Não sobrecarregar.** Começar pelos mais fortes e claros.

## 5. Assets por asset group (Seção 9)

Preparar: headlines curtas e longas; descrições; imagens quadradas, horizontais, verticais quando possível; **logo**; **vídeos próprios** sempre que possível; URLs finais coerentes; chamada, sitelink, snippet quando fizer sentido.

**Regra:** sem vídeo próprio, a plataforma pode gerar vídeo — **raramente** é o melhor padrão; preferir vídeos aprovados no DEOC/briefing.

## 6. Nomenclatura (Seção 10)

**Campanha PMax (exemplo canônico):**

`cmp-hs-prevent-202605-011 | pmax | mql | expansao | antifraude-cfo`

**Asset group:**

`{adgroup_id} | {intencao} | {temperatura} | {tipo} | {slug}`

## 7. Orçamento e PMax (Seção 12)

PMax pode **oscilar** no aprendizado. **Não alterar diariamente** sem evidência. Restante: aprendizado mínimo, ajustes graduais, tCPA/tROAS com histórico, maximizar conversões para volume inicial quando fizer sentido.

## 8. Go-live — trechos PMax (Seção 14)

- PMax com **assets suficientes**;
- **audience signals configurados**;
- PMax com **asset groups, URL expansion, brand controls e metas de conversão** conferidos quando aplicável.

## 9. O que evitar (Seção 17 — PMax)

- PMax **sem asset decente**;
- PMax **sem audience signal**;
- campanha **sem conversão testada** (geral, mas afeta PMax em especial).

## 10. Síntese legado (skill 12)

Passos: conversão validada; prospecting/remarketing/ambos documentados; asset groups por hipótese **sem mensagens opostas** no mesmo grupo; signals como ponto de partida; URL expansion, brand controls, conversões, lance; assets do pack cobrindo mínimo; change log.

## 11. Campos JSON principais

- `gates`: pré-requisitos §8 “quando usar”
- `campanha`: um objeto (expandir para lista no futuro se precisar)
- `campanha.audience_signals[]`: `tipo`, `descricao`, `notas`
- `campanha.asset_groups[]`: `adgroup_id`, `angulo`, textos, flags de imagem/logo/vídeo
- `guardrails`: URL expansion, brand controls, metas, lances
- `pre_go_live_pmax`: espelho §14
