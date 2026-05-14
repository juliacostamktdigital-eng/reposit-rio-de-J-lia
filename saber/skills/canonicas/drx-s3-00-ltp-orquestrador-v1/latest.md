---
slug: drx-s3-00-ltp-orquestrador-v1
name: ltp-thinking-process
description: >
  Orquestra o Logical Thinking Process (LTP) de Dettmer/TOC de forma faseada e interativa,
  guiando o usuario pelas ferramentas logicas para diagnosticar problemas sistemicos,
  resolver conflitos e planejar mudancas. Use SEMPRE que mencionar: LTP, thinking process,
  current reality tree, CRT, evaporating cloud, future reality tree, FRT, prerequisite tree,
  IO map, UDE, efeitos indesejaveis, causa raiz, root cause, conflito sistemico, o que mudar,
  para o que mudar, como causar a mudanca, restricao, constraint, TOC tools. Tambem acione
  para: analisar problema, encontrar causa raiz, resolver conflito, planejar mudanca,
  diagnosticar por que algo nao funciona - especialmente em sistemas organizacionais ou
  estrategicos.
---

# Logical Thinking Process (LTP) - Orquestrador

> **Este skill e o maestro do processo LTP. Ele guia o sequenciamento, mantem a coerencia entre fases e delega a execucao de cada fase ao skill especifico. Ele proprio NAO executa nenhuma fase.**

---

## Filosofia Central

O LTP responde a quatro perguntas sequenciais sobre qualquer sistema:

1. **O que mudar?** (diagnostico) -> IO Map + Current Reality Tree
2. **Para o que mudar?** (solucao) -> Evaporating Cloud + Future Reality Tree
3. **Como causar a mudanca?** (execucao) -> Prerequisite Tree
4. **Como sustentar a mudanca?** (gestao da mudanca) -> Behavioral approach

Cada pergunta exige ferramentas logicas especificas. O processo e executado **uma fase por vez**, com validacao do usuario entre fases. Nunca avance para a proxima fase sem confirmar com o usuario que o output atual esta validado.

---

## Mapa de Fases e Skills

| Fase | Pergunta | Ferramenta | Skill a invocar |
|------|----------|------------|-----------------|
| 0+1 | O que mudar? (benchmark) | IO Map | `skill-ltp-iomap.md` |
| 2 | O que mudar? (diagnostico) | Current Reality Tree | `skill-ltp-crt.md` *(a criar)* |
| 3 | Para o que mudar? (conflito) | Evaporating Cloud | `skill-ltp-ec.md` *(a criar)* |
| 4 | Para o que mudar? (futuro) | Future Reality Tree | `skill-ltp-frt.md` *(a criar)* |
| 5 | Como causar a mudanca? | Prerequisite Tree | `skill-ltp-prt.md` *(a criar)* |
| 6 | Como sustentar? | Gestao da Mudanca | *(a criar)* |

---

## Como Iniciar o LTP

Quando o usuario invocar o LTP (ou qualquer trigger do processo), faca:

**1. Verificar se existe contexto ja coletado:**
- Existem os arquivos `context/` no projeto? Ler `context/business.md`, `context/constraints.md` e `DECISIONS.md` (se disponível) -> Use como base
- Existe um IO Map com status `[VALIDADO]`? -> Identifique em qual fase o processo esta e retome a partir dai

**2. Se estiver comecando do zero, pergunte:**

> "Qual e o sistema que queremos analisar? Descreva brevemente o contexto, o que voce gerencia ou influencia, e qual resultado deveria estar acontecendo mas nao esta."

**3. Apresente o roteiro das fases:**

Apos entender o contexto inicial, exiba o mapa de fases acima e diga:

> "Vamos percorrer este processo fase por fase. Cada fase entrega um output validado que serve de input para a proxima. Comecamos pelo IO Map - ele define o padrao ideal do sistema antes de olharmos para os problemas. Podemos iniciar?"

**4. Acione o skill da fase correspondente:**

Diga ao usuario qual skill sera usado e inicie-o:

> "Para a Fase 0+1, vou usar o skill `skill-ltp-iomap.md`."

---

## Protocolo de Progressao entre Fases

A cada transicao de fase, o orquestrador deve:

1. **Confirmar que o output anterior esta validado** - status `[VALIDADO]` presente
2. **Resumir o que foi produzido** - 2-3 linhas sobre o que a fase entregou
3. **Explicar o input que a proxima fase consome** - o que sera carregado adiante
4. **Apresentar a proxima fase** - proposito, pergunta que responde, output esperado
5. **Perguntar se pode avancar** - nao avancar sem confirmacao explicita

Exemplo de transicao IO Map -> CRT:

> "O IO Map esta validado. Ele estabelece que o Goal e [X] e que os Critical Success Factors sao [CSF1], [CSF2] e [CSF3]. Agora vamos para a Fase 2 - a Current Reality Tree - que vai comparar essa realidade ideal com o que esta acontecendo de fato, identificando os Undesirable Effects e suas causas raiz. Para isso usarei o skill `skill-ltp-crt.md`. Podemos avancar?"

---

## Registro de Progresso

Mantenha um bloco de progresso visivel ao usuario no inicio de cada resposta quando retomar uma sessao LTP:

```
## Progresso LTP - [Nome do Sistema]

- [x] Fase 0+1: IO Map ........................ [VALIDADO]
- [ ] Fase 2: Current Reality Tree ........... [PENDENTE]
- [ ] Fase 3: Evaporating Cloud .............. [PENDENTE]
- [ ] Fase 4: Future Reality Tree ............ [PENDENTE]
- [ ] Fase 5: Prerequisite Tree .............. [PENDENTE]
```

---

## Regras de Salto de Fase

Se o usuario quiser pular diretamente para uma ferramenta especifica (ex: "preciso de uma Evaporating Cloud ja"):

1. **Alerte sobre o risco:** explique que cada ferramenta consome o output da anterior. Sem CRT, a EC nao tem causas raiz para conflitualizar. Sem IO Map, a CRT nao tem benchmark para identificar UDEs.

2. **Pergunte pelos inputs necessarios:**
   - Para EC: "Voce ja tem uma Critical Root Cause identificada? E sabe articular o conflito subjacente?"
   - Para FRT: "Voce ja tem injections definidas? Elas vieram de uma EC?"
   - Para PrT: "Voce tem um FRT com Desired Effects confirmados?"

3. **Se o usuario confirmar que tem os inputs**, prossiga com o skill especifico, mas registre no bloco de progresso que as fases anteriores foram puladas.

---

## Principios Logicos Transversais (aplicar em todas as fases)

### Categories of Legitimate Reservation (CLR)

Aplique estas reservas a CADA entidade e conexao em qualquer arvore:

1. **Clarity** - A entidade e clara e sem ambiguidade?
2. **Entity Existence** - A entidade realmente existe na realidade?
3. **Causality Existence** - Existe relacao causal real (nao apenas correlacao)?
4. **Cause Insufficiency** - A causa e suficiente para o efeito, ou faltam causas adicionais?
5. **Additional Cause** - Existe outra causa independente que tambem produz o mesmo efeito?
6. **Cause-Effect Reversal** - Causa e efeito estao na direcao correta?
7. **Predicted Effect Existence** - Se a causa e verdadeira, que outro efeito verificavel deveria existir?
8. **Tautology** - Ha logica circular (efeito "prova" causa que "prova" efeito)?

Verbalize: "Se [causa], entao [efeito]... mas sera que [reserva]?"

### Regras de Construcao de Entidades

- Declaracao completa no presente (sujeito + verbo + complemento)
- Nunca entidades compostas (duas ideias em uma caixa) - separe
- Nunca logica "if-then" embutida dentro de uma entidade
- Cada seta causal deve sobreviver: "Se [causa], entao [efeito]" - intuitivamente verdadeiro
- Arvores de suficiencia (CRT, FRT): use "Se... entao..."
- Arvores de necessidade (IO Map, PrT): use "Para... precisamos de..."

### Notacao

- **Ellipse (AND logico):** causas que JUNTAS sao necessarias para produzir o efeito
- **Setas independentes:** causas que SOZINHAS produzem o efeito
- **"Oxygen":** condicoes ubiquas - existem mas nao sao uteis de incluir
- **UDE:** Efeito Indesejavel - verificavel contra o IO Map
- **DE:** Efeito Desejavel - o UDE resolvido/invertido
- **Injection:** condicao que nao existe hoje, introduzida para mudar a realidade
- **Negative Branch:** cadeia causal indesejada que emerge de uma injection ou DE
