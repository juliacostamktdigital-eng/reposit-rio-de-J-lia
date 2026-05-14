# Estrutura de Equipe — Colli & Co
**Status:** v1 — Fundamento
**Atualizado:** 2026-04-15
**Fonte:** humano — extraido de v4-synk-rh (sistema de RH)

---

## 1. Squads

A equipe e organizada em squads multidisciplinares. Cada squad atende uma carteira de clientes ou funcao interna.

| Squad | Tipo | Foco |
|-------|------|------|
| **Arcade** | Cliente | Carteira de clientes |
| **Billions** | Cliente | Carteira de clientes (grandes contas) |
| **CS** | Interno | Customer Success |
| **Exclusive** | Cliente | Carteira premium |
| **Falcons** | Cliente | Carteira de clientes |
| **Financial** | Interno | Financeiro e controladoria |
| **Gestao** | Interno | Lideranca e diretoria |
| **Invictus** | Cliente | Carteira de clientes |
| **People** | Interno | People & Performance (RH) |
| **Sharks** | Cliente | Carteira de clientes |
| **Startech** | Interno/Produto | Tecnologia e desenvolvimento de produto |

---

## 2. Funcoes e Papeis

### Lideranca e Gestao

| Funcao | Responsabilidade |
|--------|-----------------|
| Gerente de PE&G | Direcao estrategica do cliente; responsavel pelo resultado de PE&G (Product, Execution & Growth) |
| Coordenador de PE&G | Governanca de execucao e qualidade na carteira |
| Coordenador Administrativo | Gestao administrativa interna |
| Product Manager | Produto digital interno |

### Atendimento e Sucesso do Cliente

| Funcao | Responsabilidade |
|--------|-----------------|
| Account Manager (AM) | Relacionamento com cliente, gestao de contrato, renovacoes, upsell |
| Customer Success (CS) | Saude do cliente, NPS, churn prevention |
| Sales Enablement | Capacitacao do time de vendas do cliente |

### Execucao de Marketing

| Funcao | Especialidade |
|--------|--------------|
| Gestor de Trafego | Meta Ads, Google Ads, performance de midia paga |
| Social Media | Conteudo organico, comunidade, calendario editorial |
| Copywriter (Redacao Publicitaria) | Textos de campanha, e-mail, landing page |
| Designer Grafico | Producao visual, criativos |
| Web Designer | UI, mockups, materiais digitais |
| UX/UI Designer | Experiencia do usuario, wireframes |
| Profissional de Audiovisual | Video e foto profissional |

### CRM, Dados e Tecnologia

| Funcao | Especialidade |
|--------|--------------|
| Analista de CRM | Configuracao e gestao de CRM (GHL, HubSpot, Kommo) |
| Analista de Automacao | n8n, Make, fluxos de automacao |
| Analista de BI | BigQuery, Power BI, dashboards |
| Analista de Dados | Modelagem, ETL, qualidade de dados |
| Analista de SEO | Otimizacao organica, linkbuilding |
| Desenvolvedor Backend | Node.js, APIs, integrações |
| Desenvolvedor Frontend | React, TypeScript, UI |
| Desenvolvedor Full Stack | Full stack |

### Vendas e Prospeccao

| Funcao | Responsabilidade |
|--------|-----------------|
| Pré-Vendas / SDR | Qualificacao de leads inbound, agendamento de reunioes |
| Prospecção Ativa / BDR | Geracao de demanda outbound |
| LDR (List Development Representative) | Enriquecimento e listas de prospeccao |
| Closer (Executivo de Vendas) | Fechamento de contratos |

### People & RH

| Funcao | Responsabilidade |
|--------|-----------------|
| HRBP | Business Partner de RH, registro de feedbacks, planos de acao |
| People & Performance | Cultura, desenvolvimento, performance |
| Talent Acquisition | Recrutamento e selecao |
| Talent Research | Pesquisa e mapeamento de talentos |
| Financeiro | Financas, folha, controladoria |

---

## 3. Localidades (Atuacao)

| Escritorio | Modalidade |
|-----------|------------|
| Paulista (SP) | Presencial / Hibrido |
| Campinas (SP) | Presencial / Hibrido |
| Porto Alegre (RS) | Presencial / Hibrido |
| Sinop (MT) | Presencial / Hibrido |
| Remoto | Totalmente remoto |

**Presencialidade:** pode ser configurada de 1x a 5x por semana (dado registrado no v4-synk-rh).

---

## 4. Recrutadores e Canais de Selecao

### Recrutadores ativos

- Eliza Hubner
- Fernanda Luz
- Izabela Moreno
- Maria Luiza Diaz
- Mirella Lima

### Principais canais de origem de candidatos

| Canal | Tipo |
|-------|------|
| LinkedIn (Colli, Erick Cardoso, Gustavo, Gui Duarte, Paulo, Talent) | Hunting e candidatura |
| Gupy | Plataforma ATS |
| Indeed / Catho / Infojobs | Job boards |
| Indicacoes | Rede V4, Colli&Co, socios |
| Instagram / Trafego Pago | Marketing de recrutamento |
| GMA / In-hire / Hiring Hub | Especializados |

---

## 5. Sistema de Gestao de Pessoas — V4 Synk RH

O sistema **v4-synk-rh** (aplicacao React + Supabase) e a fonte de verdade operacional para:

- Perfis de colaboradores (funcao, squad, escritorio, presencialidade)
- Candidatos e funil de recrutamento
- Registros de HRBP (feedbacks 1:1, desligamentos, planos de acao)
- Desligamentos e historico

> Acesso: aplicacao interna — nao exposta publicamente.
> Dados sensiveis de colaboradores NAO devem ser replicados para este cerebro.

---

## 6. Hierarquia de RBAC (Permissoes no Sistema de RH)

O sistema RH tem controle de acesso baseado em papel (RBAC):

- **Admin:** visao completa de todos os colaboradores e unidades
- **Lider:** visao do seu squad / time direto
- **HRBP:** acesso a registros de feedback e planos de acao
- **Colaborador:** acesso ao proprio perfil

---

## Lacunas conhecidas

- Numero exato de colaboradores ativos (dado volatil — consulte v4-synk-rh)
- Organograma formal desenhado (nao encontrado no repositorio)
- Responsaveis nominais por cada squad (nao disponivel neste cerebro por privacidade)
