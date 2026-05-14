# Referência Do Plano De Mídia Leadgen

Fonte normativa: `assets/canonicos/03_PLANO_DE_MIDIA_CANONICO.md`.

## Princípio

Plano de mídia não é apenas divisão de verba por canal. É a tese financeira-operacional de como a campanha pretende gerar demanda qualificada.

Ele precisa responder:

- quanto vamos investir;
- em quais canais;
- com qual objetivo;
- com quais metas de funil;
- com quais premissas;
- quais cenários são esperados;
- quais sinais indicam saúde;
- quando a leitura deve ser feita;
- que decisão será tomada se a meta não for atingida.

## Estrutura Obrigatória

### Resumo Executivo

- cliente;
- período;
- objetivo principal;
- budget total;
- meta principal;
- canal principal;
- premissa central;
- maior risco;
- critério de sucesso.

### Premissas Comerciais

- total de unidades ou volume disponível;
- receita total endereçável quando aplicável;
- ticket médio;
- margem ou valor esperado;
- percentual de vendas esperado por origem/canal;
- taxa lead -> MQL;
- taxa MQL -> SQL;
- taxa SQL -> oportunidade;
- taxa oportunidade -> venda;
- capacidade de atendimento;
- tempo máximo de atendimento;
- ciclo médio de venda;
- valor esperado por venda;
- meta de receita.

## Distribuição Por Canal

Para cada canal:

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
- critério de canal viável;
- critério de corte ou revisão.

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

## Estrutura De Campanhas

Para cada campanha:

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
- público e exclusões;
- ângulo/mensagem;
- CTA;
- métrica de sucesso;
- janela de decisão;
- período mínimo de teste.

## Estrutura De Criativos Planejados

Para cada leva:

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

## Plano De Tracking

O plano precisa referenciar:

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

Sem isso, o plano não é N2.

## Ritmo De Leitura

- diária: problemas graves, gasto, reprovação, tracking quebrado;
- semanal: ritmo de geração, CPL, lead quality inicial;
- quinzenal: MQL/SQL, padrões criativos, decisões;
- mensal: aprendizado, revisão do plano e rebrief.

## Fórmulas Base

```text
leads = investimento / CPL
MQLs = leads * taxa_lead_para_mql
CPMQL = investimento / MQLs
SQLs = MQLs * taxa_mql_para_sql
CPSQL = investimento / SQLs
vendas = SQLs * taxa_sql_para_venda
receita = vendas * ticket_medio
ROAS = receita / investimento
CAC = investimento / vendas
impressoes = investimento / CPM * 1000
cliques = impressoes * CTR
lp_views = cliques * connect_rate
```

## Guardrails

- Se CPL está acima da meta, mas CPMQL está saudável, não matar automaticamente.
- Se CPL está barato, mas MQL é baixo, revisar público, promessa ou formulário.
- Se lead é bom, mas SQL é baixo, investigar SLA/handoff comercial.
- Se campanha tem gasto e zero evento, checar tracking antes de mexer em criativo.
- Se criativo tem CTR alto e baixa conversão, revisar LP/oferta.
- Se criativo tem CTR baixo e MQL bom, testar variação de hook antes de matar.
- Toda mudança relevante deve entrar em changelog.

## Critério N2

Plano está N2 quando:

- tem premissas explícitas;
- conecta receita/ticket à meta;
- tem distribuição por canal;
- separa canais pagos, orgânicos, offline, CRM e parceiros;
- tem metas por etapa;
- tem hipóteses por campanha;
- tem cronograma quando necessário;
- tem previsto vs realizado quando já em execução;
- tem tracking;
- tem cenários;
- tem critérios de leitura;
- está linkado ao DEOC e à planilha de testes.

## Critério N3

Plano está N3 quando:

- previsto vs realizado é revisado;
- premissas são atualizadas com dados reais;
- guardrails são refinados;
- decisões por ciclo entram em changelog;
- aprendizados alimentam o próximo plano;
- diferenças por cohort/segmento viram biblioteca.
