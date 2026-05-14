# Evaporating Cloud (EC) — Referência de Construção

## O que é

A Evaporating Cloud (também chamada Conflict Resolution Diagram) é uma ferramenta de **lógica de necessidade** que articula um conflito subjacente e o resolve surfaceando e invalidando **assumptions ocultas**. O conflito "evapora" quando descobrimos que uma assumption que sustenta a necessidade de uma das posições conflitantes é falsa ou pode ser invalidada por uma injection.

## Estrutura da EC

```
    [A] Objetivo Comum
   /                   \
 [B] Requisito 1     [C] Requisito 2
   \                   /
   [D] Pré-req de B   [D'] Pré-req de C
         ←CONFLITO→
```

Leitura:
- "Para alcançar [A], precisamos de [B]" (A→B)
- "Para alcançar [A], precisamos de [C]" (A→C)
- "Para satisfazer [B], precisamos de [D]" (B→D)
- "Para satisfazer [C], precisamos de [D']" (C→D')
- "[D] e [D'] estão em conflito direto" — não podem coexistir

## Tipos de EC

### EC de 3 UDEs (3-UDE Cloud)
Quando 3 UDEs da CRT convergem para um padrão:
- UDE1 e UDE2 são consequências de posições opostas (D e D')
- UDE3 é consequência do conflito em si (a oscilação ou paralisia)

### EC Standalone
Quando o conflito é identificado diretamente, sem necessidade de CRT prévia:
- O usuário já sabe que existe um dilema/trade-off
- Útil para decisões difíceis onde "ambas as opções parecem ruins"

## Procedimento de Construção (12 passos)

### Passo 1: Identificar o Conflito
A partir da CRT: a Critical Root Cause geralmente envolve um conflito:
- "Precisamos fazer X para resolver a causa raiz"
- "Mas fazer X viola/prejudica Y que também precisamos"
- Se não é óbvio, pergunte: "Por que esta root cause persiste? O que impede a organização de resolvê-la?"

### Passo 2: Articular os Dois Lados (D e D')
- D = a ação/condição que um lado defende
- D' = a ação/condição oposta que o outro lado defende
- D e D' devem ser **mutuamente exclusivos** — fazer um impede fazer o outro
- Formule como condições no presente: "Investimos pesado em aquisição" vs. "Focamos em retenção e expansão"

### Passo 3: Identificar os Requisitos (B e C)
- B = a necessidade legítima que justifica D: "Para [B], precisamos de [D]"
- C = a necessidade legítima que justifica D': "Para [C], precisamos de [D']"
- B e C devem ser necessidades reais e legítimas — NÃO posições ou opiniões

### Passo 4: Identificar o Objetivo Comum (A)
- A = o objetivo de nível superior que TANTO B quanto C servem
- Teste: "Para [A], precisamos de [B]" E "Para [A], precisamos de [C]" — ambos devem ser verdadeiros
- Se B e C não compartilham um objetivo comum, o conflito pode ser falso

### Passo 5: Verificar a Estrutura
Leia toda a EC:
- "Para [A], precisamos de [B], e para [B], precisamos de [D]"
- "Para [A], precisamos de [C], e para [C], precisamos de [D']"
- "Mas [D] e [D'] conflitam"
- Cada afirmação de necessidade faz sentido? Se não, ajuste.

### Passo 6: Surfacear Assumptions (A→B)
Pergunte: "POR QUE [B] é necessário para [A]? Quais são as premissas por trás dessa necessidade?"
- Liste TODAS as assumptions — mesmo as óbvias
- Cada assumption é uma crença que, se falsa, quebraria a conexão

### Passo 7: Surfacear Assumptions (A→C)
Mesmo processo para a conexão A→C.

### Passo 8: Surfacear Assumptions (B→D)
Pergunte: "POR QUE [D] é a ÚNICA forma de satisfazer [B]?"
- Esta é geralmente a conexão mais rica em assumptions invalidáveis
- Muitas vezes assume-se que D é a única opção, mas existem alternativas

### Passo 9: Surfacear Assumptions (C→D')
Mesmo processo para C→D'.

### Passo 10: Surfacear Assumptions do Conflito (D↔D')
Pergunte: "POR QUE [D] e [D'] não podem coexistir?"
- Às vezes o conflito é de tempo, não de essência (podem ser feitos em sequência)
- Às vezes o conflito é de recurso (poderiam coexistir com mais recursos)
- Às vezes o conflito é conceitual (uma redefinição resolve)

### Passo 11: Identificar Injections
Para cada assumption, pergunte: "E se esta premissa fosse falsa? O que mudaria?"
- Uma **injection** é uma condição ou ação que **não existe hoje** mas que, se introduzida, invalidaria a assumption
- Injections quebram a necessidade em uma das conexões, fazendo o conflito "evaporar"
- Priorize injections que:
  1. Estão dentro do span of control
  2. São factíveis com recursos disponíveis
  3. Não criam novos conflitos graves

### Passo 12: Validar as Injections
Para cada injection candidata, pergunte:
- "Se implementarmos esta injection, a assumption realmente se torna inválida?"
- "A injection é factível? Realista?"
- "A injection cria novos problemas?" (se sim, estes serão tratados como Negative Branches na FRT)

## A Arte de Surfacear Assumptions

Esta é a parte mais valiosa e mais difícil da EC. Dicas:

1. **Assuma que cada conexão tem pelo menos 3-5 assumptions ocultas** — force-se a encontrá-las
2. **Muitas assumptions são culturais ou setoriais** — "todo mundo faz assim" não é causalidade
3. **Pergunte "E se o oposto fosse verdade?"** para cada assumption
4. **Busque assumptions de tempo** — "precisamos de D agora" pode não ser verdade se D puder ser feito depois
5. **Busque assumptions de escopo** — "precisamos de D para TODOS" pode não ser verdade se D for necessário apenas para um segmento

## Armadilhas Comuns

1. **Conflito falso:** D e D' não são realmente mutuamente exclusivos — na verdade podem coexistir
2. **A ≠ objetivo real:** Se A está errado, toda a EC está errada. Teste rigorosamente
3. **Injections que são "desejo mágico":** "Se tivéssemos orçamento infinito..." não é uma injection útil
4. **Pular o surfaceamento de assumptions:** A tentação é ir direto para injections. Resista. As melhores injections emergem de assumptions bem articuladas
5. **Assumptions que são fatos:** "A gravidade existe" não é invalidável. Foque em assumptions que são crenças ou políticas

## Transição para a Fase Seguinte

A EC completa fornece:
- **Injections validadas** → estas são os inputs da Future Reality Tree (FRT)
- Cada injection será testada na FRT: "Se implementarmos esta injection, ela realmente produz os Desired Effects?"
- Injections que criam efeitos colaterais serão tratadas como Negative Branches na FRT
