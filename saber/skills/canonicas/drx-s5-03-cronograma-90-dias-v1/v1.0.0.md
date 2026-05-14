---
slug: drx-s5-03-cronograma-90-dias-v1
name: drx-s5-03-cronograma-90-dias-v1
description: "Constrói o cronograma técnico e executável (90-180 dias) com base na Árvore de Transição dentro do projeto DR-X. Extrai ações, classifica complexidade, identifica dependências e distribui no tempo, garantindo sequência lógica, priorizaçã..."
---

# Cronograma de Implementação (90-180 dias)

## Descrição
Constrói o cronograma técnico e executável (90-180 dias) com base na Árvore de Transição dentro do projeto DR-X. Extrai ações, classifica complexidade, identifica dependências e distribui no tempo, garantindo sequência lógica, priorização por impacto sistêmico e eliminação de achismos.
Ativar quando cronograma, planejamento de implementação, plano de ação, timeline, 90 dias for necessário.

## Quando Usar
- Triggers: "cronograma de implementação", "plano de 90 dias", "montar cronograma", "timeline de ação", "distribuir ações no tempo", "plano de execução"
- **NÃO usar quando:**
  1. A Árvore de Transição não foi concluída — sem ela não há ações para distribuir
  2. A FRT não foi validada — o cronograma parte de uma injeção validada
  3. O cliente não validou a direção no Board 1 — não cronogramar sem validação

## Inputs Necessários
Solicitar antes de iniciar. Se faltar algum, perguntar antes de prosseguir:

1. **Árvore de Transição** — output da skill-arvore-de-transicao (sequência lógica de ações → efeitos → resultados)
2. **FRT** `[VALIDADO]` — output da skill-ltp-frt (injeção e sistema futuro)
3. **PRT** — output da skill-ltp-prt (condições necessárias e obstáculos, se aplicável)
4. **context/business.md** + **context/gtm.md** + **context/constraints.md** `[VALIDADO]` — capacidade operacional, time disponível, restrições
5. **Fluxo de Estratégia** — output da skill-fluxo-de-estrategia (macroetapas e prioridades)
6. **Diagnóstico de travas** — contextos das travas 1-7 (para priorizar por impacto)
7. **Board 1 — Checkpoint de Confirmação** — registro de Quick Wins aprovados (ações já em andamento)

---

## Processo de Execução

### 1. Extrair Ações da Árvore de Transição
Cada ação da Árvore de Transição vira uma linha do cronograma.

**Para cada ação, registrar:**
- Descrição da ação
- Efeito intermediário esperado (da Árvore de Transição)
- Nova condição gerada

**Incluir também:**
- Condições necessárias da PRT (se houver) — viram ações preparatórias
- Quick Wins do Board 1 (se já iniciados — registrar status atual)

### 2. Classificar Tipo de Ação

| Tipo | Característica | Exemplo |
|---|---|---|
| **Estratégica** | Define estrutura do sistema | Reposicionar oferta, redefinir ICP |
| **Tática** | Ajusta funcionamento | Reestruturar funil, criar conteúdos |
| **Operacional** | Execução recorrente | Publicar posts, enviar e-mails |

### 3. Classificar Complexidade
Para cada ação, avaliar:

| Complexidade | Critérios | Duração Base |
|---|---|---|
| **Baixa** | Sem dependências externas, equipe atual domina | 1-2 semanas |
| **Média** | Depende de outro time/sistema, exige aprendizado | 2-4 semanas |
| **Alta** | Mudança estrutural, múltiplas dependências | 4-8 semanas |

**Critérios objetivos para classificar:**
- Quantas áreas estão envolvidas? (1 = baixa, 2-3 = média, 4+ = alta)
- Tem dependência externa? (não = baixa, sim = média/alta)
- Exige mudança cultural ou de processo? (não = baixa/média, sim = alta)

### 4. Identificar Dependências
Para cada ação, perguntar: *"Essa ação pode começar antes da anterior terminar?"*

- Se **não** → **sequencial** (uma depois da outra)
- Se **sim** → **paralelo** (podem rodar juntas)

Registrar as dependências explicitamente (ação X depende de ação Y).

### 5. Priorizar por Impacto Sistêmico
Ações que afetam capacidade de aquisição, conversão e retenção entram primeiro.

**Critérios de priorização:**
1. Endereça trava crítica? (usar diagnóstico — travas com maior score primeiro)
2. Desbloqueia outras ações? (dependências — ações bloqueadoras sobem)
3. Gera resultado visível rápido? (Quick Wins já aprovados no Board 1)

**Conectar com Fluxo de Estratégia:** ações de aquisição (Travas 7-6) antes de monetização (Travas 3-2), a menos que o diagnóstico indique outra prioridade.

### 6. Distribuir no Tempo
Organizar por blocos:

| Período | Foco | Tipos de ação |
|---|---|---|
| **0-30 dias** | Estrutura base + Quick Wins | Ações preparatórias, condições da PRT, ajustes rápidos |
| **30-90 dias** | Otimização | Ações táticas, ajustes de funil, implementação de processos |
| **90-180 dias** | Escala | Ações estratégicas, expansão, consolidação |

**Regras:**
- Não empilhar mais de 3 ações de alta complexidade no mesmo bloco
- Quick Wins do Board 1 entram obrigatoriamente em 0-30 dias
- Ações com dependências externas ganham buffer de 50% na duração

### 7. Montar Cronograma Visual
Consolidar tudo em tabela:

| # | Ação | Tipo | Complexidade | Dependência | Duração | Bloco | Trava endereçada |
|---|---|---|---|---|---|---|---|
| 1 | [ação] | Estratégica | Alta | — | 4 sem | 0-30d | Trava 7 |
| 2 | [ação] | Tática | Média | Ação 1 | 3 sem | 30-90d | Trava 5 |

### 8. Validar com Capacidade Operacional
Cruzar o cronograma com a realidade do cliente (dos arquivos de context/):
- O time disponível consegue executar este volume?
- Há sobreposição excessiva de ações complexas?
- O cronograma é realista ou aspiracional?

Se o cronograma excede a capacidade: remover ou postergar ações de menor impacto. Registrar o que foi adiado e por quê.

---

## Formato de Saída

```markdown
## Cronograma de Implementação — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome]
**Horizonte:** [90 / 180 dias]
**Injeção:** [condição da FRT]

### Bloco 1: Estrutura Base (0-30 dias)
| # | Ação | Tipo | Complexidade | Dependência | Duração | Trava |
|---|---|---|---|---|---|---|
| [linhas] |

### Bloco 2: Otimização (30-90 dias)
| [mesmo formato] |

### Bloco 3: Escala (90-180 dias)
| [mesmo formato] |

### Quick Wins (do Board 1)
| Ação | Status | Resultado |
|---|---|---|
| [ação] | [em andamento / concluído] | [resultado observado] |

### Validação de Capacidade
- Time disponível: [sim/requer ajuste]
- Sobreposição: [ok/reduzir]
- Ações adiadas: [lista, se houver]

### Conexões com Artefatos DR-X
- Árvore de Transição: [ações extraídas]
- PRT: [condições incluídas como ações preparatórias]
- Fluxo de Estratégia: [macroetapas priorizadas]
- Diagnóstico de travas: [priorização por score]
```

---

## Exceções e Fallbacks
- **Árvore de Transição incompleta:** montar cronograma parcial com as ações disponíveis. Marcar como `DRAFT — ÁRVORE DE TRANSIÇÃO INCOMPLETA`. Completar quando a Árvore for finalizada.
- **Horizonte inferior a 90 dias:** ajustar blocos para 0-15d / 15-45d / 45-Xd. Manter a lógica de Estrutura → Otimização → Escala.
- **Capacidade operacional insuficiente para o plano completo:** priorizar por impacto sistêmico e cortar a cauda. Registrar ações removidas como "Horizonte 2" na Matriz de Expansão.
- **Ação sem dependência identificável:** classificar como paralela e alocar no bloco de menor carga.
- **Cliente quer adicionar ações fora do escopo DR-X:** registrar como demanda adicional, não incluir no cronograma principal. Pode ser endereçada na NBO do Board Final.
