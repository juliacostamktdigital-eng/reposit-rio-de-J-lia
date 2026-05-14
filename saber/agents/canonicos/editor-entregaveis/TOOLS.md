# TOOLS - Editor de Entregaveis
**Status:** v2
**Atualizado:** 2026-04-30
**Fonte:** agente:codex

---

## Como o Paperclip trabalha com skills

As skills deste agente sao ativadas na aba **Skills** do Paperclip. No run seguinte, o Paperclip vincula as skills ativas ao ambiente `CODEX_HOME/skills/`.

Este arquivo define contrato de uso de ferramentas e limites operacionais. O catalogo de skills esperadas vive em `./skills/README.md`.

## Skills ativas esperadas

- `saber-slide-intake`
- `delivery-format-router`
- `saber-claim-evidence-map`
- `saber-slide-schema-registry`
- `v4-slide-design-system`
- `v4-html-slide-builder`
- `v4-landing-page-builder`
- `v4-creative-format-builder`
- `openai-image-asset-generator`
- `v4-pptx-builder`
- `v4-slide-qa-gate`

## Permitido

- Ler arquivos indicados na issue/brief.
- Ler Plano de ROI e artefatos em `projetos/<slug>/`.
- Ler outputs aprovados dos especialistas.
- Criar/editar entregaveis no path combinado.
- Criar `source/deck.json`, `source/delivery.json`, HTML visual, landing pages, criativos e exports quando necessario.
- Gerar assets visuais com `openai-image-asset-generator` quando houver **`OPENAI_IMAGE_API_KEY`** no adapter env (não uses `OPENAI_API_KEY` no agente se quiseres Codex por assinatura).
- Rodar comandos locais necessarios para gerar, renderizar e validar decks.
- Usar assets oficiais V4 dentro do repositorio.
- Usar busca textual dentro do escopo do cliente ou da iniciativa.

## Nao permitido

- Alterar outputs de especialistas sem task explicita.
- Alterar Plano de ROI.
- Criar guia de voz/mensagem.
- Rodar comandos destrutivos.
- Baixar assets externos sem autorizacao.
- Usar fontes externas como evidencias de negocio sem autorizacao.
- Gravar API keys reais em arquivos versionados.
- Expor secrets, tokens ou dados sensiveis.

## Preferencias tecnicas

- HTML visual e o artefato principal neste inicio, mas o formato depende do brief.
- `source/deck.json` e a fonte estruturada do deck.
- `source/delivery.json` e a fonte estruturada para landing pages, criativos e image packs.
- PPTX editavel e export opcional.
- Slides devem ser 16:9. Criativos podem ser 16:9, 9:16, 1:1, 4:5 ou 1.91:1 conforme canal.
- Em HTML, usar frames com aspect ratio fixo. Em PptxGenJS, usar `LAYOUT_16x9` ou layout equivalente `10 x 5.625`.
- Render/QA visual deve acontecer sempre que o ambiente tiver ferramenta disponivel.
