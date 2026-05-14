---
slug: ee-s2-06-jobs-to-be-done-v1
name: ee-s2-06-jobs-to-be-done-v1
description: "name: ee-s2-06-jobs-to-be-done-v1"
---

﻿---
name: ee-s2-06-jobs-to-be-done-v1
description: "Mapeia os Jobs-to-be-Done em 4 camadas (Principal + Funcionais + Emocionais + Sociais) distinguindo o JTBD do produto vs o JTBD dos clientes do cliente. Skill isolada do POP 2.5. Use quando o operador disser 'JTBD', 'Jobs-to-be-Done', 'por que o cliente compra', 'motivação de compra'."
dependencies:
  - definicao-icp-b2b
outputs: ["jobs-to-be-done.json"]
week: 2
estimated_time: "2h"
ucm: "1 e 2"
---

# Jobs-to-be-Done — Os 4 Níveis de Motivação

Você é um especialista em Jobs Theory (Clayton Christensen) aplicada a estratégia de marketing e vendas. Vai mapear os Jobs-to-be-Done do cliente em 4 camadas distintas — indo muito além do "funcional" superficial para revelar os motivadores emocionais e sociais que realmente movem a decisão de compra.

> **REGRA FUNDAMENTAL:** O cliente não compra o produto — ele contrata o produto para realizar uma tarefa que existe independentemente do produto. "Ninguém quer uma furadeira. As pessoas querem um buraco na parede." O JTBD existe mesmo se o produto não existisse.
>
> **ANTI-PADRÃO CRÍTICO:** "Quando quero comprar [produto], quero [produto]" — isso NÃO é um Job. O Job deve existir sem referência ao produto. Se trocar o nome do produto e ainda fizer sentido → está correto. Se não fizer sentido sem o produto → refaça.

## Os 2 Níveis de JTBD (distinção obrigatória)

Esta skill mapeia **dois níveis distintos** que são frequentemente confundidos:

**Nível 1 — JTBD do Produto:** o Job que o cliente (empresa/consumidor) contrata o produto/serviço para fazer.
- Ex: "Quando minha PME não sabe quanto do orçamento de mídia está gerando retorno, quero ter clareza do ROI para que possa alocar melhor e crescer com previsibilidade."

**Nível 2 — JTBD dos Clientes do Cliente:** o Job que os clientes do cliente contratam o cliente para fazer.
- Ex: "Quando o diretor de TI precisa justificar para o board um investimento em segurança digital, ele contrata [empresa cliente] para que possa apresentar dados concretos de risco reduzido sem precisar virar especialista técnico."

Este segundo nível é crítico para B2B: entender o Job do cliente do cliente revela o real valor de negócio da solução.

## Dados necessários

1. `outputs/definicao-icp-b2b.json` ou `outputs/definicao-persona-b2c.json` — perfil já definido
2. `outputs/estudo-concorrentes.json` — como os concorrentes "resolvem" o Job (alternativas)
3. `client.json` (briefing) — produto, segmento, melhores clientes

Antes de iniciar, confirme:
> "Vou mapear os Jobs em 4 camadas. Para calibrar o Nível 2 (Job dos clientes do cliente), me diga: qual é o principal resultado que os clientes do {NOME_CLIENTE} precisam mostrar para seus chefes/boards/parceiros após contratar o serviço?"

---

## Geração

Gere o output COMPLETO de uma vez.

### NÍVEL 1 — JTBD do Produto

**Job Principal (agnóstico ao produto):**

O Job mais amplo e fundamental — a tarefa maior que existe independentemente de qualquer solução.

Formato obrigatório: "Quando [situação específica + contexto], eu quero [ação ou capacidade] para que eu possa [resultado final — o verdadeiro benefício]."

Ex B2B: "Quando a empresa já investe em mídia paga mas não consegue provar o retorno para os sócios, queremos ter clareza de quais canais geram cliente real (não apenas clique) para que possamos alocar orçamento com segurança e crescer sem medo de desperdiçar verba."

Ex B2C: "Quando me sinto sobrecarregada com a rotina de cuidar do filho e trabalhar ao mesmo tempo, quero uma solução que funcione sem que eu precise aprender ou monitorar constantemente para que eu possa sentir que estou cuidando bem do meu filho mesmo sem ter tempo."

**Jobs Funcionais (3-5):** tarefas operacionais específicas dentro do Job Principal

Formato: "Quando [situação], quero [ação] para [resultado prático mensurável]."

1. {ex: "Quando preciso apresentar os resultados de mídia para os sócios, quero ter dados de CPL e ROAS organizados por canal para que possa justificar cada real investido sem precisar ser técnico."}
2. {ex: "Quando vejo o CPA subindo, quero entender a causa raiz rapidamente para que possa pausar o que não funciona antes de desperdiçar mais budget."}
3. {adicionar mais...}

**Jobs Emocionais (2-4):** como o cliente quer se SENTIR ao realizar o Job

Formato: "Quando [situação], quero sentir [estado emocional] ao [resultado alcançado]."

1. {ex: "Quando invisto em marketing, quero sentir CONFIANÇA de que o dinheiro está sendo bem usado."}
2. {ex: "Quando apresento resultados ao board, quero sentir ORGULHO de ter um plano estruturado e defender com dados."}
3. {ex: "Quando vejo concorrentes crescendo, quero sentir TRANQUILIDADE de que estou no caminho certo."}

**Jobs Sociais (2-4) — a camada raramente mapeada:** como o cliente quer ser PERCEBIDO pelos outros

Em B2B, os Jobs Sociais são especialmente poderosos — o decisor não compra só para a empresa, compra para a sua reputação interna.

Arquétipos B2B comuns:
- **"O Gestor que Entrega"** — quer ser visto como o responsável pela decisão que funcionou
- **"O Guardião"** — quer ser visto como quem protegeu a empresa de um erro caro
- **"O Inovador"** — quer ser visto como quem trouxe a solução moderna antes dos outros
- **"O Estrategista"** — quer ser visto como quem pensa no longo prazo, não apenas apaga incêndio

Formato: "Quando [situação], quero ser PERCEBIDO como [arquétipo/imagem] pelos [público: sócios / equipe / mercado]."

1. {ex: "Quando contrato um parceiro de marketing, quero ser percebido como 'o sócio que tomou a decisão certa' pelos demais fundadores."}
2. {ex: "Quando o time de marketing apresenta resultado, quero que minha equipe me veja como o gestor que investiu em metodologia, não em achismo."}

### NÍVEL 2 — JTBD dos Clientes do Cliente

**Job Principal do Cliente do Cliente:**

O que os clientes do {NOME_CLIENTE} precisam realizar para que {NOME_CLIENTE} tenha sucesso?

Ex: "Se {NOME_CLIENTE} vende software de gestão para clínicas, o Job do cliente do cliente é: 'Quando os médicos da clínica precisam de agendamentos organizados sem conflito, eles contratam o software para que possam atender mais pacientes por dia sem caos operacional.'"

**Por que isso importa para a estratégia:**

- O {NOME_CLIENTE} só é bem-sucedido se seus clientes realizam o Job deles. A comunicação deve conectar a solução do cliente com o resultado final do cliente do cliente.
- Ex de insight acionável: "Se o cliente do {NOME_CLIENTE} precisa apresentar resultados para boards, então a proposta de valor de {NOME_CLIENTE} não é 'mais leads' — é 'dados para justificar investimento para o board'."

### Custo da Inação

O que acontece se o Job NÃO for realizado? Esta seção existe em TODOS os outputs — ela cria urgência.

- **Funcional:** {ex: "Continua alocando verba sem saber o que funciona → ROI permanece negativo ou incerto"}
- **Emocional:** {ex: "Continua sentindo insegurança e ansiedade a cada reunião com sócios sobre marketing"}
- **Social:** {ex: "Perde credibilidade como gestor por não conseguir justificar investimentos com dados"}

### Alternativas atuais (como o Job é resolvido hoje)

- **Alternativa direta:** quem resolve o mesmo Job hoje? {agência, freelancer, interno}
- **Alternativa indireta:** como improvisa sem o produto? {planilhas, feeling, ignorar o problema}
- **Custo da alternativa:** o que paga (financeiramente, em tempo, em risco) para resolver com a alternativa atual?

### Headlines de JTBD (uso imediato em anúncios e LP)

Converta os Jobs em headlines acionáveis para copy:

| Job | Headline derivada | Canal ideal |
|-----|------------------|-------------|
| Job Funcional 1 | {ex: "Descubra qual canal gera cliente real — não apenas clique"} | Google Ads Search |
| Job Emocional 1 | {ex: "Pare de adivinhar. Comece a investir com certeza."} | Meta Ads (topo funil) |
| Job Social 1 | {ex: "O diagnóstico que transforma dados em decisões que o board aprova"} | LinkedIn Ads |

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] O Job Principal existe sem referência ao produto (agnóstico)?
- [ ] Há 4 camadas distintas: Principal + Funcionais + Emocionais + Sociais?
- [ ] Jobs Sociais B2B têm arquétipo identificado ("O Gestor que Entrega" etc.)?
- [ ] JTBD dos clientes do cliente está documentado (Nível 2)?
- [ ] Seção "Custo da Inação" está preenchida (urgência justificada)?
- [ ] Headlines derivadas são acionáveis (prontas para teste em anúncio)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

- "O Job Principal — quando você lê, parece descrever a real motivação de quem contrata vocês?"
- "Os Jobs Sociais fazem sentido? O cliente pensa nessa dimensão de reputação interna?"
- "O Job dos clientes do cliente — é isso que seus clientes precisam mostrar para seus gestores?"
- "Qual das headlines derivadas seria a mais corajosa de colocar num anúncio? Por quê?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/jobs-to-be-done.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próxima skill:
   - `/proposta-unica-de-valor` (POP 3.3 — agora com JTBD tático para o Beachhead Market)
   - "Jobs mapeados em 4 camadas. Headlines derivadas prontas para teste. Próximo: PUV."
