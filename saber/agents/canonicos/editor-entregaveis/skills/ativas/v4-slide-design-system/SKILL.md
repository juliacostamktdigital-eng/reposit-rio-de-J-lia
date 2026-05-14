---
name: v4-slide-design-system
description: Use para aplicar o design system V4 Company a decks 16:9, definindo cores, tipografia, logo, componentes e regras visuais antes de construir ou revisar PPTX.
---

# V4 Slide Design System

## Quando usar

Use em qualquer deck HTML visual ou export PPTX produzido pelo `editor-entregaveis`.

## Objetivo

Garantir que todo entregavel visual siga V4 Company como padrao principal.

## Fontes canonicas locais

Consulte quando precisar de detalhe:

- `brain_v4_colli/empresa/skills/saber/skills/skills_extract_entregas/skills/design-system-v4-company-plugin/claude-code/.claude/skills/v4-brand-v2/SKILL.md`
- `brain_v4_colli/empresa/skills/saber/skills/skills_extract_entregas/skills/design-system-v4-company-plugin/claude-code/.claude/skills/v4-slides/SKILL.md`
- assets em `brain_v4_colli/empresa/skills/saber/skills/skills_extract_entregas/skills/design-system-v4-company-plugin/claude-code/assets/`

## Regras obrigatorias

- Formato: 16:9.
- Fundo padrao: `#1A1814`.
- Vermelho V4: `#E50914`.
- Branco: `#FFFFFF`.
- Cinza apoio: `#464646`.
- Amarelo V4: `#FFDD00`, apenas para CTA/destaque pontual.
- Nunca usar `#000000` como fundo principal.
- Nunca usar `#E80403`.
- Evitar azul, verde, teal e paletas fora do brandbook.
- Logo no canto inferior direito em todos os slides.
- Titulo em caixa alta, preferindo Morganite/Morgane; fallback Arial Black.
- Corpo em IBM Plex Sans; fallback Calibri.

## Workflow

1. Defina master/layout base antes de criar slides.
2. Escolha componentes conforme o schema.
3. Controle densidade: uma ideia dominante por slide.
4. Use contraste alto e respiro.
5. Garanta que nenhum elemento toque margem minima.
6. Use grid consistente entre slides.
7. Registre qualquer excecao no QA.

## Referencias

- Consulte `references/V4-SLIDE-TOKENS.md` para tokens e medidas.
- Consulte `references/V4-COMPONENTS.md` para componentes visuais.
