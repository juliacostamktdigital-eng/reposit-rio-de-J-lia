# NotebookLM MCP — Guia de Uso

> MCP que conecta o Claude Code diretamente ao NotebookLM para pesquisa sem alucinações.

---

## O que é e para que serve

Quando você pede pro Claude pesquisar em documentação local, ele lê múltiplos arquivos repetidamente (custo alto de tokens), busca por palavras-chave sem entender contexto, e inventa APIs quando não encontra o que precisa.

O NotebookLM MCP resolve isso conectando o Claude diretamente ao NotebookLM — a base de conhecimento do Google powered por Gemini 2.5 — que já pré-processou seus documentos e responde com síntese inteligente e zero alucinações.

```
Sua tarefa → Claude pergunta pro NotebookLM → Gemini sintetiza a resposta → Claude escreve o código certo
```

**Diferenciais:**
- Zero alucinações: o NotebookLM recusa responder se não tiver a informação nos seus docs
- Pesquisa iterativa: Claude faz várias perguntas em sequência, cada uma aprofundando a anterior
- Biblioteca compartilhada: salva links de notebooks com tags — Claude seleciona o notebook certo automaticamente
- Setup único: autenticou uma vez, funciona em Claude Code, Cursor e Codex

---

## Setup técnico

### Pré-requisitos

- Node.js >= 18
- Claude Code instalado
- Repositório do MCP: `~/Trabalho V4/projetos/notebooklm-mcp-custom/`

### Opção 1 — Usar via npx (mais simples, versão pública)

```bash
claude mcp add notebooklm npx notebooklm-mcp@latest
```

Ou manualmente em `~/.claude.json`:

```json
{
  "mcpServers": {
    "notebooklm": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "notebooklm-mcp@latest"]
    }
  }
}
```

### Opção 2 — Usar o fork customizado (versão V4)

Aponta pro binário compilado local:

```json
{
  "mcpServers": {
    "notebooklm": {
      "type": "stdio",
      "command": "node",
      "args": ["/Users/SEU_USUARIO/Trabalho V4/projetos/notebooklm-mcp-custom/dist/index.js"]
    }
  }
}
```

> Substitua `SEU_USUARIO` pelo seu usuário. Após qualquer alteração no código, rode `npm run build` dentro do projeto para recompilar.

### Autenticação (feita uma vez)

Fale no Claude:

```
"Log me in to NotebookLM"
```

Uma janela do Chrome abre. Faça login com sua conta Google e feche. Pronto — as credenciais ficam salvas localmente.

> Use uma conta Google dedicada, não a sua conta principal. O MCP usa automação de browser (Patchright) que pode ser detectada pelo Google.

### Configurar perfil de ferramentas

Cada ferramenta ativa consome tokens do contexto. Menos ferramentas = respostas mais rápidas e baratas.

| Perfil | Ferramentas | Quando usar |
|---|---|---|
| `minimal` | 5 | Só consultas, uso no dia a dia |
| `standard` | 10 | + gestão de biblioteca |
| `full` | 16 | Acesso completo a todas as funcionalidades |

```bash
# Ver configuração atual
npx notebooklm-mcp config get

# Definir perfil
npx notebooklm-mcp config set profile standard

# Desabilitar ferramentas específicas
npx notebooklm-mcp config set disabled-tools "cleanup_data,re_auth"

# Resetar para padrões
npx notebooklm-mcp config reset
```

Configurações ficam salvas em `~/.config/notebooklm-mcp/settings.json`.

---

## Como usar (fluxo básico)

### 1. Preparar o notebook no NotebookLM

1. Acesse [notebooklm.google.com](https://notebooklm.google.com)
2. Crie um notebook e suba seus documentos (PDFs, Google Docs, links, vídeos do YouTube)
3. Compartilhe: **Configurações → Compartilhar → Qualquer pessoa com o link → Copiar**

### 2. Adicionar à biblioteca local

```
"Adiciona esse notebook à biblioteca com o nome 'Docs do Cliente X' e a tag 'cliente-x': [link]"
```

### 3. Usar em tarefas

```
"Pesquisa sobre [tema] no NotebookLM antes de codar"
"Usa o notebook do Cliente X para entender como funciona [feature]"
```

O Claude vai fazer várias perguntas sequenciais ao NotebookLM, construindo entendimento completo antes de escrever código.

---

## Comandos em linguagem natural

| Intenção | O que falar |
|---|---|
| Autenticar | "Faz login no NotebookLM" |
| Adicionar notebook | "Adiciona [link] à biblioteca com tag 'cliente-x'" |
| Listar notebooks | "Mostra nossos notebooks" |
| Selecionar notebook | "Usa o notebook do React" |
| Pesquisar primeiro | "Pesquisa isso no NotebookLM antes de codar" |
| Ver o browser ao vivo | "Me mostra o browser" |
| Corrigir autenticação | "Conserta a autenticação do NotebookLM" |
| Trocar conta Google | "Re-autentica com outra conta Google" |
| Limpeza total | "Roda o cleanup do NotebookLM" |
| Limpeza mantendo biblioteca | "Cleanup mas mantém minha biblioteca" |

---

## Referência completa das ferramentas

### Consulta

| Ferramenta | O que faz |
|---|---|
| `ask_question` | Faz uma pergunta a um notebook. Parâmetros principais: `question` (obrigatório), `notebook_id` ou `notebook_url` (opcional — usa o notebook ativo se omitido) |

### Gestão de biblioteca

| Ferramenta | O que faz |
|---|---|
| `add_notebook` | Salva um notebook na biblioteca local com metadados (nome, descrição, tópicos, tags) |
| `list_notebooks` | Lista todos os notebooks salvos |
| `get_notebook` | Retorna detalhes de um notebook pelo ID |
| `select_notebook` | Define o notebook ativo para as próximas consultas |
| `update_notebook` | Atualiza metadados de um notebook (nome, tags, URL, etc.) |
| `remove_notebook` | Remove um notebook da biblioteca |
| `search_notebooks` | Busca notebooks por texto nos metadados |
| `get_library_stats` | Estatísticas gerais da biblioteca (total, por tag, etc.) |

### Sessões

| Ferramenta | O que faz |
|---|---|
| `list_sessions` | Lista sessões abertas com o NotebookLM |
| `close_session` | Fecha uma sessão específica |
| `reset_session` | Reinicia uma sessão (limpa contexto da conversa) |

### Sistema e autenticação

| Ferramenta | O que faz |
|---|---|
| `get_health` | Verifica estado de auth, sessões ativas e configurações |
| `setup_auth` | Abre browser para autenticação inicial no Google |
| `re_auth` | Re-autentica (útil para trocar de conta Google) |
| `cleanup_data` | Remove todos os dados locais do MCP (sessões, auth, biblioteca) |

### Geração de conteúdo

| Ferramenta | O que faz |
|---|---|
| `generate_audio_overview` | Gera podcast de overview do notebook |
| `generate_study_guide` | Gera guia de estudo |
| `generate_briefing_doc` | Gera documento de briefing |
| `generate_faq` | Gera FAQ baseado nos documentos |
| `generate_timeline` | Gera linha do tempo dos eventos nos docs |
| `generate_presentation` | Gera apresentação com os pontos principais |

### Upload de fonte

| Ferramenta | O que faz |
|---|---|
| `notebooklm_upload_source` | Faz upload de um arquivo local como fonte para um notebook |

---

## Arquivos locais relevantes

| Arquivo | O que é |
|---|---|
| `~/.config/notebooklm-mcp/settings.json` | Configurações do MCP (perfil, tools desabilitadas) |
| `~/.config/notebooklm-mcp/library.json` | Biblioteca de notebooks salvos |
| `~/Trabalho V4/projetos/notebooklm-mcp-custom/` | Código-fonte do fork customizado V4 |

---

## Avisos importantes

- Use uma **conta Google dedicada** para automação — não a conta principal
- O MCP usa automação de browser com comportamento humanizado (velocidade de digitação realista, delays naturais, movimentos de mouse), mas não há garantia de que o Google não detecte uso automatizado
- A conta gratuita tem limites diários de consultas — respeite os limites

---

## Comparativo de abordagens

| Abordagem | Custo de tokens | Alucinações | Qualidade |
|---|---|---|---|
| Passar docs pro Claude | Alto (múltiplas leituras) | Sim | Variável |
| Busca web | Médio | Alta | Incerto |
| RAG local | Médio-alto | Médio | Depende do setup |
| **NotebookLM MCP** | **Mínimo** | **Zero** | **Síntese especializada** |
