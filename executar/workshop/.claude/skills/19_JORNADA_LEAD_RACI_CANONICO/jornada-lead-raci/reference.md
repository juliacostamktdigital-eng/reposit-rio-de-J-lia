# Referência — Jornada + RACI ↔ playbook 19

Canônico: `19_JORNADA_LEAD_RACI_CANONICO.md`.

## Passos ↔ JSON

| Passo | Conteúdo | Onde no JSON |
|-------|-----------|--------------|
| 1 | Etapas + touchpoints | `etapas[].etapa_funil`, `etapas[].touchpoints[]` |
| 2 | R / A / C / I | `etapas[].responsible`, `etapas[].accountable`, `etapas[].consulted`, `etapas[].informed` |
| 3 | Evidência mínima | `etapas[].evidencia_minima` |
| 4 | Capacidade e SLA | `validacao_capacidade_sla` |
| 5 | Publicação / links | `meta.link_*`, `publicacao.onde_colado_*` |

## Saídas do playbook ↔ estrutura

| Saída | Campo / bloco |
|-------|----------------|
| Mapa: etapas + touchpoints | `etapas[]` |
| Quem faz o quê | RACI por linha |
| Evidência por responsável | `evidencia_minima` (registro esperado) |
| RACI mínimo | R/A obrigatórios na auditoria; C/I recomendados |

## Componentes críticos

Dono **Accountable** claro; evidência mínima (não só memória); SLA viável; integração com loop de melhoria (`loop-ajuste-marketing-vendas` / A-4).

## Auditoria (`--audit`)

- `meta`: projeto, responsável do artefato, `link_funil_unificado_a2`, `link_protocolo_a4`.
- **Cada etapa** em `etapas[]`: `etapa_funil`, `accountable`, `responsible`, `evidencia_minima` obrigatórios.
- `validacao_capacidade_sla.resumo` preenchido (passo 4).
- `meta.link_funil_unificado_a2` e `meta.link_protocolo_a4` (DoD: links com A-2 e A-4).
- `publicacao.onde_colado_funil` e/ou `onde_colado_protocolo` documentados (passo 5).

## Nota sobre C e I

Podem ser listas de strings no JSON ou texto único; o script renderiza como lista ou texto.
