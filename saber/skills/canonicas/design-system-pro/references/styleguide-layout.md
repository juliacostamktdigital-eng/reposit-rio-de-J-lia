# Template do Layout do Styleguide

## Layout com Sidebar (`/app/styleguide/layout.tsx`)

```tsx
"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"
import { navigation } from "./navigation"

export default function StyleguideLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const pathname = usePathname()

  return (
    <div className="flex min-h-screen">
      {/* Sidebar Fixa */}
      <aside className="w-64 border-r bg-card p-6 flex flex-col gap-6 fixed top-0 left-0 h-screen overflow-y-auto">
        <div>
          <Link href="/styleguide" className="text-xl font-bold">
            Design System
          </Link>
        </div>

        <nav className="flex flex-col gap-6">
          {navigation.map((section) => (
            <div key={section.title}>
              <h3 className="text-sm font-semibold text-muted-foreground mb-2 uppercase tracking-wider">
                {section.title}
              </h3>
              <ul className="flex flex-col gap-1">
                {section.items.map((item) => (
                  <li key={item.href}>
                    <Link
                      href={item.href}
                      className={cn(
                        "block px-3 py-2 rounded-md text-sm transition-colors",
                        pathname === item.href
                          ? "bg-primary text-primary-foreground"
                          : "hover:bg-muted"
                      )}
                    >
                      {item.name}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </nav>
      </aside>

      {/* Conteúdo Principal */}
      <main className="flex-1 ml-64 overflow-auto">
        {children}
      </main>
    </div>
  )
}
```

## Página do Styleguide (`/app/styleguide/page.tsx`)

A página principal deve exibir todos os design tokens. Organize em seções:

### Estrutura Recomendada

```tsx
export default function StyleguidePage() {
  return (
    <div className="p-8 space-y-12">
      {/* Header */}
      <div>
        <h1 className="text-4xl font-bold">Design Tokens</h1>
        <p className="text-muted-foreground mt-2">
          Fundação visual do design system
        </p>
      </div>

      {/* Paleta de Cores */}
      <section>
        <h2 className="text-2xl font-semibold mb-4">Cores</h2>

        {/* Primary Scale */}
        <h3 className="text-lg font-medium mb-2">Primary</h3>
        <div className="grid grid-cols-10 gap-2">
          {/* Swatch para cada shade 50-900 */}
          <ColorSwatch name="50" variable="--primary-50" />
          {/* ... */}
        </div>

        {/* Neutral Scale */}
        {/* Semantic Colors */}
        {/* Surface Colors */}
      </section>

      {/* Tipografia */}
      <section>
        <h2 className="text-2xl font-semibold mb-4">Tipografia</h2>
        {/* Exemplos de cada nível tipográfico */}
      </section>

      {/* Border Radius */}
      <section>
        <h2 className="text-2xl font-semibold mb-4">Border Radius</h2>
        {/* Exemplos visuais */}
      </section>

      {/* Sombras */}
      <section>
        <h2 className="text-2xl font-semibold mb-4">Sombras</h2>
        {/* Cards com diferentes sombras */}
      </section>

      {/* Componentes Demo */}
      <section>
        <h2 className="text-2xl font-semibold mb-4">Componentes</h2>
        {/* Button, Card, Badge, Alert, RadioGroup */}
      </section>

      {/* Dark Mode Toggle */}
      <section>
        <h2 className="text-2xl font-semibold mb-4">Dark Mode</h2>
        {/* Botão de toggle + preview */}
      </section>
    </div>
  )
}
```

### Componente ColorSwatch

```tsx
function ColorSwatch({
  name,
  color,
  textColor = "white"
}: {
  name: string
  color: string
  textColor?: string
}) {
  return (
    <div
      className="rounded-lg p-3 aspect-square flex flex-col justify-end"
      style={{ backgroundColor: color }}
    >
      <span className="text-xs font-mono" style={{ color: textColor }}>
        {name}
      </span>
    </div>
  )
}
```
