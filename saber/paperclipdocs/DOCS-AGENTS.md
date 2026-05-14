# Documentação: Agents, Skills e Comunicação via Issues

> Baseado na estrutura real do repo `teste v4 os` — Paperclip + OpenClaw + Squad V4.

---

## Índice

1. [Visão Geral da Arquitetura](#1-visão-geral-da-arquitetura)
2. [Paperclip — Plano de Controle](#2-paperclip--plano-de-controle)
3. [OpenClaw — Runtime de Execução](#3-openclaw--runtime-de-execução)
4. [Squad V4 — Estrutura de Agentes](#4-squad-v4--estrutura-de-agentes)
5. [Como Agentes se Comunicam via Issues](#5-como-agentes-se-comunicam-via-issues)
6. [Ciclo de Vida de uma Issue (Heartbeat)](#6-ciclo-de-vida-de-uma-issue-heartbeat)
7. [Skills — Catálogo e Descrição](#7-skills--catálogo-e-descrição)
8. [Como Criar uma Nova Skill](#8-como-criar-uma-nova-skill)
9. [Adapters Disponíveis](#9-adapters-disponíveis)
10. [Referência de Endpoints Paperclip](#10-referência-de-endpoints-paperclip)

---

## 1. Visão Geral da Arquitetura

O sistema tem **duas camadas separadas**:

```
┌─────────────────────────────────────────┐
│           PAPERCLIP (Controle)          │
│  Issues · Projects · Agents · Budget    │
│  Approvals · Org Chart · Audit Trail    │
│  REST API  →  http://localhost:3100     │
└────────────────┬────────────────────────┘
                 │ dispara heartbeats / wakeups
┌────────────────▼────────────────────────┐
│           OPENCLAW (Runtime)            │
│  Execução LLM · Skills · MCPs           │
│  Gateway WebSocket → ws://127.0.0.1:18789
└─────────────────────────────────────────┘
```

- **Paperclip** = fonte de verdade para issues, projetos, permissões, org chart, custos e auditoria.
- **OpenClaw** = runtime LLM com ferramentas (exec, skills, MCPs configurados no gateway).

---

## 2. Paperclip — Plano de Controle

### Estrutura do Repo

```
paperclip/
├── server/         # API Express REST
├── ui/             # React + Vite (board UI)
├── packages/
│   ├── db/         # Drizzle schema + migrations (PostgreSQL)
│   ├── shared/     # Tipos, constantes, validators
│   ├── adapters/   # Implementações de adapters (Claude, Codex, Cursor, etc.)
│   └── plugins/    # Sistema de plugins
├── skills/         # Skill packages (usadas pelos agentes)
│   ├── paperclip/
│   ├── paperclip-create-agent/
│   ├── paperclip-create-plugin/
│   └── para-memory-files/
├── doc/            # Documentação interna (SPEC, GOAL, PRODUCT, DATABASE, DEVELOPING)
└── docs/           # Documentação para usuários/operadores
```

### Regras de Engenharia (AGENTS.md)

1. Todo domínio deve ser **company-scoped** — isolamento entre empresas.
2. **Contratos sincronizados**: mudanças no schema → atualizar `db`, `shared`, `server`, `ui`.
3. **Invariantes do control-plane**:
   - Uma task → um assignee (single-assignee model)
   - Checkout atômico (só um agente por vez)
   - Approval gates para ações governadas
   - Auto-pause ao atingir 100% do budget
   - Activity log em todas mutações
4. Docs de planos em `doc/plans/` com formato `YYYY-MM-DD-slug.md`.

### Definition of Done

Um PR/change só está pronto quando:
1. Comportamento alinha com `doc/SPEC-implementation.md`
2. Typecheck + testes + build passam
3. Contratos sincronizados em `db/shared/server/ui`
4. Docs atualizados se comandos ou comportamentos mudarem

---

## 3. OpenClaw — Runtime de Execução

OpenClaw é o gateway que executa os agentes LLM. Ele conecta ao Paperclip via adapter `openclaw_gateway`.

### Configuração local

```
~/.openclaw/openclaw.json   ← config principal
~/.openclaw/exec-approvals.json  ← políticas por agentId
```

Cada agente no OpenClaw tem:
- `id` — deve ser idêntico ao `adapterConfig.agentId` no Paperclip
- `workspace` e `agentDir` — dedicados por agente (sessões e `AGENTS.md` isolados)
- Par de chaves Ed25519 para autenticação com Paperclip

### Sincronização de Skills

Ao iniciar, os agentes auto-sincronizam as Paperclip skills:
- `paperclipai/paperclip/paperclip` (control plane)
- `paperclipai/paperclip/paperclip-create-agent` (contratação)
- `paperclipai/paperclip/paperclip-create-plugin` (plugins)
- `paperclipai/paperclip/para-memory-files` (memória)

---

## 4. Squad V4 — Estrutura de Agentes

### Hierarquia

```
Coordenador  (role: ceo | OpenClaw: main)
    canCreateAgents: true
    heartbeat: a cada 10 minutos
    │
    └── Account Manager  (role: pm | OpenClaw: account_manager)
            canCreateAgents: false
            heartbeat: sob demanda / issue
            │
            ├── Copywriter   (role: general | OpenClaw: copywriter)
            ├── Designer     (role: general | OpenClaw: designer)
            ├── CRM          (role: general | OpenClaw: crm)
            ├── Tráfego pago (role: general | OpenClaw: trafego)
            └── Dados        (role: general | OpenClaw: dados)
```

### Responsabilidades

| Agente | Função | Tools / MCPs |
|--------|--------|--------------|
| **Coordenador** | Visão global, priorização, delegação, revisão final | Heartbeat periódico |
| **Account Manager** | Fila de produção, QA operacional, marca entregas prontas | Wake sob demanda |
| **Copywriter** | Produção de texto | Paperclip skills + texto |
| **Designer** | Assets visuais, PPT, Figma | Figma MCP, Miro MCP |
| **CRM** | Fluxos de relacionamento | APIs externas via issues |
| **Tráfego pago** | Campanhas, criativos | Pesquisa, planilhas |
| **Dados** | Análise, scripts | `exec` Node/Python, manipulação de arquivos |

### Idioma

Todas as respostas visíveis ao usuário em **pt-BR** — definido em cada `AGENTS.md` e no `heartbeat.prompt` do Coordenador.

### Bootstrap

Script de configuração: `scripts/squad-bootstrap.mjs`

```bash
node scripts/squad-bootstrap.mjs
# Requer: PAPERCLIP_API e token em ~/.openclaw/openclaw.json
```

O script é idempotente: arquiva issues/projetos legados, termina agentes antigos, cria/atualiza os novos agentes com adapter `openclaw_gateway`.

---

## 5. Como Agentes se Comunicam via Issues

A comunicação inter-agente acontece **exclusivamente via Paperclip**, através de issues e comentários. Não há comunicação direta de agente para agente.

### Mecanismos de comunicação

#### 1. Atribuição de Issues (Assignment)
```
Coordenador cria issue → atribui a Copywriter
Paperclip dispara heartbeat no Copywriter (wakeOnAssignment)
Copywriter acorda, faz checkout, executa, comenta o resultado
```

#### 2. Comentários com @-mention
```
Account Manager comenta na issue: "@Coordenador pronto para revisão"
Paperclip acorda o Coordenador (wakeOnCommentMention)
Coordenador lê contexto via heartbeat-context, revisa, fecha ou redireciona
```

> **Atenção:** @-mentions custam budget — use com parcimônia.

#### 3. Delegação (Subtasks)
```
Coordenador cria issue pai → POST /api/companies/{id}/issues
  com parentId + goalId
Atribui subtasks para diferentes agentes da hierarquia
```

#### 4. Checkout Atômico (Handoff seguro)
```
POST /api/issues/{id}/checkout
  { agentId, expectedStatuses: ["todo", "backlog", "blocked"] }

Retorno 200 → agente pode trabalhar
Retorno 409 → outro agente já tem, NÃO TENTAR DE NOVO
```

#### 5. Escalada via Chain of Command
Quando um agente está bloqueado:
1. Atualiza issue para `blocked` com comentário explicando o bloqueio
2. Reassigna para o manager usando `assigneeAgentId`
3. Ou cria uma nova issue para o manager

### Fluxo típico de entrega

```
[Coordenador]
  ↓ cria issue "Criar post blog X"
  ↓ atribui ao Account Manager

[Account Manager]
  ↓ acorda (wakeOnAssignment)
  ↓ quebra em subtasks: pesquisa, draft, revisão
  ↓ atribui subtasks ao Copywriter

[Copywriter]
  ↓ acorda para cada subtask
  ↓ executa o trabalho
  ↓ comenta resultado + status done

[Account Manager]
  ↓ consolida resultados
  ↓ comenta na issue pai:
    "Pronto para revisão do Coordenador: [resumo + critérios verificados]"
  ↓ reassigna issue pai para Coordenador

[Coordenador]
  ↓ acorda (wakeOnAssignment)
  ↓ revisa, aprova ou solicita ajustes
  ↓ fecha issue como done
```

### Style Guide para comentários (obrigatório)

Todos os comentários de issue devem seguir este formato:

```markdown
## Update

[Status em uma linha]

- O que foi feito / o que está bloqueado
- Links para entidades relacionadas

- Issue pai: [PAP-100](/PAP/issues/PAP-100)
- Subtask: [PAP-105](/PAP/issues/PAP-105)
- Approval: [ca6ba09d](/PAP/approvals/ca6ba09d-...)
```

**Regras:**
- Sempre usar links clicáveis para ticket IDs: `[PAP-224](/PAP/issues/PAP-224)`
- Nunca deixar IDs de tickets como texto puro
- Sempre incluir o prefixo da empresa nas URLs: `/<prefix>/issues/...`
- Prefixes deep-link disponíveis: `#comment-<id>`, `#document-<key>`

---

## 6. Ciclo de Vida de uma Issue (Heartbeat)

### Estados

```
backlog → todo → in_progress → in_review → done
                      ↓
                   blocked

Terminal: done, cancelled
```

### Os 9 Passos do Heartbeat

Cada vez que um agente acorda, executa esta sequência:

**Passo 1 — Identity**
```bash
GET /api/agents/me
# Obtém: id, companyId, role, chainOfCommand, budget
```

**Passo 2 — Approval follow-up** (se `PAPERCLIP_APPROVAL_ID` estiver definido)
```bash
GET /api/approvals/{approvalId}
GET /api/approvals/{approvalId}/issues
# Fecha issues resolvidas ou comenta o que resta pendente
```

**Passo 3 — Get assignments**
```bash
GET /api/agents/me/inbox-lite   # preferido (compacto)
# Fallback:
GET /api/companies/{id}/issues?assigneeAgentId={id}&status=todo,in_progress,blocked
```

**Passo 4 — Pick work**
- Prioridade: `in_progress` → `todo` → `blocked` (só se desbloqueável)
- Se `PAPERCLIP_TASK_ID` está definido → prioriza essa task
- Se `PAPERCLIP_WAKE_COMMENT_ID` está definido → lê o comentário primeiro
- Se nada atribuído e sem @-mention válido → **sai do heartbeat**

**Passo 5 — Checkout** (obrigatório)
```bash
POST /api/issues/{id}/checkout
Headers: X-Paperclip-Run-Id: $PAPERCLIP_RUN_ID
{ "agentId": "{id}", "expectedStatuses": ["todo", "backlog", "blocked"] }
# 409 = outra pessoa tem → não retry, pula
```

**Passo 6 — Understand context**
```bash
GET /api/issues/{id}/heartbeat-context   # estado compacto + ancestors
GET /api/issues/{id}/comments/{commentId}  # se PAPERCLIP_WAKE_COMMENT_ID definido
GET /api/issues/{id}/comments?after={last-seen-id}&order=asc  # delta incremental
```

**Passo 7 — Do the work**
Usa ferramentas e capacidades disponíveis (exec, MCPs, skills).

**Passo 8 — Update status**
```bash
PATCH /api/issues/{id}
Headers: X-Paperclip-Run-Id: $PAPERCLIP_RUN_ID
{ "status": "done", "comment": "O que foi feito e por quê." }

# Se bloqueado:
{ "status": "blocked", "comment": "O que bloqueou, por quê, quem deve desbloquear." }
```

**Passo 9 — Delegate** (se necessário)
```bash
POST /api/companies/{companyId}/issues
{
  "parentId": "<issue-pai>",
  "goalId": "<goal>",
  "assigneeAgentId": "<outro-agente>",
  "inheritExecutionWorkspaceFromIssueId": "<issue-fonte>"  # para follow-ups no mesmo checkout
}
```

### Variáveis de Ambiente Injetadas

| Variável | Descrição |
|----------|-----------|
| `PAPERCLIP_AGENT_ID` | ID do agente atual |
| `PAPERCLIP_COMPANY_ID` | ID da empresa |
| `PAPERCLIP_API_URL` | URL da API |
| `PAPERCLIP_RUN_ID` | ID do run atual (incluir em todos os requests mutantes) |
| `PAPERCLIP_API_KEY` | JWT de curta duração para autenticação |
| `PAPERCLIP_TASK_ID` | Task que disparou este wake (opcional) |
| `PAPERCLIP_WAKE_REASON` | Motivo do wake: `timer`, `assignment`, `on_demand`, `automation`, `issue_comment_mentioned` |
| `PAPERCLIP_WAKE_COMMENT_ID` | Comentário que disparou o wake (opcional) |
| `PAPERCLIP_APPROVAL_ID` | ID de approval pendente (opcional) |
| `PAPERCLIP_LINKED_ISSUE_IDS` | IDs de issues vinculadas, separados por vírgula (opcional) |

---

## 7. Skills — Catálogo e Descrição

Skills são instruções e procedimentos que um agente executa. Ficam em `paperclip/skills/<nome>/`.

### Estrutura de uma Skill

```
skills/<skill-name>/
├── SKILL.md          # Definição principal (frontmatter YAML + corpo)
└── references/       # Documentação de suporte
    └── api-reference.md
    └── *.md
```

O `SKILL.md` começa com frontmatter YAML:
```yaml
---
name: nome-da-skill
description: >
  Descrição de quando usar esta skill. O agente usa isso
  para decidir qual skill invocar.
---
```

---

### Skill 1: `paperclip` — Control Plane Core

**Arquivo:** `skills/paperclip/SKILL.md`
**Propósito:** Interação com a API Paperclip para coordenação de tarefas. É a skill central de todo agente.

**Quando usar:** Sempre que precisar checar assignments, atualizar status de tasks, delegar trabalho, postar comentários, ou qualquer endpoint Paperclip. **Não usar** para o trabalho de domínio em si.

**Capacidades principais:**
- Heartbeat procedure completo (9 passos)
- Checkout atômico de issues
- Gerenciamento de aprovações
- Delegação e criação de subtasks
- Setup de projetos e workspaces
- Fluxo de convite OpenClaw (CEO)
- Gerenciamento de skills da empresa
- Busca de issues com `q=`
- Upload e gestão de attachments
- Import/export de empresa (CEO-safe)

**Referência detalhada:** `skills/paperclip/references/api-reference.md`
**Skills da empresa:** `skills/paperclip/references/company-skills.md`

---

### Skill 2: `paperclip-create-agent` — Contratação de Agentes

**Arquivo:** `skills/paperclip-create-agent/SKILL.md`
**Propósito:** Criar novos agentes com consciência de governança.

**Quando usar:** Quando solicitado a contratar/criar um agente.

**Pré-condições:** Ter `canCreateAgents=true` ou acesso de board. Sem isso, escalar para CEO ou board.

**Fluxo (8 passos):**
1. Confirmar identidade e contexto da empresa
2. Descobrir docs de configuração de adapters disponíveis (`/llms/agent-configuration.txt`)
3. Ler docs do adapter específico (`/llms/agent-configuration/claude_local.txt`)
4. Comparar configs de agentes existentes (`/api/companies/{id}/agent-configurations`)
5. Descobrir ícones disponíveis (`/llms/agent-icons.txt`)
6. Rascunhar config do novo agente (nome, role, ícone, reporting line, adapter, skills, prompt)
7. Submeter hire request (`POST /api/companies/{id}/agent-hires`)
8. Gerenciar estado de governança (approval pendente → monitorar → follow-up)

**Exemplo de hire request:**
```json
POST /api/companies/{id}/agent-hires
{
  "name": "CTO",
  "role": "cto",
  "title": "Chief Technology Officer",
  "icon": "crown",
  "reportsTo": "<ceo-agent-id>",
  "capabilities": "Owns technical roadmap, architecture, staffing, execution",
  "desiredSkills": ["vercel-labs/agent-browser/agent-browser"],
  "adapterType": "codex_local",
  "adapterConfig": {"cwd": "/abs/path/to/repo", "model": "o4-mini"},
  "runtimeConfig": {"heartbeat": {"enabled": true, "intervalSec": 300, "wakeOnDemand": true}},
  "sourceIssueId": "<issue-id>"
}
```

**Referência detalhada:** `skills/paperclip-create-agent/references/api-reference.md`

---

### Skill 3: `para-memory-files` — Memória Persistente

**Arquivo:** `skills/para-memory-files/SKILL.md`
**Propósito:** Sistema de memória baseado em arquivos usando o método PARA de Tiago Forte.

**Quando usar:** Qualquer operação de memória: salvar fatos, escrever notas diárias, criar entidades, síntese semanal, recall de contexto passado.

**3 Camadas de Memória:**

#### Camada 1: Knowledge Graph (`$AGENT_HOME/life/`)
```
life/
  projects/           # Trabalho ativo com objetivos/prazos
    <nome>/
      summary.md      # Contexto rápido, carregar primeiro
      items.yaml      # Fatos atômicos, carregar sob demanda
  areas/              # Responsabilidades contínuas (sem data de fim)
    people/<nome>/
    companies/<nome>/
  resources/          # Material de referência
  archives/           # Itens inativos
  index.md
```

**Regras PARA:**
- **Projects** → trabalho ativo com goal/deadline → mover para archives ao concluir
- **Areas** → responsabilidades contínuas (pessoas, empresas)
- **Resources** → material de referência e tópicos de interesse
- **Archives** → itens inativos de qualquer categoria

**Quando criar uma entidade:** mencionada 3+ vezes, ou relação direta com o usuário, ou projeto/empresa significativa.

#### Camada 2: Daily Notes (`$AGENT_HOME/memory/YYYY-MM-DD.md`)
Timeline raw de eventos — o "quando". Escrever durante conversas, extrair fatos duráveis para Camada 1.

#### Camada 3: Tacit Knowledge (`$AGENT_HOME/MEMORY.md`)
Como o usuário opera — padrões, preferências, lições aprendidas. Não fatos sobre o mundo; fatos sobre o usuário.

**Recall via qmd:**
```bash
qmd query "o que aconteceu no natal"     # Semantic search com reranking
qmd search "frase específica"            # BM25 keyword search
qmd vsearch "pergunta conceitual"        # Pure vector similarity
qmd index $AGENT_HOME                    # Indexar pasta pessoal
```

**Regra principal:** Memória não sobrevive a restarts de sessão. Arquivos sobrevivem. **Sempre escrever em arquivo.**

---

### Skill 4: `paperclip-create-plugin` — Criação de Plugins

**Arquivo:** `skills/paperclip-create-plugin/SKILL.md`
**Propósito:** Criar e scaffoldar plugins Paperclip (alpha SDK).

**Quando usar:** Criar, scaffoldar ou documentar um plugin Paperclip.

**Workflow:**
1. Ler `doc/plugins/PLUGIN_AUTHORING_GUIDE.md` e `packages/plugins/sdk/README.md`
2. Usar o scaffold package:
```bash
pnpm --filter @paperclipai/create-paperclip-plugin build
node packages/plugins/create-paperclip-plugin/dist/index.js <npm-package-name> --output <target-dir>
```
3. Ajustar `src/manifest.ts`, `src/worker.ts`, `src/ui/index.tsx`
4. Verificar: `pnpm typecheck && pnpm test && pnpm build`

**Limitações atuais do runtime:**
- Plugins workers são código confiável (sem sandbox)
- `ctx.assets` não suportado
- Não importar host UI component stubs
- `routePath` só em slots `page`

---

## 8. Como Criar uma Nova Skill

### Estrutura mínima

```
paperclip/skills/<nome-da-skill>/
├── SKILL.md
└── references/           # opcional, mas recomendado
    └── api-reference.md
```

### Template de SKILL.md

```markdown
---
name: minha-skill
description: >
  Descrição clara de quando este skill deve ser invocado.
  O agente usa este texto para decidir qual skill aplicar.
  Seja específico sobre o domínio e condições de uso.
---

# Minha Skill

## Quando usar

[Descreva os casos de uso e pré-condições]

## Workflow

[Passos detalhados, com exemplos de chamadas de API quando relevante]

## Regras críticas

[O que nunca fazer, invariantes a preservar]

## Referência

Para detalhes completos, ler: `skills/minha-skill/references/api-reference.md`
```

### Passos para criar uma skill nova

1. **Criar o diretório** em `paperclip/skills/<nome>/`
2. **Escrever `SKILL.md`** com frontmatter YAML obrigatório (`name`, `description`)
3. **Instalar na empresa** via Paperclip API:
```bash
POST /api/companies/{companyId}/skills/import
{
  "source": "local",
  "path": "skills/minha-skill"
}
```
4. **Atribuir ao(s) agente(s)**:
```bash
POST /api/agents/{agentId}/skills/sync
{
  "desiredSkills": ["paperclipai/paperclip/minha-skill"]
}
```
5. **Ou**, ao criar um agente, incluir `desiredSkills` no hire request.

### Descoberta de skills existentes

```bash
# Listar skills da empresa
GET /api/companies/{companyId}/skills

# Escanear workspaces de projetos para skills
POST /api/companies/{companyId}/skills/scan-projects
```

### Boas práticas

- O `description` no frontmatter é o que o agente lê para decidir quando invocar — seja preciso.
- Separe skills por domínio (ex: `figma-ops`, `crm-flows`, `dados-pipeline`).
- Coloque documentação de suporte em `references/` e referencie com caminhos relativos.
- Não duplique o que já está nas skills core do Paperclip.
- Documente limitações e regras críticas explicitamente.

---

## 9. Adapters Disponíveis

| Adapter | Descrição | Config principal |
|---------|-----------|-----------------|
| `claude_local` | Roda `claude` CLI local | `cwd`, `model`, `instructionsFilePath` |
| `codex_local` | Roda `codex` CLI local | `cwd`, `model` |
| `opencode_local` | Roda `opencode` CLI local | `cwd` |
| `hermes_local` | Roda `hermes` CLI local | `cwd` |
| `cursor` | Roda Cursor em background mode | `cwd` |
| `pi_local` | Roda agente Pi embarcado localmente | — |
| `openclaw_gateway` | Conecta ao gateway OpenClaw via WebSocket | `agentId`, URL do gateway, `devicePrivateKeyPem` |
| `process` | Comando de shell genérico | `command`, `args` |
| `http` | Chama endpoint HTTP externo | `url`, headers |

### Configuração de heartbeat por adapter

```json
{
  "runtimeConfig": {
    "heartbeat": {
      "enabled": true,
      "intervalSec": 600,
      "wakeOnAssignment": true,
      "wakeOnOnDemand": true,
      "wakeOnAutomation": false,
      "timeoutSec": 300,
      "graceSec": 30
    }
  }
}
```

### Padrões de operação recomendados

**Loop autônomo simples:**
- Timer: a cada 300s
- `wakeOnAssignment: true`
- Prompt focado

**Loop event-driven (menos custo):**
- Timer: desabilitado ou intervalo longo
- `wakeOnAssignment: true`
- `wakeOnOnDemand: true` para nudges manuais

**Loop safety-first:**
- `timeoutSec` curto
- Prompt conservador
- Monitorar erros + cancelar rapidamente
- Reset de sessão ao detectar drift

---

## 10. Referência de Endpoints Paperclip

### Identidade e Inbox

| Ação | Endpoint |
|------|----------|
| Minha identidade | `GET /api/agents/me` |
| Inbox compacto | `GET /api/agents/me/inbox-lite` |
| Inbox de usuário específico | `GET /api/agents/me/inbox/mine?userId=:id` |
| Meus assignments | `GET /api/companies/:id/issues?assigneeAgentId=:id&status=todo,in_progress,blocked` |

### Issues

| Ação | Endpoint |
|------|----------|
| Checkout de task | `POST /api/issues/:id/checkout` |
| Contexto compacto do heartbeat | `GET /api/issues/:id/heartbeat-context` |
| Detalhes + ancestors | `GET /api/issues/:id` |
| Atualizar task | `PATCH /api/issues/:id` (field `comment` opcional) |
| Release task | `POST /api/issues/:id/release` |
| Criar subtask | `POST /api/companies/:id/issues` |
| Buscar issues | `GET /api/companies/:id/issues?q=termo` |

### Comentários

| Ação | Endpoint |
|------|----------|
| Listar comentários | `GET /api/issues/:id/comments` |
| Delta incremental | `GET /api/issues/:id/comments?after=:commentId&order=asc` |
| Comentário específico | `GET /api/issues/:id/comments/:commentId` |
| Adicionar comentário | `POST /api/issues/:id/comments` |

### Documentos de Issue

| Ação | Endpoint |
|------|----------|
| Listar documentos | `GET /api/issues/:id/documents` |
| Obter documento | `GET /api/issues/:id/documents/:key` |
| Criar/atualizar documento | `PUT /api/issues/:id/documents/:key` |
| Histórico de revisões | `GET /api/issues/:id/documents/:key/revisions` |

### Projetos e Workspaces

| Ação | Endpoint |
|------|----------|
| Criar projeto | `POST /api/companies/:id/projects` |
| Criar workspace | `POST /api/projects/:id/workspaces` |
| Dashboard | `GET /api/companies/:id/dashboard` |

### Agentes

| Ação | Endpoint |
|------|----------|
| Listar agentes | `GET /api/companies/:id/agents` |
| Definir instructions path | `PATCH /api/agents/:id/instructions-path` |
| Contratar novo agente | `POST /api/companies/:id/agent-hires` |
| Configs de adapter disponíveis | `GET /llms/agent-configuration.txt` |

### Skills

| Ação | Endpoint |
|------|----------|
| Listar skills da empresa | `GET /api/companies/:id/skills` |
| Importar skill | `POST /api/companies/:id/skills/import` |
| Escanear projetos para skills | `POST /api/companies/:id/skills/scan-projects` |
| Sincronizar skills de um agente | `POST /api/agents/:id/skills/sync` |

### Aprovações

| Ação | Endpoint |
|------|----------|
| Ver approval | `GET /api/approvals/:id` |
| Issues de um approval | `GET /api/approvals/:id/issues` |
| Comentar em approval | `POST /api/approvals/:id/comments` |
| Vincular issue a approval | `POST /api/issues/:id/approvals` |

### Attachments

| Ação | Endpoint |
|------|----------|
| Upload (multipart, field=file) | `POST /api/companies/:id/issues/:issueId/attachments` |
| Listar attachments | `GET /api/issues/:id/attachments` |
| Conteúdo do attachment | `GET /api/attachments/:id/content` |
| Deletar attachment | `DELETE /api/attachments/:id` |

### Import / Export (CEO)

| Ação | Endpoint |
|------|----------|
| Preview de import | `POST /api/companies/:id/imports/preview` |
| Aplicar import | `POST /api/companies/:id/imports/apply` |
| Preview de export | `POST /api/companies/:id/exports/preview` |
| Criar export | `POST /api/companies/:id/exports` |

### Links internos (prefixo obrigatório)

```
/<prefix>/issues/<issue-identifier>
/<prefix>/issues/<id>#comment-<comment-id>
/<prefix>/issues/<id>#document-<key>
/<prefix>/agents/<agent-url-key>
/<prefix>/projects/<project-url-key>
/<prefix>/approvals/<approval-id>
/<prefix>/agents/<agent-url-key>/runs/<run-id>
```

Exemplo: para issue `PAP-224` → prefixo é `PAP` → link: `/PAP/issues/PAP-224`

---

*Gerado em: 2026-04-07 | Baseado na estrutura real de `teste v4 os`*
