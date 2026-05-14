---
slug: drx-s3-01-ltp-crt-v1
name: drx-s3-01-ltp-crt-v1
description: "Executa a Fase 2 do Logical Thinking Process (LTP/TOC): a **Árvore de Realidade Atual (Current Reality Tree — CRT)**. A CRT mapeia os efeitos indesejados (UDEs) do sistema, traça as relações de causa e efeito entre eles e identifica a(s)..."
---

# Skill: LTP — Fase 2: Árvore de Realidade Atual (CRT)

## Descrição
Executa a Fase 2 do Logical Thinking Process (LTP/TOC): a **Árvore de Realidade Atual (Current Reality Tree — CRT)**. A CRT mapeia os efeitos indesejados (UDEs) do sistema, traça as relações de causa e efeito entre eles e identifica a(s) causa(s) raiz estrutural(is) que sustentam o cenário atual — revelando a **trava do sistema** (a restrição que impede o alcance da Meta).

A CRT responde: *"O que está acontecendo hoje no sistema que impede o alcance da Meta?"*

Este skill entrega um diagnóstico validado com causa raiz identificada, pronto para servir de input à Fase 3 (Nuvem de Conflitos) ou, quando o conflito for evidente sem ambiguidade, diretamente à Fase 4 (FRT).

## Quando Usar
- Triggers diretos: "CRT", "árvore de realidade atual", "mapear UDEs", "identificar trava", "causa raiz", "Fase 2 do LTP", "o que trava o sistema"
- Acionado pelo orquestrador `ltp-thinking-process.skill` após IO Map validado
- Quando o cliente descreve vários problemas mas não enxerga a estrutura conectando todos eles
- **NÃO usar se:**
  1. O IO Map do cliente não existir ou não estiver com status `[VALIDADO]` — executar `skill-ltp-iomap.md` primeiro
  2. Não houver nenhum dado de contexto sobre o cliente (arquivos context/, transcrições ou anotações) — a CRT precisa de fatos, não de suposições

---

## Inputs Necessários

Verificar antes de iniciar. Se algum item obrigatório faltar, informar o usuário antes de prosseguir:

1. ✅ **IO Map com status `[VALIDADO]`** — obrigatório. Extrair: Goal, CSFs e NCs
2. ✅ **context/business.md** + **context/gtm.md** + **context/constraints.md** — obrigatório. Fonte de UDEs declarados no kickoff, restrições operacionais e contexto do sistema
3. ⚙️ **Outputs de diagnósticos anteriores** *(input primário quando disponíveis)*
   - **Diagnósticos de Trava:** `clientes/[cliente]/trava-[1-7]-*.md`
     → Extrair: UDEs por frente, consolidação causal, determinação preliminar de cada trava
   - **Fluxo de Receita:** `clientes/[cliente]/fluxo-receita.md`
     → Extrair: hipótese de restrição principal, análise de gargalos, visão sistêmica TOC e seção "Pontos de Atenção para a CRT"
   - Quando disponíveis, são a fonte mais rica — coletados sistematicamente antes da CRT
   - Se nenhum foi executado ainda: usar arquivos `context/` + IO Map como fallback
4. ⚙️ **Transcrições ou anotações de reuniões** *(complemento)* — declarações literais do cliente

> **Regra de ouro:** O que já está documentado **não** precisa ser recoletado. Use os dados existentes como ponto de partida e sinalize ao usuário o que foi reaproveitado vs. derivado.

---

## Processo de Execução

### Step 0 — Leitura de Contexto

Antes de qualquer output:
1. Leia o `io-map.md` validado — extraia: Goal, lista completa de CSFs e NCs
2. Leia os arquivos `context/business.md`, `context/gtm.md` e `context/constraints.md` — extraia: UDEs já listados, restrições operacionais, sintomas declarados
3. **Verifique quais diagnósticos anteriores existem na pasta do cliente** (`clientes/[cliente]/`):
   - Arquivos `trava-[N]-*.md` → se existirem, leia todos; extraia UDEs, consolidações causais, determinações preliminares
   - Arquivo `fluxo-receita.md` → se existir, leia; priorize as seções "Hipótese de Restrição Principal" e "Pontos de Atenção para a CRT"
4. Monte internamente a **lista preliminar de UDEs** agregando todas as fontes disponíveis
5. Identifique quais NCs do IO Map estão **visivelmente não satisfeitas** na realidade atual — cada gap é candidato a UDE adicional

**Declare o contexto de entrada antes de prosseguir:**
> ⚠️ **Contexto de entrada desta CRT:**
> - Diagnósticos de trava disponíveis: [N de 7] — [listar quais / "nenhum"]
> - Fluxo de receita disponível: [Sim / Não]
> - Master contexto: [Sim]
>
> *[Se contexto incompleto:]* Esta CRT será construída com contexto parcial. Os UDEs e a hipótese de trava refletem os dados disponíveis — o output é válido para o contexto fornecido, mas pode ser revisitado e aprofundado após a execução dos diagnósticos faltantes.

---

### Etapa 1 — Coleta dos Efeitos Indesejados (UDEs)

**Objetivo:** Levantar 8 a 15 UDEs que representem sintomas reais, verificáveis e recorrentes do sistema.

**Fontes de UDEs (em ordem de prioridade):**
1. **Outputs de diagnósticos anteriores** (quando disponíveis):
   - Skills de trava (T1–T7): UDEs coletados por frente do fluxo de receita + consolidação causal + determinação preliminar
   - Fluxo de Receita: gargalos, visão sistêmica TOC e hipótese de restrição → UDEs de natureza operacional/estrutural
2. Declarações literais do cliente em reunião registradas nos arquivos de context/ (ex: *"a gente vende e depois não tem recorrência"*)
3. Dados e métricas negativos nos arquivos de context/ (concentração de risco, gargalos descritos, métricas ausentes)
4. Gaps nas NCs do IO Map — cada NC que claramente não está sendo satisfeita na operação atual é um UDE adicional

**Formato correto de UDE:**
- Descreve um estado negativo **observável** no presente — não uma ação, não uma ausência de solução
- Verificável: alguém de fora poderia confirmar por observação ou dado
- Sem solução embutida: "ausência de processo de pós-venda" é uma NC não satisfeita — não é UDE; "clientes não recompram após a entrega" é UDE
- Sem julgamento de causa: o UDE descreve *o que acontece*, não *por que* acontece

**Exemplos de UDE bem formulado:**
- ✅ "Leads chegam mas não convertem em proposta"
- ✅ "75% da receita depende de um único cliente"
- ✅ "Vendedor com maior margem recebe comissão menor do que vendedor de menor margem"
- ❌ "Não existe processo de pós-venda" (solução embutida — reformule para o efeito observável)
- ❌ "O time não é comprometido" (julgamento de pessoa — reformule para estrutura)

**Teste de validação para cada UDE (aplicar os três):**
1. *"Isso acontece com frequência ou sistematicamente?"* — se sim, manter
2. *"Se isso não acontecesse, o resultado do sistema melhoraria?"* — se sim, manter
3. *"Isso é verificável — alguém externo poderia confirmar?"* — se não, reformular

Registrar cada UDE com identificador:
```
UDE-01: [declaração observável, presente, sem causa embutida]
UDE-02: ...
```

---

### Etapa 2 — Mapeamento de Causas e Efeitos

**Objetivo:** Conectar os UDEs em cadeias lógicas usando lógica de suficiência (≠ lógica de necessidade do IO Map).

**Regra da lógica de suficiência:**
- "SE [causa] ENTÃO [efeito]" — a causa, sozinha ou combinada com uma condição existente no sistema, é suficiente para produzir o efeito
- Nunca: "PARA que [efeito] exista, precisamos de [causa]" — isso é necessidade (IO Map)

**Construção do mapa — pergunta para cada par de UDEs:**
*"UDE-X acontece PORQUE UDE-Y acontece?"*
- Sim → traçar seta: UDE-Y → UDE-X
- Parcialmente → identificar entidade intermediária que conecta os dois

**Entidades intermediárias:** quando dois UDEs não se conectam diretamente, inserir uma entidade causal entre eles. Pode ser outro UDE ou um fato neutro do sistema (ex: "estrutura de incentivo premia componentes sobre projetos").

**Validação de cada seta — aplicar os três testes:**
1. **Existência:** a causa existe de fato no sistema? (não é hipotética)
2. **Causalidade real:** a causa *sozinha* (ou com condição existente declarada) produz o efeito — ou é apenas correlação temporal?
3. **Leitura em voz alta:** "porque [causa], [efeito]" — soa lógico para alguém de fora do sistema?

Se algum teste falhar, a entidade ou a seta precisam ser reformulados.

---

### Etapa 3 — Identificação de Efeitos Convergentes

**Objetivo:** Encontrar nós do mapa onde múltiplas cadeias convergem para a mesma entidade.

**Sinal de trava:** quando uma entidade explica **3 ou mais UDEs** diferentes, ela é candidata à causa raiz / trava sistêmica.

**Pergunta-chave:** *"Se corrigirmos este ponto, quantos desses UDEs deixam de existir ou perdem sua força?"*

Quando um nó responder "muitos" → destacar como **ponto de alavancagem**.

---

### Etapa 4 — Distinção Causa vs. Sintoma

**Teste para cada entidade candidata a causa raiz:**
*"Isso acontece PORQUE outra coisa (estrutural) está acontecendo?"*
- Sim → é efeito/sintoma → posicioná-lo acima na cadeia e continuar descendo
- Não → é candidato a causa raiz

**Armadilha frequente:** UDEs que parecem causas mas são efeitos de algo mais profundo.
- *"O time não faz follow-up"* → parece causa → mas acontece PORQUE não existe processo estruturado de follow-up → a causa raiz é estrutural
- *"As vendas não crescem"* → é sempre efeito, nunca causa raiz

---

### Etapa 5 — Identificação das Causas Raízes

**Causas raízes legítimas são sempre estruturais:**
- Falha de processo (processo inexistente, incompleto ou mal definido)
- Falha de definição estratégica (ICP não definido, meta sem decomposição, posicionamento ausente)
- Falha de priorização (recursos e atenção alocados no lugar errado)
- Falha de incentivo (estrutura que recompensa comportamento contrário à meta)
- Gargalo de capacidade (recurso físico ou de competência que limita todo o sistema)

**NÃO são causas raízes:**
- *"As pessoas não fazem X"* — pessoas se comportam conforme o sistema permite e recompensa; a causa é a estrutura
- Eventos externos pontuais — a CRT mapeia padrões estruturais, não exceções

**Número ideal:** 1 a 3 causas raízes. Se mais de 3 emergirem, provavelmente algumas são intermediárias — subir um nível de abstração.

---

### Etapa 6 — Formulação da Hipótese de Trava

Com base nas causas raízes, formular a **hipótese de trava do sistema**:

```
HIPÓTESE DE TRAVA:
[Declaração da condição estrutural que, se removida ou corrigida,
eliminaria a maioria dos UDEs e desbloquearia o caminho para a Meta.]
```

Esta hipótese é o input para a próxima fase:
- Se a trava envolve um conflito estrutural (duas ações legítimas que se bloqueiam mutuamente) → Nuvem de Conflitos
- Se a injeção é direta (causa raiz com solução clara sem trade-off) → FRT direto

---

### Etapa 7 — Validação com o Usuário

Apresentar ao usuário, tudo de uma vez:
1. Lista de UDEs com indicação de fonte (arquivos de context/ / derivado)
2. Mapa de causa e efeito em formato textual hierárquico
3. Causas raízes identificadas
4. Hipótese de trava

**Perguntas de validação:**
> 1. "Algum UDE importante está faltando ou foi formulado incorretamente?"
> 2. "Alguma relação de causa-efeito parece forçada ou não reflete a realidade da operação?"
> 3. "A causa raiz identificada ressoa com o que vocês vivem no dia a dia? Há algo estrutural mais profundo que a análise não capturou?"
> 4. "Se essa causa raiz deixasse de existir, você acredita que a maioria desses problemas desapareceria?"

Aguardar confirmação. Incorporar ajustes. Só avançar após validação explícita.

---

## Regras de Ouro

1. **NÃO iniciar sem IO Map `[VALIDADO]`** — sem padrão de desempenho ideal, UDEs são opiniões, não desvios mensuráveis
2. **NÃO formular UDEs com solução embutida** — reformular para o efeito observável negativo
3. **NÃO usar "as pessoas" como causa raiz** — investigar a estrutura que gera o comportamento
4. **NÃO avançar para Nuvem ou FRT sem validação explícita** da hipótese de trava
5. **NÃO ultrapassar 15 UDEs** — acima disso, agrupar ou elevar abstração
6. **NÃO recoletaar dados já presentes** nos arquivos `context/` ou IO Map — reutilize e sinalize a fonte

---

## Formato de Saída Obrigatório

```markdown
## Árvore de Realidade Atual — [Nome do Cliente]
**Data:** [data] | **Consultor:** [nome]
**IO Map base:** [Goal do IO Map validado]

---

### UDEs Identificados

| # | UDE | Fonte | Validação |
|---|-----|-------|-----------|
| UDE-01 | [declaração observável, presente] | arquivos de context/ | ✓ |
| UDE-02 | [declaração observável, presente] | derivado (gap NC 2.1) | pendente |
| ... | ... | ... | ... |

*Total: [N] UDEs*

---

### Mapa de Causa e Efeito

```
[Meta bloqueada — estado topo]
         ↑
[UDE-05: efeito mais visível]
         ↑
[UDE-03: efeito intermediário]          [UDE-04: efeito paralelo]
         ↑                                        ↑
[UDE-01: efeito convergente] ←————————————————————
         ↑
[Entidade intermediária: condição estrutural]
         ↑
[CAUSA RAIZ: declaração estrutural]
```

**Leitura:** "SE [causa raiz] ENTÃO [entidade intermediária] (dado que [condição existente]).
SE [entidade intermediária] ENTÃO [UDE-01]. SE [UDE-01] ENTÃO [UDE-03] E [UDE-04]."

---

### Causas Raízes Identificadas

**Causa Raiz 1:** [nome / rótulo]
- Declaração: [condição estrutural no presente]
- UDEs explicados: UDE-01, UDE-03, UDE-07

**Causa Raiz 2:** [nome / rótulo] *(se houver)*
- Declaração: [condição estrutural no presente]
- UDEs explicados: UDE-02, UDE-06

---

### Hipótese de Trava do Sistema

> **TRAVA:** [declaração da restrição estrutural central]
>
> *Efeito esperado se removida:* [declaração dos UDEs que deixariam de existir]
> *Conexão com o IO Map:* [qual CSF ou NC passaria a ser satisfeita]

---

### Pontos de Atenção sobre o Contexto desta CRT

*Preencher apenas se algum input ideal estava ausente no momento da execução:*

- [ ] Diagnósticos de trava não executados: [listar — ex: T2, T4, T6]
- [ ] Fluxo de receita não executado

> *Esses diagnósticos podem revelar UDEs adicionais ou alterar a hipótese de trava. Esta CRT é válida para o contexto disponível — recomenda-se revisitar após a execução dos itens acima.*

*(Se todos os inputs estavam disponíveis: omitir esta seção ou registrar "Todos os inputs disponíveis — CRT construída com contexto completo.")*

---

### Próximo Passo Recomendado

- [ ] **Há conflito estrutural?** (duas ações legítimas que se bloqueiam) → Nuvem de Conflitos (`skill-ltp-nuvem.md`)
- [ ] **Injeção direta e clara?** (causa raiz com solução sem trade-off) → FRT (`skill-ltp-frt.md`)

---

> **CRT Status:** `[AGUARDANDO VALIDAÇÃO]`
```

### Após validação confirmada

Atualizar o status e registrar:
```
> **CRT Status:** `[VALIDADO PELO USUÁRIO]`
> **Trava confirmada:** [resumo em 1 linha]
> **Próximo passo:** [Nuvem de Conflitos / FRT] — `skill-ltp-[nuvem/frt].md`
```

Salvar ou atualizar o arquivo `crt.md` do cliente com o output completo.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output (causas raízes identificadas + hipótese de trava confirmada).
