# Referência Do Gerador De Copy Para Campanhas Leadgen

Fontes:

- `assets/canonicos/04_DOCUMENTO_COPY_FINAL_DCC_CANONICO.md`
- `.claude/skills/04_DOCUMENTO_COPY_FINAL_DCC_CANONICO/biblioteca-angulos-hooks-copy/reference.md`
- `.claude/skills/01_TAXONOMIA_UTM_IDS_E_SUBPARAMETROS/gerador-taxonomia-utm-ids/reference.md`

## Princípio

Copy de anúncio não é frase solta. Cada variação deve preservar a hipótese de comunicação, a etapa de funil, a promessa, a prova e os atributos que serão lidos depois em performance.

## Campos Obrigatórios Por Anúncio

- `creative_id` previsto;
- persona;
- etapa;
- formato;
- hook;
- texto principal;
- headline;
- descrição;
- CTA;
- prova usada;
- objeção atacada;
- `utm_content` ou atributos previstos;
- variação.

## Estrutura Da Copy

### Texto Principal

Deve conter:

- hook nos primeiros caracteres;
- contexto/tensão;
- mecanismo ou promessa;
- prova ou credencial;
- CTA coerente.

### Headline

Deve reforçar:

- benefício principal;
- dor central;
- ação esperada;
- oferta.

### Descrição

Use para:

- reduzir objeção;
- qualificar o lead;
- deixar claro próximo passo;
- reforçar prova.

### CTA

Exemplos por etapa:

- TOFU: descobrir, diagnosticar, entender, ver análise;
- MOFU: comparar, avaliar, ver como funciona, receber diagnóstico;
- BOFU: solicitar conversa, agendar, falar com especialista, pedir proposta.

## Variações Controladas

Uma variação deve mudar uma alavanca principal:

- hook;
- prova;
- objeção;
- promessa;
- CTA;
- formato;
- etapa.

Evite mudar persona, dor, promessa e formato ao mesmo tempo, porque isso destrói a leitura do teste.

## Regras Por Etapa

### TOFU

- educar;
- criar tensão;
- nomear dor;
- atacar status quo;
- evitar CTA muito agressivo se o público ainda não está consciente.

### MOFU

- explicar mecanismo;
- mostrar prova;
- responder objeção;
- comparar alternativa;
- qualificar intenção.

### BOFU

- reforçar oferta;
- reduzir risco;
- mostrar urgência real;
- usar CTA direto;
- deixar próximo passo claro.

## Claims

### Permitidos

- promessas sustentadas por prova;
- comparações verificáveis;
- números com fonte;
- benefícios plausíveis.

### Proibidos

- garantias absolutas sem base;
- promessas financeiras não comprovadas;
- termos jurídicos sensíveis;
- superlativos sem prova;
- claims que o cliente não consegue entregar;
- claims que criam risco regulatório.

## Conexão Com Tracking

Cada anúncio deve preservar:

- formato -> `fmt`;
- persona -> `icp`;
- hook -> `hook`;
- motivador -> `mot`;
- dor -> `dor`;
- ângulo -> `ang`;
- etapa -> `stage`;
- versão -> `ver`.

Formato:

```text
fmt-[formato]__icp-[persona]__hook-[tipo]__mot-[motivador]__dor-[dor]__ang-[angulo]__stage-[etapa]__ver-[versao]
```

## Critérios De Qualidade

Copy está aprovada quando:

- tem hipótese explícita;
- usa linguagem da persona;
- não promete sem prova;
- CTA combina com etapa;
- objeção relevante foi considerada;
- `utm_content` permite leitura posterior;
- variação está isolada;
- não há claim proibido.
