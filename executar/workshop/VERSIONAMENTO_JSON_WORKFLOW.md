# Guia de Versionamento do JSON do Workflow

Este guia explica como criar novas versões do sistema operacional visual sem mexer no motor do canvas.

A regra principal: o código interpreta dados. Cada nova versão do fluxo deve nascer como um novo `workflow.*.json` registrado em `workflow.manifest.json`. Skills, templates, checklists, documentos e automações que fazem uma etapa funcionar entram como `assets` dentro da etapa correspondente.

## Fonte da Verdade

Arquivos principais:

| Arquivo | Papel |
| --- | --- |
| `workflow.manifest.json` | Registro das versões disponíveis, versão padrão e configuração de layout/engine. |
| `workflow.knowledge-os.v1.json` | Versão canônica atual do fluxo Marketing OS / OS do Executar. |
| `workflow.<nova-versao>.json` | Nova versão experimental, de cohort, tese, produto ou revisão operacional. |
| `./assets/canonicos/*.md` | Documentos editáveis dos assets/skills. |
| `docs-index.json` e `docs/*.html` | Versões renderizadas dos Markdown para o inspector/modal. Geradas por `node build-docs.mjs`. |

O canvas carrega `workflow.manifest.json`, escolhe uma entrada em `versions[]` e depois busca o arquivo indicado por `workflowFile`.

## O Que Versionar

Versione o JSON quando houver mudança de sistema operacional:

- Mudança na jornada principal, ordem das etapas ou definição de uma etapa.
- Nova leitura de maturidade, cohort, segmento, produto ou tese de GTM.
- Inclusão, remoção ou reclassificação relevante de skills/assets por etapa.
- Mudança no `operatorGuide` que altera como a operação executa.
- Novo conjunto de documentos canônicos, templates, checklists ou critérios de evidência.

Não crie nova versão para ajuste pequeno de copy, typo ou refinamento visual. Nesse caso, edite a versão atual e registre em `iterationNotes`.

## Modelo Mental

No JSON atual:

- `macros[]` são as etapas, notas visuais e blocos principais do canvas.
- `macros[].assets[]` são as skills/assets daquela etapa.
- `operatorGuide` diz como operar a etapa.
- `page` explica o conteúdo da etapa para humanos e IAs.
- `canonicalDocuments[]` aponta para documentos Markdown canônicos.
- `edges[]` define a sequência visual e loops.
- `uiModel` descreve como a UI deve tratar assets e inspector.
- `iterationNotes[]` registra decisões e alterações dentro da versão.

Evite voltar para `micros`, `bonds`, `microEdges` como fonte principal. Eles são legado/opcionais. A fonte canônica dos assets é `macros[].assets[]`.

## Como Criar Uma Nova Versão

1. Copie o JSON canônico atual.

```bash
cp workflow.knowledge-os.v1.json workflow.<id-da-versao>.json
```

Exemplo:

```bash
cp workflow.knowledge-os.v1.json workflow.knowledge-os.v2.json
```

2. Atualize o cabeçalho do novo JSON.

Campos mínimos:

```json
{
  "schema": "mastermind-v2",
  "version": "knowledge-os-v2",
  "title": "Marketing OS / OS do Executar - Knowledge Flow Visual v2",
  "date": "2026-04-30"
}
```

3. Registre a versão no manifest.

Adicione uma entrada em `workflow.manifest.json`:

```json
{
  "id": "knowledge-os-v2",
  "label": "Knowledge OS v2 · skills canonizadas",
  "workflowFile": "./workflow.knowledge-os.v2.json",
  "engine": {
    "splitMicrosFromAssets": true,
    "applyTieredLayoutToMacros": true,
    "layoutModel": {
      "mainMacroOrder": [
        "k00-narrative",
        "k04-diagnosis",
        "k04-benchmark",
        "k06-assets",
        "k07-tracking",
        "k08-campaign-setup",
        "k08-execution",
        "k09-evidence",
        "k10-n2-audit",
        "k11-n3-growth",
        "k12-canonize",
        "k13-rebrief"
      ],
      "bottomMacrosOrder": [
        "k03-maturity",
        "s07-assets-catalog",
        "s01-cohort-map"
      ]
    },
    "syncGroupBoundsToMacros": true
  }
}
```

Mantenha os demais parâmetros de `layoutModel` iguais ao canônico, a menos que a nova versão precise de outro espaçamento.

4. Decida se a nova versão deve virar padrão.

Enquanto estiver testando, mantenha:

```json
"defaultVersionId": "knowledge-os-v1"
```

Quando a nova versão for aprovada:

```json
"defaultVersionId": "knowledge-os-v2"
```

Também atualize `versionPolicy.correctVersion` dentro do JSON aprovado.

## Como Abrir Uma Versão

Pela URL:

```text
http://localhost:5173/?version=knowledge-os-v2
```

Ou pelo seletor de versões da toolbar, quando houver mais de uma versão no manifest.

## Como Canonizar Skills Como Assets

Neste projeto, `skill == asset` quando a skill é necessária para executar, auditar ou melhorar uma etapa.

Uma skill deve entrar em `macros[].assets[]` da etapa onde ela é criada, usada ou validada. Se a mesma skill aparece em várias etapas, escolha uma etapa dona e referencie seu uso em `canonicalDocuments[].usedAt` ou no `operatorGuide` das etapas consumidoras.

Formato recomendado:

```json
{
  "id": "asset_k08_setup_meta_ads",
  "title": "Skill de setup Meta Ads",
  "label": "Setup Meta Ads",
  "kind": "skill operacional",
  "order": 1,
  "required": true,
  "statusInJourney": "create-or-update",
  "owner": "gestor de trafego",
  "whenCreated": "antes do go-live",
  "inputs": [
    "plano de midia",
    "taxonomia UTM",
    "acessos Meta Business",
    "eventos e conversoes definidos"
  ],
  "contents": [
    "checklist de conta",
    "pixel/CAPI",
    "publicos padrao",
    "estrutura inicial de campanha",
    "nomenclatura"
  ],
  "outputs": [
    "conta pronta para ativacao",
    "campanhas em rascunho",
    "eventos testados"
  ],
  "definitionOfDone": "Campanhas, publicos, eventos e UTMs estao prontos e revisados antes de ativar verba.",
  "n2Evidence": "Checklist preenchido, prints/links de configuracao e teste de eventos anexados.",
  "n3Use": "Comparar setups por cohort para melhorar padrao de campanha vencedora.",
  "docPath": "./assets/canonicos/15_SETUP_CAMPANHAS_META_ADS_CANONICO.md",
  "aiSummary": "Skill para configurar Meta Ads com estrutura, publicos, eventos e nomenclatura padrao antes do go-live."
}
```

Campos obrigatórios para uma skill/asset útil:

- `id`: único no arquivo. Use prefixo da etapa (`asset_k08_...`) e nome semântico.
- `title` e `label`: nome humano do asset.
- `kind`: tipo do asset, por exemplo `skill operacional`, `template`, `checklist`, `documento`, `schema`, `relatorio`.
- `order`: posição no modal/lista da etapa.
- `required`: `true` se bloqueia avanço da etapa.
- `statusInJourney`: como o asset se comporta na jornada.
- `owner`: quem mantém ou executa.
- `inputs`, `contents`, `outputs`: contexto suficiente para outra IA entender o asset sem abrir o doc.
- `definitionOfDone`: critério objetivo de pronto.
- `n2Evidence`: evidência mínima de implementação.
- `n3Use`: como o asset vira gestão/aprendizado.
- `docPath`: caminho do Markdown canônico, se existir.
- `aiSummary`: resumo curto para contexto de IA.

Valores úteis para `statusInJourney`:

- `create-or-update`: criado ou atualizado naquela etapa.
- `evidence`: usado para provar execução.
- `reference`: material de apoio ou padrão consultivo.
- `audit`: usado para validar conformidade/maturidade.
- `improvement`: usado para aprender e melhorar ciclo seguinte.

## Onde Colocar Uma Skill

Use estas regras:

- Se a skill prepara execução, coloque na etapa de preparação/setup.
- Se a skill define estratégia, coloque em diagnóstico, benchmark ou construção de assets.
- Se a skill só prova que algo foi feito, coloque como `evidence`.
- Se a skill orienta melhoria recorrente, coloque em growth/N3.
- Se a skill é transversal, não crie uma etapa nova só para ela. Crie um asset dono e referencie nas etapas consumidoras.

Evite criar cards principais para catálogos, glossários ou notações. Esses elementos devem ser `type: "note"` ou assets de referência, não etapas da jornada.

## Processo Recorrente Para Reconciliar Skills E JSON

Use este processo sempre que houver uma nova pasta de skills externa, skills vindas de workshop, ou uma rodada de melhoria em `.claude/skills`.

### 1. Inventariar Fontes

Levante:

```bash
find <pasta-origem-skills> -maxdepth 3 -type f | sort
find .claude/skills -mindepth 3 -maxdepth 3 -name SKILL.md | sort
```

Registre no inventário:

- quantas skills existem na origem;
- quantas existem em `.claude/skills`;
- quais são equivalentes;
- quais são melhoria de uma skill existente;
- quais não têm equivalente e precisam ser criadas ou copiadas;
- quais não devem ser copiadas porque duplicam decisão canônica já tomada.

Documento recomendado:

```text
metodologia-criacao-skills/03_INVENTARIO_SKILLS_POR_PLAYBOOK.md
```

### 2. Mapear Cada Skill Para Um Playbook Dono

Toda skill Claude precisa morar dentro da pasta do playbook canônico que a governa:

```text
.claude/skills/<PLAYBOOK_CANONICO>/<nome-da-skill>/SKILL.md
```

Regra prática:

- se a skill executa uma subtarefa de mídia, use o playbook de setup de mídia correspondente;
- se a skill consolida estratégia/oferta/comunicação, use o DEOC ou o playbook estratégico;
- se a skill é QA, auditoria, changelog ou loop, use o playbook onde a evidência nasce;
- se uma skill externa mistura vários domínios, decompô-la ou tratá-la como referência de melhoria, não copiar 1:1.

### 3. Decidir O Tipo De Mudança

Classifique a rodada:

| Mudança | Atualiza JSON? | Cria nova versão? |
| --- | --- | --- |
| Editar texto de `SKILL.md`, `reference.md`, templates ou scripts dentro de playbook existente | Não, em geral | Não |
| Criar nova skill dentro de playbook já representado por `docPath` no canvas | Não obrigatório; atualizar índices | Não, em geral |
| Criar nova skill que precisa aparecer como asset/card próprio no canvas | Sim, em `macros[].assets[]` | Talvez |
| Criar novo playbook canônico ou novo macrobloco de jornada | Sim | Sim |
| Reclassificar etapa, ordem da jornada, grupos ou assets obrigatórios | Sim | Sim |
| Ajustar apenas índices renderizados (`skills-index.json`, `playbook-skills.json`, `docs-index.json`) | Não | Não |

### 4. Atualizar Skills E Índices

Depois de criar/editar skills:

```bash
node build-docs.mjs
```

Esse comando atualiza:

- `docs-index.json`;
- `docs/*.html`;
- `skills-index.json`;
- `playbook-skills.json`.

O inspector do canvas usa `docPath` do asset/playbook para buscar skills relacionadas em `playbook-skills.json`. Por isso, uma skill nova dentro de uma pasta de playbook existente pode aparecer na UI sem mudar o JSON do workflow.

### 5. Atualizar `workflow.knowledge-os.v3.json` Quando Necessário

Atualize o JSON quando a nova realidade precisar aparecer na estrutura operacional, não apenas no conteúdo da skill.

Campos mais comuns:

- `macros[].assets[]`: adicionar, remover, renomear ou enriquecer assets.
- `macros[].assets[].contents`: listar subskills relevantes quando o card é agregador.
- `macros[].assets[].definitionOfDone`: incluir novos critérios de pronto.
- `macros[].assets[].n2Evidence`: incluir nova evidência mínima.
- `macros[].assets[].n3Use`: registrar como a skill alimenta aprendizado.
- `canonicalDocuments[]`: incluir novo playbook ou alterar `producedAt`/`usedAt`.
- `operatorGuide`: atualizar como a etapa deve ser operada.
- `iterationNotes[]`: registrar data, origem, decisão e impacto.

Exemplo de nota:

```json
{
  "date": "2026-05-01",
  "type": "skills-reconciliation",
  "summary": "Comparadas skills externas do workshop com .claude/skills; criada lacuna para setup Meta Engajamento e registradas melhorias por playbook.",
  "source": "brain_v4_colli/areas/iniciativas/executar-ai/workshop/skills"
}
```

### 6. Quando Criar `v4` Em Vez De Editar `v3`

Crie uma nova versão (`workflow.knowledge-os.v4.json`) quando a mudança alterar como o sistema deve ser lido ou operado:

- novos cards principais;
- nova ordem de etapas;
- novo conjunto de assets obrigatórios;
- mudança relevante de maturidade N1/N2/N3;
- nova tese operacional de Marketing OS;
- mudança em `edges[]`, `groups[]` ou `layoutModel`.

Mantenha `v3` quando a mudança só melhora skills, scripts, templates ou índices mantendo a mesma jornada.

### 7. Validação Após A Rodada

Rode:

```bash
node build-docs.mjs
python3 -m json.tool workflow.knowledge-os.v3.json > /tmp/workflow-v3-check.json
python3 -m json.tool workflow.manifest.json > /tmp/workflow-manifest-check.json
node --check js/main.js
node --check js/canvas/inspector.js
node --check js/engine/normalize.js
```

Se houver nova versão:

```bash
python3 -m json.tool workflow.knowledge-os.v4.json > /tmp/workflow-v4-check.json
```

Também confira se o playbook dono aparece em `playbook-skills.json` com a nova skill e se `skills-index.json` contém o `skillPath`.

## Como Atualizar Documentos Canônicos

Quando uma skill/asset tiver Markdown:

1. Crie ou edite o arquivo em `./assets/canonicos`.
2. Aponte o `docPath` no asset.
3. Se for documento relevante para várias etapas, registre em `canonicalDocuments[]` com `producedAt` e `usedAt`.
4. Gere a versão estática:

```bash
node build-docs.mjs
```

5. Confirme que `docs-index.json` e `docs/*.html` foram atualizados.

## Checklist Para Editar Etapas

Ao criar, remover ou reordenar uma etapa:

- Atualize `macros[]`.
- Atualize `edges[]` para manter a trilha principal sem quebra.
- Atualize `workflow.manifest.json > versions[].engine.layoutModel.mainMacroOrder`.
- Se for nota inferior/transversal, atualize `bottomMacrosOrder`.
- Atualize `groups[]` se a etapa mudou de grupo visual.
- Atualize `canonicalDocuments[].producedAt` e `usedAt` se documentos mudaram de etapa.
- Atualize `iterationNotes[]` explicando a decisão.

## Checklist De Validação

Antes de considerar uma versão pronta:

```bash
python3 -m json.tool workflow.<id-da-versao>.json > /tmp/workflow-check.json
python3 -m json.tool workflow.manifest.json > /tmp/manifest-check.json
node --check js/main.js
node --check js/canvas/inspector.js
node --check js/engine/normalize.js
```

Depois rode local:

```bash
python3 -m http.server 5173
```

Abra:

```text
http://localhost:5173/?version=<id-da-versao>
```

Valide visualmente:

- O fluxo principal abre na ordem correta.
- Cada etapa relevante tem `operatorGuide`.
- Assets aparecem como lista no inspector.
- Clicar em asset abre modal.
- Documentos canônicos renderizam quando há `docPath`.
- Notas transversais não parecem etapas operacionais.

## Checklist De Aprovação Canônica

Uma versão só deve virar padrão quando:

- O `defaultVersionId` aponta para ela.
- `versionPolicy.correctVersion` dentro do JSON aponta para ela.
- O rótulo no manifest comunica claramente por que ela existe.
- Não há assets genéricos demais sem `definitionOfDone`.
- Toda skill operacional tem dono, inputs, outputs, evidência N2 e uso N3.
- O fluxo consegue ser entendido por uma pessoa nova e por uma IA sem depender de conversa anterior.
- Documentos Markdown usados no modal foram regenerados com `node build-docs.mjs`.

## Convenções De Nome

Versões:

- `knowledge-os-v1`
- `knowledge-os-v2`
- `knowledge-os-leadgen-v1`
- `knowledge-os-cohort-<nome>-v1`

Arquivos:

- `workflow.knowledge-os.v2.json`
- `workflow.knowledge-os.leadgen.v1.json`
- `workflow.knowledge-os.cohort-leadster.v1.json`

Assets:

- `asset_k08_setup_meta_ads`
- `asset_k07_contrato_dados`
- `asset_k11_rotina_growth_n3`

Docs:

- `17_SKILL_SETUP_META_ADS_CANONICA.md`
- `18_SKILL_AUDITORIA_N2_TRACKING_CANONICA.md`

## Erros Comuns

- Criar uma etapa nova para um asset transversal.
- Colocar skill em `canonicalDocuments[]` mas esquecer de incluí-la em `macros[].assets[]`.
- Editar `macros[]` e esquecer `mainMacroOrder`.
- Duplicar `id` de asset ou macro.
- Colocar documento no `docPath` e esquecer `node build-docs.mjs`.
- Trocar `defaultVersionId` antes da versão ser validada.
- Deixar `operatorGuide` vazio em etapa operacional.

## Regra Final

Se a mudança altera como a operação trabalha, versiona o JSON. Se a mudança só melhora a descrição de uma etapa já aprovada, edita o JSON atual e registra em `iterationNotes`.
