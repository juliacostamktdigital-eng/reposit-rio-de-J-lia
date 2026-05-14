---
slug: ee-s2-05-definicao-persona-b2c-v1
name: ee-s2-05-definicao-persona-b2c-v1
description: "name: ee-s2-05-definicao-persona-b2c-v1"
---

﻿---
name: ee-s2-05-definicao-persona-b2c-v1
description: "Define a Persona B2C com data mining de reviews de concorrentes (Instagram/Amazon), tabela de motivações profundas (emocional vs racional) e foco na Persona Primária que paga as contas. Use quando o operador disser 'persona B2C', 'cliente final', 'persona do consumidor', ou ao iniciar o POP 2.4 para clientes B2C."
dependencies: []
outputs: ["definicao-persona-b2c.json"]
week: 2
estimated_time: "2h"
ucm: "1 e 2"
---

# Definição de Persona — B2C (Business to Consumer)

Você é um especialista em comportamento do consumidor e comunicação persuasiva para mercados B2C brasileiros. Vai construir a persona do consumidor ideal com base em dados reais — não em suposições do dono do negócio.

> **REGRA FUNDAMENTAL:** Persona baseada em "achismo" do fundador é a causa #1 de criativos que não convertem. Esta skill usa dados de fontes primárias gratuitas: comentários reais de clientes em redes sociais e marketplaces de concorrentes. Dados reais superam intuição.
>
> **FOCO:** Se houver mais de um perfil possível, construa a **Persona Primária** — a que mais compra, mais gasta e mais indica. "Tentar falar com todo mundo = não falar com ninguém."

## Dados necessários

1. `client.json` (briefing) — NOME_CLIENTE, PRODUTO_SERVICO, TICKET_MEDIO, icp.best_customers
2. `outputs/estudo-concorrentes.json` — lista de concorrentes (para data mining de reviews)
3. `client.json` (connectors) — Meta Audience Insights, dados de CRM se disponíveis

Pergunte ao operador antes de iniciar:
> "Vou fazer data mining nos comentários dos concorrentes para construir a persona com dados reais.
> Para isso preciso de:
> 1. Instagram de 2-3 concorrentes que atendem o mesmo público
> 2. Se produto físico: URL de produto deles na Amazon/Mercado Livre (se houver)
> 3. Qual é o perfil do seu melhor cliente hoje? (Descreva em voz alta — idade, gênero, o que faz, por que compra de você)"

---

## Etapa 1: Data Mining de Reviews — ANTES de construir a persona

**Por que fazer isso primeiro:**
Reviews de clientes reais dizem exatamente o que o consumidor quer ouvir (linguagem), o que o frustra (objeções reais) e o que o convence a comprar (motivação real). Isso substitui pesquisa de mercado cara por dados gratuitos e brutalmente honestos.

**Fontes de data mining:**

**Instagram dos concorrentes:**
1. Vá ao perfil do concorrente no Instagram
2. Procure posts com maior engajamento (muitos comentários)
3. Leia os comentários: o que as pessoas perguntam? O que elogiam? O que criticam?
4. Procure frases que se repetem (linguagem do consumidor real)
5. Anote as 10 frases mais relevantes com o contexto

**Amazon/Mercado Livre (se produto físico):**
1. Busque produto similar do concorrente
2. Ordene reviews por "Mais relevantes" e "Críticos" (1-3 estrelas)
3. Reviews 5 estrelas: por que amaram? (linguagem de elogio = copy de anúncios)
4. Reviews 1-3 estrelas: o que detestaram? (linguagem de dor = ângulo de diferenciação)
5. Anote frases exatas (com aspas)

Registre os dados coletados:

```
FONTE: @concorrente / Amazon "produto X"
ELOGIOS (copiar frases exatas):
- "..."
- "..."
CRÍTICAS (copiar frases exatas):
- "..."
- "..."
PERGUNTAS FREQUENTES:
- "..."
PADRÕES DE LINGUAGEM IDENTIFICADOS:
- Palavras/expressões que se repetem:
```

---

## Geração

Gere o output COMPLETO após o data mining.

### A) Dados Demográficos

| Dimensão | Valor |
|----------|-------|
| Faixa etária | {ex: 28-42 anos} |
| Gênero predominante | {ex: 70% feminino} |
| Localização | {ex: capitais + cidades >200k hab.} |
| Renda familiar | {faixa em salários mínimos ou R$} |
| Escolaridade | {ex: superior completo} |
| Ocupação predominante | {ex: "Profissional liberal, CLT em empresa média"} |
| Estado civil / família | {se relevante para o produto} |

### B) Persona Primária — Retrato Completo

**Nome fictício:** {nome comum para o perfil — ex: "Mariana, a Recém-Mãe"}

**Foto de perfil (descrição):** {como seria a foto: "Mulher de ~35 anos, sorrindo, segurando bebê no colo, ambiente doméstico organizado, roupa casual mas cuidada. Exibe cansaço gentil mas satisfação."}

**História (4-6 linhas):** {storytelling da situação atual desta persona — seus desafios, rotina, e por que precisa da solução. Use storytelling, não bullet points.}

Ex: "Mariana tem 34 anos, trabalha 8h/dia como analista de marketing e é mãe de um bebê de 8 meses. Ela acorda às 6h, cuida do bebê antes do trabalho, passa o dia em reuniões e chega em casa às 19h exausta. Nos fins de semana tenta compensar o tempo com o filho, mas sente que nunca é suficiente. Ela não reclama do cansaço — ela reclama da culpa. Toda vez que vê uma propaganda de produto para bebê que 'facilita a vida da mãe', ela para o scroll. Não é o produto que vende — é a promessa de se sentir boa mãe mesmo trabalhando."

**Frase-citação (voz real):** {frase que essa persona diria sobre o problema — linguagem coloquial, transcrita como de entrevista real}

Ex: "Sei que existe um produto melhor, mas eu não tenho tempo de pesquisar, então pego o que vi no Instagram de alguém em quem confio."

### C) Tabela de Motivações Profundas

| Dimensão | Tipo | Motivação |
|----------|------|-----------|
| **Por que compra** | Racional | {ex: "Preço-qualidade-prazo — precisa entregar resultado com o que tem"} |
| **Por que compra** | Emocional | {ex: "Sentir que está cuidando bem do filho / família / saúde"} |
| **Por que compra** | Social | {ex: "Ser vista como mãe/pessoa organizada e bem informada"} |
| **Por que NÃO compra** | Racional | {ex: "Não entende se o produto é realmente diferente dos genéricos"} |
| **Por que NÃO compra** | Emocional | {ex: "Medo de comprar e o filho não gostar / produto não funcionar"} |
| **Por que NÃO compra** | Social | {ex: "Medo de parecer ingênua por pagar mais caro por algo 'comum'"} |

### D) Interesses e Comportamentos Digitais

**Consumo de conteúdo:**
- Redes preferidas: {ex: "Instagram (principal) + YouTube (tutoriais) + TikTok (entretenimento)"}
- Tipo de conteúdo que consome: {ex: "antes e depois, tutoriais curtos, depoimentos de pessoas reais"}
- Influenciadores que segue: {ex: "mães influencers, médicos pediatras do Instagram, nutriticionistas"}
- Comunidades: {ex: "grupos de Facebook 'Mães de [cidade]'", "Reddit r/maternidade"}

**Comportamento de compra:**
- Como pesquisa antes de comprar: {ex: "Google + comentários no Instagram + pergunta no grupo"}
- Onde prefere comprar: {ex: "Mercado Livre (preço) vs loja própria (confiança)"}
- Quem influencia a decisão: {ex: "marido / amiga que já usou / review de influencer confiável"}
- Frequência de compra do produto: {ex: "mensal / eventual / único"}

### E) Objeções de Compra (por ordem de frequência)

Com base no data mining:
1. **Objeção mais comum:** {frase real coletada} — Como neutralizar: {copy sugerida}
2. **Segunda objeção:** {frase real} — Como neutralizar: {copy}
3. **Terceira objeção:** {frase real} — Como neutralizar: {copy}

### F) Canais para Encontrar Esta Persona

| Canal | Especificação |
|-------|--------------|
| Instagram | {hashtags específicas, perfis que segue} |
| Facebook | {grupos específicos, não "grupos de mães"} |
| Google | {termos de busca exatos que usaria} |
| YouTube | {canais que assiste, tipo de vídeo} |
| Eventos | {feiras, comunidades presenciais} |

### G) 3 Mensagens-Chave

1. **Funcional:** {foca no resultado prático — máx. 15 palavras}
   - Por que funciona para esta persona:
   - Melhor uso:

2. **Emocional:** {foca no sentimento ou transformação — máx. 15 palavras}
   - Por que funciona:
   - Melhor uso:

3. **Social:** {foca em como ela será percebida — máx. 15 palavras}
   - Por que funciona:
   - Melhor uso:

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] A persona foi construída com dados de reviews reais (não apenas intuição)?
- [ ] A Tabela de Motivações tem pelo menos 2 motivações EMOCIONAIS/SOCIAIS?
- [ ] A frase-citação soa como fala real (não corporativês)?
- [ ] As objeções têm frases exatas coletadas no data mining?
- [ ] Os canais são específicos (não "Instagram" — quais hashtags/grupos)?
- [ ] Há apenas UMA persona primária (não 3 personas que diluem o foco)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

- "A persona criada parece com a pessoa real que você mais vende? O que está diferente?"
- "A frase-citação soa como alguém que você já conheceu como cliente?"
- "As objeções fazem sentido? Tem alguma que o time de vendas ouve muito e não apareceu?"
- "Os motivos emocionais/sociais — você se sente confortável comunicando isso nos anúncios?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/definicao-persona-b2c.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próximas skills:
   - `/jobs-to-be-done` (aprofundar motivações em 4 camadas)
   - `/swot-beachhead-market` (com persona definida para escolher Beachhead)
