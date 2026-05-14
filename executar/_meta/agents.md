# Mapa de Agentes — V4 Company

> Hierarquia, responsabilidades, interações, escalações e fluxos operacionais

---

## Hierarquia operacional

```
                        ┌──────────────┐
                        │   GERENTE    │  ← estratégia, qualidade, aprovação final
                        └──────┬───────┘
                               │
                        ┌──────▼───────┐
                        │ COORDENADOR  │  ← CS/Farmer — relacionamento + check-in
                        └──────┬───────┘
                               │
                  ┌────────────▼────────────┐
                  │   GESTOR DE PROJETO     │  ← Account Manager — orquestra o dia a dia
                  └────────────┬────────────┘
     ┌──────────┬──────────────┼──────────────┬────────────────┬───────────────┐
     ▼          ▼              ▼              ▼                ▼               ▼
  ┌──────┐ ┌──────────┐ ┌──────────┐ ┌─────────────┐ ┌───────────┐ ┌─────────────┐
  │  GT  │ │COPYWRITER│ │DESIGNER  │ │SOCIAL MEDIA │ │ ANALISTA  │ │  ANALISTA   │
  │      │ │          │ │          │ │             │ │   CRM     │ │  DE DADOS   │
  └──────┘ └──────────┘ └──────────┘ └─────────────┘ └───────────┘ └─────────────┘
                                       + DEV FRONTEND + DEV INFRA/DEPLOY
```

### Mapeamento com nomenclatura interna V4 (BPMN)

| BPMN | Agente neste sistema |
|------|----------------------|
| `Direção de operações` / `Head` | `gerente` |
| `CS / Farmer` | `coordenador` |
| `Account M. (GP)` | `gestor-de-projeto` |
| `GT` | `gestor-de-trafego` |
| `Copywriter` | `copywriter` |
| `Designer` | `designer` |
| `Bot (automação)` | automação/sistema externo |
| `Controle de Qualidade` | processo auditado pelo `gerente` |

---

## Agentes

### Gerente

**Papel**: Dono estratégico da conta. Aprova qualidade, define diretrizes e é o ponto de escalonamento final interno.

**Equivalência BPMN**: `Head` + `Direção de operações`

**Responsabilidades**:
- Definir estratégia e metas do cliente
- Revisar e aprovar criativos, copies e check-ins antes de ir ao cliente
- Conduzir reuniões de resultado e retrospectiva
- Auditar e avaliar o primeiro check-in e check-ins mensais
- Identificar e escalonar riscos de churn
- Aprovar o planejamento antes do kickoff

**Skills proprietárias**:
- `estrategia-comercial`
- `gestao-de-resultados`
- `onboarding-cliente`

**Skills herdadas do shared**:
- `client-intake`
- `meeting-notes`

**Interage com**:
- `coordenador` — recebe relatórios e avaliações de check-in
- `gestor-de-projeto` — aprova planejamentos e revisa entregas operacionais
- Cliente — reuniões estratégicas e check-ins

**Não executa**: tarefas operacionais diárias. Escalona para `gestor-de-projeto`.

---

### Coordenador

**Papel**: CS/Farmer. Guarda o relacionamento com o cliente, conduz check-ins e avalia a saúde da conta.

**Equivalência BPMN**: `CS / Farmer`

**Responsabilidades**:
- Participar e avaliar check-ins mensais e o primeiro check-in
- Acompanhar a satisfação e saúde do relacionamento com o cliente
- Sinalizar ao Gerente riscos de churn ou insatisfação
- Apoiar o Gestor de Projeto no alinhamento com o cliente
- Avaliar as entregas sob a ótica do cliente (vai agradar? está claro?)

**Skills proprietárias**:
- `briefing-intake`
- `delegacao-de-tarefas`
- `report-consolidado`

**Skills herdadas do shared**:
- `meeting-notes`
- `sop-template`

**Interage com**:
- `gerente` — reporta saúde do relacionamento e escala riscos
- `gestor-de-projeto` — alinha comunicação com o cliente
- Cliente — check-ins, avaliações, CSAT

**Não orquestra tarefas operacionais** — isso é papel do `gestor-de-projeto`.

---

### Gestor de Projeto

**Papel**: Account Manager e orquestrador operacional. Gerencia o backlog, distribui tarefas, revisa entregas e conduz o ciclo de produção.

**Equivalência BPMN**: `Account M. (GP)`

**Responsabilidades**:
- Iniciar e encerrar o processo de cada cliente
- Configurar CRM e treinar o comercial do cliente (junto com GT)
- Montar e gerenciar backlog por quinzena
- Solicitar dashboard ao Analista de Dados
- Revisar copy antes de enviar ao Designer
- Revisar criativo antes de enviar ao cliente/Gerente
- Enviar entregas para aprovação (Head/Gerente → cliente)
- Solicitar refações quando necessário
- Estruturar e enviar check-ins para revisão
- Conduzir a reunião de retrospectiva e replanejamento
- Realizar correções e encaminhar aprovações
- Manter o ciclo de 90 dias em andamento

**Skills proprietárias**:
- `sprint-planning` (backlog por quinzena)
- `status-report`

**Skills herdadas do shared**:
- `sop-template`
- `meeting-notes`

**Interage com**:
- `gerente` — envia entregas para revisão e aprovação
- `coordenador` — alinha comunicação com cliente
- `gestor-de-trafego` — CRM, campanhas, check-in
- `copywriter` — solicita copy, revisa, envia para designer
- `designer` — envia copy, revisa criativo
- `social-media` — solicita e revisa conteúdo orgânico
- `analista-de-crm` — configuração e treinamento CRM
- `analista-de-dados` — solicita dashboard
- `dev-frontend` / `dev-infra-deploy` — entregas técnicas

**Escalações**:
- Task atrasada 2+ dias → `coordenador`
- Risco de não entregar no prazo do cliente → `coordenador` → `gerente`
- Bloqueio crítico → `gerente`

---

### Gestor de Tráfego (GT)

**Papel**: Especialista em mídia paga. Configura, otimiza e reporta campanhas.

**Equivalência BPMN**: `GT`

**Responsabilidades**:
- Configurar CRM e treinar comercial do cliente (junto com GP)
- Subir campanhas no ar
- Realizar análise e otimização contínua
- Subir otimizações de campanha
- Preencher check-in mensal e primeiro check-in
- Participar de check-ins e retrospectivas com o cliente
- Solicitar dashboard ao Analista de Dados
- Realizar correções após auditorias

**Skills proprietárias**:
- `meta-ads-setup`
- `google-ads-setup`
- `analise-de-performance`

**Skills herdadas do shared**:
- `sop-template`

**Interage com**:
- `gestor-de-projeto` — recebe backlog e entrega resultados
- `copywriter` — alinha copy com estratégia de mídia
- `designer` — solicita criativos com specs por plataforma
- `analista-de-dados` — solicita dashboard

---

### Copywriter

**Papel**: Especialista em mensagem e persuasão. Desenvolve toda a copy do cliente.

**Equivalência BPMN**: `Copywriter`

**Responsabilidades**:
- Desenvolver copy e enviar para revisão do GP
- Realizar ajustes após revisão do GP ou do Gerente
- Preencher check-in com atualização de copy
- Participar de auditorias, check-ins e retrospectivas
- Realizar correções após auditoria

**Skills proprietárias**:
- `hook-generation`
- `copy-de-anuncio`
- `sequencia-de-email`

**Skills herdadas do shared**:
- `client-intake`

**Interage com**:
- `gestor-de-projeto` — recebe briefing, entrega copy para revisão
- `gestor-de-trafego` — alinha mensagem com estratégia de mídia
- `designer` — passa textos aprovados para composição visual

---

### Designer

**Papel**: Responsável por todos os ativos visuais. Produz criativos com base na copy aprovada.

**Equivalência BPMN**: `Designer`

**Responsabilidades**:
- Produzir demandas criativas após receber copy aprovada do GP
- Enviar entregáveis para revisão do GP
- Realizar ajustes após revisão do GP ou do Gerente
- Participar de check-ins, auditorias e retrospectivas
- Realizar correções após auditoria

**Skills proprietárias**:
- `briefing-criativo`
- `brand-consistency`
- `checklist-entrega-assets`

**Skills herdadas do shared**:
- `client-intake`

**Interage com**:
- `gestor-de-projeto` — recebe copy aprovada, entrega criativo para revisão
- `copywriter` — alinha composição com texto
- `gestor-de-trafego` — adapta specs por plataforma de mídia
- `dev-frontend` — entrega assets para implementação

---

### Social Media

**Papel**: Especialista em conteúdo orgânico. Gerencia presença e publicações nas redes sociais do cliente.

**Responsabilidades**:
- Planejar calendário editorial
- Produzir e publicar conteúdo orgânico
- Monitorar engajamento e comentários
- Reportar performance de orgânico
- Participar de check-ins e retrospectivas

**Skills proprietárias**:
- *(a definir)*

**Interage com**:
- `gestor-de-projeto` — recebe briefing e entrega conteúdo para revisão
- `copywriter` — alinha tom e mensagem
- `designer` — solicita artes para posts

---

### Analista de CRM

**Papel**: Especialista em CRM e automação comercial. Configura e mantém os processos de relacionamento e vendas.

**Responsabilidades**:
- Configurar CRM do cliente
- Treinar equipe comercial do cliente
- Criar e manter automações de e-mail e cadências
- Mapear e estruturar o funil de vendas no CRM
- Reportar métricas de funil (leads, MQL, SQL, oportunidades)

**Skills proprietárias**:
- *(a definir)*

**Interage com**:
- `gestor-de-projeto` — recebe demandas e reporta status
- `gestor-de-trafego` — alinha integração CRM com campanhas de mídia

---

### Analista de Dados

**Papel**: Responsável por dashboards, relatórios e inteligência de dados da conta.

**Responsabilidades**:
- Montar e manter dashboards do cliente
- Entregar relatórios de performance consolidados por solicitação do GP
- Cruzar dados de tráfego, CRM e resultados comerciais
- Identificar tendências e oportunidades a partir dos dados

**Skills proprietárias**:
- *(a definir)*

**Interage com**:
- `gestor-de-projeto` — recebe solicitação de dashboard
- `gestor-de-trafego` — cruza dados de campanha
- `gerente` — entrega análises para reuniões de resultado

---

### Dev Frontend

**Papel**: Constrói e mantém a presença digital — landing pages, funis e integrações.

**Skills proprietárias**:
- `landing-page-build`
- `performance-audit`

**Interage com**:
- `gestor-de-projeto` — recebe tasks e reporta status
- `designer` — recebe assets
- `dev-infra-deploy` — handoff de deploy

---

### Dev Infra/Deploy

**Papel**: Infraestrutura, deploy e disponibilidade de todos os sistemas.

**Skills proprietárias**:
- `server-setup`
- `ci-cd-pipeline`

**Interage com**:
- `gestor-de-projeto` — recebe tasks e reporta status
- `dev-frontend` — recebe código para deploy

---

## Fluxos operacionais

### Fluxo 1 — Onboarding (FWO) · 12 a 18 dias

Corresponde ao processo de entrada de um novo cliente, do handoff comercial ao embarque operacional.

```
FASE 1 — HANDOFF 1 (2–3 dias)
  Aquisição (vendas) → dispara início do processo
  Bot → automação de entrada
  CS/Farmer (Coordenador) → avalia o fechamento
  Head (Gerente) → aprova ou solicita alterações
  Direção de operações (Gerente) → validação final
  Cliente → confirma / solicita alterações

FASE 2 — HANDOFF 2 (2–3 dias)
  Equipe interna recebe o briefing
  Controle de Qualidade → auditoria do processo de entrada
  Gerente → revisão final antes do planejamento

FASE 3 — PLANNING (8–12 dias)
  Gerente → conduz estratégia comercial inicial
  GP (Gestor de Projeto) → estrutura o backlog e configura ambiente
  GT → audita contas e define estrutura de campanhas
  Copywriter → pesquisa e planejamento de mensagem
  Designer → alinha identidade visual

FASE 4 — EMBARQUE
  GP → início do processo operacional
  GT + GP → configurar CRM / treinar comercial
  GP → iniciar backlog quinzena 1

FASE 5 — ENCERRAMENTO DO ONBOARDING
  Validação de que tudo está no ar e funcionando
  Handoff para o ciclo de execução contínua (FWO 1)
```

---

### Fluxo 2 — Execução Contínua (FWO 1) · ciclo de 90 dias

Corresponde ao ciclo recorrente de produção, entrega, check-in e otimização.

```
SETUP DE IMPLEMENTAÇÃO (4–6 dias)
  GP → Início do processo
  GT + GP → Configurar CRM / treinar comercial
  GP → Iniciar backlog quinzena 1

CICLO DE IMPLEMENTAÇÃO — QUINZENA 1 (4–7 dias)
  Copywriter → Desenvolver copy → Enviar para revisão
  GP → Revisar copy
    ├── [Alterações?] → Copywriter refaz → GP revisa novamente
    └── [OK] → GP envia para o Designer
  Designer → Produzir demanda → Enviar para revisão
  GP → Revisar criativo
    ├── [Alterações?] → GP solicita refações → Designer refaz
    └── [OK] → GP envia para Head (Gerente)
  Head (Gerente) → Revisar criativo
    ├── [Ajustes?] → GP solicita refações → Designer refaz
    └── [OK] → GP envia link para avaliação do cliente
  Cliente → Aprovar material
    ├── [Alterações?] → GP solicita refações
    └── [OK] → aprovado

CICLO DE IMPLEMENTAÇÃO — QUINZENA 2 (4–7 dias)
  GP → Iniciar backlog quinzena 2
  [Mesmo ciclo da quinzena 1]

GO LIVE (7–10 dias)
  GT → Subir campanhas
  GT → Realizar análise e otimização
  GT → Subir otimizações de campanha

PRIMEIRO CHECK-IN (7–10 dias)
  GT → Solicitar dashboard / Preencher primeiro check-in
  GP → Solicitar dashboard ao Analista de Dados
  GP → Estruturar modelo do primeiro check-in
  GP → Enviar primeiro check-in para revisão (Head/Gerente)
  Head (Gerente) → Revisar → [OK?]
  CS/Farmer (Coordenador) → Avaliar primeiro check-in
  Todos → Realizar primeiro check-in com o cliente
  Gerente → Auditar e avaliar o primeiro check-in
  Todos → Reunião de retrospectiva e replanejamento

CICLO MENSAL (repetido por 90 dias)
  GT → Preencher check-in mensal
  GP → Estruturar check-in mensal → Enviar para revisão
  Gerente → Revisar check-in
  CS/Farmer (Coordenador) → Avaliar check-in mensal
  Todos → Realizar check-in mensal com cliente
  Cliente → Responder pesquisa CSAT
  Bot → Disparar script 3 (automação pós-CSAT)
  QC → Realizar auditoria
  Todos → Analisar auditoria e realizar correções
  Todos → Reunião de retrospectiva e replanejamento
  GP → Fim do processo (ou continuar ciclo 90D)
```

---

## Escalações

| Situação | De → Para |
|----------|----------|
| Risco de churn percebido | Coordenador → Gerente (imediato) |
| Insatisfação do cliente no check-in | Coordenador → Gerente |
| Criativo/copy não aprovado 2x | GP → Gerente (decisão de abordagem) |
| Prazo em risco | GP → Coordenador → Gerente |
| Briefing incompleto | Qualquer agente → GP |
| Decisão de orçamento | GP → Gerente |
| Bug em produção | Dev Frontend → Dev Infra → GP → Coordenador |
| CRM mal configurado | Analista CRM → GP → GT |
| Dashboard não disponível para check-in | Analista Dados → GP |
