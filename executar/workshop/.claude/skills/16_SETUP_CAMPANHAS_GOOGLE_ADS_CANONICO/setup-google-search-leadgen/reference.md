# Referência — Google Search leadgen (playbook 16 + legado 11)

Fonte primária: **`16_SETUP_CAMPANHAS_GOOGLE_ADS_CANONICO.md`**. Complemento operacional: **`11-estrutura-campanhas-google-ads-search.md`**.

## 1. Quando usar Search (Seção 7)

Indicado quando há **demanda ativa**:

- busca por problema;
- busca por solução;
- busca por categoria;
- busca por concorrente **quando permitido**;
- busca de marca quando houver estratégia de defesa/captura.

## 2. Estrutura inicial de campanhas (Seção 7)

### Não-marca / intenção principal

- Grupo 00: problema direto;
- Grupo 01: solução/categoria;
- Grupo 02: comparativos/alternativas;
- Grupo 03: segmento/persona quando houver volume.

### Marca

- **Separada** para medir captura de demanda existente;
- pode ser desligada se não fizer sentido;
- **não misturar** com não-marca na leitura de aquisição (ver Seção 17).

### Concorrentes

- só quando **permitido e estratégico**;
- copy conforme regras legais e políticas de marca.

## 3. Palavras-chave (Seção 7)

- termos de **alta intenção**;
- correspondência **frase/exata** para controle inicial;
- **ampla** apenas quando conversão e negativas estiverem **maduras**;
- **negativas desde o dia 1.**

## 4. Negativas e cadência (Seção 11)

Lista inicial inclui exemplos do canônico: vagas/emprego; grátis/free quando não estratégico; curso/aula quando não é oferta; PDF/modelo quando indesejado; termos irrelevantes; regiões fora do escopo; **marca do cliente em campanha não-marca** quando a leitura exige aquisição pura.

**Revisar** termos de busca na primeira semana e em **cadência semanal** no início.

## 5. Nomenclatura (Seção 10)

**Campanha:** `{campaign_id} | search | {objetivo} | {movimento} | {slug}`

**Grupo:** `{adgroup_id} | {intencao} | {temperatura} | {tipo} | {slug}`

**Asset RSA (referência creative_id no governança interna):** `{creative_id} | {formato} | {hook} | {persona} | {slug} | {versao}`

## 6. Orçamento (Seção 12)

Fragmentação controlada; aprendizado; evitar mudanças grandes antes da janela de leitura; **tCPA/tROAS** com histórico; maximizar conversões para volume inicial quando fizer sentido; **não alterar budget/lance todo dia** (Seção 17).

## 7. Go-live Search (trecho Seção 14)

- Search com **negativas iniciais**;
- Search com **clusters, negativas e RSAs conferidos** quando aplicável.

## 8. O que evitar (recortes Seção 17 relevantes)

- **rodar Search sem negativas**;
- **misturar marca e não-marca** sem leitura separada;
- otimizar para **clique** quando o objetivo é lead qualificado;
- avaliar só por **CPL** sem MQL/SQL.

## 9. Síntese legado (skill 11)

Entradas típicas: plano de mídia Search, pack de produção (LP/mensagem), funil, benchmark de termos.

Componentes críticos legados: taxonomia por intenção; clustering; match types e governança de termos; **negativas + rotina de search terms**; coerência anúncio → LP → conversão.

## 10. Formato JSON (campos principais)

- `campanhas[].tipo`: `nao_marca` | `marca` | `concorrentes`
- `campanhas[].grupos[].keywords[]`: `termo`, `match`, `nota`
- `campanhas[].grupos[].rsa`: `headlines[]`, `descricoes[]`, `path1`, `path2`
- `negativas_baseline[]`: `termo`, `motivo`, `escopo` (conta / campanha / lista compartilhada)
- `rotina_search_terms`: texto com cadência
