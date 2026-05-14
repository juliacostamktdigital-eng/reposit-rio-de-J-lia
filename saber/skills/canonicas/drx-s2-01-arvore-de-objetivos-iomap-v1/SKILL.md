---
slug: drx-s2-01-arvore-de-objetivos-iomap-v1
name: drx-s2-01-arvore-de-objetivos-iomap-v1
description: "Executa as duas primeiras fases do Logical Thinking Process (LTP/TOC): **Definição do Sistema** (Fase 0) e **construção do IO Map** (Fase 1). O IO Map é uma árvore de lógica de necessidade que estabelece o padrão de desempenho desejado d..."
---

# Skill: LTP — Fase 0+1: Definição do Sistema & IO Map

## Descrição
Executa as duas primeiras fases do Logical Thinking Process (LTP/TOC): **Definição do Sistema** (Fase 0) e **construção do IO Map** (Fase 1). O IO Map é uma árvore de lógica de necessidade que estabelece o padrão de desempenho desejado do sistema — o benchmark contra o qual toda a análise subsequente (CRT, EC, FRT) será feita. Sem IO Map, os UDEs não podem ser identificados com rigor: seriam apenas opiniões.

Este skill entrega um IO Map validado pelo usuário, pronto para servir de input à Fase 2 (Current Reality Tree).

## Quando Usar
- Triggers diretos: "IO Map", "fazer IO Map", "montar IO Map", "Fase 1 do LTP", "definir o sistema"
- Acionado pelo orquestrador `ltp-thinking-process.skill` ao iniciar o LTP
- Também quando o usuário quer identificar os Critical Success Factors de um sistema antes de diagnosticar problemas
- NÃO usar se o IO Map já existir e estiver com status `[VALIDADO]` — nesse caso, use-o diretamente como input para a CRT

## Inputs Necessários

**Verificar primeiro:** existem os arquivos `context/` no projeto com status `[VALIDADO]`?

Inputs de contexto para esta skill:
1. **context/business.md** — modelo de negócio, revenue streams, capacidade
2. **context/gtm.md** — canais, funil, ICP, ciclo de vendas, mercado

- **Se sim:** leia-os. Extraia: sistema, Goal declarado, ICP, restrições mencionadas, horizonte estratégico. **Não recolete o que já foi coletado.**
- **Se não:** faça as seguintes perguntas de uma vez antes de prosseguir:
  1. Qual é o sistema que estamos analisando? (empresa, departamento, processo?)
  2. Quem é o "dono" deste sistema — quem tem decisão sobre ele?
  3. Qual é o resultado que este sistema deveria estar produzindo mas não está?
  4. O que está claramente dentro do seu controle direto vs. o que você influencia mas não controla?

---

## Processo de Execução

### Fase 0: Definição do Sistema

**Objetivo:** Estabelecer os limites do sistema antes de qualquer análise. Um IO Map sem limites claros é ambíguo e gera CSFs genéricos demais.

**Step 0.1 — Leitura do contexto**
- Se os arquivos `context/` existirem: extraia os elementos abaixo diretamente dos documentos (`context/business.md` e `context/gtm.md`)
- Se não existirem: use as respostas coletadas nos Inputs

**Step 0.2 — Construir a declaração do sistema**

Monte o bloco de contexto com:
- **Sistema:** [nome e escopo do sistema]
- **Dono:** [quem tem span of control — decisão direta]
- **Sphere of influence:** [o que o dono pode influenciar mas não controla diretamente]
- **Goal declarado:** [o resultado final que o sistema existe para alcançar]
- **Limites:** [o que está dentro vs. fora do sistema]

**Step 0.3 — Apresentar e confirmar**

Exiba o bloco de contexto ao usuário e pergunte: "Este recorte do sistema está correto? Algo fora do limite que deveria estar dentro, ou vice-versa?"

Aguarde confirmação antes de avançar para a Fase 1. Não continue sem isso.

---

### Fase 1: Construção do IO Map

**Objetivo:** Derivar o padrão de desempenho ideal do sistema como uma hierarquia de condições necessárias.

**Lógica de base:** O IO Map usa **lógica de necessidade** (≠ lógica de suficiência da CRT).
- Leia de baixo para cima: "Para [Goal], precisamos de [CSF1] **E** [CSF2] **E** [CSF3]"
- Leia de cima para baixo: "[Goal] requer [CSF1], que por sua vez requer [NC1] **E** [NC2]"

**Step 1.1 — Confirmar ou refinar o Goal**

O Goal deve ser:
- Uma condição desejada no presente ("A empresa gera lucro crescente e sustentável")
- Único e no topo da hierarquia
- Teste: "Se este sistema funcionasse perfeitamente, qual seria o resultado final?"

Atenção: o que parece ser Goal frequentemente é CSF. Se dois itens parecem igualmente fundamentais, teste: se trocar os papéis (um vira Goal, o outro vira CSF), qual faz mais sentido? Escolha o que tem primazia absoluta como Goal.

**Step 1.2 — Derivar os Critical Success Factors (CSFs)**

Pergunte: "Quais são as 3 a 5 condições sem as quais o Goal é impossível?"

Critérios de um CSF válido:
- Se removido, o Goal se torna inalcançável
- É uma condição de estado, não uma ação ("Receita suficiente e previsível", não "Aumentar receita")
- Mutuamente exclusivo em escopo, coletivamente exaustivo em cobertura
- Se mais de 5 CSFs emergirem, eleve o nível de abstração — você está misturando CSFs com NCs

Exemplos de CSFs bem formulados:
- "Receita suficiente e previsível"
- "Base de clientes satisfeita e retida"
- "Equipe capacitada e engajada"
- "Operação entrega dentro do prazo e qualidade"

**Step 1.3 — Derivar as Necessary Conditions (NCs)**

Para cada CSF, pergunte: "O que precisa estar em vigor para que este CSF seja satisfeito?"

Critérios de uma NC válida:
- É um estado, não uma ação ("Processo de onboarding está estruturado", não "Estruturar onboarding")
- Pode suportar mais de um CSF (conexão lateral)
- Máximo 3 níveis abaixo de um CSF — se precisar de mais, o sistema está mal delimitado

**Step 1.4 — Montar a hierarquia textual**

Use indentação para representar a estrutura:

```
[GOAL]
├── [CSF 1]
│   ├── [NC 1.1]
│   └── [NC 1.2]
├── [CSF 2]
│   ├── [NC 2.1]
│   │   └── [NC 2.1.1]
│   └── [NC 2.2]
└── [CSF 3]
    └── [NC 3.1]
```

**Step 1.5 — Verificar a lógica de necessidade**

Aplique o **Teste de 10.000 pés**: leia o IO Map de cima para baixo e de baixo para cima. Cada conexão deve sobreviver ao teste: "Para [superior], precisamos de [inferior]."

Se uma conexão não é intuitivamente óbvia para alguém fora do sistema, a entidade está mal formulada — reformule antes de apresentar.

Armadilhas a verificar antes de apresentar:
- NCs formuladas como ações (reformular para estados)
- Mais de 5 CSFs (elevar abstração)
- IO Map genérico demais (não específico ao sistema analisado)
- Qualquer entidade com duas ideias dentro dela (separar)

---

### Validação Final — Obrigatória

Apresente o IO Map completo ao usuário e faça **as três perguntas de validação**, todas de uma vez:

> **"Antes de avançarmos para o diagnóstico da realidade atual, preciso que você valide este IO Map:"**
>
> 1. **CSF faltando?** "Se eu ignorar completamente qualquer um destes CSFs, o Goal ainda seria possível? Existe alguma condição crítica que não está listada?"
> 2. **NC no lugar errado?** "Alguma Necessary Condition está alocada ao CSF errado? Ela deveria suportar outro CSF?"
> 3. **NC redundante ou operacional?** "Alguma NC é um 'como fazer' em vez de um 'o que precisa existir'? Alguma é redundante com outra?"

Aguarde resposta. Incorpore ajustes. Então exiba o IO Map revisado com o status:

> `[VALIDADO PELO USUÁRIO — PRONTO PARA CRT]` ou `[AGUARDANDO VALIDAÇÃO]`

---

## 🛑 Regras de Ouro

1. **NÃO avance para a CRT sem `[VALIDADO]` explícito** do usuário. O IO Map não validado produz UDEs arbitrários.
2. **NÃO recolete dados** que já existem nos arquivos `context/`.
3. **NÃO execute Fase 0 e Fase 1 em uma única resposta** — pause após a Fase 0 para confirmar o recorte do sistema.
4. **NÃO formule entidades compostas** (duas ideias numa caixa). Se precisar de "e" para descrever uma entidade, separe.
5. **NÃO inclua ações** (verbos no infinitivo) como entidades — apenas condições de estado.

---

## Formato de Saída Obrigatório

### Bloco de Contexto (output da Fase 0)

```
## Definição do Sistema

- **Sistema:** [nome e escopo]
- **Dono / Span of Control:** [quem decide]
- **Sphere of Influence:** [o que influencia mas não controla]
- **Goal:** [declaração no presente]
- **Limites:** dentro: [...] / fora: [...]

> Status: [AGUARDANDO CONFIRMAÇÃO DO SISTEMA]
```

---

### IO Map (output da Fase 1)

```
## IO Map — [Nome do Sistema]

**Goal:** [declaração completa]

### Critical Success Factors

**CSF 1:** [declaração]
  - NC 1.1: [condição necessária]
  - NC 1.2: [condição necessária]

**CSF 2:** [declaração]
  - NC 2.1: [condição necessária]
    - NC 2.1.1: [sub-condição, se necessário]
  - NC 2.2: [condição necessária]

**CSF 3:** [declaração]
  - NC 3.1: [condição necessária]

---

### Leitura da Lógica

Para atingir [GOAL], precisamos de [CSF 1] E [CSF 2] E [CSF 3].

Para [CSF 1], precisamos de [NC 1.1] E [NC 1.2].
Para [CSF 2], precisamos de [NC 2.1] E [NC 2.2]. Para [NC 2.1], precisamos de [NC 2.1.1].
Para [CSF 3], precisamos de [NC 3.1].

---

### Perguntas de Validação

1. Algum CSF está faltando?
2. Alguma NC está alocada ao CSF errado?
3. Alguma NC é um "como fazer" em vez de um "o que precisa existir"?

> Status: [AGUARDANDO VALIDAÇÃO]
```

---

### Após validação confirmada

Atualize o status e registre:

```
> **IO Map Status:** [VALIDADO PELO USUÁRIO — PRONTO PARA CRT]
> **Próximo passo:** Fase 2 — Current Reality Tree (`skill-ltp-crt.md`)
> Compare cada NC e CSF com a realidade atual: onde a realidade não satisfaz uma condição → candidato a UDE.
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/io-map.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
