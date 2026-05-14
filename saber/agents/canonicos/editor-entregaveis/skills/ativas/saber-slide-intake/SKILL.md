---
name: saber-slide-intake
description: Use para iniciar qualquer entrega do Saber em slides HTML 16:9, confirmando objetivo, insumos aprovados, tipo de deck, paths, lacunas e criterio de aceite antes de construir.
---

# Saber Slide Intake

## Quando usar

Use no inicio de qualquer tarefa do `editor-entregaveis`, antes de escrever narrativa, desenhar slides ou gerar PPTX.

## Objetivo

Transformar uma demanda aberta em um contrato de entrega claro:

- cliente/projeto
- tipo de deck
- audiencia
- decisao que o deck precisa provocar
- insumos aprovados
- lacunas
- path final
- criterio de aceite

## Workflow

1. Leia issue, brief e instrucoes do usuario.
2. Identifique o `slug` do projeto e o `delivery-slug`.
3. Liste os insumos esperados e marque cada um como `ok`, `faltando`, `conflitante` ou `opcional`.
4. Classifique o tipo de deck:
   - `diagnostico-semanal`
   - `entrega-final-saber`
   - `gtm-comercial`
   - `proposta-cliente`
   - `handoff-executar`
   - `decisao-executiva`
   - `custom`
5. Defina o output bundle:

```text
projetos/<slug>/entregaveis/<delivery-slug>/
  index.html
  source/deck.json
  exports/deck.pptx
  qa/qa-report.md
  README.md
```

6. Se houver lacuna bloqueante, registre antes de montar slides.
7. Se houver material suficiente, passe para `saber-claim-evidence-map`.

## Checklist de aceite do intake

- O tipo de deck esta explicito.
- A audiencia esta explicita.
- O objetivo do deck esta em uma frase.
- Os insumos aprovados estao listados por path.
- O path final esta definido.
- Lacunas e conflitos estao visiveis.
- O deck esta confirmado como HTML visual 16:9.
- A necessidade de export PPTX esta marcada como `sim`, `nao` ou `depois`.

## Saida esperada

```markdown
## Intake da entrega

- Projeto:
- Delivery slug:
- Tipo de deck:
- Audiencia:
- Decisao-alvo:
- Path final:
- Insumos ok:
- Insumos faltando:
- Conflitos:
- Proximo passo:
```
