---
name: posicionamento-competitivo-beachhead
description: Consolida mapa competitivo 2x2, SWOT específica do cliente e scorecard de beachhead para decidir segmento inicial onde concentrar força antes do DEOC e da mídia. Use após benchmark e sizing, quando precisar decisão estratégica de eixos, diferenciação e primeiro recorte atacável.
---

# Posicionamento Competitivo Beachhead

## Quando Usar

Use quando benchmark e TAM/SAM/SOM já deram contexto, mas falta **decisão** de onde jogar primeiro e **como se posicionar** contra alternativas.

## Componentes

1. **Mapa 2x2:** dois eixos que revelam tradeoff real (ex.: generalista vs especialista; conveniência vs profundidade).
2. **SWOT específica:** itens só valem se não forem genéricos ao trocar o nome da empresa.
3. **Beachhead:** segmento com melhor combinação de urgência, pagamento, acesso, tamanho, espaço competitivo e alinhamento com forças do cliente.

## Regra SWOT

```text
Se trocar o nome da empresa e o item ainda servir para qualquer negócio do setor, está genérico demais.
```

Cada item: título, evidência, impacto, implicação estratégica.

## Scorecard Beachhead (playbook)

| Critério | Peso sugerido |
| --- | --- |
| Urgência da dor | Alta |
| Capacidade de pagar | Alta |
| Facilidade de acesso | Média |
| Tamanho do segmento | Média |
| Espaço / baixa densidade competitiva | Alta |
| Alinhamento com forças | Alta |

Pontue cada segmento de 1 a 5. **Maior é melhor** em todos os critérios; para competição use “atratividade por espaço de mercado” (5 = menos disputado / mais brecha).

## Inputs

- concorrentes e benchmark;
- TAM/SAM/SOM ou premissas de tamanho;
- forças reais do cliente;
- gaps exploráveis;
- segmentos candidatos (2 a 5).

## Workflow

1. Escolha eixos 2x2 que exponham decisão, não decoração.
2. Posicione cliente, concorrentes e alternativas indiretas.
3. Preencha SWOT com evidência e implicação.
4. Defina segmentos beachhead e pontue.
5. Escolha vencedor e declare o que **não** será atacado no ciclo 1.

## Output Esperado

- mapa 2x2 descrito;
- SWOT específica;
- scorecard e segmento recomendado;
- implicações para DEOC, oferta, canais e criativos.

Use `templates/beachhead-scorecard.md`.
Use `templates/posicionamento-beachhead.json` com o script para gerar relatório Markdown e CSV do scorecard.

## Script Utilitário

```bash
python3 scripts/score_beachhead.py templates/posicionamento-beachhead.json --md /tmp/beachhead.md --csv /tmp/beachhead-scores.csv
```

## Definition Of Done

- Eixos 2x2 sustentam escolha estratégica.
- SWOT não é genérica.
- Beachhead não é “todo o mercado”.
- Segmento recomendado tem pontuação e justificativa.
