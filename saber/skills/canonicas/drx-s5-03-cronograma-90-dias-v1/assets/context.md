# Contexto: Cronograma de Implementação

> Referência rápida para consulta durante execução.

---

## Definição

Padronizar a construção de um cronograma técnico e executável (90-180 dias) com base na Árvore de Transição, garantindo: Sequência lógica das ações, Estimativa de tempo baseada em complexidade, Priorização por impacto sistêmico, Eliminação de achismos

**Escopo:** None

**Aplica-se quando:**
- Árvore de Transição
- Injeção definida
- FRT (Sistema funcionando com a injeção)
- PRT (se necessário)

---

## Processo de Referência

**1. Extrair ações da Árvore de Transição**

**2. Classificar tipo de ação em Estratégica, Tática ou Operacional**

**3. Classificar complexidade em Baixa, Média ou Alta**

**4. Estimar esforço técnico conforme duração base por complexidade**

**5. Identificar dependências perguntando se a ação pode começar antes da anterior terminar**

**6. Priorizar pelo impacto sistêmico, considerando ações que afetam capacidade de aquisição, conversão e retenção**

**7. Distribuir no tempo por blocos: 0-30 dias (Estrutura base), 30-90 dias (Otimização), 90-180 dias (Escala)**


---

## Saídas Esperadas

- Lista de ações estruturantes
- Classificação de esforço
- Dependências claras
- Linha do tempo realista
- Base para gestão de execução

---

## Riscos e Pontos de Atenção

- ⚠️ Ausência de critérios objetivos para classificação de complexidade (Baixa/Média/Alta) pode gerar inconsistência entre consultores
- ⚠️ Estimativa de esforço sem tabela de referência explícita torna o passo 4 subjetivo e não reproduzível
- ⚠️ Nenhuma exceção documentada: o POP não prevê o que fazer se a Árvore de Transição estiver incompleta ou ausente
- ⚠️ Priorização por impacto sistêmico (passo 6) depende de julgamento especializado sem critério formal, criando risco de viés
- ⚠️ Sem ferramenta definida, a saída pode variar em formato e estrutura entre execuções

---

## Dependências

- Árvore de Transição concluída e validada
- Injeção definida e aprovada
- FRT disponível e consistente com a injeção
- PRT disponível quando aplicável
- Conhecimento do consultor sobre o contexto sistêmico do cliente para execução dos passos 2, 3 e 6
