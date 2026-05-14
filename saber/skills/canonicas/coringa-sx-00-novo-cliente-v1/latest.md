---
slug: coringa-sx-00-novo-cliente-v1
name: coringa-sx-00-novo-cliente-v1
description: "Cria um cliente novo a partir do template canônico (`Template/Clientes/_template-cliente/`), preenche `cliente.md`, ajusta `produtos/Saber/` para conter apenas o sub-produto contratado, remove placeholders e deixa a estrutura pronta para..."
---

# Skill: Onboarding de Novo Cliente (Coringa SX-00)

## Descrição
Cria um cliente novo a partir do template canônico (`Template/Clientes/_template-cliente/`), preenche `cliente.md`, ajusta `produtos/Saber/` para conter apenas o sub-produto contratado, remove placeholders e deixa a estrutura pronta para a primeira ingestão de inputs (skill `coringa-sx-01`).

É a primeira skill da jornada — precede todas as `coringa-sx-01` a `sx-05` e qualquer skill de produto (`ee-*`, `drx-*`).

## Quando Usar
- Triggers: "Novo cliente", "Criar cliente X", "Onboarding de cliente", "Start cliente", "Iniciar engajamento"
- **Sempre** como passo 0 antes de qualquer outra skill em um cliente que ainda não existe
- NÃO usar para clientes já existentes — para reabrir/atualizar, edite os arquivos diretamente

## Inputs Necessários
A skill solicita ao usuário os seguintes campos. Não prosseguir sem todos os obrigatórios.

| Campo | Obrigatório | Exemplo |
|---|---|---|
| Nome comercial | Sim | `Globo Traduções e Eventos` |
| Produto Ativo | Sim | `Saber/E.E` · `Saber/DR-X` · `Executar` · `Ter` · `Potencializar` |
| Slug do produto | Sim | `ee-2026-04` · `drx-2026-04` · `exec-2026-05` |
| Data de início | Não (default: hoje) | `2026-04-27` |
| Stakeholder principal — nome | Sim | `Frederico` |
| Stakeholder principal — papel | Sim | `Dono / Decisor estratégico` |
| Stakeholder principal — contato | Não | telefone, email |
| Cidade da empresa | Não | `Brasília, DF` |
| Setor | Não | `Tradução e interpretação` |

---

## Processo de Execução

### Step 0: Validar inputs
1. Confirmar que `Produto Ativo` é um dos cinco valores válidos.
2. Confirmar que `slug` segue o padrão `<prefixo>-AAAA-MM` e é compatível com o produto:
   - `Saber/E.E` → slug começa com `ee-`
   - `Saber/DR-X` → slug começa com `drx-`
   - `Executar` → slug começa com `exec-`
   - `Ter` → slug começa com `ter-`
   - `Potencializar` → slug começa com `pot-`
3. Confirmar que `Template/Clientes/[Nome comercial]/` ainda **não existe**. Se existir, parar e pedir confirmação ao usuário (sobrescrever? renomear?).

### Step 1: Criar pasta do cliente a partir do template
1. Copiar recursivamente `Template/Clientes/_template-cliente/` → `Template/Clientes/[Nome comercial]/`.
2. Preservar toda a estrutura (`MAPA.md`, `cliente.md`, `STATUS.md`, `DECISIONS.md`, `context/`, `inputs/`, `ativos-cliente/`, `produtos/`). Os `outputs/` de cada produto já vêm dentro da estrutura copiada — não é necessário criar separadamente.

### Step 2: Ajustar `produtos/` ao Produto Ativo
- Se `Produto Ativo = Saber/E.E`: remover `produtos/Saber/DR-X/` (manter apenas `Saber/E.E/`).
- Se `Produto Ativo = Saber/DR-X`: remover `produtos/Saber/E.E/` (manter apenas `Saber/DR-X/`).
- Se `Produto Ativo = Executar`, `Ter` ou `Potencializar`: remover `produtos/Saber/` inteiro. Manter apenas a pasta correspondente ao produto ativo (com README.md já existente; popular com `produto.md`, `STATUS.md`, `changelog.md` baseado no padrão de Saber).

### Step 3: Preencher `cliente.md`
- Substituir `[Nome do Cliente]` pelo nome comercial.
- Preencher campos: nome, cidade, setor (deixar `[Não preenchido]` quando não informado).
- Adicionar entrada de stakeholder na tabela com nome, papel, contato, localização.
- Definir bloco *Produto Ativo*: `Produto Ativo: <valor>`, `Slug: <slug>`, `Fase atual: S1 — Kickoff`, `Próximo passo: Realizar kickoff e gerar context/`.

### Step 4: Atualizar `MAPA.md`
- Substituir `[Nome do Cliente]` pelo nome comercial no título.
- Substituir placeholders na seção "O que é" por `[AGUARDANDO COMPLEMENTO]`.
- Em "Estado atual": preencher `Produto ativo` e `Step em execução` com paths concretos baseados no Produto Ativo.
- Em "Onde encontrar cada coisa → Execução": deixar apenas a sub-seção do Produto Ativo (remover as outras para evitar ruído visual).

### Step 5: Atualizar `produtos/<Produto Ativo>/produto.md`
- Substituir `[Nome do Cliente]` pelo nome comercial.
- Definir: `Sub-produto`, `Slug do contrato`, `Início`.
- Manter Objetivo e Escopo de Entregas como placeholders `[AGUARDANDO COMPLEMENTO]`.

### Step 6: Atualizar `STATUS.md` do cliente
- Definir: `Produto ativo`, `Fase ativa: S1 — Kickoff`, `Status: kickoff em andamento`, `Risco principal: a definir`, `Próximo movimento: Realizar kickoff`.
- Manter context files em `[AGUARDANDO]`.

### Step 7: Adicionar entrada inicial em `DECISIONS.md`
- Inserir bloco D1 com data atual, autor (consultor responsável, se conhecido), decisão: "Início do engajamento — produto contratado: [Produto Ativo] (slug [slug])".

### Step 8: Reportar ao usuário
- Caminho do cliente criado: `Template/Clientes/[Nome comercial]/`.
- Estrutura ajustada (qual sub-produto ficou ativo).
- Próximos passos sugeridos:
  1. Adicionar materiais iniciais em `inputs/` (transcrições, formulários, documentos).
  2. Rodar `coringa-sx-01-pipeline-extracao-v1` quando primeiro material chegar.
  3. Completar `cliente.md` (CNPJ, demais stakeholders) conforme dados forem coletados.

---

## Critério de Sucesso

A skill foi bem-sucedida quando, após execução:

- [ ] `Template/Clientes/[Nome]/` existe.
- [ ] Toda a estrutura de pastas e arquivos do `_template-cliente/` foi replicada.
- [ ] `produtos/Saber/` (ou produto ativo equivalente) contém apenas a sub-pasta correspondente ao Produto Ativo.
- [ ] `cliente.md` tem Nome Comercial preenchido (não mais `[Nome do Cliente]`) e *Produto Ativo* declarado com valor não-placeholder.
- [ ] `MAPA.md` tem título personalizado e Estado atual preenchido com Produto Ativo concreto.
- [ ] `DECISIONS.md` tem entrada D1 inicial.
- [ ] Nenhum `[Nome do Cliente]` remanescente nos arquivos `.md` do cliente novo (verificar com grep).
- [ ] Arquivos de `context/` permanecem vazios/template — esta skill **não** preenche conhecimento; isso é responsabilidade das skills `coringa-sx-01` em diante.
- [ ] `produtos/<P>/outputs/` existe com as 4 subpastas (`slides/`, `envios/`, `visual/`, `dashboards/`).

## Não-objetivos

- A skill **não** processa transcrições nem extrai contexto — isso é `coringa-sx-01`.
- A skill **não** gera kickoff deck — isso é `coringa-sx-04`.
- A skill **não** valida dados do cliente — apenas estrutura a pasta. Validação é responsabilidade do consultor.
