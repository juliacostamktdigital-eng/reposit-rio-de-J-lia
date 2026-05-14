---
name: briefing-criativo-video-first
description: Cria briefing criativo video-first conectando DEOC/DCC, plano de mídia, hipótese, persona, mensagem, formato, direção visual, roteiro base, creative_id e utm_content. Use antes de produzir vídeos, UGC, founder, demo, motion, screen-record, estáticos ou carrosséis para campanhas de leadgen.
---

# Briefing Criativo Video-First

## Quando Usar

Use quando uma hipótese de campanha precisa virar peça criativa produzível, analisável e aprovada.

Situações típicas:

- transformar DEOC/DCC e plano de mídia em briefing;
- criar pack de produção criativa;
- alinhar copy, design, motion, captação e mídia;
- definir `creative_id` e `utm_content` antes da produção;
- garantir que cada criativo tenha hipótese e critério de leitura;
- registrar pendências de prova, asset, LP, aprovação ou tracking.

## Inputs Necessários

- planejamento estratégico/UCM;
- DEOC/DCC;
- plano de mídia;
- benchmark de segmento;
- catálogo **`banco-tipos-criativos`** (receita / `tipo_id`, quando o projeto já versiona tipos);
- **`selecao-pack-criativo-ciclo`** quando o trabalho vier de um pack (prioridade, qtd por tipo, critério de leitura);
- hipótese de teste;
- persona/ICP;
- etapa do funil;
- formato desejado;
- restrições de marca;
- claims permitidos/proibidos;
- aprendizados anteriores;
- taxonomia UTM/creative ID.

## Workflow

1. Defina identificação:
   - `brief_id`;
   - `test_id`;
   - `creative_id_previsto`;
   - cliente;
   - campanha;
   - conjunto/ad group;
   - responsável;
   - data;
   - status.
2. Declare objetivo e hipótese:
   - objetivo do criativo;
   - etapa do funil;
   - métrica primária;
   - métrica secundária;
   - evento esperado;
   - hipótese.
3. Descreva persona:
   - cargo/papel;
   - nível de consciência;
   - dor;
   - desejo;
   - objeção provável;
   - linguagem;
   - prova que convence.
4. Estruture mensagem:
   - hook;
   - dor/desejo;
   - ângulo;
   - promessa;
   - mecanismo;
   - prova;
   - CTA;
   - função no funil;
   - hipótese de aprendizado;
   - destino;
   - objeção atacada.
5. Defina formato e produção:
   - formato;
   - duração;
   - proporção;
   - canal/placement;
   - estilo visual;
   - captação/motion/narração/legenda;
   - direção visual;
   - textos em tela.
6. Crie roteiro base:
   - hook inicial;
   - contexto;
   - tensão;
   - mecanismo;
   - prova;
   - CTA.
7. Preencha tracking:
   - formato;
   - persona;
   - hook;
   - motivador;
   - dor;
   - ângulo;
   - etapa;
   - versão;
   - `utm_content` previsto.
8. Registre pendências e decisão de aprovação.

## Output Esperado

- brief criativo completo;
- roteiro base ou estrutura slide a slide;
- direção visual;
- textos em tela;
- copy/legenda do anúncio;
- `creative_id`;
- `utm_content` previsto;
- critério de aprovação;
- métrica de leitura;
- pendências para backlog.

Use `templates/brief-criativo.md` para entrega manual.
Use `templates/brief-criativo.json` com o script para gerar briefs e matriz CSV.

## Script Utilitário

```bash
python3 scripts/build_creative_brief.py templates/brief-criativo.json --md /tmp/briefs-criativos.md --csv /tmp/briefs-criativos.csv
```

O script gera um documento Markdown com os briefs e uma matriz CSV normalizada para controle de produção e tracking.

## Definition Of Done

- Cada criativo tem objetivo claro.
- Cada criativo tem hipótese.
- Persona, dor, hook, promessa, prova e CTA estão definidos.
- Claims e restrições foram considerados.
- `creative_id` e `utm_content` estão preenchidos.
- Brief é coerente com LP/oferta.
- Critério de leitura está explícito.
- Pendências não ficam escondidas.

## Cuidados

- Não inventar prova.
- Não criar promessa fora do DEOC/DCC.
- Não remover tracking.
- Não alterar persona sem registrar.
- Não criar variação sem ID.
- Não produzir peça sem hipótese de aprendizado.
