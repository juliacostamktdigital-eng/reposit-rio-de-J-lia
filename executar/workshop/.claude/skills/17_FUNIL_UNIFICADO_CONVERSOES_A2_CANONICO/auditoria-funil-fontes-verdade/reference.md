# Referência — Auditoria de funil ↔ playbook 17

Canônico: `17_FUNIL_UNIFICADO_CONVERSOES_A2_CANONICO.md`.

## Âncoras no canônico

| Tema no playbook | Onde entra na auditoria |
|------------------|-------------------------|
| Fonte da verdade por etapa (1 sistema) | Dimensões `fvt-*` + tabela conciliação por etapa |
| Evidência mínima auditável | Campo `evidencia` em cada dimensão |
| Campos mínimos obrigatórios | Seção `campos_minimos` + KPI “% campos preenchidos” |
| Eventos de tracking | Seção `eventos_tracking` |
| Etapas sem dono | `etapas_sem_dono` ↔ threshold **vermelho** (“etapas sem dono”) |
| Planilha paralela / vocabulários concorrentes | Dimensão `fvt-01`, `gov-01` |
| Thresholds V/A/V | § **Como gerenciar** — aplicados ao consolidado |
| Cadência e change log | `meta.cadencia_rodada`; lembrar `changelog-funil-conversoes` |

## Dimensões padrão (`dimensoes[]`)

| ID | Foco | Lê no playbook |
|----|------|----------------|
| `fvt-01` | CRM × planilha backup × relatório plataforma conciliáveis | Vermelho: discrepância entre fontes |
| `fvt-02` | Uma fonte preferencial por etapa respeitada na prática | Componentes críticos; DoD |
| `trk-01` | Eventos necessários existem e disparam | Passo 5; saídas |
| `crm-01` | Campos mínimos com adesão aceitável | KPI + amarelo “pouco dado confiável” |
| `gov-01` | Donos e governança (SLA de dado, treino, mudanças registradas) | Dono (lacuna); change log |
| `ops-01` | Funil cabível na operação (volume vs capacidade) | Passo 6; componentes críticos |

Inclua `n.a.` com justificativa quando o escopo não exige a dimensão (ex.: sem mídia paga ainda).

## Heurística do script (`--summary`)

1. Se qualquer dimensão obrigatória (não `n.a.`) está **`vermelho`** → consolidado **vermelho**.
2. Senão, se **`etapas_sem_dono`** tem linhas com `impacto_operacional: true` (ou texto preenchido sem marcação explícita, tratado como risco) → tendência vermelho; preferir marcar `impacto_operacional` no JSON.
3. Senão, se existe **`amarelo`** em dimensão aplicável ou adesão de campos `amarelo` → **amarelo**.
4. Caso contrário → **verde** (ou **incompleto** se houver dimensão sem semáforo preenchido).

Ajustes finos ficam no relatório narrativo (`parecer_humano`).

## Status válidos no JSON

`verde`, `amarelo`, `vermelho`, `n.a.` (string). Vazio = pendente → `--audit` acusa.

## Relação com `funil-unificado-conversoes-a2`

A auditoria compara **“declarado no artefato A-2”** vs **“observado na operação”**. Link em `referencia_funil.link_artefato` + `versao`.
