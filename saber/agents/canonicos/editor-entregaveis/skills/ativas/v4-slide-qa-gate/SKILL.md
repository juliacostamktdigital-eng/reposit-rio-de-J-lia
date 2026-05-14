---
name: v4-slide-qa-gate
description: Use antes do handoff de qualquer entregavel visual Saber para validar HTML/PPTX/LP/criativo, aspect ratio, design V4, overflow, narrativa, evidencias e pacote final.
---

# V4 Slide QA Gate

## Quando usar

Use sempre depois de gerar ou editar o artefato visual principal, antes de entregar para CEO/Coordenador.

## Objetivo

Impedir que um deck incompleto, sem fonte, fora da marca ou visualmente quebrado siga para revisao.

## Workflow

1. Verifique existencia do output bundle.
2. Valide o artefato principal (`index.html`, `landing/index.html`, `creatives/*.html` ou `exports/deck.pptx`).
3. Valide `source/deck.json` ou `source/delivery.json`.
4. Compare slides gerados com schema.
5. Rode checklist editorial.
6. Rode checklist de design V4.
7. Rode checklist de evidencias.
8. Registre problemas em `qa/qa-report.md`.
9. Corrija bloqueantes antes do handoff.

## Criterios bloqueantes

- Nao existe artefato principal.
- Artefato nao esta no aspect ratio/formato definido no brief.
- Claim final sem evidencia.
- Texto cortado ou sobreposto.
- Slide sem funcao narrativa.
- Uso de cor proibida como padrao visual.
- Logo ausente em slides finais.
- HTML nao navegavel ou sem estado visual final.
- PPTX solicitado e exportado como imagem sem editabilidade.

## Saida esperada

```markdown
# QA Report - <delivery>

## Status

- Resultado: aprovado/com ressalvas/bloqueado

## Checks

| Area | Status | Observacao |
|---|---|---|
| Formato 16:9 | ok | ... |
| Design V4 | ok | ... |
| Evidencias | ok | ... |
| Navegabilidade/Editabilidade | ok | ... |
| Overflow | ok | ... |
| Narrativa | ok | ... |

## Correcoes feitas

## Lacunas restantes
```

## Referencias

- Consulte `references/QA-CHECKLIST.md` para criterios detalhados.
