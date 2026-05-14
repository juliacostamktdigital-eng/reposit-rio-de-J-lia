---
name: qa-lp-ponto-conversao
description: Valida LP, formulário, WhatsApp, agendamento ou quiz antes do go-live, checando promessa, mobile, carregamento, formulário, campos ocultos, UTMs, CRM, backup, eventos, thank-you, dedupe, LGPD e claims. Use em QA pré-publicação, lead teste, validação N2 ou quando gaps da LP precisam virar backlog.
---

# QA LP Ponto Conversão

## Quando Usar

Use antes do go-live ou após alteração relevante no ponto de conversão.

Situações típicas:

- nova LP vai ao ar;
- formulário mudou;
- campos ocultos foram adicionados;
- WhatsApp/agendamento precisa preservar origem;
- GTM/eventos foram configurados;
- CRM/backup precisa receber lead;
- promessa/claim foi alterado;
- mobile ou carregamento pode afetar conversão.

## Inputs Necessários

- URL com UTMs teste;
- LP/formulário/WhatsApp/agendamento/quiz;
- CRM;
- planilha backup;
- GTM/eventos;
- claims permitidos/proibidos;
- checklist N2;
- evidências do teste.

## Workflow

1. Abra URL com UTMs teste.
2. Valide coerência:
   - anúncio -> LP;
   - headline;
   - promessa;
   - CTA;
   - prova;
   - claims.
3. Valide UX:
   - mobile;
   - carregamento;
   - links;
   - CTAs;
   - formulário;
   - fricção.
4. Valide tracking:
   - UTMs lidas;
   - UTMs persistidas;
   - campos ocultos preenchidos;
   - first-touch preservado;
   - last-touch atualizado;
   - IDs `v4_*`.
5. Envie lead teste.
6. Valide destino:
   - planilha backup;
   - CRM;
   - eventos;
   - thank-you;
   - dedupe.
7. Classifique cada critério:
   - ok;
   - pendência;
   - bloqueio.
8. Gere decisão:
   - go;
   - go com pendência;
   - no-go;
   - bloquear tracking;
   - bloquear formulário;
   - bloquear claim.
9. Envie gaps que impedem leitura confiável para o backlog `06`.

## Output Esperado

- checklist de QA;
- evidências;
- gaps;
- decisão go/no-go;
- backlog de correções;
- recomendações por severidade.

Use `templates/checklist-qa-lp.md` para revisão manual.
Use `templates/qa-lp.json` com o script para gerar relatório e backlog.

## Script Utilitário

```bash
python3 scripts/qa_lp_conversion.py templates/qa-lp.json --md /tmp/qa-lp.md --csv /tmp/qa-lp-gaps.csv
```

O script classifica critérios, gera decisão e exporta gaps para backlog.

## Definition Of Done

- Promessa está coerente com criativo.
- CTA e formulário funcionam.
- Campos ocultos capturam UTMs/IDs.
- Evento está configurado.
- Lead chega na fonte da verdade.
- CRM recebe origem.
- Backup recebe lead.
- Mobile e carregamento estão aceitáveis.
- LGPD/política está ok.
- Evidência de teste está registrada.

## Cuidados

- Não aprovar LP sem lead teste.
- Não aprovar se CRM não recebe origem.
- Não aprovar se first-touch é sobrescrito.
- Não aprovar claim proibido.
- Não tratar evento configurado como suficiente sem validar lead criado.
