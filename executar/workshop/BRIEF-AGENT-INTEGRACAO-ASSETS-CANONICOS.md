# Briefing (agente) — integração de skills e assets no Marketing OS

**Atualizado:** 2026-04-30  
**Fonte:** alinhamento 04-30 (`Calls/04-30 Alinhamento de Workflow...-transcript.txt`) + `VERSIONAMENTO_JSON_WORKFLOW.md`

---

## Papel

Você integra **skills/assets semi-briefados** (trabalho externo ou em pasta de rascunho) com o que já está em **`assets/canonicos/`**, resolve duplicidade, preserva o melhor conteúdo e gera **nova versão** do workflow JSON + manifest, **sem editar o V1 in-place** como fonte de evolução (crie V2+ conforme o guia).

---

## Objetivo

1. Unificar o backlog de skills do colaborador com os **assets canônicos** já versionados.  
2. Garantir que o canvas (HTML/JSON) aponte para **caminhos corretos** de markdown e que não haja skills duplicadas sem decisão explícita.  
3. Quando o conteúdo canônico for substituído ou fundido, arquivar o anterior de forma rastreável em **`assets/legacy/drafts/`** (criar a pasta se não existir), em vez de apagar sem registro.

---

## Escopo

- **Dentro do escopo:** jornada / OS de **marketing** (Executar, assets do `workflow_marketing_os_v1`).  
- **Fora do escopo (por agora):** fluxos de **vendas** ou assets que não pertençam a este OS — não misturar no mesmo JSON de marketing.

---

## Leitura obrigatória antes de editar

1. `workflow_marketing_os_v1/VERSIONAMENTO_JSON_WORKFLOW.md` — regras de `workflow.*.json`, `workflow.manifest.json`, quando versionar.  
2. Cabeçalho e `iterationNotes` do `workflow.knowledge-os.v1.json` para manter consistência de schema e convenções.  
3. `workflow_marketing_os_v1/assets/canonicos/README.md` (se existir) — convenções de nomenclatura.

---

## Insumos (o que o humano pode te entregar)

- Diretório ou arquivos com **skills playbooks** / briefings parciais.  
- **Fonte padrão neste projeto:** `workflow_marketing_os_v1/assets/legacy/merge/` (skills e templates a comparar com `assets/canonicos/`).  
- Contexto de chat ou notas de decisão (opcional).  
- Indicação explícita de **qual pasta** é a “fonte” a integrar, se for diferente de `assets/legacy/merge/` (não inventar caminhos).

---

## Procedimento

### 1. Inventário e comparação

- Liste os assets na **fonte** e os arquivos em **`assets/canonicos/*.md`**.  
- Para cada par sobreposto (mesmo tema, mesmo estágio da jornada, ou ID/nome equivalente), compare qualidade, completude e aderência ao framework (`macros[].assets[]`, etapas).

### 2. Resolução de conflito (merge ou substituição)

- Se a **versão nova** for claramente melhor: mantenha-a como canônica; mova a versão canônica **antiga** para **`assets/legacy/drafts/`** com nome datado ou sufixo `_superseded` se útil.  
- Se forem **complementares**: fundir em **um** documento canônico (alinha à decisão de merge de documentos relacionados, ex.: narrativas que viram um único artefato).  
- Se a canônica atual permanecer melhor: coloque a tentativa nova em **`assets/legacy/drafts/`** com nota curta no topo ou em `iterationNotes` do JSON.

### 3. Novos arquivos canônicos

- Novos assets estáveis entram em **`assets/canonicos/`** com o mesmo padrão de nomes dos existentes (`SNAKE_UPPER`, prefixo numérico se for o padrão da pasta).  
- Atualize referências cruzadas se o projeto usar catálogo ou mapa (ex.: `00_MAPA_*`, `14_CATALOGO_*`).

### 4. Nova versão do workflow JSON

- **Não** reescrever o histórico do `workflow.knowledge-os.v1.json` como único mecanismo de evolução: para mudanças estruturais ou novo conjunto de referências, criar **`workflow.knowledge-os.v2.json`** (ou id acordado), copiando do V1 e ajustando `schema`/`version`/`title`/`date` conforme `VERSIONAMENTO_JSON_WORKFLOW.md`.  
- Atualizar **`workflow.manifest.json`** para registrar a nova versão e, se combinado com o time, definir qual entrada é padrão.  
- Garantir que **`macros[].assets[]`** e **`canonicalDocuments[]`** apontem para os caminhos finais dos `.md` em `assets/canonicos/`.

### 5. Build e verificação

- Rodar **`node build-docs.mjs`** (na pasta `workflow_marketing_os_v1`) para regenerar HTML/docs do inspector, quando o fluxo do projeto exigir paridade com markdown.  
- Conferir que não ficaram links quebrados para assets removidos da raiz de `canonicos/`.

### 6. Registro de decisões

- Documentar no **`iterationNotes`** do novo JSON (ou no PR): o que entrou, o que foi para `drafts`, e por quê.  
- Se DCC/UCM ou outros pares forem fundidos, registrar explicitamente no mesmo campo.

---

## Restrições

- Não inventar conteúdo de negócio: onde faltar dado, **marcar lacuna** no texto ou em nota.  
- Não misturar escopo de vendas no pacote deste OS sem instrução explícita.  
- Coordenação com outro contributor: evitar editar os mesmos arquivos em paralelo sem combinar (processo git: branch → PR → merge → pull da `main`).

---

## Definition of Done

- [ ] Duplicidades tratadas (merge, draft ou descarte justificado).  
- [ ] Markdown canônico atualizado; superseded em `assets/legacy/drafts/` quando aplicável.  
- [ ] Novo `workflow.knowledge-os.vN.json` + `workflow.manifest.json` alinhados ao guia.  
- [ ] `build-docs` executado se o projeto depender de HTML gerado.  
- [ ] `iterationNotes` (ou equivalente) descreve a revisão.

---

## Referências rápidas

| Artefato | Caminho |
| --- | --- |
| Workflow v2 (padrão no manifest) | `workflow_marketing_os_v1/workflow.knowledge-os.v2.json` |
| Workflow v1 (baseline) | `workflow_marketing_os_v1/workflow.knowledge-os.v1.json` |
| Manifest | `workflow_marketing_os_v1/workflow.manifest.json` |
| Assets canônicos | `workflow_marketing_os_v1/assets/canonicos/` |
| Rascunhos / arquivados | `workflow_marketing_os_v1/assets/legacy/drafts/` (criar se necessário) |
| Skills a integrar (entrada) | `workflow_marketing_os_v1/assets/legacy/merge/` |
| Guia de versionamento | `workflow_marketing_os_v1/VERSIONAMENTO_JSON_WORKFLOW.md` |
