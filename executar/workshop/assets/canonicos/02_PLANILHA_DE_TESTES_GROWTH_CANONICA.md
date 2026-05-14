# Planilha Canônica de Testes de Growth
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + canônico original sem skill merge dedicada.  
**Decisão de merge:** sem skill dedicada; mantido como fonte de testes, hipóteses e aprendizado.


Status: v1 para workshop  
Escopo: rotina N3 de growth para campanhas de demanda qualificada  
Objetivo: definir uma planilha/base que permita registrar hipóteses, criativos, campanhas, leads, avanço no funil e decisões.

## 1. Princípio

A planilha de testes não é um relatório de mídia. Ela é o lugar onde o time transforma execução em aprendizado.

Ela precisa responder:

- o que testamos;
- por que testamos;
- qual variável mudou;
- quais variáveis ficaram constantes;
- qual criativo/campanha gerou lead;
- qual lead virou MQL/SQL/oportunidade/venda;
- qual padrão criativo ou canal parece funcionar;
- qual decisão será tomada no próximo ciclo.

## 2. Estrutura recomendada de abas

### Aba 00 - README

Função: explicar como usar a planilha.

Campos/conteúdo:

- cliente;
- cohort;
- segmento;
- período analisado;
- fonte dos dados;
- dono da planilha;
- cadência de atualização;
- link para DCC;
- link para plano de mídia;
- link para taxonomia UTM;
- glossário de status e métricas.

### Aba 01 - Testes

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

Valores sugeridos para `status_teste`:

```text
planejado
rodando
pausado
concluido
inconclusivo
cancelado
```

Valores sugeridos para `tipo_teste`:

```text
criativo
copy
oferta
publico
canal
lp
formulario
handoff
tracking
orcamento
```

Valores sugeridos para `alavanca`:

```text
formato
hook
dor
angulo
persona
prova
cta
lp
segmentacao
lance
evento
sla-vendas
```

Valores sugeridos para `decisao`:

```text
escalar
manter
ajustar
matar
replicar
criar-novo-teste
corrigir-tracking
revisar-oferta
acionar-vendas
inconclusivo
```

### Aba 02 - Criativos

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

Valores para `formato`:

```text
video
static
carousel
ugc
founder
demo
proof
lp
email
whatsapp
```

Valores para `tipo_video`:

```text
roteirizado
depoimento
demo
ugc
founder
motion
screen-record
antes-depois
```

### Aba 03 - Campanhas

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

### Aba 04 - Ad groups / conjuntos

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

### Aba 05 - Leads e funil

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

Valores para `lead_status`:

```text
novo
contatado
conectado
qualificado
desqualificado
oportunidade
venda
perdido
sem-resposta
duplicado
```

Valores para `feedback_quality`:

```text
otimo
bom
medio
ruim
invalido
sem-feedback
```

Valores para `disqualification_reason`:

```text
sem-fit
sem-budget
timing
nao-responde
fora-regiao
perfil-invalido
concorrente
duplicado
erro-contato
outro
```

### Aba 06 - Performance mídia

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

### Aba 07 - Performance funil

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

### Aba 08 - Aprendizados

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

## 3. Exemplo de linha de teste

```csv
test_id,client_id,tipo_teste,alavanca,hipotese,variavel_testada,variaveis_controladas,persona,canal,campaign_id,adgroup_id,creative_ids,metrica_primaria,meta_primaria,decisao
tst-hs-prevent-202605-004,cli-hs-prevent,criativo,hook,"Hooks de ROI para CFO geram MQL mais barato que hooks de medo","hook-roi vs hook-medo","mesmo canal, mesma LP, mesmo budget, mesmo publico frio",cfo,meta,cmp-hs-prevent-202605-001,adg-hs-prevent-202605-003,"crv-hs-prevent-202605-014;crv-hs-prevent-202605-015",cost_per_mql,300,rodando
```

## 4. Métricas que importam

Métricas de mídia:

- spend;
- impressões;
- CTR;
- CPC;
- CPM;
- LP views;
- connect rate;
- leads;
- CPL.

Métricas de qualidade:

- MQL;
- custo por MQL;
- SQL;
- custo por SQL;
- oportunidade;
- custo por oportunidade;
- venda;
- CAC;
- ROAS;
- velocidade de atendimento;
- taxa de lead inválido;
- taxa de fonte desconhecida.

Métricas por atributo criativo:

- MQL por formato;
- MQL por hook;
- MQL por dor;
- MQL por persona;
- MQL por ângulo;
- SQL por formato;
- venda por campanha/criativo;
- custo por MQL por padrão criativo.

## 5. Regra de leitura

Não matar criativo apenas por CPL.

A leitura correta considera:

- volume suficiente;
- custo por lead;
- qualidade do lead;
- avanço no funil;
- feedback comercial;
- etapa do funil;
- objetivo da campanha;
- tempo de aprendizado;
- consistência do tracking.

## 6. Como a IA deve usar a planilha

A IA deve conseguir:

- resumir os testes ativos;
- identificar criativos vencedores;
- agrupar performance por atributos;
- detectar tracking quebrado;
- detectar campanhas com lead barato e baixa qualidade;
- detectar criativos caros com boa qualidade;
- sugerir novos testes;
- gerar o debrief N3;
- gerar briefing do próximo ciclo.

## 7. Critério N2

A planilha está N2 quando:

- todo teste tem hipótese;
- todo criativo tem ID;
- toda campanha tem ID;
- todo lead tem origem;
- há pelo menos uma ligação entre campanha/criativo e lead;
- existe decisão registrada ao final do ciclo.

## 8. Critério N3

A planilha está N3 quando:

- decisões são tomadas a partir dela;
- aprendizados viram briefing do próximo ciclo;
- padrões são canonizados;
- erros de tracking são corrigidos;
- qualidade comercial entra na leitura.

## 9. O que evitar

Evitar:

- planilha que só replica métrica de plataforma;
- teste sem hipótese;
- criativo sem atributo;
- campanha sem objetivo claro;
- lead sem UTM;
- decisão sem aprendizado;
- otimização por CPL isolado;
- mudar várias variáveis ao mesmo tempo sem registrar.
