# Skills - Editor de Entregaveis
**Status:** v2
**Atualizado:** 2026-04-27
**Fonte:** agente:codex

---

## Contrato canonico

O Editor de Entregaveis agora opera como builder multiformato. As skills antigas foram preservadas em `skills/legacy/2026-04-27-pre-v4-slide-builder/` e nao devem ser ativadas sem decisao explicita.

Todo entregavel deve respeitar o `Delivery format contract` do brief. O padrao inicial para decks e HTML 16:9, usando principalmente o design system V4 Company. Landing pages, criativos, image packs e exports PPTX sao suportados quando o brief pedir.

## Estrutura local por agente

- `skills/ativas/` guarda as skills canonicas deste agente.
- `skills/incubacao/` guarda candidatas em teste ou adaptacao.
- `skills/legacy/` guarda skills antigas aposentadas.
- Cada skill local deve conter `SKILL.md` e `META.md`.
- Promocao para catalogo global segue `skills/CHECKLIST-PROMOCAO-PARA-GLOBAL.md`.

## Skills ativas

| Skill | Obrigatoria? | Quando usar |
|---|---|---|
| `delivery-format-router` | Sim | Ler o contrato de formato do brief e escolher skill, bundle, dimensao e exports |
| `saber-slide-intake` | Sim | Abrir qualquer tarefa de entrega e confirmar insumos, tipo de deck, paths e criterio de aceite |
| `saber-claim-evidence-map` | Sim | Mapear claims, recomendacoes e evidencias antes de montar slides |
| `saber-slide-schema-registry` | Sim | Escolher o formato de deck e a sequencia de slides/componentes |
| `v4-slide-design-system` | Sim | Aplicar identidade V4 Company em layout, cores, tipografia e componentes |
| `v4-html-slide-builder` | Sim | Construir o `index.html` visual 16:9 a partir de `source/deck.json` |
| `v4-landing-page-builder` | Opcional | Construir landing pages responsivas quando a entrega for LP |
| `v4-creative-format-builder` | Opcional | Construir criativos 16:9, 9:16, 1:1, 4:5 e 1.91:1 |
| `openai-image-asset-generator` | Opcional | Gerar fundos, texturas, cutouts, objetos e icones com OpenAI Images API |
| `v4-pptx-builder` | Opcional | Exportar `.pptx` editavel 16:9 a partir de `source/deck.json` quando necessario |
| `v4-slide-qa-gate` | Sim | Validar formato, marca, overflow, narrativa, evidencias e editabilidade |

## Regras de uso

- Nao iniciar build sem intake.
- Nao ignorar o formato/aspect ratio definido no brief.
- Nao montar slide com claim sem fonte.
- Nao entregar apenas `.md` quando a tarefa pedir entregavel.
- Nao finalizar sem `index.html` e `qa/qa-report.md`.
- Nao gerar PPTX como substituto da iteracao visual quando HTML for suficiente.
- Se o ambiente nao permitir gerar/renderizar PPTX, registre bloqueio e entregue o melhor source estruturado possivel.
