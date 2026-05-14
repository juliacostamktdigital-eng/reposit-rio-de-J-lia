---
name: controle-duplicacao-assets
description: Audita documentos e artefatos frente ao catálogo oficial (playbook 14), elimina redundância e notas que fingem ser assets, e registra decisão manter, mesclar, arquivar ou criar (gaps) com motivo e owner. Use após inventário de assets, antes de escalar produção de peças ou quando existir UCM/DCC paralelos, versões duplicadas de DEOC ou notas sem função operacional.
---

# Controle de duplicação de assets

## Fonte canônica

Playbook **`14_CATALOGO_OFICIAL_ASSETS_JORNADA_CANONICO.md`**, em especial:

- **Objetivo do artefato:** separar etapa da jornada do inventário de assets; a decisão de merge cita **controle de duplicação de assets** como função transversal.
- **Seção 13** — o que está fora da jornada principal (meta-leitura vs implementação).
- **Seção 14** — **cinco perguntas** para saber se algo é asset canônico ou anotação, referência ou ruído operacional.

## Quando usar

- Inventário de documentos existentes diverge do **pacote v1** ou do **catálogo 14**.
- Suspeita de **UCM/DCC paralelos** ao DEOC, ou várias “versões da verdade” para mídia/LP/vendas.
- Antes de **criar novo** playbook, Notion ou planilha sem passar pelo teste da Seção 14.
- Governança: reduzir **ruído operacional** citado no canônico.

## Inputs

- Lista de documentos / links e sua função **autodeclarada**.
- **Catálogo oficial** (`catalogo-assets-jornada-marketing-os` / `reference.md` ou JSON).
- Objetivo da auditoria (ex.: “preparar N3”, “limpeza pré-pacote v1”).

## Outputs

- Por item existente: decisão **manter**, **mesclar** ou **arquivar**.
- Registro de **gaps**: o que falta **criar** para cobrir um asset canônico, com owner.
- Motivo e owner em toda decisão não óbvia.

## Workflow

1. Liste tudo o que o time trata como “asset” ou documento vivo.
2. Para cada item, responda às **cinco perguntas** da Seção 14 (sim/não).
3. Se **não** para todas → não é asset canônico; desloque para **mesclar** em fonte única, **arquivar** ou tratar como **referência** (sem duplicar na jornada).
4. Compare com o **catálogo 14** e com **legado** (ex.: UCM/DCC → DEOC).
5. Preencha `templates/controle-duplicacao.md` ou o JSON e rode `scripts/evaluate_controle_duplicacao.py --audit`.
6. Execute mudanças enfileiradas (mescla real, redirect de links, comunicação ao time).

## Artefatos

- `reference.md` — perguntas canônicas, decisões, anti-padrões.
- `templates/controle-duplicacao.md`
- `templates/controle-duplicacao.json`
- `scripts/evaluate_controle_duplicacao.py`

## Scripts

```bash
python3 scripts/evaluate_controle_duplicacao.py templates/controle-duplicacao.json --md ./auditoria-duplicacao.md
python3 scripts/evaluate_controle_duplicacao.py templates/controle-duplicacao.json --audit
```

## Definition of Done

Nenhum documento crítico com **função duplicada** sem decisão explícita; itens que falham na Seção 14 não seguem como entrega paralela; gaps **criar** têm owner; o time sabe qual é a **fonte única** por tema (oferta, tracking, etc.).
