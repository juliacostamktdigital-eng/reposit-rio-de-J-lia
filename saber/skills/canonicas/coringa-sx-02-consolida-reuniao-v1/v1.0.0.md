---
slug: coringa-sx-02-consolida-reuniao-v1
name: coringa-sx-02-consolida-reuniao-v1
description: "Executa o fluxo completo de ingestão e atualização de uma reunião com o cliente:"
---

# Skill: Consolida Reunião

## Descrição
Executa o fluxo completo de ingestão e atualização de uma reunião com o cliente:
1. Salva o arquivo bruto em `inputs/reunioes/`
2. Gera síntese em `inputs/sinteses/`
3. Classifica o conteúdo e atualiza seletivamente `context/`, `DECISIONS.md` e `STATUS.md`
4. Atualiza `MAPA.md` se houver mudança de direção, novo risco ou nova prioridade

Responde à pergunta: *"O que mudou, foi confirmado ou surgiu de novo nessa reunião — e onde isso precisa ser registrado?"*

### Regra central
**Nenhuma reunião pode existir apenas como registro.** Ela deve obrigatoriamente gerar pelo menos um destes efeitos: síntese, decisão registrada, atualização de contexto ou atualização de execução.

## Quando Usar
- Triggers diretos: "consolida reunião", "atualiza contexto", "processar reunião", "transcrição de reunião"
- Toda vez que uma reunião com o cliente for concluída e houver transcrição ou anotações disponíveis
- **NÃO usar se:**
  1. Não houver transcrição nem anotações da reunião — sem fonte, não há o que consolidar
  2. Os arquivos `context/` do cliente não existirem — executar `coringa-sx-01-pipeline-extracao` primeiro

---

## Inputs Necessários

1. ✅ **Transcrição ou anotações da reunião** — obrigatório. Pode ser:
   - Arquivo de transcrição (ex: `.md` gerado pelo Gemini/Otter)
   - Anotações do consultor coladas no chat
   - Ambos combinados (quando houver conflito entre fontes, prevalece a anotação do consultor)
2. ✅ **Arquivos de `context/` atuais do cliente** — obrigatório. Ler apenas o(s) relevante(s):
   - `context/business.md` — se a reunião trouxe dados de modelo de negócio, receita ou capacidade
   - `context/gtm.md` — se a reunião trouxe dados de canais, funil, ICP, ciclo de vendas, mercado
   - `context/constraints.md` — se a reunião trouxe novas restrições, UDEs ou diagnóstico de trava
   - `DECISIONS.md` — sempre lido, pois todas as decisões são registradas aqui

---

## Processo de Execução

### Step 0 — Ingestão do Arquivo Bruto

1. Se a transcrição/anotação foi fornecida como conteúdo no chat (e não como arquivo já salvo), salvar em:
   `clientes/[nome-cliente]/inputs/reunioes/YYYY-MM-DD-[nome-reuniao].md`
   - Formato do nome: data ISO + slug descritivo (ex: `2026-04-08-reuniao-followup.md`)
   - Se já existe arquivo salvo no caminho correto, pular este passo
2. Confirmar ao consultor onde o arquivo foi salvo (ou já estava)

---

### Step 1 — Leitura de Contexto

1. Leia os arquivos de `context/` relevantes (business, gtm e/ou constraints) — mapeie seções existentes e itens pendentes
2. Leia `DECISIONS.md` — mapeie decisões anteriores e questões abertas
3. Leia a transcrição/anotações da reunião
4. Identifique o número da versão: kickoff = v1, primeira reunião pós-kickoff = v2, sequência incremental
5. Identifique a data da reunião (extraia da transcrição ou pergunte ao consultor se não estiver explícita)
6. Determine qual(is) arquivo(s) precisam ser atualizados

---

### Step 2 — Gerar Síntese

Antes de qualquer atualização, gerar o arquivo de síntese em:
`clientes/[nome-cliente]/inputs/sinteses/YYYY-MM-DD-[nome-reuniao].md`

**Estrutura obrigatória da síntese:**
```markdown
# Síntese — [Nome da Reunião] ([YYYY-MM-DD])

## Resumo executivo
[2–3 linhas: o que aconteceu e qual foi o resultado principal]

## Principais achados
- [achado 1]
- [achado 2]

## Decisões identificadas
- [decisão 1] → registrar em DECISIONS.md
- [decisão 2]

## Dúvidas abertas
- [dúvida 1]

## Impactos no projeto
- Contexto: [sim/não — quais arquivos context/ mudam]
- Execução: [sim/não — qual STATUS.md ou output muda]
- Direção: [sim/não — o MAPA.md precisa ser atualizado?]
```

> Salvar a síntese ANTES de fazer qualquer atualização nos demais arquivos.

---

### Step 3 — Classificação e Extração de Mudanças

Varra a transcrição buscando quatro tipos de conteúdo:

**1. Confirmações de itens pendentes**
- Cada item `[ ]` nos "Pontos de Dúvida" dos arquivos de context/: foi respondido nessa reunião?
- Se sim: extraia a resposta literal

**2. Novas informações em seções existentes**
- Dados novos que complementam campos já existentes (ex: nova métrica, novo canal de aquisição declarado, novo UDE mencionado)
- Mapear ao campo/seção correspondente

**3. Correções de dados anteriores**
- Informação que contradiz ou substitui dado registrado nos arquivos de context/
- Registrar tanto o dado antigo quanto o novo — o consultor decide qual prevalece

**4. Novos tópicos sem seção equivalente**
- Temas relevantes que surgem na reunião e não têm seção correspondente nos arquivos de context/ atuais
- Candidatos a nova seção no documento

**5. Novas dúvidas**
- Perguntas que surgem na reunião e ficam em aberto para próxima rodada

---

### Step 4 — Apresentar Diff Proposto

**Antes de qualquer edição**, exibir o resumo estruturado das mudanças para o consultor revisar:

```
MUDANÇAS PROPOSTAS — Reunião [N] ([YYYY-MM-DD]):

✅ Confirmados (Pontos de Dúvida):
  - Item [N]: "[dúvida original]" → [resposta confirmada]
  - Item [N]: "[dúvida original]" → [resposta confirmada]

📝 Atualizações in-place:
  - Seção [X] / [Campo]: [valor atual] → [novo valor]
  - Seção [X] / UDEs: + "[novo UDE adicionado]"

⚠️ Conflitos identificados (requer decisão do consultor):
  - [Campo]: valor atual = "[A]" | reunião informou "[B]" — qual prevalece?

🆕 Novas seções propostas:
  - "[Título da nova seção]": [breve descrição do conteúdo]

❓ Novas dúvidas registradas:
  - [nova dúvida surgida na reunião]
```

> Aguardar confirmação do consultor. Incorporar ajustes. Só gerar o documento após aprovação.

---

### Step 5 — Atualizar Arquivos de Contexto e Execução

Com as mudanças aprovadas, gerar as versões atualizadas dos arquivos afetados:

**Regra de seleção — qual arquivo atualizar:**
- Dados de modelo de negócio, receita, capacidade → `context/business.md`
- Dados de canais, funil, ICP, ciclo, mercado, concorrência → `context/gtm.md`
- Novas restrições, UDEs, diagnóstico de trava → `context/constraints.md`
- Decisões estratégicas, questões abertas, injeções confirmadas → `DECISIONS.md`
- Múltiplos arquivos podem ser atualizados na mesma reunião

**Atualizações in-place (dentro das seções existentes):**
- Informação nova adicionada a seção existente: incluir `[novo — Reunião N]` ao final do item
- Informação corrigida: substituir valor antigo pelo novo + `[atualizado — Reunião N]`
- Dúvida confirmada: marcar `[x]` no checkbox + adicionar resposta com `[confirmado — Reunião N]`

**Novas seções (quando houver tópico sem seção equivalente):**
- Criar nova seção ao final do arquivo mais relevante
- Título no formato: `### [Título Temático] [Reunião N]`

**Registro em DECISIONS.md:**
```markdown
## Reunião [N] — [YYYY-MM-DD]
- **Decisão:** [decisão tomada]
- **Por quê:** [justificativa]
- **Impacto:** [o que muda operacionalmente]
```

**Novas dúvidas:**
- Adicionar à seção "Questões Abertas" do `DECISIONS.md` com `[ ]`

**Sempre atualizar `produtos/[produto-ativo]/STATUS.md`:**
- Adicionar a reunião à seção "Última ação" (com data)
- Atualizar bloqueios e pendências, se a reunião resolveu ou criou algum
- Se a reunião concluiu uma fase ou abriu uma nova, atualizar `Fase atual`/`Próxima fase` e a "Síntese das Fases" correspondente
- Se a reunião gerou drafts de novos entregáveis em curso, registrar na tabela de Entregáveis em curso

---

### Step 6 — Atualizar MAPA.md

Atualizar `MAPA.md` **somente se** a reunião trouxer ao menos uma das condições abaixo:
- Mudança de direção ou prioridade (ex: foco estratégico mudou)
- Novo risco relevante ou risco anterior resolvido
- Novo produto iniciado ou produto encerrado
- Próximo passo crítico diferente do que estava registrado

O que atualizar no MAPA:
- Bloco **⚡ Estado atual** — status geral, foco, risco, próximo passo
- Bloco **📥 Últimos inputs relevantes** — adicionar linha com a reunião
- Bloco **🧾 Decisões recentes** — adicionar linha para cada nova decisão

> Se nenhuma dessas condições se aplicar, NÃO tocar no MAPA.

---

## Regras de Ouro

1. **NÃO reorganizar seções existentes** — atualizar in-place ou criar nova seção ao final
2. **NÃO inferir** informações não ditas explicitamente na reunião
3. **NÃO salvar sem confirmação** do consultor após o diff proposto
4. **NÃO resolver conflitos sozinho** — quando um dado da reunião contradiz o contexto, apresentar ambos e aguardar decisão
5. **NÃO alterar o status de validação** dos arquivos — quem valida é o consultor
6. **DECISIONS.md sempre** — toda reunião gera um entry, mesmo que pequeno

---

## Formato de Saída Obrigatório

Após confirmação do consultor, gerar os arquivos atualizados (apenas os modificados).

**Salvar em (por ordem de execução):**
1. `clientes/[nome-cliente]/inputs/reunioes/YYYY-MM-DD-nome.md` — arquivo bruto (Step 0)
2. `clientes/[nome-cliente]/inputs/sinteses/YYYY-MM-DD-nome.md` — síntese (Step 2)
3. `clientes/[nome-cliente]/context/business.md` — se houver mudanças de negócio
4. `clientes/[nome-cliente]/context/gtm.md` — se houver mudanças de GTM
5. `clientes/[nome-cliente]/context/constraints.md` — se houver novas restrições/UDEs
6. `clientes/[nome-cliente]/DECISIONS.md` — sempre (entry da reunião)
7. `clientes/[nome-cliente]/produtos/[produto-ativo]/STATUS.md` — sempre (registra a reunião como última ação; atualiza fase/síntese se aplicável)
8. `clientes/[nome-cliente]/MAPA.md` — se houver mudança de direção, risco ou prioridade (Step 6)

Se não tiver permissão de escrita, exibir o conteúdo completo no chat para o consultor salvar manualmente.
