---
slug: drx-s3-02-ltp-nuvem-de-conflitos-v1
name: drx-s3-02-ltp-nuvem-de-conflitos-v1
description: "Executa a Fase 3 do Logical Thinking Process (LTP/TOC): a **Nuvem de Conflitos (Evaporating Cloud — EC)**. A Nuvem identifica e resolve o **conflito estrutural** que mantém a trava do sistema ativa."
---

# Skill: LTP — Fase 3: Nuvem de Conflitos (Evaporating Cloud)

## Descrição
Executa a Fase 3 do Logical Thinking Process (LTP/TOC): a **Nuvem de Conflitos (Evaporating Cloud — EC)**. A Nuvem identifica e resolve o **conflito estrutural** que mantém a trava do sistema ativa.

A EC responde: *"Por que o sistema continua gerando o mesmo resultado indesejado, mesmo quando as pessoas se esforçam para mudar?"*

A resposta é sempre a mesma: porque há um conflito entre duas ações legítimas que sustentam necessidades reais — e esse conflito é mantido por **premissas ocultas** que nunca foram questionadas. Quando uma premissa é desafiada e quebrada, nasce a **injeção** — a ideia que elimina o conflito sem sacrificar nenhuma das duas necessidades.

Este skill entrega a injeção conceitual validada, pronta para ser operacionalizada na Fase 4 (FRT).

## Quando Usar
- Triggers diretos: "Nuvem de Conflitos", "Evaporating Cloud", "conflito estrutural", "EC", "Fase 3 do LTP", "por que a empresa fica presa entre duas escolhas"
- Após CRT com status `[VALIDADO]` revelar uma causa raiz ligada a uma escolha estrutural recorrente
- Quando o cliente oscila entre duas estratégias sem conseguir avançar em nenhuma
- Quando há conflito visível entre áreas ou pessoas que, na verdade, buscam o mesmo objetivo
- **NÃO usar se:**
  1. A causa raiz da CRT for direta (ausência estrutural simples sem trade-off) — ir direto para FRT
  2. A CRT ainda não estiver com status `[VALIDADO]`
  3. O conflito identificado for interpessoal/político — a Nuvem analisa estrutura, não pessoas

---

## Inputs Necessários

1. ✅ **CRT com status `[VALIDADO]`** — obrigatório. Extrair: hipótese de trava, causas raízes
2. ✅ **IO Map com status `[VALIDADO]`** — para referenciar o Objetivo Comum (A) da Nuvem
3. ✅ **context/business.md + context/gtm.md + context/constraints.md** — para entender o contexto operacional do conflito

---

## Estrutura da Nuvem de Conflitos

A Nuvem tem sempre **5 elementos** e **5 setas** (relações de necessidade):

```
                    [D — Ação]
                  ↗
[B — Necessidade]
                  ↗
[A — Objetivo Comum]
                  ↘
[C — Necessidade]
                  ↘
                    [D' — Ação conflitante]
```

**Definições:**
- **A — Objetivo Comum:** o que ambos os lados querem alcançar; deve ser formulado como condição de estado desejada
- **B — Necessidade 1:** por que o lado D acredita que sua ação é necessária para alcançar A
- **C — Necessidade 2:** por que o lado D' acredita que sua ação é necessária para alcançar A
- **D — Ação 1:** o que o sistema faz hoje (ou precisa fazer) para satisfazer B
- **D' — Ação conflitante:** o que o sistema faz hoje (ou precisa fazer) para satisfazer C
- **Conflito:** D e D' são mutuamente excludentes — executar um inviabiliza o outro

**Setas e suas lógicas:**
- A → B: "Para [A], precisamos de [B]" (necessidade)
- B → D: "Para [B], precisamos de [D]" (necessidade)
- A → C: "Para [A], precisamos de [C]" (necessidade)
- C → D': "Para [C], precisamos de [D']" (necessidade)
- D ↔ D': conflito — as duas ações se bloqueiam

---

## Processo de Execução

### Step 0 — Leitura de Contexto

Antes de qualquer output:
1. Leia a CRT validada — extraia: hipótese de trava, causas raízes, UDEs centrais
2. Leia o IO Map — extraia: Goal (candidato ao Objetivo Comum A da Nuvem)
3. Leia o arquivos de context/ — extraia: conflitos operacionais já descritos, decisões recorrentes problemáticas
4. Formule internamente a hipótese de conflito a ser testada

---

### Etapa 1 — Identificação do Conflito Central

**Objetivo:** Encontrar o par de ações que se bloqueiam mutuamente, ambas defensáveis pelo cliente.

**Sinal de conflito estrutural:**
- O cliente oscila entre duas estratégias sem conseguir manter nenhuma
- Decisões recorrentes que se contradizem ao longo do tempo
- "Precisamos fazer X" e "mas também precisamos fazer Y" — e X e Y são incompatíveis
- A trava da CRT existe justamente porque o sistema está preso entre dois movimentos

**Pergunta estruturante:**
*"Onde vocês sentem que precisam escolher entre duas coisas importantes — onde avançar em uma significa recuar na outra?"*

**Exemplos clássicos:**
- Crescer receita rápido vs. manter capacidade de entrega com qualidade
- Escalar investimento em mídia vs. manter ROI positivo
- Atender mais clientes vs. manter padrão de atendimento
- Priorizar projetos (margem alta) vs. não perder a base de distribuição (fluxo de caixa imediato)

---

### Etapa 2 — Definição do Objetivo Comum (A)

**Objetivo:** Formular o estado desejado que AMBOS os lados do conflito querem alcançar.

**Regras de formulação de A:**
- Estado presente, não ação: "Crescimento sustentável e previsível" — não "crescer"
- Nível acima do conflito — se A fosse atingido, nenhum dos dois lados reclamaria
- Deve ser reconhecido imediatamente por ambas as partes como desejável

**Teste:** *"Se [A] fosse verdadeiro, o conflito entre D e D' ainda existiria?"* — se sim, A está mal formulado (ainda está no nível do conflito, não acima dele)

**Referência ao IO Map:** o Goal do IO Map é frequentemente o Objetivo Comum A da Nuvem.

---

### Etapa 3 — Identificação das Necessidades (B e C)

**Objetivo:** Explicar POR QUE cada lado acredita que sua ação é necessária para atingir A.

**Pergunta para B:** *"Por que [lado D] acredita que [D] é necessário para atingir [A]?"*
**Pergunta para C:** *"Por que [lado D'] acredita que [D'] é necessário para atingir [A]?"*

**Regras:**
- B e C devem ser necessidades legítimas — ambas fazem sentido isoladamente
- B e C NÃO conflitam entre si — apenas D e D' conflitam
- Se B e C parecerem já conflitar, você está no nível errado — suba mais um nível

**Exemplos:**
- B: "Precisamos de receita imediata para manter o caixa" → D: "Manter foco em distribuição (ticket rápido)"
- C: "Precisamos de margem maior para investir em crescimento" → D': "Migrar para projetos (ticket alto, prazo longo)"

---

### Etapa 4 — Mapeamento das Ações Conflitantes (D e D')

**Objetivo:** Tornar explícito o que o sistema **faz hoje** (ou acredita que precisa fazer) para satisfazer cada necessidade.

**Pergunta para D:** *"O que vocês fazem (ou precisam fazer) para garantir [B]?"*
**Pergunta para D':** *"O que vocês fazem (ou precisam fazer) para garantir [C]?"*

**Confirmar o conflito:** *"Vocês concordam que fazer [D] dificulta ou inviabiliza [D'], e vice-versa?"*
- Se sim → conflito confirmado, avançar para Etapa 5
- Se não → o conflito não está bem formulado; revisar D e D'

---

### Etapa 5 — Validação da Nuvem Completa

Apresentar a Nuvem montada e validar cada seta com o cliente:

> "Para [A], precisamos de [B]?" — aguardar confirmação
> "Para [B], precisamos de [D]?" — aguardar confirmação
> "Para [A], precisamos de [C]?" — aguardar confirmação
> "Para [C], precisamos de [D']?" — aguardar confirmação
> "[D] e [D'] realmente se bloqueiam?" — aguardar confirmação

Se qualquer seta não for confirmada, reformular o elemento ou a relação antes de prosseguir.

---

### Etapa 6 — Surfacing de Premissas

**Objetivo:** Tornar explícitas as premissas ocultas que sustentam cada seta. É aqui que a solução se esconde.

**Premissas sustentam as setas.** Para cada seta, a premissa responde:
*"Por que acreditamos que [inferior] é necessário para [superior]?"*

**Perguntas para cada seta:**

Para a seta **A → B:**
*"Por que acreditamos que [B] é necessário para [A]? Isso é sempre verdade?"*

Para a seta **B → D:**
*"Por que acreditamos que [D] é a única forma de satisfazer [B]? Existe outra maneira de satisfazer [B] que não exija [D]?"*

Para a seta **A → C:**
*"Por que acreditamos que [C] é necessário para [A]? Isso é sempre verdade?"*

Para a seta **C → D':**
*"Por que acreditamos que [D'] é a única forma de satisfazer [C]? Existe outra maneira de satisfazer [C] que não exija [D']?"*

Para o **conflito D ↔ D':**
*"Por que acreditamos que fazer [D] impede [D'] — e vice-versa? Isso é uma lei da física ou uma escolha feita historicamente?"*

> **Registrar todas as premissas explicitamente**, mesmo as que parecem "óbvias" — as mais óbvias são frequentemente as mais frágeis.

---

### Etapa 7 — Desafio das Premissas e Geração da Injeção

**Objetivo:** Encontrar a premissa que, ao ser desafiada, dissolve o conflito.

**Método:**
Para cada premissa identificada, perguntar:
1. *"Isso é sempre verdade ou apenas em condições específicas?"*
2. *"O que teria que mudar para que essa premissa deixasse de ser verdade?"*
3. *"Se essa premissa não existisse, o conflito entre D e D' ainda existiria?"*

**Premissa-alvo:** aquela cuja quebra permite que **B e C sejam satisfeitas simultaneamente**, sem que D e D' entrem em conflito.

**A injeção nasce aqui:**
```
INJEÇÃO: [condição nova que torna possível satisfazer B e C sem o conflito entre D e D']
```

**Características de uma injeção válida:**
- É uma condição de estado, não uma ação ("X existe e está operando" — não "fazer X")
- Quando verdadeira, permite que D e D' coexistam ou se tornem desnecessários na forma atual
- É conceitual neste momento — será operacionalizada na FRT e no Plano de Transição

**Importante para o consultor:**
*"A injeção não é o plano. É a condição lógica que precisa se tornar verdadeira. O plano vem depois."*

---

### Etapa 8 — Validação Final com o Usuário

Apresentar a Nuvem completa com premissas e injeção:

**Perguntas de validação:**
> 1. "A Nuvem como um todo faz sentido — cada seta representa algo que vocês reconhecem como real no sistema?"
> 2. "A premissa que identificamos como frágil — vocês concordam que ela pode ser questionada? Em quais circunstâncias ela não seria verdadeira?"
> 3. "A injeção proposta — se ela fosse verdadeira, vocês acreditam que o conflito entre [D] e [D'] deixaria de existir?"
> 4. "Essa injeção é algo que vocês seriam capazes de criar ou viabilizar com os recursos disponíveis?"

Aguardar confirmação. Incorporar ajustes. Avançar apenas com validação explícita.

---

## Regras de Ouro

1. **NÃO usar a Nuvem para conflitos interpessoais** — a EC analisa estrutura, não pessoas; se o conflito parece ser entre duas pessoas, investigar a estrutura que coloca essas pessoas em posições opostas
2. **NÃO avançar para FRT sem injeção validada** — a injeção deve ser confirmada pelo usuário antes de projetar efeitos futuros
3. **NÃO pular o surfacing de premissas** — as premissas são onde a solução vive; sem elas, a injeção é arbitrária
4. **NÃO formular D ou D' como "fazer" — formular como condição de estado atual** que o sistema tenta manter
5. **NÃO aceitar uma Nuvem onde B e C já conflitam** — se conflitam, você está no nível errado; subir abstração
6. **A injeção é conceitual, não operacional** — não confundir com plano de ação; a operacionalização acontece na FRT e no Plano de Transição

---

## Formato de Saída Obrigatório

```markdown
## Nuvem de Conflitos — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome]
**Trava CRT de origem:** [hipótese de trava validada na CRT]

---

### Diagrama da Nuvem

```
                          [D: ação 1]
                        ↗
[B: necessidade 1]
                        ↗
[A: objetivo comum] →
                        ↘
[C: necessidade 2]
                        ↘
                          [D': ação conflitante]

                    D ↔ D' [CONFLITO]
```

---

### Nuvem — Leitura Completa

**A — Objetivo Comum:** [declaração]

**B — Necessidade 1:** [declaração]
→ "Para [A], precisamos de [B]"

**C — Necessidade 2:** [declaração]
→ "Para [A], precisamos de [C]"

**D — Ação 1:** [declaração]
→ "Para [B], precisamos de [D]"

**D' — Ação Conflitante:** [declaração]
→ "Para [C], precisamos de [D']"

**Conflito:** [por que D e D' se bloqueiam]

---

### Premissas Identificadas

**Seta A → B:** "[premissa que sustenta que B é necessário para A]"
**Seta B → D:** "[premissa que sustenta que D é a única forma de satisfazer B]"
**Seta A → C:** "[premissa que sustenta que C é necessário para A]"
**Seta C → D':** "[premissa que sustenta que D' é a única forma de satisfazer C]"
**Conflito D ↔ D':** "[premissa que sustenta que D e D' são mutuamente excludentes]"

---

### Premissa Desafiada

> **Premissa frágil identificada:** [declaração]
>
> **Por que pode ser questionada:** [raciocínio]
> **Condição para quebrá-la:** [o que precisa ser verdadeiro para que a premissa deixe de ser válida]

---

### Injeção Lógica

> **INJEÇÃO:** [condição de estado que, quando verdadeira, dissolve o conflito]
>
> *Efeito na Nuvem:* [como a injeção permite que B e C sejam satisfeitas sem conflito entre D e D']
> *Conexão com o IO Map:* [qual CSF ou NC esta injeção endereça]

---

> **EC Status:** `[AGUARDANDO VALIDAÇÃO]`
```

### Após validação confirmada

```
> **EC Status:** `[VALIDADO PELO USUÁRIO]`
> **Injeção confirmada:** [resumo em 1 linha]
> **Próximo passo:** FRT — `skill-ltp-frt.md`
```

Salvar ou atualizar o arquivo `nuvem-conflitos.md` do cliente com o output completo.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output (conflito central + premissa quebrada + injeção validada).
