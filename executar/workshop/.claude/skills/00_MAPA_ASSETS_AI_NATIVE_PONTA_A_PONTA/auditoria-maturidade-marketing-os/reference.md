# Referencia Da Auditoria De Maturidade

Fonte normativa: `assets/canonicos/00_MAPA_ASSETS_AI_NATIVE_PONTA_A_PONTA.md`.

## Intencao Da Auditoria

A auditoria separa "ter coisas" de "ter um sistema operando". O objetivo e descobrir se a conta consegue rodar, ser auditada, aprender e melhorar sem depender de memoria individual.

## Escala De Maturidade

### N0 - Ausente

Use quando:

- nao ha asset;
- nao ha dono;
- nao ha evidencia;
- o processo depende de conversa solta;
- a informacao precisa ser recoletada.

### N1 - Existente Ou Rascunho

Use quando:

- existe arquivo, checklist, campanha, planilha ou setup inicial;
- ha definicao informal;
- parte do processo foi feita, mas sem rastro suficiente;
- nao da para auditar de ponta a ponta.

N1 nao deve ser vendido como implementado.

### N2 - Implementado E Auditavel

Use quando:

- assets obrigatorios existem;
- donos estao claros;
- dados minimos sao preservados;
- ha evidencia de execucao;
- processo consegue ser auditado;
- lead teste, quando aplicavel, percorre a cadeia inteira.

N2 responde: "isso roda e eu consigo provar".

### N3 - Gerenciado

Use quando:

- dados sao lidos em cadencia;
- decisoes sao registradas;
- hipoteses entram no backlog;
- aprendizados alimentam o proximo ciclo;
- padroes sao canonizados para reuso;
- mudancas tem changelog.

N3 responde: "isso melhora com base em dados".

## Componentes Avaliaveis

### 1. Handoff E Discovery

N2 exige:

- promessa comercial documentada;
- escopo e exclusoes;
- stakeholders e aprovadores;
- discovery/transcricao;
- riscos e perguntas abertas.

N3 exige:

- desvios recorrentes voltam para vendas/onboarding;
- pendencias e riscos sao acompanhados;
- tempo e completude do handoff sao medidos.

Falsos positivos:

- kickoff feito sem sintese operacional;
- escopo em contrato, mas nao traduzido para execucao;
- promessa comercial conhecida apenas pelo closer.

### 2. Diagnostico E Pacote V1

N2 exige:

- diagnostico por componente;
- baseline de marketing e vendas;
- causa do problema separada de sintoma;
- lista curta de assets v1;
- lista do que fica fora;
- dependencias do cliente.

N3 exige:

- diagnosticos comparados por ciclo;
- gaps recorrentes viram melhoria de processo;
- mudancas de pacote v1 sao registradas.

Falsos positivos:

- diagnostico que so diz "resultado ruim";
- criar todos os assets sem criterio;
- nao registrar o que ficou fora.

### 3. Estrategia, Oferta E Mercado

N2 exige:

- benchmark ou leitura externa;
- DEOC/UCM/DCC ou equivalente;
- personas ou ICP operacional;
- narrativa, proposta e provas;
- claims permitidos/proibidos.

N3 exige:

- angulos vencedores marcados;
- objeções comerciais entram no documento;
- aprendizados por cohort/segmento versionados.

Falsos positivos:

- persona generica;
- promessa sem prova;
- benchmark sem decisao.

### 4. Midia

N2 exige:

- plano de midia com budget, canais, metas e hipoteses;
- cenarios;
- estrutura planejada de campanha;
- plano de tracking;
- guardrails.

N3 exige:

- previsto vs realizado revisado;
- premissas atualizadas com dados reais;
- decisoes de budget registradas.

Falsos positivos:

- verba dividida por canal sem tese;
- CPL como unica decisao;
- campanha sem hipotese.

### 5. Criativo E LP

N2 exige:

- briefing por criativo;
- criativos com ID e hipotese;
- LP/ponto de conversao coerente com promessa;
- QA de claims, CTA, formulario, mobile e tracking.

N3 exige:

- performance retroalimenta novos briefs;
- atributos vencedores sao reaproveitados;
- LP recebe testes registrados.

Falsos positivos:

- peca bonita sem hipotese;
- LP publicada sem lead teste;
- varias versoes sem controle.

### 6. Tracking E Dados

N2 exige:

- taxonomia UTM;
- IDs de campanha/adgroup/criativo/teste;
- campos CRM/backup;
- first-touch/last-touch quando aplicavel;
- teste ponta a ponta;
- dicionario de dados.

N3 exige:

- qualidade comercial usada no debrief;
- campanhas otimizadas por MQL/SQL/venda;
- erros de dados viram acao corretiva.

Falsos positivos:

- UTM chega na LP, mas nao no CRM;
- planilha backup inexistente;
- creative_id sem preenchimento;
- CRM e plataforma nao conciliam.

### 7. CRM, SLA E Vendas

N2 exige:

- MQL/SQL definidos;
- SLA e roteamento;
- dono comercial;
- motivos de desqualificacao;
- feedback volta para marketing.

N3 exige:

- SLA monitorado;
- motivos de perda alimentam copy/oferta;
- marketing e vendas revisam juntos o funil.

Falsos positivos:

- "vendas atende rapido" sem timestamp;
- rejeicao sem motivo;
- lead sem dono.

### 8. Testes, Performance E Aprendizado

N2 exige:

- planilha de testes;
- export de midia;
- export CRM/leads;
- decisao por teste;
- leitura inclui qualidade do lead.

N3 exige:

- debrief em cadencia;
- backlog priorizado;
- changelog de mudancas;
- aprendizados viram proximo briefing.

Falsos positivos:

- relatorio sem decisao;
- teste sem variavel;
- aprendizado sem evidencia ou limite.

## Regras De Score

Pontue cada componente:

- N0 = 0 pontos;
- N1 = 1 ponto;
- N2 = 2 pontos;
- N3 = 3 pontos;
- bloqueado = 0 pontos e severidade minima `bloqueador`.

Score geral:

```text
score = soma_pontos / pontos_possiveis
```

Faixas:

- 0-39%: vermelho, sistema nao confiavel;
- 40-69%: amarelo, operacao parcial com riscos;
- 70-84%: verde parcial, N2 predominante;
- 85-100%: verde forte, N2/N3 consistente.

## Regra De Decisao

- Se tracking, LP/formulario ou CRM estao bloqueados, nao recomendar go-live sem risco aceito.
- Se estrategia/oferta esta N0/N1, nao recomendar escala de midia.
- Se ha campanha sem hipotese e sem planilha, nao chamar de teste.
- Se nao ha feedback comercial, nao otimizar apenas por CPL.
- Se nao ha debrief e changelog, nao chamar de N3.
