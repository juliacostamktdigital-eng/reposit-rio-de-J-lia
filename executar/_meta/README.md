# V4 Company — Sistema de Skills para Multi-Agentes (processo Executar)

> Assessoria de Marketing e Vendas  
> Versão do sistema: `1.0.0` — Atualizado em: 2026-04-06

Este diretório vive em **`executar/_meta/`** e documenta o processo **Executar** (entrega). Para a visão do repositório inteiro, veja o `README.md` na raiz.

---

## O que é este repositório

Este repositório centraliza todas as **skills** (capacidades operacionais documentadas) dos agentes da V4 Company no processo **Executar**. Cada skill é um bloco de instrução versionado que define como um agente deve executar uma tarefa específica.

O sistema foi projetado para:

- **Reutilização** — skills do `executar/shared/` são herdadas por múltiplos agentes
- **Rastreabilidade** — cada mudança de comportamento fica registrada com versão e data
- **Especialização** — cada skill declara explicitamente para qual segmento, tier e software se aplica
- **Escalabilidade** — novos agentes e skills seguem o mesmo padrão e podem ser adicionados sem quebrar os existentes

---

## Estrutura de pastas

```
skills_colli_co/
├── README.md
├── executar/
│   ├── README.md                 ← visão do processo Executar
│   ├── _meta/                    ← você está aqui
│   │   ├── README.md
│   │   ├── versioning.md
│   │   ├── agents.md
│   │   └── taxonomy.md
│   ├── shared/
│   │   ├── context.md
│   │   └── {skill-name}/
│   │       ├── context.md
│   │       ├── v1.0.0.md
│   │       ├── latest.md
│   │       └── CHANGELOG.md
│   └── agents/
│       ├── gerente/
│       ├── coordenador/
│       ├── gestor-de-trafego/
│       ├── copywriter/
│       ├── gestor-de-projeto/
│       ├── designer/
│       ├── social-media/
│       ├── analista-de-crm/
│       ├── analista-de-dados/
│       ├── dev-frontend/
│       └── dev-infra-deploy/
│           └── {skill-name}/
│               ├── context.md
│               ├── v1.0.0.md
│               ├── latest.md
│               └── CHANGELOG.md
└── saber/                        ← processo SABER (separado)
```

---

## Como usar

### Consumir uma skill

1. Leia o `context.md` da skill para entender propósito, owner e versão atual
2. Use o `latest.md` para obter o conteúdo mais recente
3. Se precisar de uma versão específica, acesse o arquivo `v{X}.Y.Z.md` correspondente

### Criar uma nova skill

1. Crie a pasta dentro do agente owner ou em `executar/shared/` se for reutilizável
2. Escreva o `context.md` com todos os metadados (ver template em `versioning.md` nesta pasta)
3. Escreva o conteúdo em `v1.0.0.md`
4. Copie o conteúdo para `latest.md`
5. Inicie o `CHANGELOG.md` com a entrada `v1.0.0`

### Atualizar uma skill existente

1. Decida o tipo de mudança (ver `versioning.md`)
2. Crie o novo arquivo versão (`v1.1.0.md`, `v2.0.0.md`, etc.)
3. Atualize `latest.md` com o novo conteúdo
4. Atualize `context.md` (campo `latest` e `updated`)
5. Adicione entrada no `CHANGELOG.md`

---

## Agentes do sistema

| Agente | Papel | Arquivo |
|--------|-------|---------|
| `gerente` | Estratégia e resultados do cliente | `executar/agents/gerente/context.md` |
| `coordenador` | CS/Farmer — relacionamento e check-ins | `executar/agents/coordenador/context.md` |
| `gestor-de-trafego` | Mídia paga e performance | `executar/agents/gestor-de-trafego/context.md` |
| `copywriter` | Conteúdo e persuasão | `executar/agents/copywriter/context.md` |
| `gestor-de-projeto` | Account Manager — processos e entregas | `executar/agents/gestor-de-projeto/context.md` |
| `designer` | Ativos visuais e marca | `executar/agents/designer/context.md` |
| `dev-frontend` | Páginas e experiência digital | `executar/agents/dev-frontend/context.md` |
| `dev-infra-deploy` | Infraestrutura e deploy | `executar/agents/dev-infra-deploy/context.md` |

---

## Referências cruzadas

- Taxonomia completa → `taxonomy.md`
- Regras de versionamento → `versioning.md`
- Mapa de interações entre agentes → `agents.md`
