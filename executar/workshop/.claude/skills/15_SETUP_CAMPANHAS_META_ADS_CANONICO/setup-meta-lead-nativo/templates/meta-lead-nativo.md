# Meta Ads — Lead nativo (Instant Form) — especificação

| Campo | Valor |
|-------|-------|
| Cliente | |
| Versão deste doc | |
| Data | |
| Responsável media | |
| Link planilha growth / backup | |
| Link contrato de dados | |
| Referência estrutura campanhas (setup principal) | URL ou path do `estrutura-campanha-meta` preenchido |

---

## A. Pré-requisitos (playbook 15 — captação de leads / nativo)

Marque antes de publicar o formulário ou ligar verba.

| Critério | OK (s/n) | Evidência / nota |
|----------|---------|-------------------|
| Oferta e mensagem alinhadas ao DEOC / guardrails | | |
| CRM + SLA marketing–vendas definidos | | |
| Planilha backup ativa e dono definido | | |
| SLA de **primeiro contato** acordado por escrito **antes** de ativar lead nativo | | |
| Hipótese de teste e leitura registradas (planilha growth) | | |

---

## B. Lead Form (conteúdo e qualificação)

### B.1 Identificação na Meta

| Campo | Valor |
|-------|-------|
| Nome interno do formulário (na biblioteca / campanha) | |
| Idioma do form | |
| Estratégia volume vs intenção | volume maior / equilibrado / prioriza intenção |

### B.2 Introdução (instant experience)

- **Headline / promessa:**  
- **Benefício imediato / o que a pessoa recebe:**  
- **Coerência com o anúncio (mesma promessa):** s / n — notas:

### B.3 Campos

**Campos padrão Meta selecionados** (listar): nome, email, telefone, cidade, etc.

| Campo | Obrigatório (s/n) | Uso no MQL / CRM |
|-------|-------------------|------------------|

**Campos custom** (se houver):

| Pergunta / campo | Tipo | Obrigatório | Critério MQL / roteamento |
|------------------|------|-------------|---------------------------|

### B.4 Perguntas de qualificação

Mínimo coerente com o canônico: suficientes para intenção **sem** matar volume.

| # | Pergunta | Tipo de resposta | O que define lead “correto” / MQL |
|---|----------|------------------|-----------------------------------|

### B.5 Privacidade e compliance

- Link ou texto de política / base legal (nota operacional):  
- Consentimento / opções exibidas (resumo):  

### B.6 Pós-envio

- Mensagem de agradecimento:  
- Próximo passo (CTA): site / WhatsApp / agendar / outro:  
- Tempo esperado de retorno (alinhado ao SLA):  

---

## C. Origem, taxonomia e contrato de dados

| Campo | Valor |
|-------|-------|
| `campaign_id`(s) associados | |
| Como `adgroup_id` / `creative_id` chegam ao CRM (campos ou notas) | |
| UTMs ou parâmetros usados | |
| Campos obrigatórios no CRM para este fluxo (lista) | |

---

## D. Integração e operação

| Modo de destino | Detalhe (ferramenta, URL webhook, conta) |
|-----------------|------------------------------------------|
| CRM direto / Zapier / webhook / Leads Center / download manual | |

| Papel | Nome |
|-------|------|
| Owner técnico integração | |
| Owner comercial / SLA | |

### SLA de follow-up

| Parâmetro | Valor |
|-----------|-------|
| Tempo máximo até 1º contato (minutos / horas úteis) | |
| Canal do 1º contato | |
| Script ou playbook comercial (link) | |

---

## E. Públicos complementares (remarketing form)

| Audiência | Definição | Uso (conjunto / campanha) |
|-----------|-----------|---------------------------|
| Abriu form, não enviou | | |

**Exclusões** relevantes para não competir com aquisição ou duplicar lead:

---

## F. Teste ponta a ponta

| Etapa | OK (s/n) | Data | Notas |
|-------|-----------|------|-------|
| Envio lead teste | | | |
| Apareceu no CRM com campos corretos | | | |
| Apareceu na planilha backup | | | |
| Origem / IDs preservados | | | |

---

## G. Matriz de testes (lead nativo)

- **O que varia neste ciclo:**  
- **O que fica constante:**  

---

## H. Checklist pré go-live — específico lead nativo

| Item | OK (s/n) |
|------|---------|
| Campos e perguntas conferidos com vendas / MQL | |
| Integração testada com lead real | |
| SLA comunicado ao time que responde | |
| Remarketing “aberto sem envio” definido (se aplicável) | |
| Não há objetivo de otimizar só CPL sem critério de qualidade na planilha | |

---

## I. Gaps / N3

**Gaps conhecidos para fechar N2 ou evoluir N3:**
