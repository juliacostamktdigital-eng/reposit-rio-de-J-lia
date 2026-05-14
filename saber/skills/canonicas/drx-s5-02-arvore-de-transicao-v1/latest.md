---
slug: drx-s5-02-arvore-de-transicao-v1
name: drx-s5-02-arvore-de-transicao-v1
description: "Padronizar a construção da Árvore de Transição para transformar a injeção em ações práticas, garantir que a mudança ocorra de forma lógica e ordenada, evitar implementação caótica e conectar ação → efeito intermediário → resultado sistêmico"
---

# Árvore de Transição

## Descrição
Padronizar a construção da Árvore de Transição para transformar a injeção em ações práticas, garantir que a mudança ocorra de forma lógica e ordenada, evitar implementação caótica e conectar ação → efeito intermediário → resultado sistêmico
Ativar quando logical thinking process, árvore de transição, planejamento executável, pe&g for necessário.

## Quando Usar
- Trigger: "Logical Thinking Process", "Árvore de Transição", "Planejamento Executável", "PE&G"
- NÃO usar quando: Ausência de ferramentas especificadas em todos os passos impede automação direta do fluxo; A validação lógica (passo 5 e 6) exige julgamento consultivo humano, não replicável por IA sem contexto do caso; A construção da cadeia causal (passos 2, 3 e 4) depende de raciocínio situacional sobre o cliente específico; Sem critérios objetivos de 'completude', o passo 6 pode gerar ambiguidade na execução
## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

1. **Injeção validada na FRT**
2. **Obstáculos tratados na PRT (se necessário)**

## Processo de Execução

### 1. Posicionar a injeção começando pela condição validada

### 2. Identificar primeira ação necessária perguntando: qual é o primeiro movimento que precisa acontecer para isso se tornar possível?

### 3. Definir efeito intermediário perguntando: se essa ação acontecer, o que passa a ser possível que antes não era?

### 4. Continuar a cadeia repetindo o ciclo: Ação → Efeito → Nova condição → Próxima ação

### 5. Testar a lógica para cada passo perguntando: se isso não acontecer, o próximo passo ainda é possível?
- Condicional: Se não, a ordem está correta
### 6. Validar completude perguntando: essa sequência garante que a injeção se torne realidade?

## Formato de Saída
- Diagrama ou tabela com: Ação, Efeito intermediário e Nova condição
- Sequência lógica de ações
- Relação clara entre ações e efeitos
- Plano estruturado por impacto
- Base para cronograma e priorização

## Exceções e Fallbacks
- Utilizar sempre após a injeção estar validada na FRT
- Obstáculos relevantes devem ter sido tratados na PRT quando necessário
