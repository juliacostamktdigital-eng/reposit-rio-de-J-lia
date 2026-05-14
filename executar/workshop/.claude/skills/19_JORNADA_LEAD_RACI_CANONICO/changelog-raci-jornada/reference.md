# Referência — Change log RACI ↔ playbook 19

## O que o canônico exige

Linha 102: **Registro obrigatório: change log do RACI (mudanças por papel e por quê).**

Cadência (linha 100): **mensal** ou **ao mudar estrutura do time** — o change log deve acompanhar esse ritmo (incluindo entradas de “sem mudança” quando fizer sentido para auditoria interna).

## Dimensões sugeridas (`dimensao`)

Valores livres; exemplos alinhados à jornada + componentes críticos do playbook (linhas 62–67):

| Valor sugerido | Uso |
|----------------|-----|
| `papel_R` / `papel_A` / `papel_C` / `papel_I` | Troca de Responsible, Accountable, Consulted, Informed |
| `evidencia_minima` | O que deve ficar registrado por etapa |
| `sla_handoff` | Expectativa ou dono de SLA (liga com A-4) |
| `etapa_funil` | Inclusão/remanejamento de etapa no mapa |
| `touchpoint` | Novo canal ou ponto de contato com dono |
| `capacidade` | Ajuste quando SLA era irreal vs time |
| `outro` | Mudança miscelânea documentada |

## Campo `papel_afetado`

Texto curto: `R`, `A`, `C`, `I`, `R+A`, `time inteiro`, etc. Facilita filtro e encaixa nos campos do `jornada-lead-raci.json` (`responsible`, `accountable`, …).

## Comunicação

O inventário da skill cita **plano de comunicação**. Use:

- **`comunicacao_alvos`:** quem precisa saber (ex.: Marketing, SDR, Closer, CS).
- **`comunicacao_status`:** `pendente` · `feita` · `n/a` (ex.: mudança só documental).

## Relação com outras skills

| Skill | Papel |
|-------|--------|
| `jornada-lead-raci` | Artefato “estado atual” — bump `versao_artefato` após mudança registrada aqui |
| `changelog-funil-conversoes` | Paralelo para A-2; mudança de etapa do funil pode exigir **dois** logs (funil + RACI) |
| `auditoria-raci-sla-evidencias` | Fonte de achados que viram entradas neste log |
| `protocolo-handoff-mql-sql-a4` | Mudanças de SLA/handoff frequentemente cruzam com `papel_A` / `sla_handoff` |
