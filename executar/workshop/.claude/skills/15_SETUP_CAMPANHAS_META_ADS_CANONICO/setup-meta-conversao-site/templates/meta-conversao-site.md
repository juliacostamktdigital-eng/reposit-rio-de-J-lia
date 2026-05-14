# Meta Ads — Conversão no site — especificação

| Campo | Valor |
|-------|-------|
| Cliente | |
| Versão deste doc | |
| Data | |
| Responsável media | |
| Link planilha growth / backup | |
| Link contrato de dados | |
| Ref. estrutura campanhas (`setup-campanhas-meta-ads`) | |

---

## A. Escopo da conversão (playbook 15 — Seção 9)

| Campo | Valor |
|-------|-------|
| Tipo de conversão principal | lead formulário LP / agendamento / compra / trial / outro |
| Nome do evento de otimização na Meta (interface) | |
| Nome/ID do evento no funil (fonte da verdade) | |
| Volume esperado / hipótese (compatível com profundidade do evento) | |
| Justificativa **profundidade vs volume** (Seção 5) | |

---

## B. Pré-requisitos mínimos

| Critério | OK (s/n) | Evidência |
|----------|---------|-----------|
| LP / ambiente de conversão aprovado (QA) | | |
| Evento disparando em teste (Events Manager ou fluxo controlado) | | |
| Pixel instalado e eventos conferidos | | |
| CAPI configurada quando aplicável | | |
| Domínio verificado (se exigido pela conta/feature) | | |
| UTMs e taxonomia alinhadas ao plano | | |

---

## C. URLs e pontos de medição

| Destino | URL | Notas |
|---------|-----|-------|
| LP principal (URL final dos anúncios) | | |
| Thank-you / obrigado (se distinto e relevante ao pixel) | | |
| Página intermédia (se houver) | | |

**Parâmetros UTM / IDs obrigatórios na URL final:**

---

## D. Pixel, CAPI e eventos

| Campo | Valor |
|-------|-------|
| Pixel ID | |
| Evento(s) priorizado(s) na conta | |
| Resumo CAPI (token/partner / status) | |
| Deduplicação / same event ID (nota operacional) | |

**Eventos de suporte registrados (não necessariamente otimização):**

| Evento | Função no funil |
|--------|------------------|

---

## E. Públicos e exclusões (conversão)

| Audiência | Temperatura | Uso |
|-----------|-------------|-----|
| | | |

**Exclusões obrigatórias para não disputar com aquisição ou duplicar conversões:**

**Visitantes LP/site (30D etc.) — definição usada:**

---

## F. Estrutura de mídia (resumo)

*Detalhe completo em `estrutura-campanha-meta`; aqui só o que muda para conversão.*

| `campaign_id` | Objetivo na Meta | Notas |
|---------------|------------------|-------|

**Matriz de testes**

- **Varia neste ciclo:**  
- **Constante:**  

---

## G. Teste ponta a ponta

| Etapa | OK (s/n) | Data | Notas |
|-------|-----------|------|-------|
| Disparo teste visto na Meta (Ads / Events Manager) | | | |
| Se conversão = lead na LP: planilha backup | | | |
| Se conversão = lead na LP: CRM / handoff | | | |
| UTMs / origem preservados no legado esperado | | | |

---

## H. Checklist pré go-live — específico conversão site

| Item | OK (s/n) |
|------|---------|
| Nenhuma campanha de “conversão” sem evento validado (Seção 16) | |
| Pixel/eventos testados (Seção 13) | |
| Exclusões de convertidos definidas onde remarketing exige | |
| Orçamento por conjunto compatível com aprendizado (Seção 12) | |
| Change log preparado para mudanças de evento ou URL | |

---

## I. Gaps / N3

**Gaps para N2 ou evolução N3:**
