# Referência — Change log do funil ↔ playbook 17

## Âncora canônica

Trecho literal do **`17_FUNIL_UNIFICADO_CONVERSOES_A2_CANONICO.md`** (§ Gerenciado):

> **Registro obrigatório:** change log do funil (o que mudou, por quê, impacto esperado/observado).

A **cadência com registro** está na mesma seção (revisão quinzenal → mensal).

## Campos mínimos ↔ frases do playbook

| Frase no playbook | Campo sugerido no JSON |
|-------------------|-------------------------|
| o que mudou | `resumo`, `antes`, `depois`, `dimensao` |
| por quê | `motivo` |
| impacto esperado | `impacto_esperado` |
| impacto observado | `impacto_observado`, `data_revisao_impacto` |

## `dimensao` (valores recomendados)

| Valor | Uso |
|-------|-----|
| `definicao` | Mudança em critério “passou / não passou” |
| `etapa` | Inclusão, remoção, renome, ordem |
| `evento` | Conversão / evento de tracking |
| `campo` | Campo mínimo CRM (ou equivalente) |
| `fonte_verdade` | Troca de sistema-fonte por etapa |
| `handoff` | Ponto com protocolo A-4 |
| `taxa_aceitavel` | Ajuste de faixa V/A/V |
| `outro` | Texto livre justificado |

## `estado`

- `rascunho` — ainda não comunicado ao time operacional.
- `publicado` — passou a valer; artefatos e/ou CRM alinhados.
- `revisao_pendente` — aguardando medir impacto observado.

## Auditoria (`--audit`)

- **Meta:** `projeto`, `dono_changelog`, `link_artefato_funil`.
- **Por entrada iniciada** (qualquer texto em resumo/antes/motivo etc.): obrigatórios `data`, `autor`, `dimensao`, `resumo`, `antes`, `depois`, `motivo`, `impacto_esperado`.
- Entradas totalmente vazias (modelo) são ignoradas.
- `publicado` com `impacto_observado` vazio gera **aviso** (preencher após primeira leitura).

## Relação com outras skills

| Skill | Papel |
|-------|--------|
| `funil-unificado-conversoes-a2` | Artefato “verdade” versionado; change log não o substitui |
| `auditoria-funil-fontes-verdade` | Pode gerar itens que viram entradas no changelog |
