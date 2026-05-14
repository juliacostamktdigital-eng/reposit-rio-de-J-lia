---
name: changelog-raci-jornada
description: Change log obrigatório do RACI da jornada do lead — registro de mudanças por papel, evidência mínima e SLA quando o time ou o processo muda (playbook 19 § Gerenciado). Histórico versionável com antes/depois, motivo, impacto e comunicação ao time. Complementa `jornada-lead-raci`.
---

# Change log do RACI (jornada do lead)

## Fonte canônica

Playbook **`19_JORNADA_LEAD_RACI_CANONICO.md`**, seção **Como gerenciar (Gerenciado)**:

- **Cadência de revisão:** mensal **ou quando trocar estrutura do time**.
- **Registro obrigatório:** **change log do RACI** — mudanças **por papel** e **por quê**.

Esta skill não substitui a atualização do artefato principal em **`jornada-lead-raci`**; o fluxo correto é **registrar a mudança aqui** e **refletir** em `versao_artefato` / JSON da jornada, com links cruzados.

## Quando usar

- Mudança de **Accountable** ou **Responsible** em qualquer etapa.
- Alteração de **evidência mínima** esperada no CRM.
- Ajuste de **SLA** ou de **handoff** ligado a um papel (coerente com protocolo A-4).
- Entrada de/saída de pessoas (SDR, closer, marketing) que muda o mapa R/A/C/I.
- Rodada de **`auditoria-raci-sla-evidencias`** que exija correção estrutural de donos.
- **Manutenção cadencial:** pode registrar explicitamente *sem alteração estrutural no período* (linha de auditoria).

## Princípio

Em 30 segundos o leitor entende: **antes → depois**, **por quê**, **quem precisa ser comunicado**, **versão do artefato após a mudança**, **o que medir** para validar o impacto.

## Dependências

- Artefato **`jornada-lead-raci`** — link em `meta.link_artefato_jornada_raci` (alinhado a `meta.link_funil_unificado_a2` e `link_protocolo_a4` no JSON da jornada).
- Opcional: **`funil-unificado-conversoes-a2`**, **`protocolo-handoff-mql-sql-a4`**, **`auditoria-raci-sla-evidencias`**.

## Workflow

1. Antes ou em paralelo à alteração no CRM/protocolo, abrir entrada em `historico[]`.
2. Preencher **dimensão**, **etapa** (se aplicável), **papel afetado**, **antes/depois**, **motivo**, **impacto esperado** e **comunicação** (alvos + status).
3. Após review, subir **`versao_raci_atual`** no `meta` e em **`versao_raci_apos`** na entrada; espelhar em `jornada-lead-raci` (`versao_artefato`).
4. Na primeira janela de leitura operacional, preencher **impacto observado** e **data revisão impacto**.

```bash
python3 scripts/render_changelog_raci.py --write-default templates/changelog-raci.json
python3 scripts/render_changelog_raci.py templates/changelog-raci.json --md ./changelog-raci-consolidado.md
python3 scripts/render_changelog_raci.py templates/changelog-raci.json --audit
```

## Definition of Done (entrada)

`data`, `autor`, `dimensao`, `resumo`, `antes`, `depois`, `motivo`, `impacto_esperado` preenchidos; `estado` = `publicado` após acordo; `comunicacao_alvos` quando a mudança afetar execução do time; `versao_raci_apos` quando a mudança for material no artefato.

## Artefatos

- `reference.md`
- `templates/changelog-raci.md`
- `templates/changelog-raci.json`
- `scripts/render_changelog_raci.py`
