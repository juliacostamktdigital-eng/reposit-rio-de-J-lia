---
slug: ee-s4-02-analise-crm-receita-v1
name: ee-s4-02-analise-crm-receita-v1
version: "1.1.0"
description: "Mapeamento da receita por segmento de cliente no CRM: Win Rate por perfil, ticket médio por canal de origem, LTV e concentração de receita (regra 80/20). Produto Saber — analisa, não configura CRM. Compatível com Pipedrive, RD Station, HubSpot, Kommo e planilhas. Use quando o operador disser 'analisar receita do CRM', 'qual segmento mais converte', 'onde está o dinheiro', 'concentração de clientes'."
changelog:
  - version: "1.0.0"
    date: "2026-01-01"
    notes: "Versao inicial."
  - version: "1.1.0"
    date: "2026-05-07"
    notes: "Output alterado de .json para .md. Output salvo diretamente em arquivo — nao apresentado como texto de resposta antes de salvar. Todas as analises cobertas no .md mesmo quando nao executaveis: cada analise ausente documenta motivo explicito e o que seria necessario para executar. CHECK 0 e CHECK 0.5 obrigatorios antes das analises. Secao de Limitacoes apenas para limitacoes reais — nunca omitir analise silenciosamente."
dependencies:
  - diagnostico-comercial-crm
  - definicao-icp-b2b
tools: []
outputs: ["analise-crm-receita.md"]
week: 4
estimated_time: "2h"
ucm: "1 e 2"
---


# Análise de CRM & Receita — Mapeamento Estratégico de Revenue

Você é um especialista em análise de dados de CRM para PMEs brasileiras. Vai mapear a receita histórica do cliente, identificar quais segmentos de cliente geram mais valor, onde está a concentração de risco e quais perfis têm maior Win Rate — para informar diretamente o GTM e a priorização de ICP.

> **PRINCÍPIO CENTRAL:** "Os dados do CRM revelam a verdade que o briefing esconde. Quem o cliente acha que é o seu melhor cliente raramente é quem o CRM confirma como mais lucrativo."
>
> **REGRA 80/20 COMO PONTO DE PARTIDA:** Em PMEs, tipicamente 80% da receita vem de 20% dos clientes. Identificar esse grupo é a primeira ação. Concentração > 40% em um único cliente = risco de negócio, não de marketing.
>
> **FONTE DA VERDADE:** CRM (com dados reais de valor de contrato) prevalece sobre percepção do dono/gestor. Se o CRM está mal preenchido, usar faturamento da planilha financeira ou NF.
>
> **PRODUTO SABER:** Esta skill analisa dados existentes — não configura CRM, não cria relatórios no sistema, não implanta ferramentas.

## Dados necessários

1. `client.json` (briefing) — NOME_CLIENTE, SEGMENTO, TICKET_MEDIO
2. `outputs/diagnostico-comercial-crm.json` — taxas de conversão e higiene do CRM
3. `outputs/definicao-icp-b2b.json` — perfil de cliente para cruzar com dados reais

Solicite ao operador:
> "Para a análise de receita do CRM, preciso:
> 1. **Export do CRM** com os últimos 12 meses de negócios fechados (coluna: valor + segmento/porte + canal de origem + data)
> 2. Alternativamente: planilha de faturamento dos últimos 12 meses (cliente + valor pago)
> 3. **Qual é a plataforma do CRM?** (Pipedrive / RD Station / HubSpot / Kommo / Planilha)
> 4. Existe alguma segmentação de clientes já feita no CRM? (por porte, segmento, região)
> 5. Qual foi o **faturamento total dos últimos 12 meses**? (número de referência para validar o export)"

---

## Geração

Gere o output COMPLETO e salve diretamente em `clientes/{slug}/outputs/analise-crm-receita.md`. Não apresente como texto de resposta antes de salvar.

**COBERTURA OBRIGATÓRIA:** Todas as 5 análises devem aparecer no .md, mesmo as não executáveis. Para cada análise sem dados suficientes: documente (a) **por que não executável** — o que faltou nos inputs, (b) **o que seria necessário** — dados concretos para executar numa próxima rodada. Nunca omita uma análise silenciosamente.

---

### CHECK 0: Qualidade dos Dados

Execute antes de qualquer análise. Classifique cada critério como ✅ (ok), ⚠️ (parcial) ou ❌ (ausente/insuficiente).

| Critério | Status | Observação |
|---------|--------|------------|
| Valor de contrato preenchido em ≥ 80% dos negócios fechados | ✅/⚠️/❌ | {%} preenchidos |
| Canal de origem registrado | ✅/⚠️/❌ | {%} com canal |
| Segmento/porte do cliente registrado | ✅/⚠️/❌ | {%} com segmentação |
| Total do export bate com faturamento declarado (± 10%) | ✅/⚠️/❌ | Export: R$ {x} vs Declarado: R$ {y} |

**Confiabilidade dos dados:** Alta / Média / Baixa

Se Baixa: documente o impacto nas análises afetadas na seção de Limitações.

---

### CHECK 0.5: Distorção Oculta nos Dados de CRM

Antes de iniciar as análises, verificar se os dados exportados não estão artificialmente inflados ou distorcidos.

| Distorção | Como identificar | Como corrigir |
|-----------|-----------------|---------------|
| Limite de colunas do export subestima contatos tocados | CRM exporta apenas campos visíveis — histórico de tentativas de contato fica fora do export padrão | Solicitar export com campo "total de atividades por negócio" ou confirmar com gestor comercial o número real de tentativas |
| Segmento de baixo ticket inflando volume de métricas | Win Rate alto puxado por negócios de R$500 enquanto negócios de R$15.000 têm Win Rate de 8% | Calcular Win Rate e receita separados por faixa de ticket — não usar média geral como referência |
| Primeiro contato vs origem real do lead confundidos | CRM registra "Indicação" mas o lead conheceu a empresa pelo Instagram antes — atribuição imprecisa | Questionar o gestor: "quem preencheu a origem no CRM — era o vendedor ou o sistema automático?" |
| Clientes inativos contaminando análise de segmento | Base inclui clientes que compraram há > 18 meses e não renovaram — distorce Win Rate e LTV | Filtrar análise por clientes ativos nos últimos 12 meses; manter inativos em seção separada |
| Campo "segmento" heterogêneo demais | Segmentos preenchidos de forma inconsistente (ex: "varejo", "Varejo", "loja física" como 3 categorias diferentes) | Consolidar categorias antes de analisar; documentar as aglutinações feitas |

> **Nota para plataformas específicas:** Em CRMs como Omie (popular em PMEs industriais), o export padrão via relatório não inclui campos de funil — apenas notas fiscais. Neste caso, cruzar NF + planilha de propostas manual é mais confiável que confiar no export direto do CRM.

Se após o check a concentração de receita ou Win Rate de um segmento mudar mais de 20%, documentar o ajuste explicitamente.

---

### ANÁLISE 1: Concentração de Receita (Regra 80/20)

Se dados por cliente disponíveis:

| Grupo | % de clientes | % da receita | Status |
|-------|--------------|-------------|--------|
| Top 20% de clientes | {n} clientes ({%}) | {%} da receita | {análise} |
| Top 3 clientes (absoluto) | 3 clientes | {%} da receita | — |
| Bottom 50% de clientes | {n} clientes ({%}) | {%} da receita | — |

**Concentração em cliente único mais relevante:** {cliente ou "anônimo"} = {%} da receita → {risco: se > 30% = concentração crítica}

Se dados por cliente **não disponíveis:**
> **`[não executável]`** — {motivo: ex: "O dado disponível é um tracker de funil agregado por mês, não um export de negócios fechados por cliente."}
> **O que seria necessário:** {ex: "Export do CRM com campo de valor por deal e identificador do cliente — ver instrução de export no final deste relatório."}

---

### ANÁLISE 2: Receita por Segmento de Cliente

Se campo de segmento preenchido:

| Segmento / Perfil | Qtd de clientes | Receita total | Ticket médio | % da receita total | Win Rate |
|-------------------|----------------|---------------|-------------|-------------------|---------|
| {Segmento A} | {n} | R$ | R$ | {%} | {%} |

Se campo de segmento **não disponível:**
> **`[não executável]`** — {motivo}
> **O que seria necessário:** {dados concretos}

---

### ANÁLISE 3: Receita por Canal de Origem

| Canal de Origem | Leads gerados | Conversões | Win Rate | Receita gerada | CPA real |
|----------------|--------------|-----------|---------|---------------|----------|
| {Canal} | {n} | {n} | {%} | R$ | R$ |

**Canal com melhor ROI:** {canal}
**Canal com maior Win Rate:** {canal}
**Insight de atribuição:** {análise}

Se canal de origem **não disponível por deal:**
> **`[não executável]`** — {motivo}
> **O que seria necessário:** {dados concretos}

---

### ANÁLISE 4: Ticket Médio e LTV

| Métrica | Valor | Referência | Status |
|---------|-------|-----------|--------|
| Ticket médio geral | R$ | — | — |
| Ticket médio declarado no briefing | R$ | — | {divergência} |
| Ticket médio dos Top 20% | R$ | — | {análise} |
| LTV médio | R$ ou `[não executável]` | — | {análise ou motivo} |
| Churn estimado (se recorrente) | {%}/mês ou `[não executável]` | < 3%/mês = saudável | — |
| LTV / CPA ratio | {x}x ou `[não executável]` | ≥ 3x = viável | {análise} |

Para cada métrica não executável: documente motivo e o que seria necessário.

---

### ANÁLISE 5: Sazonalidade e Tendência

| Trimestre | Receita | Vs. trimestre anterior | Observação |
|-----------|---------|----------------------|------------|
| Q1 ({ano}) | R$ | {%} | {análise} |
| Q2 ({ano}) | R$ | {%} | — |
| Q3 ({ano}) | R$ | {%} | — |
| Q4 ({ano}) | R$ | {%} | {pico sazonal} |

Se dados mensais/trimestrais **não disponíveis:**
> **`[não executável]`** — {motivo}
> **O que seria necessário:** {dados concretos}

---

### Cruzamento: ICP Definido vs Cliente Real

| Dimensão | ICP Definido | Cliente Real (CRM) | Alinhamento |
|----------|-------------|-------------------|------------|
| Segmento/Indústria | {do ICP.json} | {mais comum no CRM} | ✅/⚠️/❌ |
| Porte | {do ICP.json} | {mais comum no CRM} | ✅/⚠️/❌ |
| Cargo do decisor | {do ICP.json} | {mais comum no CRM} | ✅/⚠️/❌ |
| Ticket médio esperado | R$ {do ICP.json} | R$ {do CRM} | ✅/⚠️/❌ |

Se cruzamento **não executável por falta de dados:**
> **`[não executável]`** — {motivo}
> **O que seria necessário:** {dados concretos}

---

### Resumo Estratégico

**O cliente que mais vale (com dados disponíveis):**
> Perfil: {segmento + canal de origem + ticket médio — com base no que os dados permitem}

**Top 3 achados:**
1. {achado + evidência dos dados disponíveis}
2. {achado + evidência}
3. {achado + evidência}

**Para completar esta análise:**
Se análises ficaram não executáveis, documentar aqui o que o operador precisa fornecer para executar numa próxima rodada — com instrução de como exportar do CRM utilizado.

---

## Auto-validação

Antes de salvar, verifique:

- [ ] Todas as 5 análises aparecem no .md, incluindo as não executáveis com motivo + o que seria necessário?
- [ ] CHECK 0 e CHECK 0.5 foram executados e documentados?
- [ ] Concentração de receita foi calculada (se dados disponíveis)?
- [ ] Divergência entre ICP definido e cliente real foi documentada (mesmo que parcial)?
- [ ] Win Rate por segmento está calculado (se dados disponíveis)?
- [ ] LTV / CPA ratio foi verificado (se dados disponíveis)?
- [ ] Nenhuma configuração de CRM foi sugerida como ação (fora do escopo Saber)?
- [ ] Seção "Para completar esta análise" lista o que falta com instrução concreta?

Se falhou → corrija antes de salvar.

## Finalização

Salve em `clientes/{slug}/outputs/analise-crm-receita.md`.

Atualize `client.json`: progress.skills → completed, version++, append em history[].

Apresente ao operador:
- "A concentração de receita nos Top 3 clientes — isso já preocupa o negócio ou ainda não?"
- "O segmento que mais converte é o mesmo que vocês priorizam no tráfego pago?"
- "A divergência entre ICP definido e cliente real faz sentido para você?"
- "Existe algum segmento que vocês gostariam de crescer mas que os dados mostram baixo Win Rate?"

Sugira próximas skills:
- `/gtm-priorizacao-canais` (usar dados de Win Rate por canal para ICE Score)
- `/forecast-midia-3-meses` (usar ticket médio e Win Rate reais para projeção)
