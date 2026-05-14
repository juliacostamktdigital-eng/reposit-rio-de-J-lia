---
name: saber-claim-evidence-map
description: Use antes de montar decks Saber para mapear claims, recomendacoes, evidencias, fontes e lacunas, garantindo que nenhum slide final contenha afirmacao sem lastro.
---

# Saber Claim Evidence Map

## Quando usar

Use depois do intake e antes do schema de slides. Use tambem durante QA quando aparecer claim novo.

## Objetivo

Criar uma matriz de rastreabilidade entre:

- claim
- evidencia
- fonte/path
- dono da fonte
- slide destino
- status de risco

## Workflow

1. Leia os insumos aprovados.
2. Extraia claims, recomendacoes, metricas e diagnosticos.
3. Para cada claim, identifique a evidencia direta.
4. Marque o status:
   - `aprovado`: fonte clara e coerente
   - `fraco`: fonte existe, mas nao sustenta a frase inteira
   - `sem-fonte`: nao pode entrar no deck final
   - `conflitante`: precisa de decisao do CEO/Coordenador
5. Sugira o slide destino para cada claim.
6. Bloqueie ou reescreva claims `sem-fonte`.

## Regras

- Nao invente benchmark, numero ou causalidade.
- Nao transforme hipotese em fato.
- Nao esconda conflito entre especialistas.
- Quando a evidencia for qualitativa, escreva o claim como leitura, nao como certeza estatistica.
- Quando a fonte for externa, registre URL/data de acesso ou path local.

## Saida esperada

```markdown
## Claim Evidence Map

| Claim | Evidencia | Fonte | Dono | Slide | Status | Acao |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | aprovado/fraco/sem-fonte/conflitante | ... |
```

## Referencias

- Consulte `references/CLAIM-EVIDENCE-RULES.md` para padroes de escrita e bloqueio.
