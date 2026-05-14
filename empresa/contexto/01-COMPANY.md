# Contexto da Empresa — V4 Company & Colli & Co
**Status:** v1 — Fundamento
**Atualizado:** 2026-04-15
**Fonte:** humano (Luis Santos) + pesquisa publica

---

## 1. V4 Company — Visao Geral

A **V4 Company** e a maior rede de assessoria de marketing de performance do Brasil, fundada ha mais de 10 anos.

| Indicador | Valor |
|-----------|-------|
| Unidades franqueadas | +250 |
| Empresas atendidas | +7.000 |
| Profissionais na rede | +3.500 |
| Parceiros (Matriz + Franqueados) | +300 |
| Certificacoes | Google Premier Partner, Meta Business Partner (top 1%) |

**Modelo de negocio:** assessoria de marketing orientada a performance — a V4 e responsavel por construir e otimizar o processo de vendas pela internet de seus clientes.

**Posicionamento:** "Nosso negocio e vender o seu."

---

## 2. Colli & Co — Identidade da Franquia

**Colli & Co** e a franquia V4 Company operada por Vinicius Colli, uma das maiores unidades individuais da rede.

### Diferenciais da unidade

- Plataforma propria de IA: **Colli & Co IA+** (V4 AI)
- Squads multidisciplinares com profissionais alocados por cliente
- Infraestrutura de dados propria (BigQuery como DWH)
- Desenvolvimento de produtos SaaS internos (V4 Synk RH, Copilot Flows)
- Transicao em curso para modelo SWAS (Saber / Ter / Executar / Potencializar)

### Escritorios e presencialidade

| Escritorio | Modalidade |
|-----------|------------|
| Paulista (SP) | Presencial |
| Campinas (SP) | Presencial |
| Porto Alegre (RS) | Presencial |
| Sinop (MT) | Presencial |
| Remoto | Hibrido |

---

## 3. Modelo SWAS — Framework de Receita

A Colli & Co esta em transicao de receita **puramente recorrente (Executar)** para um mix de quatro pilares:

```
SABER          TER            EXECUTAR        POTENCIALIZAR
Consultoria    Ferramentas    Operacao        Amplificacao
estrategica    e sistemas     recorrente      de resultados
one-time       contratados    (AMS)           (escala)
(~60 dias)
```

| Pilar | Natureza | Objetivo | Exemplo de produto |
|-------|---------|----------|--------------------|
| **Saber** | One-time | Estruturacao estrategica | Diagnostico e Planejamento |
| **Ter** | One-time/recorrente | Ferramentas e ativos | CRM, Site, E-commerce |
| **Executar** | Recorrente (AMS) | Operacao continua de marketing | Gestao de midia, Social Media |
| **Potencializar** | Recorrente | Amplificacao e escala | Profissionais alocados, BI |

> **Motivacao da transicao:** escalar receita sem escalar linearmente a equipe. O modelo "Executar" puro e intensivo em horas; o "Saber" permite entrega de alto valor em prazo fixo.

---

## 4. Clientes — Tiers e Segmentos

### Tier de cliente (faturamento anual da empresa)

**Definicao padrao:** classificacao do cliente pelo **faturamento anual** da empresa, em **reais (R$)**. "M" = milhoes.

| Tier | Faturamento anual |
|------|-------------------|
| Tiny | < R$ 1,2M |
| Small | > R$ 1,2M < R$ 2,4M |
| Medium (-) | > R$ 2,4M < R$ 10M |
| Medium (=) | > R$ 10M < R$ 25M |
| Medium (+) | > R$ 25M < R$ 50M |
| Large | > R$ 50M < R$ 200M |
| Large' | > R$ 200M < R$ 480M |
| Enterprise | > R$ 480M |

**Sistemas e modelos:** em dados operacionais (ex.: FWO, Projection Planner) o campo `tier` costuma aparecer **agregado** em **cinco** valores (`tiny`, `small`, `medium`, `large`, `enterprise`) para planilhas, cohorts e motor de simulacao — alinhado ao export FWO (`TINY`, `SMALL`, etc.). Isso **nao substitui** a segmentacao fina acima; Medium (-), (=) e (+), assim como Large vs Large', podem colapsar no rotulo `medium` ou `large` conforme a base.

**Nao confundir** com tiers de **oferta de produto** (ex.: pacotes de diagnostico em midia paga, planos Food START/GROWTH/SCALE, tiers de plano de software). Esses eixos estao no catalogo em `02-PRODUCTS.md` e no vocabulario vertical (Food).

### Segmentos verticais atendidos

- **Varejo e E-commerce** — midia, SEO, CRM, marketplace
- **Food Service** — produto dedicado V4 Food 2.0 (START/GROWTH/SCALE)
- **B2B** — SDR, CRM de vendas, LinkedIn Ads
- **Servicos** — branding, redes sociais, captacao de leads
- **Franquias e redes** — governanca de marketing por unidade

### Ciclo de vida do cliente

```
Prospecao → Diagnostico (SABER) → Implementacao (TER) → Operacao (EXECUTAR) → Expansao (POTENCIALIZAR)
```

---

## 5. Contexto Estrategico Atual (2026)

### Principais desafios

1. **Cockpit fragmentado:** 73 planilhas de dados parciais; quebras frequentes comprometem gestao em tempo real.
2. **Escalabilidade do SABER:** infraestrutura atual foi construida para o EXECUTAR; nao suporta entrega de consultoria em escala.
3. **SDR manual:** qualificacao de leads ainda depende de humanos; SDR IA em construcao.
4. **Migracao de plataforma:** FWO → HOPS (projetos), tl;dv → Mediahub Recorder (transcricoes).

### Metas estrategicas

- Unificar dados em cockpit unico (BigQuery → dashboards)
- Automatizar SDR (MQL → SQL 100% via IA)
- Lançar primeiro produto SWAS "Saber" em escala
- Reduzir dependencia de planilhas manuais para zero

---

## 6. Plataforma de IA — Colli & Co IA+ (V4 AI)

Plataforma proprietaria de agentes inteligentes integrados ao ecossistema operacional.

### Metricas de uso (ultimo trimestre)

| Metrica | Valor |
|---------|-------|
| Sessoes totais | 28.621 |
| Usuarios ativos | 352 (263 da Colli) |
| Uso via Agentes Automaticos | 95% |

### Agentes em producao

| Agente | Funcao |
|--------|--------|
| SDR IA | Qualificacao de leads (em construcao) |
| ROI Plan Spiced | Geracao de plano de ROI para prospects |
| Concepcao de Copy | Criacao de copys e campanhas |
| Use Case Map | Mapeamento de casos de uso de cliente |
| Persona | Geracao de personas de marketing |
| Growthstorm | Brainstorming de hipoteses de crescimento |
| Auditoria Ekyte | Analise de produtividade e backlog |

---

## Lacunas conhecidas (informacao nao encontrada)

- Faturamento anual exato da unidade Colli & Co
- NPS / CSAT atual consolidado
- Lista completa de clientes ativos (dado sensivel — nao deve viver neste cerebro)
- Metas numericas 2026 detalhadas por pilar SWAS
