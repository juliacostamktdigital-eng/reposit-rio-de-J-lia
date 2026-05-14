---
slug: coringa-sx-03-outputs-validados-template-v1
name: coringa-sx-03-outputs-validados-template-v1
description: "Mantém o índice acumulativo de **tudo que foi validado** no engajamento — tanto outputs entregues ao cliente final quanto rodadas internas que tiveram seu status promovido para `[VALIDADO]`. Skills subsequentes leem este documento como \"..."
---

# Skill: Changelog de Outputs e Rodadas Validadas (Coringa SX-03)

## Descrição

Mantém o índice acumulativo de **tudo que foi validado** no engajamento — tanto outputs entregues ao cliente final quanto rodadas internas que tiveram seu status promovido para `[VALIDADO]`. Skills subsequentes leem este documento como "o que já sabemos sobre este cliente".

**Localização:** `clientes/[nome-cliente]/produtos/[produto-ativo]/changelog.md`

## Quando Usar

A skill é disparada **na transição de status `[AGUARDANDO VALIDAÇÃO]` → `[VALIDADO]`** de qualquer artefato. Triggers típicos:

- Consultor sinaliza "validado", "aprovado", "ok pode seguir" sobre um arquivo ou rodada
- Output que estava na pasta do produto migra para `outputs/`
- `master-contexto.md` ou `context/*.md` sai de `[AGUARDANDO VALIDAÇÃO]` para `[VALIDADO]`
- Fase fecha (ambos os critérios — entregável validado + context sincronizado — são satisfeitos)

**O que conta como "validado" para este changelog:**

| Tipo | Exemplo | Entry no changelog? |
| :--- | :--- | :--- |
| Output ao cliente final | Deck do kickoff aprovado | ✅ Sim |
| Rodada interna validada | `master-contexto.md` promovido para `[VALIDADO]` | ✅ Sim |
| Context populado e validado | `context/business.md` promovido para `[VALIDADO]` | ✅ Sim (entry agrupado da rodada) |
| Fase concluída | S1 fechada (entregável + context sincronizados) | ✅ Sim |
| Rodada interna **não** validada | `sx-01` rodou mas master-contexto ainda em `[AGUARDANDO]` | ❌ Não |
| Decisão registrada em `DECISIONS.md` | D1, D2, D3 | ❌ Não (vive em `DECISIONS.md`, não duplica aqui) |

## Regra de Ouro

**Nunca sobrescrever entries existentes** — apenas adicionar novos ao final, em ordem cronológica de validação.

---

## Formato de Entry

```markdown
## [YYYY-MM-DD] — [Tipo] · [Título curto]

- **Validado por:** [nome do consultor]
- **Origem:** [skill/processo que gerou — ex: `coringa-sx-01`, kickoff, S2-sizing]
- **Arquivos afetados:** [lista de paths que ficaram com status `[VALIDADO]`]
- **Resumo:** [1–3 linhas: o que foi validado e qual o significado para o engajamento]
- **Próximo desbloqueio:** [o que esta validação destrava — ex: "permite iniciar S2", "permite mover entregáveis para produtos/<P>/outputs/"]
```

**Tipos possíveis:**
- `Rodada interna` — context populado, master-contexto consolidado
- `Entregável validado` — output que pode migrar para `outputs/` e/ou ser enviado ao cliente
- `Fase concluída` — fecha um Sx (ambos os critérios atendidos)
- `Decisão de escopo` — mudança contratual ou de direção registrada também em `DECISIONS.md`

---

## Template do arquivo (quando criado pela primeira vez)

```markdown
# Changelog — [Nome do Cliente] / [Produto Ativo]

> Índice acumulativo de tudo que foi validado neste produto.
> Inclui rodadas internas validadas, outputs entregues e fases concluídas.
> Skills subsequentes leem este documento como "o que já sabemos sobre este cliente".
>
> **Regra:** nunca sobrescrever entries existentes — apenas adicionar novos ao final, em ordem cronológica.

---

<!-- ENTRIES ABAIXO -->
```

---

## Não-objetivos

- A skill **não** valida — apenas registra a validação que o consultor já fez.
- A skill **não** duplica decisões que vivem em `DECISIONS.md`.
- A skill **não** é o local de trabalho em construção — arquivos analíticos ficam na raiz do produto; quando enviados ao cliente, vão para `outputs/` do produto.
