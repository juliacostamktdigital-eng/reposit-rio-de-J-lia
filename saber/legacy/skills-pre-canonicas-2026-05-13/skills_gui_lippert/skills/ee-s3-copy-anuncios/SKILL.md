---
name: ee-s3-copy-anuncios
description: "Gera 30+ variações de copy de anúncios por funil e plataforma (Meta Ads + Google Ads). Output exportado para Google Sheets. Use quando disser /ee-s3-copy-anuncios ou 'copy de ads' ou 'textos de anúncio' ou 'copy para Meta'."
dependencies:
  - ee-s3-brandbook
  - ee-s1-persona-icp
  - ee-s2-posicionamento
inputs:
  - client.json (briefing)
  - ee-s3-brandbook.json
  - ee-s1-persona-icp.json
  - ee-s2-posicionamento.json
output: ee-s3-copy-anuncios.json
export: google-sheets
week: 3
type: automated
estimated_time: "2h"
---

# Copy de Anúncios — 30+ Variações por Funil × Plataforma

Você é um copywriter especializado em mídia paga para PMEs brasileiras. Vai criar a planilha completa de copy para anúncios prontas para subir no Meta Ads Manager e Google Ads.

## Dados necessários

1. `client.json` (seção `briefing`) — nome, segmento, produto/serviço, oferta, plataformas de mídia
2. `outputs/ee-s3-brandbook.json` — tom de voz, vocabulário, headlines, CTAs, do's/don'ts
3. `outputs/ee-s1-persona-icp.json` — ICP, dores, desejos, objeções, linguagem
4. `outputs/ee-s2-posicionamento.json` — PUV, diferenciais, posicionamento
5. `client.json` (seção `history`) — decisões anteriores

---

## Geração

Gere o output COMPLETO de uma vez usando os dados de `client.json` (briefing) e outputs de skills dependentes em `outputs/`.

Consulte `references/regras-copy-performance.md` para limites de caracteres e regras de cada plataforma.

### 30+ variações por fase do funil

**TOPO DE FUNIL — Consciência do problema**
Tom: educativo, empático, sem vender.
- Meta Ads: texto principal (3 var, máx. 125 chars) + título (3 var, máx. 40 chars) + descrição (2 var, máx. 30 chars)
- Google Ads Responsivo: títulos (5, máx. 30 chars) + descrições (3, máx. 90 chars)

**MEIO DE FUNIL — Consideração**
Tom: educativo + prova social.
- Meta Ads: texto principal (3 var, com dado/resultado) + título (3 var)
- Google Ads: títulos (5) + descrições (3)

**FUNDO DE FUNIL — Conversão**
Tom: direto, urgência real, benefício claro.
- Meta Ads: texto principal (3 var, hooks: dor/resultado/urgência) + título (3 var) + descrição (2 var)
- Google Ads: títulos com intenção de compra (5) + descrições com CTA direto (3)

**REMARKETING**
- Texto principal (2 var, diferente da copy fria) + título (2 var)

**REGRAS DE COPY APLICADAS:** Liste as 5 principais regras aplicadas para que o consultor entenda a lógica.

### Revisão em formato de planilha

Apresente todas organizadas:
```
FASE       | PLATAFORMA | TIPO        | TEXTO                    | CHARS
Topo       | Meta       | Principal   | "Você sabia que..."      | 98/125
```

### Exportação para Google Sheets

Crie via GOG CLI:
```bash
gog sheets create --title "Copy Anúncios - {NOME_CLIENTE}" --no-input
```
4 abas: Topo, Meio, Fundo, Remarketing. Coluna "Status" para o consultor marcar como Aprovada/Rejeitada/Em teste.

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Consistente com outputs anteriores (brandbook, posicionamento)?
- [ ] Nenhuma copy ultrapassa limite de caracteres da plataforma?
- [ ] Copy do topo fala do PROBLEMA sem mencionar o produto?
- [ ] Remarketing é diferente da copy fria (não repetição)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

Revise o output. O que está errado, exagerado ou faltando?

- "A copy do topo fala do PROBLEMA sem mencionar o produto?"
- "O fundo de funil tem CTA claro e específico?"
- "O remarketing é diferente da copy fria?"
- "Os limites de caracteres estão respeitados?"
- "O tom é consistente com o brandbook?"
- "Quer exportar para Google Sheets?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s3-copy-anuncios.json` (com campo `summary` no topo, incluindo link Sheets)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph

## Formato do output (ee-s3-copy-anuncios.json)

```json
{
  "funnel_stages": [
    {
      "name": "topo_de_funil",
      "objective": "Consciência do problema",
      "tone": "Educativo, empático, sem vender",
      "platforms": [
        {
          "name": "meta_ads",
          "variations": [{ "type": "text_primary", "text": "string", "headline": "string", "description": "string", "cta": "string", "char_count": { "text": 98, "headline": 34, "description": 28 } }]
        },
        {
          "name": "google_ads",
          "variations": [{ "type": "responsive_search", "headlines": ["string x5"], "descriptions": ["string x3"] }]
        }
      ]
    }
  ],
  "copy_rules_applied": ["string — 5 regras aplicadas"],
  "total_variations": 30,
  "sheets_url": "string — link do Google Sheets"
}
```
