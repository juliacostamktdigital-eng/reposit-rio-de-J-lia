# QA Checklist - V4 Slides

## Pacote

- Artefato principal existe.
- `source/deck.json` ou `source/delivery.json` existe.
- `qa/qa-report.md` existe.
- `README.md` resume entrega, fontes e lacunas.
- `exports/deck.pptx` existe apenas quando solicitado.

## Formato

- Deck em 16:9.
- Slides sem mudanca acidental de tamanho.
- Margens consistentes.

## Design V4

- Fundo principal `#1A1814` quando aplicavel.
- Vermelho correto `#E50914`.
- Nao usa `#000000` como fundo principal.
- Nao usa `#E80403`.
- Nao usa azul/verde/teal como sistema de categorias.
- Logo no canto inferior direito.
- Tipografia segue Morganite/Morgane ou fallback; corpo segue IBM Plex Sans ou fallback.

## Narrativa

- Cada slide tem uma funcao.
- A abertura explicita a tese.
- O sumario orienta decisao, nao apenas lista assuntos.
- Diagnosticos levam a recomendacoes.
- Plano de acao fecha com dono, prazo e criterio.

## Evidencias

- Claims estao ligados ao mapa de evidencias.
- Numeros tem fonte e periodo.
- Hipoteses estao marcadas como hipoteses.
- Conflitos aparecem em lacunas ou decisao pendente.

## Navegabilidade e editabilidade

- HTML abre localmente ou via servidor sem quebrar assets.
- Slides mantem frame 16:9.
- Navegacao entre slides funciona quando houver interacao.
- Textos continuam selecionaveis/iteraveis no codigo.
- Quando houver PPTX, textos sao editaveis.
- Tabelas e shapes sao editaveis quando possivel.
- Imagens sao usadas apenas para logo, assets, screenshots ou visuais reais.

## Visual

- Sem texto cortado.
- Sem sobreposicao incoerente.
- Sem excesso de bullets.
- Sem tabela ilegivel.
- Sem logo distorcido.
- Sem densidade que exija zoom para leitura.
