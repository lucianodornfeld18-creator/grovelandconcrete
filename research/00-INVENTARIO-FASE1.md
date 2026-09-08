# Fase 1 — Inventário e decisões registradas (Groveland Concrete)

Data: 2026-09-07

## Ativos localizados

| Ativo | Caminho | Status |
|---|---|---|
| Ocoee Concrete (site) | `C:\Users\luana\SSD-Antigo-Lucia\Projetos\ocoeeconcrete` | Existente, git repo, ~40+ páginas (concrete/, pavers/, blog/, retaining-walls/, foundation-installation/, stucco/) |
| GCM Best Services Corp (site da empresa real) | `C:\Users\luana\SSD-Antigo-Lucia\gcm-site` | Existente, site "atelier" premium, schema LocalBusiness real |
| Auditoria técnica anterior do Ocoee | `C:\Users\luana\SSD-Antigo-Lucia\Downloads\AUDITORIA_OCOEECONCRETE_v1.md` | Documento de maio/2026 com concorrentes reais da região West Orange e 7 problemas técnicos |
| Windermere Concrete (site) | `C:\Users\luana\Documents\Codex\2026-08-20\co\work\windermereconcrete` | Existente, git repo, dist/ publicável, Cloudflare Worker de contato |
| Lakewood Ranch Concrete (site) | `C:\Users\luana\Documents\Codex\Projects\lakewoodranchconcretefl` | Existente, git repo, wrangler, muitas páginas de cidade/blog |
| Planilha EMD (Keyword Planner) | `C:\Users\luana\Documents\Codex\2026-09-03\pr\outputs\emd-concreto-fl\pesquisa_emd_concreto_florida_google_ads_2026-09-07.xlsx` | Confirmada, ainda não analisada linha a linha para o cluster de Groveland/South Lake |

## Identidade real confirmada (uso interno — NÃO citar no branding do Groveland)

**GCM Best Services Corp** — Orlando, FL 32819 · (407) 250-1948 · `gcmbestservicescorp.com`
Alegações no próprio site: licensed & insured (sem nº de licença publicado), 4.9★/59 reviews Google (autodeclarado, não verificado por nós), crews próprias, sem subcontratados.

Catálogo real confirmado (8 serviços): Luxury Pavers, Architectural Concrete, Custom Driveways, Pool Decks, Patios & Outdoor Living, Retaining Walls, Artificial Turf, Outdoor Lighting.

**Excluído do catálogo do Groveland** (aparecem no ocoeeconcrete.com legado mas não no site real da GCM): foundation-installation, stucco. Tratados como não confirmados — não usar.

## Catálogo de serviços do Groveland Concrete (subconjunto aprovado para o posicionamento rural/lotes maiores)

- Concrete driveways, incluindo long driveways
- Concrete slabs (workshop slabs, RV pads, boat pads)
- Concrete patios
- Concrete repair & resurfacing
- Sidewalks & walkways
- Paver driveways / paver patios
- Retaining walls (enquadrados como solução de declive/drenagem, não como estrutura de contenção pesada não confirmada)

Não anunciar: fundações, stucco, estruturas, muros de arrimo estruturais fora do escopo decorativo/paisagismo, pool shells, room additions — conforme regra do prompt mestre e ausência de confirmação no catálogo real da GCM.

## Decisões tomadas com o proprietário (2026-09-07)

1. **Catálogo Ocoee/GCM**: confirmado via arquivos no SSD antigo (não era necessário pedir cópia — já estavam no disco, só não no caminho citado no prompt).
2. **Sobreposição Groveland × Windermere Concrete**: os dois sites continuam existindo com conteúdo sobre Groveland, mas **sem duplicidade**. `grovelandconcrete.com` assume a intenção comercial primária/âncora de Groveland (ângulo: long driveways, RV/boat pads, workshop slabs, acesso rural, declive, drenagem). A página `windermereconcrete.com/groveland` deve permanecer no enquadramento genérico atual (cidade Tier-2, sem aprofundar nesses mesmos ângulos). **Pendente**: rodar comparação de similaridade textual entre as duas páginas antes da publicação do Groveland; ajustar `windermereconcrete/groveland` se houver sobreposição real de frases/estrutura.
3. **Dados de Keyword Planner/GSC/Bing/Twilio/Cloudflare**: sem acesso autenticado nesta sessão. Pesquisa de palavras-chave e concorrência será feita via web pública (WebSearch/WebFetch), rotulada como `COMPETITOR`, `AUTOCOMPLETE`, `AI-CITED` ou `EXPERT-GAP` — nunca como `VOLUME` ou `GSC` sem uma exportação real. Contas/números de Twilio, Cloudflare, Search Console e Bing Webmaster Tools ficam para depois do site pronto, com placeholders no meio tempo.

## Sobreposição adicional a checar

`windermereconcrete.com` TIER1 já inclui **Clermont** e **Montverde**, que também estão nas "seeds a validar" do prompt do Groveland (raio de 30 milhas). Antes de criar páginas cidade×serviço para Clermont ou Montverde no Groveland, validar no registro global quem fica com a intenção primária dessas duas cidades — mesma lógica aplicada a Groveland.

## Pendências reais para o proprietário

- Confirmar se okay usar os arquivos do Ocoee/GCM no SSD antigo como fonte de verdade do catálogo (ou se há uma versão mais recente em outro lugar).
- Twilio number, alias de e-mail Cloudflare e e-mail de destino final para `grovelandconcrete.com` — pendente, usar placeholders até então.
- Identidade legal/licença a divulgar no formulário de lead (se exigido por lei) — ainda não solicitado ao proprietário; será levantado na fase de compliance do formulário.
