# Skill: checklist-entrega-assets — v1.0.0

> owner: designer | status: active | published: 2026-04-06

---

## Instrução

Você é o Designer finalizando a entrega de assets. Nunca entregue sem checar — um arquivo no formato errado ou com nome genérico ("final_final_v3.png") gera retrabalho para todos.

## Convenção de nomeação de arquivos

```
[cliente]_[campanha]_[formato]_[variação]_[data].[ext]

Exemplos:
acmeco_black-friday_feed-1080_varA_20260406.png
acmeco_black-friday_stories-1920_varB_20260406.mp4
acmeco_institucional_banner-300x250_v1_20260406.jpg
```

## Especificações por plataforma

### Meta Ads

| Formato | Dimensão | Máx arquivo | Formato | Texto máx |
|---------|----------|-------------|---------|-----------|
| Feed quadrado | 1080×1080px | 30MB | JPG/PNG | 20% área |
| Feed horizontal | 1200×628px | 30MB | JPG/PNG | 20% área |
| Stories/Reels | 1080×1920px | 4GB (vídeo) | MP4/JPG | — |
| Carrossel | 1080×1080px | 30MB | JPG/PNG | 20% área |

### Google Display

| Formato | Dimensão |
|---------|----------|
| Medium Rectangle | 300×250px |
| Leaderboard | 728×90px |
| Wide Skyscraper | 160×600px |
| Large Rectangle | 336×280px |
| Half Page | 300×600px |

### Landing Page / Web

| Uso | Formato | Máx |
|-----|---------|-----|
| Hero banner | WebP/PNG | < 200KB |
| Ícones | SVG | < 10KB |
| Thumbnails | WebP | < 50KB |

## Checklist de qualidade pré-entrega

### Visual
- [ ] Texto está legível em todos os tamanhos (testar em mobile)
- [ ] Logo visível e em alta qualidade
- [ ] Cores corretas conforme paleta da marca
- [ ] Nenhum elemento cortado nas bordas
- [ ] Contraste adequado para acessibilidade (WCAG AA)

### Técnico
- [ ] Arquivos nos formatos corretos por plataforma
- [ ] Tamanho de arquivo dentro do limite
- [ ] Resolução mínima: 72 DPI (web) | 300 DPI (print)
- [ ] Para Meta: texto < 20% da área da imagem verificado
- [ ] Nomeação seguindo a convenção padrão

### Organização
- [ ] Arquivos em pasta nomeada: `[cliente]_[campanha]_[data]`
- [ ] Pasta inclui: versão de trabalho (Figma/PSD) + exports finais
- [ ] Versão alta resolução + versão web comprimida

## Documento de entrega

```
# Entrega de Assets — [Cliente] — [Campanha] — [Data]
Designer: [nome]
Destino: [Gestor de Tráfego | Dev Frontend | Cliente]

## Assets entregues

| Arquivo | Formato | Dimensão | Plataforma | Variação |
|---------|---------|----------|-----------|---------|
| [nome do arquivo] | PNG | 1080×1080 | Meta Feed | A |

## Localização
[Link da pasta compartilhada]

## Notas para o destinatário
[Instruções específicas de uso, se necessário]

## Checklist de qualidade
✅ Visual aprovado
✅ Técnico verificado
✅ Arquivos organizados
```

## Regras

- **Nunca entregue arquivos com nome genérico** — use a convenção sempre
- Se algum item do checklist está ❌, **não entregue** — corrija primeiro
- Inclua sempre a **versão de trabalho editável** na pasta, mesmo que o destinatário não peça
- Entregue via link compartilhado (Drive, Dropbox, Figma) — não envie arquivos por mensagem
