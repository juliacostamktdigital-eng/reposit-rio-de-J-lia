# Taxonomia do Sistema de Skills

> Definições canônicas dos eixos de classificação usados nos metadados de cada skill

---

## Eixo: `segment` — Segmento de mercado do cliente

Define o modelo de negócio do cliente atendido.

| Valor | Descrição | Exemplos |
|-------|-----------|---------|
| `b2b` | Empresa que vende para outras empresas | SaaS B2B, agências, consultorias, distribuidoras |
| `b2c` | Empresa que vende diretamente ao consumidor final | E-commerce, infoprodutos, academias, clínicas |
| `b2b2c` | Empresa que vende para empresas que vendem ao consumidor | Franquias, marketplaces, plataformas de benefícios |

Uma skill pode pertencer a múltiplos segmentos. Se não houver restrição, omita o campo ou use todos os valores.

---

## Eixo: `tier` — Porte do cliente (investimento mensal em marketing)

| Valor | Faixa de investimento | Características típicas |
|-------|-----------------------|------------------------|
| `starter` | Até R$ 5.000/mês | Time reduzido, menos automação, foco em resultados rápidos |
| `growth` | R$ 5.000 – R$ 30.000/mês | Time dedicado, começando a escalar, mais canais |
| `scale` | R$ 30.000 – R$ 100.000/mês | Operação madura, múltiplos canais, otimização contínua |
| `enterprise` | Acima de R$ 100.000/mês | Contratos complexos, integrações, SLA formal |

---

## Eixo: `software` — Tipo de integração ou execução

| Valor | Descrição |
|-------|-----------|
| `mcp` | Execução via MCP Server (Model Context Protocol) — integração direta com ferramentas externas através de protocolo de contexto |
| `api` | Consumo direto de API externa (REST, GraphQL, webhook) |
| `manual` | Procedimento executado pelo agente sem integração de software — puro raciocínio + output textual |

---

## Eixo: `specialization` — Especialismo de negócio

Define o nicho ou vertical de atuação para o qual a skill foi otimizada.

| Valor | Descrição | Contexto típico |
|-------|-----------|----------------|
| `ecom` | E-commerce — lojas virtuais | Shopify, WooCommerce, VTEX, Nuvemshop |
| `inside-sales` | Vendas internas — time comercial com alto volume de leads | CRM intensivo, SDR + Closer, sequências de cadência |
| `local-business` | Negócio local — presença física + digital | Google Meu Negócio, tráfego geolocalizado, clínicas, restaurantes |
| `saas` | Software as a Service | Trial/freemium, MRR, churn, activation |
| `infoproduto` | Produtos digitais — cursos, mentorias, ebooks | Lançamentos, perpétuo, comunidades |

---

## Eixo: `owner` — Agente responsável

O campo `owner` define qual agente é **responsável pela manutenção** da skill. Agentes consumers apenas a consomem.

| Valor | Agente |
|-------|--------|
| `gerente` | Gerente |
| `coordenador` | Coordenador |
| `gestor-de-trafego` | Gestor de Tráfego |
| `copywriter` | Copywriter |
| `gestor-de-projeto` | Gestor de Projeto |
| `designer` | Designer |
| `dev-frontend` | Dev Frontend |
| `dev-infra-deploy` | Dev de Infra/Deploy |
| `shared` | Skill sem owner único — mantida coletivamente |

---

## Combinações comuns (exemplos)

| Skill | segment | tier | software | specialization |
|-------|---------|------|----------|---------------|
| Setup de Meta Ads para e-com | b2c | starter, growth | mcp | ecom |
| Cadência de e-mail B2B SaaS | b2b | growth, scale | api | saas, inside-sales |
| Relatório de performance tráfego | b2b, b2c | all | manual | — |
| Landing page com integração CRM | b2b | growth | api | inside-sales |
| Onboarding de cliente novo | b2b, b2c | all | manual | — |

---

## Notas de uso

- Um campo vazio ou ausente significa **sem restrição** — a skill serve para todos os valores daquele eixo
- Prefira ser **restritivo** ao criar: é melhor ter uma skill focada e funcional do que genérica e imprecisa
- Se uma skill funciona em todos os tiers, omita o campo `tier`
- Se uma skill só funciona com MCP específico, documente o nome do MCP nos inputs da skill
