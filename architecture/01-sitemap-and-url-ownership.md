# Mapa de arquitetura e propriedade de URL — Groveland Concrete

Baseado nas 100 perguntas (`research/05-100-questions.md`) e no catálogo confirmado. Objetivo: ~30 URLs reais, não 100 posts automáticos, e nenhuma página cidade×serviço sem justificativa de demanda/diferença local.

## Cidades — decisão de propriedade

| Cidade/área | Decisão | Justificativa |
|---|---|---|
| **Groveland** | Página própria (âncora) | Cidade-sede do hub. |
| **Mascotte** | Página própria | Concorrência quase nula encontrada (arquivo 03); perfil rural compatível. |
| **Minneola** | Página própria | Boom de subdivisão de alta densidade (Hills of Minneola) = demanda real de driveways/calçadas novas. |
| **Howey-in-the-Hills** | Página própria | Vilarejo lakefront rural + projeto de 560 casas 55+ anunciado; terreno de "rolling hills" relevante para retaining walls/drenagem. |
| **Rural / unincorporated Lake County** | Página própria (não é uma "cidade", é um hub temático) | Zoneamento agrícola/equestre (lotes 5+ acres) é o público-alvo ideal do catálogo completo (long driveway, RV/boat pad, workshop slab). |
| **Leesburg** | Sem página dedicada agora | Extremo do raio de 30 milhas, mais urbanizada, risco de overlap ao norte não confirmado. Mencionada apenas no hub de área de serviço. |
| **Center Hill** | Sem página dedicada agora | Fora do condado-núcleo (Sumter), jurisdição de permit pouco clara, população pequena. Mencionada apenas no hub de área de serviço + no diretório de permits (link direto para a página oficial de permit de driveway de Sumter County, que É um achado real e útil). |
| **Clermont** | **Página própria — RESOLVIDO 2026-09-07** | Dono confirmou: hubs irmãos podem cobrir a mesma cidade desde que não haja duplicidade/similaridade textual. Página do Groveland cobre especificamente a borda rural/lago (chain of lakes, boat pads, lotes maiores), não o núcleo suburbano denso — ângulo deliberadamente diferente do windermereconcrete.com. Checagem de similaridade (8-gram/Jaccard) contra a página real `/clermont/` do windermereconcrete: 0 n-gramas compartilhados. |
| **Montverde** | **Página própria — RESOLVIDO 2026-09-07** | Mesma decisão do Clermont. Ângulo do Groveland: lotes de estate da Bella Collina (1,65–2,77 acres), terreno inclinado, retaining walls/drenagem — não seleção de acabamento. Checagem de similaridade contra `/montverde/` do windermereconcrete: 0 n-gramas compartilhados. |

**Nota adicional de overlap (Minneola):** o `_data.py` do windermereconcrete.com também lista Minneola em TIER2 (página de cidade única, sem city×service completo) — o mesmo nível que Groveland tinha antes desta decisão. Como o dono já autorizou o mesmo modelo aplicado a Groveland ("os dois ficam, sem duplicidade"), a página `/minneola/` do Groveland Concrete deve seguir a mesma regra: ângulo próprio (boom de subdivisão + driveways/calçadas em construção nova), e checagem de similaridade textual contra `windermereconcrete.com/minneola` antes de publicar.

## Serviços — páginas (8)

1. `/concrete-driveways/` — inclui o ângulo de long driveway como diferencial central
2. `/rv-and-boat-pads/` — RV pads + boat pads juntos (mesma ferramenta/calculadora, specs técnicas relacionadas, mas cada um com sua seção e FAQ própria)
3. `/workshop-slabs/` — slabs para oficina/metal building/barn
4. `/concrete-patios/`
5. `/concrete-repair-resurfacing/`
6. `/sidewalks-walkways/`
7. `/paver-driveways/` — split from a combined paver page on 2026-09-07 to target "paver driveway" and "paver patio" as separate primary keywords
8. `/paver-patios/`
8. `/retaining-walls/` — enquadrado como solução de declive/drenagem

## Ferramentas / ativo original (gate de citabilidade)

1. `/tools/driveway-cost-calculator/` — Long Driveway Cost & Volume Planner (ativo-bandeira)
2. `/tools/rv-boat-pad-calculator/`
3. `/tools/workshop-slab-guide/` — guia de decisão de espessura
4. `/tools/site-access-checklist/` — checklist de acesso de caminhão-betoneira em lote rural
5. `/tools/drainage-slope-planner/`
6. `/permits/` — diretório de permits de South Lake (Groveland Building Division/eTRAKiT, Lake County Building Services, Town of Montverde/Citizenserve, Sumter County driveway permitting)

## Guias/artigos (`/guides/`)

- long-driveway-cost-florida
- concrete-truck-access-rural-driveway
- concrete-vs-gravel-driveway-florida
- rv-pad-vs-driveway
- boat-pad-vs-rv-pad
- best-base-sandy-soil-florida
- why-concrete-driveway-cracking
- maintain-concrete-driveway-florida-climate
- fixing-flooding-sloped-driveway
- repair-vs-replace-driveway
- resurfacing-vs-new-pour-cost
- is-resurfacing-worth-it-before-selling

## Comparações (`/compare/`)

- rebar-vs-wire-mesh
- paver-vs-concrete-driveway
- stamped-vs-plain-patio

## FAQ

Agrupadas contextualmente dentro das páginas de serviço/ferramenta (espessura, PSI, cura, permits, drenagem) — sem página FAQ solta genérica, conforme regra do prompt mestre de não criar URL sem necessidade.

## Institucional/legal

`/about/` (Editorial Standards verdadeiro), `/process/`, `/contact/`, `/privacy-policy/`, `/terms/`, `/accessibility/`, `/thank-you/` (noindex), `404`.

## Total estimado

≈ 5 cidades + 8 serviços + 6 ferramentas/permits + 12 guias + 3 comparações + 8 institucionais/legais ≈ **42 URLs indexáveis + utilitárias**, todas rastreáveis às 100 perguntas de origem. Nenhuma URL nova para Clermont/Montverde até resolução do overlap.
