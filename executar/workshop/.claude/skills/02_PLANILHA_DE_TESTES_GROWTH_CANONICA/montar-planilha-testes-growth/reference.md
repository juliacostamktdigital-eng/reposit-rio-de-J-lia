# Referência Da Planilha De Testes Growth

Fonte normativa: `assets/canonicos/02_PLANILHA_DE_TESTES_GROWTH_CANONICA.md`.

## Princípio

A planilha de testes não é relatório de mídia. Ela é o lugar onde execução vira aprendizado.

Ela deve responder:

- o que testamos;
- por que testamos;
- qual variável mudou;
- quais variáveis ficaram constantes;
- qual criativo/campanha gerou lead;
- qual lead virou MQL, SQL, oportunidade ou venda;
- qual padrão criativo ou canal parece funcionar;
- qual decisão será tomada no próximo ciclo.

## Abas Obrigatórias

### `00_README`

Função: explicar como usar a planilha.

Campos:

- cliente;
- cohort;
- segmento;
- período analisado;
- fonte dos dados;
- dono da planilha;
- cadência de atualização;
- link para DEOC/DCC;
- link para plano de mídia;
- link para taxonomia UTM;
- glossário de status e métricas.

### `01_TESTES`

Função: registrar hipóteses e decisões.

Colunas:

- `test_id`
- `client_id`
- `periodo`
- `status_teste`
- `tipo_teste`
- `alavanca`
- `hipotese`
- `variavel_testada`
- `variaveis_controladas`
- `cohort`
- `segmento`
- `persona`
- `etapa_funil`
- `canal`
- `campanha_id`
- `adgroup_id`
- `creative_ids`
- `tipo_campanha`
- `movimento`
- `publico`
- `temperatura`
- `posicionamento`
- `metrica_primaria`
- `metrica_secundaria`
- `meta_primaria`
- `meta_secundaria`
- `data_inicio`
- `data_fim_prevista`
- `data_fim_real`
- `resultado_resumo`
- `decisao`
- `aprendizado`
- `proximo_passo`
- `dono`

Valores recomendados:

- `status_teste`: `planejado`, `rodando`, `pausado`, `concluido`, `inconclusivo`, `cancelado`;
- `tipo_teste`: `criativo`, `copy`, `oferta`, `publico`, `canal`, `lp`, `formulario`, `handoff`, `tracking`, `orcamento`;
- `alavanca`: `formato`, `hook`, `dor`, `angulo`, `persona`, `prova`, `cta`, `lp`, `segmentacao`, `lance`, `evento`, `sla-vendas`;
- `decisao`: `escalar`, `manter`, `ajustar`, `matar`, `replicar`, `criar-novo-teste`, `corrigir-tracking`, `revisar-oferta`, `acionar-vendas`, `inconclusivo`.

### `02_CRIATIVOS`

Função: listar cada criativo com atributos analisáveis.

Colunas:

- `creative_id`
- `test_id`
- `campaign_id`
- `adgroup_id`
- `nome_plataforma`
- `formato`
- `tipo_video`
- `persona`
- `hook`
- `creative_slug`
- `dor`
- `desejo`
- `angulo`
- `nivel_consciencia`
- `etapa_funil`
- `cta`
- `promessa`
- `prova_usada`
- `objecao_atacada`
- `duracao_video`
- `asset_url`
- `thumb_url`
- `copy_url`
- `status_aprovacao`
- `data_publicacao`
- `versao`

### `03_CAMPANHAS`

Função: registrar estrutura de mídia e metas.

Colunas:

- `campaign_id`
- `nome_campanha`
- `canal`
- `tipo_campanha`
- `objetivo`
- `movimento`
- `campaign_slug`
- `cohort`
- `segmento`
- `periodo`
- `orcamento_planejado`
- `orcamento_realizado`
- `evento_otimizacao`
- `meta_cpl`
- `meta_cpmql`
- `meta_sql`
- `meta_venda`
- `data_inicio`
- `data_fim`
- `status`
- `link_plataforma`

### `04_ADGROUPS`

Função: registrar audiência, público ou keyword.

Colunas:

- `adgroup_id`
- `campaign_id`
- `nome_adgroup`
- `canal`
- `publico`
- `temperatura`
- `posicionamento`
- `adgroup_slug`
- `persona`
- `segmentacao`
- `geo`
- `placement`
- `keyword`
- `match_type`
- `etapa_funil`
- `orcamento`
- `status`

### `05_LEADS_FUNIL`

Função: ser a base de match entre marketing e vendas.

Colunas:

- `lead_id`
- `created_at`
- `client_id`
- `test_id`
- `campaign_id`
- `adgroup_id`
- `creative_id`
- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_content`
- `utm_term`
- `nome`
- `email`
- `telefone`
- `empresa`
- `cargo`
- `lead_status`
- `is_mql`
- `mql_at`
- `is_sql`
- `sql_at`
- `is_opportunity`
- `opportunity_at`
- `is_won`
- `won_at`
- `deal_value`
- `disqualification_reason`
- `sales_owner`
- `first_contact_at`
- `speed_to_lead_minutes`
- `feedback_quality`
- `feedback_notes`

### `06_PERFORMANCE_MIDIA`

Função: consolidar dados de plataforma.

Colunas:

- `date`
- `campaign_id`
- `adgroup_id`
- `creative_id`
- `canal`
- `spend`
- `impressions`
- `reach`
- `frequency`
- `clicks`
- `ctr`
- `cpc`
- `cpm`
- `lp_views`
- `connect_rate`
- `leads`
- `cpl`
- `platform_conversions`
- `cost_per_platform_conversion`

### `07_PERFORMANCE_FUNIL`

Função: consolidar qualidade real por etapa.

Colunas:

- `campaign_id`
- `adgroup_id`
- `creative_id`
- `test_id`
- `leads`
- `mqls`
- `sqls`
- `opportunities`
- `sales`
- `revenue`
- `lead_to_mql_rate`
- `mql_to_sql_rate`
- `sql_to_opp_rate`
- `opp_to_sale_rate`
- `cost_per_mql`
- `cost_per_sql`
- `cost_per_opp`
- `cac`
- `roas`
- `avg_speed_to_lead_minutes`
- `unknown_source_rate`

### `08_APRENDIZADOS`

Função: transformar resultado em conhecimento.

Colunas:

- `learning_id`
- `test_id`
- `client_id`
- `cohort`
- `segmento`
- `padrao_observado`
- `evidencia`
- `limite_da_conclusao`
- `recomendacao`
- `vira_playbook`
- `vira_antipadrao`
- `vira_novo_teste`
- `data`
- `dono`

## Critério N2

A planilha está N2 quando:

- todo teste tem hipótese;
- todo criativo tem ID;
- toda campanha tem ID;
- todo lead tem origem;
- há pelo menos uma ligação entre campanha/criativo e lead;
- existe decisão registrada ao final do ciclo.

## Critério N3

A planilha está N3 quando:

- decisões são tomadas a partir dela;
- aprendizados viram briefing do próximo ciclo;
- padrões são canonizados;
- erros de tracking são corrigidos;
- qualidade comercial entra na leitura.

## O Que Evitar

- planilha que só replica métrica de plataforma;
- teste sem hipótese;
- criativo sem atributo;
- campanha sem objetivo claro;
- lead sem UTM;
- decisão sem aprendizado;
- otimização por CPL isolado;
- mudar várias variáveis ao mesmo tempo sem registrar.
