set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

default:
  @just --list

sync:
  uv sync --locked

browser:
  uv run playwright install chromium

build:
  uv run mkdocs build --strict
  find site -type f -name '*.pdf' ! -path 'site/pdf/algoritmi_distribuiti.pdf' -delete

serve:
  uv run mkdocs serve

fix-images:
  uv run python scripts/fix_image_assets.py --vault docs

fix-images-no-normalize:
  uv run python scripts/fix_image_assets.py --vault docs --no-normalize-existing-asset-refs

pdf:
  mkdir -p dist
  cp site/pdf/algoritmi_distribuiti.pdf dist/algoritmi_distribuiti.pdf
  ls -lh dist/algoritmi_distribuiti.pdf

docs: sync browser build pdf

all: docs
