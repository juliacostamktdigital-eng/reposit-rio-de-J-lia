# Contexto: Árvore de Pré-Requisitos (PRT)

> Referência rápida para consulta durante execução.

---

## Definição

Padronizar o uso da Árvore de Pré-Requisitos (PRT) para: Identificar obstáculos que podem impedir a implementação da injeção; Transformar barreiras em condições necessárias; Reduzir risco de falha na execução; Preparar o terreno para a Árvore de Transição. A PRT garante que a injeção não falhe por falta de preparo do sistema.

**Escopo:** Aplicável quando há obstáculos relevantes na implementação da injeção, incluindo casos de injeção estrutural ou complexa, resistência do cliente, falta de recursos, mudanças que envolvem várias áreas, ou quando o cliente declara impossibilidade de implementação imediata.

**Aplica-se quando:**
- Condição definida na FRT (Árvore de Realidade Futura)

---

## Processo de Referência

**1. Posicionar a injeção - Relembrar a condição definida na FRT**
- Ferramenta: FRT
**2. Identificar obstáculos - Perguntar: 'O que pode impedir isso de acontecer?' e registrar obstáculos reais, não desculpas**

**3. Validar obstáculos - Perguntar: 'Isso realmente impediria a implementação?' Se sim, manter**
- Condição: Resposta afirmativa do cliente
**4. Definir condições necessárias - Para cada obstáculo, perguntar: 'O que precisa existir para que isso deixe de ser um impedimento?'**

**5. Conectar obstáculos entre si - Identificar dependências e construir relações lógicas entre obstáculos**

**6. Validar com o cliente - Perguntar: 'Se essas condições existirem, a implementação fica viável?'**
- Condição: Resposta afirmativa do cliente

---

## Saídas Esperadas

- Diagrama com injeção, obstáculos e condições necessárias para removê-los
- Lista de obstáculos reais
- Relação de causa entre obstáculos
- Condições que precisam existir para remover cada obstáculo
- Mapa de preparação para implementação

---

## Exceções

- Não utilizar PRT quando a injeção é simples
- Não utilizar PRT quando não há resistência
- Não utilizar PRT quando a implementação é direta - ir direto para a Árvore de Transição

---

## Riscos e Pontos de Atenção

- ⚠️ Identificação de obstáculos depende de diálogo qualitativo com o cliente — não automatizável sem perda semântica
- ⚠️ Validação de obstáculos (passo 3) exige julgamento contextual do consultor sobre respostas do cliente
- ⚠️ Construção de relações lógicas entre obstáculos (passo 5) requer raciocínio causal complexo e interpretação sistêmica
- ⚠️ Risco de capturar 'desculpas' como obstáculos reais caso a facilitação seja inadequada
- ⚠️ Ausência de ferramenta definida em 4 dos 6 passos reduz rastreabilidade e padronização da execução

---

## Dependências

- FRT (Árvore de Realidade Futura) concluída e com injeção claramente definida
- Participação ativa do cliente em pelo menos os passos 2, 4 e 6
- Conhecimento do consultor em Logical Thinking Process (TOC)
- Ferramenta de diagramação para construção da árvore (não especificada no POP)
