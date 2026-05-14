---
slug: drx-s5-01-ltp-prt-arvore-pre-requisitos-v1
name: drx-s5-01-ltp-prt-arvore-pre-requisitos-v1
description: "Identifica obstáculos que podem impedir a implementação da injeção e transforma barreiras em condições necessárias, utilizando a Árvore de Pré-Requisitos (PRT) do Logical Thinking Process. A PRT garante que a injeção não falhe por falta..."
---

# Árvore de Pré-Requisitos (PRT)

## Descrição
Identifica obstáculos que podem impedir a implementação da injeção e transforma barreiras em condições necessárias, utilizando a Árvore de Pré-Requisitos (PRT) do Logical Thinking Process. A PRT garante que a injeção não falhe por falta de preparo do sistema, preparando o terreno para a Árvore de Transição.
Ativar quando Logical Thinking Process, pré-requisitos, obstáculos, implementação, injeção for necessário.

## Quando Usar
- Triggers: "árvore de pré-requisitos", "PRT", "obstáculos da injeção", "o que pode impedir", "barreiras de implementação", "pré-requisitos para a mudança"
- **NÃO usar quando:**
  1. A injeção é simples e direta — ir direto para a Árvore de Transição
  2. Não há resistência do cliente nem obstáculos estruturais — a PRT é opcional
  3. A FRT não foi concluída — sem FRT, não há injeção validada para analisar

- **USAR obrigatoriamente quando:**
  - A injeção é estrutural ou complexa
  - O cliente demonstra resistência ("não dá para fazer agora")
  - Faltam recursos, pessoas ou sistemas
  - A mudança envolve várias áreas

## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

1. **FRT** `[VALIDADO]` — output da skill-ltp-frt (injeção validada + sistema funcionando com a injeção)
2. **CRT** `[VALIDADO]` — output da skill-ltp-crt (causa-raiz e contexto do problema)
3. **IO Map** `[VALIDADO]` — output da skill-ltp-iomap (Goal e CSFs do sistema)
4. **context/business.md** + **context/gtm.md** + **context/constraints.md** `[VALIDADO]` — contexto operacional do cliente (recursos, time, sistemas)
5. **Nuvem de Conflitos** — output da skill-ltp-nuvem (se houver conflito estrutural já trabalhado)

---

## Processo de Execução

### 1. Posicionar a Injeção
Relembrar a condição definida na FRT que precisa se tornar verdadeira.

**Exemplo:** *"ICP definido e aplicado"*

Registrar: a injeção, o estado futuro desejado (da FRT) e o estado atual (da CRT).

### 2. Identificar Obstáculos
Perguntar ao cliente: *"O que pode impedir isso de acontecer?"*

Registrar obstáculos reais, não desculpas. Fontes de obstáculos:
- **Pessoas:** time não tem conhecimento, resistência cultural, falta de responsável
- **Processos:** falta processo, processo atual conflita com a mudança
- **Ferramentas:** falta ferramenta, sistema não suporta
- **Recursos:** falta budget, falta tempo, falta prioridade
- **Externo:** dependência de terceiros, regulação, mercado

**Usar context/constraints.md** para verificar restrições operacionais já conhecidas do kickoff.

### 3. Validar Obstáculos
Para cada obstáculo, perguntar: *"Isso realmente impediria a implementação?"*

- Se **sim**: manter
- Se **não**: descartar (era desculpa, não obstáculo)
- Se **parcialmente**: registrar como risco, não obstáculo

Manter apenas obstáculos que efetivamente bloqueariam a implementação.

### 4. Definir Condições Necessárias
Para cada obstáculo validado, perguntar: *"O que precisa existir para que isso deixe de ser um impedimento?"*

Registrar em tabela:

| Obstáculo | Condição Necessária |
|---|---|
| Time não sabe fazer | Treinamento estruturado |
| Falta CRM | Sistema implementado |
| Falta dados | Métricas definidas |

A condição necessária deve ser **acionável** (algo que pode ser feito), não abstrata.

### 5. Conectar Obstáculos Entre Si
Alguns obstáculos dependem de outros. Construir relações lógicas:
- O obstáculo A precisa ser resolvido antes de B?
- Resolver C automaticamente resolve D?
- Existem obstáculos em paralelo (independentes)?

Organizar em sequência de resolução (o que vem primeiro, o que vem depois).

### 6. Validar com o Cliente
Perguntar: *"Se essas condições existirem, a implementação fica viável?"*

- Se **sim**: a PRT está validada. Avançar para a Árvore de Transição.
- Se **não**: há obstáculo oculto. Voltar ao passo 2 e perguntar *"O que mais poderia impedir?"*
- Se **parcialmente**: refinar as condições necessárias.

---

## Formato de Saída

```markdown
## PRT — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome]
**Injeção:** [condição definida na FRT]

### Obstáculos Identificados e Condições Necessárias

| # | Obstáculo | Categoria | Condição Necessária | Depende de |
|---|---|---|---|---|
| 1 | [obstáculo] | [Pessoas/Processo/Ferramenta/Recurso/Externo] | [condição acionável] | — |
| 2 | [obstáculo] | [categoria] | [condição] | Obstáculo 1 |
| 3 | [obstáculo] | [categoria] | [condição] | — |

### Sequência de Resolução
1. [condição que precisa existir primeiro]
2. [condição que depende da anterior]
3. [condições independentes — podem ser paralelas]

### Validação
**Cliente confirmou viabilidade com condições?** [Sim/Não/Parcial]
**Observações:** [registro de ressalvas ou obstáculos ocultos]

### Conexões com Artefatos DR-X
- FRT: [injeção de referência]
- CRT: [causa-raiz relacionada]
- Master-contexto: [restrições já conhecidas]
```

---

## Exceções e Fallbacks
- **Nenhum obstáculo relevante identificado:** a PRT não é necessária. Registrar que "não foram identificados obstáculos estruturais" e avançar direto para a Árvore de Transição.
- **Cliente não consegue articular obstáculos:** usar o arquivos de context/ e o diagnóstico de travas para sugerir potenciais barreiras. Apresentar como hipóteses e validar.
- **Obstáculo depende de decisão de terceiro (ex: investidor, sócio ausente):** registrar como obstáculo externo com prazo de resolução. Não travar a PRT inteira — tratar como condição em paralelo.
- **Condição necessária é inviável (ex: "contratar 10 pessoas" quando não há budget):** escalar como restrição estratégica. Pode exigir rever a injeção ou buscar alternativa na Nuvem de Conflitos.
