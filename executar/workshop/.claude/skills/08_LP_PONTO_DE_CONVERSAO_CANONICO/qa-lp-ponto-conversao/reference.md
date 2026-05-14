# Referência Do QA LP / Ponto De Conversão

Fonte normativa: `assets/canonicos/08_LP_PONTO_DE_CONVERSAO_CANONICO.md`.

## Princípio

Antes do go-live, validar velocidade, mobile, formulário, CTA, prova, fricção, evento, UTMs, planilha backup e CRM. Gaps que impedem leitura confiável entram no `06_ASSETS_ESQUECIDOS_E_BACKLOG_CANONICO.md`.

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

## Eventos Mínimos

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

## Checklist N2

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

## Checklist De QA Antes Do Go-Live

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

## Bloqueios

Bloquear go-live quando:

- formulário não envia;
- CRM não recebe lead;
- origem não chega no CRM;
- planilha backup não recebe lead;
- UTMs não são capturadas;
- first-touch é sobrescrito;
- evento principal não dispara;
- thank-you não funciona;
- claim proibido aparece;
- mobile impede conversão;
- LGPD/política ausente em contexto obrigatório.

## Decisões

- `go`: sem bloqueios e pendências controladas;
- `go_com_pendencia`: pendência leve com dono e prazo;
- `no_go`: correção necessária antes;
- `bloquear_tracking`: origem/eventos impedem leitura;
- `bloquear_formulario`: conversão não funciona;
- `bloquear_claim`: risco jurídico/compliance.
