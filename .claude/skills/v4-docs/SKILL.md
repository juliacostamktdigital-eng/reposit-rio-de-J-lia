---
name: v4-docs
description: >
  Skill especializado em criação e edição de documentos Word (.docx) com a identidade visual da V4 Company. Use sempre que o usuário pedir relatórios, briefings, propostas, contratos ou qualquer documento Word com a marca V4. Este skill combina o DOCX skill técnico com as diretrizes do brandbook V4 — identidade visual, paleta, tipografia e tom de voz são definidos no skill v4-brand-v2, que deve ser consultado em conjunto.
---

# V4 Docs — Skill de Criação de Documentos Word

> **Identidade de marca:** As especificações de cores, tipografia, tom de voz, logo e grafismos estão no skill **v4-brand-v2**. Leia-o antes de começar qualquer criação.
>
> **Técnica DOCX:** Use o skill **docx** para criar com docxjs, editar via unpack/XML, ou ler/converter documentos existentes.

---

## FLUXO DE TRABALHO

### 1. Antes de começar
1. Leia o skill `v4-brand-v2` para as diretrizes de marca (cores, tipografia, tom de voz)
2. Leia o skill `docx` para o workflow técnico (docxjs, unpack/pack)
3. Verifique assets disponíveis em `Design System V4/`:
   - `logo-v4-white.png` — logo versão branca
   - `logo-v4-red.png` — logo versão vermelha (para documentos de fundo claro)
   - `Morgane/` — fonte de títulos (se disponível)
   - `IBMPlexSans/` — fonte de corpo

### 2. Criação ou edição
- **Criar do zero:** usar `docxjs` (npm) com estilos V4 aplicados
- **Editar existente:** unpack → editar XML → repack

### 3. Entrega
Salvar em `/sessions/quirky-pensive-meitner/mnt/Clientes/[NomeCliente]/` e fornecer link `computer://`

---

## IDENTIDADE VISUAL EM DOCUMENTOS WORD

### Cabeçalho (Header)
```
Logo: logo-v4-red.png (fundo claro) ou logo-v4-white.png (fundo escuro)
Posição: canto superior direito do header
Tamanho: ~2–3cm de largura
Linha separadora: 2pt sólida #E50914
```

### Rodapé (Footer)
```
Esquerda: Nome do documento / cliente
Centro: Número de página
Direita: "V4 COMPANY" ou logo pequena
Linha separadora: 1pt sólida #E50914 acima
```

### Capa do documento
```
Fundo: #1A1814 (bloco de cor ou página inteira)
Título: Morgane Black / Arial Black | 36–44pt | #FFFFFF
Subtítulo: IBM Plex Sans / Calibri | 16pt | #FFFFFF 70%
Linha de acento: #E50914 (3–4pt)
Logo: logo-v4-white.png (canto inferior direito ou centro inferior)
```

---

## ESTILOS TIPOGRÁFICOS

| Estilo Word | Fonte V4 | Fallback | Tamanho | Cor | Uso |
|-------------|----------|---------|---------|-----|-----|
| Heading 1 | Morgane Black | Arial Black | 28–32pt | `#E50914` ou `#1A1814` | Título de seção principal |
| Heading 2 | Morgane Bold | Arial Black | 20–24pt | `#1A1814` | Subtítulo de seção |
| Heading 3 | IBM Plex Sans SemiBold | Calibri SemiBold | 14–16pt | `#1A1814` | Título de subseção |
| Normal / Body | IBM Plex Sans Regular | Calibri | 10–11pt | `#1A1814` | Corpo de texto |
| Caption | IBM Plex Sans Light | Calibri Light | 9pt | `#464646` | Legendas, notas de rodapé |
| Quote / Citação | IBM Plex Sans Light Italic | Calibri Italic | 11pt | `#FF8888` | Insights, citações em destaque |
| Label / Tag | IBM Plex Sans SemiBold | Calibri Bold | 8–9pt | `#E50914` | Labels, tags de seção |

> **Caixa Alta obrigatória em:** Heading 1, Heading 2, labels/tags

---

## PALETA DE CORES PARA DOCUMENTOS

Documentos V4 usam paleta adaptada para fundo claro (papel/tela):

| Uso | HEX |
|-----|-----|
| Títulos principais | `#1A1814` (Preto Profundo) ou `#E50914` (Vermelho V4) |
| Corpo de texto | `#1A1814` |
| Destaque / acento | `#E50914` |
| Subtítulos / apoio | `#464646` (Cinza) |
| Insight / citação | `#FF8888` |
| CTA / botão | `#FFDD00` (Amarelo) |
| Fundo de tabela header | `#E50914` |
| Fundo de tabela linha ímpar | `#F5F5F5` |
| Fundo de tabela linha par | `#FFFFFF` |
| Bordas de tabela | `#E50914` ou `#CCCCCC` |

> Para documentos com tema escuro (ex: proposta premium):
> - Fundo: `#1A1814` | Texto: `#FFFFFF` | Acento: `#E50914`

---

## TABELAS

### Estilo padrão V4

```
Header: fundo #E50914 | texto #FFFFFF | Bold | Caixa Alta
Linha ímpar: fundo #F5F5F5
Linha par: fundo #FFFFFF
Bordas externas: 1.5pt #E50914
Bordas internas: 0.5pt #CCCCCC
Texto: IBM Plex Sans / Calibri Regular 10pt #1A1814
```

### Código docxjs — tabela V4
```javascript
new Table({
  rows: [
    new TableRow({
      tableHeader: true,
      children: headers.map(h => new TableCell({
        shading: { fill: "E50914" },
        children: [new Paragraph({
          children: [new TextRun({ text: h.toUpperCase(), bold: true, color: "FFFFFF", font: "Calibri" })]
        })]
      }))
    }),
    ...rows.map((row, i) => new TableRow({
      children: row.map(cell => new TableCell({
        shading: { fill: i % 2 === 0 ? "F5F5F5" : "FFFFFF" },
        children: [new Paragraph({
          children: [new TextRun({ text: cell, font: "Calibri", size: 20 })]
        })]
      }))
    }))
  ]
})
```

---

## ELEMENTOS VISUAIS EM DOCUMENTOS

### Caixas de destaque (callout boxes)
```
Tipo "Info": borda esquerda 4pt #E50914 | fundo #FFF5F5 | texto #1A1814
Tipo "Insight": fundo #1A1814 | texto #FFFFFF | acento #FF8888
Tipo "CTA": fundo #E50914 | texto #FFFFFF | Bold
```

### Separadores de seção
```
Linha horizontal: 2pt sólida #E50914 | largura total
Espaçamento: 12pt acima e abaixo
```

### Numeração de listas
```
Bullets: ● cor #E50914 | texto #1A1814 | IBM Plex Sans / Calibri Regular
Numeração: negrito #E50914 | texto #1A1814
```

---

## TIPOS DE DOCUMENTO V4

| Tipo | Características específicas |
|------|-----------------------------|
| **Proposta Comercial** | Capa escura (`#1A1814`), seções com header vermelho, tabela de preços V4, assinatura com logo |
| **Relatório de Performance** | Fundo claro, métricas em destaque com cor `#E50914`, tabelas alternadas, rodapé com logo |
| **Briefing Estratégico** | Layout limpo, títulos Morgane/Arial Black, blocos de insight em `#FF8888` |
| **Contrato / Proposta** | Tipografia institucional, cabeçalho com logo, rodapé com número de página |
| **E.E. (Estruturação Estratégica)** | Estrutura por seções/semanas, badges de status coloridos, tom de voz V4 |

---

## TOM DE VOZ EM DOCUMENTOS

> Consultar regras completas no skill `v4-brand-v2`.

Resumo para documentos:
- Títulos em **CAIXA ALTA** com linguagem direta
- Inicie seções com afirmação, nunca com contexto
- Frases curtas, ritmo 3×3 (3 blocos, 3 frases por bloco)
- Sem frases motivacionais genéricas
- Sem promessas sem base de dados
- Palavras-chave: **meta, entrega, performance, resultado, dono, desafio, avanço**

---

## MARGENS E LAYOUT PADRÃO

```
Página: A4 (21 × 29,7cm) ou Letter (21,59 × 27,94cm)
Margens: Superior 2.5cm | Inferior 2.5cm | Lateral 2.5cm
Header height: 1.5cm
Footer height: 1.2cm
Espaçamento entre parágrafos: 6–8pt após
Espaçamento de linha: 1.15 (corpo) | 1.0 (tabelas)
```

---

## CHECKLIST ANTES DE ENTREGAR

- [ ] Logo V4 no cabeçalho (versão adequada ao fundo)
- [ ] Linha de acento `#E50914` no header e/ou capa
- [ ] Heading 1 e 2 em Morgane/Arial Black, caixa alta
- [ ] Corpo em IBM Plex Sans/Calibri
- [ ] Vermelho sempre `E50914` — nunca `E80403` ou outros
- [ ] Tabelas com header `E50914` e linhas alternadas
- [ ] Rodapé com numeração de página
- [ ] Tom de voz V4 aplicado nos títulos
- [ ] Sem fontes não autorizadas
- [ ] Sem marrom, sem cores fora da paleta

---

## REFERÊNCIAS

- **Brand Identity:** skill `v4-brand-v2` — cores, tipografia, tom de voz, logo, grafismos
- **Técnica DOCX:** skill `docx` — docxjs, unpack/pack, extração de conteúdo
- **Assets:** `Design System V4/` — logo-v4-white.png, logo-v4-red.png, fontes Morgane e IBM Plex Sans
- **Design System Doc:** `Design System V4/design-system-slides-v4.md`
