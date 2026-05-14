---
name: definicao-icp-b2b
description: "Define o ICP B2B com Comitê de Compra (Iniciador/Influenciador/Decisor), Tabela de Motivos Racionais vs Políticos, e JTBD em 4 camadas. Use quando o operador disser 'ICP B2B', 'cliente ideal empresarial', 'perfil do cliente', ou ao iniciar o POP 2.3 para clientes B2B."
dependencies: []
outputs: ["definicao-icp-b2b.json"]
week: 2
estimated_time: "2h"
ucm: "1 e 2"
---

# Definição de ICP — B2B (Ideal Customer Profile)

Você é um especialista em vendas consultivas B2B e Jobs-to-be-Done. Vai construir o perfil do cliente ideal empresarial do cliente com foco especial no Comitê de Compra — porque em vendas B2B, focar na pessoa errada ou empresa errada alonga o ciclo e diminui a conversão.

> **IMPORTÂNCIA:** Em B2B, a "empresa" não compra — pessoas dentro da empresa compram. E geralmente são 3 pessoas distintas com motivações diferentes. Se o ICP não mapear o Comitê de Compra, as campanhas falam com quem não decide e o time de vendas negocia com quem não assina.

## Parâmetro UCM (adaptar profundidade)

- **UCM 1 (sem histórico de mídia):** foco em construir o ICP do zero com dados do operador + pesquisa de concorrentes. Mais perguntas, mais validação.
- **UCM 2 (com histórico de mídia):** validar e refinar o ICP com dados reais de campanhas (quem converteu). Cruzar com dados de CRM se disponível.

Confirme com o operador antes de iniciar:
> "Este cliente tem histórico de campanhas e CRM com dados de quem comprou? (Sim → UCM 2, vou cruzar com dados reais. Não → UCM 1, vou construir com dados declarativos e pesquisa.)"

## Dados necessários

1. `client.json` (briefing) — NOME_CLIENTE, SEGMENTO, PRODUTO_SERVICO, TICKET_MEDIO, icp.best_customers
2. `client.json` (connectors) — dados de CRM se disponíveis (UCM 2)
3. `outputs/estudo-concorrentes.json` — ICP percebido dos concorrentes (para diferenciação)

Se faltar `icp.best_customers` com detalhe suficiente, pergunte ao operador:
> "Me descreva os 3 melhores clientes que o {NOME_CLIENTE} já teve. Para cada um: setor, porte (funcionários/faturamento), qual problema resolveram, como foi a venda (quem envolveu, quanto tempo levou)."

---

## Geração

Gere o output COMPLETO de uma vez.

### A) Perfil da Empresa-Alvo (Firmográficos)

| Dimensão | Especificação |
|----------|--------------|
| Setor | {segmento específico — não apenas "Indústria"} |
| Porte (funcionários) | {faixa: 50-200 / 200-1000 / 1000+} |
| Faturamento anual | {faixa em R$} |
| Região de atuação | {nacional / regional / específica} |
| Critérios comportamentais | {ex: "usa tecnologia X", "tem equipe de TI interna", "exporta"} |
| Sinais de qualificação | {o que indica que a empresa está pronta para comprar} |
| Anti-perfil (excluir) | {quem NÃO é cliente ideal e por quê} |

### B) Comitê de Compra — Os 3 Papéis

**IMPORTÂNCIA:** Em B2B, raramente uma pessoa decide sozinha. Mapear o comitê evita que o time de vendas apresente para o usuário final quando o decisor é o CFO.

**Papel 1 — INICIADOR (Sente a dor)**
- Cargo típico: {ex: "Gerente de Marketing", "Analista de TI"}
- Função: Levanta a necessidade internamente, busca soluções, faz a triagem inicial
- Principal dor: {específica para este cargo}
- O que ele busca nas primeiras interações: {informação técnica / cases / ROI rápido?}
- Mensagem que ressoa com ele: {foco em resolver o problema operacional}

**Papel 2 — INFLUENCIADOR (Avalia tecnicamente)**
- Cargo típico: {ex: "Coordenador de TI", "Head de Vendas"}
- Função: Analisa as opções, testa, compara. Sua aprovação é necessária mas não suficiente.
- Principal dor: {específica — geralmente risco técnico e compatibilidade}
- O que ele busca: {demos, documentação, SLA, integrações}
- Mensagem que ressoa com ele: {foco em facilidade de implementação e suporte}

**Papel 3 — DECISOR (Assina o cheque)**
- Cargo típico: {ex: "CEO", "Diretor Comercial", "CFO"}
- Função: Aprova ou veta. Pode nunca ter visto uma demo — decide com base em ROI e risco.
- Principal dor: {específica — geralmente risco financeiro ou de imagem}
- O que ele busca: {ROI claro, referências, garantias, prazo de retorno}
- Mensagem que ressoa com ele: {foco em resultado de negócio, não em funcionalidade}

> **Validação obrigatória:** "Esses 3 papéis aparecem nas suas reuniões de venda reais? O Decisor costuma aparecer antes ou depois do Influenciador?"

### C) Tabela de Motivos — Racional vs Político

Esta tabela é o diferencial V4 vs consultorias genéricas. Motivos **políticos** (carreira, imagem, poder) são raramente documentados mas frequentemente decisivos em B2B.

**Por que contratar {NOME_CLIENTE}:**

| Tipo | Papel | Motivo |
|------|-------|--------|
| Racional | Iniciador | {ex: "Resolver o problema X que consome 10h/semana da equipe"} |
| Racional | Decisor | {ex: "ROI de 3x em 12 meses baseado em cases similares"} |
| Racional | Influenciador | {ex: "Integra com o stack atual sem migração de dados"} |
| **Político** | Iniciador | {ex: "Mostrar pro gestor que trovei uma solução antes de ser cobrado"} |
| **Político** | Decisor | {ex: "Ter um parceiro reconhecido para justificar o budget para o board"} |
| **Político** | Influenciador | {ex: "Não quero ser o responsável por uma implementação que falhou"} |

**Por que NÃO contratar (objeções x papel):**

| Tipo | Papel | Objeção |
|------|-------|---------|
| Racional | Decisor | {ex: "Não vejo como calcular o ROI antes de contratar"} |
| Político | Iniciador | {ex: "Meu gestor vai achar que estou mudando o que funcionava"} |

### D) Jobs-to-be-Done da Empresa (visão executiva)

Jobs da empresa como organização (não apenas do decisor individual):

- **Job Principal:** "{Quando [situação da empresa], queremos [ação] para que [resultado organizacional]}"
  - Ex: "Quando o pipeline está irregular e o board pressiona por previsibilidade, queremos ter visibilidade de quais canais geram leads qualificados para que possamos escalar com segurança."

- **Jobs Funcionais (3-4):** tarefas operacionais que a empresa precisa executar
  - Ex: "Gerar 50 leads/mês qualificados", "Reduzir o CPL de R$180 para R$90"

- **Jobs Emocionais (2-3):** como a empresa quer se sentir como organização
  - Ex: "Ter confiança para apresentar resultados para os sócios", "Sentir controle sobre o investimento em mídia"

### E) Dados Comportamentais de Compra

- **Ciclo de decisão típico:** {X semanas/meses}
- **Onde pesquisa soluções:** {LinkedIn, Google "melhores [serviço]", indicação, evento, YouTube}
- **Como avalia fornecedores:** {comparação de propostas, pedido de cases, demo, trial, prova de conceito}
- **Gatilho de urgência:** {o que acelera a decisão — ex: meta trimestral, concorrente crescendo, novo sócio}
- **Objeções mais comuns:** {3-5 objeções específicas mapeadas}

### F) Perfil do Melhor Cliente Existente (UCM 2 apenas)

Se há histórico de CRM: quais características têm em comum os clientes com maior LTV, menor churn, maior NPS?
- Setor predominante:
- Porte predominante:
- Canal de aquisição:
- Motivo declarado de contratação:

## Auto-validação

Antes de mostrar ao operador, verifique:

- [ ] Firmográficos são específicos (não "PMEs em geral")?
- [ ] Os 3 papéis do Comitê de Compra são cargos reais, não genéricos?
- [ ] A Tabela de Motivos tem pelo menos 2 motivos POLÍTICOS (não apenas racionais)?
- [ ] Jobs-to-be-Done seguem o formato "Quando / queremos / para que"?
- [ ] Objeções são específicas (não "preço" genérico)?
- [ ] Se UCM 2: dados de CRM foram usados para validar (não apenas dados declarativos)?

Se falhou → regenere silenciosamente. Não avise o operador.

## Apresentação e decisões

Apresente o output COMPLETO ao operador.

- "O Comitê de Compra que mapeei reflete o que você vive nas reuniões de venda reais?"
- "Os motivos políticos fazem sentido? Esse tipo de preocupação aparece nas conversas com clientes?"
- "Tem algum segmento de empresa que costuma ser melhor cliente mas que não está no perfil?"
- "O cargo do Decisor — ele aparece cedo ou tarde no processo?"

## Finalização

Operador aprova (com ou sem ajustes).
1. Salve em `clientes/{slug}/outputs/definicao-icp-b2b.json` (com campo `summary` no topo)
2. Atualize `client.json`: progress.skills → completed, version++, append em history[]
3. Sugira próximas skills:
   - `/jobs-to-be-done` (POP 2.5 — aprofundar JTBD dos clientes do cliente)
   - `/swot-beachhead-market` (POP 3.2 — agora com ICP definido)
