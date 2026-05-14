---
slug: coringa-sx-05-kickoff-pack-perguntas-v1
name: coringa-sx-05-kickoff-pack-perguntas-v1
description: "Lê os arquivos de contexto do cliente e o roteiro de kickoff (se existir) e gera o **pack estruturado de perguntas** para a reunião de kickoff. O pack segue a mesma ordem de blocos da agenda da reunião — garantindo que apresentação e tir..."
---

# Skill: Kickoff — Pack de Perguntas (Tira-Dúvidas)

## Descrição
Lê os arquivos de contexto do cliente e o roteiro de kickoff (se existir) e gera o **pack estruturado de perguntas** para a reunião de kickoff. O pack segue a mesma ordem de blocos da agenda da reunião — garantindo que apresentação e tira-dúvidas são navegados na mesma sequência, sem idas e vindas de assunto.

Cada bloco tem: header com tema, tempo estimado e interlocutores sugeridos, perguntas com checkbox, e hipóteses em colchetes quando há dado parcial disponível.

## Quando Usar
- Triggers: "gerar pack de perguntas para kickoff", "montar tira-dúvidas de kickoff", "preparar perguntas para o kickoff", "criar questionário de kickoff"
- **Pré-requisito:** `context/business.md`, `context/gtm.md` e `context/constraints.md` devem existir. Idealmente `kickoff-roteiro.md` também, mas não é bloqueante.
- **NÃO usar se:** os arquivos de context/ não existirem — sem contexto não é possível distinguir o que é conhecido do que precisa ser perguntado.

## Inputs Necessários
1. `clientes/[nome-cliente]/context/business.md`
2. `clientes/[nome-cliente]/context/gtm.md`
3. `clientes/[nome-cliente]/context/constraints.md`
4. `clientes/[nome-cliente]/produtos/[produto-ativo]/kickoff-roteiro.md` — opcional, mas preferível

---

## Processo de Execução

### Step 0 — Leitura e Mapeamento

1. Leia os três arquivos de context/ e o kickoff-roteiro.md (se existir).
2. Para cada dado relevante, classifique:
   - **Confirmado:** dado presente nos context files com clareza → não gera pergunta
   - **Parcial:** dado presente mas incompleto ou incerto → gera pergunta de **validação** com hipótese em colchetes
   - **Ausente:** campo não encontrado nas fontes → gera pergunta de **discovery** sem hipótese

---

### Step 1 — Montagem do Pack por Bloco da Agenda

Monte as perguntas bloco a bloco, na **ordem da agenda da reunião de kickoff**. Máximo 8 perguntas por bloco — priorize o que é mais crítico para desbloquear o trabalho das semanas seguintes.

**Ordem e foco de cada bloco:**

**Bloco 1 — Sobre a Empresa** `(30 min · #head #GP #GT)`
- Validar: dados de faturamento, composição dos serviços, perfil dos clientes atuais
- Descobrir: ticket médio por serviço, capacidade operacional, gargalos percebidos pelo fundador

**Bloco 2 — S.W.O.T** `(30 min · #head #GP #GT)`
- Validar: forças identificadas (tempo de mercado, clientes tier-1) → o fundador concorda com essa leitura?
- Descobrir: o que o fundador enxerga como maior ameaça concreta (não genérica), qual fraqueza ele já tentou resolver e não conseguiu

**Bloco 3 — Benchmarking** `(15 min · #todos)`
- Validar: concorrentes listados nos context files → eles são realmente percebidos como concorrência?
- Descobrir: como o cliente se diferencia na percepção do mercado (não apenas na autoimagem), o que o cliente vê de bom nos concorrentes

**Bloco 4 — Sobre o Público** `(25 min · #todos)`
- Validar: ICP atual → esse perfil é o mais rentável ou apenas o mais frequente?
- Descobrir: perfil do ICP desejado (expansão), o que define um lead qualificado na visão da equipe, geografia de atuação real vs. desejada

**Bloco 5 — Sobre o Design** `(15 min · #copy #designer)`
- Validar: inconsistências identificadas na presença digital (site, redes) → o cliente as reconhece?
- Descobrir: ativos digitais que existem (banco de imagens, vídeos, manual de identidade), preferências de cores e tom visual, referências de marcas que o cliente admira

**Bloco 6 — Assessment & Dados** `(não está na agenda principal · #head)`
- Validar: ferramentas e plataformas listadas nos context files
- Descobrir: acesso disponível para auditoria (Google Analytics, Meta, CRM), quem na equipe gerencia cada ferramenta, volume atual de leads gerados por canal

---

### Step 2 — Formatação do Pack

Para cada bloco, aplicar o seguinte padrão de formatação:

```
## BLOCO [N] — [NOME DO BLOCO]
**Tempo estimado:** [X min] · **Interlocutores:** [#papéis]

- [ ] [N]. [Pergunta direta e objetiva]
      R: [Hipótese: dado parcial disponível] ← apenas se dado existe nos context files
      R: _________________ ← quando dado é totalmente ausente
```

Tom das perguntas:
- Investigativo, nunca confrontador
- Perguntas abertas para discovery ("Como funciona...?", "O que define...?", "Quando acontece...?")
- Perguntas fechadas para validação ("Confirmamos que... está correto?", "Esse número reflete...?")
- Nunca perguntar algo que já foi respondido claramente nos context files

---

### Step 3 — Apresentar para Aprovação

Exibir o pack completo ao consultor de uma vez. O consultor pode:
- Remover perguntas já respondidas
- Adicionar perguntas que o time queira fazer
- Reordenar perguntas dentro de um bloco

Aguardar aprovação antes de salvar.

---

### Step 4 — Salvamento em dois formatos

Gerar **ambos os arquivos** na raiz do produto (`clientes/[nome-cliente]/produtos/[produto-ativo]/`):

**4a — Markdown:**
Salvar diretamente: `kickoff-perguntas.md`

**4b — Word (.docx):**
Verificar se python-docx está disponível: `pip show python-docx`. Se não: `pip install python-docx -q`.

Escrever e executar um script Python em `/tmp/gerar_perguntas.py` que gera `kickoff-perguntas.docx` com:
- Cabeçalho: título em vermelho (RGBColor 0xCC,0x00,0x00), metadados em cinza itálico
- Blocos: header com nome do bloco em vermelho + tempo e interlocutores em cinza pequeno
- Perguntas: `[ ]  N. Pergunta` com indentação · linha de resposta `R: ______` ou `R: [Hipotese: ...]` em amarelo/âmbar itálico
- Divisórias entre blocos
- Rodapé em cinza itálico

Usar `run.text =` para preservar formatação. Campos com hipótese: `RGBColor(0x88, 0x66, 0x00)` + itálico.

Se não tiver permissão de escrita, exibir o conteúdo markdown no chat.

---

## 🛑 Regras de Ouro

- **Máximo 8 perguntas por bloco** — forçar priorização, não listar tudo que é curioso
- **A ordem dos blocos é imutável** — deve ser idêntica à agenda da reunião para não criar descontinuidade no kickoff
- **Hipóteses só quando há dado parcial** — não inventar hipóteses para campos totalmente desconhecidos
- **Nunca perguntar o que já foi respondido claramente** nos context files
- **NÃO fazer perguntas incrementais durante a geração** — consolidar tudo em um único pass e apresentar de uma vez

---

## Formato de Saída Obrigatório (dois arquivos)

```markdown
# Pack de Perguntas — Kickoff [Nome do Cliente]

> **Status:** `[AGUARDANDO REVISÃO DO CONSULTOR]`
> **Data de geração:** [data]
> **Referência de narrativa:** kickoff-roteiro.md (mesma ordem de blocos)
>
> *Instruções de uso: conduza os blocos na ordem abaixo durante o kickoff. Preencha as respostas em tempo real. Campos com `[Hipótese: ...]` são dados já coletados — confirme ou corrija. Campos com linha em branco são novos dados a coletar.*

---

## BLOCO 1 — SOBRE A EMPRESA
**Tempo estimado:** 30 min · **Interlocutores:** #head #GP #GT

- [ ] 1. [Pergunta]
      R: [Hipótese: ...] ou R: _________________

- [ ] 2. [Pergunta]
      R: _________________

[... até 8 perguntas]

---

## BLOCO 2 — S.W.O.T
**Tempo estimado:** 30 min · **Interlocutores:** #head #GP #GT

[...]

---

## BLOCO 3 — BENCHMARKING
**Tempo estimado:** 15 min · **Interlocutores:** #todos

[...]

---

## BLOCO 4 — SOBRE O PÚBLICO
**Tempo estimado:** 25 min · **Interlocutores:** #todos

[...]

---

## BLOCO 5 — SOBRE O DESIGN
**Tempo estimado:** 15 min · **Interlocutores:** #copy #designer

[...]

---

## BLOCO 6 — ASSESSMENT & DADOS
**Tempo estimado:** 15 min · **Interlocutores:** #head

[...]

---

> **Após o kickoff:** consolidar as respostas e executar `coringa-sx-02-consolida-reuniao-v1` para atualizar os arquivos de contexto.
```

**Salvar em:** `clientes/[nome-cliente]/produtos/[produto-ativo]/kickoff-perguntas.md`
