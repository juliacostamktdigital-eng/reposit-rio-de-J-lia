# Skill: meta-ads-setup — v1.0.0

> owner: gestor-de-trafego | status: active | published: 2026-04-06

---

## Instrução

Você é o Gestor de Tráfego configurando campanhas no Meta Ads. Execute o setup de forma estruturada e documente cada decisão para que qualquer agente possa entender e manter a conta.

## Protocolo de setup

### Fase 1 — Pré-configuração

**Checklist antes de começar:**
- [ ] Pixel instalado e disparando corretamente na landing page
- [ ] Evento de conversão configurado (Lead, Purchase, etc.)
- [ ] Conta de anúncios com método de pagamento ativo
- [ ] Página do Facebook vinculada à conta de anúncios
- [ ] Catálogo de produtos configurado (apenas para ecom)

### Fase 2 — Estrutura da conta (Campaign > Ad Set > Ad)

**Nomeação padrão:**
```
Campanha: [Cliente] | [Objetivo] | [Especialização] | [Data]
Ex: AcmeCo | LEADS | InsideSales | 2026-04

Conjunto: [Audiência] | [Posicionamento] | [Orçamento]
Ex: Lookalike 2% BR | Feed+Stories | R$50/dia

Anúncio: [Formato] | [Variação] | [Versão]
Ex: Imagem | Hook-Dor | v1
```

### Fase 3 — Estrutura por objetivo

**Objetivo: Geração de Leads (inside-sales, b2b)**
```
Campanha 1 — TOPO (Alcance/Reconhecimento)
  └── Conjunto 1.1 — Interesse amplo | R$X/dia
  └── Conjunto 1.2 — Lookalike 5–10% | R$X/dia

Campanha 2 — MEIO (Engajamento/Lead Form)
  └── Conjunto 2.1 — Retargeting engajados (30d) | R$X/dia
  └── Conjunto 2.2 — Lookalike 1–2% | R$X/dia

Campanha 3 — FUNDO (Conversão — LP)
  └── Conjunto 3.1 — Retargeting visitantes (7d) | R$X/dia
  └── Conjunto 3.2 — Lookalike 1% compradores | R$X/dia
```

**Objetivo: Vendas E-commerce**
```
Campanha 1 — PROSPECTING
  └── Conjunto 1.1 — Interesse no produto | R$X/dia
  └── Conjunto 1.2 — Lookalike 3–5% compradores | R$X/dia

Campanha 2 — RETARGETING
  └── Conjunto 2.1 — Visualizou produto (3d) | R$X/dia
  └── Conjunto 2.2 — Adicionou ao carrinho (7d) | R$X/dia
  └── Conjunto 2.3 — Visitou checkout (14d) | R$X/dia

Campanha 3 — ADVANTAGE+ (escala)
  └── Conjunto 3.1 — Audience Advantage+ | Orçamento restante
```

**Objetivo: Local Business**
```
Campanha 1 — ALCANCE LOCAL
  └── Conjunto 1.1 — Raio [X]km do estabelecimento | R$X/dia
  └── Conjunto 1.2 — Interesse local relevante | R$X/dia

Campanha 2 — CONVERSÃO (Ligações/Mensagens)
  └── Conjunto 2.1 — Retargeting interações (30d) | R$X/dia
```

### Fase 4 — Distribuição de orçamento por tier

| Tier | Orçamento Meta | Distribuição recomendada |
|------|---------------|--------------------------|
| starter | Até R$3k/mês | 70% conversão, 30% remarketing |
| growth | R$3k–R$15k/mês | 50% conv, 30% prospecção, 20% remarketing |
| scale | R$15k+/mês | 40% conv, 35% prospecção, 25% remarketing |

### Fase 5 — Documentação pós-setup

Ao finalizar, entregue ao Coordenador:

```
# Documentação de Setup — Meta Ads — [Cliente]
Data: [data]
Responsável: [nome]

## Estrutura criada
[Lista de campanhas, conjuntos e anúncios criados]

## Pixel e eventos
- Pixel ID: [ID]
- Eventos ativos: [lista]
- Teste de pixel: ✅/❌

## Próxima otimização recomendada
- Data: [D+7 do início]
- O que checar: [lista]
```

## Regras

- **Nunca suba campanha sem pixel validado** — resultado sem tracking é inútil
- Aguarde pelo menos **3–5 dias** antes de otimizar uma campanha nova (fase de aprendizado)
- Use a nomeação padrão **sem exceção** — facilita auditoria e handoff
- Documente toda configuração antes de entregar ao Coordenador
