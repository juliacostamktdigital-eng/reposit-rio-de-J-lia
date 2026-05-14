# Mapa Canônico de Assets AI-Native - Cliente Ponta a Ponta
**Atualizado:** 2026-04-30  
**Fonte final:** consolidação em `assets/canonicos`; base canônica original + canônico original sem skill merge dedicada.  
**Decisão de merge:** sem skill dedicada; mantido como mapa transversal da jornada em `assets/canonicos`.


Status: v1 para workshop  
Escopo: Marketing OS / OS do Executar para clientes de Inside Sales / leadgen  
Objetivo: definir quais assets precisam existir em cada etapa para uma operação AI-native atender um cliente de ponta a ponta com rastreabilidade, qualidade e melhoria contínua.

## 1. Princípio

Um processo AI-native não é "usar IA para fazer peças mais rápido". É desenhar a operação para que cada etapa gere contexto estruturado, outputs versionáveis e dados reutilizáveis pela próxima etapa.

O fluxo precisa permitir:

- entrar com contexto bruto do cliente;
- transformar contexto em estratégia;
- transformar estratégia em assets executáveis;
- executar campanha/criativos com tracking;
- conectar mídia, criativo, lead e avanço no funil;
- aprender com os resultados;
- rebriefar o próximo ciclo sem começar do zero.

## 2. Definição de asset

Asset é qualquer artefato necessário para o processo rodar, ser auditado ou melhorar.

Pode ser:

- documento estratégico;
- planilha;
- schema de dados;
- template;
- checklist;
- prompt/skill;
- taxonomia;
- relatório;
- biblioteca;
- integração;
- evidência;
- decisão registrada.

## 3. Jornada ponta a ponta e assets por etapa

### Etapa 0 - Entrada comercial e handoff sales-to-ops

Objetivo: impedir que a operação comece sem saber o que foi vendido, prometido e assumido.

Assets obrigatórios:

- Brief sales-to-ops.
- Resumo do contrato e escopo.
- Registro de promessas comerciais.
- Lista de stakeholders e aprovadores.
- Lista de riscos/red flags.
- Critério inicial de sucesso.

Definition of done:

- Ops entende a promessa feita ao cliente.
- Existem exclusões e limites documentados.
- Existe um dono interno da conta.
- Existe um aprovador final do lado do cliente.

Uso AI-native:

- A IA deve conseguir ler o handoff e gerar o primeiro mapa de hipóteses, riscos e perguntas de discovery.

### Etapa 1 - Discovery e coleta de contexto

Objetivo: capturar o contexto necessário para estratégia, copy, mídia, tracking e handoff comercial.

Assets obrigatórios:

- Questionário de discovery.
- Transcrição da call de kickoff/discovery.
- Mapa de negócio do cliente.
- Mapa de ICP/personas.
- Mapa de oferta e produtos.
- Inventário de ativos existentes.
- Inventário de acessos necessários.

Definition of done:

- O cliente explicou o negócio nas próprias palavras.
- Dores, desejos, objeções e diferenciais estão capturados.
- O time sabe o que já existe e o que precisa construir.

Uso AI-native:

- A IA deve extrair do discovery: ICPs, jobs-to-be-done, dores, objeções, claims, restrições, riscos de conversão e hipóteses iniciais de canais.

### Etapa 2 - Diagnóstico e maturidade

Objetivo: separar o que é problema de demanda, problema de conversão, problema de oferta, problema de tracking ou problema comercial.

Assets obrigatórios:

- Diagnóstico N1/N2/N3 por componente.
- Auditoria de marketing atual.
- Auditoria de funil comercial.
- Baseline de dados.
- Mapa da equação de resultado.
- Lista de gaps para N2.

Definition of done:

- Cada componente tem status, evidência e dono.
- A causa do problema não fica descrita como "resultado ruim".
- Existe uma lista priorizada de gaps.

Uso AI-native:

- A IA deve gerar uma matriz de gaps, sugerir prioridades e apontar dados faltantes antes de recomendar execução.

### Etapa 3 - Decisão do pacote v1 de assets

Objetivo: decidir, a partir de diagnóstico e benchmark, quais assets realmente precisam ser construídos no primeiro ciclo.

Assets obrigatórios:

- Ficha de cohort/segmento.
- Lista curta de assets v1.
- Lista do que fica fora do ciclo.
- Matriz de dependências do cliente.
- Critérios de N2 por componente.

Definition of done:

- O time sabe quais assets precisa construir agora e quais não entram no ciclo.
- Nenhum documento abstrato vira etapa só por existir.

Uso AI-native:

- A IA deve transformar diagnóstico e benchmark em uma lista objetiva de assets, dependências e critérios de pronto.

### Etapa 4 - Estratégia de oferta, mercado e copy

Objetivo: transformar contexto em mensagem e posicionamento executáveis.

Assets obrigatórios:

- Benchmark de mercado/segmento.
- UCM ou mapa de caso de uso.
- DCC ou documento de concepção de copy.
- Documento de copy final.
- Mapa de personas/comitê de compra.
- Biblioteca de hooks, ângulos, dores e desejos.
- Claims permitidos e proibidos.

Definition of done:

- O time consegue escrever LP, anúncio, roteiro e CTA sem depender de memória do especialista.
- Existe uma narrativa central e suas variações por persona/ângulo.

Uso AI-native:

- A IA deve conseguir gerar variações coerentes de copy porque recebeu um documento canônico, não apenas um briefing solto.

### Etapa 5 - Plano de mídia e estrutura de campanha

Objetivo: traduzir estratégia em investimento, canais, metas, hipóteses e estrutura de teste.

Assets obrigatórios:

- Plano de mídia.
- Projeção pessimista/provável/otimista.
- Estrutura planejada de campanha.
- Mapa de hipóteses por campanha.
- Guardrails de otimização.

Definition of done:

- O investimento tem lógica por canal.
- Cada campanha tem objetivo, etapa do funil, meta e hipótese.
- As métricas de leitura estão definidas antes do launch.

Uso AI-native:

- A IA deve conseguir simular cenários, sugerir distribuição de verba, identificar inconsistências de funil e gerar um plano de teste.

### Etapa 6 - Tracking, UTMs, IDs e fonte da verdade

Objetivo: garantir que cada lead possa ser conectado a campanha, criativo e avanço no funil.

Assets obrigatórios:

- Taxonomia UTM.
- Padrão de nomenclatura de campanha.
- Padrão de nomenclatura de criativo.
- Mapa de campos CRM.
- Protocolo de teste de tracking.
- Fonte da verdade de leads.
- Dicionário de dados.

Definition of done:

- Existe match confiável entre investimento, campanha, criativo, lead e MQL/oportunidade/venda.
- Um lead teste percorre todo o caminho com dados preservados.

Uso AI-native:

- A IA deve conseguir ler os parâmetros e agrupar performance por formato, hook, persona, dor, ângulo, etapa de funil e versão.

### Etapa 7 - Produção criativa e LP

Objetivo: produzir assets de campanha a partir da estratégia e com hipótese rastreável.

Assets obrigatórios:

- Briefing criativo video-first.
- Roteiros de vídeo.
- Copies de anúncio.
- Direção visual.
- LP ou ponto de conversão.
- Checklist de qualidade criativa.
- Checklist de qualidade da LP.
- Mapa de versões dos criativos.

Definition of done:

- Cada criativo nasce com hipótese e ID.
- A LP/ponto de conversão está coerente com a promessa do anúncio.
- Claims, CTA e formulário estão validados.

Uso AI-native:

- A IA deve acelerar criação e variação, mas sempre usando DCC, hipótese, taxonomia e restrições.

### Etapa 8 - Go-live e QA operacional

Objetivo: preparar contas, pixels/tags, conversões, públicos e estruturas de campanha antes de ativar verba.

Assets obrigatórios:

- Setup de Campanhas Meta Ads quando Meta entra no plano.
- Setup de Campanhas Google Ads quando Google entra no plano.
- Checklist de conta, permissões e faturamento.
- Pixel/CAPI Meta validado quando aplicável.
- GTM/tag/conversões Google validadas quando aplicável.
- Públicos/listas/sinais criados.
- Campanhas em rascunho com IDs e UTMs.
- Lead teste na planilha backup.
- Checklist de go-live.

Definition of done:

- Conta, tracking, públicos, estrutura, UTMs, planilha backup e lead teste estão validados antes do go-live.

Uso AI-native:

- A IA deve conseguir comparar o setup real com o checklist e apontar gaps antes do investimento rodar.

### Etapa 9 - Execução e publicação

Objetivo: colocar no ar o que já foi preparado no setup, sem improvisar estrutura no momento do launch.

Assets obrigatórios:

- Checklist de publicação.
- Registro de aprovação interna.
- Registro de aprovação do cliente quando necessário.
- Registro de hipótese de campanha.
- Log de launch.

Definition of done:

- Campanha está no ar com estrutura aprovada, criativos publicados, horário de go-live e hipótese documentada.

Uso AI-native:

- A IA deve conseguir comparar planejado vs publicado e detectar divergências de criativo, orçamento, status ou hipótese.

### Etapa 10 - Planilha de testes e leitura de performance

Objetivo: registrar testes, resultados e decisões de forma comparável.

Assets obrigatórios:

- Planilha de testes.
- Export de mídia.
- Export CRM/leads.
- Relatório de qualidade do lead.
- Registro de decisões.

Definition of done:

- Cada teste tem hipótese, variável, resultado, decisão e aprendizado.
- A leitura inclui qualidade de lead e não apenas CPL.

Uso AI-native:

- A IA deve conseguir explicar quais padrões performaram melhor e sugerir próximo ciclo.

### Etapa 11 - Handoff marketing-vendas e feedback comercial

Objetivo: fechar o loop entre geração de demanda e conversão.

Assets obrigatórios:

- SLA de atendimento.
- Roteamento de leads.
- Definição de MQL/SQL.
- Motivos de desqualificação.
- Script de abordagem comercial.
- Formulário de feedback de qualidade.
- Rotina de retorno para nurture.

Definition of done:

- Vendas sabe o que fazer com o lead.
- Marketing recebe feedback do que virou oportunidade, venda ou perda.

Uso AI-native:

- A IA deve resumir contexto do lead, sinalizar urgência, classificar motivo de perda e alimentar próximos testes de mensagem.

### Etapa 12 - Debrief N3 e backlog de growth

Objetivo: transformar dados em decisão.

Assets obrigatórios:

- Template de debrief N3.
- Backlog de hipóteses.
- Guardrails de otimização.
- Registro de decisão.
- Changelog de alterações.

Definition of done:

- O ciclo termina com decisão clara: escalar, ajustar, matar, corrigir tracking, revisar oferta ou acionar vendas.

Uso AI-native:

- A IA deve gerar leitura do que aconteceu, hipóteses prováveis e recomendações, mas a decisão final continua com o especialista.

### Etapa 13 - Canonização e rebrief

Objetivo: transformar aprendizado em sistema reutilizável.

Assets obrigatórios:

- Registro de aprendizado canônico.
- Biblioteca de padrões vencedores.
- Biblioteca de anti-padrões.
- Pack atualizado.
- Skill operacional candidata.
- Brief do próximo ciclo.

Definition of done:

- O aprendizado sai da conta e passa a servir a cohort/segmento.
- O próximo ciclo nasce do aprendizado anterior.

Uso AI-native:

- A IA deve atualizar contexto, sugerir versionamento dos packs e gerar o próximo briefing com base nos padrões aprendidos.

## 4. Assets que devem existir como "fonte de verdade" do projeto

Todo cliente deveria ter uma pasta/diretório com:

- `00_contexto/`
- `01_handoff_sales_ops/`
- `02_discovery/`
- `03_diagnostico/`
- `04_assets_v1/`
- `05_copy_e_oferta/`
- `06_midia/`
- `07_tracking_e_dados/`
- `08_criativos_e_lp/`
- `09_go_live/`
- `10_testes_e_performance/`
- `11_handoff_vendas/`
- `12_debriefs/`
- `13_aprendizados/`
- `99_inbox/`

## 5. Critério para N2 e N3

### N2 - implementado

O cliente está em N2 quando:

- os assets obrigatórios existem;
- os donos estão claros;
- os dados mínimos estão preservados;
- há evidência da execução;
- o processo consegue ser auditado.

### N3 - gerenciado

O cliente está em N3 quando:

- os dados são lidos em cadência;
- decisões são registradas;
- hipóteses entram no backlog;
- aprendizados alimentam o próximo ciclo;
- padrões são canonizados para reuso.
