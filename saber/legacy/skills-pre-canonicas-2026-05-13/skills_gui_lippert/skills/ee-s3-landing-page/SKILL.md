---
name: ee-s3-landing-page
description: "Cria a landing page de conversão: copy completa seção por seção, geração de código React+Tailwind, e deploy na Vercel. Mix auto + manual. Use quando disser /ee-s3-landing-page ou 'criar LP' ou 'landing page' ou 'página de conversão'."
dependencies:
  - ee-s2-posicionamento
  - ee-s3-brandbook
  - ee-s2-diagnostico-cro
inputs:
  - client.json (briefing)
  - ee-s2-posicionamento.json
  - ee-s3-brandbook.json
  - ee-s2-diagnostico-cro.json
output: ee-s3-landing-page.json
week: 3
type: mixed
estimated_time: "6h"
---

# Landing Page — Copy + Código + Deploy

Você é um copywriter especializado em landing pages de conversão para PMEs brasileiras, com conhecimento em desenvolvimento React/Tailwind. Vai criar a LP completa: copy persuasiva, código funcional e deploy na Vercel.

## Dados necessários

1. `client.json` (seção `briefing`) — nome, segmento, produto/serviço, WhatsApp, site atual
2. `outputs/ee-s2-posicionamento.json` — PUV, posicionamento, diferenciais
3. `outputs/ee-s3-brandbook.json` — tom de voz, paleta, tipografia, vocabulário, headlines, CTAs
4. `outputs/ee-s2-diagnostico-cro.json` — análise de conversão, problemas identificados, wireframe sugerido
5. `outputs/ee-s3-identidade-visual.json` — se existir, usar paleta e tipografia
6. `client.json` (seção `history`) — decisões anteriores

Se brandbook ou posicionamento não existirem, avise e sugira rodar antes.

---

## Geração

Gere o output COMPLETO de uma vez: copy da LP + código + instruções de deploy. Use os dados de `client.json` (briefing) e outputs de skills dependentes em `outputs/`.

Consulte `references/copy-patterns-lp.md` para padrões de copy de alta conversão.

### Copy completa (seção por seção)

**HERO:** Headline (máx. 8 palavras), subheadline (1-2 frases), CTA primário, CTA secundário
**PROBLEMA:** 3 dores do ICP (título + 1 frase de empatia cada)
**SOLUÇÃO:** 3-4 benefícios com ícone sugerido, conectados ao PUV
**COMO FUNCIONA:** 3 passos simples (título + 1 frase)
**ENTREGÁVEIS:** Lista principal com benefício de cada
**PROVA SOCIAL:** Estrutura para 2-3 depoimentos + números de impacto
**FAQ:** 5 objeções mais comuns do ICP com respostas que vendem
**CTA FINAL:** Headline de urgência + subtítulo de reassurance + botão

**META / SEO:** Title tag (máx. 60 chars), meta description (máx. 155 chars), OG tags

### Código React + Tailwind

Gere o código completo da LP:
- Next.js ou React SPA com Tailwind CSS
- Mobile-first, totalmente responsivo
- CTA com link para WhatsApp: `https://wa.me/{WHATSAPP}?text={MENSAGEM_ENCODED}`
- SEO básico, Google Fonts, cores da paleta como variáveis Tailwind
- Componentes por seção (Hero, Problem, Solution, HowItWorks, SocialProof, FAQ, FinalCTA)
- FAQ com accordion, scroll suave, sem imagens pesadas, PageSpeed-friendly

### Deploy na Vercel

Instruções para deploy:
```bash
cd landing-{slug}
npm install && npm run dev  # teste local
vercel --yes --prod          # deploy
```

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Consistente com outputs anteriores (posicionamento, brandbook)?
- [ ] Headline do hero é baseada na PUV (não genérica)?
- [ ] FAQ responde as 5 objeções reais do ICP?
- [ ] Código é mobile-first e PageSpeed-friendly?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador — copy seção por seção em formato de preview.

**DECISÃO 1:** Copy da LP — aprovar ou ajustar?

Apresente preview visual da estrutura:
```
━━ HERO ━━ → ━━ PROBLEMA ━━ → ━━ SOLUÇÃO ━━ → ━━ COMO FUNCIONA ━━
━━ PROVA SOCIAL ━━ → ━━ FAQ ━━ → ━━ CTA FINAL ━━
```

Valide:
- Headline do hero é específica e orientada ao benefício?
- As 3 dores são as que o ICP realmente sente?
- Os 3 passos do "como funciona" são verdadeiros?
- O cliente tem depoimentos reais? Se sim, cole aqui.
- As respostas do FAQ respondem as objeções reais de venda?
- O CTA aponta para WhatsApp ou formulário?
- O WhatsApp está correto?

Após aprovação da copy, gere o código e instrua o operador a testar localmente. Depois, execute o deploy.

**Checklist pós-deploy:**
- Abriu corretamente no desktop e mobile?
- PageSpeed > 90?
- WhatsApp CTA funciona?
- Meta tags corretas?

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s3-landing-page.json` (com campo `summary` no topo, incluindo URL de deploy)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph

## Formato do output (ee-s3-landing-page.json)

```json
{
  "sections": [
    { "name": "hero", "headline": "string", "subheadline": "string", "cta_primary": "string", "cta_secondary": "string" },
    { "name": "problem", "headline": "string", "cards": [{ "title": "string", "body": "string" }] },
    { "name": "solution", "headline": "string", "benefits": [{ "icon": "string", "title": "string", "body": "string" }] },
    { "name": "how_it_works", "headline": "string", "steps": [{ "number": 1, "title": "string", "body": "string" }] },
    { "name": "deliverables", "headline": "string", "items": [{ "title": "string", "benefit": "string" }] },
    { "name": "final_cta", "headline": "string", "subheadline": "string", "cta": "string" }
  ],
  "faq": [{ "question": "string", "answer": "string" }],
  "social_proof": {
    "testimonials": [{ "name": "string", "role": "string", "text": "string" }],
    "stats": [{ "number": "string", "label": "string" }]
  },
  "meta": { "title": "string", "description": "string", "og_title": "string", "og_description": "string", "og_type": "website" },
  "deploy_url": "string",
  "whatsapp_link": "string"
}
```
