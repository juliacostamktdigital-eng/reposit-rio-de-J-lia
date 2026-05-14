# skills_colli_co

> **V4 Company — Assessoria de Marketing e Vendas**  
> Repositório de skills para o sistema multi-agente da V4 Colli

---

## LEIA ISTO PRIMEIRO — Instruções para agentes de IA

Se você é um agente de IA que acabou de acessar este repositório, siga esta ordem:

1. **Leia este arquivo até o fim** — ele explica a estrutura completa
2. **Leia `executar/_meta/agents.md`** — mapa de hierarquia, papéis e escalações de todos os agentes do processo **Executar**
3. **Leia `executar/_meta/taxonomy.md`** — definição de segment, tier, software e specialization
4. **Leia `executar/_meta/versioning.md`** — regras obrigatórias de semver, imutabilidade de `v*.*.*.md`, atualização de `latest.md` e **pull request obrigatória por skill** (sem merge direto de alteração de skill na principal sem revisão)
5. **Se for editar skills em `saber/skills/`:** leia também **`saber/skills/VERSIONAMENTO.md`** — alinha `SKILL.md` Paperclip ao mesmo padrão de `client-intake` (`v{X.Y.Z}.md` + `latest.md` + `CHANGELOG.md`)
6. **Leia o `context.md` do agente que você representa** — ex: `executar/agents/gerente/context.md`
7. **Só se o trabalho for o processo SABER (Paperclip):** leia `saber/README.md` e `saber/_meta/README.md` — não misture com o organograma de `executar/agents/`.

Não invente convenções. Tudo que você precisa saber está nestes arquivos.

---

## Padrão ideal de versionamento de skills

**Referência canónica no repositório:** `executar/shared/client-intake/` — ficheiros `v{X.Y.Z}.md` imutáveis, `latest.md` como cópia integral da versão aprovada, `CHANGELOG.md` e `context.md`.

| Obrigação | Detalhe |
|-----------|---------|
| Nova versão ao alterar conteúdo | Criar um **novo** `v{X.Y.Z}.md`; **nunca** editar versões já publicadas. |
| Promover versão finalizada | Copiar o conteúdo aprovado do novo `v{X.Y.Z}.md` para **`latest.md`** (e para **`SKILL.md`** nas skills SABER Paperclip — ver abaixo). |
| Governança | **Uma pull request por skill** para aprovação; não integrar mudanças de skill diretamente na branch principal sem revisão. |

| Documento | Âmbito |
|-----------|--------|
| [`executar/_meta/versioning.md`](executar/_meta/versioning.md) | Processo Executar: semver, templates, imutabilidade, depreciação, PR por skill |
| [`executar/shared/README.md`](executar/shared/README.md) | Skills partilhadas + ligação ao exemplo `client-intake` |
| [`saber/skills/VERSIONAMENTO.md`](saber/skills/VERSIONAMENTO.md) | Skills SABER: mesmo princípio + `SKILL.md` / `latest.md` / `v*.*.*.md` |

---

## O que é este repositório

Centraliza **skills** (capacidades operacionais documentadas) em dois processos distintos na raiz:

| Pasta | Processo | Conteúdo |
|-------|----------|----------|
| **`executar/`** | Entrega V4 Colli (assessoria mkt/vendas, BPMN handoff/quinenas) | `executar/agents/`, `executar/shared/`, `executar/_meta/` |
| **`saber/`** | SABER × Paperclip (OPS) | `saber/agents/`, `saber/skills/` (em construção) |
| **`projects/`** | Trabalho por projeto | Espaço de trabalho por iniciativa (código, docs, scripts). Convenções e exemplo em `projects/README.md` (`project1_example/`). |
| **`outputs/`** | Resultados obtidos | Artefatos gerados (exports, relatórios, entregas). **Uma subpasta por projeto**, cada uma com `README.md` próprio. Ver `outputs/README.md`. |

Uma skill é um arquivo de instrução versionado que define **como** um agente executa uma tarefa específica.

**Processo SABER (Paperclip / OPS):** pasta **`saber/`** — agents, skills e organograma próprios; ainda sem skills de domínio criadas. Comece por `saber/README.md`.

**Processo Executar (entrega Colli):** pasta **`executar/`** — ver `executar/README.md`.

**Trabalho e resultados (raiz do repositório):**

- **`projects/`** — pasta de **trabalho**: cada projeto ou cliente com pasta própria; o modelo está em `projects/project1_example/`. Detalhes em `projects/README.md`.
- **`outputs/`** — pasta de **resultados**: o que foi gerado na prática. Para cada projeto, criar `outputs/<nome>/` e documentar no `README.md` dentro dessa pasta (índice, datas, referência às skills usadas). Detalhes em `outputs/README.md`.

**Hierarquia (modelo V4 no processo Executar):**
```
Gerente → Coordenador → Gestor de Projeto → Equipe
```

**Agentes (processo Executar):**

| Pasta | Agente | Papel resumido | BPMN equiv. |
|-------|--------|---------------|-------------|
| `executar/agents/gerente/` | Gerente | Estratégia, aprovação de qualidade, resultado final | `Head` / `Direção de operações` |
| `executar/agents/coordenador/` | Coordenador | CS/Farmer — relacionamento e check-ins com cliente | `CS / Farmer` |
| `executar/agents/gestor-de-projeto/` | Gestor de Projeto | Account Manager — orquestra backlog, revisões e aprovações | `Account M. (GP)` |
| `executar/agents/gestor-de-trafego/` | Gestor de Tráfego | Campanhas pagas — Meta Ads e Google Ads | `GT` |
| `executar/agents/copywriter/` | Copywriter | Textos persuasivos — anúncios, e-mail, landing page | `Copywriter` |
| `executar/agents/designer/` | Designer | Ativos visuais e consistência de marca | `Designer` |
| `executar/agents/social-media/` | Social Media | Conteúdo orgânico e gestão de redes sociais | — |
| `executar/agents/analista-de-crm/` | Analista de CRM | Configuração de CRM e automação comercial | — |
| `executar/agents/analista-de-dados/` | Analista de Dados | Dashboards e relatórios de performance | — |
| `executar/agents/dev-frontend/` | Dev Frontend | Landing pages, tracking e integrações | — |
| `executar/agents/dev-infra-deploy/` | Dev Infra/Deploy | Servidores, CI/CD e disponibilidade | — |

**Skills compartilhadas (processo Executar):**

| Pasta | Skill | Quem usa |
|-------|-------|---------|
| `executar/shared/client-intake/` | Coleta estruturada de dados do cliente novo | gerente, coordenador, copywriter, designer |
| `executar/shared/meeting-notes/` | Registro padronizado de reuniões | gerente, coordenador, gestor-de-projeto |
| `executar/shared/sop-template/` | Geração de Procedimento Operacional Padrão | coordenador, gestor-de-projeto, devs, tráfego |

---

## Estrutura de pastas

```
skills_colli_co/
│
├── README.md                         ← você está aqui
├── projects/                         ← trabalho por projeto (ex.: project1_example/)
├── outputs/                          ← resultados obtidos (subpastas + README por projeto)
├── executar/                         ← processo Executar (entrega V4)
│   ├── README.md
│   ├── _meta/                        ← documentação do sistema Executar
│   │   ├── README.md
│   │   ├── agents.md
│   │   ├── versioning.md
│   │   └── taxonomy.md
│   ├── shared/                       ← skills sem owner único (Executar); ver shared/README.md
│   │   ├── README.md
│   │   ├── context.md
│   │   └── {skill-name}/
│   │       ├── context.md
│   │       ├── v1.0.0.md
│   │       ├── latest.md
│   │       └── CHANGELOG.md
│   └── agents/
│       └── {agent-name}/
│           ├── context.md
│           └── {skill-name}/
│               ├── context.md
│               ├── v1.0.0.md
│               ├── latest.md
│               └── CHANGELOG.md
│
└── saber/                            ← processo SABER (Paperclip)
    ├── README.md
    ├── _meta/
    ├── agents/
    └── skills/
        ├── README.md
        └── VERSIONAMENTO.md          ← versionamento oficial alinhado a client-intake
```

---

## Como CONSUMIR uma skill (processo Executar)

```
1. executar/agents/{agente}/{skill}/context.md   → propósito, inputs, outputs e restrições
2. executar/agents/{agente}/{skill}/latest.md    → protocolo de execução atual
3. Versão específica → executar/agents/{agente}/{skill}/v{X}.Y.Z.md
```

**Regra de ouro:** `latest.md` é sempre o conteúdo correto para uso em produção.

---

## Como CRIAR uma nova skill (Executar)

```
Passo 1 — Decida onde fica
  - Usada por 1 agente?         → executar/agents/{agente}/{nova-skill}/
  - Usada por 2+ agentes?      → executar/shared/{nova-skill}/

Passo 2 — Crie o context.md com frontmatter YAML obrigatório:
  ---
  skill: nome-da-skill
  owner: nome-do-agente
  latest: v1.0.0
  status: active
  segment: [b2b, b2c, b2b2c]
  tier: [starter, growth, scale, enterprise]
  software: [mcp, api, manual]
  specialization: [ecom, inside-sales, local-business, saas, infoproduto]
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  ---

Passo 3 — Escreva o conteúdo em v1.0.0.md
Passo 4 — Copie v1.0.0.md → latest.md
Passo 5 — Crie CHANGELOG.md com a entrada inicial
```

---

## Como ATUALIZAR uma skill existente (Executar)

```
Passo 1 — Tipo de mudança (regras em executar/_meta/versioning.md):
  MAJOR / MINOR / PATCH

Passo 2 — Novo arquivo versionado (ex: v1.1.0.md); nunca edite versões antigas

Passo 3 — Atualize latest.md

Passo 4 — Atualize context.md (latest, updated)

Passo 5 — CHANGELOG.md
```

---

## Taxonomia rápida

| Eixo | Valores válidos |
|------|----------------|
| `segment` | `b2b` `b2c` `b2b2c` |
| `tier` | `starter` `growth` `scale` `enterprise` |
| `software` | `mcp` `api` `manual` |
| `specialization` | `ecom` `inside-sales` `local-business` `saas` `infoproduto` |

Definições completas em `executar/_meta/taxonomy.md`.

---

## Hierarquia de agentes (resumo — Executar)

```
GERENTE
    ↓
COORDENADOR
    ↓
GESTOR DE PROJETO
    ↓
┌──────┬──────────┬──────────┬─────────────┬───────────┬────────────┬──────────┬─────────┐
GT   COPY    DESIGNER   SOCIAL   AN.CRM   AN.DADOS   DEV FRONT   DEV INFRA
```

Hierarquia detalhada, interações, escalações e fluxos BPMN: `executar/_meta/agents.md`

---

## Regras que toda IA deve seguir (skills Executar)

1. **Nunca edite um arquivo `v{X}.Y.Z.md`** — versões são imutáveis após criação
2. **Sempre atualize `latest.md` e `context.md`** ao criar nova versão
3. **Sempre registre no `CHANGELOG.md`** toda mudança
4. **Respeite o owner** — só altere skills do agente que você representa ou de `executar/shared/`
5. **Siga a taxonomia exata**
6. **Skill em `executar/shared/`** só entra ali se for usada por 2+ agentes sem modificação
7. **`draft`** antes de produção quando aplicável

---

## Referências completas (Executar)

| Documento | Conteúdo |
|-----------|---------|
| `executar/README.md` | Visão do processo Executar |
| `executar/_meta/README.md` | Visão geral detalhada do sistema de skills Executar |
| `executar/_meta/agents.md` | Hierarquia, papéis, interações e escalações |
| `executar/_meta/versioning.md` | Versionamento + templates + PR por skill |
| `executar/shared/README.md` | Skills partilhadas e padrão `client-intake` |
| `saber/skills/VERSIONAMENTO.md` | Versionamento skills SABER (`SKILL.md` + `latest.md` + `v*.*.*.md`) |
| `executar/_meta/taxonomy.md` | segment, tier, software, specialization |
| `executar/shared/context.md` | Promoção de skills para shared |
