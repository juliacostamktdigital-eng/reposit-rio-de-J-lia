# Contrato de Dados Marketing -> CRM e Backup de UTMs
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + canônico original sem skill merge dedicada.  
**Decisão de merge:** sem skill dedicada; mantido como contrato de dados transversal.


Status: v1 para workshop  
Escopo: armazenamento, match e análise pós-campanha de UTMs, IDs, leads e avanço no funil  
Objetivo: definir onde armazenar UTMs e como estruturar uma fonte de verdade analisável para retro-otimizar campanhas.

## 1. Princípio

O tracking não termina quando a UTM chega no formulário. O tracking só está útil quando permite responder depois:

```text
qual campanha, conjunto e criativo geraram leads que avançaram no funil?
```

Para isso, a operação precisa de um contrato de dados entre:

- mídia;
- LP/formulário/WhatsApp;
- planilha backup;
- CRM;
- planilha de testes;
- dashboard/debrief.

## 2. Onde armazenar as UTMs

### Camada 1 - URL

UTMs vêm na URL de entrada.

Função:

- transportar origem até a LP ou ponto de conversão.

Limitação:

- pode se perder se usuário navegar, voltar depois ou converter em outro canal.

### Camada 2 - Browser/session storage/cookie

Guardar first-touch e last-touch no navegador.

Função:

- preservar origem mesmo se o usuário navegar antes de converter.

Regras:

- first-touch: gravar uma vez e não sobrescrever;
- last-touch: atualizar a cada nova visita/conversão relevante;
- TTL sugerido: 90 a 180 dias em B2B/inside sales.

### Camada 3 - Campos ocultos no formulário

Enviar UTMs e IDs junto com o lead.

Função:

- garantir que a origem vire dado do lead.

Campos:

- `first_utm_*`;
- `last_utm_*`;
- `v4_client_id`;
- `v4_campaign_id`;
- `v4_adgroup_id`;
- `v4_creative_id`;
- `v4_test_id`;
- URL da LP;
- timestamp.

### Camada 4 - Planilha de backup

Armazenar todo lead capturado em uma tabela padronizada, independente do CRM do cliente.

Função:

- evitar perda de dados quando o CRM não recebe UTMs;
- permitir deduplicação;
- permitir export/análise;
- servir como fallback para projetos com CRM frágil.

### Camada 5 - CRM

Armazenar origem, status e avanço comercial.

Função:

- permitir leitura de funil e receita por origem.

### Camada 6 - Base analítica / planilha de testes

Cruzar mídia + leads + CRM.

Função:

- retro-otimizar campanhas por qualidade real.

## 3. Resposta direta: precisa de planilha de backup?

Sim. Sempre.

Todo cliente deve ter uma planilha de backup padronizada, mesmo quando o CRM parece confiável.

Motivos:

- o CRM pode não receber todos os campos;
- integrações podem falhar sem aviso;
- o cliente pode alterar etapas/campos;
- exportações de mídia e CRM podem não bater;
- a operação precisa de uma fonte mínima para auditoria e análise pós-campanha;
- a planilha de growth precisa de uma base estável para cruzar campanha, conjunto, criativo, lead e qualidade comercial.

Ela não substitui o CRM. Ela é o cinto de segurança do tracking.

## 4. Formato padrão da planilha de backup

Nome sugerido:

```text
backup_leads_{client_id}_{ano_mes}
```

Exemplo:

```text
backup_leads_cli-hs-prevent_2026-05
```

## 5. Abas recomendadas

### Aba 00_README

Campos/conteúdo:

- cliente;
- período;
- dono;
- origem dos dados;
- link da LP;
- link CRM;
- link plano de mídia;
- link taxonomia UTM;
- data da última atualização;
- observações de qualidade de dados.

### Aba 01_RAW_LEADS

Registro bruto de todo lead capturado.

Colunas:

- `raw_row_id`
- `captured_at`
- `source_form`
- `landing_page_url`
- `conversion_url`
- `thank_you_url`
- `ip_hash` quando aplicável
- `user_agent` quando aplicável
- `name`
- `email`
- `phone`
- `company`
- `role`
- `segment`
- `message`
- `consent_lgpd`
- `raw_payload`

### Aba 02_ATTRIBUTION

Origem e IDs.

Colunas:

- `lead_id`
- `raw_row_id`
- `client_id`
- `first_utm_source`
- `first_utm_medium`
- `first_utm_campaign`
- `first_utm_content`
- `first_utm_term`
- `first_landing_page_url`
- `first_seen_at`
- `last_utm_source`
- `last_utm_medium`
- `last_utm_campaign`
- `last_utm_content`
- `last_utm_term`
- `last_landing_page_url`
- `last_seen_at`
- `v4_campaign_id`
- `v4_adgroup_id`
- `v4_creative_id`
- `v4_test_id`

### Aba 03_PARSED_PARAMS

Campos já quebrados para análise.

Colunas:

- `lead_id`
- `campaign_id`
- `adgroup_id`
- `creative_id`
- `test_id`
- `objetivo`
- `tipo_campanha`
- `movimento`
- `campaign_slug`
- `cohort`
- `segmento`
- `periodo`
- `publico`
- `temperatura`
- `posicionamento`
- `adgroup_slug`
- `formato`
- `persona`
- `hook`
- `creative_slug`
- `dor`
- `angulo`
- `stage`
- `versao`
- `placement`
- `geo`
- `keyword`
- `match_type`

### Aba 04_CRM_MATCH

Resultado do cruzamento com CRM.

Colunas:

- `lead_id`
- `crm_contact_id`
- `crm_deal_id`
- `crm_owner`
- `crm_created_at`
- `lead_status`
- `mql_status`
- `mql_at`
- `sql_status`
- `sql_at`
- `opportunity_status`
- `opportunity_at`
- `deal_status`
- `won_at`
- `lost_at`
- `deal_value`
- `disqualification_reason`
- `lost_reason`
- `feedback_quality`
- `feedback_notes`
- `match_method`
- `match_confidence`

Valores para `match_method`:

```text
lead_id
email
phone
email_phone
crm_native
manual
no_match
```

Valores para `match_confidence`:

```text
high
medium
low
none
```

### Aba 05_MEDIA_EXPORT

Export da plataforma de mídia.

Colunas:

- `date`
- `source`
- `campaign_id`
- `campaign_name`
- `adgroup_id`
- `adgroup_name`
- `creative_id`
- `creative_name`
- `spend`
- `impressions`
- `clicks`
- `ctr`
- `cpc`
- `cpm`
- `platform_leads`
- `platform_conversions`

### Aba 06_ANALYTICS_READY

Tabela pronta para análise.

Grão recomendado:

```text
1 linha por lead_id
```

Colunas:

- `lead_id`
- `captured_at`
- `campaign_id`
- `adgroup_id`
- `creative_id`
- `test_id`
- `source`
- `medium`
- `cohort`
- `segmento`
- `tipo_campanha`
- `movimento`
- `publico`
- `temperatura`
- `posicionamento`
- `persona`
- `formato`
- `hook`
- `creative_slug`
- `dor`
- `angulo`
- `stage`
- `versao`
- `lead_status`
- `is_mql`
- `is_sql`
- `is_opportunity`
- `is_won`
- `deal_value`
- `disqualification_reason`
- `feedback_quality`
- `speed_to_lead_minutes`

### Aba 07_PIVOTS

Visões recomendadas:

- leads por campanha;
- MQL por campanha;
- CPMQL por campanha;
- MQL por criativo;
- MQL por formato;
- MQL por hook;
- MQL por persona;
- MQL por dor;
- MQL por ângulo;
- SQL por criativo;
- vendas por campanha;
- taxa de fonte desconhecida;
- leads sem match CRM;
- leads sem atendimento.

## 6. Dicionário de dados

Todo campo deve ter:

- nome;
- tipo;
- descrição;
- exemplo;
- obrigatório;
- fonte;
- regra de atualização.

Exemplo:

| Campo | Tipo | Fonte | Obrigatório | Regra |
|---|---|---|---|---|
| `lead_id` | string | backup/CRM | sim | único por lead |
| `first_utm_source` | string | cookie/form | sim | write-once |
| `last_utm_source` | string | cookie/form | sim | update on conversion |
| `creative_id` | string | UTM/content | sim | parseado ou informado |
| `is_mql` | boolean | CRM | sim | atualizado no match |

## 7. Como gerar o lead_id

Opções:

### Ideal

Gerar UUID no momento da conversão e enviar para:

- planilha backup;
- CRM;
- automação;
- thank you page;
- eventos.

### Aceitável na v1

Criar hash/dedup por:

```text
email_normalizado + telefone_normalizado + data
```

### Evitar

Usar só nome ou só telefone sem normalização.

## 8. Como retro-otimizar campanhas com a planilha

Processo:

1. Exportar mídia por campanha/conjunto/criativo.
2. Capturar leads na planilha backup.
3. Atualizar status CRM.
4. Cruzar por `lead_id`, email/telefone ou campos de origem.
5. Parsear UTMs e creative_id.
6. Agrupar por atributos.
7. Comparar lead barato vs lead qualificado.
8. Registrar decisão na planilha de testes.
9. Rebriefar próximo ciclo.

## 9. Perguntas que a base deve responder

- Qual campanha trouxe mais MQLs?
- Qual criativo trouxe MQLs mais baratos?
- Qual hook trouxe SQLs?
- Qual formato trouxe lead ruim?
- Qual persona avança mais?
- Qual dor gera conversa comercial melhor?
- Qual canal gera lead barato mas sem fit?
- Qual campanha tem problema de SLA?
- Qual percentual de leads está sem origem?
- Qual percentual de leads não deu match no CRM?

## 10. Critérios de qualidade de dados

### Bom

- `unknown_source_rate` menor que 10%;
- `crm_match_rate` maior que 90%;
- `creative_id_fill_rate` maior que 95%;
- `mql_feedback_rate` maior que 80%;
- `lead_id_duplicate_rate` baixo e monitorado.

### Alerta

- mais de 15% de origem desconhecida;
- leads sem `creative_id`;
- CRM sem motivo de desqualificação;
- muitos leads sem primeiro contato;
- planilha backup e CRM divergentes.

## 11. Critério N2

Contrato de dados está N2 quando:

- existe planilha backup padronizada;
- UTMs chegam na conversão;
- IDs chegam na planilha;
- CRM recebe origem ou existe match confiável;
- first-touch e last-touch são preservados;
- existe dicionário de dados;
- existe teste ponta a ponta;
- análise pós-campanha é possível.

## 12. Critério N3

Contrato de dados está N3 quando:

- dados são atualizados em cadência;
- debrief usa qualidade comercial;
- campanhas são otimizadas por MQL/SQL/venda;
- padrões de criativo são analisados;
- erros de dados viram ação corretiva;
- aprendizados alimentam DCC, plano de mídia e briefing.

## 13. Próximo estado ideal

V1:

- planilha backup padronizada;
- export manual de mídia;
- atualização manual/semi-manual de CRM;
- análise por planilha.

V2:

- sync automático mídia -> base;
- sync CRM -> base;
- dashboard;
- alertas de tracking quebrado;
- parsing automático de UTMs.

V3:

- MCP/API direto nas plataformas;
- agente analisando performance;
- sugestão de otimização;
- geração automática de debrief e rebrief.
