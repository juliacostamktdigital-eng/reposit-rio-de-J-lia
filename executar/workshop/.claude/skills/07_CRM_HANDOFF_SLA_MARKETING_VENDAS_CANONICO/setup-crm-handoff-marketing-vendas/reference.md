# Referência Do Setup CRM Handoff Marketing-Vendas

Fonte normativa: `assets/canonicos/07_CRM_HANDOFF_SLA_MARKETING_VENDAS_CANONICO.md`.

## Princípio

Marketing não termina no lead. Para o OS funcionar, o lead precisa carregar contexto até vendas e voltar com feedback.

O handoff deve ligar:

```text
campanha -> criativo -> lead -> contexto do lead -> atendimento -> qualificação -> oportunidade -> venda/perda -> aprendizado
```

## Definições

### Lead

Contato capturado por campanha, formulário, WhatsApp, evento, indicação ou canal orgânico.

### MQL

Lead que atende critérios mínimos de fit e intenção definidos entre marketing e vendas.

Exemplos:

- cargo adequado;
- empresa no ICP;
- segmento atendido;
- dor compatível;
- orçamento provável;
- respondeu ou agendou;
- demonstrou interesse real;
- não é duplicado ou inválido.

### SQL

MQL aceito por vendas como oportunidade real de abordagem comercial.

### Oportunidade

SQL com diagnóstico/necessidade validada e próximo passo comercial claro.

## Campos Mínimos No CRM

### Identificação

- `lead_id`;
- `created_at`;
- `nome`;
- `email`;
- `telefone`;
- `empresa`;
- `cargo`;
- `segmento`;
- `cidade_estado`.

### Origem

- `first_utm_source`;
- `first_utm_medium`;
- `first_utm_campaign`;
- `first_utm_content`;
- `first_utm_term`;
- `last_utm_source`;
- `last_utm_medium`;
- `last_utm_campaign`;
- `last_utm_content`;
- `last_utm_term`;
- `campaign_id`;
- `adgroup_id`;
- `creative_id`;
- `test_id`.

### Funil

- `lead_status`;
- `mql_status`;
- `sql_status`;
- `opportunity_status`;
- `deal_status`;
- `lifecycle_stage`.

### Atendimento

- `sales_owner`;
- `assigned_at`;
- `first_contact_at`;
- `speed_to_lead_minutes`;
- `contact_attempts`;
- `last_contact_at`;
- `next_step`;
- `next_step_date`.

### Qualidade

- `fit_score`;
- `intent_score`;
- `lead_quality`;
- `disqualification_reason`;
- `feedback_notes`.

### Comercial

- `deal_value`;
- `expected_close_date`;
- `lost_reason`;
- `won_at`;
- `lost_at`.

## Status Padronizados

### Lead Status

- `novo`;
- `atribuido`;
- `contatado`;
- `conectado`;
- `sem-resposta`;
- `qualificado`;
- `desqualificado`;
- `duplicado`;
- `invalido`.

### MQL Status

- `pendente-validacao`;
- `aceito-marketing`;
- `rejeitado-marketing`;
- `enviado-vendas`.

### SQL Status

- `pendente-vendas`;
- `aceito-vendas`;
- `rejeitado-vendas`;
- `em-diagnostico`.

### Opportunity Status

- `aberta`;
- `proposta-enviada`;
- `negociacao`;
- `ganha`;
- `perdida`;
- `sem-fit`.

## Motivos De Desqualificação

Usar lista fechada:

- `sem-fit`;
- `sem-budget`;
- `timing-ruim`;
- `nao-responde`;
- `fora-regiao`;
- `cargo-inadequado`;
- `empresa-inadequada`;
- `concorrente`;
- `estudante`;
- `fornecedor`;
- `duplicado`;
- `dados-invalidos`;
- `curioso`;
- `ja-cliente`;
- `outro`.

## SLA

### Lead Quente

- primeiro contato em até 5 minutos;
- mínimo de 3 tentativas no primeiro dia;
- mínimo de 6 tentativas em 7 dias;
- canais: telefone, WhatsApp, email;
- se não responder, nurture.

### Lead Morno

- primeiro contato em até 2 horas úteis;
- mínimo de 3 tentativas em 7 dias;
- se não responder, nurture.

### Lead Frio

- qualificação assíncrona;
- fluxo de conteúdo;
- retentativa após novo sinal de intenção.

## Contexto Para Vendas

Cada lead deveria chegar com:

- campanha de origem;
- criativo de origem;
- promessa vista;
- CTA clicado;
- persona presumida;
- dor/ângulo do criativo;
- etapa do funil;
- formulário preenchido;
- página de conversão;
- observação da campanha;
- sugestão de abordagem.

## Feedback Para Marketing

Campos obrigatórios:

- lead era válido?
- era ICP?
- tinha dor real?
- tinha timing?
- tinha orçamento?
- entendeu a oferta?
- objeção principal;
- motivo de perda/desqualificação;
- qualidade percebida;
- comentário livre.

## Critério N2

CRM/handoff está N2 quando:

- campos mínimos existem;
- lead carrega origem;
- MQL/SQL estão definidos;
- SLA está definido;
- responsável comercial está definido;
- motivo de desqualificação é obrigatório;
- feedback volta para marketing;
- existe evidência de teste ponta a ponta.

## Critério N3

CRM/handoff está N3 quando:

- qualidade comercial entra no debrief;
- campanhas são avaliadas por MQL/SQL/venda;
- SLA é monitorado;
- motivos de perda alimentam copy e oferta;
- aprendizados comerciais viram novos testes;
- marketing e vendas revisam juntos o funil.
