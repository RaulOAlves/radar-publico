# Radar público

Histórico público do Radar de IA, GeoIA e Setores, publicado como arquivos estáticos.

## Atualizar

```sh
python3 -m unittest discover -s scripts/tests -v
python3 scripts/build_radar.py source/radar-ia-geo.md --output public
```

## Endpoints

- `v1/radar/latest.json`: edição mais recente.
- `v1/radar/feed.xml`: RSS com até 50 itens.
- `v1/radar/radar-canonico.json`: todos os itens canônicos.
- `v1/radar/editions/AAAA-MM-DD.json`: arquivo diário.
- `v1/radar/manifest.json`: versão, contagens e hashes.
- `v1/radar/quarantine.json`: itens que exigem revisão manual.

O Markdown de origem fica em `source/`. O gerador padrão usa somente biblioteca padrão do Python.
