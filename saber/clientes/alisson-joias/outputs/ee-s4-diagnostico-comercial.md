# Diagnóstico Comercial — Alisson Joias

> **Data:** 07/05/2026
> **Fontes:** CSV de acompanhamento mensal (jan/2025–jan/2026) · Transcrição Kick-Off 05/02/2026 · Screenshots CRM Kommo (abril/2026) · Cliente Oculto WhatsApp (07/05/2026)
> Dados não disponíveis sinalizados como `[não disponível]`.

---

## 1. Funil de Vendas — Taxas vs Benchmarks

### 1.1 Funil Geral (Orgânico + Mídia) — Janeiro/2026

| Etapa | Volume | Taxa Real | Benchmark¹ | Gap | Status |
|---|---|---|---|---|---|
| Lead → Qualificado | 678 → 516 | **76,1%** | 30–50% | +26–46pp | ACIMA |
| Qualificado → Orçamento | 516 → 297 | **57,6%** | 50–65% | no range | NO BENCHMARK |
| Orçamento → Negociação | 297 → 146 | **49,2%** | 40–60% | no range | NO BENCHMARK |
| Negociação → Venda | 146 → 130 | **89,0%** | 70–85% | +4–19pp | ACIMA |
| **Lead → Venda (total)** | 678 → 130 | **19,2%** | 3–8% | +11–16pp | **ACIMA** |

¹ Referência: varejo consultivo de ticket médio-alto (framework-diagnostico-comercial.md)

**Leitura:** O funil orgânico performa 2–4× acima do benchmark. Quem chega pelo canal próprio (WhatsApp orgânico, Instagram, indicação) converte bem. O processo humano funciona para o canal que o time domina.

---

### 1.2 Funil de Mídia Paga (Meta Ads) — Janeiro/2026

| Etapa | Volume | Taxa Real | Benchmark | Gap | Status |
|---|---|---|---|---|---|
| Lead → Qualificado | 369 → 90 | **24,4%** | 30–50% | −6 a −26pp | ABAIXO |
| Qualificado → Orçamento | 90 → 26 | **28,9%** | 50–65% | −21 a −36pp | CRÍTICO |
| Orçamento → Negociação | 26 → 3 | **11,5%** | 40–60% | −28 a −48pp | CRÍTICO |
| Negociação → Venda | 3 → 2 | 66,7% | 70–85% | — (n pequeno) | — |
| **Lead → Venda (mídia)** | 369 → 2 | **0,54%** | 3–8% | −2,5 a −7,5pp | **CRÍTICO** |

**Causa raiz identificada:** Leads chegando via formulário. A consultora precisa iniciar o contato pelo WhatsApp Business Cloud API usando Message Template (custo por disparo + aprovação da Meta). Resultado: leads chegando à noite, janela de 24h perdida sem automação ativa. Confirmado por Leivany (tráfego) e Alisson no Kick-Off.

**Impacto financeiro estimado:**
- Cenário atual: 369 leads × 0,54% = 2 vendas → R$ 7.805 faturados
- Cenário com 10% de conversão (conservador para o segmento): 37 vendas × R$ 4.812 ticket médio = **R$ 178.044**
- **Diferença: ~R$ 170k/mês com o mesmo investimento de R$ 1.233**

> Jan/2026 é o primeiro mês com tráfego pago relevante (1,25% do share de leads vs 100% orgânico). O CPA de R$ 475,88 por venda de mídia é aceitável — o problema não é o custo do lead, é a taxa de conversão.

---

### 1.3 Evolução do Funil — 2025 completo

| Mês | Leads | Vendas | Conv. L→V | Faturamento | Ticket Médio |
|---|---|---|---|---|---|
| Jan/25 | 917 | 201 | 21,9% | R$ 670k | R$ 3.334 |
| Mar/25 | 671 | 225 | 33,5% | R$ 706k | R$ 3.141 |
| Mai/25 | 757 | 263 | 34,7% | R$ 863k | R$ 3.284 |
| Jun/25 | 473 | 239 | 50,5% | R$ 748k | R$ 3.131 |
| Nov/25 | 947 | 294 | 31,0% | **R$ 1.171k** | R$ 3.983 |
| Dez/25 | 740 | 179 | 24,2% | R$ 668k | R$ 3.735 |
| Jan/26 | 678 | 130 | 19,2% | R$ 625k | **R$ 4.812** |

**Padrões:**
- Novembro é o pico absoluto (Black Friday) — 40% acima do segundo melhor mês
- Ticket médio em crescimento consistente: R$ 3.334 (jan/25) → R$ 4.812 (jan/26) = +44% em 12 meses
- Volume de leads em queda de set/25 para jan/26, mas margem por venda aumentando — sinal de reposicionamento funcionando
- A taxa de conversão negociação→venda acima de 85% em quase todos os meses indica que quem chega à negociação fecha

---

## 2. Processo Comercial e CRM

### 2.1 Higiene do CRM (Kommo)

**Campos preenchidos — observação dos screenshots:**

| Campo | Status observado |
|---|---|
| Etapa do funil | Preenchido em todos os leads visíveis |
| Ticket / valor da negociação | Inconsistente — visto R$ 1 (placeholder), R$ 1.730, R$ 2.500, R$ 52.450 |
| Vendedora responsável | Preenchido na maioria |
| Produto / tipo de peça | `[Selecione]` — não preenchido na maioria dos leads visíveis |
| Forma de entrega | `Nenhum` / em branco na maioria |
| Tipo de entrega | `Nenhum` em todos os leads visualizados |
| Observações sobre o item | Em branco nos leads visualizados |
| Data de criação do lead | Presente |
| Data da última atividade | Presente via histórico de mensagens |

**Conclusão sobre higiene:** Campos comerciais críticos (produto, forma de entrega, ticket real) não são preenchidos sistematicamente. O CRM está sendo usado como inbox de WhatsApp, não como ferramenta de gestão de funil.

---

**Leads Zumbi — sinal identificado:**

Nos screenshots do CRM, um lead específico ("Lúcia Mãe do Benício") apresenta automação disparando a mesma mensagem template repetidas vezes sem resposta do lead e sem evolução de etapa. A tarefa registrada é "Acompanhar" — genérica, sem prazo ou ação específica.

No Kick-Off (fev/2026), Tássio Câmara reportou 43 tarefas atrasadas no painel. Número atual não disponível nos inputs.

Padrão de tarefa dominante nos leads visualizados: **"Acompanhar"** — sem especificação da próxima ação, sem prazo, sem critério de saída da etapa.

---

**LRT (Lead Response Time) — observação indireta:**

Não há dado sistematizado de LRT disponível nos inputs. O que foi observado:
- Automação de follow-up ativa no Kommo com alertas "Não deixar esse lead esfriar!" — indica que o problema de demora é reconhecido e tentou-se resolver via automação
- No Kick-Off, Alisson confirmou que leads chegam à noite sem resposta imediata
- Leivany (tráfego) afirmou que a automação resolveria a quebra de contato noturno

**`[não disponível]`** tempo médio de primeira resposta por lead, por canal e por consultora.

---

### 2.2 Processo Declarado vs Processo Real

| Dimensão | Declarado (Kick-Off) | Real (observado nos inputs) |
|---|---|---|
| Uso do CRM | "O time tem prática no CRM, está plugado ao ERP" | Consultoras respondem fora do CRM pelo WhatsApp direto — leads não mudam de etapa |
| Tarefas | "A gerente faz acompanhamento focando em tarefas e na regra 80/20" | Tarefas dominantemente genéricas ("Acompanhar"), sem ação estratégica definida |
| Playbook | "O playbook e a cadência é o gargalo principal" (reconhecido como inexistente) | Cada consultora decide a estratégia na hora da tarefa |
| Qualificação | Sem lead score definido — "o time se confunde sobre em qual lead focar" | Confirmado nos screenshots: sem campo de scoring visível no CRM |
| Automação | Cloud API WhatsApp conectada há ~1 semana no kick-off | SalesBot ativo (pós-venda, follow-up), mas com erros de disparo duplicado identificados |

---

### 2.3 Análise do Atendimento — Cliente Oculto (07/05/2026)

**Canal de entrada:** WhatsApp (número +55 85 9771-1274)
**Produto solicitado:** Aliança de casamento

**O que funcionou:**
- Consultora assumiu o atendimento após abertura automática
- Conduziu qualificação natural: ocasião, tamanho do aro, preferência de material e modelo
- Apresentou catálogo segmentado (Alianças Clássicas) de forma visual e organizada
- Listou benefícios proativamente: garantia vitalícia, certificado de autenticidade, entrega em 7 dias, fabricação própria
- Tom adequado ao posicionamento premium (sem pressão de fechamento)

**O que não funcionou / pontos de atenção:**
- A abertura da conversa foi via automação com mensagem de boas-vindas, mas o texto continha uma frase de difícil leitura ("a mensagem e a frequência com que nos comunicamos por enquanto...") — sinal de template não revisado
- O orçamento apresentado listou múltiplos produtos com preços e referências em formato confuso, misturando valores de produtos distintos sem hierarquia clara
- Não foi identificado momento de fechamento ou próximo passo claro ao final da conversa visível

**Ciclo observado no cliente oculto:** Abertura → qualificação de produto → envio de catálogo → cotação → sem confirmação de próximo passo visível nos inputs disponíveis.

---

### 2.4 Perfil do Time — Hunter vs Farmer

| Dimensão | Evidência |
|---|---|
| **Farmer (predominante)** | Conversão orgânica de 19% — quem vem pela base converte muito bem |
| **Farmer** | Alta recorrência de clientes com ticket e taxa de conversão maiores que novos leads (confirmado no Kick-Off) |
| **Farmer** | Time otimizado para atender quem já tem relacionamento com a marca |
| **Hunter (fragilidade)** | 0,54% de conversão em leads frios de mídia paga |
| **Hunter** | Sem script ou cadência para leads que não iniciaram contato por conta própria |
| **Hunter** | Consultoras com 100–200 leads simultâneos — volume incompatível com perfil Farmer de alta personalização |

**Diagnóstico:** O time comercial da Alisson Joias é estruturalmente Farmer sendo pressionado a operar como Hunter. A estratégia de tráfego pago exige um perfil Hunter na ponta (SDR de qualificação e ativação) para que o Farmer (consultoras) foque apenas no fechamento. Sem essa separação, o volume de leads frios degrada a qualidade do atendimento aos leads quentes.

---

## 3. SLA de Atendimento por Score

Alisson Joias opera com ciclo de venda de 1–7 dias para o canal orgânico. Para leads de casamento (aliança), o ciclo de consideração pode ser maior, mas a decisão de fechar tende a ser rápida quando a confiança está estabelecida.

| Score | SLA | Responsável | Canal | Alerta se não cumprido |
|---|---|---|---|---|
| ⭐⭐⭐⭐⭐ Lead quente | **5 minutos** | Consultora sênior designada | WhatsApp direto + abordagem personalizada | Escalar para gerente imediatamente |
| ⭐⭐⭐⭐ Qualificado | **1 hora** | Consultora do turno | WhatsApp via CRM | Alerta automático para gerente após 90 min |
| ⭐⭐⭐ Morno | **Régua automática em 4h** | SDR IA / Salesbot | Sequência WhatsApp | Consultora entra apenas se lead responder |
| ⭐⭐ / ⭐ Frio | **Nutrição passiva em 7 dias** | Automação | Disparo segmentado | Sem alerta — revisar mensalmente |

> **Observação crítica:** O SLA de 5 minutos para leads quentes é hoje inviável para leads de mídia paga vindos de formulário — a consultora depende de Message Template para iniciar o contato (custo + aprovação Meta). O SLA só é executável se o canal de entrada do lead mudar para Click-to-WhatsApp.

---

## Consolidado

```
✅ FUNCIONANDO                        ❌ QUEBRADO / CRÍTICO
──────────────────────────────────    ──────────────────────────────────────
Funil orgânico: 19% L→V              Funil mídia paga: 0,54% L→V
Ticket médio +44% em 12 meses        Formulário mata janela de 24h
Sistema de comissionamento           Leads não mudam etapa no CRM
  protege margem                     Consultoras respondem fora do CRM
Automação pós-venda ativa            Salesbot com erro de disparo duplicado
Alta recorrência de clientes         Campos CRM sem preenchimento sistemático
Fabricação própria (entrega 7 dias)  RFM identificado mas não ativado
Black Friday R$ 1,17M (nov/25)       Time Farmer operando como Hunter
                                       sem estrutura SDR
```
