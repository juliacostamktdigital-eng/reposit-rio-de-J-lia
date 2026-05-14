---
name: handoff-copy-para-vendas
description: Transforma promessa de campanha, dores, objeções, LP, anúncios e critérios MQL/SQL em handoff acionável para vendas. Use antes do go-live, ao alinhar SDR/comercial, quando houver nova campanha/LP/oferta ou quando leads chegam sem contexto de abordagem.
---

# Handoff Copy Para Vendas

## Quando Usar

Use para garantir que o time comercial saiba qual expectativa a campanha criou no lead e como abordar sem quebrar a promessa.

Situações típicas:

- nova campanha de leadgen vai ao ar;
- LP ou oferta mudou;
- vendedores não sabem por que o lead converteu;
- MQL/SQL está baixo apesar de leads qualificados;
- objeções comerciais precisam voltar para copy;
- SDR precisa de script inicial e perguntas de qualificação.

## Inputs Necessários

- DCC/DEOC;
- anúncios ativos;
- LP ou ponto de conversão;
- promessa da campanha;
- dores e objeções por persona;
- oferta e CTA;
- critérios MQL/SQL;
- motivos de desqualificação;
- feedback comercial;
- campos de tracking relevantes.

## Workflow

1. Resuma a promessa da campanha em linguagem comercial.
2. Declare a expectativa criada no lead:
   - o que ele acredita que receberá;
   - qual problema espera resolver;
   - qual objeção pode carregar;
   - qual prova ele viu antes de converter.
3. Liste dores, desejos e objeções por persona.
4. Crie perguntas de qualificação conectadas às dores.
5. Defina critérios MQL/SQL e motivos de desqualificação.
6. Escreva script de primeiro contato:
   - abertura contextual;
   - pergunta de diagnóstico;
   - aprofundamento;
   - ponte para oferta;
   - próximo passo.
7. Mapeie objeções esperadas com respostas seguras.
8. Registre sinais que vendas deve devolver para marketing:
   - objeção nova;
   - promessa desalinhada;
   - lead sem perfil;
   - dor recorrente;
   - claim confuso;
   - pergunta frequente.

## Output Esperado

- resumo para vendas;
- expectativa criada pela campanha;
- script inicial;
- perguntas de qualificação;
- objeções esperadas e respostas;
- critérios MQL/SQL;
- motivos de desqualificação;
- próximos passos recomendados;
- feedback loop para marketing.

Use `templates/handoff-copy-vendas.md` para entrega manual.
Use `templates/handoff-copy-vendas.json` com o script para gerar Markdown/CSV.

## Script Utilitário

```bash
python3 scripts/build_sales_handoff.py templates/handoff-copy-vendas.json --md /tmp/handoff-vendas.md --csv /tmp/handoff-vendas.csv
```

O script gera um handoff comercial estruturado por persona, dor, objeção, pergunta e resposta.

## Definition Of Done

- Vendas entende a promessa que trouxe o lead.
- Abordagem inicial referencia a campanha sem soar robótica.
- Critérios MQL/SQL estão explícitos.
- Objeções e respostas estão conectadas à copy.
- Motivos de desqualificação estão claros.
- Feedback comercial tem caminho de volta para marketing.

## Cuidados

- Não entregar só lista de anúncios.
- Não usar script genérico sem contexto da promessa.
- Não prometer no comercial algo que a campanha não sustentou.
- Não ignorar objeções reais.
- Não tratar todos os leads como se viessem do mesmo ângulo.
