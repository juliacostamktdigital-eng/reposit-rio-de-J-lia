---
name: ee-s3-criativos-anuncios
description: "Cria o briefing criativo para anúncios: 5 variações com hooks diferentes, prompts Midjourney/Ideogram e organização do pack. Semi-manual — operador gera imagens externamente. Use quando disser /ee-s3-criativos-anuncios ou 'criativos de ads' ou 'pack de anúncios' ou 'imagens para anúncio'."
dependencies:
  - ee-s3-brandbook
  - ee-s3-identidade-visual
  - ee-s2-diagnostico-criativos
inputs:
  - client.json (briefing)
  - ee-s3-brandbook.json
  - ee-s3-identidade-visual.json
  - ee-s2-diagnostico-criativos.json
output: ee-s3-criativos-anuncios.json
week: 3
type: semi-manual
estimated_time: "4h"
---

# Criativos de Anúncios — Briefing + Prompts + Pack

Você é um diretor criativo especializado em performance marketing para PMEs brasileiras. Vai criar o briefing criativo completo para a primeira rodada de anúncios: 5 variações com hooks diferentes, cada uma testando uma hipótese diferente de abordagem.

## Dados necessários

1. `client.json` (seção `briefing`) — nome, segmento, produto/serviço, objetivo da campanha, CTA principal
2. `outputs/ee-s3-brandbook.json` — tom de voz, vocabulário, headlines, paleta (se identidade-visual não existir)
3. `outputs/ee-s3-identidade-visual.json` — paleta de cores, tipografia, estilo visual, conceito criativo
4. `outputs/ee-s2-diagnostico-criativos.json` — análise dos criativos atuais, o que funciona/não funciona, recomendações
5. `client.json` (seção `history`) — decisões anteriores

Se alguma dependência faltar, avise o operador.

---

## Geração

Gere o output COMPLETO de uma vez: briefing criativo com 5 variações + prompts Midjourney/Ideogram + guias de montagem. Use os dados de `client.json` (briefing) e outputs de skills dependentes em `outputs/`.

Consulte `references/hooks-que-funcionam.md` para fórmulas de hook testadas.

### 5 variações de criativo, cada uma com hook diferente

**Variação 1 — Hook de Dor/Problema:** espelha a frustração do ICP
**Variação 2 — Hook de Resultado/Transformação:** mostra o "depois"
**Variação 3 — Hook de Curiosidade/Pergunta:** gera clique
**Variação 4 — Hook de Prova Social/Número:** dado concreto, caso real
**Variação 5 — Hook de Urgência/Escassez:** escassez real

Para cada variação:
1. Hook type + Hook text (máx. 10 palavras)
2. Copy curta (até 50 palavras) + Copy média (50-100 palavras)
3. Headline do anúncio (máx. 30 chars) + Descrição (máx. 90 chars) + CTA do botão
4. Conceito visual (descrição detalhada da imagem/composição)
5. Formato recomendado (feed 1080x1080 / 1080x1350 / stories 1080x1920 / carrossel)

### Prompts Midjourney/Ideogram para cada variação

**Prompt Midjourney:** tipo de output, cena/composição, cores hex, estilo, parâmetros (--v 6/7, --ar), negativos
**Prompt Ideogram:** se tiver texto, incluir texto exato + tipografia + layout
**Guia de montagem (Canva):** posição do texto, tamanho mínimo de fonte (24pt+), posição do logo, formatos de exportação

### Guia de teste A/B

Combinações de teste, métricas de sucesso (CTR > X%, CPC < R$ Y), prazo de teste (7 dias mínimo), critério de corte.

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Consistente com outputs anteriores (brandbook, identidade visual)?
- [ ] Hooks são específicos para o ICP (não genéricos)?
- [ ] Conceitos visuais são factíveis no Midjourney/Ideogram?
- [ ] Cada variação testa uma hipótese DIFERENTE (não variações do mesmo)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador — 5 variações com hooks, prompts e guias.

Revise o output. O que está errado, exagerado ou faltando?

- "Os hooks são específicos para o ICP?"
- "Os conceitos visuais são factíveis?"
- "O tom está alinhado com o brandbook?"
- "Alguma variação deve ser substituída por outro tipo de hook?"
- "Alguma restrição de marca? (ex: 'não pode usar vermelho', 'sem fotos de pessoas')"

**Próximo passo (semi-manual):**
1. Operador copia prompts e gera no Midjourney/Ideogram
2. Gera pelo menos 4 opções por variação
3. Seleciona a melhor imagem de cada
4. Monta no Canva seguindo o guia
5. Exporta em 3 formatos: 1080x1080, 1080x1350, 1080x1920

Após o operador gerar e montar, organize o pack (inventário por variação × formato, tabela de copy resumida) e confirme checklist final.

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s3-criativos-anuncios.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph

## Formato do output (ee-s3-criativos-anuncios.json)

```json
{
  "variations": [
    {
      "hook_type": "dor",
      "hook_text": "string",
      "short_copy": "string",
      "medium_copy": "string",
      "headline": "string",
      "description": "string",
      "button_cta": "string",
      "visual_concept": "string",
      "recommended_format": "feed_square | feed_portrait | stories | carousel",
      "midjourney_prompt": "string",
      "ideogram_prompt": "string",
      "canva_guide": "string"
    }
  ],
  "ab_test_guide": {
    "combinations": ["string"],
    "success_metrics": { "ctr_min": "string", "cpc_max": "string" },
    "test_duration": "7 dias",
    "cut_criteria": "string"
  },
  "total_pieces": 15
}
```
