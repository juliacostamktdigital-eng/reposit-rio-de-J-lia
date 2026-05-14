# Executar — processo V4 Colli (entrega / assessoria)

Pasta que concentra o modelo operacional **Executar**: hierarquia Gerente → Coordenador → Gestor de Projeto → equipe, skills compartilhadas e documentação de sistema.

É o mesmo processo referenciado pelo BPMN de handoff, quinzenas, check-ins e aprovações documentado em `executar/_meta/agents.md`.

## Conteúdo

| Subpasta | Função |
|----------|--------|
| `executar/_meta/` | Taxonomia, versionamento, mapa de agentes e fluxos |
| `executar/shared/` | Skills usadas por vários agentes deste processo; padrão de ficheiros e PR por skill em [`shared/README.md`](shared/README.md) |
| `executar/agents/` | Um diretório por agente + skills proprietárias |

## Relação com o resto do repositório

- **`saber/`** — processo SABER (Paperclip / OPS); organograma e skills **separados**.
- **Raiz** — apenas `README.md`, BPMNs de referência (CSV) e pastas de processo (`executar/`, `saber/`).
