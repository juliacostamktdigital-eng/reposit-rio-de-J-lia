# Referência Da Arquitetura De LP / Ponto De Conversão

Fonte normativa: `assets/canonicos/08_LP_PONTO_DE_CONVERSAO_CANONICO.md`.

## Princípio

A LP não é só uma página bonita. Ela é o contrato entre a promessa do criativo e o próximo passo comercial.

Uma LP N2 precisa:

- continuar a promessa do anúncio;
- qualificar o lead sem matar conversão;
- capturar UTMs e IDs;
- acionar o CRM e a planilha backup;
- permitir leitura de funil;
- entregar evidência de que está funcionando.

## Tipos De Ponto De Conversão

### Landing Page Própria

Usada quando há necessidade de explicar oferta, construir confiança e capturar dados com tracking completo.

### Formulário Nativo

Usado quando velocidade de conversão é prioridade, mas exige preservar campaign/ad/creative IDs.

### WhatsApp

Usado quando venda consultiva depende de conversa rápida. Precisa preservar origem no link, pré-mensagem ou middleware.

### Página De Agendamento

Usada quando o próximo passo é call. Precisa capturar origem e enviar contexto para CRM.

### Quiz/Diagnóstico

Usado quando qualificação é parte da experiência. Precisa guardar respostas como campos de lead.

## Estrutura Canônica

### Hero

Deve conter:

- headline;
- subheadline;
- promessa clara;
- CTA primário;
- indicação de para quem é;
- continuidade com o anúncio.

O usuário precisa entender em 5 segundos:

- onde chegou;
- o que ganha;
- por que deve continuar.

### Problema E Tensão

- dor principal;
- implicação prática;
- custo de não agir;
- conexão com persona.

### Solução / Mecanismo

- o que a empresa oferece;
- como funciona;
- por que é diferente;
- mecanismo de geração de resultado.

### Benefícios

Separar:

- racionais;
- emocionais;
- impacto financeiro;
- impacto operacional;
- impacto de risco.

### Provas

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

### Objeções / FAQ

Responder:

- preço;
- prazo;
- implementação;
- risco;
- suporte;
- integração;
- garantia;
- adequação ao perfil.

### Formulário

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

### CTA

Cada CTA deve definir:

- texto;
- destino;
- etapa do funil;
- evento;
- expectativa criada;
- próximo passo comercial.

## Tracking Obrigatório

A LP precisa:

- ler UTMs da URL;
- persistir UTMs em cookie/local storage ou equivalente;
- preencher campos ocultos;
- enviar campos para CRM e planilha backup;
- preservar first-touch;
- atualizar last-touch em nova conversão;
- gerar evento de conversão;
- permitir teste ponta a ponta.

## Eventos Recomendados

Mínimos:

- `page_view`;
- `lp_view`;
- `form_start`;
- `form_submit`;
- `lead_created`;
- `whatsapp_click`;
- `schedule_click`;
- `thank_you_view`.

Qualidade quando possível:

- `mql_created`;
- `sql_created`;
- `opportunity_created`;
- `deal_won`.

## Critério N2

LP está N2 quando:

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
