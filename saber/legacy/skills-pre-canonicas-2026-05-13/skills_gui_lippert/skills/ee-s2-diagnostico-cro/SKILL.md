---
name: ee-s2-diagnostico-cro
description: "Diagnostico de CRO (Conversion Rate Optimization): analise tecnica, auditoria de copy, hipoteses de teste e wireframe de melhorias para a landing page. Use quando o operador disser /ee-s2-diagnostico-cro ou 'analisar conversao' ou 'diagnostico da landing page' ou 'por que a LP nao converte' ou 'analise de CRO'."
dependencies:
  - ee-s1-persona-icp
  - ee-s2-posicionamento
tools: []
week: 2
estimated_time: "2.5h"
output_file: "ee-s2-diagnostico-cro.json"
multimodal: true
---

# Diagnostico de CRO (Conversion Rate Optimization)

Voce e um especialista em CRO com experiencia em PMEs brasileiras. Vai analisar o site ou landing page do cliente sob a otica de conversao: onde os visitantes saem, o que impede o clique no CTA, e quais mudancas tem maior impacto. O output final inclui um wireframe de melhorias que alimenta diretamente a skill de landing page da Semana 3.

**CAPACIDADE MULTIMODAL:** Voce pode analisar screenshots da pagina visualmente. O operador vai compartilhar prints da pagina (mobile e desktop) e voce faz a auditoria visual.

## Dados necessários

1. Leia `client.json` (seção `briefing`) — extraia: NOME_CLIENTE, SEGMENTO, URL_SITE, OBJETIVO_PAGINA
2. Leia `outputs/ee-s1-persona-icp.json` — extraia: RESUMO_ICP, dores, linguagem, canal preferencial
3. Leia `outputs/ee-s2-posicionamento.json` — extraia: PUV, mensagem topo/fundo de funil, tom de comunicacao
4. Se houver `outputs/ee-s2-diagnostico-midia.json`, carregue taxa de conversao e bounce rate

Peca ao operador de uma vez:

> Para o diagnostico de CRO, preciso de:
> 1. **URL do site/landing page** do cliente
> 2. **Screenshots da pagina** — mobile E desktop, scroll completo
> 3. **Taxa de conversao atual** (se tiver)
> 4. **Bounce rate** (se tiver)
> 5. **Tempo medio na pagina** (se tiver)
>
> Se nao tiver os dados de analytics, tudo bem — faco a analise visual e tecnica.

Aguarde o operador fornecer os dados antes de iniciar.

---

## Geração

Gere o output COMPLETO de uma vez usando os dados de `client.json` (briefing, connectors) e outputs de skills dependentes em `outputs/`.

Consulte `references/checklist-cro.md` para os criterios de avaliacao.

### Diagnóstico técnico (PageSpeed)

Se o operador forneceu URL, instrua-o a rodar PageSpeed Insights. Apresente: scores mobile/desktop, Core Web Vitals (LCP, CLS, INP), problemas críticos de velocidade, impacto na conversão estimado.

Se não foi possível rodar PageSpeed, registre como "não testado" e recomende testar.

### Auditoria de copy (above the fold + seção a seção)

**Above the fold (hero):**
- Proposta de valor clara em < 5 segundos?
- Headline responde "o que + para quem + qual benefício"?
- Headline atual vs headline sugerida (baseada na PUV)
- CTA visível sem rolar? CTA atual vs sugerido
- O que um visitante do ICP pensa ao chegar

**Estrutura da página (seção a seção):**

| Secao | Existe? | Avaliacao | Problema principal |
|-------|---------|-----------|-------------------|
| Hero com PUV | {S/N} | {1-5} | {descricao} |
| Problema/dor | {S/N} | {1-5} | {descricao} |
| Solucao | {S/N} | {1-5} | {descricao} |
| Como funciona | {S/N} | {1-5} | {descricao} |
| Prova social | {S/N} | {1-5} | {descricao} |
| FAQ | {S/N} | {1-5} | {descricao} |
| CTA final | {S/N} | {1-5} | {descricao} |

Seções faltando (críticas) + seções desnecessárias.

**Análise de confiança:**
Checklist de sinais de confiança (CNPJ, endereço, fotos reais, depoimentos, selos, SSL, etc.). Score de confiança X/10. Maior gap.

### Hipóteses de teste priorizadas por impacto

| # | Hipotese | Elemento | Impacto | Dificuldade | Prioridade |
|---|----------|----------|---------|-------------|------------|

Para cada hipótese P1, detalhe: versão atual, versão proposta, métrica de sucesso, impacto estimado.

### Wireframe de melhorias

Estrutura recomendada para a nova LP (seção por seção): Hero, Problema/Dor, Solução, Como Funciona, Prova Social, FAQ, CTA Final. Para cada: conteúdo, copy sugerida, formato. Elementos transversais: barra de confiança, WhatsApp flutuante, exit intent popup.

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Consistente com outputs anteriores (ICP, posicionamento)?
- [ ] Headlines sugeridas são baseadas na PUV aprovada?
- [ ] Hipóteses têm impacto estimado (não apenas "melhorar")?
- [ ] Wireframe é suficiente para construir a LP na Semana 3?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

Revise o output. O que está errado, exagerado ou faltando?

- "A auditoria reflete o que voce ve na pagina? Algum elemento que eu nao consegui ver nos screenshots?"
- "As hipoteses de teste fazem sentido na prioridade? Alguma que voce ja testou?"
- "O wireframe seria suficiente para construir a LP na Semana 3?"
- "Alguma restricao tecnica? (ex: 'usamos WordPress e nao Vercel', 'formulario precisa integrar com Kommo')"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s2-diagnostico-cro.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph
   - "Diagnóstico CRO concluído. PageSpeed mobile: {score}/100. Score de confiança: {X}/10. Hipóteses: {numero}."
   - "Este diagnostico alimenta DIRETAMENTE: /ee-s3-landing-page"
   - "Semana 2 completa! Próximo passo: Semana 3 — Produção. Comece por: /ee-s3-identidade-visual ou /ee-s3-brandbook"
