# Plano de Mídia Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/03-plano-midia-estrategia-canais-campanhas.md`.  
**Decisão de merge:** skill 03 incorporada ao canônico 03 mantendo cenários, fórmulas, colunas, N2/N3 e guardrails do playbook original.


Status: v1 para workshop  
Escopo: campanhas de geração de demanda qualificada  
Objetivo: padronizar como construir plano de mídia para que investimento, metas, canais e hipóteses sejam auditáveis e conectados ao funil.

## 1. Princípio

O plano de mídia não é apenas uma divisão de verba por canal. Ele é a tese financeira-operacional de como a campanha pretende gerar demanda qualificada.

Ele precisa responder:

- quanto vamos investir;
- em quais canais;
- com qual objetivo;
- com quais metas de funil;
- com quais premissas;
- quais cenários são esperados;
- quais sinais indicam que a campanha está saudável;
- quando a leitura deve ser feita;
- que decisão será tomada se a meta não for atingida.

## 2. Inputs obrigatórios

Antes de montar o plano, reunir:

- contrato/escopo;
- objetivo do cliente;
- ticket médio ou valor por venda;
- meta de vendas ou oportunidades;
- orçamento disponível;
- período de trabalho;
- cohort;
- segmento;
- funil de venda;
- histórico de mídia;
- histórico comercial;
- benchmark de segmento;
- capacidade comercial do cliente;
- SLA de atendimento;
- DEOC;
- legados UCM/DCC apenas quando o DEOC ainda não estiver consolidado;
- restrições legais ou comerciais;
- baseline histórico por canal, quando existir;
- definição de lead correto e qualidade mínima esperada.

## 3. Estrutura do documento

### 3.1 Resumo executivo

Deve conter:

- cliente;
- período do plano;
- objetivo principal;
- budget total;
- meta principal;
- canal principal;
- premissa central;
- maior risco;
- critério de sucesso.

Exemplo:

```text
Cliente: HS Prevent
Período: maio-julho/2026
Objetivo: gerar demanda qualificada para Onboarding Digital
Budget: R$ 60.000
Meta principal: 220 MQLs
Premissa central: CFOs e Heads de Produto respondem melhor a criativos sobre risco financeiro e conversão segura
Maior risco: CRM não preservar origem e qualidade do lead
Critério de sucesso: CPMQL dentro da meta e avanço consistente para SQL
```

### 3.2 Premissas comerciais

Campos:

- total de unidades ou volume disponível;
- VGV/receita total endereçável quando aplicável;
- ticket médio;
- metragem média e valor por m² quando for imobiliário;
- margem ou valor esperado;
- percentual de vendas esperado por origem/canal;
- taxa de conversão lead -> MQL;
- taxa de conversão MQL -> SQL;
- taxa de conversão SQL -> oportunidade;
- taxa de conversão oportunidade -> venda;
- capacidade de atendimento;
- tempo máximo de atendimento;
- ciclo médio de venda;
- valor esperado por venda;
- meta de receita ou VGV quando aplicável.

Nos planos reais de mídia imobiliária, a primeira camada não começa no canal, mas no potencial comercial:

```text
unidades disponíveis -> ticket/VGV -> % de vendas por origem -> vendas atribuíveis ao digital -> leads necessários -> investimento
```

Isso evita definir verba sem saber qual fatia do resultado a mídia deve carregar.

### 3.3 Cenários

Criar pelo menos três cenários:

- pessimista;
- provável;
- otimista.

Para cada cenário, definir:

- CPL;
- número de leads;
- taxa lead -> MQL;
- número de MQLs;
- custo por MQL;
- taxa MQL -> SQL;
- número de SQLs;
- custo por SQL;
- taxa SQL -> oportunidade;
- número de oportunidades;
- taxa de venda;
- vendas previstas;
- CAC;
- ROAS/receita prevista.

### 3.4 Distribuição por canal

Para cada canal, definir:

- canal;
- objetivo;
- etapa do funil;
- investimento total;
- investimento mensal;
- percentual do budget;
- CPL esperado;
- leads esperados;
- MQLs esperados;
- CPMQL esperado;
- papel do canal;
- risco do canal;
- critério de canal viável: aderência ao ICP/ticket, probabilidade de retorno e qualidade esperada do lead;
- critério de corte ou revisão.

Padrões observados nos planos CSV:

- separar captação, branding, remarketing, CRM, WhatsApp/automações e offline;
- declarar `% Invest` e `% Leads`, porque canal com pouco investimento pode ter papel estratégico sem grande volume;
- distinguir canal pago de canais que geram venda sem verba direta, como corretores, relacionamento, portais e offline;
- manter CPL previsto mesmo quando o papel do canal é awareness ou remarketing;
- explicitar ROAS/CAC por canal, não só no total.

Canais possíveis:

- Meta Ads;
- Google Search;
- Google Display;
- YouTube;
- LinkedIn;
- TikTok;
- Email/CRM;
- WhatsApp;
- remarketing;
- offline;
- parceiros;
- portais.

### 3.5 Estrutura de campanhas

Para cada campanha, definir:

- `campaign_id`;
- nome da campanha;
- canal;
- objetivo;
- cohort;
- segmento;
- etapa do funil;
- orçamento;
- evento de otimização;
- público;
- oferta;
- LP/ponto de conversão;
- criativos previstos;
- hipótese;
- público e exclusões derivados do ICP/anti-ICP;
- ângulo/mensagem derivados do DEOC;
- oferta e CTA;
- métrica de sucesso;
- janela de decisão;
- meta de leitura;
- período mínimo de teste.

Exemplo:

```text
campaign_id: cmp-hs-prevent-202605-001
canal: Meta Ads
objetivo: leadgen
etapa: tofu
orçamento: R$ 18.000
evento: lead
público: CFO/CEO fintech e instituições financeiras
oferta: diagnóstico de risco no onboarding digital
criativos: 6 vídeos + 3 estáticos de prova
hipótese: hooks de ROI e risco financeiro geram MQLs mais qualificados para CFO
meta: CPMQL <= R$ 300
período mínimo: 14 dias ou volume mínimo de 30 MQLs
```

### 3.6 Estrutura de criativos planejados

Para cada leva criativa, definir:

- quantidade;
- formato;
- persona;
- etapa de funil;
- hook;
- dor/desejo;
- ângulo;
- CTA;
- prova usada;
- status de produção;
- ID previsto.

Exemplo:

```text
Leva 01
Quantidade: 8 criativos
Formatos: 5 vídeos, 2 estáticos, 1 carrossel
Personas: CFO, Head de Produto, CTO
Hooks: ROI, fraude invisível, fricção no onboarding
Ângulos: risco financeiro, segurança sem fricção, autoridade técnica
CTA: solicitar diagnóstico
```

### 3.7 Plano de tracking

O plano de mídia precisa referenciar:

- taxonomia UTM;
- campaign IDs;
- adgroup IDs;
- creative IDs;
- test IDs;
- fonte da verdade;
- campos CRM;
- lead source;
- first-touch/last-touch;
- teste de tracking antes do go-live.

Sem isso, o plano não está N2. A instrumentação mínima deve existir antes do go-live: evento principal, UTMs/IDs, destino, fonte da verdade, CRM/backup e critério de qualidade do lead.

### 3.8 Ritmo de leitura

Definir:

- leitura diária: problemas graves, gasto, reprovação, tracking quebrado;
- leitura semanal: ritmo de geração, CPL, lead quality inicial;
- leitura quinzenal: MQL/SQL, padrões criativos, decisões de otimização;
- leitura mensal: aprendizado, revisão de plano e rebrief.

### 3.9 Cronograma de investimento

Quando o plano atravessar várias semanas ou meses, criar um cronograma de investimento.

Campos:

- período;
- escala/fator de aceleração;
- investimento por canal no período;
- investimento total do período;
- meta de leads do período;
- meta de MQL/SQL/vendas;
- receita prevista;
- observação de sazonalidade.

Uso:

- planejar ramp-up;
- reduzir verba em semanas de baixa intenção;
- acelerar perto de janelas comerciais;
- comparar previsto vs realizado por lote/semana;
- evitar gastar budget de forma linear quando o ciclo de venda não é linear.

### 3.10 Previsto vs realizado

Planos mais maduros precisam reservar colunas de realizado ao lado das metas.

Campos recomendados:

- investimento previsto;
- investimento realizado;
- impressões previstas;
- impressões realizadas;
- cliques previstos;
- cliques realizados;
- LP views previstas;
- LP views realizadas;
- leads/compras previstas;
- leads/compras realizadas;
- receita prevista;
- receita realizada;
- ROAS previsto;
- ROAS realizado.

Esse formato transforma o plano em instrumento de gestão, não só em orçamento inicial.

### 3.11 Plano por lote ou janela comercial

Quando a campanha tiver lotes, turmas, viradas de preço, pré-lançamento ou lançamento, modelar cada janela separadamente.

Cada lote deve conter:

- investimento;
- meta de vendas/compras;
- ROAS alvo;
- CPM previsto;
- impressões;
- CTR;
- cliques;
- connect rate;
- LP views;
- taxa LP -> próximo evento;
- custo por evento intermediário;
- taxa evento -> compra/venda;
- custo por compra/venda;
- ticket médio;
- faturamento previsto.

Esse padrão apareceu no plano de evento, em que cada lote tinha investimento, meta de venda, CPM, CTR, CPC, LP view, checkout, compra, ticket e faturamento.

## 4. Fórmulas base

### Leads esperados

```text
leads = investimento / CPL
```

### MQLs esperados

```text
MQLs = leads * taxa_lead_para_mql
```

### Custo por MQL

```text
CPMQL = investimento / MQLs
```

### SQLs esperados

```text
SQLs = MQLs * taxa_mql_para_sql
```

### Custo por SQL

```text
CPSQL = investimento / SQLs
```

### Vendas esperadas

```text
vendas = SQLs * taxa_sql_para_venda
```

### Receita prevista

```text
receita = vendas * ticket_medio
```

### ROAS

```text
ROAS = receita / investimento
```

### CAC

```text
CAC = investimento / vendas
```

### Impressões

```text
impressoes = investimento / CPM * 1000
```

### Cliques

```text
cliques = impressoes * CTR
```

### LP views

```text
lp_views = cliques * connect_rate
```

### Custo por LP view

```text
custo_lp_view = investimento / lp_views
```

### Evento intermediário

```text
eventos_intermediarios = lp_views * taxa_lp_para_evento
```

Exemplos de eventos intermediários:

- initiate checkout;
- form start;
- lead;
- WhatsApp click;
- agendamento;
- diagnóstico iniciado.

### Custo por evento intermediário

```text
custo_evento = investimento / eventos_intermediarios
```

## 5. Colunas recomendadas para planilha de plano de mídia

Identificação:

- `client_id`
- `plano_id`
- `periodo`
- `cohort`
- `segmento`
- `responsavel`

Premissas:

- `budget_total`
- `ticket_medio`
- `meta_vendas`
- `meta_receita`
- `ciclo_venda_dias`
- `capacidade_atendimento`

Funil:

- `taxa_lead_mql`
- `taxa_mql_sql`
- `taxa_sql_opp`
- `taxa_opp_venda`

Canais:

- `canal`
- `objetivo`
- `etapa_funil`
- `investimento`
- `investimento_mes`
- `percentual_budget`
- `cpl_previsto`
- `leads_previstos`
- `mqls_previstos`
- `cpmql_previsto`
- `sqls_previstos`
- `cpsql_previsto`
- `vendas_previstas`
- `cac_previsto`
- `roas_previsto`

Cronograma:

- `periodo`
- `semana`
- `lote`
- `fator_escala`
- `investimento_previsto_periodo`
- `investimento_realizado_periodo`
- `leads_previstos_periodo`
- `mqls_previstos_periodo`
- `sqls_previstos_periodo`
- `vendas_previstas_periodo`
- `receita_prevista_periodo`

Mídia intermediária:

- `cpm_previsto`
- `impressoes_previstas`
- `ctr_previsto`
- `cliques_previstos`
- `cpc_previsto`
- `connect_rate_previsto`
- `lp_views_previstas`
- `custo_lp_view_previsto`
- `taxa_lp_evento`
- `evento_intermediario`
- `eventos_intermediarios_previstos`
- `custo_evento_intermediario`

Controle:

- `cenario`
- `risco`
- `criterio_revisao`
- `status`
- `link_campanha`

## 6. Guardrails de decisão

O plano deve definir guardrails, não regras cegas.

Exemplos:

- Se CPL está acima da meta, mas CPMQL está saudável, não matar automaticamente.
- Se CPL está barato, mas MQL é baixo, revisar público, promessa ou formulário.
- Se lead é bom, mas SQL é baixo, investigar SLA/handoff comercial.
- Se campanha tem gasto e zero evento, checar tracking antes de mexer em criativo.
- Se criativo tem CTR alto e baixa conversão, revisar LP/oferta.
- Se criativo tem CTR baixo e MQL bom, testar variação de hook antes de matar.
- Se LP views caem muito abaixo dos cliques, investigar velocidade da página, tracking, pixel e experiência mobile.
- Se checkout/form_start existe, mas compra/lead cai, revisar formulário, oferta, fricção, preço ou expectativa criada.
- Se canal de branding não gera lead direto, avaliar contribuição por remarketing, busca de marca, tráfego direto e influência no funil.
- Se o realizado diverge do previsto por lote/semana, recalcular a projeção antes de prometer resultado acumulado.
- Toda mudança relevante de mix, budget, hipótese, público, criativo ou destino deve entrar em change log com motivo, métrica observada e próxima leitura esperada.
- Decisões antecipadas devem estar escritas: o que muda se CPL, CPMQL, qualidade de lead, taxa MQL->SQL ou tracking saírem da faixa.

## 7. Critério N2

Plano de mídia está N2 quando:

- tem premissas explícitas;
- conecta VGV/receita/ticket à meta de vendas;
- tem distribuição de verba por canal;
- separa canais pagos, orgânicos, offline, CRM, relacionamento e parceiros;
- tem metas por etapa do funil;
- tem hipóteses por campanha;
- tem cronograma quando o período não é curto;
- tem previsto vs realizado quando há execução em andamento;
- tem plano de tracking;
- tem cenários;
- tem critérios de leitura;
- está linkado ao DCC e à planilha de testes.

## 8. Critério N3

Plano de mídia está N3 quando:

- previsto vs realizado é revisado;
- as premissas são atualizadas com dados reais;
- guardrails são refinados;
- decisões por ciclo são registradas em change log;
- aprendizados alimentam o próximo plano;
- diferenças por cohort/segmento viram biblioteca.

## 9. Assets relacionados

Este documento depende de:

- DEOC;
- benchmark de segmento;
- plano de tracking/UTM;
- planilha de testes;
- CRM/handoff;
- dashboard de performance;
- debrief N3.
