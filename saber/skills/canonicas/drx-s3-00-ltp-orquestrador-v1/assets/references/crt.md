# Current Reality Tree (CRT) — Referência de Construção

## O que é

A CRT é uma árvore de **lógica de suficiência** que modela a realidade atual do sistema como uma rede de relações causa-efeito. Seu propósito é responder "O que mudar?" identificando as Critical Root Causes que produzem a maioria dos Undesirable Effects observados.

## Estrutura

```
        [UDE 1]        [UDE 2]        [UDE 3]
           ↑              ↑              ↑
      [Causa Int.]    [Causa Int.]   [Causa Int.]
           ↑         ↗    ↑              ↑
      [Causa Int.]  /  [Causa Int.]  [Causa Int.]
           ↑       /      ↑         ↗
      ────────────────────────────────
           ↑
    [CRITICAL ROOT CAUSE]
```

A CRT lê de baixo para cima: "Se [causa], então [efeito]."

## Conceitos Fundamentais

### UDEs (Undesirable Effects)
- São os **sintomas** observáveis do sistema — NÃO as causas
- Devem ser verificáveis: existe evidência de que este efeito está ocorrendo?
- Devem ser indesejáveis em relação ao IO Map (não é opinião — é gap mensurável)
- Devem estar no **presente do indicativo**: "O ciclo de vendas é longo demais" (não "o ciclo de vendas deveria ser menor")
- Tipicamente 5-10 UDEs são suficientes para um sistema

### Como Identificar UDEs
Compare a realidade com o IO Map:
- Para cada NC e CSF, pergunte: "Esta condição está sendo satisfeita?"
- Se não → formule o gap como um efeito observável
- Teste: "Isso é um fato verificável, não uma opinião?" Se sim → é candidato a UDE

### Root Causes vs. Critical Root Causes
- **Root Cause:** qualquer entidade na base da CRT que não tem causa anterior dentro do sistema
- **Critical Root Cause:** a root cause que, se eliminada, removeria ≥70% dos UDEs
- Nem toda root cause é crítica. Foque energia nas que têm maior alavancagem
- Se nenhuma root cause individual atinge 70%, pode ser necessário atacar 2-3 em combinação

### Correlação vs. Causalidade
A CRT exige causalidade real, não correlação. Para cada conexão, aplique o teste:
1. Se eu removo a causa, o efeito desaparece? (necessidade)
2. Quando a causa está presente, o efeito sempre ocorre? (suficiência)
3. Existe um mecanismo causal explicável? (não é coincidência)

## Procedimento de Construção (10 passos)

### Passo 1: Definir o Sistema a ser Modelado
- Use a definição de sistema da Fase 0
- Relembre os limites: o que está dentro do span of control e sphere of influence?

### Passo 2: Determinar os UDEs
- Liste 5-10 UDEs derivados da comparação IO Map vs. realidade
- Cada UDE deve ser:
  - Uma declaração completa no presente
  - Verificável (não especulativa)
  - Indesejável em relação ao IO Map
  - Dentro do sistema definido
- Organize os UDEs em uma "starting matrix" — uma tabela onde cada UDE é testado contra os outros: "X causa Y?" "Y causa X?" "Nenhum dos dois?"

### Passo 3: Determinar os Dois Primeiros Níveis de Causalidade
Para cada UDE, pergunte: "POR QUE este efeito existe?"
- Identifique 1-3 causas diretas para cada UDE
- Formule cada causa como entidade completa no presente
- Crie "clusters" (aglomerados) de UDE + suas causas diretas

### Passo 4: Iniciar a CRT
- Posicione os UDEs no topo
- Posicione suas causas diretas abaixo
- Use AND (ellipse) quando múltiplas causas são TODAS necessárias juntas
- Use setas independentes quando cada causa sozinha é suficiente

### Passo 5: Melhorar a Lógica dos Clusters Iniciais
Aplique as CLR a cada cluster:
- **Clarity:** cada entidade é clara e sem ambiguidade?
- **Entity Existence:** cada entidade realmente existe?
- **Cause Sufficiency:** a causa é suficiente para produzir o efeito? Faltam co-causas (AND)?
- **Causality Existence:** a relação é causal ou apenas correlação?

### Passo 6: Identificar Causas Adicionais
- Para cada efeito, pergunte: "Existe outra causa independente que também produziria este efeito?"
- Causas adicionais entram como setas independentes (OR lógico)
- Teste: "Se a causa original NÃO existisse, este efeito AINDA poderia ocorrer por causa desta outra causa?"

### Passo 7: Buscar Conexões Laterais
- Examine se causas de um cluster também afetam efeitos de outro cluster
- Estas conexões laterais são o que transforma clusters isolados em um sistema interconectado
- Conexões laterais revelam o V-shape pattern: múltiplos UDEs convergindo para poucas causas raiz

### Passo 8: Construir as Cadeias Causais Para Baixo
- Para cada causa intermediária, continue perguntando "Por quê?"
- Continue até chegar a entidades que:
  - Estão fora do sistema (ambiente externo)
  - São políticas ou decisões que podem ser mudadas
  - São fatos da realidade que não podem ser alterados
- Estas são as Root Causes

### Passo 9: Escrutinar a CRT Inteira
Aplique as 8 CLR ao fluxo completo:
- Leia cada cadeia causal de baixo para cima
- Teste: "Se [root cause], então... então... então [UDE]" — cada passo faz sentido?
- Identifique Negative Reinforcing Loops (loops de feedback que amplificam o problema)

### Passo 10: Decidir Quais Root Causes Atacar
- Marque cada root cause e conte quantos UDEs ela afeta
- A que afeta mais UDEs (≥70%) é a **Critical Root Cause**
- Se nenhuma atinge 70% sozinha, identifique a combinação mínima que atinge
- Priorize: está dentro do span of control? É atuável?

## Negative Reinforcing Loops

Loops onde o efeito reforça a causa que reforça o efeito. São comuns em sistemas disfuncionais e explicam por que problemas "parecem crescer sozinhos."

Padrão:
```
[Causa A] → [Efeito B] → [Efeito C] → amplifica [Causa A]
```

Quando encontrar um loop: marque-o explicitamente. Loops são pontos de alta alavancagem — quebrar o loop em qualquer ponto resolve o ciclo.

## Armadilhas Comuns

1. **UDEs que são causas, não efeitos:** Se você pode perguntar "por que?" e obter uma resposta mais observável, o UDE está profundo demais
2. **Entidades compostas:** "Nossa equipe é pequena E inexperiente" — separe em duas entidades
3. **Saltar de UDE para solução:** A CRT NÃO resolve — ela diagnostica. Soluções vêm na EC/FRT
4. **CRT grande demais:** Se tem mais de 30-40 entidades, o escopo do sistema pode estar amplo demais
5. **Ignorar o IO Map:** UDEs sem referência ao IO Map são apenas reclamações

## Transição para a Fase Seguinte

A CRT completa fornece:
- As **Critical Root Causes** → input para a Evaporating Cloud (EC)
- O conflito subjacente normalmente envolve: para resolver a root cause, seria necessário fazer X, mas X conflita com Y que também é necessário
- A EC vai articular este conflito e buscar injections para resolvê-lo
