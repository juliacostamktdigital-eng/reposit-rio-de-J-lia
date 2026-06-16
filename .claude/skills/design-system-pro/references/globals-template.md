# Template do globals.css

Use este template como base para gerar o arquivo `globals.css` com os tokens extraídos da imagem de referência. Substitua todos os valores entre colchetes `[...]` pelos valores reais extraídos.

## Template Completo

```css
@import "tailwindcss";

:root {
  /* === BASE === */
  --background: [cor de fundo da página, ex: 0 0% 100%];
  --foreground: [cor do texto principal, ex: 222.2 84% 4.9%];

  /* === CARD === */
  --card: [fundo do card, ex: 0 0% 100%];
  --card-foreground: [texto do card, ex: 222.2 84% 4.9%];

  /* === POPOVER / DROPDOWN / TOOLTIP === */
  --popover: [mesmo que card ou branco];
  --popover-foreground: [mesmo que card-foreground];

  /* === PRIMARY (cor principal da marca) === */
  --primary: [cor primária extraída, ex: 221.2 83.2% 53.3%];
  --primary-foreground: [branco ou escuro baseado em contraste, ex: 210 40% 98%];

  /* === SECONDARY === */
  --secondary: [cinza claro ou versão muted, ex: 210 40% 96.1%];
  --secondary-foreground: [texto escuro, ex: 222.2 47.4% 11.2%];

  /* === MUTED === */
  --muted: [fundo cinza claro, ex: 210 40% 96.1%];
  --muted-foreground: [texto cinza médio, ex: 215.4 16.3% 46.9%];

  /* === ACCENT === */
  --accent: [mesmo que secondary ou leve tint, ex: 210 40% 96.1%];
  --accent-foreground: [texto escuro, ex: 222.2 47.4% 11.2%];

  /* === DESTRUCTIVE === */
  --destructive: [cor de erro/vermelho, ex: 0 84.2% 60.2%];
  --destructive-foreground: [branco, ex: 210 40% 98%];

  /* === BORDERS & INPUTS === */
  --border: [cor de borda extraída, ex: 214.3 31.8% 91.4%];
  --input: [borda levemente mais escura para inputs, ex: 214.3 31.8% 91.4%];
  --ring: [cor primária para focus rings, ex: 221.2 83.2% 53.3%];

  /* === BORDER RADIUS === */
  --radius: [raio extraído, ex: 0.5rem];

  /* === CHART COLORS === */
  --chart-1: [primária];
  --chart-2: [cor complementar];
  --chart-3: [variação];
  --chart-4: [variação];
  --chart-5: [variação];

  /* === SIDEBAR === */
  --sidebar: [fundo da sidebar, ex: 0 0% 98%];
  --sidebar-foreground: [texto da sidebar];
  --sidebar-primary: [primária];
  --sidebar-primary-foreground: [branco];
  --sidebar-accent: [accent];
  --sidebar-accent-foreground: [texto escuro];
  --sidebar-border: [cor de borda];
  --sidebar-ring: [primária];

  /* === CORES SEMÂNTICAS CUSTOMIZADAS === */
  --success: [verde, ex: 142.1 76.2% 36.3%];
  --success-foreground: [branco, ex: 355.7 100% 97.3%];
  --warning: [amarelo/laranja, ex: 45.4 93.4% 47.5%];
  --warning-foreground: [escuro para contraste, ex: 26 83.3% 14.1%];
  --info: [azul, ex: 201.3 96.3% 32.2%];
  --info-foreground: [branco, ex: 204 100% 97.1%];
}

.dark {
  /* Valores invertidos para modo escuro */
  --background: [fundo escuro, ex: 222.2 84% 4.9%];
  --foreground: [texto claro, ex: 210 40% 98%];
  --card: [fundo card escuro, ex: 222.2 84% 4.9%];
  --card-foreground: [texto card claro, ex: 210 40% 98%];
  --popover: [mesmo que card escuro];
  --popover-foreground: [mesmo que card-foreground escuro];
  --primary: [primária ajustada para escuro];
  --primary-foreground: [texto sobre primária escura];
  --secondary: [secondary escuro, ex: 217.2 32.6% 17.5%];
  --secondary-foreground: [texto claro, ex: 210 40% 98%];
  --muted: [muted escuro, ex: 217.2 32.6% 17.5%];
  --muted-foreground: [texto muted claro, ex: 215 20.2% 65.1%];
  --accent: [accent escuro, ex: 217.2 32.6% 17.5%];
  --accent-foreground: [texto claro, ex: 210 40% 98%];
  --destructive: [vermelho ajustado para escuro, ex: 0 62.8% 30.6%];
  --destructive-foreground: [texto claro, ex: 210 40% 98%];
  --border: [borda escura, ex: 217.2 32.6% 17.5%];
  --input: [input escuro, ex: 217.2 32.6% 17.5%];
  --ring: [ring para escuro, ex: 224.3 76.3% 48%];
  --sidebar: [sidebar escura];
  --sidebar-foreground: [texto sidebar claro];
  --sidebar-primary: [primária];
  --sidebar-primary-foreground: [texto claro];
  --sidebar-accent: [accent escuro];
  --sidebar-accent-foreground: [texto claro];
  --sidebar-border: [borda escura];
  --sidebar-ring: [ring escuro];
  --success: [verde ajustado para escuro];
  --success-foreground: [texto claro];
  --warning: [amarelo ajustado para escuro];
  --warning-foreground: [texto claro];
  --info: [azul ajustado para escuro];
  --info-foreground: [texto claro];
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-destructive-foreground: var(--destructive-foreground);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-sidebar: var(--sidebar);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-success: var(--success);
  --color-success-foreground: var(--success-foreground);
  --color-warning: var(--warning);
  --color-warning-foreground: var(--warning-foreground);
  --color-info: var(--info);
  --color-info-foreground: var(--info-foreground);
}

body {
  background: var(--background);
  color: var(--foreground);
  font-family: [fonte extraída], sans-serif;
}
```

## Gerando Escalas de Cores

Para gerar uma escala harmoniosa a partir de uma cor base:

1. **50:** Versão muito clara (95-98% lightness)
2. **100:** Versão clara (90-95% lightness)
3. **200:** Versão levemente clara (80-85% lightness)
4. **300:** Versão intermediária clara (65-75% lightness)
5. **400:** Versão intermediária (50-60% lightness)
6. **500:** Cor base (a cor extraída)
7. **600:** Versão levemente escura (40-45% lightness)
8. **700:** Versão escura (30-35% lightness)
9. **800:** Versão muito escura (20-25% lightness)
10. **900:** Versão quase preta (10-15% lightness)

Mantenha o hue (matiz) constante e ajuste saturation levemente (mais saturado no meio, menos nos extremos).

## Formato de Cores

shadcn/ui usa o formato HSL sem a função `hsl()`. Exemplo:
- Correto: `221.2 83.2% 53.3%`
- Incorreto: `hsl(221.2, 83.2%, 53.3%)`
- Incorreto: `#3b82f6`

Converta todas as cores extraídas para este formato HSL.
