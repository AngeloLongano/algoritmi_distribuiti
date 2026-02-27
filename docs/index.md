# Appunti di Algoritmi Distribuiti

Questa è la versione pubblicata con MkDocs, con navigazione ad albero e build automatica su GitHub Pages.

## Capitoli pubblicati

- [0. Ripasso sugli algoritmi](00-ripasso/index.md)
- [1. Teoria della complessità](01-teoria-della-complessita/index.md)
- [4. Fondamenti di algoritmi distribuiti](04-fondamenti-algoritmi-distribuiti/index.md)
- [5. Spanning Tree Construction](05-spanning-tree-construction/index.md)

## PDF unico

Il PDF completo viene generato in CI a ogni push su `main` ed è scaricabile dagli artifact del workflow:
[pages.yml](https://github.com/AngeloLongano/algoritmi_distribuiti/actions/workflows/pages.yml)

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
