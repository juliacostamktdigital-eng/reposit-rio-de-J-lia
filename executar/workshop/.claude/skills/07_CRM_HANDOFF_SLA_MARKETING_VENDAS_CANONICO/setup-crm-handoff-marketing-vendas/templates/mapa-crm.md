# Mapa CRM Handoff Marketing-Vendas

## 1. Contexto

- Cliente:
- CRM:
- Responsável marketing:
- Responsável vendas:
- Data:
- Fonte do lead:
- Critério de sucesso:

## 2. Definições

| Estágio | Definição | Critério de entrada | Critério de saída | Dono |
| --- | --- | --- | --- | --- |
| Lead |  |  |  |  |
| MQL |  |  |  |  |
| SQL |  |  |  |  |
| Oportunidade |  |  |  |  |
| Venda/perda |  |  |  |  |

## 3. Campos CRM

| Campo | Categoria | Obrigatório? | Existe? | Regra | Observação |
| --- | --- | --- | --- | --- | --- |
| `lead_id` | identificação | sim |  |  |  |
| `first_utm_source` | origem | sim |  | não sobrescrever |  |
| `last_utm_source` | origem | sim |  | atualizar por conversão |  |
| `campaign_id` | origem | sim |  | preservar |  |
| `creative_id` | origem | sim |  | preservar |  |
| `lead_status` | funil | sim |  | lista fechada |  |
| `sales_owner` | atendimento | sim |  | obrigatório |  |
| `speed_to_lead_minutes` | atendimento | sim |  | calculado |  |
| `lead_quality` | qualidade | sim |  | lista/score |  |
| `disqualification_reason` | qualidade | sim |  | lista fechada |  |
| `feedback_notes` | qualidade | sim |  | texto controlado |  |

## 4. Status

### Lead Status

- `novo`
- `atribuido`
- `contatado`
- `conectado`
- `sem-resposta`
- `qualificado`
- `desqualificado`
- `duplicado`
- `invalido`

### MQL Status

- `pendente-validacao`
- `aceito-marketing`
- `rejeitado-marketing`
- `enviado-vendas`

### SQL Status

- `pendente-vendas`
- `aceito-vendas`
- `rejeitado-vendas`
- `em-diagnostico`

## 5. SLA

| Tipo de lead | Primeiro contato | Tentativas | Canais | Regra se não responder |
| --- | --- | --- | --- | --- |
| Quente | até 5 min | 3 no primeiro dia / 6 em 7 dias | telefone, WhatsApp, email | nurture |
| Morno | até 2h úteis | 3 em 7 dias | WhatsApp, email, telefone | nurture |
| Frio | assíncrono | retentativa por sinal | email/conteúdo | fluxo de conteúdo |

## 6. Roteamento

| Regra | Critério | Dono | Fallback | Alerta |
| --- | --- | --- | --- | --- |
| Segmento |  |  |  |  |
| Região |  |  |  |  |
| Ticket |  |  |  |  |
| Disponibilidade |  |  |  |  |

## 7. Contexto Para Vendas

| Campo | Origem | Obrigatório? | Observação |
| --- | --- | --- | --- |
| Campanha | UTM/CRM | sim |  |
| Criativo | UTM/CRM | sim |  |
| Promessa vista | copy/LP | sim |  |
| CTA clicado | LP/form | sim |  |
| Persona presumida | UTM/content | sim |  |
| Dor/ângulo | UTM/content | sim |  |
| Sugestão de abordagem | handoff/copy | sim |  |

## 8. Checklist N2

| Critério | Status | Evidência | Gap |
| --- | --- | --- | --- |
| Campos mínimos existem |  |  |  |
| Lead carrega origem |  |  |  |
| MQL/SQL definidos |  |  |  |
| SLA definido |  |  |  |
| Responsável comercial definido |  |  |  |
| Desqualificação obrigatória |  |  |  |
| Feedback volta para marketing |  |  |  |
| Teste ponta a ponta |  |  |  |
