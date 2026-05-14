---
slug: drx-s3-03-ltp-frt-injecao-v1
name: drx-s3-03-ltp-frt-injecao-v1
description: "Executa a Fase 4 do Logical Thinking Process (LTP/TOC): a **Árvore de Realidade Futura (Future Reality Tree — FRT)**. A FRT demonstra como o sistema passa a funcionar quando a **injeção** se torna verdadeira — mostrando que a solução é *..."
---

# Skill: LTP — Fase 4: Árvore de Realidade Futura (FRT)

## Descrição
Executa a Fase 4 do Logical Thinking Process (LTP/TOC): a **Árvore de Realidade Futura (Future Reality Tree — FRT)**. A FRT demonstra como o sistema passa a funcionar quando a **injeção** se torna verdadeira — mostrando que a solução é **sistêmica** (remove múltiplos UDEs de uma vez), não pontual.

A FRT responde: *"O que acontece no sistema quando essa condição passa a ser verdadeira?"*

Este skill entrega a cadeia lógica de transformação validada — da injeção até a Meta — pronta para servir de base ao **Plano de Transição** (prioridades de implementação).

## Quando Usar
- Triggers diretos: "FRT", "árvore de realidade futura", "projetar o futuro", "Fase 4 do LTP", "o que acontece quando a injeção for verdadeira", "como o sistema muda"
- Acionado pelo orquestrador `ltp-thinking-process.skill` após injeção validada
- Sempre que uma injeção for definida — independente de ter vindo da Nuvem de Conflitos, diretamente da CRT, do IO Map ou de uma auditoria de dados
- **NÃO usar se:**
  1. A injeção não estiver validada — sem injeção confirmada, a FRT é especulativa
  2. A CRT não estiver com status `[VALIDADO]` — sem UDEs confirmados, não há referência para verificar que a injeção os remove

---

## Inputs Necessários

1. ✅ **Injeção validada** — obrigatório. Pode ter origem em:
   - Nuvem de Conflitos (`nuvem-conflitos.md` com status `[VALIDADO]`)
   - CRT com causa raiz direta (sem conflito estrutural)
   - IO Map — requisito do sistema inexistente identificado como injeção
   - Auditoria de dados — ausência objetiva de estrutura
2. ✅ **CRT com status `[VALIDADO]`** — para verificar que a injeção remove os UDEs identificados
3. ✅ **IO Map com status `[VALIDADO]`** — para verificar que a cadeia de efeitos satisfaz os CSFs e NCs

---

## Estrutura da FRT

A FRT usa **lógica de suficiência** (igual à CRT), mas na direção positiva:

```
[META — Goal do IO Map]
         ↑
[Efeito Desejado N — nível mais próximo da meta]
         ↑
[Efeito Intermediário ...]
         ↑
[Efeito Intermediário ...]
         ↑
[Primeiros Efeitos Positivos]
         ↑
[INJEÇÃO — condição que se torna verdadeira]
```

**Lógica de leitura:** "SE [injeção] → ENTÃO [efeito 1]. SE [efeito 1] (E [condição existente]) → ENTÃO [efeito 2]..."

---

## Processo de Execução

### Step 0 — Leitura de Contexto

Antes de qualquer output:
1. Leia a Nuvem (se existir) — extraia a injeção validada e o contexto do conflito resolvido
2. Leia a CRT validada — extraia todos os UDEs; eles serão a lista de verificação da FRT
3. Leia o IO Map — extraia Goal, CSFs e NCs; a FRT deve mostrar como o sistema os satisfará
4. Leia o arquivos de context/ — para contextualizar as condições existentes do sistema

---

### Etapa 1 — Posicionamento Preciso da Injeção

**Objetivo:** Declarar a injeção com precisão como **condição de estado no presente** — não como ação.

**Formatos corretos:**
- ✅ "ICP está definido e aplicado em todas as frentes de aquisição"
- ✅ "Processo comercial estruturado existe e é seguido pelo time"
- ✅ "Capacidade de entrega é dimensionada antes de escalar marketing"
- ❌ "Definir o ICP" (ação, não estado)
- ❌ "O time vai seguir o processo" (futuro incerto, não condição de estado)

**Verificar:** a injeção está dentro do **span of control** do dono do sistema? (definido no IO Map Fase 0)
- Se sim → avançar
- Se não → sinalizar ao usuário que a injeção depende de fatores externos; ajustar ou adicionar injeção de segundo nível

---

### Etapa 2 — Projeção dos Primeiros Efeitos

**Objetivo:** Identificar o que muda **imediatamente** quando a injeção se torna verdadeira.

**Pergunta estruturante:**
*"Se [injeção] for verdadeira agora, o que muda imediatamente no comportamento ou resultado do sistema?"*

**Construção das primeiras setas:**
```
SE [injeção] → ENTÃO [primeiro efeito positivo]
```

**Validar cada seta:**
1. O efeito é consequência **lógica e suficiente** da injeção? (não é esperança)
2. A injeção sozinha (ou com condição existente declarada) produz esse efeito?
3. O efeito é observável e verificável?

**Entidades condicionantes:** quando a injeção sozinha não é suficiente para o efeito, declarar explicitamente a condição existente que precisa estar presente:
```
SE [injeção] E [condição existente no sistema] → ENTÃO [efeito]
```

---

### Etapa 3 — Conexão aos UDEs da CRT (Substituição)

**Objetivo:** Para cada UDE da CRT, mostrar que ele deixa de existir ou é substituído por um efeito desejado quando a injeção é verdadeira.

**Pergunta para cada UDE:**
*"[UDE-X] ainda existiria se a injeção fosse verdadeira?"*
- Não → identificar qual efeito positivo da FRT o substitui → conectar na cadeia
- Parcialmente → identificar o que ainda seria necessário além da injeção → candidato a injeção de segundo nível

**Tabela de substituição:**

| UDE (CRT) | Efeito Substituto (FRT) | Status |
|-----------|------------------------|--------|
| UDE-01: [declaração] | [efeito desejado correspondente] | ✓ eliminado pela injeção |
| UDE-02: [declaração] | [efeito desejado correspondente] | ⚠️ exige injeção adicional |
| ... | ... | ... |

UDEs não eliminados pela injeção principal são candidatos a **injeções de segundo nível** — registrar mas não bloquear a FRT por isso.

---

### Etapa 4 — Expansão da Cadeia de Efeitos

**Objetivo:** Continuar a cadeia até alcançar os CSFs e a Meta do IO Map.

**Pergunta de expansão:**
*"Se [efeito atual] for verdadeiro, o que melhora a seguir no sistema?"*

Continuar até que a cadeia chegue a estados que reconhecivelmente satisfazem os CSFs do IO Map:
- "Previsibilidade de receita aumenta" → satisfaz CSF "Receita suficiente e previsível"
- "Taxa de conversão estabiliza em patamar mensurável" → satisfaz NC correspondente
- etc.

**Teste de completude:**
Verificar cada CSF do IO Map: a cadeia da FRT chega até ele?
- Sim → CSF coberto pela FRT
- Não → há uma lacuna — investigar se falta uma injeção adicional ou se o CSF está além do escopo desta injeção

---

### Etapa 5 — Identificação de Ramos Negativos (Negative Branches)

**Objetivo:** Verificar se a injeção pode gerar **efeitos colaterais indesejados** — novos problemas criados pela própria solução.

**Pergunta de verificação:**
*"Se [injeção ou efeito positivo X] for verdadeiro, isso pode causar algum problema novo no sistema?"*

**Exemplos clássicos de ramos negativos:**
- Aumentar conversão sem dimensionar capacidade de entrega → gera gargalo operacional novo
- Estruturar processo comercial rígido → pode gerar perda de flexibilidade para casos atípicos
- Escalar aquisição antes de resolver retenção → amplifica o churn

**Para cada ramo negativo identificado:**
1. Declarar o efeito colateral
2. Identificar se há uma **ação preventiva** (trim — aparar o ramo antes que aconteça) ou uma **injeção de segundo nível** que o resolve
3. Incorporar na FRT como desvio a ser gerenciado

**Regra:** Ramos negativos não invalidam a FRT — eles aprimoram o plano. Registrá-los é mais valioso do que ignorá-los.

---

### Etapa 6 — Validação Final

**Objetivo:** Confirmar que a FRT demonstra que o sistema alcança a Meta quando a injeção é verdadeira.

**Teste de completude — verificar antes de apresentar:**
- [ ] A injeção está no nível mais baixo da cadeia (condição raiz)
- [ ] Cada seta sobrevive ao teste "SE → ENTÃO" lógico
- [ ] Todos (ou a maioria) os UDEs da CRT têm um efeito substituto na FRT
- [ ] A cadeia chega até o Goal declarado no IO Map
- [ ] Ramos negativos foram identificados e tratados

**Perguntas de validação ao usuário:**
> 1. "A cadeia de efeitos — de baixo para cima — faz sentido lógico? Há alguma seta que parece um salto sem justificativa?"
> 2. "Algum UDE da lista ainda existiria mesmo com a injeção em vigor? Há algo que a injeção não resolve?"
> 3. "Os efeitos colaterais identificados (ramos negativos) são reconhecíveis? Há outros que a análise não capturou?"
> 4. "Ao chegar no topo da cadeia, você reconhece que o sistema estaria produzindo os resultados da Meta?"

Aguardar confirmação. Incorporar ajustes. Avançar apenas com validação explícita.

---

## Regras de Ouro

1. **NÃO construir FRT com injeção não validada** — injeção sem validação gera FRT especulativa, não analítica
2. **NÃO pular a verificação de ramos negativos** — ignorar efeitos colaterais é o erro mais comum de implementação
3. **NÃO formular entidades da FRT como ações** — apenas estados (condições que passam a ser verdadeiras)
4. **NÃO assumir que a injeção principal resolve 100% dos UDEs** — registrar os UDEs não cobertos como candidatos a injeções adicionais
5. **NÃO avançar para o Plano de Transição sem FRT validada** — o plano de ação deve ser derivado da cadeia causal, não de intuição
6. **A FRT não é um plano de ação** — é a demonstração lógica de que o plano funcionará; o plano vem depois

---

## Formato de Saída Obrigatório

```markdown
## Árvore de Realidade Futura — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome]
**Injeção base:** [declaração da injeção validada]
**Origem da injeção:** [Nuvem de Conflitos / CRT direta / IO Map / Auditoria]

---

### Cadeia de Efeitos — FRT

```
[GOAL: declaração do IO Map]
         ↑
[Efeito Desejado N: estado que satisfaz CSF X]
         ↑
[Efeito Desejado N-1: estado intermediário]
         ↑
[Efeito Desejado N-2: estado intermediário]
         ↑
[Primeiros Efeitos Positivos]
         ↑
[INJEÇÃO: condição de estado validada]
```

**Leitura:** "SE [injeção] → ENTÃO [primeiro efeito]. SE [primeiro efeito] (E [condição existente]) → ENTÃO [segundo efeito]..."

---

### Substituição de UDEs

| UDE (CRT) | Efeito Substituto (FRT) | Status |
|-----------|------------------------|--------|
| UDE-01: [declaração] | [efeito desejado] | ✓ eliminado |
| UDE-02: [declaração] | [efeito desejado] | ✓ eliminado |
| UDE-0X: [declaração] | [não endereçado diretamente] | ⚠️ injeção adicional necessária |

---

### Cobertura dos CSFs (IO Map)

| CSF | Endereçado na FRT? | Efeito da FRT que o satisfaz |
|-----|-------------------|------------------------------|
| CSF 1: [declaração] | ✓ | [efeito correspondente na cadeia] |
| CSF 2: [declaração] | ✓ | [efeito correspondente na cadeia] |
| CSF N: [declaração] | ⚠️ | [fora do escopo desta injeção] |

---

### Ramos Negativos Identificados

**Ramo Negativo 1:**
- Trigger: SE [injeção/efeito X] → PODE causar [efeito indesejado]
- Prevenção (Trim): [ação preventiva ou injeção de segundo nível]

**Ramo Negativo 2:** *(se houver)*
- Trigger: [...]
- Prevenção: [...]

*(Se nenhum ramo negativo for identificado, registrar: "Nenhum ramo negativo identificado nesta análise.")*

---

### Injeções Adicionais Necessárias

> UDEs não cobertos pela injeção principal:
> - UDE-0X: [declaração] → Injeção adicional sugerida: [condição]
>
> *(Se todos os UDEs foram cobertos, registrar: "Injeção principal cobre todos os UDEs identificados na CRT.")*

---

> **FRT Status:** `[AGUARDANDO VALIDAÇÃO]`
```

### Após validação confirmada

```
> **FRT Status:** `[VALIDADO PELO USUÁRIO]`
> **Injeção validada:** [resumo em 1 linha]
> **Ramos negativos a monitorar:** [lista resumida]
> **Próximo passo:** Plano de Transição — priorizar injeções e definir sequência de implementação
```

Salvar ou atualizar o arquivo `frt.md` do cliente com o output completo.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output (injeção validada + ramos negativos identificados + próximo passo).
