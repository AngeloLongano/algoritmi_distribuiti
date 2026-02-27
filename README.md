# Appunti di Algoritmi Distribuiti

Repository per pubblicazione note con MkDocs base, deploy su GitHub Pages e generazione PDF unica in CI.

## Workflow locale docs

```bash
just sync
just browser  # una tantum
just build
just fix-images
# opzionale: mantiene i riferimenti assets cosi' come sono
# just fix-images-no-normalize
# pipeline completa (sync + browser + build + pdf in dist/)
# just docs
```

## Struttura corrente

- `docs/index.md`
- `docs/00-ripasso/index.md`
- `docs/01-teoria-della-complessita/index.md`
- `docs/04-fondamenti-algoritmi-distribuiti/index.md`
- `docs/05-spanning-tree-construction/index.md`

## PDF unico

Il PDF completo viene generato nel workflow GitHub Actions:
[pages.yml](https://github.com/AngeloLongano/algoritmi_distribuiti/actions/workflows/pages.yml)
  - Look-up operations
