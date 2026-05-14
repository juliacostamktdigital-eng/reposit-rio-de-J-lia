---
slug: drx-s4-03-puv-proposta-unica-de-valor-v1
name: drx-s4-03-puv-proposta-unica-de-valor-v1
description: "Define e consolida a Proposta Única de Valor do negócio dentro do projeto DR-X. Conecta a dor central do cliente, o mecanismo da solução e o resultado esperado em uma mensagem clara que sustentará comunicação, marketing, vendas e discurs..."
---

# Definição de PUV (Proposta Única de Valor)

## Descrição
Define e consolida a Proposta Única de Valor do negócio dentro do projeto DR-X. Conecta a dor central do cliente, o mecanismo da solução e o resultado esperado em uma mensagem clara que sustentará comunicação, marketing, vendas e discurso estratégico.
Ativar quando posicionamento estratégico, proposta de valor, PUV, mensagem de valor for necessário.

## Quando Usar
- Triggers: "definir PUV", "proposta de valor", "proposta única de valor", "por que o cliente deve escolher", "mensagem central", "posicionamento de valor"
- **NÃO usar quando:**
  1. O ICP ainda não foi definido — resolver ICP antes, pois a PUV depende de saber para quem
  2. A Matriz CVB (Diferenciais Competitivos) não está pronta — a PUV precisa dos diferenciais reais como insumo
  3. O diagnóstico de travas não foi concluído — sem diagnóstico, a dor central pode estar errada

## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

1. **context/business.md** + **context/gtm.md** + **context/constraints.md** `[VALIDADO]` — visão geral do negócio, produto, modelo de monetização
2. **Ficha de ICP** — output da skill-definicao-de-icps (quem é o cliente ideal, qual dor tem)
3. **Matriz CVB** — output da skill-diferenciais-competitivos-matriz-cvb (diferenciais reais validados)
4. **Diagnóstico de travas** — contextos das travas 1-7 (para entender onde o sistema falha e o que o cliente sente)
5. **Análise SWOT** — output da skill-analise-swot (forças exploráveis e fraquezas a evitar na promessa)
6. **Estudo de Concorrentes** — output da skill-estudo-de-concorrentes (lacunas de mercado, promessas commoditizadas)

---

## Processo de Execução

### 1. Definir Público-Alvo Prioritário
A partir da Ficha de ICP, confirmar para quem a PUV está sendo construída:
- Para quem essa proposta é realmente desenhada?
- Quem mais se beneficia da solução?
- Quem tende a perceber valor mais rapidamente?

Se o ICP tem variantes (B2B vs B2C), definir PUV separada para cada.

### 2. Identificar a Dor Central
Cruzar o ICP com o diagnóstico de travas para encontrar a dor principal:
- Qual problema gera urgência no ICP?
- O que o cliente tenta resolver repetidamente sem sucesso?
- Qual trava do sistema afeta diretamente a experiência do ICP?

**Fonte primária:** Diagnóstico das travas (qual trava mais impacta o ICP).
**Fonte secundária:** Master-contexto (UDEs declaradas pelo cliente no kickoff).

A dor deve ser específica e verificável — não genérica.

### 3. Definir o Mecanismo da Solução
Descrever como a solução atua para resolver a dor:
- O que a empresa faz de diferente? (buscar nos diferenciais da Matriz CVB)
- Qual é o método, abordagem ou lógica central?
- O cliente consegue entender como funciona em uma frase?

**Regra:** O mecanismo deve ser sustentável pela operação atual. Se o diferencial da CVB depende de esforço heroico (falhou no reality check), não usar na PUV.

### 4. Definir o Resultado Esperado
Descrever a mudança concreta que o cliente pode esperar:
- O que muda na prática ao adotar a solução?
- O resultado é observável ou mensurável?
- Em quanto tempo o cliente percebe valor?

**Conectar ao Forecast:** Se possível, quantificar o resultado (ex: "aumento de X% em Y meses").

### 5. Montar a PUV
Consolidar os três elementos em uma frase ou parágrafo curto:

**Estrutura:**
> Para [ICP], que [dor central], [nome do negócio] oferece [mecanismo da solução], que [resultado esperado].

**Variações aceitas:** a estrutura é referência, não fôrma. A PUV final deve soar natural, não formulaica.

### 6. Validar a PUV — 4 Testes
Submeter a PUV aos quatro testes de qualidade:

| Teste | Pergunta | Aprovado? |
|---|---|---|
| **Clareza** | Alguém externo entende em 10 segundos? | [ ] |
| **Relevância** | Isso realmente importa para o ICP? | [ ] |
| **Diferenciação** | Isso distingue o negócio das alternativas? (verificar contra Estudo de Concorrentes — promessas commoditizadas) | [ ] |
| **Sustentação** | O sistema consegue entregar isso em escala? (verificar contra SWOT — fraquezas) | [ ] |

Se falhar em qualquer teste, revisar o elemento correspondente antes de avançar.

### 7. Documentar e Preparar para Apresentação
Registrar a PUV final em documento com:
- PUV consolidada (frase/parágrafo)
- Elementos de suporte: ICP, dor, mecanismo, resultado
- Testes de validação preenchidos
- Conexões com CVB, SWOT e diagnóstico de travas

Apresentar ao cliente no comitê. A PUV alimenta o discurso comercial, campanhas de marketing e materiais de venda.

---

## Formato de Saída

```markdown
## PUV — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome]

### Proposta Única de Valor
> [PUV consolidada]

### Elementos de Suporte
- **ICP:** [descrição resumida]
- **Dor central:** [dor identificada + trava relacionada]
- **Mecanismo:** [como a solução atua + diferencial da CVB]
- **Resultado:** [mudança concreta esperada + prazo]

### Testes de Validação
- [x] Clareza: [evidência]
- [x] Relevância: [evidência]
- [x] Diferenciação: [evidência vs concorrentes]
- [x] Sustentação: [evidência de capacidade operacional]

### Conexões com Artefatos DR-X
- ICP: [referência ao artefato]
- CVB: [diferenciais utilizados]
- SWOT: [forças exploradas / fraquezas evitadas]
- Travas: [travas endereçadas pela PUV]
```

---

## Exceções e Fallbacks
- **ICP ainda não validado pelo cliente:** construir PUV como draft, marcar como `DRAFT — ICP PENDENTE DE VALIDAÇÃO`. Revisar após validação do ICP.
- **Nenhum diferencial real encontrado na CVB:** a PUV não pode ser construída sobre diferencial inexistente. Registrar como bloqueio e recomendar foco em construção de diferencial antes de definir PUV.
- **Cliente com múltiplos ICPs divergentes:** criar PUV separada para cada ICP. Não tentar uma PUV genérica que "sirva para todos".
- **Dor central não é clara no diagnóstico:** complementar com entrevista direta ao cliente. Registrar que a dor foi definida por entrevista, não por diagnóstico estruturado.
