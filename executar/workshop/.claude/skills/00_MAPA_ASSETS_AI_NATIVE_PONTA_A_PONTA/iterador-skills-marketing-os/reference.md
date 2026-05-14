# Rubrica Do Iterador De Skills

Fonte normativa principal: `assets/canonicos/00_MAPA_ASSETS_AI_NATIVE_PONTA_A_PONTA.md`.

Esta rubrica serve para atualizar skills do Marketing OS sem perder a relacao com o workflow visual, com o playbook canonico e com a boa arquitetura de skills.

## Contrato De Contexto

Toda edicao precisa responder quatro perguntas antes de mudar arquivos:

- Qual e o workflow mais recente?
- Qual playbook canonico governa a skill?
- Qual capacidade operacional a skill deve executar?
- O que deve continuar no playbook, em vez de entrar no `SKILL.md`?

Se uma skill estiver em `.claude/skills/<PLAYBOOK_DIR>/<skill>/`, o playbook acima dela e `assets/canonicos/<PLAYBOOK_DIR>.md`.

Se uma skill nao tiver playbook direto, trate como transversal: leia o canônico `00` e os canonicos dos playbooks afetados.

## Anatomia Esperada De Uma Skill

O `SKILL.md` deve conter:

- frontmatter com `name` estavel e `description` acionavel;
- `Quando Usar` com gatilhos reais de usuario;
- fronteira de `Nao use` quando houver risco de confusao;
- `Inputs Necessarios`;
- workflow operacional em passos;
- `Output Esperado`;
- uso de templates/scripts quando existirem;
- `Definition Of Done`;
- `Armadilhas`, `Cuidados` ou riscos quando a operacao for fragil;
- referencias para playbook, `reference.md`, templates e scripts.

Detalhes extensos devem ir para `reference.md`. Exemplos, schemas e formatos devem ir para `templates/` ou `scripts/` quando isso economizar contexto e reduzir erro.

## Checklist De Melhoria

Use esta lista para revisar uma skill:

- A description permite disparo correto sem ser generica?
- A skill executa uma capacidade pequena, nao um playbook inteiro?
- Os inputs diferenciam obrigatorio, desejavel e evidencia ausente?
- O workflow gera decisao ou artefato concreto?
- O output tem formato claro?
- O DoD e verificavel?
- A skill sabe quando chamar outra skill ou enviar gap para backlog?
- O texto evita prometer dado, maturidade ou decisao sem evidencia?
- O `reference.md` nao repete o `SKILL.md` sem necessidade?
- Scripts e templates ainda batem com o fluxo descrito?

## Escala De Intervencao

### Leve

Use para clareza, gatilhos, pequenas lacunas e referencias quebradas.

Mudancas tipicas:

- melhorar description;
- explicitar `Nao use`;
- ajustar DoD;
- corrigir link de template/script;
- adicionar armadilha operacional.

### Media

Use quando a skill esta certa, mas incompleta.

Mudancas tipicas:

- reorganizar workflow;
- mover detalhes para `reference.md`;
- criar ou ajustar template;
- alinhar outputs com playbook;
- adicionar chamada para skill dependente.

### Profunda

Use quando a capacidade esta mal separada ou misturada.

Mudancas tipicas:

- dividir uma skill em duas;
- criar skill nova para capacidade independente;
- transformar conteudo normativo longo em referencia;
- atualizar script/template junto com `SKILL.md`;
- revisar `playbook-skills.json` via build.

## Anti-Padroes

Evite:

- copiar secoes inteiras do playbook canonico para o `SKILL.md`;
- criar checklist generico sem decisao;
- misturar criacao, QA, leitura e governanca numa skill unica;
- remover fronteiras N2/N3;
- apagar scripts/templates que ainda sao referenciados;
- renomear `name` sem atualizar o ecossistema;
- editar skill especialista sem ler o canônico do diretório pai;
- atualizar indice manualmente quando `node build-docs.mjs` resolve.

## Regras Para Extensao

Crie uma nova skill quando a nova capacidade:

- tem gatilho de usuario proprio;
- recebe inputs diferentes;
- produz output diferente;
- pode ser usada sem carregar a skill original;
- teria workflow e DoD proprios.

Estenda a skill atual quando a nova capacidade:

- e subpasso natural do mesmo trabalho;
- usa os mesmos inputs;
- produz o mesmo artefato final;
- so precisa de mais criterio, template ou script auxiliar.

## Validacao Semantica

Depois de editar, confira:

- o playbook canonico ainda e citado corretamente;
- o workflow mais recente nao contradiz a mudanca;
- as skills irmas nao ficaram duplicadas;
- o output da skill alimenta o proximo asset ou decisao da jornada;
- gaps viram backlog, QA, changelog ou acionamento de outra skill;
- qualquer novo script tem exemplo de uso e valida entrada minima.
