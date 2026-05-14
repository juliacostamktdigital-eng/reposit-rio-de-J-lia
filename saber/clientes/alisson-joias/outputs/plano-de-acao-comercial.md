# Plano de Ação Comercial — Alisson Joias
**POP 8.3 | Módulo Comercial**
**Data:** 07/05/2026
**Diagnósticos de entrada:** `ee-s4-diagnostico-comercial` · `ee-s4-cliente-oculto` · `analise-crm-receita`

---

## Premissa

Este documento opera em dois níveis. O nível estratégico responde às perguntas de **como** o comercial deveria funcionar — metodologia, estrutura de time, canal e automação. O nível tático traduz essas decisões em ações com prazo e responsável.

A Alisson Joias já possui um Playbook de Vendas aprovado (referência interna) que descreve o modelo "To Be". O diagnóstico revelou que a operação atual está significativamente abaixo desse modelo. Este plano é o mapa de transição.

---

## PARTE 1 — Avaliação Estratégica do Processo Comercial

### 1.1 Metodologia de Vendas — Existe uma? É adequada?

**Situação atual:** Não existe metodologia formal documentada. O processo comercial é intuitivo, baseado na experiência individual de cada consultora. O resultado: cada atendimento tem uma cadência diferente, qualidade inconsistente e sem critério de priorização de leads.

**Comparativo com o mercado:**

| Metodologia | Adequação ao contexto Alisson Joias | Avaliação |
|---|---|---|
| **BANT** (Budget, Authority, Need, Timing) | Alta — simples, direta, funciona em B2C consultivo de ticket médio-alto via WhatsApp | **Recomendada** |
| SPICED (Situation, Pain, Impact, Critical Event, Decision) | Média — mais adequada a ciclos longos B2B com múltiplos stakeholders | Não se aplica |
| MEDDIC | Baixa — desenhada para vendas enterprise complexas | Não se aplica |
| Venda Consultiva pura | Alta — mas exige playbook e treinamento formalizado para funcionar em escala | Complementar ao BANT |

**Recomendação:** Adotar **BANT como metodologia oficial de qualificação** — já previsto no Playbook interno. O processo não precisa parecer um interrogatório: BANT é aplicado de forma conversacional, dentro do fluxo natural de atendimento no WhatsApp.

**As 4 perguntas estruturantes por lead:**

| Dimensão | Pergunta para o atendimento | O que qualifica |
|---|---|---|
| **Budget** | "Você já tem uma referência de valor em mente para o par?" | Acima de R$2.000 = entra no funil ativo |
| **Authority** | "Você e seu noivo(a) vão decidir juntos ou você está pesquisando sozinha?" | Decisora única ou casal = prioridade |
| **Need** | "É para um casamento já marcado ou ainda está na fase de pesquisa?" | Evento definido = urgência real |
| **Timing** | "Qual é a data do casamento?" | ≤ 30 dias = lead quente; > 90 dias = nutrição |

---

### 1.2 Estrutura do Time — É a ideal?

**Situação atual:** Todas as consultoras executam simultaneamente o papel de **SDR** (qualificação, primeiro contato, triagem) e **Closer** (apresentação, proposta, fechamento). Com 100–200 leads simultâneos por consultora, o resultado é previsível: ninguém faz nenhum dos dois bem.

**O problema da estrutura atual:**

```
Lead entra → Consultora (faz tudo) → Tenta qualificar + propor + fechar ao mesmo tempo
                                     → Sobrecarga → Tarefas genéricas → Leads zumbi
```

**Modelo ideal (alinhado ao Playbook interno):**

```
Lead entra → SDR IA (triagem BANT 24/7) → Lead qualificado (SAL)
                                         → Consultora Closer (fechamento consultivo de alto valor)
                                         Lead frio → Nutrição automática (Funil de Refugo)
```

**O que muda para cada papel:**

| Papel | Função atual (As Is) | Função ideal (To Be) |
|---|---|---|
| **SDR IA** | Não existe | Triagem BANT 24/7, resposta imediata, lead scoring, handoff para consultora |
| **Consultora** | SDR + Closer + Admin de CRM | Closer: recebe só leads ⭐⭐⭐⭐⭐, foco em qualificação emocional, curadoria visual e fechamento |
| **Gerente Comercial** | Acompanhamento reativo de tarefas | Pipeline review ativo, forecast semanal, coaching de fechamento |

**Impacto esperado da separação de papéis:** Consultora que hoje atende 150 leads com 19% de conversão, com o filtro do SDR IA, atenderá 30–40 leads qualificados com potencial de conversão de 40–60% — mais resultado, menos esforço.

---

### 1.3 Modelo de Atendimento e Canal — WhatsApp é o certo? Como usar?

**Situação atual:** WhatsApp é o canal correto para o perfil do ICP ("Pop Ficando Rico" — decisão emocional, rápida, via celular). O problema não é o canal; é como ele está sendo usado.

**Gaps identificados no uso do canal:**

| Gap | Evidência | Impacto |
|---|---|---|
| Consultoras saindo do Kommo para WhatsApp pessoal | Screenshot CRM: "Claro, vou te chamar no meu WhatsApp de consultora para ficar melhor" | Pipeline invisível ao gestor — dados perdidos |
| Formulário Meta Ads incompatível com WhatsApp | Lead de mídia não pode receber mensagem ativa — exige template pago | Taxa de contato zero nas primeiras horas |
| Automação de abertura com template mal escrito | "a mensagem e a frequência com que nos comunicamos por enquanto..." (cliente oculto) | Primeira impressão ruim em posicionamento premium |

**Modelo ideal de canal:**

```
Meta Ads → Click-to-WhatsApp (lead inicia conversa)
                ↓
         Número central do Kommo (WhatsApp Business API)
                ↓
         SDR IA (bot BANT) → Score → Roteamento
                ↓                         ↓
         Consultora via Kommo         Nutrição automática
         (100% dentro do CRM)         (Funil de Refugo)
```

**Ligação telefônica:** Não é o modelo primário para Alisson Joias. O cliente de aliança e joia de ticket R$4.800 compra via WhatsApp com curadoria visual (fotos/vídeos). Ligação entra apenas como recurso de resgate para leads ⭐⭐⭐⭐⭐ que não responderam em 24h.

---

### 1.4 Automação — O que existe? O que deveria existir?

**Situação atual:**

| Automação existente | Status | Problema |
|---|---|---|
| SalesBot de boas-vindas (abertura de conversa) | Ativo | Template com texto confuso; não faz triagem BANT |
| Follow-up automático de leads sem resposta | Ativo com bug | Disparo duplicado identificado (mesma mensagem múltiplas vezes) |
| Automação pós-venda | Ativa | Funcional — ponto positivo |
| SDR IA com qualificação BANT | Não existe | Principal gap do processo |
| Lead scoring automático | Não existe | Sem priorização → consultoras trabalham tudo por igual |
| Funil de recompra (30/60/90 dias) | Não existe | 90% dos novos clientes não retornam — "balde furado" |
| Funil de refugo (leads parados) | Não existe | 259 leads em Orçamento parados = R$1,5M potencial não trabalhado |

**Modelo de automação ideal — 3 Funis:**

**Funil 1 — Novos Leads (aquisição)**
```
Entrada Click-to-WhatsApp → Bot BANT (coleta Budget, Need, Timing) → Lead Score
→ ⭐⭐⭐⭐⭐ Quente (>30pts): Notificação imediata para consultora → Atendimento < 5min
→ ⭐⭐⭐ Morno (15-29pts): Fila de atendimento + nutrição
→ ⭐ Frio (<15pts): Catálogo automático + nutrição passiva 7 dias
```

**Funil 2 — Recompra (fidelização)**
```
Cliente pós-venda → 30 dias sem compra → Disparo automático (bônus/novidade)
→ Responde: Cria card no funil principal (tag "Recompra")
→ Não responde: 60 dias → Segunda tentativa com oferta diferenciada
→ 90 dias sem resposta: Nutrição passiva mensal
```

**Funil 3 — Refugo (proativo)**
```
Lead parado > 7 dias sem atividade → Consultora em momento de baixo fluxo →
Contato proativo com novidade/coleção nova → Aquecimento para funil principal
```

---

### 1.5 Síntese — As Is vs To Be

| Dimensão | As Is (hoje) | To Be (modelo ideal) |
|---|---|---|
| **Metodologia** | Intuitiva, inconsistente | BANT estruturado — consultivo e fluido |
| **Estrutura** | Consultoras fazem tudo (SDR + Closer) | SDR IA triagem + Consultoras como Closers |
| **Canal** | WhatsApp fragmentado (CRM + pessoal) | WhatsApp 100% centralizado no Kommo via API |
| **Automação** | SalesBot com bug, sem scoring | 3 funis + lead scoring BANT + SDR IA |
| **Priorização** | Nenhuma — atende por ordem de chegada | Lead scoring define quem atende primeiro |
| **Recompra** | Inexistente (90% não retornam) | Funil automático 30/60/90 dias |
| **Pós-venda** | Automação ativa (ponto positivo) | Manter + integrar ao funil de recompra |

---

## PARTE 2 — Plano de Ação (Estratégico + Tático)

### Matriz de Priorização

| # | Ação | Nível | Impacto | Esforço | Tipo |
|---|---|---|---|---|---|
| 1 | Migrar Meta Ads de formulário para Click-to-WhatsApp | Tático | Alto | Baixo | ⚡ Quick Win |
| 2 | Corrigir bug de disparo duplicado do SalesBot | Tático | Alto | Baixo | ⚡ Quick Win |
| 3 | Implementar CTA de fechamento pós-proposta | Tático | Alto | Baixo | ⚡ Quick Win |
| 4 | Script BANT conversacional para consultoras | Tático | Médio | Baixo | ⚡ Quick Win |
| 5 | Proibir atendimento fora do Kommo + treinamento | Estratégico | Alto | Médio | 🏗️ Estrutural |
| 6 | Implementar lead scoring BANT no Kommo | Estratégico | Alto | Médio | 🏗️ Estrutural |
| 7 | Configurar SDR IA com triagem BANT (bot Kommo) | Estratégico | Alto | Alto | 🏗️ Estrutural |
| 8 | Ativar Funil de Recompra (30/60/90 dias) | Estratégico | Alto | Alto | 🏗️ Estrutural |
| 9 | Estruturar Funil de Refugo com routina da consultora | Estratégico | Médio | Médio | 🏗️ Estrutural |
| 10 | Revisão semanal de pipeline + coaching de fechamento | Tático | Alto | Baixo | 📅 Recorrente |

---

### ⚡ QUICK WINS — 7 dias

---

**QW-01 — Migrar campanha Meta Ads para Click-to-WhatsApp**

| | |
|---|---|
| **O quê** | Trocar o objetivo da campanha ativa de "Geração de Leads (formulário)" para "Mensagens — Click-to-WhatsApp" |
| **Por quê** | Formulário cria janela de 24h intransponível — lead de mídia chega sem poder ser contactado via WhatsApp. Com Click-to-WhatsApp o lead inicia a conversa, eliminando a barreira do Message Template. Conversão atual: 0,54% vs benchmark 3–8% |
| **Quem** | Leivany (GT) |
| **Quando** | Até 48h após aprovação |
| **Onde** | Meta Ads Manager |
| **Como** | Duplicar conjunto de anúncios ativo → alterar objetivo para Mensagens → vincular ao número Kommo → configurar mensagem de abertura automática alinhada ao posicionamento premium |
| **Quanto** | Sem custo adicional — redistribuição do budget existente |
| **Métrica** | Taxa de contato realizado ≥ 60% em 14 dias pós-mudança |

---

**QW-02 — Corrigir bug de disparo duplicado do SalesBot**

| | |
|---|---|
| **O quê** | Identificar e corrigir a regra de automação que dispara a mesma mensagem repetidamente para o mesmo lead sem resposta |
| **Por quê** | Lead "Lúcia Mãe do Benício" recebeu a mesma mensagem template em loop sem evolução de etapa — comportamento que queima o contato e sinaliza automação de baixa qualidade, inconsistente com posicionamento premium |
| **Quem** | Tássio (Kommo admin) |
| **Quando** | Até 48h após aprovação |
| **Onde** | Kommo — SalesBot, configuração de sequência de follow-up |
| **Como** | Auditar trigger da regra → adicionar condição "máximo N disparos por lead" e "somente se sem resposta nas últimas Xh" → testar em lead homologação antes de reativar |
| **Quanto** | Sem custo adicional |
| **Métrica** | Zero ocorrências de disparo duplicado na próxima revisão semanal |

---

**QW-03 — Implementar CTA padrão de fechamento pós-proposta**

| | |
|---|---|
| **O quê** | Criar mensagem padrão enviada imediatamente após a proposta, com pergunta de próximo passo e direcionamento |
| **Por quê** | Cliente Oculto (C6: 4/10): proposta entregue sem CTA → lead assumiu o controle → conversa esfriou. Em joalheria de R$4.812 de ticket médio, cada hora sem CTA é conversão perdida. Gargalo Qualificado→Orçamento no canal pago: 28,9% vs benchmark 50–65% |
| **Quem** | Account V4 (texto) + Alisson (aprovação) + Consultoras (adoção) |
| **Quando** | Texto aprovado em 72h; adotado em 7 dias |
| **Onde** | WhatsApp via Kommo — Quick Reply salvo no sistema |
| **Como** | Template: *"Essas são as opções que separei para vocês com carinho 💛 Qual das alianças mais combina com o casal? Posso reservar enquanto conversamos os últimos detalhes — leva só 5 minutos."* Salvar como Quick Reply no Kommo para facilitar uso |
| **Quanto** | Sem custo |
| **Métrica** | 100% das propostas com CTA no mesmo dia — verificado na revisão semanal |

---

**QW-04 — Script BANT conversacional para consultoras**

| | |
|---|---|
| **O quê** | Criar e distribuir roteiro de 4 perguntas BANT integradas ao fluxo natural de atendimento, incluindo apresentação pessoal e perguntas de contexto de compra |
| **Por quê** | Cliente Oculto (C2: 5/10 e C3: 6/10): consultora enviou catálogo sem se apresentar e qualificou apenas espessura/tamanho — sem contexto de data, urgência ou orçamento. Sem BANT, a consultora não tem âncoras para criar urgência legítima nem personalizar o fechamento |
| **Quem** | Account V4 (cria) + Alisson (aprova) + Consultoras (adotam) |
| **Quando** | Script em 72h; adoção em 7 dias |
| **Onde** | WhatsApp via Kommo |
| **Como** | Sequência: *(Abertura)* "Olá, [Nome]! Sou a [Consultora], especialista em alianças da Alisson Joias 💛 Me conta — é aliança para casamento próximo ou ainda estão pesquisando?" → *(Need/Timing)* "A data já está definida?" → *(Budget)* "Têm uma referência de valor em mente para o par?" → *(Authority)* "Vocês dois vão escolher juntos?" → Catálogo segmentado |
| **Quanto** | Sem custo |
| **Métrica** | C2 e C3 ≥ 7/10 no próximo Cliente Oculto |

---

### 🏗️ ESTRUTURAIS — 30 dias

---

**EST-01 — Implementar lead scoring BANT no Kommo**

| | |
|---|---|
| **O quê** | Criar campo de score (1–5 estrelas) no Kommo com critérios BANT objetivos e SLA de resposta por score |
| **Por quê** | Sem scoring, todas as consultoras atendem todos os leads com igual prioridade — com 100–200 leads/consultora, o resultado são 226+ tarefas em atraso e leads ⭐⭐⭐⭐⭐ perdendo o SLA de 5 minutos junto com leads frios |
| **Quem** | Account V4 (define critérios) + Tássio (configura Kommo) + Gerente (treina time) |
| **Quando** | Configurado em 15 dias; time treinado em 30 dias |
| **Onde** | Kommo — campo customizado + regra de alerta por score |
| **Como** | Score BANT: Budget declarado acima de R$2.000 (+2pts) · Evento com data (+2pts) · Urgência ≤ 30 dias (+2pts) · Decisora única (+1pt) · Canal orgânico (+1pt) = Máx 8pts. Faixas: ⭐⭐⭐⭐⭐ (7-8pts) resposta em < 5min; ⭐⭐⭐⭐ (5-6pts) < 1h; ⭐⭐⭐ (3-4pts) régua automática 4h; ⭐⭐ (<3pts) nutrição passiva |
| **Quanto** | Sem custo adicional |
| **Métrica** | 100% dos leads com score preenchido; zero leads ⭐⭐⭐⭐⭐ sem resposta > 5min na revisão semanal |

---

**EST-02 — Configurar SDR IA com triagem BANT no Kommo**

| | |
|---|---|
| **O quê** | Configurar o SalesBot do Kommo como SDR IA: resposta imediata 24/7 + coleta das 4 perguntas BANT + score automático + roteamento por temperatura |
| **Por quê** | Sem SDR IA, consultoras Farmer estão sendo forçadas a operar como Hunter sem cadência ou script — resultado: 0,54% de conversão no canal pago. O SDR IA resolve a janela noturna, a triagem de leads frios e libera a consultora para o que ela faz bem: fechar |
| **Quem** | Tássio (configuração técnica Kommo) + Account V4 (roteiro do bot) + Alisson (aprovação) |
| **Quando** | Piloto com canal de mídia em 30 dias |
| **Onde** | Kommo — SalesBot + Cloud API WhatsApp |
| **Como** | Fluxo: Entrada → Bot apresenta Alisson Joias + faz P1 (ocasião/produto) → P2 (data do evento) → P3 (referência de valor) → P4 (decide sozinho ou casal) → Score automático → Roteamento: Quente = notificação consultora; Morno = fila + mensagem de valor; Frio = catálogo automático + nutrição |
| **Quanto** | Sem custo adicional (Kommo já possui SalesBot no plano ativo) |
| **Métrica** | Taxa de contato realizado (lead → resposta humana) ≥ 60% em leads de mídia paga com o bot ativo, em 30 dias |

---

**EST-03 — Ativar Funil de Recompra (30/60/90 dias)**

| | |
|---|---|
| **O quê** | Criar funil dedicado de pós-venda no Kommo com automação de reengajamento aos 30, 60 e 90 dias após a compra |
| **Por quê** | 90% dos novos clientes não retornam no mês seguinte por ausência de contato ativo. Base de clientes recorrentes representa hoje 40–50% do faturamento — e essa base cresce de forma passiva, sem estratégia. O funil de recompra ativa esse ativo |
| **Quem** | Tássio (configura Kommo) + Account V4 (cria copy das mensagens) + Alisson (aprova) |
| **Quando** | Configurado em 20 dias; ativo em 30 dias |
| **Onde** | Kommo — funil separado + SalesBot |
| **Como** | D+30: mensagem com novidade de coleção ou peça complementar ao que comprou · D+60: oferta diferenciada (ex: gravação gratuita, desconto em peça complementar) · D+90: convite para evento presencial ou lançamento exclusivo. Se responder em qualquer etapa → card automático criado no funil principal com tag "Recompra" |
| **Quanto** | Sem custo adicional |
| **Métrica** | Taxa de recompra em 90 dias ≥ 15% da base de clientes ativos (hoje estimada em ~0%) |

---

**EST-04 — Padronizar uso do CRM: zero atendimento fora do Kommo**

| | |
|---|---|
| **O quê** | Definir regra operacional clara (nenhum atendimento no WhatsApp pessoal da consultora) + configurar campos obrigatórios por etapa no Kommo |
| **Por quê** | Consultoras migrando para WhatsApp pessoal torna o pipeline invisível — gestor não tem dados, forecast é impossível, análise 80/20 e LTV não são calculáveis. É a raiz da maioria dos problemas de CRM identificados |
| **Quem** | Alisson/Gerente (define regra e comunicação ao time) + Tássio (configura campos obrigatórios por etapa) |
| **Quando** | Regra definida em 7 dias; conformidade verificada em 30 dias |
| **Onde** | Kommo + WhatsApp Business centralizado |
| **Como** | Reunião com time: "Por que isso importa para suas comissões" (sem dados = sem forecast = meta imprecisa). Configurar campo "Valor real" como obrigatório na etapa Orçamento (bloqueia avanço de etapa sem preenchimento). Meta de conformidade: ≥ 80% dos negócios com valor preenchido real (não R$1) |
| **Quanto** | Sem custo adicional |
| **Métrica** | ≥ 80% dos deals em Orçamento ou superior com valor real preenchido; zero evidências de leads sendo conduzidos fora do Kommo — verificado em próximo Cliente Oculto e revisão semanal |

---

### 📅 RECORRENTES

---

**REC-01 — Pipeline Review semanal + coaching de fechamento**

| | |
|---|---|
| **O quê** | Reunião semanal de 30 min: revisão de pipeline (tarefas atrasadas, leads zumbi, forecast) + 1 análise de conversa real por semana (coaching de fechamento baseado em evidência) |
| **Quem** | Gerente Comercial / Alisson |
| **Quando** | Toda segunda-feira antes do início do atendimento |
| **Métrica** | Zero leads sem tarefa específica com prazo; zero leads em etapa > 7 dias sem atividade; mínimo 1 insight de fechamento por semana |

---

### Resumo Executivo

| Nível | Tipo | Qtd | Prazo | Impacto esperado |
|---|---|---|---|---|
| Estratégico | Decisões de modelo | 4 | 30 dias | Separação SDR/Closer, automação BANT, 3 funis ativos, CRM centralizado |
| Tático | Quick Wins | 4 | 7 dias | Canal de mídia desbloqueado, bug corrigido, CTA implementado, BANT em uso |
| Tático | Estruturais | 4 | 30 dias | Lead scoring, SDR IA, recompra e padronização CRM |
| Tático | Recorrentes | 1 | Contínuo | Pipeline gerenciado com dados reais |

**A decisão de maior impacto estratégico:** Separar o papel de SDR (hoje inexistente ou executado por consultoras sem cadência) do papel de Closer (consultoras). Enquanto essa separação não existir, escalar tráfego pago apenas aumenta o caos — mais leads frios chegando para um time que não tem processo para convertê-los.

**A ação de maior ROI imediato:** Click-to-WhatsApp (QW-01). O diagnóstico comprova que quando o Meta Ads converte (jan/2026), o ROAS é de 8,2x e o CPA de R$475 é sustentável. A barreira não é investimento — é o processo de contato. A mudança de tipo de campanha remove esse bloqueio sem custo adicional.

---

## O que NÃO está neste plano e por quê

| Ação excluída | Motivo |
|---|---|
| Contratar SDR humano dedicado | SDR IA deve ser testado primeiro — confirmar hipótese com dados antes de gerar custo fixo de headcount |
| Reconfigurar campanha de Engajamento e Venda Meta Ads | Budget marginal (R$37 em Venda, R$1.058 em Engajamento) — impacto menor que otimizar o canal de leads que já tem volume |
| Implantar novo CRM | O problema é de uso, não de ferramenta — Kommo tem todas as funcionalidades necessárias |
| Definir política de desconto | Fora do escopo diagnóstico — decisão comercial de Alisson; o CTA e o script BANT reduzem a pressão de desconto sem precisar de política formal |

---

## Próxima skill sugerida

Com o plano de ação comercial aprovado, os gaps de processo estão mapeados e priorizados. A próxima etapa é consolidar todos os diagnósticos do módulo (Mídia + CRO + Comercial) em um relatório unificado de travas com scoring e sequenciamento causal:

→ `/diagnostico-travas-scoring` — Consolida os outputs de todas as dimensões, identifica a Restrição Maior e define a ordem de resolução para o deck de entrega final.
