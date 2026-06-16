---
name: account-handoff
description: Transforma form de kickoff + transcript de reunião de vendas na primeira versão da Knowledge Base do cliente — gera deck HTML interativo, 4 markdowns em docs/handoff/ e Mission Control preliminar.
user-invocable: true
---

# /account-handoff — Transformar vendas em Knowledge Base

Converte materiais de vendas na primeira KB estruturada do cliente para iniciar a operação.

## Entregáveis

**1. Deck HTML interativo** (`kickoff-deck.html`) com dois modos:
- **Modo Account:** análise interna, chips de factibilidade, alertas
- **Modo Cliente:** linguagem diplomática, sem dados sensíveis

**2. 4 markdowns em `docs/handoff/`:**
- `00-resumo-vendas.md` — resumo executivo
- `02-form-kickoff.md` — form reorganizado
- `03-perguntas-kickoff.md` — agenda da reunião
- `04-promessas-e-riscos.md` — promessas com classificação (factível/otimista/perigoso)

**3. CLAUDE.md / AGENTS.md preliminares** na raiz do cliente

**4. Mission Control preliminar** com OKRs, apostas, combinados, personas

## Fluxo

1. Validar existência da pasta do cliente (se não existir → `/novo-cliente`)
2. Coletar inputs de `docs/handoff/inputs/`
3. Ler integralmente todos os arquivos
4. Marcar cada afirmação como EVIDÊNCIA, INFERÊNCIA ou LACUNA
5. Gerar markdowns e deck HTML
6. Atualizar `links.md`

## Uso do deck na reunião

Abrir em Modo Account para ver análise interna. Trocar para Modo Cliente antes de compartilhar tela. Marcar cada bloco como ✅ confirmado, ✏️ ajustar ou ❓ lacuna.

## Princípios

- Não inventar fatos — separar evidência vs inferência vs lacuna
- Material interno tem prioridade sobre suposição
- "Roda com o que tem" — lacunas viram perguntas, não bloqueios
- Linguagem cliente-facing por padrão; análise crítica só em Modo Account
