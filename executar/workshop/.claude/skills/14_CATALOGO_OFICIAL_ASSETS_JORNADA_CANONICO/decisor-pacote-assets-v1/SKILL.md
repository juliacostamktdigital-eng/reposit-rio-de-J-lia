---
name: decisor-pacote-assets-v1
description: Decide o pacote de assets do ciclo v1 após diagnóstico e benchmark — lista curta no ciclo, lista explícita fora do ciclo, matriz de dependências do cliente e critérios N2 por componente (playbook 14 seção 6). Use com handoff, diagnóstico GTM, benchmark e catálogo oficial; antes de tracking amplo e produção em massa de peças.
---

# Decisor — pacote de assets v1

## Fonte canônica

Playbook **`14_CATALOGO_OFICIAL_ASSETS_JORNADA_CANONICO.md`**, **Seção 6 — Decisão do pacote v1**.

Quatro entregáveis **obrigatórios** nessa etapa:

1. **Lista curta de assets v1** — após diagnóstico e benchmark, dentro da construção de assets.
2. **Lista de assets fora do ciclo** — evitar que tudo vire card/entrega.
3. **Matriz de dependências do cliente** — antes de tracking e setup.
4. **Critérios de N2 por componente** — antes da auditoria.

## Relação com o catálogo

Use **`catalogo-assets-jornada-marketing-os`** (lista oficial e `listar_assets_aplicaveis.py`) como **menu** de opções. Esta skill **restringe** o menu ao que entra em v1, documenta o que fica **fora** e liga **dependências** e **N2** por componente.

**Critérios N2** do DEOC e comunicação estão no playbook **13** (Seção 6); outros componentes (mídia, tracking, CRM) devem ter critérios auditáveis equivalentes — ver `reference.md`.

## Inputs (inventário + prática)

- Handoff EXECUTAR, diagnóstico GTM, benchmark (mercado, beachhead quando couber).
- Objetivo do ciclo, canal previsto, ordem de grandeza de orçamento, prazo.
- Capacidade do cliente (tempo, decisões, acessos) e riscos conhecidos.
- Saída opcional do filtro de catálogo (`contexto-catalogo.json` → Markdown).

## Outputs

- Pacote v1 priorizado (P0 bloqueia go-live, P1 escopo v1, P2 stretch).
- Inventário **fora do ciclo** com motivo e **quando reavaliar**.
- Dependências do cliente com o que cada uma **bloqueia**.
- Tabela de **N2 mínimo** por componente ou bloco da jornada.

## Workflow

1. Consolide diagnóstico + benchmark: o que é **bloqueio real** vs **desejo**.
2. Rode ou consulte o catálogo filtrado ao contexto do cliente.
3. Monte a **lista curta v1**: só o que será produzido/necessário **neste ciclo**; nomeie owner ou lado (cliente/agência).
4. Monte a lista **fora do ciclo**: tudo o que alguém pediu mas não entra — com motivo (capacidade, escopo, fase, risco).
5. Preencha **dependências**: acessos BM, GTM, CRM, legal, aprovações, dados — e qual asset isso bloqueia.
6. Defina **N2 por componente**: uma frase de “o que precisa ser verdade” + evidência esperada.
7. Valide com `scripts/build_pacote_v1.py ... --audit` antes de congelar o pacote.
8. Socialize com cliente e time; registre mudanças em versão.

## Artefatos

- `reference.md` — texto da Seção 6, heurísticas e ligação com N2.
- `templates/pacote-assets-v1.md`
- `templates/pacote-assets-v1.json`
- `scripts/build_pacote_v1.py`

## Scripts

```bash
python3 scripts/build_pacote_v1.py templates/pacote-assets-v1.json --md ./pacote-v1.md
python3 scripts/build_pacote_v1.py templates/pacote-assets-v1.json --audit
```

## Definition of Done

Os quatro blocos do playbook 14 estão preenchidos; cada linha do pacote v1 referencia **nome de asset** alinhado ao catálogo ou justifica customização; **fora do ciclo** não está vazio (explícito); dependências amarram a bloqueios reais; N2 por componente é verificável na auditoria.
