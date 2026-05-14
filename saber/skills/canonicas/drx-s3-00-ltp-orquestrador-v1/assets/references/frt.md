# Future Reality Tree (FRT) — Referência de Construção

## O que é

A FRT é uma árvore de **lógica de suficiência** que testa se as injections propostas na Evaporating Cloud realmente produzirão os Desired Effects (DEs). É o "simulador lógico" da mudança: antes de implementar, verificamos se a lógica segura.

## Estrutura

```
    [DE 1]         [DE 2]         [DE 3]
       ↑              ↑              ↑
  [Efeito Int.]   [Efeito Int.]  [Efeito Int.]
       ↑              ↑         ↗
  [Efeito Int.]   [Efeito Int.]
       ↑         ↗       ↑
  ──────────────────────────
       ↑
  [INJECTION 1]    [INJECTION 2]
```

Leitura: "Se [Injection], então [Efeito Intermediário], então... [Desired Effect]"

## Conceitos Fundamentais

### Desired Effects (DEs)
- São os UDEs da CRT **invertidos/resolvidos**
- "O ciclo de vendas é longo demais" → "O ciclo de vendas está dentro do target de X dias"
- Cada UDE da CRT deve ter um DE correspondente na FRT

### Injections
- Vêm da Evaporating Cloud (Fase 3)
- São condições/ações que NÃO existem hoje e serão introduzidas
- Na FRT, ficam na **base** da árvore e são marcadas como entidades especiais
- Cada injection é uma "intervenção" no sistema

### Negative Branches
- Cadeias causais INDESEJADAS que emergem de uma injection ou DE
- São efeitos colaterais da mudança proposta
- Devem ser identificadas, desenvolvidas (traçar a cadeia) e "trimadas" (resolvidas com injections adicionais)

### Positive Reinforcing Loops
- Loops onde DEs alimentam condições que produzem mais DEs
- São o mecanismo de sustentabilidade da mudança
- Se a FRT não tem positive loops, a mudança pode não ser autossustentável

## Procedimento de Construção (10 passos)

### Passo 1: Converter UDEs em DEs
- Para cada UDE da CRT, escreva o DE correspondente
- O DE deve ser o **oposto lógico** do UDE, não apenas a negação
- "Clientes reclamam da demora" → "Clientes recebem atendimento dentro do SLA" (não "Clientes não reclamam")
- Use presente do indicativo

### Passo 2: Formular DEs no Presente
- Todos os DEs devem ser escritos como se já fossem realidade
- Isso permite testar a lógica: "Se [injection], então [consequência], então... [DE]"

### Passo 3: Adicionar Injections e Requisitos da EC
- Posicione as injections na base da FRT
- Se a EC produziu mais de uma injection, todas entram na FRT
- Injections dos requisitos B e C da EC também entram se forem relevantes

### Passo 4: Preencher os Gaps
- Entre as injections (base) e os DEs (topo), construa a cadeia causal
- Pergunte: "Se [injection], o que acontece em seguida? E depois?"
- Construa de baixo para cima, passo a passo
- Cada passo deve passar no teste "Se... então..."

### Passo 5: Construir Positive Reinforcing Loops
- Identifique onde DEs ou efeitos intermediários podem realimentar condições mais baixas na árvore
- Loops positivos são essenciais para sustentabilidade
- Padrão: "O resultado melhora → gera mais confiança → permite mais investimento → resultado melhora ainda mais"

### Passo 6: Buscar Negative Branches
Para cada injection e cada efeito intermediário, pergunte:
- "O que poderia dar errado ao implementar isso?"
- "Existe algum efeito colateral indesejado?"
- "Quem poderia ser prejudicado por essa mudança?"
- "Que regra, política ou norma esta ação poderia violar?"

### Passo 7: Desenvolver Negative Branches
Para cada efeito colateral identificado:
- Trace a cadeia causal: "Se [injection/DE], então [efeito colateral 1], então [efeito colateral 2]..."
- Continue até chegar ao efeito final indesejado
- Esta cadeia é uma "Negative Branch"

### Passo 8: Trimar Negative Branches
Para cada Negative Branch:
- Identifique o ponto na cadeia onde uma **injection adicional** pode interromper o efeito colateral
- Formule a injection que "trima" a branch
- Quanto mais cedo na cadeia, melhor (prevenir é melhor que remediar)

### Passo 9: Incorporar Injections de Trim na FRT
- Adicione as injections de trim à FRT
- Verifique se elas não criam NOVAS negative branches
- Se criarem, repita os passos 7-8 para as novas branches

### Passo 10: Escrutinar a FRT Inteira
Aplique as CLR ao fluxo completo:
- Cada cadeia "Se [base] → [topo]" faz sentido?
- As injections são suficientes para produzir os DEs?
- Faltam co-causas (AND) em algum ponto?
- Os positive reinforcing loops são realistas?
- As negative branches foram todas endereçadas?

## Escrutínio Específico da FRT

### Existence Reservations
- Cada DE é realmente alcançado pelas injections propostas?
- Não faz sentido "desejar" um DE sem cadeia causal que o sustente

### Additional Cause
- O DE depende APENAS das injections, ou depende também de fatores externos?
- Se depende de fatores externos não controlados, o risco é alto

### Scrutinizing Injections
- A injection é factível? Está dentro do span of control?
- A injection tem custo? O custo é aceitável?
- A injection depende de outras injections? Se sim, qual a sequência?

### "Oxygen" na FRT
- Algumas condições necessárias são tão ubíquas que não vale incluir
- Ex: "A empresa continua existindo" — é necessário, mas não informativo
- Inclua apenas se houver risco real de a condição não se manter

## Usando a Negative Branch como Ferramenta Standalone

A Negative Branch pode ser usada independentemente:
- Quando alguém propõe uma solução e você quer testar efeitos colaterais
- Quando está avaliando riscos de uma decisão
- Estrutura: [Ação Proposta] → [Consequência 1] → [Consequência 2] → [Efeito Indesejado]

## Armadilhas Comuns

1. **FRT otimista demais:** Se não encontrou negative branches, provavelmente não procurou direito
2. **DEs que são vagos:** "As coisas melhoram" não é um DE — seja específico e mensurável
3. **Pular positive reinforcing loops:** Sem loops, a mudança tende a regredir ao status quo
4. **Injections que dependem de milagres:** Se a injection é "A cultura muda", isso é um DE, não uma injection
5. **Esquecer de verificar interdependência entre injections:** Injections podem se reforçar ou conflitar entre si

## Transição para a Fase Seguinte

A FRT completa fornece:
- A **lista final de injections** (incluindo as de trim) → input para o Prerequisite Tree
- A **sequência lógica** das injections → informa a priorização na implementação
- A **lista de DEs esperados** → métricas de sucesso da mudança
