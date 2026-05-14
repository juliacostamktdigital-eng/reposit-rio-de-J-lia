# Skills canonicas SABER

Esta pasta e a **fonte de verdade atual** para skills SABER prontas para uso em agentes canonicos e sincronizacao com Paperclip.

Veja tambem [`INDEX.md`](INDEX.md) para a lista navegavel das skills canonizadas.

Use esta pasta para consolidar a ultima versao aprovada de skills que vieram de:

- `../news/`
- `../skills_extract_entregas/skills/`
- pacotes `.skill` importados/exportados do Paperclip
- skills incubadas em `areas/iniciativas/agentizacao_saber/agents/canonicos/*/skills/incubacao/`

## Leia isto primeiro

Se voce e um agente de IA trabalhando em skills SABER:

1. Leia `../README.md`.
2. Leia `../VERSIONAMENTO.md`.
3. Leia este arquivo ate o fim.
4. Se a skill tambem existe em agentes canonicos, leia o `META.md` local da skill no agente antes de substituir qualquer coisa.
5. Se for sincronizar com Paperclip, leia:
   - `brain_v4_colli/areas/iniciativas/agentizacao_saber/agents/SKILL-FORMATO-PAPERCLIP.md`
   - `brain_v4_colli/areas/iniciativas/agentizacao_saber/workstation/GUIDE-SYNC-AGENTES-SKILLS-PAPERCLIP.md`

Nao invente convencoes. A regra desta pasta e versionar antes de promover.

## Papel desta pasta

| Pasta | Papel |
|---|---|
| `../news/` | Entrada bruta ou reorganizada. Nao e fonte final. |
| `../skills_extract_entregas/skills/` | Fonte historica/de trabalho para skills extraidas de entregas. |
| `./<skill-slug>/` | Fonte canonica atual da skill SABER. |
| `agents/canonicos/*/skills/ativas/` | Espelho operacional por agente, sincronizado a partir daqui quando aplicavel. |
| Paperclip producao | Runtime/importacao. Nao deve ser tratado como unica fonte autoral. |

## Estrutura obrigatoria por skill

```text
canonicas/
  <skill-slug>/
    context.md
    v1.0.0.md
    latest.md
    SKILL.md
    CHANGELOG.md
    META.md
    references/
    templates/
    scripts/
    assets/
```

Arquivos obrigatorios:

| Arquivo | Obrigatorio | Funcao |
|---|---:|---|
| `context.md` | Sim | Metadados da skill canonica, owner, status e versao atual. |
| `vX.Y.Z.md` | Sim | Versao imutavel aprovada. Nunca editar depois de publicada. |
| `latest.md` | Sim | Copia integral da versao aprovada mais recente. |
| `SKILL.md` | Sim | Copia integral de `latest.md`, usada pelo Paperclip. |
| `CHANGELOG.md` | Sim | Historico cronologico de mudancas. |
| `META.md` | Sim | Origem, equivalencias, agentes consumidores e observacoes operacionais. |

Pastas opcionais:

| Pasta | Uso |
|---|---|
| `references/` | Metodo, checklists, rubricas, regras e exemplos longos. |
| `templates/` | Modelos de output e schemas. |
| `scripts/` | Validadores, normalizadores e geradores deterministas. |
| `assets/` | Exemplos visuais, PDFs, imagens ou arquivos de apoio. |

## Frontmatter de `context.md`

Template minimo:

```yaml
---
skill: nome-da-skill
owner: saber
latest: v1.0.0
status: active
process: saber
runtime: paperclip
source: manual
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Campos recomendados quando aplicavel:

```yaml
product: [drx, ee, transversal, design, gtm, ops]
agents:
  - editor-entregaveis
  - especialista-growth-v4
origin_paths:
  - brain_v4_colli/empresa/skills/saber/skills/news/...
equivalent_to:
  - brain_v4_colli/empresa/skills/saber/skills/skills_extract_entregas/skills/...
paperclip_skill_name: nome-da-skill
```

## Como criar uma skill canonica

1. Defina o slug final em kebab-case.
2. Crie `canonicas/<skill-slug>/`.
3. Escreva a primeira versao em `v1.0.0.md`.
4. Copie integralmente `v1.0.0.md` para `latest.md`.
5. Copie integralmente `latest.md` para `SKILL.md`.
6. Crie `context.md`.
7. Crie `CHANGELOG.md`.
8. Crie `META.md` com origem e decisao de equivalencia.
9. Adicione `references/`, `templates/`, `scripts/` e `assets/` quando existirem.
10. So depois espelhe nos agentes canonicos que vao usar a skill.

## Como atualizar uma skill canonica

1. Classifique a mudanca como `MAJOR`, `MINOR` ou `PATCH` conforme `../VERSIONAMENTO.md`.
2. Crie um novo arquivo versionado, por exemplo `v1.1.0.md`.
3. Nunca edite versoes antigas `vX.Y.Z.md`.
4. Atualize `latest.md` com copia integral da nova versao.
5. Atualize `SKILL.md` com copia integral de `latest.md`.
6. Atualize `context.md` (`latest` e `updated`).
7. Atualize `CHANGELOG.md`.
8. Atualize `META.md` se mudou origem, equivalencia, agentes consumidores ou status.
9. Propague para `agents/canonicos/*/skills/ativas/` apenas depois da promocao.
10. Rode dry-run do sync Paperclip antes de aplicar em producao.

## Regra de ouro

`latest.md` e `SKILL.md` devem estar sempre em paridade na versao aprovada atual.

- `latest.md` existe para governanca e leitura canonica.
- `SKILL.md` existe para compatibilidade com Paperclip.
- `vX.Y.Z.md` existe para historico imutavel.

Se os tres divergirem sem motivo documentado, a skill nao esta pronta para sincronizar.
