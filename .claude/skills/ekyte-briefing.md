---
name: ekyte-briefing
description: Monta briefings estruturados e pré-preenchidos para tarefas Ekyte usando templates por sigla + contexto NotebookLM do cliente. Funciona como subskill da /ekyte-task (passo 6) ou invocável diretamente para rascunhar demanda sem criar task.
user-invocable: true
---

# /ekyte-briefing — Montar briefing estruturado para task Ekyte

Substitui textos genéricos por briefings completos, contextualizados e prontos para a API Ekyte.

## Modos de operação

**Modo subskill**: invocado pela `/ekyte-task` no passo 6 — recebe pacote estruturado (cliente, sigla, tipo, quantidade, contexto), devolve `briefing_ekyte_text` pronto para o campo `description_create_task`.

**Modo standalone**: Julia chama diretamente para pensar a demanda sem criar task ainda.

## Fluxo

1. Carregar `drives.md` e `backups-crm.md` de `clientes/_skill-ekyte/`
2. Carregar template por sigla de `clientes/_skill-ekyte/briefing-templates/<SIGLA>.md`
3. Verificar cache de sessão para NotebookLM do cliente (TTL 90 dias por público)
4. Se cache miss → consultar via `/cs-notebooklm-consulta-cliente`
5. Pré-preencher campos do template com dados reais da síntese
6. Formular perguntas ativas em **lote único** para Julia responder (não pedir uma por vez)
7. Validar Drive, KV e acesso a ferramentas
8. Compor estrutura Markdown completa
9. Converter para **texto plano formatado** para a API Ekyte:
   - Emojis numerados (1️⃣ 2️⃣ 3️⃣)
   - TÍTULOS EM CAIXA ALTA
   - Bullets com `•`
   - URLs soltas
   - Sem tags HTML
10. Mostrar preview; aguardar confirmação ou ajustes
11. Devolver JSON estruturado para `/ekyte-task`

## Formato de saída obrigatório (Ekyte REST)

Ekyte via REST **não interpreta HTML**. O campo `description` deve ser texto plano com:
```
1️⃣ OBJETIVO
• Descrição do que deve ser feito

2️⃣ PÚBLICO
• Definição do público-alvo

3️⃣ REFERÊNCIAS
• https://drive.google.com/...

4️⃣ ENTREGÁVEIS
• Lista de peças e formatos
```

## Cache de público (TTL 90 dias)

Para cada cliente + linha de produto, o público-alvo fica em cache em `clientes/_skill-ekyte/` para evitar reconsulta a cada task.

## Guardrails

- **Nunca fabricar dados** ausentes do NotebookLM — deixar campo em branco e sinalizar
- Cache é por cliente, não por sigla
- Cliente sem NotebookLM = pausar e pedir autorização da Julia antes de continuar
- Ekyte REST = texto plano; **sem HTML**
- Não chamar MCP Ekyte — responsabilidade da `/ekyte-task`
