# Workflow Canvas · Marketing OS

Board HTML/CSS/JS (pan/zoom, inspector, edges, micros). **Tudo que aparece no canvas é montado a partir do JSON referenciado no manifest** — você versiona **conteúdo e estrutura** ali; o código só interpreta.

## Guia de versionamento

Para criar novas versões do fluxo, canonizar skills como assets e manter o manifest sem confusão, use:

```text
VERSIONAMENTO_JSON_WORKFLOW.md
```

Resumo da regra: cada nova versão operacional deve ser um novo `workflow.*.json` registrado em `workflow.manifest.json`; skills/templates/checklists entram como `macros[].assets[]` na etapa dona.

## Rodar localmente

```bash
python3 -m http.server 5173
```

Abrir `http://localhost:5173/` na pasta deste projeto.

> Importante: abra via HTTP local, não via `file://`. O canvas busca JSON e documentos estáticos com `fetch()`.

## Documentos canônicos no inspector

Os `.md` editáveis ficam em `./assets/canonicos`. O canvas lê uma versão estática pré-compilada:

| Caminho | Função |
|--------|--------|
| `build-docs.mjs` | Lê os Markdown numerados em `./assets/canonicos` e gera HTML estático. |
| `docs/*.html` | HTML renderizado para leitura dentro do inspector. |
| `docs-index.json` | Índice usado pelo inspector para renderizar HTML e copiar Markdown bruto. |

Depois de editar qualquer documento canônico:

```bash
node build-docs.mjs
```

## Contrato dinâmico (sem mexer no código)

| Caminho | Função |
|--------|--------|
| **`workflow.manifest.json`** | Lista de versões: qual arquivo JSON carregar (`workflowFile`), rótulo no seletor e **`engine`** (comportamento). |
| **`workflow.*.json`** | Conteúdo: canvas, grupos, nós (macros), edges, micros (quando aplicável), `microEdges`, etc. |

Ao criar **outra linha do tempo / workshop**:

1. Copie um JSON existente ou comece pelo formato atual (`workflow.v1.json`).
2. Registre uma nova entrada em **`workflow.manifest.json`** (`id`, `label`, `workflowFile`, `engine`).
3. Opcional: `?version=meu-id` na URL ou escolha no seletor da toolbar.

Nenhuma alteração em `main.js` é obrigatória só para apontar para um arquivo novo — desde que o manifest referencie `workflowFile` correto.

## Engine (`workflow.manifest.json` → `versions[].engine`)

| Flag | Efeito |
|------|--------|
| **`splitMicrosFromAssets`** | `true`: cada item em `nodes[].assets` vira um **micro** + vínculos bond; `false`: assets ficam só como lista dentro do macro. |
| **`applyTieredLayoutToMacros`** | `true`: **`applyLinearSpineLayout`** recalcula **todas** as posições dos macros na trilha (ordem em `layoutModel.mainMacroOrder`, gaps, tiers). **`false`**: usa **`x`, `y`, `w`, `h`** dos macros já vindos do JSON (após migração `nodes` → `macros`). |
| **`layoutModel`** | Parâmetros da trilha linear **ou** da grade de micros quando o layout linear está **desligado** (`microLayout`: `topGap`, `gap`, `rowH`, …). `bottomRowOffsetFromMain` controla a distância visual entre a trilha principal e a faixa transversal inferior. |
| **`syncGroupBoundsToMacros`** | Recalcula retângulos dos grupos em função dos macros. |

### Estratégia atual

O manifest aponta para uma única versão correta: `knowledge-os-v1`.

Com `applyTieredLayoutToMacros: true`, você edita textos, edges, lista de macros e micros; a posição na trilha principal é gerada pelo motor a partir de `layoutModel.mainMacroOrder`.

## Formato do workflow (`workflow.*.json`)

- **`canvas`**: `width`, `height`, `initialView` (`pan` implícito como `x`/`y` + `zoom`).
- **`nodes`** (legado): lista de etapas com `assets`; o loader migra para schema interno `mastermind-v2`.
- Ou **`macros` / `micros`** + **`schema`: `"mastermind-v2"`** se você exportar já no formato mastermind.
- **`edges`**: `from`, `to`, `kind` (`main` \| `support` \| `loop`), `label`, `order`, opcional `points`.
- **`microEdges`**: sequências declarativas entre micros (`from`, `to`, `label`).
- **`groups`**: molduras (podem usar `includeMacroIds` conforme `syncGroupBoundsToMacros`).

## Arquivos principais

| Arquivo | Papel |
|---------|--------|
| `index.html` | Shell do board |
| `styles.css` | Canvas, nós, edges, inspector |
| `js/main.js` | Carrega manifest → JSON → `buildWorkflowView` → render |
| `js/engine/normalize.js` | Migração, layout, edges derivadas |
| `workflow.manifest.json` | Versão correta ativa e configuração do engine |
| `workflow.knowledge-os.v1.json` | Dados do board e links para documentos canônicos |
| `docs-index.json` | Índice estático dos documentos para o inspector |

Legenda das linhas e interação estão nos hints dentro do `index.html`.
