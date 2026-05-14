---
name: changelog-funil-conversoes
description: Governança do Funil Unificado (A-2) — registro obrigatório de mudanças em definições, etapas, eventos, campos e fontes da verdade, com motivo e impacto esperado/observado (playbook 17 § Gerenciado). Mantém histórico versionável e apoia auditorias e revisões quinzenais/mensais.
---

# Change log do funil (A-2)

## Fonte canônica

Playbook **`17_FUNIL_UNIFICADO_CONVERSOES_A2_CANONICO.md`**, seção **Como gerenciar (Gerenciado)**:

- **Cadência de revisão** quinzenal (até estabilizar) e mensal (depois), **com registro de mudanças**.
- **Registro obrigatório:** change log do funil — **o que mudou**, **por quê**, **impacto esperado/observado**.

Esta skill implementa esse registro de forma repetível; não substitui alinhamento Mkt+Vendas nem atualização do artefato principal em **`funil-unificado-conversoes-a2`**.

## Quando usar

- Após qualquer alteração em etapa, definição “passa/não passa”, evento de conversão, campo mínimo, fonte da verdade ou handoff refletido no funil.
- Ao fechar uma rodada de **`auditoria-funil-fontes-verdade`** que exija correção estrutural.
- Na cadência de governança (quinzenal/mensal), mesmo quando “não houve mudança” — registrar explicitamente *sem alteração estrutural* (entrada opcional de manutenção).

## Princípio

Um change log bom responde em 30 segundos: **antes → depois**, **por quê**, **o que medir para saber se deu certo**, e **quem registrou/apoiou**.

## Dependências

- Artefato **`funil-unificado-conversoes-a2`** (versão vigente) — link em `meta.link_artefato_funil`.
- **`auditoria-funil-fontes-verdade`** quando a mudança vier de achado auditável.

## Workflow

1. Atualizar o JSON/planilha interna **antes** de publicar mudança em CRM/tracking (ou em paralelo, nunca “depois sem registro”).
2. Para cada mudança, preencher uma entrada em `historico[]` com dimensão, antes/depois, motivo, impacto esperado; após janela de leitura, **impacto observado**.
3. Bump de **`versao_funil`** no artefato A-2 quando a mudança for material; referenciar `versao_funil_apos` na entrada.
4. Gerar leitura humana consolidada:

```bash
python3 scripts/render_changelog_funil.py --write-default templates/changelog-funil.json
python3 scripts/render_changelog_funil.py templates/changelog-funil.json --md ./changelog-funil-consolidado.md
python3 scripts/render_changelog_funil.py templates/changelog-funil.json --audit
```

## Definition of Done (entrada)

`data`, `autor`, `dimensao`, `resumo`, `antes`, `depois`, `motivo`, `impacto_esperado` preenchidos; `estado` = `publicado` após review; `impacto_observado` e `data_revisao_impacto` quando a mudança já tiver sido medida na operação (cadência playbook).

## Artefatos

- `reference.md`
- `templates/changelog-funil.md`
- `templates/changelog-funil.json`
- `scripts/render_changelog_funil.py`
