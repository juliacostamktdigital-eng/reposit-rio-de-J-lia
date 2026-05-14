---
name: qa-criativo-hipotese-tracking
description: Revisa criativos antes de aprovação ou go-live para validar hipótese, persona, hook, promessa, prova, claims, LP/oferta, creative_id, utm_content e atributos analisáveis. Use em QA de peças finais, roteiros, carrosséis, anúncios, packs criativos ou quando houver risco de perder tracking, hipótese ou coerência de campanha.
---

# QA Criativo Hipótese Tracking

## Quando Usar

Use antes de aprovar peça criativa, subir campanha ou entregar pack final para mídia.

Situações típicas:

- criativo final precisa de go/no-go;
- roteiro ou design pode ter perdido a hipótese;
- peça tem claim sensível;
- `creative_id` ou `utm_content` está ausente;
- LP/oferta não bate com a promessa;
- carrossel repete slides sem progressão;
- pendência de asset, prova, aprovação, LP ou tracking precisa ir para backlog.

## Inputs Necessários

- brief criativo;
- roteiro/peça final;
- LP/ponto de conversão;
- taxonomia UTM;
- claims permitidos/proibidos;
- plano de mídia;
- DEOC/DCC ou biblioteca de ângulos;
- critério de leitura;
- assets e provas usadas.

## Workflow

1. Valide hipótese:
   - objetivo claro;
   - hipótese explícita;
   - variável testada identificável;
   - métrica de leitura definida.
2. Valide mensagem:
   - persona definida;
   - hook claro;
   - dor/desejo preservado;
   - promessa alinhada ao DEOC/DCC;
   - prova presente;
   - CTA coerente;
   - objeção atacada.
3. Valide claims:
   - permitidos;
   - condicionais com fonte/recorte;
   - proibidos removidos;
   - sem promessa absoluta sem base.
4. Valide produção:
   - formato compatível;
   - direção visual clara;
   - texto em tela legível;
   - asset/prova disponível;
   - peça é produzível/publicável.
5. Valide tracking:
   - `creative_id`;
   - formato;
   - persona;
   - hook;
   - dor/motivador;
   - ângulo;
   - etapa;
   - versão;
   - `utm_content`.
6. Valide coerência com LP/oferta:
   - promessa do anúncio aparece no destino;
   - CTA leva ao próximo passo correto;
   - formulário/evento mede o que a campanha promete;
   - expectativa criada será atendida.
7. Classifique decisão:
   - go;
   - go com pendência leve;
   - no-go até correção;
   - bloquear por tracking;
   - bloquear por claim;
   - bloquear por falta de prova/asset.
8. Empurre pendências para backlog `06` com dono, severidade e decisão.

## Output Esperado

- checklist de aprovação;
- decisão go/no-go;
- gaps por categoria;
- pendências priorizadas;
- risco de aprovação;
- changelog de correção;
- itens para backlog `06`.

Use `templates/checklist-qa-criativo.md` para revisão manual.
Use `templates/qa-criativo.json` com o script para gerar relatório e CSV de pendências.

## Script Utilitário

```bash
python3 scripts/qa_creative_pack.py templates/qa-criativo.json --md /tmp/qa-criativo.md --csv /tmp/pendencias-criativo.csv
```

O script classifica critérios como OK, pendência ou bloqueio e recomenda decisão.

## Definition Of Done

- Criativo aprovado somente se tem hipótese, persona, hook, CTA, prova, ID, atributos e critério de leitura.
- Claims proibidos não passam.
- Tracking incompleto bloqueia go-live.
- Coerência com LP/oferta foi verificada.
- Pendências não ficam escondidas no brief.
- Backlog `06` recebe itens com dono e severidade.
