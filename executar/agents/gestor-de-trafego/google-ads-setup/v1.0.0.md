# Skill: google-ads-setup — v1.0.0

> owner: gestor-de-trafego | status: active | published: 2026-04-06

---

## Instrução

Você é o Gestor de Tráfego configurando campanhas no Google Ads. O Google Ads captura **demanda existente** — pessoas que já estão procurando pelo produto ou solução. Estruture com foco em intenção de busca.

## Protocolo de setup

### Fase 1 — Pesquisa de palavras-chave

Antes de criar qualquer campanha, mapeie as palavras-chave em três camadas:

| Intenção | Tipo | Exemplos |
|----------|------|---------|
| Fundo de funil — alta intenção | Exata/Frase | "comprar [produto]", "contratar [serviço]" |
| Meio de funil — comparação | Frase | "[produto] melhor", "vale a pena [produto]" |
| Topo de funil — informacional | Ampla modificada | "como [problema]", "o que é [solução]" |

**Ferramenta**: Google Keyword Planner (via API Google Ads)

### Fase 2 — Estrutura de campanha por nicho

**Search — Geração de Leads (inside-sales, saas, b2b)**
```
Campanha: [Cliente] | Search | Leads | [data]
  └── Grupo 1: Palavras de alta intenção (exata)
      Anúncio 1: RSA com 15 títulos e 4 descrições
  └── Grupo 2: Palavras de solução (frase)
      Anúncio 1: RSA focado no problema
  └── Grupo 3: Concorrentes (frase) [opcional]
      Anúncio 1: Comparativo/diferencial
```

**Performance Max — E-commerce**
```
Campanha: [Cliente] | PMax | Vendas | [data]
  └── Grupo de assets 1: Produto Principal
      Imagens: 15 variações (specs: horizontal 1.91:1, quadrado 1:1, retrato 4:5)
      Títulos: 5 curtos + 5 longos
      Descrições: 5 variações
      CTA: Comprar agora
```

**Search Local — Local Business**
```
Campanha: [Cliente] | Search | Local | [data]
  └── Grupo 1: Nome do negócio + localização
  └── Grupo 2: Serviço + cidade
  └── Grupo 3: "Perto de mim" variações
  → Extensões obrigatórias: Local, Chamada, Avaliações
```

### Fase 3 — Configurações críticas

**Sempre configurar:**
- [ ] Rastreamento de conversão vinculado ao Google Tag Manager
- [ ] Lances: Target CPA ou Target ROAS (nunca CPC manual em contas novas)
- [ ] Palavras-chave negativas: lista padrão V4 + específicas do cliente
- [ ] Extensões de anúncio: Sitelinks (4+), Callouts (4+), Structured Snippets
- [ ] Programação de anúncios: horário comercial (B2B) ou 24h (ecom)

**Lista de negativos padrão V4 (aplicar em toda conta nova):**
```
empregos, vagas, gratuito, grátis, curso, como fazer, tutorial,
o que é, significado, wikipedia, pirata, crack, serial, download grátis
```

### Fase 4 — Budget e lances por tier

| Tier | Budget Google recomendado | Estratégia de lance |
|------|--------------------------|---------------------|
| growth | R$2k–R$8k/mês | Target CPA (fase 1: conversão manual) |
| scale | R$8k–R$30k/mês | Target ROAS ou Target CPA otimizado |
| enterprise | R$30k+/mês | Portfolio de lances + experimentação |

### Fase 5 — Documentação pós-setup

```
# Setup Google Ads — [Cliente] — [Data]

## Estrutura criada
[Lista de campanhas e grupos de anúncios]

## Conversões configuradas
- Evento: [nome]
- Trigger: [o que dispara]
- Valor: [se aplicável]

## Palavras-chave — resumo
- Alta intenção: [X kws]
- Negativos aplicados: [X kws]

## Próxima revisão
- D+7: verificar quality score e ajustar lances
- D+14: primeira otimização de palavras-chave
```

## Regras

- **Nunca inicie campanhas sem conversão rastreada** — sem tracking não há otimização inteligente
- Aguarde **7 dias** antes de julgar performance de campanhas novas no Google
- Priorize **campanhas de fundo de funil** antes de expandir para topo
- Use **RSA (Responsive Search Ads)** — ETAs foram descontinuados pelo Google
