---
name: resumo-lead-para-vendas
description: Gera resumo comercial de um lead para vendas a partir de UTMs, campanha, criativo, promessa, LP, formulário, persona presumida, dor, ângulo e etapa do funil. Use quando um lead precisa chegar ao vendedor com contexto de abordagem, perguntas de qualificação, próximo passo e campos de feedback para marketing.
---

# Resumo Lead Para Vendas

## Quando Usar

Use quando um lead capturado por marketing precisa ser entregue para SDR/vendas sem perder a conversa que a campanha começou.

Situações típicas:

- lead novo no CRM;
- vendedor precisa entender origem e promessa;
- lead veio de criativo/LP específico;
- campanha tem persona/dor/ângulo rastreados;
- MQL precisa de contexto antes do primeiro contato;
- vendas deve devolver feedback padronizado para marketing.

## Inputs Necessários

- dados do lead;
- UTMs first/last-touch;
- `campaign_id`;
- `creative_id`;
- `test_id`;
- LP/página de conversão;
- formulário preenchido;
- promessa vista;
- CTA clicado;
- persona presumida;
- dor/ângulo;
- etapa do funil;
- oferta;
- critérios MQL/SQL.

## Workflow

1. Identifique origem:
   - canal;
   - campanha;
   - criativo;
   - teste;
   - LP/ponto de conversão.
2. Traduza tracking em contexto:
   - persona presumida;
   - hook;
   - dor/motivador;
   - ângulo;
   - etapa;
   - formato.
3. Resuma a promessa vista pelo lead.
4. Gere abordagem sugerida:
   - abertura contextual;
   - referência ao interesse demonstrado;
   - pergunta de qualificação;
   - exploração da dor;
   - conexão com promessa;
   - próximo passo.
5. Liste perguntas de qualificação.
6. Defina sinais positivos/negativos.
7. Inclua campos que vendas deve devolver:
   - `is_mql`;
   - `is_sql`;
   - `is_opportunity`;
   - `is_won`;
   - `disqualification_reason`;
   - `lead_quality`;
   - `speed_to_lead_minutes`;
   - `feedback_notes`.

## Output Esperado

- resumo do lead;
- contexto de campanha/criativo;
- promessa e expectativa;
- abordagem sugerida;
- perguntas de qualificação;
- próximos passos;
- checklist de feedback comercial;
- campos para planilha de testes.

Use `templates/resumo-lead-vendas.md` para entrega manual.
Use `templates/leads-contexto.json` com o script para gerar resumos em Markdown/CSV.

## Script Utilitário

```bash
python3 scripts/build_lead_sales_summary.py templates/leads-contexto.json --md /tmp/resumos-leads.md --csv /tmp/resumos-leads.csv
```

O script transforma uma lista de leads com contexto de origem em resumos comerciais.

## Definition Of Done

- Lead tem origem clara.
- Vendedor entende promessa, dor e CTA.
- Abordagem sugerida é específica.
- Perguntas de qualificação conectam dor e fit.
- Feedback de vendas está padronizado.
- Campos para planilha de testes estão presentes.

## Cuidados

- Não enviar lead sem contexto de campanha.
- Não tratar todos os leads como iguais.
- Não inventar persona quando tracking não sustenta.
- Não deixar feedback comercial em texto solto sem campos mínimos.
