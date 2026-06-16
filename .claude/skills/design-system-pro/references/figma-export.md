# Exportação para Figma

Este documento descreve como exportar o design system para o Figma após aprovação do usuário.

## Opção 1: MCP do Figma (Preferida)

Se o MCP do Figma (`mcp.figma.com`) estiver conectado, use as ferramentas nativas:

- `create_design_system_rules` — Cria regras do design system no Figma
- `get_variable_defs` — Consulta variáveis existentes
- `get_design_context` — Obtém contexto de design

O MCP permite interação direta sem necessidade de scripts adicionais.

## Opção 2: Figma Plugin API (Script)

Quando o MCP não estiver disponível, gere um script JavaScript para a Figma Plugin API. O usuário pode executá-lo de duas formas:

1. **Console do Figma:** Abrir o console de desenvolvedor no Figma Desktop (Menu > Plugins > Development > Open Console) e colar o script
2. **Plugin personalizado:** Criar um plugin local e rodar o script

### Template do Script de Exportação

```javascript
// ========================================
// Design System PRO - Figma Export Script
// ========================================
// Cole este script no console do Figma ou
// use-o como base para um plugin personalizado.

// ----- CORES -----

function createColorStyle(name, hex) {
  const style = figma.createPaintStyle();
  style.name = name;

  // Converter hex para RGB (0-1)
  const r = parseInt(hex.slice(1, 3), 16) / 255;
  const g = parseInt(hex.slice(3, 5), 16) / 255;
  const b = parseInt(hex.slice(5, 7), 16) / 255;

  style.paints = [{
    type: 'SOLID',
    color: { r, g, b },
    opacity: 1
  }];

  return style;
}

// Organização hierárquica com / (barras)
// Ex: "Primary/500" aparece como subgrupo no Figma

const colors = {
  // Primary Scale
  "Primary/50": "#[valor]",
  "Primary/100": "#[valor]",
  "Primary/200": "#[valor]",
  "Primary/300": "#[valor]",
  "Primary/400": "#[valor]",
  "Primary/500": "#[valor]",
  "Primary/600": "#[valor]",
  "Primary/700": "#[valor]",
  "Primary/800": "#[valor]",
  "Primary/900": "#[valor]",

  // Neutral Scale
  "Neutral/50": "#[valor]",
  "Neutral/100": "#[valor]",
  // ... continua até 900

  // Semantic
  "Semantic/Success": "#[valor]",
  "Semantic/Warning": "#[valor]",
  "Semantic/Error": "#[valor]",
  "Semantic/Info": "#[valor]",

  // Background & Surface
  "Surface/Background": "#[valor]",
  "Surface/Card": "#[valor]",
  "Surface/Muted": "#[valor]",

  // Border
  "Border/Default": "#[valor]",
  "Border/Input": "#[valor]",
};

for (const [name, hex] of Object.entries(colors)) {
  createColorStyle(name, hex);
}

// ----- TIPOGRAFIA -----

async function createTextStyles() {
  const fontFamily = "[Fonte Extraída]";

  // Carregar a fonte primeiro
  await figma.loadFontAsync({ family: fontFamily, style: "Regular" });
  await figma.loadFontAsync({ family: fontFamily, style: "Bold" });
  await figma.loadFontAsync({ family: fontFamily, style: "Medium" });
  await figma.loadFontAsync({ family: fontFamily, style: "SemiBold" });

  const textStyles = [
    { name: "Heading/H1", size: 48, weight: "Bold", lineHeight: 56 },
    { name: "Heading/H2", size: 36, weight: "Bold", lineHeight: 44 },
    { name: "Heading/H3", size: 30, weight: "SemiBold", lineHeight: 38 },
    { name: "Heading/H4", size: 24, weight: "SemiBold", lineHeight: 32 },
    { name: "Heading/H5", size: 20, weight: "Medium", lineHeight: 28 },
    { name: "Heading/H6", size: 16, weight: "Medium", lineHeight: 24 },
    { name: "Body/Large", size: 18, weight: "Regular", lineHeight: 28 },
    { name: "Body/Regular", size: 16, weight: "Regular", lineHeight: 24 },
    { name: "Body/Small", size: 14, weight: "Regular", lineHeight: 20 },
    { name: "Body/XSmall", size: 12, weight: "Regular", lineHeight: 16 },
    { name: "Label/Large", size: 14, weight: "Medium", lineHeight: 20 },
    { name: "Label/Regular", size: 12, weight: "Medium", lineHeight: 16 },
  ];

  for (const ts of textStyles) {
    const style = figma.createTextStyle();
    style.name = ts.name;
    style.fontName = { family: fontFamily, style: ts.weight };
    style.fontSize = ts.size;
    style.lineHeight = { value: ts.lineHeight, unit: "PIXELS" };
  }
}

// ----- SOMBRAS (EFFECT STYLES) -----

function createShadowStyle(name, shadows) {
  const style = figma.createEffectStyle();
  style.name = name;
  style.effects = shadows.map(s => ({
    type: "DROP_SHADOW",
    color: { r: 0, g: 0, b: 0, a: s.opacity },
    offset: { x: s.x, y: s.y },
    radius: s.blur,
    spread: s.spread || 0,
    visible: true,
    blendMode: "NORMAL"
  }));
  return style;
}

const shadows = {
  "Shadow/SM": [{ x: 0, y: 1, blur: 2, opacity: 0.05 }],
  "Shadow/MD": [
    { x: 0, y: 4, blur: 6, spread: -1, opacity: 0.1 },
    { x: 0, y: 2, blur: 4, spread: -2, opacity: 0.1 }
  ],
  "Shadow/LG": [
    { x: 0, y: 10, blur: 15, spread: -3, opacity: 0.1 },
    { x: 0, y: 4, blur: 6, spread: -4, opacity: 0.1 }
  ],
  "Shadow/XL": [
    { x: 0, y: 20, blur: 25, spread: -5, opacity: 0.1 },
    { x: 0, y: 8, blur: 10, spread: -6, opacity: 0.1 }
  ],
};

for (const [name, s] of Object.entries(shadows)) {
  createShadowStyle(name, s);
}

// ----- VARIÁVEIS (DESIGN TOKENS) -----

async function createVariables() {
  // Criar coleção de variáveis
  const collection = figma.variables.createVariableCollection("Design Tokens");

  // Renomear o modo padrão para "Light"
  collection.renameMode(collection.modes[0].modeId, "Light");

  // Adicionar modo Dark
  const darkModeId = collection.addMode("Dark");
  const lightModeId = collection.modes[0].modeId;

  // Função helper para criar variável de cor
  function createColorVariable(name, lightHex, darkHex) {
    const variable = figma.variables.createVariable(
      name,
      collection.id,
      "COLOR"
    );

    function hexToRgb(hex) {
      const r = parseInt(hex.slice(1, 3), 16) / 255;
      const g = parseInt(hex.slice(3, 5), 16) / 255;
      const b = parseInt(hex.slice(5, 7), 16) / 255;
      return { r, g, b, a: 1 };
    }

    variable.setValueForMode(lightModeId, hexToRgb(lightHex));
    variable.setValueForMode(darkModeId, hexToRgb(darkHex));
    return variable;
  }

  // Criar variáveis para cada token
  createColorVariable("background", "#[light]", "#[dark]");
  createColorVariable("foreground", "#[light]", "#[dark]");
  createColorVariable("primary", "#[light]", "#[dark]");
  createColorVariable("primary-foreground", "#[light]", "#[dark]");
  createColorVariable("secondary", "#[light]", "#[dark]");
  createColorVariable("secondary-foreground", "#[light]", "#[dark]");
  createColorVariable("muted", "#[light]", "#[dark]");
  createColorVariable("muted-foreground", "#[light]", "#[dark]");
  createColorVariable("accent", "#[light]", "#[dark]");
  createColorVariable("accent-foreground", "#[light]", "#[dark]");
  createColorVariable("destructive", "#[light]", "#[dark]");
  createColorVariable("destructive-foreground", "#[light]", "#[dark]");
  createColorVariable("border", "#[light]", "#[dark]");
  createColorVariable("input", "#[light]", "#[dark]");
  createColorVariable("ring", "#[light]", "#[dark]");
  createColorVariable("success", "#[light]", "#[dark]");
  createColorVariable("warning", "#[light]", "#[dark]");
  createColorVariable("info", "#[light]", "#[dark]");

  // Variável de número para border-radius
  const radiusVar = figma.variables.createVariable(
    "radius",
    collection.id,
    "FLOAT"
  );
  radiusVar.setValueForMode(lightModeId, 8); // valor em pixels
  radiusVar.setValueForMode(darkModeId, 8);
}

// ----- EXECUTAR -----

async function main() {
  console.log("🎨 Criando Design System no Figma...");

  // Cores
  console.log("📦 Criando Color Styles...");
  for (const [name, hex] of Object.entries(colors)) {
    createColorStyle(name, hex);
  }

  // Tipografia
  console.log("📝 Criando Text Styles...");
  await createTextStyles();

  // Sombras
  console.log("🌫️ Criando Effect Styles...");
  for (const [name, s] of Object.entries(shadows)) {
    createShadowStyle(name, s);
  }

  // Variáveis
  console.log("🔧 Criando Variables...");
  await createVariables();

  console.log("✅ Design System criado com sucesso!");
  figma.notify("Design System PRO exportado com sucesso! 🎉");
}

main();
```

### Instruções para o Usuário

Ao entregar o script, forneça estas instruções:

1. Abra o Figma Desktop
2. Crie um novo arquivo ou abra o arquivo de destino
3. Vá em **Plugins > Development > New Plugin**
4. Selecione "Figma design" e "Empty"
5. No arquivo `code.ts` do plugin, cole o script gerado
6. Execute o plugin
7. Todos os styles e variables serão criados automaticamente

### Observações

- A Figma Plugin API requer `loadFontAsync()` antes de definir propriedades de fonte
- Use notação com `/` para hierarquia (ex: `Primary/500` cria subgrupo `Primary` com item `500`)
- Variables suportam múltiplos modos (Light/Dark) nativamente
- O script é idempotente — rodar duas vezes cria duplicatas, então avise o usuário
