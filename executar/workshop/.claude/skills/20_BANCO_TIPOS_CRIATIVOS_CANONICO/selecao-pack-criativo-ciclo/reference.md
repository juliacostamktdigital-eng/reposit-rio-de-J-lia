# Referência — Pack de produção ↔ playbook 20

## Função desta skill

O playbook **20** obriga que o Pack de Produção use o **banco de tipos**; o **`assets/canonicos/templates/pack-producao.md`** detalha o escopo completo: **criativos**, **ambiente de conversão**, **guardrails** e **checklist**. O JSON desta skill cobre o mesmo escopo para automação (`--md` / `--audit`).

## Mapeamento etapa / temperatura → tipos

| Contexto típico | Filtro no banco |
|-----------------|-----------------|
| Topo / aquisição fria | `temperatura`: frio; objetivo: clique, aware, lead inicial |
| Meio | morno; prova, comparação, objeção |
| Quente / remarketing | quente; urgência, oferta, recuperação |
| Canal | restrinja `formato` ao que o canal aceita bem (ex.: Reels vs Search RSAs) |

## Campos `selecao[]`

| Campo | Nota |
|-------|------|
| `tipo_id` | Deve existir no `banco-tipos.json` (ex.: `TIPO-003`) |
| `quantidade_pecas` | Unidades distintas (ex.: 3 vídeos ≠ 3 variações da mesma peça — use notas) |
| `hipotese_teste` | O que aprendemos se ganhar/perder |
| `criterio_leitura` | Métrica primária + guardrails (CPL, CTR hook, thumbstop, etc.) |
| `mensagem_angulo` | Ângulo por peça (template canônico) |
| `prova_usada` | Prova declarada no anúncio |
| `cta` | CTA |
| `destino` | LP, WA, form, lead nativo, etc. |

## Blocos canônicos adicionais

| Bloco JSON | Conteúdo |
|------------|----------|
| `plano_contexto` | Cliente/segmento, hipótese macro, oferta, ICP, persona |
| `ambiente_conversao` | LP, formulário/WA/agenda, tracking mínimo |
| `guardrails` | Núcleo fixo vs o que pode variar |
| `checklist_conformidade` | Quatro checagens mínimas do template oficial |

## Gestão (§ Gerenciado — playbook 20)

Ao publicar campanhas, **retroalimentar** o banco: preencher `campanhas_onde_usado` no tipo (via processo do `banco-tipos-criativos`) para KPI “tipos usados por campanha”.

## Exceção sem banco

`meta.justificativa_sem_banco` + `meta.link_banco_tipos` vazio só em **auditoria com aviso** — usar para projeto novo antes do DoD do catálogo, com plano de fechar o banco na mesma sprint.
