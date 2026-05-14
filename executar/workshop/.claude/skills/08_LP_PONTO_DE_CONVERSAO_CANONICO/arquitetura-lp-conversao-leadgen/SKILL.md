---
name: arquitetura-lp-conversao-leadgen
description: Desenha arquitetura de LP, formulário, WhatsApp, agendamento ou quiz para leadgen, garantindo coerência com anúncio, DEOC, oferta, prova, objeções, MQL, campos CRM, LGPD, eventos e tracking. Use antes de design/dev de ponto de conversão ou quando precisar mapear seções, CTAs, formulário, campos ocultos e thank-you.
---

# Arquitetura LP Conversão Leadgen

## Quando Usar

Use quando a campanha precisa de um ponto de conversão que preserve promessa, qualifique o lead e gere dados rastreáveis.

Tipos de ponto de conversão:

- landing page própria;
- formulário nativo;
- WhatsApp;
- página de agendamento;
- quiz/diagnóstico.

## Inputs Necessários

- planejamento estratégico/UCM;
- DEOC/DCC;
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

## Workflow

1. Defina tipo de ponto de conversão e hipótese.
2. Garanta continuidade anúncio -> LP:
   - promessa;
   - persona;
   - dor;
   - ângulo;
   - CTA;
   - etapa do funil.
3. Desenhe estrutura canônica:
   - hero;
   - problema/tensão;
   - solução/mecanismo;
   - benefícios;
   - provas;
   - objeções/FAQ;
   - formulário;
   - CTAs;
   - thank-you.
4. Para cada seção, defina:
   - objetivo;
   - título;
   - subtítulo;
   - descrição;
   - bullets/ícones;
   - prova/asset visual;
   - CTA;
   - evento;
   - observação de tracking.
5. Defina formulário:
   - campos visíveis;
   - campos ocultos;
   - consentimento LGPD;
   - regra de qualificação;
   - fricção aceitável.
6. Defina tracking:
   - UTMs;
   - IDs `v4_*`;
   - first-touch;
   - last-touch;
   - CRM;
   - planilha backup;
   - eventos.
7. Defina página de obrigado e próximo passo comercial.

## Output Esperado

- mapa de seções;
- hero e promessa;
- CTAs;
- formulário;
- campos ocultos;
- eventos;
- página de obrigado;
- requisitos de CRM/backup;
- checklist N2.

Use `templates/mapa-lp.md` para entrega manual.
Use `templates/lp-arquitetura.json` com o script para gerar mapa Markdown/CSV.

## Script Utilitário

```bash
python3 scripts/build_lp_architecture.py templates/lp-arquitetura.json --md /tmp/mapa-lp.md --csv /tmp/mapa-lp.csv
```

O script transforma a arquitetura em matriz de seções e lista de campos/eventos.

## Definition Of Done

- Headline é coerente com criativo.
- Promessa está clara.
- CTA funciona e cria expectativa correta.
- Formulário qualifica sem matar conversão.
- Campos ocultos capturam UTMs/IDs.
- Evento está definido.
- CRM e backup recebem origem.
- LP é mobile-first.
- LGPD/política está ok.
- Teste ponta a ponta foi planejado.

## Cuidados

- Não mudar promessa entre anúncio e LP.
- Não criar formulário sem campos ocultos.
- Não fazer WhatsApp sem preservar origem.
- Não usar prova sem fonte.
- Não deixar CTA sem próximo passo comercial claro.
