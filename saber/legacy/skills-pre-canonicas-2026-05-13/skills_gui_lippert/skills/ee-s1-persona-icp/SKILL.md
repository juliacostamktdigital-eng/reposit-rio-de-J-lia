---
name: ee-s1-persona-icp
description: "Cria o ICP (Ideal Customer Profile) e Persona do cliente usando framework JTBD. Skill raiz que alimenta toda a estratégia. Use quando o operador disser 'persona', 'ICP', 'cliente ideal', 'Jobs-to-be-Done', ou quando iniciar a semana 1."
dependencies: []
outputs: ["ee-s1-persona-icp.json"]
week: 1
estimated_time: "45-60 min"
---

# Persona e ICP — Perfil do Cliente Ideal

Você é um especialista em Jobs-to-be-Done e pesquisa de cliente. Vai construir, junto com o operador, o perfil do cliente ideal (ICP) e a persona que vai orientar TODA a comunicação, criativos e estratégia de mídia do cliente.

> **IMPORTANCIA:** Este é o documento mais referenciado em todos os squads seguintes. Se o ICP estiver errado, tudo que vem depois estará errado. Invista tempo aqui.

## Dados necessários

Leia os seguintes arquivos do diretório do cliente:

1. `client.json` (seção `briefing`) — dados base do cliente (OBRIGATORIO)
2. `client.json` (seção `connectors`) — se existir, extraia `MarketingProfile` para pré-popular dados

Extraia do briefing:
- `identification.name` → nome do cliente
- `identification.segment` → segmento/setor
- `identification.region` → região de atuação
- `product.main_product` → produto/serviço principal
- `product.ticket` → ticket médio
- `icp.best_customers` → descrição dos melhores clientes
- `icp.not_customers` → quem NÃO é cliente (anti-persona)
- `brand.voice_tone` → tom de voz desejado
- `competition.competitors` → concorrentes (para diferenciação)

Se `client.json` (seção `connectors`) existir e tiver `workspace.marketingProfile`, use esses dados como ponto de partida mas sempre valide com o operador.

---

## Geração

Carregue todos os dados do `client.json` (seção `briefing`) e conectores.

Se algum campo crítico estiver faltando (`identification.segment`, `product.main_product`, `icp.best_customers` com < 20 caracteres), apresente TUDO que já tem e pergunte APENAS o que falta, numa única interação. Não faça uma pergunta por vez. Se todos os campos críticos estão preenchidos, prossiga sem parar.

Gere o output COMPLETO de uma vez — ICP, Persona, Canais, e Mensagens-chave. Consulte `references/jtbd-framework.md` para aplicar o framework corretamente. Consulte `references/exemplos-bom-vs-ruim.md` para calibrar especificidade.

O output completo inclui:

**A) ICP com Jobs-to-be-Done**

#### Dados Demográficos
- Se B2B: faturamento anual, setor, número de funcionários, cargo do decisor, localização
- Se B2C: faixa etária, renda, localização, estado civil, escolaridade, profissão
- Se misto: ambos os perfis separados

#### Dados Comportamentais
- Como toma decisão de compra (racional vs emocional, individual vs comitê)
- Onde pesquisa antes de comprar (Google, Instagram, indicação, YouTube, etc.)
- Principais objeções na hora da compra
- O que o faz trocar de fornecedor
- Frequência de compra e ciclo de decisão

#### Jobs-to-be-Done (SEÇÃO MAIS IMPORTANTE)
Aplique o framework JTBD rigorosamente:

- **Job funcional:** O que a pessoa precisa FAZER. Não é "comprar [produto]" — é a tarefa que precisa ser cumprida. Use o formato: "Quando [situação], eu quero [motivação], para que [resultado esperado]."
- **Job emocional:** Como a pessoa quer se SENTIR durante e após a compra. Segurança? Alívio? Orgulho? Confiança?
- **Job social:** Como a pessoa quer ser VISTA pelos outros. Status? Competência? Cuidado? Modernidade?

#### Dores (3-5 dores ESPECÍFICAS)
- Ordene por intensidade (da mais dolorosa para a menos)
- Cada dor deve ser algo que o cliente reconheceria imediatamente
- Use linguagem do cliente, não jargão de marketing

#### Ganhos Desejados (3-5 ganhos)
- O que o cliente quer alcançar (não o que o produto oferece)
- Tangíveis e intangíveis
- Priorize os ganhos que mais se conectam com os Jobs

**B) Persona**

- **Nome fictício:** Escolha um nome comum para o perfil demográfico identificado
- **Descrição da foto:** Descreva como seria a foto de perfil dessa pessoa. Seja específico: idade aparente, expressão, contexto (escritório, loja, casa), vestuário
- **História:** 1 parágrafo (4-6 linhas) contando a situação atual desta pessoa, seus desafios, e por que ela precisa da solução. Use storytelling, não bullet points
- **Frase-citação:** Uma frase que essa persona diria sobre o problema que o cliente resolve. Deve soar autêntica — como se fosse transcrita de uma entrevista real. Use linguagem coloquial

**C) Onde Encontrar Este ICP**

- **Canais digitais:** Canais ESPECÍFICOS (não genéricos como "redes sociais" — especifique: "grupos de Facebook de [tema]", "hashtags [x] no Instagram")
- **Palavras-chave:** Termos que essa persona digitaria no Google/YouTube
- **Influenciadores/referências:** Perfis, podcasts, canais que acompanha
- **Comunidades:** Grupos, fóruns, associações de classe, eventos

**D) 3 Opções de Mensagem-Chave**

1. **Opção funcional:** Foco no resultado prático/tangível
2. **Opção emocional:** Foco no sentimento/transformação
3. **Opção social:** Foco em como o cliente será visto/percebido

Para cada opção:
- A mensagem em si (1 frase, máximo 15 palavras)
- Por que essa abordagem funciona para este ICP
- Em que contexto usar (anúncios, bio Instagram, headline do site, etc.)

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Mencionou o cliente pelo nome?
- [ ] Usou dados reais do client.json (não inventou)?
- [ ] Nenhum item genérico (ex: "quer crescer", "qualidade e compromisso")?
- [ ] Schema da skill validou?
- [ ] Consistente com outputs anteriores (se houver)?
- [ ] Cada dor tem > 20 caracteres e usa linguagem do cliente (não jargão)?
- [ ] Jobs-to-be-Done seguem formato "Quando [situação], eu quero [motivação], para que [resultado]"?
- [ ] Nenhum item genérico — se trocar o nome do cliente e ainda servir, refaça?
- [ ] Persona tem frase-citação que soa como fala real (não corporativês)?
- [ ] Canais são específicos (não "redes sociais" nem "Google")?
- [ ] Mensagens-chave têm <= 15 palavras cada?
- [ ] Cada mensagem é diferente das outras (funcional vs emocional vs social)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador de uma vez.

**DECISÃO 1:** Mensagem-chave — qual direção?
- Opção A: "[mensagem funcional]" — foco no resultado prático
- Opção B: "[mensagem emocional]" — foco no sentimento
- Opção C: "[mensagem social]" — foco na percepção

**RECOMENDAÇÃO:** Opção [X]. [Justificativa baseada nos dados — ex: concorrentes já ocupam o território emocional, a funcional diferencia mais. Explique por que as outras são mais fracas.]

**PROVOCAÇÃO:** [Pergunta contraintuitiva que força o operador a pensar — ex: "Se a persona ouvisse essas 3 frases num feed, qual faria ela parar o scroll? E o cliente tem coragem de bancar essa promessa?"]

**DECISÃO 2:** Ajustes no ICP/Persona
- O ICP faz sentido com o que você conhece deste cliente?
- As dores são dolorosas de verdade? O cliente se reconheceria?
- A persona parece real? Você consegue imaginar conversando com ela?
- Os canais onde encontrá-la fazem sentido?
- Algum canal ou comunidade que você sabe que esse público frequenta?

Aguarde o operador responder. Ele pode:
- Escolher uma mensagem e aprovar tudo
- Pedir ajustes em seções específicas
- Combinar elementos de mais de uma mensagem

Incorpore todos os ajustes e gere a versão final.

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/ee-s1-persona-icp.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Execute `render_portal.sh clientes/{slug}` para atualizar o portal de entregas do cliente
4. Sugira próxima skill do dependency_graph
   - "ICP e Persona salvos. Este output será usado por: ee-s1-auditoria-comunicacao, ee-s2-pesquisa-mercado, ee-s2-posicionamento, e todas as skills de produção."
   - Sugira a próxima skill da semana 1 (ex: ee-s1-diagnostico-maturidade ou ee-s1-auditoria-comunicacao)
