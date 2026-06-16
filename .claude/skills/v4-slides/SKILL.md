---
name: v4-slides
description: >
  Skill especializado em criação e edição de apresentações PowerPoint (.pptx) com a identidade visual da V4 Company. Use sempre que o usuário pedir slides, apresentações ou decks com a marca V4. Este skill combina o PPTX skill técnico com as diretrizes do brandbook V4 — identidade visual, paleta, tipografia e tom de voz são definidos no skill v4-brand-v2, que deve ser consultado em conjunto.
---

# V4 Slides — Skill de Criação de Apresentações

> **Identidade de marca:** As especificações de cores, tipografia, tom de voz, logo e grafismos estão no skill **v4-brand-v2**. Leia-o antes de começar qualquer criação.
>
> **Técnica PPTX:** Use o skill **pptx** para unpack/edit/pack, geração via pptxgenjs e extração de conteúdo.

---

## FLUXO DE TRABALHO

### 1. Antes de começar
1. Leia `v4-brand-v2` para as diretrizes de marca
2. Leia o skill `pptx` para o workflow técnico
3. Verifique assets em `Design System V4/`:
   - `logo-v4-white.png` — logo para fundos escuros (padrão)
   - `logo-v4-red.png` — logo para fundos claros
   - `Morgane/` — fonte de títulos
   - `IBMPlexSans/` — fonte de corpo

### 2. Criação ou edição
- **Editar existente:** unpack → editar XML → pack
- **Criar do zero:** pptxgenjs ou unpack de template base

### 3. Entrega
Salvar em `/sessions/quirky-pensive-meitner/mnt/Clientes/[NomeCliente]/` com link `computer://`

---

## ANATOMIA DE SLIDE PADRÃO V4

Dimensões: **9144000 × 5143500 EMU** (widescreen 16:9)

```
┌──────────────────────────────────────────────────────────┐  fundo: #1A1814
│ ████ BARRA TOPO (h=54864, #E50914, largura total)        │
│                               SUBTÍTULO DE SEÇÃO ▸       │  Calibri 7.5pt #E50914, topo dir.
│                                                          │
│  TÍTULO PRINCIPAL                                        │  Arial Black 28–32pt #FFFFFF
│  subtítulo descritivo em caps                            │  Calibri 9pt #E50914 (abaixo do título)
│                                                          │
│  [CONTEÚDO: cards, tabelas, fluxos, métricas...]         │
│                                          [Logo V4]       │  canto inferior direito ~0.45"×0.45"
└──────────────────────────────────────────────────────────┘
```

### Posição do logo
- **Canto inferior direito** de todos os slides
- Tamanho: ~0.45" × 0.45" (ratio 1:1 — nunca distorcer)
- Arquivo: `logo-v4-white.png` em fundos escuros (padrão), `logo-v4-red.png` em fundos claros
- Margem mínima do canto: 0.1" em cada eixo

### Padrão de título `//`
- Usar `//` apenas quando os dois lados são **curtos e equilibrados**
- ✅ Válido: `DIAGNÓSTICO // SITUAÇÃO ATUAL`, `ORGANIZAÇÃO // FRENTES DE ATUAÇÃO`
- ❌ Inválido: título onde um dos lados é longo ou descritivo → usar título único direto
- Em dúvida, título único é sempre mais forte

### ❌ Não usar
- Número de seção como marca d'água — remove foco do conteúdo

---

## PALETA COMPLETA PARA SLIDES

### Core V4
| Uso | HEX |
|-----|-----|
| Vermelho principal | `#E50914` |
| Fundo de slide | `#1A1814` |
| Fundo de card / módulo | `#111111` ou `#1E1E1E` |
| Fundo de card escuro premium | `#2A0005` |
| Branco | `#FFFFFF` |
| Cinza apoio | `#464646` |
| Cinza claro (texto secundário) | `#AAAAAA` |

### Cores funcionais (dentro da paleta V4 oficial)
| Uso | HEX | Quando usar |
|-----|-----|-------------|
| Positivo / SIM / confirmado | `#FFDD00` | badges "SIM", checkmarks, indicadores positivos — amarelo V4 |
| Negativo / NÃO / crítico | `#E50914` | badges "NÃO", X, alertas — vermelho V4 |
| Insight / Detalhe | `#FF8888` | citações, insights em destaque — vermelho claro da escala |
| CTA / Destaque principal | `#FFDD00` | chamadas para ação, botões — amarelo V4 |
| Apoio / Neutro | `#464646` | categorias secundárias, rótulos de apoio — cinza V4 |

> ⚠️ Nunca usar `#000000` puro — usar `#1A1814`. Nunca usar `#E80403` — usar `#E50914`.
> ⚠️ **Azul, verde, teal e outras cores NÃO existem no brandbook V4.** Não incluir mesmo em slides densos ou categorizados por tipo. Usar variações dentro da paleta oficial (vermelho, amarelo, cinza, branco).

---

## PADRÕES DE COMPONENTES

### 1. Cards de módulo (2 ou 3 colunas)

```
Card:
  Fundo: #111111 ou #1A1A1A
  Borda superior: 2pt sólida na cor da categoria — usar vermelho #E50914, amarelo #FFDD00 ou cinza #464646
  Ou: sem borda + diferença de fundo sutil

Header do card:
  Ícone em círculo colorido (cor da categoria) + NOME EM CAPS
  Cor do nome: cor da categoria
  Tamanho: ~9pt Bold

Corpo do card:
  Seções internas com label em caps pequeno + cor da categoria
  Ex: "► FUNÇÃO ESTRATÉGICA", "≡ BUDGET & CANAIS", "◆ DISTRIBUIÇÃO & OBJETIVO"
  Labels: 7–8pt Bold, cor da categoria
  Texto: Calibri/IBM 9pt #FFFFFF ou #CCCCCC
  Bullets: › ou • em cor da categoria

Insight / Benefício Exclusivo:
  Box com fundo ligeiramente mais claro + borda esquerda 3pt #E50914 ou cor da categoria
  Texto italic ou light, cor #FF8888 ou #FFDD00
```

### 2. Métricas em destaque (números grandes)

```
Número principal:
  Tamanho: 32–48pt | Bold | cor #E50914 (ou cor da métrica)
  Ex: "R$ 953k", "70,4%", "R$ 1.138.084"

Label acima:
  Texto descritivo caps | 7–8pt | #AAAAAA

Label abaixo:
  Contexto | 8pt | #FFFFFF 70% italic
  Ex: "Faturamento total" | "1.425 de 2.024 vendas totais sem origem"
```

### 3. Badges de status

```
SIM / Positivo:
  Fundo: #FFDD00 | texto: #1A1814 | ✓ | Bold caps | bordas arredondadas (amarelo V4)

NÃO / Negativo:
  Fundo: #E50914 | texto: #FFFFFF | ✗ | Bold caps | bordas arredondadas (vermelho V4)

ORGÂNICO / Neutro positivo:
  Fundo: #464646 | texto: #FFFFFF | Bold caps (cinza V4)

Personalizado (ex: "A DEFINIR"):
  Fundo: #1A1814 | borda: 1pt #464646 | texto: #AAAAAA | caps

  ❌ Não usar verde #00C851 — fora da paleta V4
```

### 4. Fluxo de progressão (numbered flow)

```
Estrutura: 3 colunas com setas conectoras entre elas

Coluna:
  Número: "01" | Arial Black 18pt | #E50914
  Título: NOME EM CAPS | 10pt Bold | #FFFFFF
  Subtítulo: descrição | 8pt | #E50914 (ex: "TOPO DE FUNIL")
  Itens internos com label + valor
  Ex: "ORIGEM → Lead Frio (Ads/Orgânico)"
      "DESTINO → Dólar (R$247) ou Comunidade (R$49)"
      "Histórico: 1.123 vendas"

Seta conectora:
  › ou → entre colunas | #E50914 | tamanho ~16pt

Insight bottom bar:
  Fundo: #111111 | borda esquerda 3pt #E50914
  Texto: Calibri Light Italic | 9pt | #FFFFFF/#AAAAAA
  Destaque na frase: palavra-chave em cor #E50914 ou bold
```

### 5. Tabelas V4

```
Header:
  Fundo: #E50914 | texto: #FFFFFF | Bold | Caixa Alta | 8–9pt

Linha ímpar:  fundo #1E1E1E
Linha par:    fundo #2A2A2A
Linha com destaque (Bold):  fundo #1A0005 + texto Bold

Células de badge inline: badge de status dentro da célula (SIM/NÃO/ORGÂNICO)

Rodapé de legenda:
  Linha com bolinhas coloridas + label de categoria
  Ex: ● AQUISIÇÃO (TOPO) ● EDUCAÇÃO (MEIO) ● CONSULTORIA (FUNDO) ● ESPECIALIZADO
```

### 6. Tabs de navegação internas

```
Quando um slide tem 3 fases ou categorias lado a lado no topo:
  Tab selecionada:  fundo #E50914 | texto #FFFFFF | Bold caps
  Tab não selecionada: fundo #1E1E1E | texto #AAAAAA | caps
  Borda entre tabs: 1pt #333333
  Conteúdo abaixo das tabs: métricas + descrição

Ex: [CONTEÚDO DE VALOR] [▶ LIVE OBRIGATÓRIA ◀] [REMARKETING AGRESSIVO]
```

### 7. Barra de progresso

```
Container: fundo #333333 | h=20–24pt | borda-radius 4pt
Preenchimento: fundo #E50914 | largura proporcional ao %
Label left:  "SEM RASTREIO (70,4%)" | 8pt Bold #FFFFFF
Label right: "RASTREADO (29,6%)" | 8pt #AAAAAA
```

### 8. Ícones em círculos coloridos

```
Círculo:
  Tamanho: 28–36pt diâmetro
  Cor: sempre dentro da paleta V4 oficial
    - #E50914 (vermelho) — padrão, destaque, principal
    - #FFDD00 (amarelo) — CTA, positivo, atenção leve
    - #464646 (cinza) — neutro, secundário
    - #1A1814 (fundo) — com borda #E50914

  ❌ Sem azul, verde, teal ou outras cores fora da paleta

Ícone interno:
  Emoji ou ícone unicode | branco | centralizado
  Exemplos: 📊 💰 🎓 📱 ⚠️ 🎯 🔁

Uso: header de card, label de seção, indicador de tipo
```

### 9. Slide com 2 seções empilhadas

```
Quando um slide tem conteúdo denso, divida em 2 blocos verticais:

Bloco superior (h~45% do slide):
  Título + conteúdo 1

Linha divisória:
  1pt sólida #E50914 | largura total | entre os dois blocos

Bloco inferior (h~45%):
  Título + conteúdo 2

Cada bloco tem seu próprio título, subtítulo e logo V4
```

---

## TIPOS DE SLIDE

| Tipo | Estrutura | Componentes principais |
|------|-----------|----------------------|
| **Capa / Abertura** | Título grande centrado ou alinhado esq. | Fundo `#1A1814`, título Morgane/Arial Black 40pt, subtítulo vermelho |
| **Agenda / Índice** | 2 colunas com checkmarks | Ícone ✓ vermelho, texto corpo, número watermark |
| **Visão Geral / Tabela** | Tabela full-width | Header `#E50914`, badges inline, legenda de cores |
| **Cards Duplos** | 2 colunas iguais | Borda top colorida, ícone, seções internas |
| **Cards Triplos** | 3 colunas | Mesma estrutura, ícones distintos por categoria |
| **Métrica Destaque** | Número grande + contexto | 48pt vermelho, label, barra progresso opcional |
| **Fluxo de Progressão** | 3 colunas com setas | Numeração 01→02→03, insight bar abaixo |
| **Diagnóstico** | Split: problema esq. + riscos dir. | Métrica grande, barra, lista de riscos com ícones |
| **Slide Dual (2 blocos)** | Dois mini-slides empilhados | Linha `#E50914` separando, cada bloco independente |
| **Calendário / Timeline** | Linha do tempo ou Q1–Q4 | Caixas por período, ações listadas abaixo |
| **Fechamento / CTA** | Box de CTA + próximos passos | Botão `#E50914`, seta, texto instrucional |

---

## FONTES — FALLBACK

| Elemento | Fonte V4 | Fallback |
|----------|----------|---------|
| Título principal | Morgane Black | Arial Black |
| Subtítulo / header de card | Morgane Bold | Arial Black |
| Corpo / bullets | IBM Plex Sans Regular | Calibri |
| Legenda / apoio | IBM Plex Sans Light | Calibri Light |
| Tag de seção / label | IBM Plex Sans SemiBold | Calibri Bold |
| Métrica grande | IBM Plex Sans Bold | Arial Bold |

---

## CHECKLIST ANTES DE ENTREGAR

- [ ] Fundo `#1A1814` em todos os slides
- [ ] Barra `#E50914` no topo (h=54864 EMU)
- [ ] Subtítulo de seção `#E50914` caps abaixo do título principal
- [ ] Título direto, sem `//` quando um dos lados for longo ou descritivo
- [ ] Logo `logo-v4-white.png` no **canto inferior direito**, 0.45"×0.45", proporcional
- [ ] Vermelho sempre `E50914` — nunca `E80403` ou `000000`
- [ ] Badges SIM/NÃO/ORGÂNICO com cores corretas
- [ ] Tabelas com header `E50914` + linhas alternadas
- [ ] Cards com borda top colorida por categoria
- [ ] Métricas importantes em tipografia grande + vermelho
- [ ] Fluxos numerados com setas `→` entre colunas
- [ ] Insight bars com fundo `#111111` + borda esq. `#E50914`
- [ ] Cores funcionais dentro da paleta V4: amarelo=positivo/CTA, cinza=neutro, vermelho=negativo/alerta — sem verde nem azul
- [ ] Sem marrom, sem cores fora da paleta

---

## REFERÊNCIAS

- **Brand Identity:** skill `v4-brand-v2` — cores, tipografia, tom de voz, logo
- **Técnica PPTX:** skill `pptx` — unpack/pack, pptxgenjs, extração
- **Assets:** `Design System V4/` — logo, fontes Morgane e IBM Plex Sans
- **Design System Doc:** `Design System V4/design-system-slides-v4.md`
- **Referências visuais aprovadas:** slides de Roteiro Estratégico 2026 (Genspark style)
