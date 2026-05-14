# Vocabulario Canonico — Colli & Co
**Status:** v1 — Fundamento
**Atualizado:** 2026-04-15
**Fonte:** humano

> Regra: sempre use os termos desta lista. Nunca use sinonimos ou nomes alternativos.
> Quando um novo termo entrar em uso, adicione aqui antes de usa-lo em outros documentos.

---

## Termos de Negocio

| Termo canonico | Definicao | Nao usar |
|----------------|-----------|----------|
| **SWAS** | Framework de receita: Saber, Ter, Executar, Potencializar | "modelo de negocio 4 pilares" |
| **Saber** | Pilar de consultoria estrategica one-time (~60 dias) | "diagnostico", "consultoria" (generico) |
| **Ter** | Pilar de implementacao de ferramentas e ativos (one-time) | "setup", "implementacao" (isolado) |
| **Executar** | Pilar de operacao recorrente (AMS — Agency Managed Services) | "recorrente", "mensalidade" |
| **Potencializar** | Pilar de amplificacao e escala (recorrente) | "upsell" (generico) |
| **PE&G** | Product, Execution & Growth — area responsavel pela entrega ao cliente | "delivery", "execucao" |
| **Account Manager (AM)** | Responsavel pelo relacionamento e sucesso do cliente | "gerente de conta", "CS" (diferente) |
| **Squad** | Time multidisciplinar que atende carteira de clientes | "time", "equipe" |
| **Cockpit** | Painel de gestao centralizado da operacao | "dashboard" (no contexto de gestao interna) |
| **V4 Food 2.0** | Produto vertical dedicado ao food service (START/GROWTH/SCALE) | "produto food", "plano food" |
| **Tier (cliente)** | Porte do **cliente** por **faturamento anual** da empresa (faixas em `01-COMPANY.md`) | "tier" como sinonimo de investimento em midia ou de pacote de produto |
| **Carteira** | Conjunto de clientes atendidos por um squad ou AM | "portfolio de clientes", "base" |
| **Churn** | Cancelamento de contrato de cliente | "saida", "cancelamento" |
| **LTV** | Lifetime Value — valor total gerado por um cliente no tempo | "valor vitalicio" |
| **MRR** | Monthly Recurring Revenue — receita recorrente mensal | "receita mensal" |
| **MQL** | Marketing Qualified Lead — lead qualificado pelo marketing | "lead qualificado" |
| **SQL** | Sales Qualified Lead — lead qualificado para abordagem comercial | "lead pronto para venda" |

---

## Termos de Plataformas e Sistemas

| Termo canonico | Descricao | Nao usar |
|----------------|-----------|----------|
| **Colli & Co IA+** | Plataforma proprietaria de agentes de IA | "V4 AI", "plataforma de IA", "chatbot" |
| **FWO** | Sistema legado de gestao de projetos (sendo substituido por HOPS) | — |
| **HOPS** | Novo sistema de gestao de projetos (substitui FWO, API GraphQL) | "novo FWO" |
| **Ekyte** | Ferramenta de backlog e produtividade | "task manager" |
| **tl;dv** | Ferramenta SaaS legada de transcricao de calls (sendo substituida) | "transcricao" (generico) |
| **Mediahub Recorder** | Sistema proprio de transcricao de calls (substitui tl;dv) | "mediahub" (sozinho e ambiguo) |
| **mkt.lab** | Plataforma de consolidacao de dados de midia (Meta + Google) | "lab de marketing" |
| **BigQuery** | Data Warehouse central da Colli & Co | "DWH", "banco de dados" (impreciso) |
| **Pipefy** | CRM de oportunidades / funil de leads | — |
| **Kommo** | CRM de vendas / pipeline comercial | "AMO CRM" (nome antigo) |
| **GHL / GoHighLevel** | Plataforma de CRM e automacao para clientes | "Go High Level" |
| **HubSpot** | CRM e ferramenta de marketing automation | — |
| **Power BI** | Ferramenta de BI e dashboards | "PowerBI" (sem espaco e aceito) |
| **v4-synk-rh** | Sistema interno de gestao de RH (React + Supabase) | "sistema de RH", "app de pessoas" |
| **v4-copilot-flows** | Plataforma multi-tenant de agentes (Strapi + React) | "copilot", "flows" |
| **Event Bus** | Barramento de eventos para desacoplamento (Kafka/NATS) | "fila", "mensageria" (generico) |
| **Vault** | Sistema de armazenamento seguro de secrets/tokens | "cofre de senhas" |

---

## Termos de Dados e Arquitetura

| Termo canonico | Definicao | Nao usar |
|----------------|-----------|----------|
| **Data Warehouse (DWH)** | Repositorio analitico de dados historicos (BigQuery) | "banco de dados", "data lake" (diferente) |
| **OLAP** | Online Analytical Processing — paradigma de consulta analitica | "analitico" (use OLAP quando tecnico) |
| **OLTP** | Online Transaction Processing — paradigma transacional | "transacional" (use OLTP quando tecnico) |
| **dbt** | Ferramenta de transformacao de dados (staging/mart) | "transformacao SQL" |
| **ETL** | Extract, Transform, Load — pipeline de dados | "integracao de dados" (impreciso) |
| **Schema Registry** | Repositorio de contratos de eventos (Avro/JSON) | — |
| **Qdrant** | Banco vetorial para recuperacao semantica (retrieval) | "vetor DB" |
| **OpenTelemetry (OTEL)** | Padrao de instrumentacao de observabilidade | "telemetria" |
| **ADR** | Architecture Decision Record — registro de decisao tecnica | "decisao tecnica", "ata de decisao" |
| **AS IS** | Estado atual da arquitetura / processo | "situacao atual" |
| **TO BE** | Estado futuro desejado da arquitetura / processo | "situacao futura" |

---

## Termos de Agentes de IA

| Termo canonico | Definicao | Nao usar |
|----------------|-----------|----------|
| **Agente** | IA com instrucoes especificas, ferramentas e escopo para executar tarefas | "bot", "assistente", "chatbot" |
| **Agente semi-autonomo** | Agente que executa tarefas automaticamente mas com checkpoint humano | "bot autonomo" |
| **Skill** | Instrucao operacional reutilizavel para agentes (arquivo markdown) | "template de prompt", "instrucao" |
| **Contexto** | Informacao disponivel para o agente em uma sessao | "historico", "memoria de curto prazo" |
| **Cerebro** | Este repositorio — base de conhecimento persistente para agentes | "knowledge base", "brain" |
| **Stream** | Dado operacional vivo mantido em `projetos/` (cliente) ou `areas/` (funcao) — nao usar pasta `streams/` neste repo | "dado em tempo real", "feed" |
| **SDR IA** | Agente automatizado de qualificacao de leads (MQL → SQL) | "bot de prospecao", "SDR bot" |
| **ROI Plan** | Agente gerador de plano de ROI para prospects | "plano de roi", "roi agent" |
| **Progressive Disclosure** | Principio: CLAUDE.md e indice; `empresa/contexto/` tem o detalhe | "documentacao em camadas" |
| **LLM** | Large Language Model — modelo de linguagem de grande escala | "IA", "ChatGPT" (especificos) |

---

## Termos de Produto V4 Food 2.0

| Termo canonico | Definicao |
|----------------|-----------|
| **START** | Plano entry do V4 Food 2.0 — foco em canal proprio |
| **GROWTH** | Plano intermediario — foco em CRM e fidelizacao |
| **SCALE** | Plano avancado — foco em multiplas unidades e governanca |
| **Food Service** | Segmento de restaurantes, dark kitchens e redes alimenticias |
| **Dark Kitchen** | Cozinha apenas para delivery, sem salao |
| **Marketplace** | Plataforma de pedidos online (iFood, Rappi, etc.) |

---

## Vocabulario de Status (para arquivos do cerebro)

| Status | Significado |
|--------|-------------|
| **v1** | Versao estavel, validada |
| **draft** | Rascunho — nao usar como fonte de verdade |
| **revisado** | Versao atualizada sobre uma v1 anterior |
| **deprecated** | Conteudo obsoleto — nao usar |
| **lacuna** | Informacao que deveria existir mas nao foi encontrada |
