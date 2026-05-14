---
name: empacotamento-oferta-executavel
description: Empacota a oferta de forma dizível e executável (mecanismo, features com implicação/benefício/prova/copy, brainer comercial, condições diferenciais, escopo, pré-requisitos, limites da promessa, anti-ICP e governança de claims), alinhado ao DEOC playbook 13 seção 5.2, sem redesenhar política de preço. Inclui estrutura empacotada Hormozi-style pronta pra LP (núcleo + bônus mapeados a objeções + garantia + escassez REAL + ancoragem de preço comparativa + CTA), Forces of Progress (Moesta) como filtro pré-empacotamento e honesty constraint (escassez/garantia não-fake — Hormozi 2024 + risco CONAR/FTC). Use após benchmark e diagnóstico e antes de plano de mídia, criativos e LP; alimenta ou completa a seção Oferta e mecanismo do DEOC.
---

# Empacotamento de oferta executável

## Escopo deliberado

Esta skill cobre **empacotamento e clareza de oferta** com base na **capacidade real de entrega**. **Não** substitui decisão de política comercial de preço (tabelas, descontos, mudança estrutural de pricing). Registre apenas **lógica de preço** ou **observações** quando necessário para comunicação, sem propor novo modelo de receita.

## Quando usar

**Depois de:** benchmark (mercado, concorrentes), diagnóstico GTM, entendimento mínimo de ICP e provas disponíveis.

**Antes de:** plano de mídia, briefing criativo, LP, roteiros e scripts comerciais.

**Não usar para:** inventar promessa sem lastro; prometer garantias ou condições que gerem passivo sem capacidade comprovada.

## Fonte canônica

Playbook **`13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md`**, seção **5.2 Oferta e mecanismo** (e critérios de claims da **5.8** aplicáveis à promessa empacotada). Contexto operacional histórico: merge com a skill legada **07-empacotamento-oferta** (boa o suficiente; sem mexer em pricing).

## Relação com o DEOC

O output desta skill deve **encaixar diretamente** na seção **Oferta e mecanismo** do DEOC (`dossie-estrategico-oferta-comunicacao`). Pode ser produzido como rascunho focado só em oferta e depois fundido no DEOC completo.

## Workflow

1. Consolidar benchmark: commodity vs diferencial no segmento.
2. Fixar para quem serve e **anti-ICP** (quando não faz sentido vender).
3. **Forces of Progress (Moesta) — filtro pré-empacotamento**: 4 perguntas obrigatórias antes de empacotar — (a) **Push** está nomeado? (o que empurra o ICP pra fora do status quo?); (b) **Pull** está nomeado? (o que puxa pra essa solução específica?); (c) **Habit/inércia** está sendo ativamente atacada por algum elemento da oferta? (d) **Anxiety** da migração tem antídoto explícito (garantia, onboarding, prova social)? Se 4/4 sim → oferta tem chance. Se ≤2 → oferta não move ninguém; volte ao diagnóstico.
4. Descrever **mecanismo de geração de resultado** e **como funciona** em linguagem auditável.
5. Preencher cada **feature** no formato canônico: Feature → Como funciona → Implicação → Benefício → Prova → Como vira copy.
6. Escrever o **brainer** comercial em uma frase: *faço X em Y, para Z, com W* (condições plausíveis).
7. Listar **condições diferenciais** que reduzem risco ou aumentam confiança (com lastro).
8. **Estrutura empacotada Hormozi-style pronta pra LP**: organize a oferta em (a) **núcleo** (o que é entregue); (b) **bônus reativos** — cada bônus tem **CAMPO OBRIGATÓRIO "objeção neutralizada"**; bônus sem objeção mapeada não entra; (c) **garantia** classificada — *incondicional* / *condicional com checklist auditável* / *nenhuma + por quê* (não inventar garantia falsa); (d) **escassez REAL** — cohort, capacidade operacional, deadline de calendário ou janela de produção; **NÃO** fake countdown ou "últimas vagas" sem lastro; (e) **ancoragem de preço comparativa** — explicitar contra o quê o preço se ancora (alternativa nominal: coworking, hotel, concorrente nomeado, custo do não-agir mensurado); (f) **CTA** único com promessa-objeto consistente.
9. Tornar **escopo explícito**: entra, não entra, pré-requisitos do cliente.
10. Registrar **limites da promessa**, risco de passivo e **quando não vender**.
11. Separar **claims permitidos, proibidos e pendentes** (ver `reference.md`).
12. Rodar checklist de risco e o script `--audit` antes de declarar pronto.
13. Publicar derivados: headline central, ângulos de campanha, checklist de qualificação.

## Outputs

- Mapa de oferta executável (Markdown ou JSON → Markdown).
- Lista de claims governados e backlog do que falta provar.

## Artefatos

- `reference.md` — extrato canônico e checklists.
- `templates/oferta-executavel.md` — preenchimento manual.
- `templates/oferta-executavel.json` + `scripts/build_oferta_executavel.py` — geração e auditoria.

## Scripts

```bash
python3 scripts/build_oferta_executavel.py templates/oferta-executavel.json --md /tmp/oferta.md
python3 scripts/build_oferta_executavel.py templates/oferta-executavel.json --audit
```

## Definition of Done (espelho N2 para esta fatia)

Brainer **dizível**; condições diferenciais com lastro; escopo e pré-requisitos explícitos; provas mínimas listadas (gaps viram backlog); anti-ICP e limites da promessa claros; claims não extrapolam prova. **Honesty constraint**: escassez, urgência e garantia **não podem ser fake** — cada uma tem ou lastro operacional auditável (capacidade, cohort, calendário) ou é declarada como ausente. Hormozi 2024 reforçou que oferta com fake scarcity destrói trust e LTV; CONAR/FTC tratam como propaganda enganosa. Bônus sem objeção mapeada não entra. Detalhes em `reference.md`.
