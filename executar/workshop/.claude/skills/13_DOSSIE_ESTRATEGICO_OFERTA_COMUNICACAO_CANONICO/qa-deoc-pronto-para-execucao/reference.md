# Referência — QA DEOC (playbook 13)

## Critério N2 (Seção 6 — texto canônico)

DEOC está N2 quando:

1. Integra oferta, público, problema, concorrência e narrativa.
2. Usa benchmark e diagnóstico como base.
3. Define proposta de valor clara.
4. Lista claims permitidos/proibidos.
5. Orienta mídia, criativo, LP e vendas.
6. Define ICP e anti-ICP com critérios e exemplos operacionais.
7. Tem oferta dizível, escopo explícito, provas mínimas e limites da promessa.
8. Tem provas ou marca claims pendentes.
9. Pode ser usado por IA e humanos sem recoletar contexto.

**Interpretação para QA:** itens 1–8 exigem evidência **no documento** ou em anexo explicitamente referenciado. O item 9 é um teste de **autossuficiência**: um executor novo consegue produzir peças sem perguntas que o DEOC deveria responder.

## Critério N3 (Seção 7 — texto canônico)

DEOC está N3 quando:

1. Ângulos vencedores são marcados.
2. Objeções comerciais reais entram no documento.
3. Performance de mídia retroalimenta narrativa.
4. Aprendizados por cohort/segmento são versionados.
5. Anti-padrões de comunicação são registrados.
6. Objeções e perdas comerciais retroalimentam promessa, provas, oferta e anti-ICP.
7. Mudanças de mensagem/oferta entram em change log por ciclo.

**Interpretação:** N3 é típico após ciclos com dados. Para **primeiro** go-live, muitos itens podem ser **n.a.** com plano de evolução documentado.

## Implementação (Seção 3)

Citação operacional: *«Não usar como documento estático "bonito": se mídia, LP, criativo, CRM e vendas não conseguem aplicar o DEOC, ele ainda não conta como implementado.»*

O QA deve perguntar, por função, se o DEOC **desbloqueia** trabalho ou só descreve teoria.

## Anti-padrões (Seção 8 — veto ou retrabalho)

Evitar (se detectado, registrar e avaliar severidade):

1. Manter UCM e DCC divergentes.
2. Repetir diagnóstico sem decisão de comunicação.
3. Criar personas genéricas.
4. Escrever copy sem benchmark.
5. Prometer sem prova.
6. Ignorar alternativas percebidas.
7. Não traduzir para mídia, LP, criativo e vendas.

## Severidade sugerida

| Nível | Exemplo |
|-------|---------|
| Bloqueante | Promessa pública sem prova; ICP inoperante; matriz 5.9 vazia; anti-padrão 5, 7 ou promessa desalinhada a vendas. |
| Alto | Claims proibidos sem lista; anti-ICP sem critério; benchmark não refletido. |
| Médio | N3 não preenchido no primeiro ciclo (aceitável se explícito); cohort não versionado. |
| Baixo | Melhoria de redação, exemplos extras, densidade de provas. |

## Cobertura estrutural (Seções 5.1 a 5.9)

Use como segunda linha de defesa quando um critério N2 parece “subjetivo”:

- **5.1** Resumo com cliente, oferta, mercado, beachhead, objetivo, problema, hipótese, risco.
- **5.2** Oferta, mecanismo, brainer, escopo, limites, anti-ICP, features com prova quando aplicável.
- **5.3** ICP operacional; em B2B, papéis de decisão quando relevante.
- **5.4** Problemas com voz do cliente e ligação a conversão.
- **5.5** Alternativas ancoradas em benchmark.
- **5.6** Proposta de valor no formato canônico ou equivalente explícito.
- **5.7** Narrativa com tensão, mecanismo, prova, CTA.
- **5.8** Claims permitidos/proibidos governados; pendentes marcados.
- **5.9** Matriz de tradução para as seis saídas (mídia, briefing, LP, copy anúncios, vendas, tracking).

## Relação com outras skills

- `dossie-estrategico-oferta-comunicacao` — `build_deoc.py --audit` cobre **schema** do JSON; este QA cobre **aderência ao playbook** e decisão de negócio.
- `traducao-deoc-para-assets` — fortalece o critério N2 de orientar execução (item 5 da seção 6).
- `empacotamento-oferta-executavel` — cobre fatia 5.2; útil se o DEOC ainda estiver fino em oferta.
