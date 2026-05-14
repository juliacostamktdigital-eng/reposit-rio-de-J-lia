# Referência Da Matriz Problema Proposta Prova

Fonte normativa: `assets/canonicos/10_PLANEJAMENTO_ESTRATEGICO_UCM_CANONICO.md`.

## Princípio

Toda promessa forte precisa apontar para uma prova ou ficar marcada como claim pendente.

A matriz conecta o que dói, por que importa, como a oferta resolve e que evidência sustenta a promessa.

## Campos Por Problema

- nome do problema;
- descrição objetiva;
- impacto prático;
- impacto emocional;
- impacto financeiro ou operacional;
- voz do cliente;
- motivo de priorização;
- estágio do funil onde aparece.

## Campos De Proposta

- promessa principal;
- mecanismo único;
- diferenciais reais;
- benefício racional;
- benefício emocional;
- prova;
- risco reduzido;
- custo de não agir.

## Fórmula De Proposta

```text
Para [persona], que sofre com [problema], [produto/oferta] entrega [resultado] por meio de [mecanismo], sem [objeção], comprovado por [prova].
```

## Classificação De Prova

- `forte`: número, case, certificação, demonstração ou fonte confiável.
- `parcial`: evidência útil, mas ainda incompleta.
- `ausente`: promessa sem sustentação.
- `restrita`: evidência sensível, jurídica ou comercialmente limitada.

## Matriz 3D — Problema × Proposta × Prova-Por-Papel

A matriz 3D reconhece que **a mesma proposta exige provas distintas conforme o papel** no comitê de decisão. Uma prova que ressoa com o Economic Buyer (ROI) não convence o Technical Buyer (que quer arquitetura) e não habilita o Champion a vender pra dentro.

### Os Quatro Papéis

| Papel | O Que Quer Ver | Tipos De Prova Que Ressoam |
| --- | --- | --- |
| Economic Buyer | Justificativa financeira, payback, TCO, ROI | Caso quantificado, payback em meses, comparativo TCO 3 anos, redução de custo absoluta |
| User | Como vou usar isso no dia a dia | Demo, screenshot, fluxo guiado, vídeo de uso real, depoimento de usuário-par |
| Technical Buyer | Risco técnico, segurança, integração, conformidade | Arquitetura, certificações (SOC 2, ISO 27001), API docs, SLA, penetration test |
| Champion | Munição para defender a compra com pares | Case interno aplicável, narrativa simples, deck de uma página, ROI traduzível |

### Exemplo Concreto B2B (SaaS antifraude)

Mesma proposta — "Onboarding antifraude que aprova mais cliente bom" — ganha 4 provas distintas:

| Papel | Prova Específica |
| --- | --- |
| Economic Buyer (CFO) | "Cliente X reduziu chargebacks em 38% com payback em 4,2 meses" |
| User (analista de risco) | "Demo do score em produção mostrando alerta em <300ms" |
| Technical Buyer (CISO) | "Certificação SOC 2 Type II + arquitetura zero-trust + DPA padrão LGPD" |
| Champion (líder de produto) | "Deck de 1 página: redução de fricção sem abrir brecha — narrativa pronta pra apresentar pro CFO" |

### Aplicação Prática

- Pergunte para cada promessa-forte: **quem precisa ser convencido?** Não basta uma prova só.
- Mapeie no mínimo 1 prova por papel ativo no funil daquela conta.
- Se a prova for ausente para um papel-crítico, registre como claim pendente daquele papel.

## Anti-Claim — O Que NÃO Podemos Afirmar

Anti-claim explícito é tão importante quanto claim afirmativo. Lista o que está fora de jogo antes que copy/criativo/comercial atravesse linha vermelha.

### Três Categorias De Claim Proibido

1. **Regulatório**
   - Vedações de órgão regulador: ANVISA (saúde, suplemento, cosmético), CONAR (publicidade brasileira), Lei 14.790/2023 (apostas), BACEN (financeiro), CVM (investimento), SUSEP (seguro), ANS (saúde suplementar).
   - Exemplo proibido: "cura ansiedade" (suplemento), "garantia de retorno" (investimento), "promove saúde" sem registro ANVISA.

2. **Comparativo Sem Benchmark**
   - Comparação direta com concorrente nominal sem fonte publicada e auditável.
   - "Mais rápido que [concorrente]", "melhor que [marca]" sem teste padronizado, fonte terceira ou benchmark publicado.
   - CONAR exige base verificável; FTC exige substantiation prévio à veiculação.

3. **Factual Não Comprovado**
   - Afirmação de número, resultado ou capacidade técnica sem reasonable basis no momento da emissão.
   - "Reduz 40% do custo" sem case, "aprovação em 30s" sem benchmark interno medido, "10.000 clientes" sem contagem auditável.
   - Claim factual sem reasonable basis = passivo regulatório direto.

### Como Registrar

Cada anti-claim deve ter: `claim_proibido` (texto literal), `categoria` (regulatorio | comparativo | factual), `motivo` (qual norma/lacuna específica).

## Reasonable Basis (FTC) E Substantiation

Vocabulário regulatório formal — adotado por FTC nos EUA e referenciado pelo CONAR no Brasil.

### Reasonable Basis

Toda afirmação objetiva precisa ter base razoável **antes** de ser veiculada. Não se cria a prova depois — se tem a prova, então afirma.

Critérios FTC para reasonable basis:

- **Tipo de claim**: quanto mais específico (número, comparação, científico), mais forte deve ser a evidência.
- **Tipo de produto**: claims sobre saúde/segurança/finanças exigem evidência mais robusta que claim genérico de preferência.
- **Consequência do erro**: claim cujo erro causa dano (saúde, segurança, perda financeira) exige nível mais alto de substantiation.
- **Custo de obter evidência**: não é desculpa se o custo for razoável frente ao benefício comercial.
- **Padrão da indústria**: o que peritos da área consideram suficiente para sustentar o claim.

### Substantiation

Documentação concreta que sustenta o claim no momento da emissão. Pode ser:

- Estudo controlado (clínico, comparativo, técnico).
- Benchmark mensurado interno auditável.
- Case com cliente real assinado (não anônimo sem rastro).
- Certificação de órgão acreditado.
- Dado público de fonte primária (IBGE, BACEN, ANVISA).

**Regra prática**: se você não consegue mostrar a substantiation em 30 segundos quando questionado, o claim não tem reasonable basis e não pode ir pro ar.

### CONAR — Brasil

Código Brasileiro de Autorregulamentação Publicitária artigos 23 e 27: anúncio deve ser passível de comprovação imediata. Claim sem comprovação = anúncio anti-ético, sujeito a sustação.

## Hierarquia Message House (Atlassian)

Estrutura padrão Atlassian para garantir consistência narrativa entre todos os ativos (LP, deck, copy, criativo, sales).

```
                 ┌──────────────────────────────┐
                 │       ROOF CLAIM             │
                 │   (mensagem-mãe da marca)    │
                 └──────────────────────────────┘
                  /            |            \
          ┌────────────┐ ┌────────────┐ ┌────────────┐
          │ PILLAR 1   │ │ PILLAR 2   │ │ PILLAR 3   │
          │ (tema-     │ │ (tema-     │ │ (tema-     │
          │  suporte)  │ │  suporte)  │ │  suporte)  │
          └────────────┘ └────────────┘ └────────────┘
            |    |    |    |    |    |    |    |    |
          PP   PP   PP   PP   PP   PP   PP   PP   PP
          (proof points — provas concretas por pillar)
```

### Componentes

- **Roof Claim**: a promessa-mãe. Uma frase, memorável, sintetiza o porquê do produto/marca.
- **Pillars** (3 a 5): temas de suporte que sustentam o roof. Cada pillar é uma promessa-secundária verificável.
- **Proof Points**: evidência concreta sob cada pillar — número, case, certificação, demonstração. Cada pillar precisa de no mínimo 2 proof points.

### Regra De Consistência

Se um claim em copy não rastreia para um pillar, e um pillar não rastreia para o roof, a hierarquia está quebrada e a comunicação vai parecer fragmentada.

### Exemplo

- **Roof claim**: "Onboarding sem fricção, sem fraude."
- **Pillar 1**: Aprovação rápida — proof points: "tempo médio 28s", "97% aprovados sem revisão manual".
- **Pillar 2**: Fraude contida — proof points: "redução de 38% chargeback no caso X", "score validado em 4M decisões/mês".
- **Pillar 3**: Conformidade — proof points: "SOC 2 Type II", "DPA LGPD padrão".

## Aplicação Operacional

| Ativo | Uso da matriz |
| --- | --- |
| DEOC/DCC | Consolidar promessa, mecanismo, provas e claims |
| LP | Ordenar problema, impacto, solução, prova e objeções |
| Criativos | Transformar problema em hook com evidência |
| Mídia | Definir ângulo por etapa de funil |
| Comercial | Preparar objeções e provas de abordagem |
| Tracking | Codificar dor, ângulo, persona e stage |

## Checklist N2

- problemas priorizados por impacto;
- voz do cliente registrada;
- mecanismo explícito;
- promessa tem prova;
- claims pendentes estão separados;
- restrições estão marcadas;
- matriz traduz para ativos;
- prova mapeada por papel (Economic Buyer / User / Technical Buyer / Champion) em promessas-forte;
- anti-claims explicitamente listados nas três categorias (regulatório / comparativo / factual);
- toda afirmação objetiva tem reasonable basis documentado;
- estrutura segue Message House (roof → pillars → proof points) consistente.
