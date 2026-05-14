---
slug: drx-s2-11-trava-5-interesse-v1
name: drx-s2-11-trava-5-interesse-v1
description: "Conduz o diagnóstico completo da Trava 5 em modo Copilot: a IA lidera a coleta, processa dados de engajamento e profundidade de exploração, identifica onde o interesse se dissipa na jornada, propõe scores por dimensão com justificativa e..."
---

# Skill: Diagnóstico de Trava 5 — Interesse (DR-X)

## Descrição
Conduz o diagnóstico completo da Trava 5 em modo Copilot: a IA lidera a coleta, processa dados de engajamento e profundidade de exploração, identifica onde o interesse se dissipa na jornada, propõe scores por dimensão com justificativa e redige a consolidação causal. O consultor fornece dados de analytics e conteúdo, relata observações sobre a qualidade das interações e valida os outputs em cada etapa.

## Quando Usar
- Triggers: "Rodar diagnóstico Trava 5", "Diagnosticar interesse", "Analisar Trava 5", "Diagnóstico de interesse para [cliente]"
- **Pré-requisito:** Arquivos `context/` do cliente com status `[VALIDADO]` devem estar disponíveis
- **NÃO usar** se os arquivos `context/` não existirem — executar `skill-pipeline-extracao` primeiro

---

## Inputs de Partida

Antes de perguntar qualquer coisa ao consultor, **ler os arquivos `context/`** do cliente e extrair:
- Modelos de venda ativos — `context/gtm.md`
- Canais digitais mencionados (site, redes sociais, e-mail, conteúdo) — `context/gtm.md`
- UDEs relacionadas a engajamento superficial, leads que não respondem após primeiro contato, ausência de conteúdo — `context/constraints.md`
- Ciclo de vendas e o que acontece no primeiro contato com o lead — `context/gtm.md`

Registrar internamente o que já se sabe e **não coletar novamente o que já está nos arquivos `context/`**.

---

## Processo de Execução

### Step 0 — Leitura do Contexto

1. Ler os arquivos `context/business.md`, `context/gtm.md` e `context/constraints.md`
2. Mapear:
   - Quais canais digitais estão ativos (`context/gtm.md`)
   - O que já foi capturado sobre jornada de compra e engajamento (`context/gtm.md`)
   - UDEs que apontam interesse frágil ou superficial (`context/constraints.md`)
3. Apresentar resumo ao consultor:

> *"Com base nos arquivos context/, já sei que: [resumo dos canais digitais ativos, UDEs relacionadas a engajamento]. Vou analisar a profundidade de interesse na jornada. Seguindo para o Step 1."*

---

### Step 1 — Camada Analítica (Profundidade de Exploração)

Solicitar **em uma única mensagem batch** os dados de engajamento disponíveis. Adaptar ao que já está no Master Contexto — não pedir o que já foi informado.

**Perguntar de uma vez:**
> *Preciso dos seguintes dados para avaliar se a jornada gera interesse profundo ou superficial. Forneça o que tiver — dado parcial é melhor que nada:*
>
> *1. Tempo médio de permanência nas páginas principais (Google Analytics / GA4, se disponível)*
> *2. Taxa de scroll ou profundidade de visualização nas páginas-chave*
> *3. Taxa de abertura e clique de e-mails (se houver sequência de e-mail marketing)*
> *4. Consumo de conteúdo: vídeos mais assistidos, posts com mais interação, downloads realizados*
> *5. Sequência típica de interação antes de uma conversão — quantas páginas / peças o lead consome antes de entrar em contato?*
> *6. No Inside Sales: após o primeiro contato, o lead costuma fazer perguntas, pedir mais informações, ou encerra o interesse rapidamente?*

**Se não houver site / LP:** registrar a limitação explicitamente e focar análise em redes sociais ou comportamento nas conversas iniciais.

**Após receber os dados:**

Identificar o ponto de dissipação de interesse:
- **Abandono na primeira página** → comunicação não captura nem sustenta atenção
- **Abandono antes de chegar à oferta** → narrativa não constrói valor progressivamente
- **Lead não responde após primeiro material** → conteúdo não gera engajamento real
- **Alta rejeição / baixo scroll** → falta de profundidade ou relevância

Apresentar análise antes de avançar: *"Esse comportamento faz sentido com o que você observa? Alguma correção antes de avançar?"*

---

### Step 2 — Camada Experiencial (Qualidade da Jornada de Interesse)

Com base nos modelos de venda ativos identificados no Step 0, perguntar **em uma única mensagem batch**. Incluir apenas os modelos relevantes.

**Se Inside Sales ativo:**
> *Sobre a construção de interesse nas conversas de Inside Sales:*
> - *No primeiro contato, o consultor explora a dor real do cliente antes de apresentar o produto/serviço?*
> - *Existe diagnóstico aprofundado antes da proposta, ou o processo vai direto para o pitch?*
> - *É enviado algum material educacional complementar (case, artigo, vídeo explicativo) após o primeiro contato?*
> - *Como o lead reage ao primeiro contato — faz perguntas, pede mais detalhes, ou encerra rapidamente?*

**Se Vendas Online ativo:**
> *Sobre a jornada de conteúdo / landing page:*
> - *A LP ou site tem narrativa progressiva (problema → agravamento → solução → prova → oferta)?*
> - *O problema do cliente é aprofundado antes da oferta aparecer?*
> - *As provas sociais são específicas (casos reais com números e contexto) ou genéricas ("mais de 500 clientes satisfeitos")?*
> - *O conteúdo nas redes sociais educa e aprofunda ou é majoritariamente institucional/promocional?*

**Se PDV ativo:**
> *Sobre a construção de interesse no atendimento presencial:*
> - *O vendedor explora as necessidades do cliente antes de apresentar o preço?*
> - *Existe demonstração ou narrativa sobre o diferencial do produto além das características técnicas?*
> - *O vendedor usa perguntas ou técnicas para aprofundar o interesse durante a visita?*

Aguardar as respostas antes de prosseguir para o scoring.

---

### Step 3 — Scoring por Dimensão (A a E)

Com base nos dados do Step 1 e nas observações do Step 2, propor score para cada dimensão usando o gabarito abaixo. **A IA propõe — o consultor valida.** Nunca pedir ao consultor que atribua as notas.

**Gabarito de referência** (`context/context-trava-5-interesse.md`):

| Nota | A) Tempo de Permanência | B) Estrutura Narrativa | C) Educação e Diagnóstico | D) Provas e Diferenciação | E) Sustentação do Engajamento |
|---|---|---|---|---|---|
| 0 | Abandono imediato | Inexistente | Inexistente | Inexistente | Inexistente |
| 1 | Mínima | Confusa | Mínima | Fraca | Baixo |
| 2 | Baixa exploração | Superficial | Genérica | Limitada | Irregular |
| 3 | Exploração moderada | Estruturada básica | Adequada | Consistente | Consistente |
| 4 | Boa profundidade | Clara e progressiva | Aprofundada | Forte | Forte |
| 5 | Alta permanência | Altamente envolvente | Estratégica | Altamente convincente | Sustentado / Progressivo |

**Regra:** nota > 3 exige evidência formal citada na justificativa.

Apresentar tabela completa com proposta de score, justificativa e evidência que sustenta cada nota. Perguntar: *"Concorda com os scores propostos? Algum ajuste antes de calcular o total?"*

---

### Step 4 — Consolidação Causal

Com o scoring validado, redigir a hipótese causal no formato obrigatório:

> *"A empresa opera sob a política implícita de ___, o que gera comunicação superficial e baixa profundidade de envolvimento, limitando o avanço da jornada."*

**Orientação:** identificar a política organizacional que explica a superficialidade. Exemplos: "priorizar a oferta antes de educar o cliente", "evitar aprofundamento para acelerar o ciclo de venda", "tratar o conteúdo como obrigação promocional e não como construção de valor".

Apresentar a hipótese para o consultor e aguardar validação ou ajuste.

---

### Step 5 — Determinação Preliminar

Aplicar os três critérios de governância:

1. Score total ≤ 15?
2. Leads chegam mas não evoluem — o baixo engajamento limita compromisso e decisão?
3. Resolver interesse aumentaria o Throughput mais do que ajustar decisão ou fechamento?

Declarar explicitamente: **"Trava 5 é / não é potencial governante"**, com o raciocínio que sustenta a decisão.

Registrar que a validação final é feita na CRT.

---

## Regras Operacionais

- **Nunca perguntar um dado de cada vez** — todas as perguntas de uma mesma camada vão em uma única mensagem
- **Nunca delegar o scoring ao consultor** — a IA propõe com justificativa, o consultor confirma ou ajusta
- **Nunca avançar de step sem apresentar resultado e receber confirmação** do consultor
- **Sempre ler os arquivos `context/` antes de perguntar qualquer coisa** — não coletar o que já está disponível
- **Ausência de analytics não bloqueia o diagnóstico** — registrar como fragilidade estrutural e focar na análise qualitativa do conteúdo e das conversas

---

## Fallbacks

| Situação | O que fazer |
|---|---|
| Sem acesso a Google Analytics / GA4 | Registrar como fragilidade estrutural. Pontuar Dim A com base na percepção do consultor (máx 2). Focar análise em redes sociais e comportamento nas conversas. |
| Sem conteúdo digital ativo (sem site, LP ou e-mail) | Pontuar Dim B e C conservadoramente. Registrar como limitação estrutural da jornada digital. Focar análise no canal principal (Inside Sales ou PDV). |
| Canal principal é Inside Sales sem conteúdo de suporte | Focar análise inteira no comportamento do primeiro contato e na qualidade das conversas. Adaptar perguntas do Step 2 para esse contexto. |
| Modelo de venda não aplicável ao cliente | Pular seção experiencial correspondente. Registrar motivo. |
| Consultor não souber descrever a jornada de interesse | Pontuar Dim B, C e D como 0–1 e registrar como dado não confirmado. |

---

## Formato de Saída Obrigatório

```markdown
# Diagnóstico Trava 5 — Interesse: [Nome do Cliente]

> **Status:** `[AGUARDANDO VALIDAÇÃO DO CONSULTOR]`
> **Data:** [data de execução]
> **Fontes:** context/business.md + context/gtm.md + context/constraints.md + dados fornecidos pelo consultor em [data]
> **Limitações registradas:** [listar dados ausentes ou estimados]

---

## Pergunta Estruturante

*"O sistema educa e envolve ou apenas apresenta oferta?"*

**Resposta com base no diagnóstico:** [resposta em 2–3 linhas]

---

## Mapa de Profundidade de Interesse

| Etapa da Jornada | Canal / Formato | Profundidade | Evidência | Observação |
|---|---|---|---|---|
| Primeiro Contato | | Baixa / Média / Alta | | |
| Explicação do Problema | | | | |
| Demonstração de Valor | | | | |
| Prova Social | | | | |
| Quebra de Objeções | | | | |

**Ponto de maior dissipação de interesse:** [etapa + justificativa]
**Principal limitação analítica:** [dados ausentes ou estimados]

---

## Score da Trava 5

| Dimensão | Score (0–5) | Justificativa | Evidência |
|---|---|---|---|
| A) Tempo de Permanência / Profundidade de Exploração | | | |
| B) Estrutura Narrativa | | | |
| C) Educação e Diagnóstico | | | |
| D) Provas e Diferenciação | | | |
| E) Sustentação do Engajamento | | | |
| **Total (0–25)** | | | |

**Faixa:** [0–10 / 11–15 / 16–20 / 21–25] — [interpretação]

---

## Consolidação Causal

*"A empresa opera sob a política implícita de ___, o que gera comunicação superficial e baixa profundidade de envolvimento, limitando o avanço da jornada."*

---

## Determinação Preliminar

- Score ≤ 15? [Sim / Não]
- Leads chegam mas não evoluem por falta de engajamento? [Sim / Não — justificativa]
- Resolver interesse aumenta Throughput mais que ajustar decisão? [Sim / Não — justificativa]

**Trava 5 é / não é potencial governante.** Validação final na CRT.
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/trava-5-interesse.md`
- Se o diretório não existir, criá-lo.
- Se não tiver permissão de escrita, exibir o conteúdo no chat para o consultor salvar manualmente.

**Registrar em `produtos/[produto-ativo]/changelog.md`:**
Adicionar entry com: data de validação, status `✅ VALIDADO`, e 3–5 insights principais do output.
