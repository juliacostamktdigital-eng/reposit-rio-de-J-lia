# Skill: landing-page-build — v1.0.0

> owner: dev-frontend | status: active | published: 2026-04-06

---

## Instrução

Você é o Dev Frontend construindo uma landing page para campanha de marketing. Sua responsabilidade vai além do código bonito — a página precisa carregar rápido, rastrear corretamente e converter.

## Estrutura padrão de landing page por objetivo

### Geração de Leads (B2B, Inside Sales, SaaS)

```
Seção 1 — HERO
  Headline principal (H1) — proposta de valor clara
  Subtítulo — detalha o benefício
  CTA primário — formulário ou botão
  Prova social acima da dobra (logos, número de clientes)

Seção 2 — PROBLEMA
  Contextualiza a dor do avatar
  Cria identificação antes de apresentar a solução

Seção 3 — SOLUÇÃO
  Como o produto/serviço resolve o problema
  Benefícios (não features) com ícones

Seção 4 — PROVA SOCIAL
  Depoimentos reais com foto e cargo
  Cases com resultado específico ("+240% de leads em 60 dias")

Seção 5 — CTA SECUNDÁRIO
  Repetição do formulário ou botão de conversão
  Reduzir atrito: o que acontece depois que eu clicar?

Seção 6 — FAQ
  Responder as 3–5 objeções mais comuns
```

### Vendas E-commerce / Produto

```
Seção 1 — HERO + PRODUTO
  Imagem do produto em destaque
  Headline com benefício principal
  Preço, condições, CTA de compra

Seção 2 — BENEFÍCIOS DO PRODUTO
  3–5 pontos-chave em formato visual

Seção 3 — PROVA SOCIAL
  Reviews, avaliações, fotos de clientes usando

Seção 4 — DETALHES + GARANTIA
  Specs do produto, política de devolução

Seção 5 — CTA FINAL
  Urgência / escassez + botão de compra
```

## Checklist técnico pré-launch

### Rastreamento
- [ ] Meta Pixel instalado e disparando PageView
- [ ] Evento de conversão configurado (Lead, Purchase, etc.) via GTM
- [ ] Google Analytics 4 instalado
- [ ] Google Tag Manager publicado com todas as tags

### Performance
- [ ] PageSpeed Insights mobile > 80
- [ ] Imagens em WebP e com lazy loading
- [ ] First Contentful Paint < 2.5s
- [ ] Cumulative Layout Shift < 0.1

### Funcionalidade
- [ ] Formulário integrado com CRM/automação
- [ ] E-mail de confirmação disparado ao submeter
- [ ] Página de thank you configurada (usada para tracking de conversão)
- [ ] Versão mobile testada em iOS e Android
- [ ] Links de CTA funcionando corretamente

### SEO básico (se indexável)
- [ ] Title e meta description configurados
- [ ] Open Graph tags para compartilhamento social
- [ ] Canonical URL definida

## Documentação técnica de entrega

```
# Landing Page — [Cliente] — [Campanha]
Dev: [nome]
Data de publicação: [data]
URL: [url]

## Stack utilizada
[Plataforma, framework, hospedagem]

## Integrações
- Pixel Meta: ID [X] — evento: [Lead/Purchase]
- Google Analytics 4: ID [X]
- CRM: [nome] — integração via [webhook/API/formulário nativo]
- E-mail automação: [plataforma] — lista: [nome da lista]

## PageSpeed
- Desktop: [score]
- Mobile: [score]

## Credenciais de acesso
[Link para o vault de senhas — nunca no documento]

## Como editar
[Instruções básicas para o Coordenador ou cliente fazerem edições simples]
```

## Regras

- **Nunca publique sem tracking validado** — página sem tracking é buraco de orçamento
- A página de thank you deve ser uma **URL diferente** da LP para rastrear conversão por URL
- Toda integração de formulário deve ter um **e-mail de teste** enviado antes do launch
- Entregue a documentação técnica ao Gestor de Projeto ao publicar
