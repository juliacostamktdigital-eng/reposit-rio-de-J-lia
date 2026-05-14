# Assets Esquecidos e Backlog Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/09-briefing-pack-producao-criativos-e-conversao.md`.  
**Decisão de merge:** skill 09 referenciada como fonte de gaps operacionais; este canônico permanece transversal e não vira briefing paralelo.


Status: v1 para workshop  
Escopo: lacunas prováveis no processo AI-native de atendimento ponta a ponta  
Objetivo: listar assets que normalmente ficam fora quando o time pensa só em copy, mídia e criativo.

## 1. Leitura geral

Pelos exemplos na pasta `assets`, já existem bons materiais de:

- DEOC, agora tratado como legado dentro do DEOC;
- UCM, agora tratado como legado dentro do DEOC;
- plano de mídia;
- roteiros de captação;
- copies de LP;
- campanha de captação.

O que tende a faltar não é "mais copy". O que falta é a camada de sistema:

- handoff;
- diagnóstico;
- tracking;
- QA;
- CRM;
- SLA;
- planilha de testes;
- debrief;
- canonização;
- versionamento;
- automação.

Após revisar os exemplos de UCM, DCC, campanha e LP, a separação entre UCM e DCC deixou de ser a melhor nomenclatura operacional. Eles passam a ser tratados como partes de um asset único: `13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md`.

Após revisar o TO BE do processo SABER, o começo do EXECUTAR também passa a ter um handoff operacional próprio: `11_HANDOFF_OPERACIONAL_EXECUTAR_CANONICO.md`. Ele reaproveita a lógica inicial do SABER, mas com foco nos três insumos reais do EXECUTAR: plano de ROI, transcrição da call de vendas e transcrição da Growth Class.

Após revisar as skills canônicas do agente `analista-mercado-benchmark`, o EXECUTAR também passa a ter um benchmark próprio antes da construção dos assets: `12_BENCHMARK_MERCADO_TAM_SAM_SOM_CANONICO.md`. Ele incorpora sizing TAM/SAM/SOM, estudo de concorrentes e definição de beachhead.

## 2. Assets provavelmente esquecidos

### 2.1 Brief sales-to-ops

Por que importa:

Evita que a operação comece sem saber o que foi vendido, prometido e limitado.

Deve conter:

- promessa comercial;
- escopo;
- exclusões;
- stakeholders;
- critério de sucesso;
- riscos/red flags;
- histórico da venda;
- expectativas do cliente;
- prazo crítico;
- restrições contratuais.

### 2.2 Intake e questionário de discovery

Por que importa:

Sem discovery estruturado, DCC e plano de mídia dependem de interpretação solta.

Deve conter:

- negócio;
- oferta;
- ICP;
- diferenciais;
- concorrentes;
- histórico de marketing;
- histórico de vendas;
- objeções;
- acesso a materiais;
- stack comercial;
- stack de mídia/dados.

### 2.2.1 Dossiê Estratégico de Oferta e Comunicação

Por que importa:

É a ponte entre discovery, benchmark e execução. Sem esse asset, o time separa UCM de DCC, cria narrativa duplicada e pula direto para copy/mídia sem fonte única de oferta, público, alternativa, prova e claims permitidos.

Deve conter:

- contexto do negócio;
- objetivo da campanha;
- benchmark e beachhead;
- problemas priorizados;
- impacto e voz do cliente;
- personas e papéis de decisão;
- alternativas percebidas;
- frequência natural do problema;
- proposta de valor e mecanismo;
- inimigo/status quo;
- provas e autoridade;
- narrativa central;
- claims permitidos e proibidos;
- vocabulário de dor e prazer;
- tradução para LP, criativos, mídia e comercial.

Documento canônico: `13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md`.

### 2.2.2 Benchmark de mercado, concorrentes e TAM/SAM/SOM

Por que importa:

Sem benchmark, o pacote de assets é definido olhando apenas para dentro do cliente. O time precisa entender mercado, concorrência, ruídos, tamanho real de oportunidade e beachhead antes de escolher canal, ponto de conversão, narrativa e plano de mídia.

Deve conter:

- contexto de mercado;
- TAM;
- SAM;
- SOM calculado com capacidade e budget;
- concorrentes diretos, indiretos e substitutos;
- análise de Meta Ads Library;
- ruídos de mercado;
- mapa competitivo;
- SWOT específica;
- scorecard de beachhead;
- implicações para DEOC, mídia, LP e criativos.

Documento canônico: `12_BENCHMARK_MERCADO_TAM_SAM_SOM_CANONICO.md`.

### 2.3 Auditoria inicial de marketing

Por que importa:

Cria baseline antes da intervenção.

Deve conter:

- campanhas ativas;
- investimentos;
- CPL;
- MQL;
- criativos ativos;
- LPs;
- tracking;
- eventos;
- funil;
- top/bottom campanhas;
- top/bottom criativos;
- quick wins.

### 2.4 Auditoria comercial / CRM

Por que importa:

Resultado depende de demanda qualificada e conversão comercial.

Deve conter:

- CRM usado;
- etapas do funil;
- definição de lead/MQL/SQL;
- SLA de atendimento;
- speed-to-lead;
- taxa de contato;
- taxa de qualificação;
- motivos de perda;
- responsável comercial;
- campos obrigatórios;
- qualidade do follow-up.

### 2.5 Mapa de campos CRM

Por que importa:

Sem campos padronizados, UTM e lead source se perdem.

Deve conter:

- campos first-touch;
- campos last-touch;
- campos de campanha;
- campos de criativo;
- campos de funil;
- campos de qualidade;
- motivo de desqualificação;
- dono do lead;
- timestamps;
- regra de atualização.

### 2.6 SLA marketing-vendas

Por que importa:

Lead bom pode virar resultado ruim se vendas demora ou não entende o contexto.

Deve conter:

- o que é MQL;
- o que é SQL;
- tempo máximo de primeiro contato;
- número mínimo de tentativas;
- canal de contato;
- responsável;
- regra de roteamento;
- regra de retorno para nurture;
- motivo obrigatório de desqualificação;
- feedback para marketing.

### 2.7 Script de abordagem comercial

Por que importa:

O lead chega com promessa e contexto de campanha. Vendas precisa continuar a mesma conversa.

Deve conter:

- promessa que o lead viu;
- dor provável;
- pergunta de abertura;
- perguntas de qualificação;
- objeções esperadas;
- respostas recomendadas;
- critérios de avanço;
- próximo passo;
- mensagem WhatsApp/email.

### 2.8 Taxonomia UTM e IDs

Por que importa:

É o contrato que permite aprender quais padrões funcionam.

Deve conter:

- campaign ID;
- adgroup ID;
- creative ID;
- test ID;
- UTM source;
- UTM medium;
- UTM campaign;
- UTM content;
- UTM term;
- parâmetros customizados;
- campos parseados.

### 2.9 Protocolo de teste de tracking

Por que importa:

Tracking precisa ser provado antes do investimento rodar.

Deve conter:

- URL teste;
- formulário teste;
- validação de campos ocultos;
- validação no CRM;
- validação na planilha;
- validação de dedupe;
- validação de first/last touch;
- evidências.

### 2.10 Planilha de testes de growth

Por que importa:

Sem planilha de testes, a operação olha campanha, mas não aprende.

Deve conter:

- hipóteses;
- criativos;
- campanhas;
- leads;
- funil;
- performance mídia;
- performance comercial;
- decisões;
- aprendizados.

### 2.11 Template de debrief N3

Por que importa:

Relatório sem decisão não melhora o processo.

Deve conter:

- resultado vs meta;
- leitura de mídia;
- leitura de funil;
- leitura comercial;
- padrões vencedores;
- padrões perdedores;
- decisão;
- próxima hipótese;
- impacto no DCC/plano/briefing.

### 2.12 Registro de decisão

Por que importa:

Sem registro, o time esquece por que mudou a campanha.

Deve conter:

- data;
- decisão;
- dado usado;
- hipótese;
- responsável;
- impacto esperado;
- prazo de revisão;
- link da evidência.

### 2.13 Changelog do OS do cliente

Por que importa:

N3 é versionamento. Sem changelog, não dá para saber o que mudou.

Deve conter:

- versão;
- mudança;
- motivo;
- componente afetado;
- data;
- responsável;
- métrica esperada;
- resultado observado.

### 2.14 Biblioteca de padrões vencedores

Por que importa:

O aprendizado precisa sair da conta individual.

Deve conter:

- cohort;
- segmento;
- persona;
- padrão;
- contexto;
- evidência;
- limite da conclusão;
- recomendação;
- exemplo.

### 2.15 Biblioteca de anti-padrões

Por que importa:

Falhas recorrentes também são conhecimento.

Deve conter:

- padrão ruim;
- onde apareceu;
- por que falhou;
- dado/evidência;
- como evitar;
- exceções.

### 2.16 Rubrica N1/N2/N3 por componente

Por que importa:

Sem rubrica, auditoria vira opinião.

Deve conter:

- componente;
- definição N1;
- definição N2;
- definição N3;
- evidências;
- falso positivo;
- dono;
- frequência de revisão.

### 2.17 Checklist de QA de LP

Por que importa:

LP ruim pode destruir uma campanha boa.

Deve conter:

- promessa coerente com anúncio;
- headline clara;
- CTA claro;
- formulário funcionando;
- carregamento;
- mobile;
- tracking;
- prova;
- objeções;
- LGPD/política;
- evento configurado.

### 2.18 Checklist de QA de criativo

Por que importa:

Criativo sem hipótese não gera aprendizado.

Deve conter:

- persona;
- hook;
- dor/desejo;
- ângulo;
- CTA;
- ID;
- formato;
- versão;
- claim permitido;
- conexão com DCC;
- conexão com LP.

### 2.19 Matriz de acessos

Por que importa:

Sem acesso, o processo trava ou vira gambiarra.

Deve conter:

- Meta;
- Google Ads;
- Google Analytics;
- GTM;
- CRM;
- LP/CMS;
- planilhas;
- dashboard;
- domínio;
- WhatsApp;
- permissões;
- dono do acesso.

### 2.20 Plano de automação / AI-native

Por que importa:

Se a operação quer ser AI-native, precisa saber o que será manual, semi-automático ou automático.

Deve conter:

- etapa;
- tarefa;
- input;
- output;
- ferramenta;
- nível de automação;
- risco;
- dono;
- evidência;
- próximo passo técnico.

### 2.1 Gaps do Pack de Produção

Durante briefing, criativo, LP e go-live, registrar aqui qualquer ausência que impeça produção, conversão ou leitura confiável: prova/case inexistente, peça sem roteiro, LP sem QA, formulário sem CRM, tracking sem teste, divergência entre oferta/anúncio/destino/vendas ou restrição jurídica sobre claim.

Cada gap precisa ter dono, impacto, severidade, prazo e decisão: resolver antes do go-live, aceitar risco por ciclo, substituir hipótese ou retirar do pacote v1.

## 3. Prioridade de construção

### Prioridade 1 - Sem isso não há N2 confiável

- Brief sales-to-ops.
- Questionário discovery.
- Rubrica N1/N2/N3.
- Taxonomia UTM/IDs.
- Mapa CRM.
- Protocolo de tracking.
- Plano de mídia.
- Planejamento estratégico/UCM.
- DCC.
- Brief criativo.
- Checklist go-live.

### Prioridade 2 - Sem isso não há N3 bom

- Planilha de testes.
- Template de debrief.
- Feedback qualidade de lead.
- Backlog de hipóteses.
- Registro de decisão.
- Changelog.

### Prioridade 3 - Sem isso não escala

- Biblioteca de padrões.
- Biblioteca de anti-padrões.
- Packs por cohort.
- Skills operacionais.
- Plano de automação.
- Dashboard por squad/cohort.

## 4. Quais documentos canônicos já foram criados nesta pasta

- `00_MAPA_ASSETS_AI_NATIVE_PONTA_A_PONTA.md`
- `01_TAXONOMIA_UTM_IDS_E_SUBPARAMETROS.md`
- `02_PLANILHA_DE_TESTES_GROWTH_CANONICA.md`
- `03_PLANO_DE_MIDIA_CANONICO.md`
- `04_DOCUMENTO_COPY_FINAL_DCC_CANONICO.md`
- `05_BRIEFING_CRIATIVO_VIDEO_FIRST_CANONICO.md`
- `06_ASSETS_ESQUECIDOS_E_BACKLOG_CANONICO.md`
- `07_CRM_HANDOFF_SLA_MARKETING_VENDAS_CANONICO.md`
- `08_LP_PONTO_DE_CONVERSAO_CANONICO.md`
- `09_CONTRATO_DADOS_MKT_CRM_BACKUP_UTMS_CANONICO.md`
- `10_PLANEJAMENTO_ESTRATEGICO_UCM_CANONICO.md`
- `11_HANDOFF_OPERACIONAL_EXECUTAR_CANONICO.md`

## 5. Próximos documentos que ainda valeria criar

### 5.1 Handoff sales-to-ops canônico

Motivo:

É uma das maiores fontes de desalinhamento entre venda e execução.

### 5.2 Questionário de discovery canônico

Motivo:

Alimenta DEOC, plano de mídia, LP, criativos e riscos comerciais.

### 5.3 Mapa CRM + SLA marketing-vendas

Motivo:

Fecha a equação de resultado e evita culpar marketing por quebra comercial.

### 5.4 Checklist de QA de LP

Motivo:

LP é componente crítico de conversão e tracking.

### 5.5 Template de debrief N3

Motivo:

É o ritual que transforma resultado em decisão.

### 5.6 Registro de aprendizado canônico

Motivo:

É o que permite transformar casos individuais em biblioteca e skill.
