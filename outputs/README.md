# outputs — resultados obtidos

Esta pasta centraliza **artefatos gerados** pela operação (relatórios, exports de decks, PDFs consolidados, dumps estruturados, etc.). Não substitui o versionamento de skills em `executar/` ou `saber/`; é o lugar dos **entregáveis e outputs** produzidos nas execuções.

## Convenção por projeto

1. Crie uma subpasta por projeto ou linha de entrega: `outputs/<nome-ou-slug-do-projeto>/`.
2. Em **cada** subpasta de projeto, mantenha um **`README.md`** que documente:
   - o que a pasta contém (lista de artefatos);
   - datas ou versões relevantes;
   - referência às skills ou processos usados (caminhos em `executar/`, `saber/`, ou tarefas Paperclip), quando fizer sentido;
   - qualquer observação para quem for consumir o material depois.

Exemplo de layout:

```
outputs/
├── README.md                 ← você está aqui
└── exemplo-cliente/
    ├── README.md             ← índice e contexto deste projeto
    └── (arquivos gerados)
```

## Relação com `projects/`

- Trabalho ativo (código, planos, app) fica em **`projects/`** — ver `projects/README.md`.
- **Resultados** prontos ou exportados ficam em **`outputs/<projeto>/`**, com o `README.md` local correspondente.
