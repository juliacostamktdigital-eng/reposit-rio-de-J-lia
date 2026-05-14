# Arquitetura de dados e stack tecnica

**Status:** v2 — alinhado ao operacional da unidade  
**Atualizado:** 2026-04-15  
**Contexto:** a V4 Colli e uma **unidade franqueada**; parte relevante do stack e **cedida ou operada pela matriz**, e parte e **software proprio ou operado pela unidade**.

---

## 1. Visao geral

- **Matriz / mercado:** workspace Google (Gemini, Meet, Sheets, Docs, Slides, etc.), **Ekyte** (gestao de projetos) e ferramentas internas listadas abaixo.
- **Unidade V4 Colli:** integracoes (transcricao, WhatsApp), **Synk RH**, **SDR AI Platform** (antigo V4 AI) e o ecossistema em torno de **BigQuery** e **Flow**.
- **Dados:** a maior parte dos fluxos relevantes **termina ou passa pelo BigQuery**. A partir dai, **oportunidades ganhas** alimentam a criacao de projeto no **Flow**, que e o **software centralizador** e **cockpit de projetos**.
- **Legado em Sheets:** existem **tres planilhas macro de cockpit** no Google Sheets que estao sendo **descontinuadas** com a adocao do Flow.
- **Cockpit consolidado:** dados concatenados do cockpit **voltam para o BigQuery** e alimentam o **dashboard de PE&G**.
- **Infraestrutura:** servidores na **Digital Ocean**, com **CapRover** para gerenciar deploy e servicos.

---

## 2. Software da matriz e do mercado

### Workspace e gestao comercial / projetos

| Item | Papel |
|------|--------|
| **Google Workspace** | Gemini, Meet, Sheets, Docs, Slides e demais apps do ecossistema Google usados no dia a dia. |
| **Ekyte** | Gestao de projetos (workspace da matriz). |

### Ferramentas internas da matriz

| Item | Papel |
|------|--------|
| **MKT Lab** | Conexao de contas **Meta** e **Google** para puxar dados de midia de forma consolidada (“overall”). |
| **Workforce Manager** | Gestao de pessoas da matriz; uso pratico limitado (poucas features): envio de notas fiscais, configuracao de cargos, etc. |
| **HOPS** | Substituto historico do FWO; **em desuso** e com **vida util curta** — praticamente nao entra mais no operacional. |
| **CRM Matriz** | CRM novo de **dados de leads**, integrado a um **microsservico de “service cart”** (produtos e propostas), que por sua vez se conecta a **software de financas tambem desenvolvido pela matriz**. |

---

## 3. Software e automacoes da unidade V4 Colli

| Item | Papel |
|------|--------|
| **Gemini Calls / transcricao de calls** | Calls nas quais o convidado **ferramentas.colli@v4company.com** participa disparam **webhook no n8n**; o conteudo segue para o **BigQuery**, **classificado e organizado**. |
| **WhatsApp (coleta diaria)** | Mensagens coletadas diariamente com destino ao **BigQuery**. |
| **Synk RH** | Software de **gerenciamento de processos** da area de people. |
| **SDR AI Platform** | Evolucao do antigo **V4 AI**; foco em **gerir o produto SDR com IA** junto ao time de tech. |

**Automacao / orquestracao:** **n8n** aparece no fluxo da transcricao (webhook → BigQuery). Outras integracoes pontuais podem existir sem estarem detalhadas neste documento.

---

## 4. BigQuery como eixo analitico

O **BigQuery** concentra ingestao e preparacao de dados vindos das fontes acima (e integracoes associadas).

Fluxo macro:

1. **Fontes** (matriz, unidade, integracoes) → **BigQuery**.
2. Tabela (ou conjunto) de **oportunidades ganhas** no BigQuery → **criacao/atualizacao de projeto no Flow** (cockpit).
3. Dados do **cockpit no Flow**, uma vez concatenados/consolidados, **retornam ao BigQuery**.
4. Esse conjunto no BigQuery **alimenta o dash de PE&G**.

Camadas tipicas (conceitual): landing / raw → transformacao → tabelas analiticas → consumo em **PE&G** e outras visoes.

> Decisao historica de manter **BigQuery** como data warehouse central (vs. alternativas como Supabase para analytics) pode estar documentada em `../../areas/tecnologia/referencias/decisao arquitetura big query.md`, se o arquivo existir no repositorio.

---

## 5. Flow e cockpit

- **Flow** e o **sistema central** para acompanhamento operacional: funciona como **cockpit de projetos**, substituindo gradualmente o modelo baseado em **planilhas macro** no Sheets.
- **Transicao:** **tres planilhas macro** de cockpit no Google Sheets coexistem com o Flow enquanto a migracao nao fecha; tendencia e **extincao** dessas planilhas em favor do Flow.

---

## 6. Infraestrutura

| Componente | Uso |
|------------|-----|
| **Digital Ocean** | Servidores da unidade (e cargas associadas). |
| **CapRover** | Gerenciamento de aplicacoes e servicos em cima dos servidores (deploy, containers, organizacao do ambiente). |

---

## 7. O que este documento nao afirma

Este arquivo descreve o **estado narrado pela operacao** da unidade. Nao lista **microsservicos internos** nem **roadmaps** (barramento de eventos, observabilidade unificada, substitutos de ferramentas) salvo quando forem documentados em referencias dedicadas em `areas/tecnologia/referencias/`.

---

## Referencias opcionais no repositorio

- Arquitetura de dados (diagramas ou notas antigas): `../../areas/tecnologia/referencias/`
- Imagem de referencia, se mantida: `../../areas/tecnologia/referencias/arquitecture data.png`
