# Contexto: Árvore de Transição

> Referência rápida para consulta durante execução.

---

## Definição

Padronizar a construção da Árvore de Transição para transformar a injeção em ações práticas, garantir que a mudança ocorra de forma lógica e ordenada, evitar implementação caótica e conectar ação a efeito intermediário a resultado sistêmico

**Escopo:** Construção de Árvore de Transição como momento em que o diagnóstico se torna plano executável

**Aplica-se quando:**
- Injeção validada na FRT
- Obstáculos tratados na PRT (se necessário)

---

## Processo de Referência

**1. Posicionar a injeção - começar pela condição validada**

**2. Identificar primeira ação necessária perguntando qual é o primeiro movimento que precisa acontecer para isso se tornar possível**

**3. Definir efeito intermediário perguntando se essa ação acontecer, o que passa a ser possível que antes não era**

**4. Continuar a cadeia repetindo o ciclo: Ação > Efeito > Nova condição > Próxima ação**

**5. Testar a lógica perguntando para cada passo se isso não acontecer o próximo passo ainda é possível**

**6. Validar completude perguntando se essa sequência garante que a injeção se torne realidade**


---

## Saídas Esperadas

- Sequência lógica de ações
- Relação clara entre ações e efeitos
- Plano estruturado por impacto
- Base para cronograma e priorização
- Diagrama ou tabela com Ação, Efeito intermediário e Nova condição

---

## Exceções

- Utilizar apenas após a injeção estar validada na FRT
- Utilizar apenas após obstáculos relevantes terem sido tratados na PRT, se necessário

---

## Riscos e Pontos de Atenção

- ⚠️ Ausência de ferramentas definidas em todos os passos reduz rastreabilidade e padronização da execução
- ⚠️ Processo altamente dependente de julgamento consultivo qualificado — risco de variação de qualidade entre consultores
- ⚠️ Nenhum condicional explícito mapeado, o que pode gerar ambiguidade em situações de bloqueio ou revisão da injeção
- ⚠️ A validação de completude (passo 6) é subjetiva e sem critério mensurável definido
- ⚠️ Dependência de artefatos externos (FRT e PRT) sem protocolo de handoff formalizado

---

## Dependências

- Injeção validada na Árvore da Realidade Futura (FRT)
- Obstáculos tratados na Árvore de Pré-Requisitos (PRT), quando aplicável
- Presença ativa do Consultor com domínio do Logical Thinking Process
- Participação do Cliente para validação contextual dos efeitos intermediários
