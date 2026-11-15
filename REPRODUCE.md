# Reproduce

Interface: `npm ci --prefix web`, `npm --prefix web test`, `npm run build`.
Python: install `requirements.txt`, run `python -m pytest tests -q`.

Regional history: `python scripts/prepare_sea_history.py` downloads archives and generates outputs in `work/sea-history-v1/`. Promotion: `python scripts/promote_sea_history.py`, then `npm run build`.
