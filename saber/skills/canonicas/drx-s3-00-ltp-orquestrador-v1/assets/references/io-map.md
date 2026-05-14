# Intermediate Objectives (IO) Map — Referência de Construção

## O que é

O IO Map é uma árvore de **lógica de necessidade** que estabelece o padrão de desempenho desejado do sistema. É o benchmark contra o qual toda a análise subsequente será feita. Sem IO Map, os UDEs (Undesirable Effects) não podem ser identificados de forma rigorosa — eles seriam apenas opiniões.

## Estrutura Hierárquica

```
                    [GOAL]
                   /  |   \
              [CSF1] [CSF2] [CSF3]
             /    \     |      \
         [NC1] [NC2] [NC3]  [NC4] ...
```

- **Goal:** O resultado final que o sistema existe para alcançar. Declaração única.
- **Critical Success Factors (CSFs):** 3-5 condições absolutamente necessárias para atingir o Goal. Se qualquer CSF falhar, o Goal é inalcançável.
- **Necessary Conditions (NCs):** Condições necessárias para sustentar cada CSF. Podem ter múltiplos níveis de profundidade.

## Lógica de Necessidade

A lógica que conecta o IO Map é **necessity-based**, não sufficiency-based:
- Leia de baixo para cima: "Para [Goal], precisamos de [CSF1] **E** [CSF2] **E** [CSF3]"
- Leia de cima para baixo: "[Goal] requer [CSF1], que por sua vez requer [NC1] **E** [NC2]"

Isso é diferente da CRT/FRT que usam "Se X, então Y" (sufficiency).

## Procedimento de Construção (8 passos)

### Passo 1: Definir o Sistema
- Qual é o limite do sistema? O que está dentro vs. fora?
- Qual é o span of control do usuário? E a sphere of influence?
- Fatores no ambiente externo que afetam o sistema mas estão fora de controle

### Passo 2: Determinar o Goal do Sistema
- O Goal deve ser declarado como uma condição desejada no presente
- Pergunte: "Se este sistema funcionasse perfeitamente, qual seria o resultado?"
- Atenção: muitas vezes o que parece ser o Goal é na verdade um CSF
- Teste: se mudar o "Goal" para CSF, o antigo CSF vira Goal? Se sim, são interdependentes — escolha qual tem primazia

Exemplos de Goal statements:
- "A empresa gera lucro crescente e sustentável"
- "O sistema de saúde provê atendimento acessível e eficaz a toda a população"
- "O departamento de marketing gera leads qualificados de forma previsível e escalável"

### Passo 3: Determinar os Critical Success Factors (CSFs)
- Pergunte: "Quais são as 3-5 coisas sem as quais o Goal é impossível?"
- CSFs devem ser **mutuamente exclusivos** em escopo mas **coletivamente exaustivos** em cobertura
- Cada CSF deve ser uma condição necessária direta do Goal
- Se remover um CSF e o Goal ainda for atingível, não é um CSF verdadeiro

Exemplos de CSFs:
- "Receita suficiente e previsível"
- "Custos operacionais controlados"
- "Base de clientes satisfeita e retida"
- "Equipe capacitada e engajada"

### Passo 4: Determinar as Necessary Conditions (NCs)
- Para cada CSF, pergunte: "O que precisa estar em vigor para que este CSF seja satisfeito?"
- NCs são mais granulares e operacionais que CSFs
- Podem ter múltiplos níveis (NC de NC)
- Evite ir mais fundo do que 3 níveis abaixo dos CSFs — se precisar, o sistema pode estar mal definido

### Passo 5: Arranjar os Componentes do IO Map
- Goal no topo
- CSFs no segundo nível
- NCs abaixo de seus respectivos CSFs
- Uma NC pode suportar mais de um CSF (conexão lateral)

### Passo 6: Conectar Goal, CSFs e NCs
- Cada conexão deve passar no teste: "Para [superior], precisamos de [inferior]"
- Todas as conexões são AND lógico (todas são necessárias)

### Passo 7: Verificar as Conexões
Aplique o **"Teste de 10.000 pés":**
- Leia o IO Map inteiro de cima para baixo e depois de baixo para cima
- Pergunte: "Faz sentido para alguém que não está imerso neste sistema?"
- Se uma conexão não é intuitivamente óbvia, a entidade pode estar mal formulada

### Passo 8: Submeter a Escrutínio Externo
- Apresente o IO Map ao usuário para validação
- Pergunte especificamente:
  - "Algum CSF está faltando? Se eu ignorar completamente um destes, o Goal ainda é possível?"
  - "Alguma NC está no lugar errado? Ela suporta outro CSF?"
  - "Alguma NC é redundante ou é na verdade um 'como' e não um 'o quê'?"

## Armadilhas Comuns

1. **Confundir Goal com CSF:** Se dois itens parecem igualmente fundamentais, teste a interdependência
2. **NCs que são ações, não condições:** NCs devem ser estados ("Equipe está treinada") não ações ("Treinar a equipe")
3. **IO Map genérico demais:** Um IO Map útil é específico ao sistema e contexto — não é uma lista de desejos universal
4. **Pular para soluções:** O IO Map descreve o "destino", não o "como chegar lá"
5. **Mais de 5 CSFs:** Provavelmente você misturou CSFs com NCs — eleve o nível de abstração

## Transição para a Fase Seguinte

O IO Map completo serve como input direto para a CRT:
- Compare cada NC e CSF com a realidade atual
- Onde a realidade **não satisfaz** uma NC ou CSF → esse gap é candidato a UDE
- UDEs não são inventados — são derivados da diferença entre o IO Map e a realidade observada
