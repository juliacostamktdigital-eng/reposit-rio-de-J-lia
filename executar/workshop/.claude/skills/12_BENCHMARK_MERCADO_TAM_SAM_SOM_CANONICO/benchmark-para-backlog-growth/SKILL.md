---
name: benchmark-para-backlog-growth
description: Converte achados de benchmark de mercado em backlog de hipóteses testáveis com evidência, prioridade, métrica de sucesso primária (CPL, CAC, CTR, conversão, MQL etc.), asset impactado, dependências e registro de changelog até teste e aprendizado. Use após campo de batalha GTM, sizing e beachhead, antes de DEOC, plano de mídia, briefing criativo, LP ou ao alimentar planilha de testes.
---

# Benchmark Para Backlog Growth

## Quando Usar

Use quando o benchmark já produziu **padrões, gaps, riscos e decisões** (baseline vs. diferenciação) e o próximo passo precisa ser **execução testável**, não relatório eterno.

Momento na jornada (playbook `12`): depois de handoff, diagnóstico GTM e discovery mínimo; **antes** de DEOC definitivo, plano de mídia, briefing criativo e LP — ou para realimentar hipóteses quando canal, segmento ou oferta mudarem.

## Origem No Playbook Canônico

Esta skill implementa explicitamente:

- **Fluxo (Seção 5, passo 7):** gerar backlog de hipóteses testáveis com prioridade e métrica de sucesso.
- **Saída (Seção 7):** consumidores incluem plano de mídia e **planilha ou backlog de testes** (hipóteses priorizadas e métrica).
- **Como alimenta os assets (Seção 8):** canal prioritário, segmento, ICP, promessa, tipo de campanha/LP, provas, risco de mercado, esforço de diferenciação, **hipótese de mídia**.
- **Componentes críticos (Seção 9):** backlog **testável**, com **métrica**, **priorizado** e **rastreável** até teste e aprendizado.
- **DoD (Seção 10.1):** item obrigatório — backlog de hipóteses com prioridade e métrica.
- **Gestão contínua (Seção 12):** KPIs de % de hipóteses testadas, impacto, ciclo hipótese → teste → aprendizado; semáforo verde/amarelo/vermelho; **changelog** benchmark → decisão → teste → resultado.

## Inputs Recomendados

- saída de `benchmark-campo-batalha-gtm` (padrões, gaps, riscos, evidências);
- `sizing-mercado-tam-sam-som` e premissas de budget/CPL quando a hipótese for de aquisição;
- `posicionamento-competitivo-beachhead` (segmento inicial, promessa defensável);
- plano de mídia em rascunho, metas do ciclo e **capacidade de teste** (quantas hipóteses o time aguenta);
- referência à planilha de testes (`montar-planilha-testes-growth`) para IDs e rastreio.

## O Que É Uma Boa Hipótese

- **Testável:** condição clara de sucesso ou falha na métrica escolhida.
- **Ancorada:** pelo menos uma evidência de benchmark (link, print, nota de fonte, premissa explícita).
- **Acionável:** aponta **asset impactado** (mídia, criativo, LP, copy, oferta, DEOC, tracking).
- **Rastreável:** pode receber `test_id` / `v4_test_id` e ir para a aba de testes.

Métricas citadas no playbook para métrica de sucesso: **CPL**, **CAC**, **CTR**, **taxa de conversão**; estender para **MQL/SQL** quando o objetivo do ciclo exigir.

## Workflow

1. Liste **baseline** (o que será adotado do mercado porque já é padrão validado) e **diferenciação** (onde a conta vai se posicionar).
2. Para cada gap ou oportunidade priorizada, escreva uma hipótese no formato “Se… então… porque…”.
3. Escolha **métrica primária** alinhada ao objetivo da aquisição e **critério de sucesso** numérico ou qualitativo audível.
4. Marque **esforço**, **confiança**, **impacto** e **risco** para priorização.
5. Respeite a **capacidade de teste**: cortar fila em vez de inflar backlog inexecutável.
6. Registre **changelog** inicial: benchmark observado → decisão de testar → (depois) teste → resultado.
7. Exporte para Markdown/CSV com o script e **importe ou copie** para a planilha canônica de testes.

## Output Esperado

- lista priorizada de hipóteses;
- cada item com métrica, asset, evidência e dono sugerido;
- nota de encerramento do benchmark (sem pesquisa infinita — playbook Seção 3.3);
- bloco de changelog e checklist de aderência ao DoD (Seção 10.1).

Use `templates/backlog-hipoteses-benchmark.md`.
Use `templates/backlog-hipoteses-benchmark.json` com o script para priorizar e gerar relatório.

## Script Utilitário

```bash
python3 scripts/prioritize_benchmark_hypotheses.py templates/backlog-hipoteses-benchmark.json --md /tmp/backlog-benchmark.md --csv /tmp/backlog-benchmark.csv
```

## Definition Of Done

- Cada hipótese tem métrica de sucesso declarada.
- Evidência de benchmark está indicada (não só opinião).
- Prioridade reflete capacidade de teste e risco.
- Há registro de changelog ou campo preparado para atualização pós-teste.
- Backlog pode ser ingerido pela planilha de testes sem perda de rastreio.
