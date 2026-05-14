# Metodologia — Maturidade de GTM (V4)

Este `README.md` existe para **nortear o uso** da metodologia dentro desta pasta (`Metodo/`): como **diagnosticar**, **classificar maturidade**, **priorizar ações (packs)** e **comprovar implementação/gestão** via evidências (DoD).

## O que é (visão geral)

A tese define maturidade de GTM como a capacidade de gerar, capturar e converter demanda por meio de um sistema **documentado, repetível, mensurável e gerenciado**.

O framework central é a **Matriz 3×7**:

- **3 pilares**: Oferta & Posicionamento, Marketing, Vendas  
- **7 blocos**: Estratégia, Processos, Clientes, Dados, Gestão, Metas, Time

Referência principal (introdução + definições + níveis):
- `RFC_ Tese de Maturidade de GTM da V4 Company1.md`

## Conceitos que você precisa usar (sem isso a aplicação “escapa”)

### Implementado (Definition of Implemented)
Um processo só está **implementado** quando existem **simultaneamente**:

- **Processo definido**: critérios de entrada → execução → saída (passa/não passa)
- **Papéis e responsabilidades**: owner e responsáveis
- **Ferramentas e dados mínimos**: onde registra, quais campos são obrigatórios, como mede/audita
- **Execução comprovada**: rodou **ciclos completos** com evidência (CRM/log/ata/dashboard)

Setup sem ciclo completo = preparação, não implementação.

### Gerenciado (Definition of Managed)
Um processo só está **gerenciado** quando, além de implementado, existe:

- **Cadência (rituais)** com agenda e responsável
- **KPIs com thresholds** (verde/amarelo/vermelho) e gatilhos de ação
- **Backlog** priorizado de melhorias/experimentos (hipótese → decisão → resultado)
- **Controle de mudanças** (change log)
- **Loops inter-áreas** quando aplicável (ex.: Marketing ↔ Vendas)

Se não há cadência + KPI + decisão registrada, não está gerenciado.

## Como navegar nesta pasta

Este repositório (pasta) está organizado como um “documento base” + “módulos”:

- **Base / Fundamentos**  
  - `RFC_ Tese de Maturidade de GTM da V4 Company1.md`: resumo executivo, Matriz 3×7, definições, e a estrutura de níveis

- **Auditorias (checklists e sintomas por nível/pilar/blocos)**  
  - Exemplo: `RFC_ Tese de Maturidade de GTM da V4 Company2.md` (Auditoria detalhada Nível 1 — Oferta & Posicionamento)

- **Esteiras / Packs (intervenções padronizadas com DoD)**  
  - Exemplo: `RFC_ Tese de Maturidade de GTM da V4 Company13.md` (lista de packs por esteira/nível, com promessa, artefatos, rotinas, DoD e pré‑requisitos)

## Como aplicar a metodologia (passo a passo)

### 1) Delimite o escopo do diagnóstico
Defina claramente **o que está sendo avaliado**:

- **Pilar** (Oferta & Posicionamento / Marketing / Vendas)
- **Blocos** (7 blocos) que serão avaliados primeiro
- **Unidade** (empresa inteira, BU, time, região, squad)
- **Período** de evidência mínima (ex.: últimas 4 semanas)

Regra prática: comece por **Processos + Dados + Gestão**, porque geralmente destravam previsibilidade e permitem medir o resto.

### 2) Faça a auditoria (coleta de sinais + evidências)
Use o material de auditoria (ex.: arquivos como o `...2.md`) para coletar:

- **Sintomas** (o que acontece no dia a dia)
- **Respostas às perguntas de diagnóstico**
- **Checklists** (itens sim/não)
- **Evidências** (prints, links, amostras, registros)

Evidência típica (exemplos):
- CRM: etapa, próxima ação/data, motivos de perda, campos obrigatórios preenchidos
- Atas: weekly, forecasting, review de campanhas, win/loss
- Dashboards/relatórios: conversões por etapa, aging, acurácia de forecast
- Artefatos: playbook, template de proposta, SLAs, roteamento, catálogo de ofertas

### 3) Classifique o nível por bloco (e não “por impressão”)
Para cada **bloco** do pilar avaliado, marque:

- **Implementação**: não implementado / parcial / implementado
- **Gerenciamento**: não gerenciado / parcialmente gerenciado / gerenciado

Depois consolide um “nível” do pilar (ou do motion) com base no padrão dominante.

Importante: **maturidade não é faturamento**. É integridade do sistema.

### 4) Transforme diagnóstico em backlog (gargalos → hipóteses → intervenções)
Converta os principais gaps em um backlog simples:

- **Problema** (ex.: “pipeline sem próxima ação”)
- **Causa provável** (ex.: “campo não obrigatório + ausência de ritual de higiene”)
- **Intervenção (pack)** (ex.: base de CRM + hygiene + rotina semanal)
- **Métrica de sucesso** (ex.: 80%+ com próxima ação/data por 4 semanas)

### 5) Escolha o “próximo pack” (com pré‑requisitos)
Use as **Esteiras/Packs** para selecionar o menor conjunto de ações que:

- resolve o gargalo atual
- cria base para o próximo nível
- tem **DoD** (Definition of Done) auditável
- respeita **pré‑requisitos** (não “pular etapa”)

Regra prática: se o pré‑requisito não existe, execute o pack de fundação antes.

### 6) Execute com DoD e guarde evidências desde o dia 1
Todo pack deve produzir:

- **Artefatos âncora** (documentos/templates/configurações)
- **Rotinas implantadas** (rituais com agenda/owner)
- **DoD auditável** (amostra mínima + período mínimo)

Sem evidência → não conte como implementado.

### 7) Passe de “implementado” para “gerenciado”
Depois do primeiro ciclo completo, instale gestão:

- thresholds e gatilhos
- cadência (weekly/quinzenal/mensal)
- change log
- backlog contínuo

O objetivo não é “ter um documento”; é **ter um sistema que aprende**.

## Checklist rápido (para usar em kickoff/revisão)

- [ ] Pilar e blocos avaliados estão definidos
- [ ] Há evidências mínimas coletadas (CRM/atas/dashboards/artefatos)
- [ ] Nível por bloco foi classificado por implementação + gerenciamento
- [ ] Backlog criado com 3–5 gargalos principais
- [ ] Packs escolhidos respeitando pré‑requisitos
- [ ] DoD definido (amostra + período + métrica)
- [ ] Rituais no calendário + owners nomeados
- [ ] Change log (o que mudou / por que / impacto esperado)

## Convenções (para manter a metodologia “auditável”)

- **Se não está registrado, não existe**: decisões e rituais precisam deixar rastro (ata/log).
- **DoD sempre mensurável**: use percentuais, amostras e períodos (ex.: “4 weeklies seguidas”).
- **Evite pular para “otimização”** antes de ter integridade de dados/processo.

