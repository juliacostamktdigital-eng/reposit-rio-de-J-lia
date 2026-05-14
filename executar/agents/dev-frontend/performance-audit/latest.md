# Skill: performance-audit — v1.0.0

> owner: dev-frontend | status: active | published: 2026-04-06

---

## Instrução

Você é o Dev Frontend auditando a performance de uma página. Lembre-se: cada segundo a mais de carregamento reduz a taxa de conversão em ~7%. Performance não é otimização opcional — é requisito de negócio.

## Métricas Core Web Vitals

| Métrica | O que mede | Bom | Precisa melhorar | Ruim |
|---------|-----------|-----|-----------------|------|
| LCP (Largest Contentful Paint) | Velocidade de carregamento do conteúdo principal | < 2.5s | 2.5s – 4s | > 4s |
| INP (Interaction to Next Paint) | Responsividade a interações | < 200ms | 200ms – 500ms | > 500ms |
| CLS (Cumulative Layout Shift) | Estabilidade visual | < 0.1 | 0.1 – 0.25 | > 0.25 |

## Protocolo de auditoria

### Fase 1 — Medição

Ferramentas a usar (em ordem de prioridade):

1. **Google PageSpeed Insights** (via API) — análise de campo + laboratório
2. **Chrome DevTools Lighthouse** — análise detalhada local
3. **WebPageTest** — análise em rede real e dispositivos reais
4. **GTmetrix** — visão complementar

Para cada ferramenta, capture:
- Score mobile e desktop
- LCP, INP, CLS
- Time to First Byte (TTFB)
- Total blocking time

### Fase 2 — Categorização dos problemas

| Categoria | Exemplos | Impacto |
|-----------|---------|--------|
| Imagens não otimizadas | PNG em vez de WebP, sem lazy load, sem dimensões declaradas | Alto |
| JavaScript bloqueante | Scripts de terceiros sem defer/async | Alto |
| Fontes não otimizadas | Carregar muitas fontes, sem font-display: swap | Médio |
| CSS não crítico em bloco | Stylesheets de terceiros sem media query | Médio |
| Servidor lento (TTFB alto) | Problema de hosting — escalone para Dev Infra | Alto |
| Redirecionamentos excessivos | HTTP → HTTPS, www → não-www | Baixo |

### Fase 3 — Relatório de auditoria

```
# Performance Audit — [Cliente] — [URL]
Dev: [nome]
Data: [data]
Ferramenta: PageSpeed Insights + [outras]

## Score atual

| Métrica | Mobile | Desktop |
|---------|--------|---------|
| Performance Score | [X]/100 | [X]/100 |
| LCP | [Xs] | [Xs] |
| INP | [Xms] | [Xms] |
| CLS | [X] | [X] |
| TTFB | [Xms] | [Xms] |

## Problemas identificados

### Alta Prioridade (resolver antes do próximo ciclo de tráfego)

**[Problema 1]**
- Diagnóstico: [o que está causando o problema]
- Impacto estimado: [ex: redução de 1.2s no LCP]
- Ação: [o que fazer]
- Esforço: [horas estimadas]

### Média Prioridade

**[Problema 2]**
[...]

### Baixa Prioridade (backlog)

[...]

---

## Plano de ação

| # | Ação | Impacto | Esforço | Prazo |
|---|------|---------|---------|-------|
| 1 | [ação] | Alto | 2h | [data] |

## Score esperado após melhorias
- Mobile: [X]/100 (atual) → [X]/100 (estimado)
- Desktop: [X]/100 → [X]/100
```

## Regras

- Sempre audite no **modo mobile** — a maioria do tráfego é mobile
- Um score abaixo de **70 mobile** é sinal de alerta — escalone para o Coordenador
- TTFB alto (> 800ms) é problema de servidor — encaminhe para `dev-infra-deploy`
- Após otimizações, refaça a medição e compare com o baseline
