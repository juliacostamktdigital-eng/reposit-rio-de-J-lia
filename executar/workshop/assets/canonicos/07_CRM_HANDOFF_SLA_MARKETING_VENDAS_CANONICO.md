# CRM, Handoff e SLA Marketing-Vendas Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/05-protocolo-handoff-a4.md`.  
**Decisão de merge:** skill 05 distribuída: `18_PROTOCOLO...` é âncora do handoff MQL->SQL e este arquivo mantém CRM/SLA como complemento operacional.


Status: v1 para workshop  
Escopo: clientes de Inside Sales / leadgen  
Objetivo: garantir que a demanda gerada por marketing seja recebida, qualificada, trabalhada e devolvida com feedback para o processo de growth.

## 1. Princípio

Marketing não termina no lead. Para o OS funcionar, o lead precisa carregar contexto até vendas e voltar com feedback.

Sem isso, a operação não sabe se:

- gerou lead ruim;
- gerou lead bom que não foi atendido;
- gerou lead bom para uma oferta errada;
- gerou lead certo para um comercial sem processo;
- gerou demanda qualificada que o CRM não registrou.

## 2. Objetivo do handoff

Este arquivo é o complemento operacional do Protocolo A-4 (`18_PROTOCOLO_HANDOFF_MQL_SQL_A4_CANONICO.md`): aqui vivem campos, status, SLA, roteamento, feedback e rotina dentro do CRM.

O handoff deve ligar:

```text
campanha -> criativo -> lead -> contexto do lead -> atendimento -> qualificação -> oportunidade -> venda/perda -> aprendizado
```

## 3. Definições obrigatórias

### Lead

Contato capturado por uma campanha, formulário, WhatsApp, evento, indicação ou canal orgânico.

### MQL

Lead que atende critérios mínimos de fit e intenção definidos entre marketing e vendas.

Exemplos de critérios:

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

### Venda

Negócio fechado ou contrato assinado.

## 4. Campos mínimos no CRM

Identificação:

- `lead_id`
- `created_at`
- `nome`
- `email`
- `telefone`
- `empresa`
- `cargo`
- `segmento`
- `cidade_estado`

Origem:

- `first_utm_source`
- `first_utm_medium`
- `first_utm_campaign`
- `first_utm_content`
- `first_utm_term`
- `last_utm_source`
- `last_utm_medium`
- `last_utm_campaign`
- `last_utm_content`
- `last_utm_term`
- `campaign_id`
- `adgroup_id`
- `creative_id`
- `test_id`

Funil:

- `lead_status`
- `mql_status`
- `sql_status`
- `opportunity_status`
- `deal_status`
- `lifecycle_stage`

Atendimento:

- `sales_owner`
- `assigned_at`
- `first_contact_at`
- `speed_to_lead_minutes`
- `contact_attempts`
- `last_contact_at`
- `next_step`
- `next_step_date`

Qualidade:

- `fit_score`
- `intent_score`
- `lead_quality`
- `disqualification_reason`
- `feedback_notes`

Comercial:

- `deal_value`
- `expected_close_date`
- `lost_reason`
- `won_at`
- `lost_at`

## 5. Status padronizados

### Lead status

```text
novo
atribuido
contatado
conectado
sem-resposta
qualificado
desqualificado
duplicado
invalido
```

### MQL status

```text
pendente-validacao
aceito-marketing
rejeitado-marketing
enviado-vendas
```

### SQL status

```text
pendente-vendas
aceito-vendas
rejeitado-vendas
em-diagnostico
```

### Opportunity status

```text
aberta
proposta-enviada
negociacao
ganha
perdida
sem-fit
```

## 6. Motivos de desqualificação

Usar lista fechada para permitir análise.

Valores recomendados:

```text
sem-fit
sem-budget
timing-ruim
nao-responde
fora-regiao
cargo-inadequado
empresa-inadequada
concorrente
estudante
fornecedor
duplicado
dados-invalidos
curioso
ja-cliente
outro
```

## 7. SLA de atendimento

Definir por tipo de lead.

### Lead quente

Exemplo:

- primeiro contato em até 5 minutos;
- mínimo de 3 tentativas no primeiro dia;
- mínimo de 6 tentativas em 7 dias;
- canais: telefone, WhatsApp, email;
- se não responder, entra em cadência de nurture.

### Lead morno

Exemplo:

- primeiro contato em até 2 horas úteis;
- mínimo de 3 tentativas em 7 dias;
- se não responder, nurture.

### Lead frio

Exemplo:

- qualificação assíncrona;
- fluxo de conteúdo;
- retentativa após novo sinal de intenção.

## 8. Roteamento

Definir:

- quem recebe cada tipo de lead;
- regra por segmento;
- regra por região;
- regra por ticket;
- regra por disponibilidade do vendedor;
- regra para redistribuição;
- alerta para gestor se SLA estourar.

## 9. Contexto que marketing deve enviar para vendas

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

Exemplo de resumo:

```text
Lead veio de campanha Meta TOFU para CFOs.
Criativo: vídeo com hook de ROI e risco financeiro.
Promessa vista: reduzir fraude sem travar onboarding.
Abordagem sugerida: abrir conversa sobre perdas financeiras e custo de falso positivo.
```

## 10. Script de primeiro contato

Deve conter:

- abertura contextual;
- referência ao interesse demonstrado;
- pergunta de qualificação;
- exploração da dor;
- conexão com promessa;
- próximo passo.

Exemplo:

```text
Oi, [nome]. Vi que você pediu mais informações sobre [tema/oferta].
Normalmente quem chega por esse material está tentando resolver [dor].
Hoje esse é um problema para vocês?
```

## 11. Feedback que vendas deve devolver para marketing

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

## 12. Rotina de feedback

Cadência sugerida:

- diária: SLA e leads sem atendimento;
- semanal: qualidade de leads e motivos de desqualificação;
- quinzenal: MQL/SQL por campanha/criativo;
- mensal: aprendizado para DCC, plano de mídia e criativos.

## 13. Como conectar com a planilha de testes

Campos que devem voltar para a planilha:

- `lead_id`
- `campaign_id`
- `creative_id`
- `test_id`
- `is_mql`
- `is_sql`
- `is_opportunity`
- `is_won`
- `disqualification_reason`
- `lead_quality`
- `speed_to_lead_minutes`
- `feedback_notes`

## 14. Como a IA deve usar esse asset

A IA pode:

- resumir contexto do lead para vendas;
- detectar lead sem atendimento;
- classificar motivos de desqualificação;
- resumir feedback comercial;
- apontar campanhas com lead barato e baixa qualidade;
- apontar criativos com lead caro e alta qualidade;
- sugerir ajustes de copy com base em objeções reais;
- gerar rebrief para próximo ciclo.

## 15. Critério N2

CRM/handoff está N2 quando:

- campos mínimos existem;
- lead carrega origem;
- MQL/SQL estão definidos;
- SLA está definido;
- responsável comercial está definido;
- motivo de desqualificação é obrigatório;
- feedback volta para marketing;
- existe evidência de teste ponta a ponta.

## 16. Critério N3

CRM/handoff está N3 quando:

- qualidade comercial entra no debrief;
- campanhas são avaliadas por MQL/SQL/venda;
- SLA é monitorado;
- motivos de perda alimentam copy e oferta;
- aprendizados comerciais viram novos testes;
- marketing e vendas revisam juntos o funil.

## 17. O que evitar

Evitar:

- CRM sem UTM;
- lead sem dono;
- SLA verbal;
- motivo de perda aberto demais;
- vendas rejeitar lead sem motivo;
- marketing otimizar sem ouvir vendas;
- considerar lead como resultado final;
- atualizar last-touch sobrescrevendo first-touch;
- não deduplicar leads.
