---
name: contexto
description: Lê todos os arquivos de uma pasta de cliente, squad ou projeto e gera/atualiza CLAUDE.md, AGENTS.md e a pasta mission-control/ com OKRs, apostas, combinados, personas e histórico de check-ins.
user-invocable: true
---

# /contexto — Gerar memória do cliente/squad/projeto

Analisa Knowledge Base e gera arquivos de memória persistente para uso em todas as sessões futuras.

## Quando usar

- Analisar uma pasta de cliente, squad ou projeto
- Fazer o Claude "conhecer" um cliente
- Criar ou atualizar Mission Control de um cliente

## O que gera

### Para clientes

**`CLAUDE.md` + `AGENTS.md`** (mesmo conteúdo) com:
- Resumo do negócio
- Operações e processos
- Estratégia ativa
- Contatos principais

**`mission-control/`** com:
- `okr-quarter.md` — objetivos e resultados-chave do trimestre
- `apostas-vivas.md` — apostas estratégicas com critérios de sucesso testáveis
- `combinados.md` — compromissos pendentes, em andamento e concluídos
- `personas-call.md` — perfis de stakeholders e padrões de comunicação
- `historico-checkins.md` — histórico cronológico de check-ins

### Para squads

`CLAUDE.md` + `AGENTS.md` com membros, lista de clientes e processos

### Para projetos/áreas

`CLAUDE.md` + `AGENTS.md` com objetivos, dados, fluxos e situação atual

## Princípios

- Ler **tudo** na pasta — sem atalhos
- Distinguir evidência de inferência com `[INFERIDO]` ou `[A CONFIRMAR]`
- Preservar informações históricas no Mission Control — nunca apagar aprendizados sem evidência clara
- Nunca inventar dados; informação sem fonte vira "[não disponível]"
- Análise de squad nunca lê dentro de subpastas de clientes

## Ao final

Mostrar o que foi encontrado e pedir correções ou adições antes de confirmar.
