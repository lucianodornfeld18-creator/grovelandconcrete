# Groveland Concrete — Guia rápido de marca

> **SUPERSEDIDO em 2026-09-07:** o proprietário forneceu uma logo final própria (monograma "GC" em concreto 3D com detalhe laranja + wordmark "GROVELAND CONCRETE"). Essa é a logo em produção agora — arquivos em `png/logo-full.png` (lockup completo), `png/icon-full.png` (ícone recortado, usado no header) e `png/favicon-*.png`/`png/social-badge-512.png`. O fundo "transparente" da imagem original gerada por IA era, na verdade, um xadrez cinza desenhado nos pixels (não transparência real) — recortei o fundo de verdade com um modelo de remoção de background antes de gerar os assets. A direção Township Grid abaixo fica só como histórico.
>
> **Assets derivados (2026-09-08):** `png/logo-horizontal-light.png` / `png/logo-horizontal-dark.png` (lockup horizontal: ícone GC + wordmark, gerado a partir do lockup original — versão *dark* tem o wordmark recolorido para `#EFE7DA` para uso sobre fundo escuro), `png/logo-full-dark.png` (lockup empilhado com wordmark claro, usado no footer), mais renders reduzidos `-h160` (header) e `-h400` (footer) e cópias WebP em `webp/`. O header do site usa o lockup horizontal como `<img alt="Groveland Concrete">` dentro de `<picture>` com troca light/dark por `prefers-color-scheme` — isso substitui a regra antiga de "wordmark como texto HTML"; o `alt` e o `aria-label` do link cobrem acessibilidade/SEO.

**Direção escolhida (histórico, substituída):** 04 · Township Grid (grid de agrimensura rural, com o "lote" marcado). Escolhida em 2026-09-07 — **o proprietário sinalizou que pode querer revisar/ajustar depois**, então trate isto como a base de trabalho atual, não como definitivo. Trocar ícone/paleta depois é barato: todo o site vai consumir essas cores via variáveis CSS (tokens), então um ajuste de marca não implica reescrever páginas.

## Nome público (regra fixa)

**Groveland Concrete** — exatamente assim, sempre. Sem "FL", sem número, sem sufixo (Company/Contractors/Services/Pros/Group/LLC/24-7/#1). Usar em: header, footer, `<title>`, `WebSite.name`, `og:site_name`, assinatura de e-mail, sender display name.

## Paleta

| Token | HEX | Uso |
|---|---|---|
| `--clay` | `#6E3B25` | Cor primária da marca (ícone sobre fundo claro, texto de destaque, botões primários) |
| `--parchment` | `#E3E1D8` | Fundo neutro claro / superfície |
| `--ink` | `#201F1B` | Texto principal |
| `--ochre` | `#C77F35` | Ícone/acento sobre fundo escuro, hover states |
| `--ink-dark-bg` | `#EFE7DA` | Texto sobre fundo escuro |

Contraste clay `#6E3B25` sobre parchment `#E3E1D8` ≈ 6.3:1 — passa AA para texto normal e grande. Verificar contraste final com as cores exatas de botão/texto quando o CSS de produção for escrito.

## Tipografia

- **Display/wordmark:** Fjalla One (Google Fonts, licença SIL Open Font License — uso livre, incl. comercial)
- **Corpo de texto:** IBM Plex Sans (Google Fonts, licença OFL)
- **Dados/specs/tabelas técnicas:** IBM Plex Mono (Google Fonts, licença OFL)

## Ícone

Grid de agrimensura (linhas de seção + um "lote" marcado no cruzamento) — referência direta ao sistema usado para demarcar lotes rurais de 5+ acres no South Lake County, o público-alvo do site.

## Arquivos entregues

```
brand/
├── icon-clay.svg              — ícone limpo, cor clay, fundo transparente (uso sobre claro)
├── icon-ochre.svg             — ícone limpo, cor ochre, fundo transparente (uso sobre escuro)
├── favicon.svg                — mesmo ícone, testado para legibilidade 16–48px
├── social-badge.svg           — ícone sobre fundo clay arredondado (foto de perfil social)
├── logo-horizontal-light.svg  — ícone + "GROVELAND CONCRETE", texto escuro, fundo transparente
├── logo-horizontal-dark.svg   — ícone + "GROVELAND CONCRETE", texto claro, fundo transparente
└── png/
    ├── icon-clay-512.png, icon-clay-192.png   (RGBA, fundo transparente confirmado)
    ├── icon-ochre-512.png                      (RGBA, fundo transparente confirmado)
    ├── favicon-48.png, favicon-32.png, favicon-16.png
    ├── social-badge-512.png                    (fundo clay sólido, não transparente — é o objetivo)
    ├── logo-horizontal-light-1280.png          (RGBA, fundo transparente confirmado)
    └── logo-horizontal-dark-1280.png           (RGBA, fundo transparente confirmado)
```

Todos os PNGs foram renderizados a partir dos SVGs originais via navegador headless (Playwright), não desenhados à mão em pixel — o SVG é a fonte de verdade; regenerar o PNG a qualquer momento a partir dele.

## Regras de uso

- **Espaço de proteção mínimo:** altura de um "braço" do grid (a unidade entre duas linhas) ao redor do ícone, em qualquer aplicação.
- **Tamanho mínimo:** 24px para o ícone isolado (favicon/nav); abaixo disso, simplificar para as duas linhas + o quadrado marcado, sem tentar manter as quatro linhas completas.
- **Não fazer:** não colorir o ícone em dourado/preto (colide com a identidade visual já confirmada da GCM Best Services Corp / windermereconcrete.com); não esticar/distorcer a proporção do grid; não adicionar sombra, bisel ou gradiente — o mark é plano por design.
- **Wordmark real, não imagem, no header do site:** no site em produção, "Groveland Concrete" deve ser texto HTML de verdade estilizado com Fjalla One (via Google Fonts), não uma imagem com o texto embutido — melhor para acessibilidade e SEO. Os arquivos `logo-horizontal-*.svg/png` acima servem para contextos que exigem uma imagem fechada (assinatura de e-mail, compartilhamento social, apresentações) — não para o header do site.

## Pendências caso o proprietário volte a mexer na escolha

Como o próprio dono avisou que pode revisitar essa direção: qualquer ajuste (trocar paleta, trocar ícone, manter só a tipografia) não exige refazer as páginas — os tokens de cor abaixo são a única coisa que muda. Registrar a versão final no `network-registry.json` quando a decisão for definitiva.
