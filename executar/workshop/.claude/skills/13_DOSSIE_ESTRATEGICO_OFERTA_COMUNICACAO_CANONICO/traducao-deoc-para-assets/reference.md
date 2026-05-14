# Referência — Tradução DEOC para assets

Norma principal: **`13_DOSSIE_ESTRATEGICO_OFERTA_COMUNICACAO_CANONICO.md`**, seção **5.9**.

## Matriz canônica (texto oficial)

O DEOC deve terminar com uma matriz:

| Saída | O que recebe do DEOC |
| --- | --- |
| Plano de mídia | beachhead, canais prováveis, ângulos, premissas, ICP/anti-ICP, oferta e critérios de lead correto |
| Briefing criativo | persona, hook, dor, mecanismo, prova e CTA |
| LP | narrativa, seções, promessa, prova, objeções, formulário, escopo e CTA |
| Copy de anúncios | hooks, headlines, CTAs, variações e claims |
| Vendas | promessa vista pelo lead, objeções, anti-ICP, perguntas de qualificação e limites da oferta |
| Tracking | atributos para UTM/creative ID: persona, hook, dor, ângulo, etapa |

Esta skill **expande** cada linha em campos preenchíveis e liga ao **backlog** de peças ainda não existentes.

## Mapeamento sugerido (DEOC → asset)

| Fonte no DEOC (playbook 13) | Uso típico |
| --- | --- |
| 5.1 Resumo / beachhead | Plano de mídia, priorização de mensagem |
| 5.2 Oferta e mecanismo | Plano de mídia, LP, copy, vendas (expectativa) |
| 5.3 ICP / anti-ICP | Segmentação, exclusões, qualificação, vendas |
| 5.4 Problemas | Hook, dor, ângulos |
| 5.5 Alternativas | Objeções LP, vendas |
| 5.6 Proposta de valor | Headlines, hero LP |
| 5.7 Narrativa | Storyline LP, criativo |
| 5.8 Claims | Tudo que é texto público; só permitidos ou teste explícito |
| 5.9 (esta tradução) | Handoff para produção |

## Campos obrigatórios do schema JSON (auditoria)

Para passar em `--audit`, cada bloco deve ter texto ou listas não vazias nos campos que o canônico lista:

- **Plano de mídia:** beachhead, canais prováveis, ângulos, premissas, ICP/anti-ICP, oferta, critérios de lead correto.
- **Briefing criativo:** persona, hook, dor, mecanismo, prova, CTA (tom e tabus recomendados se houver compliance).
- **LP:** narrativa, seções, promessa, prova, objeções, formulário, escopo, CTA.
- **Copy de anúncios:** pelo menos um item em hooks, headlines e CTAs; variações e claims explícitos.
- **Vendas:** promessa vista pelo lead, objeções, anti-ICP, perguntas de qualificação, limites da oferta.
- **Tracking:** persona, hook, dor, ângulo, etapa (dimensões para UTM/creative ID).
- **Matriz determinística:** cada elemento estratégico (POV/Differentiator/Proof Point/Oferta) com `tracking_event` em PascalCase preenchido.
- **Variações por canal:** ângulo de copy + headline adaptado para Email, LP, Call de Vendas, LinkedIn e WhatsApp.
- **Message-match audit:** 4 checks booleanos respondidos (headline, promessa, CTA, tracking).

## Matriz Determinística (tracking event obrigatório)

Cada **elemento estratégico** do DEOC vira **uma linha** com colunas fixas. O `tracking_event` em **PascalCase** é a coluna mais sensível: amarra o ângulo veiculado em mídia ao evento de conversão medido na plataforma. Sem ele, não dá pra otimizar por ângulo nem atribuir corretamente pós-iOS 14.5 (attribution windows reduzidas para 7d-click + 1d-view).

| Elemento | Headline Ad | Headline LP | Subheadline LP | CTA | Sales pitch step | Tracking Event |
|---|---|---|---|---|---|---|
| **POV** — "Rooftop é experiência, não só vista" | Belô em altura: o rooftop que vira a noite | A vista é o começo. A noite é nossa. | Drinks autorais + DJ residente toda quinta a sábado | Reservar mesa | Abertura: framing experiência > vista | `ViewBeloRooftop` |
| **Differentiator** — Cozinha autoral assinada | A cozinha que o crítico chamou de "imperdível" | Assinatura do chef X, prêmio Y 2024 | Menu sazonal de 9 pratos com produtos da serra | Ver cardápio | Slide 3: prova social + diferencial chef | `ViewBeloMenu` |
| **Proof Point 1** — 4.8 no Google (1.2k reviews) | 4.8 estrelas. 1.200 pessoas concordam. | "O melhor rooftop de BH" — repetido 312 vezes | Veja o que estão falando antes de reservar | Ler reviews | Objeção "vale a pena?": jogar prova | `ClickBeloReviews` |
| **Proof Point 2** — Lista de espera 3 semanas | Por que tem fila de 3 semanas? | A demanda virou nosso melhor termômetro | Garanta sua data antes do próximo lote abrir | Reservar agora | Urgência real (não fabricada) | `LeadBeloReserva` |
| **Oferta** — Almoço executivo R$ 89 com vista | Almoço executivo com a vista do Belô — R$ 89 | Entrada + principal + sobremesa, ter-sex | Mesma cozinha do jantar, preço de almoço | Quero o executivo | Fechamento: oferta de baixo atrito de entrada | `LeadAlmocoExecutivo` |

**Naming convention do tracking_event:** PascalCase, verbo + objeto + qualificador. Padrões aceitos: `View<Algo>`, `Click<Algo>`, `Lead<Algo>`, `Purchase<Algo>`. Eventos derivados (`ViewContent`, `Lead`, `Purchase`) são os do Meta/GA4; o nome interno aqui é o **rótulo semântico** que será mapeado depois pelo time de tracking.

## Variações por Canal (mesmo núcleo, ângulo adaptado)

A oferta não muda; **a vestimenta muda**. Promessa, ICP e prova permanecem; o que se adapta é o ângulo de leitura de cada canal — tempo de atenção, formato, momento mental do leitor.

| Canal | Ângulo de copy | Headline adaptado |
|---|---|---|
| **Email** | Carta pessoal do gestor: contexto + razão da escolha do destinatário + convite. Tom 1:1, leitura calma. | "[Nome], reservei uma mesa pra te mostrar o que mudou no Belô" |
| **LP** | Storytelling completo com prova encadeada (hero → mecanismo → prova → oferta → CTA). Leitura ativa, intenção alta. | "A vista é o começo. A noite é nossa." |
| **Call de Vendas** | Roteiro consultivo: pergunta de qualificação → dor → mecanismo → prova → oferta → fechamento. Diálogo, não monólogo. | "Antes de te oferecer data, queria entender: é jantar de negócios ou comemoração?" |
| **LinkedIn** | Post profissional/curatorial: insight de mercado (hospitalidade/experiência) → caso Belô como ilustração → CTA suave. | "Por que rooftop virou a unidade de medida do jantar corporativo em BH" |
| **WhatsApp** | Mensagem curta, transacional: gatilho + oferta + CTA com link curto. Texto único, sem rolagem. | "Oi! Confirma sua mesa pro sábado? Última disponível pro pôr-do-sol às 18h. Link: [...]" |

## Message-match Audit (KlientBoost: #1 driver de bounce)

Antes de declarar a tradução pronta, **toda linha da matriz determinística** passa por 4 checks. Se 1 falha, a linha volta pra ajuste — não se publica matriz com inconsistência ad↔LP.

1. **Headline match** — o headline do ad reaparece (literal ou semanticamente próximo) no hero da LP? O lead que clicou no ad sente que chegou no lugar certo nos primeiros 3 segundos?
2. **Promessa match** — a promessa do ad é entregue (ou mantida como expectativa coerente) na LP e no roteiro de vendas? Não há "isca-e-troca" entre ângulo veiculado e oferta entregue?
3. **CTA match** — o CTA do ad ("Reservar mesa") tem correspondência clara no CTA primário da LP? Verbo, objeto e nível de compromisso batem?
4. **Tracking match** — o `tracking_event` reflete a promessa do ad e dispara no momento certo da LP/funil? Um evento `LeadAlmocoExecutivo` não pode disparar em quem clicou em ad de jantar romântico.

Auditoria sai como tabela booleana por linha; `--audit` sinaliza qualquer linha com falha.

## N2 (trecho relevante do playbook 13, seção 6)

O DEOC (e portanto sua tradução) dialoga com N2 quando **orienta mídia, criativo, LP e vendas**. Tradução incompleta ou genérica (“ver DEOC”) viola o espírito do critério **“pode ser usado por IA e humanos sem recoletar contexto”**.

## O que evitar (seção 8 + 5.9)

- Matriz só com títulos, sem conteúdo acionável.
- Headline ou hook com **claim proibido** ou sem âncora quando o DEOC exige prova.
- LP ou anúncio **desconectados** da promessa que vendas assumem.
- Tracking sem dimensões alinhadas a persona, mensagem e etapa — impossibilita aprendizado por ângulo.

## Legado

Playbooks **04 (DCC)** e **10 (UCM)** podem inspirar formato de briefing antigo; a **fonte de verdade** continua sendo o DEOC e a matriz **5.9**.
