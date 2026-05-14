# LP / Ponto de Conversão Canônico
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + `assets/legacy/merge/skills/09-briefing-pack-producao-criativos-e-conversao.md`.  
**Decisão de merge:** skill 09 dividida: ambiente de conversão incorporado aqui; briefing criativo incorporado no canônico 05.


Status: v1 para workshop  
Escopo: landing pages, formulários, WhatsApp, lead ads e qualquer ponto de conversão usado em leadgen  
Objetivo: definir o asset de conversão que recebe o tráfego, preserva contexto de campanha e transforma interesse em lead rastreável.

## 1. Princípio

A LP não é só uma página bonita. Ela é o contrato entre a promessa do criativo e o próximo passo comercial.

Uma LP N2 precisa:

- continuar a promessa do anúncio;
- qualificar o lead sem matar conversão;
- capturar UTMs e IDs;
- acionar o CRM e a planilha backup;
- permitir leitura de funil;
- entregar evidência de que está funcionando.

## 2. Tipos de ponto de conversão

### Landing page própria

Usada quando há necessidade de explicar oferta, construir confiança e capturar dados com tracking completo.

### Formulário nativo

Usado quando velocidade de conversão é prioridade, mas exige atenção para preservar campaign/ad/creative IDs.

### WhatsApp

Usado quando venda consultiva depende de conversa rápida. Precisa preservar origem no link, pré-mensagem ou middleware.

### Página de agendamento

Usada quando o próximo passo é call. Precisa capturar origem e enviar contexto para CRM.

### Quiz/diagnóstico

Usado quando qualificação é parte da experiência. Precisa guardar respostas como campos de lead.

## 3. Inputs obrigatórios

Antes de construir:

- planejamento estratégico/UCM;
- DEOC;
- plano de mídia;
- briefing criativo;
- taxonomia UTM;
- definição de MQL;
- campos CRM;
- oferta;
- prova;
- objeções;
- política/LGPD;
- assets visuais;
- restrições jurídicas.

Quando houver apresentação estratégica ou apresentação de produto, a LP deve extrair dela a ordem lógica das seções, os renders/imagens úteis, os argumentos de localização/prova e os CTAs planejados.

## 4. Estrutura canônica da LP

### 4.1 Hero

Deve conter:

- headline;
- subheadline;
- promessa clara;
- CTA primário;
- indicação de para quem é;
- continuidade com o anúncio.

O hero precisa herdar a tese do UCM:

- qual problema ou desejo abre a conversa;
- qual promessa central será sustentada;
- qual persona está sendo priorizada;
- qual ação o usuário deve tomar.

Critério:

O usuário precisa entender em 5 segundos:

- onde chegou;
- o que ganha;
- por que deve continuar.

### 4.2 Problema e tensão

Deve conter:

- dor principal;
- implicação prática;
- custo de não agir;
- conexão com a persona.

### 4.3 Solução / mecanismo

Deve conter:

- o que a empresa oferece;
- como funciona;
- por que é diferente;
- mecanismo de geração de resultado.

### 4.4 Benefícios

Separar:

- benefícios racionais;
- benefícios emocionais;
- impacto financeiro;
- impacto operacional;
- impacto de risco.

### 4.5 Provas

Podem incluir:

- cases;
- números;
- logos;
- depoimentos;
- certificações;
- prints;
- demonstração;
- autoridade técnica;
- base histórica.

### 4.6 Objeções / FAQ

Responder:

- preço;
- prazo;
- implementação;
- risco;
- suporte;
- integração;
- garantia;
- adequação ao perfil.

### 4.7 Formulário

Campos mínimos recomendados:

- nome;
- email;
- telefone;
- empresa;
- cargo;
- segmento;
- tamanho da empresa ou faturamento;
- principal desafio;
- consentimento LGPD.

Campos ocultos obrigatórios:

- `utm_source`;
- `utm_medium`;
- `utm_campaign`;
- `utm_content`;
- `utm_term`;
- `v4_client_id`;
- `v4_campaign_id`;
- `v4_adgroup_id`;
- `v4_creative_id`;
- `v4_test_id`;
- `landing_page_url`;
- `conversion_page_url`;
- `first_touch_*`;
- `last_touch_*`;
- timestamp.

### 4.8 CTA

Cada CTA deve definir:

- texto;
- destino;
- etapa do funil;
- evento;
- expectativa criada;
- próximo passo comercial.

### 4.9 Mapa de seções a partir de apresentações

Quando a LP nascer de apresentação estratégica, brandbook ou apresentação de empreendimento/produto, documentar seção por seção:

```text
Seção:
Objetivo:
Sobretítulo:
Título:
Subtítulo:
Descrição:
Bullets/ícones:
Asset visual de origem:
Slide de origem:
CTA:
Evento:
Observação de tracking:
```

Padrões extraídos dos exemplos:

- hero comunica o conceito e converte;
- seção de produto explica o que é e para quem é;
- seção de localização/contexto torna o valor concreto;
- seção de prova mostra números, certificações, base histórica, estrutura ou renders;
- seção de mecanismo explica como funciona;
- seção de benefícios traduz o mecanismo para ganhos práticos;
- seção de objeções reduz risco percebido;
- seção de tecnologia/serviços tangibiliza diferenciais;
- CTAs intermediários capturam intenção antes do fim da página;
- página de obrigado confirma o próximo passo comercial.

Esse mapa deve ser criado antes do design para evitar que informação relevante dos slides se perca na montagem visual.

## 5. Tracking obrigatório

A LP precisa:

- ler UTMs da URL;
- persistir UTMs em cookie/local storage ou equivalente;
- preencher campos ocultos;
- enviar campos para CRM e planilha backup;
- preservar first-touch;
- atualizar last-touch em nova conversão;
- gerar evento de conversão;
- permitir teste ponta a ponta.

## 6. Eventos recomendados

Eventos mínimos:

- `page_view`;
- `lp_view`;
- `form_start`;
- `form_submit`;
- `lead_created`;
- `whatsapp_click`;
- `schedule_click`;
- `thank_you_view`.

Eventos de qualidade quando possível:

- `mql_created`;
- `sql_created`;
- `opportunity_created`;
- `deal_won`.

## 6.1 Destino por hipótese e coerência de conversão

Para cada hipótese do Pack de Produção, declarar o destino mínimo viável: LP, formulário nativo, WhatsApp, agendamento ou diagnóstico/quiz. O destino precisa continuar a mesma promessa do anúncio e do DEOC. Se a promessa muda na página, o teste deixa de medir mídia/criativo e passa a medir desalinhamento.

Antes do go-live, validar velocidade, mobile, formulário, CTA, prova, fricção, evento, UTMs, planilha backup e CRM. Gaps que impedem leitura confiável entram no `06_ASSETS_ESQUECIDOS_E_BACKLOG_CANONICO.md`.

## 7. Checklist N2 da LP

A LP está N2 quando:

- headline está coerente com criativo;
- promessa está clara;
- CTA funciona;
- formulário funciona;
- campos ocultos capturam UTMs;
- evento está configurado;
- lead chega na fonte da verdade;
- CRM recebe origem;
- página é mobile-first;
- carregamento é aceitável;
- LGPD/política está ok;
- evidência de teste está registrada.

## 8. Checklist de QA

Antes do go-live:

- abrir URL com UTMs teste;
- validar se UTMs aparecem nos campos ocultos;
- preencher formulário;
- validar planilha backup;
- validar CRM;
- validar evento;
- validar thank you page;
- validar deduplicação;
- validar mobile;
- validar links e CTAs;
- validar copy contra claims proibidos.

## 9. Como a IA deve usar esse asset

A IA pode:

- revisar coerência anúncio -> LP;
- sugerir melhoria de headline;
- detectar falta de prova;
- detectar objeções sem resposta;
- comparar LP com DCC;
- gerar variações de seções;
- gerar checklist de QA;
- analisar performance por seção quando houver dados.

## 10. Critério N3

A LP está N3 quando:

- taxa de conversão é monitorada;
- qualidade do lead por LP é analisada;
- objeções comerciais retroalimentam a página;
- testes de headline/form/CTA são registrados;
- aprendizados viram versão nova documentada.

## 11. Saída esperada

Todo ponto de conversão deve gerar:

- lead rastreável;
- origem preservada;
- contexto comercial;
- evento mensurável;
- evidência para auditoria;
- dados para debrief.
