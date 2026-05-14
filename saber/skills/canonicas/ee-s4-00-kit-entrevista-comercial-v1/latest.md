---
slug: ee-s4-00-kit-entrevista-comercial-v1
name: ee-s4-00-kit-entrevista-comercial-v1
description: "Gera roteiro personalizado de perguntas para cada papel da equipe comercial (gestor, vendedor, SDR, pós-venda, dono) com base no contexto do cliente. Lê context/business.md, context/gtm.md e context/constraints.md para personalizar as perguntas. Usar antes das entrevistas de campo na Semana 4 — Fase 1, após o cliente oculto."
context_reads:
  - context/business.md
  - context/gtm.md
  - context/constraints.md
  - outputs/definicao-icp-b2b.json
week: 4
estimated_time: "30 min"
outputs: []
---

# Kit de Entrevistas Comerciais

Você é um especialista em diagnóstico comercial. Vai gerar um roteiro personalizado de perguntas para cada papel que o consultor vai entrevistar na equipe do cliente, baseado no contexto do negócio já mapeado.

> **PRINCÍPIO:** Entrevistas mal preparadas revelam o que o time quer mostrar. Perguntas calibradas ao contexto revelam o que o time não sabe que está revelando.
>
> **PERSONALIZAÇÃO É OBRIGATÓRIA:** Use os dados de `context/business.md`, `context/gtm.md` e `context/constraints.md` para calibrar cada pergunta ao cliente específico. Perguntas genéricas são lidas como auditoria punitiva — perguntas específicas geram confiança e respostas reais.
>
> **MODO DE USO:** O consultor leva este kit para as entrevistas. Não é um script a ser lido — é um mapa de navegação. Adapte o tom, pule o que já foi respondido em outra entrevista, aprofunde onde houver abertura.

## Dados necessários

Leia automaticamente antes de gerar:
1. `context/business.md` — segmento, ICP atual, faturamento, revenue streams
2. `context/gtm.md` — canal principal, ciclo de venda, funil declarado, ticket médio
3. `context/constraints.md` — gargalos e travas já identificados (hipóteses de S3)
4. `outputs/definicao-icp-b2b.json` — objeções mapeadas, perfil do comprador

Confirme com o operador:
> "Antes de gerar o kit, confirme:
> 1. Quais papéis serão entrevistados? (ex: gestor comercial, 2 vendedores, SDR, pós-venda)
> 2. Tem algum papel que você quer mapear com mais profundidade?
> 3. O time já sabe que haverá entrevistas? (impacta o tom das perguntas)"

---

## Geração

Gere o kit COMPLETO com seções separadas por papel. Para cada papel entrevistado, gere a seção correspondente. Omita papéis que não existem nesse cliente.

### Orientações Gerais para o Consultor

**Posicionamento:** "Estamos aqui para entender como o processo funciona do ponto de vista de quem está na linha de frente — não para avaliar ninguém. Sua visão é o dado mais valioso do diagnóstico."

**Postura:** Escuta ativa, sem julgamento. Deixar o entrevistado falar antes de aprofundar. Não fazer perguntas que soem como "você faz isso errado?".

**Duração sugerida por papel:** 30–45 minutos. Qualidade sobre quantidade de perguntas.

**O que observar além das respostas:**
- Hesitação ao mencionar CRM → resistência ao sistema ou desconhecimento
- Culpar sistematicamente o lead ou o preço → ausência de accountability
- Respostas muito alinhadas ao discurso do gestor → entrevistado filtrando o que diz
- Animação genuína ao descrever um deal ganho → padrão real de sucesso

---

### PAPEL 1: Gestor Comercial / Head de Vendas

> Objetivo: Mapear o processo como é gerido, os critérios de decisão e os gaps entre o que o gestor acredita que acontece e o que os dados mostrarão.

**Abertura sugerida:**
> "Me conta como o processo comercial funciona aqui — da entrada do lead até o fechamento. Tenta descrever como ele acontece no dia a dia, não necessariamente como deveria funcionar."

**Perguntas-chave:**

| # | Pergunta | O que estamos mapeando |
|---|----------|------------------------|
| 1 | "Quando um lead entra, o que acontece nos primeiros 30 minutos?" | LRT real vs declarado |
| 2 | "Quantas tentativas de contato vocês fazem antes de desistir de um lead? Em que intervalo?" | Cadência real |
| 3 | "Como os vendedores priorizam quais leads trabalhar primeiro?" | Critério de priorização — ou ausência dele |
| 4 | "Quando uma proposta é enviada e o lead some, qual é o protocolo?" | Follow-up pós-proposta |
| 5 | "O que seu melhor vendedor faz diferente dos outros?" | Padrão de sucesso não documentado |
| 6 | "Qual etapa do funil mais perde leads hoje? Por que você acha que isso acontece?" | Percepção do gargalo vs dado real |
| 7 | "Você tem algum script ou guia de conversa para o time usar?" | Existência de padronização |
| 8 | "Como você acompanha o pipeline — com qual frequência e usando quais dados?" | Maturidade de gestão comercial |

**Perguntas de aprofundamento contextual** (personalizar com os dados do cliente):
- {pergunta baseada no canal principal identificado em gtm.md — ex: "Você percebe diferença entre leads que vêm de [canal A] vs [canal B]?"}
- {pergunta baseada na trava ou gargalo identificado em constraints.md}
- {pergunta sobre o segmento ou produto específico do cliente}

**Materiais a solicitar nesta entrevista:**
- [ ] Acesso ao CRM (ou permissão para compartilhar prints)
- [ ] Dashboard ou relatório de pipeline atual
- [ ] Script ou roteiro de vendas (formal ou informal)
- [ ] Meta de conversão atual e resultado dos últimos 3 meses

---

### PAPEL 2: Vendedor / Closer

> Objetivo: Entender como as conversas de venda realmente acontecem, quais objeções o vendedor enfrenta e como lida com elas na prática.

**Abertura sugerida:**
> "Me conta sobre uma venda que você fechou recentemente que te deixou satisfeito. O que aconteceu nessa venda, do começo ao fim?"

**Perguntas-chave:**

| # | Pergunta | O que estamos mapeando |
|---|----------|------------------------|
| 1 | "Agora me conta de uma venda que você perdeu recentemente. O que aconteceu?" | Padrão de derrota + accountability |
| 2 | "Quando você recebe um lead novo, o que você faz primeiro?" | LRT e abordagem inicial real |
| 3 | "Quando o lead fala que está caro, o que você responde?" | Habilidade de contorno de objeção de preço |
| 4 | "Depois de enviar uma proposta, o que você faz?" | Follow-up pós-proposta |
| 5 | "O que você sente falta de ter para vender mais?" | Bloqueadores reais (ferramenta, produto, posicionamento) |
| 6 | "Quando você decide parar de tentar contato com um lead?" | Critério de desqualificação |
| 7 | "Você costuma perguntar para o lead por que ele não comprou?" | Cultura de aprendizado com perda |

**Perguntas de aprofundamento contextual** (personalizar com os dados do cliente):
- "Como você explica {produto/serviço} para alguém que nunca ouviu falar?"
- "Qual objeção você ouve mais? O que você responde normalmente?"
- {pergunta baseada nas objeções mapeadas em definicao-icp-b2b.json}

**Materiais a solicitar:**
- [ ] 2–3 conversas recentes (WhatsApp) — uma ganha, uma perdida
- [ ] Proposta que costuma enviar (modelo)

---

### PAPEL 3: SDR / Pré-vendas

> Objetivo: Mapear o primeiro contato, a qualificação e o handoff para o vendedor — onde o lead esfria ou aquece antes de chegar à negociação.

**Abertura sugerida:**
> "Me conta como você lida com um lead novo quando ele chega — do momento que você vê a notificação até fazer o primeiro contato."

**Perguntas-chave:**

| # | Pergunta | O que estamos mapeando |
|---|----------|------------------------|
| 1 | "Quanto tempo leva, em média, do lead entrar até você fazer o primeiro contato?" | LRT real |
| 2 | "O que você tenta descobrir no primeiro contato antes de qualificar?" | Profundidade de qualificação |
| 3 | "Como você decide se um lead é qualificado ou não?" | Critérios de qualificação (formais ou informais) |
| 4 | "O que acontece quando um lead não responde na primeira tentativa?" | Cadência de follow-up |
| 5 | "Você tem um roteiro para o primeiro contato ou vai pelo feeling?" | Padronização |
| 6 | "Qual tipo de lead você mais gosta de receber? Por quê?" | Perfil de lead que converte na visão do SDR |

**Materiais a solicitar:**
- [ ] Mensagem padrão de primeiro contato (cópia ou print)
- [ ] Quantas tentativas faz antes de desistir (protocolo real)

---

### PAPEL 4: Pós-venda / Customer Success

> Objetivo: Entender por que clientes ficam e por que saem — as causas reais de churn revelam o gap entre o que é prometido no comercial e o que é entregue.

**Abertura sugerida:**
> "Me conta quais são os tipos de clientes que mais ficam satisfeitos com vocês — o que esses clientes têm em comum?"

**Perguntas-chave:**

| # | Pergunta | O que estamos mapeando |
|---|----------|------------------------|
| 1 | "E os clientes que saem ou não renovam — o que eles têm em comum?" | Perfil de churn e causas reais |
| 2 | "Qual é a principal reclamação que você ouve dos clientes?" | Gap entre promessa de venda e entrega real |
| 3 | "Alguma vez um cliente reclamou que o que foi vendido não era o que ele esperava?" | Misalinhamento de expectativa no comercial |
| 4 | "Quais clientes você indicaria como casos de sucesso?" | Beachhead real (quem fica + recomenda) |
| 5 | "O que você mudaria no processo de vendas para facilitar seu trabalho de retenção?" | Tensão comercial vs entrega |

---

### PAPEL 5: Dono / CEO (quando envolvido em vendas)

> Objetivo: Entender a visão estratégica e onde o dono interfere diretamente no processo comercial — influência oculta que o time pode não declarar.

**Abertura sugerida:**
> "Me descreve o cliente ideal para o negócio hoje — o cliente que você quer ter mais."

**Perguntas-chave:**

| # | Pergunta | O que estamos mapeando |
|---|----------|------------------------|
| 1 | "Por que você acha que vocês perdem clientes?" | Percepção do gargalo na visão estratégica |
| 2 | "Você está satisfeito com a performance comercial hoje?" | Nível de alinhamento e confiança no time |
| 3 | "O que mudaria no negócio se o comercial performasse 30% melhor?" | Motivação real por trás do diagnóstico |
| 4 | "Você participa de alguma venda diretamente? Em quais situações?" | Dependência do dono no processo |
| 5 | "Tem algum cliente que você sente que vocês deveriam ter fechado mas não fecharam?" | Percepção do teto de conversão |

---

## Checklist Master — Materiais a Coletar no Campo

Ao encerrar as entrevistas, confirmar que saiu com:

**CRM e dados:**
- [ ] Acesso ao CRM ou prints das últimas 30 oportunidades (abertas + fechadas)
- [ ] Export de negócios fechados — últimos 12 meses (valor + segmento + canal + data)
- [ ] Faturamento total dos últimos 12 meses (referência para validar export)

**Conversas reais:**
- [ ] 5–10 conversas de WhatsApp/email — idealmente 3 ganhos + 3 perdidos
- [ ] Pelo menos 1 conversa que o vendedor considera "boa" e 1 "difícil"

**Processo:**
- [ ] Script ou roteiro de vendas (pode ser informal)
- [ ] Proposta padrão (modelo que costumam enviar)
- [ ] Cadência de contato atual (n tentativas, intervalo)
- [ ] LRT médio declarado (estimativa do gestor)

**Metas e gestão:**
- [ ] Meta de conversão atual e resultado dos últimos 3 meses (se disponível)

---

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Cada papel tem abertura sugerida + perguntas calibradas ao contexto real do cliente (não placeholders)?
- [ ] As perguntas de aprofundamento contextual foram preenchidas com dados reais (segmento, canal, produto, objeções do ICP)?
- [ ] O checklist master está completo?
- [ ] O tom é de parceria e diagnóstico — não de auditoria ou julgamento?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o kit COMPLETO ao operador.

- "Tem algum papel que você vai entrevistar que não está coberto aqui?"
- "Alguma pergunta que parece inadequada para o contexto desse cliente?"
- "Tem alguma hipótese específica que você quer testar nas entrevistas e que eu não cobri?"

## Finalização

Operador aprova (com ou sem ajustes).

1. Consultor leva o kit para as entrevistas de campo
2. Após as entrevistas + coleta de materiais, retornar para a Fase 2: `/v4-skills:e.e:ee-s4-01-diagnostico-comercial-crm-v1`
3. "Kit de entrevistas pronto para {NOME_CLIENTE}. Papéis cobertos: {lista}. Checklist de materiais incluído."
