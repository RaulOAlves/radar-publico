# Radar público

Histórico público do Radar de IA, GeoIA e Setores, publicado como arquivos estáticos.

## Atualizar

```sh
python3 -m unittest discover -s scripts/tests -v
python3 scripts/build_radar.py source/radar-ia-geo.md --output public --fail-on-quarantine
```

## Endpoints

- `v1/radar/latest.json`: edição mais recente.
- `v1/radar/kindle.json`: as 50 matérias mais recentes, no contrato otimizado para o Kindle.
- `v1/radar/feed.xml`: RSS com até 50 itens.
- `v1/radar/radar-canonico.json`: todos os itens canônicos.
- `v1/radar/editions/AAAA-MM-DD.json`: arquivo diário.
- `v1/radar/manifest.json`: versão, contagens e hashes.
- `v1/radar/quarantine.json`: itens que exigem revisão manual.
- `api/radar/article?id=radar-…`: extração sob demanda do original de um GUID canônico; não persiste nem publica o texto integral.

O Markdown de origem fica em `source/`. O gerador padrão usa somente biblioteca padrão do Python.
Com `--fail-on-quarantine`, uma entrada inválida preserva a última publicação válida.

Novos itens incluem `summary`, um resumo factual de um ou dois parágrafos. Registros históricos
sem esse campo usam `why_it_matters` como compatibilidade temporária.

Cada edição e `latest.json` também publicam `edition_id`, `generated_at`, `metrics`
(`signals`, `sources`, `high_confidence`) e `methodology`. Esses campos permitem que
leitores como o painel Kindle exibam o pulso da edição sem recalcular ou coletar dados.

## Leitura original sob demanda

A Function recebe somente o GUID de uma matéria pública, resolve a URL no canônico e extrai o
corpo com Readability. URLs arbitrárias, HTTP, redirects, documentos acima de 1 MB e artigos
extraídos acima de 350 KB são rejeitados. A resposta usa `Cache-Control: no-store`; o cache de
leitura pertence ao Kindle, não ao diretório público.
