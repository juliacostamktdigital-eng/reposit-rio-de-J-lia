---
name: biblioteca-angulos-hooks-copy
description: Cria biblioteca estratégica de ângulos, hooks, dores, desejos, objeções, provas e claims para campanhas de leadgen. Use ao transformar discovery, DEOC, DCC, benchmark, CRM e feedback comercial em hipóteses criativas, matriz de mensagens, utm_content e insumos para anúncios, LPs e roteiros.
---

# Biblioteca Ângulos Hooks Copy

## Quando Usar

Use antes de gerar anúncios, roteiros, LPs ou briefings criativos, quando o contexto ainda precisa virar uma biblioteca acionável de comunicação.

Situações típicas:

- existe DEOC/DCC/discovery, mas falta biblioteca de ângulos;
- o time precisa de hooks classificados;
- copy e mídia precisam testar hipóteses criativas;
- há objeções comerciais sem tradução para campanha;
- é preciso separar claims permitidos e proibidos;
- os atributos de copy precisam alimentar `utm_content`.

## Inputs Necessários

- discovery;
- DEOC ou DCC;
- UCM/planejamento estratégico, se existir;
- benchmark de concorrentes;
- CRM e feedback de vendas;
- histórico de campanhas;
- criativos e LPs anteriores;
- objeções reais;
- cases/provas;
- restrições jurídicas/compliance.

## Workflow

1. Extraia contexto estratégico:
   - produto/oferta;
   - persona;
   - inimigo/status quo;
   - problema priorizado;
   - proposta de valor;
   - provas disponíveis;
   - restrições.
2. Mapeie dores, desejos e objeções por persona.
3. Converta cada dor/objeção em ângulos de campanha.
4. Classifique hooks por tipo:
   - dor;
   - medo;
   - desejo;
   - ROI;
   - prova;
   - autoridade;
   - curiosidade;
   - comparação;
   - status;
   - urgência;
   - diagnóstico;
   - contraintuitivo;
   - "não parece anúncio".
5. Para cada ângulo, defina promessa, prova, objeção atacada, etapa de funil, formato recomendado e risco.
6. Separe claims permitidos, condicionais e proibidos.
7. Gere atributos para tracking:
   - `icp`;
   - `hook`;
   - `dor`;
   - `mot`;
   - `ang`;
   - `stage`;
   - `fmt`;
   - `ver`.
8. Marque hipóteses criativas prioritárias.

## Output Esperado

- biblioteca de ângulos;
- biblioteca de hooks;
- mapa de dores/desejos/objeções;
- claims permitidos/proibidos;
- hipóteses criativas;
- atributos para `utm_content`;
- riscos de comunicação.

Use `templates/biblioteca-angulos-hooks.md` para saída manual.
Use `templates/biblioteca-angulos-hooks.json` com o script para gerar Markdown/CSV.

## Script Utilitário

```bash
python3 scripts/build_copy_library.py templates/biblioteca-angulos-hooks.json --csv /tmp/hooks.csv --md /tmp/hooks.md
```

O script gera uma tabela normalizada para uso em plano de mídia, briefing criativo, UTM e leitura de performance.

## Definition Of Done

- Cada ângulo tem persona, dor, promessa, prova e risco.
- Cada hook tem tipo, origem estratégica e etapa de funil.
- Claims proibidos estão explícitos.
- Atributos para tracking foram preenchidos.
- A biblioteca consegue alimentar anúncios, LPs, roteiros e vendas.
- Não há promessa sem prova.

## Cuidados

- Não transformar benchmark em cópia de concorrente.
- Não aceitar persona genérica.
- Não criar hook bonito sem hipótese.
- Não criar claim absoluto sem comprovação.
- Não misturar dor, desejo, motivador e ângulo como se fossem a mesma coisa.
