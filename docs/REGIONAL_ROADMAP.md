# Regional history integrated

Indonesia and Malaysia now appear in the existing 2003?2024 calendar, harmonized/raw comparisons, seasonal summaries, anomalies, twelve selected-cell records, CSV export and calibrated globe. 

78 annual archives were verified and 5,038,770 observations retained during preparation. All 1,462,692 payload comparisons against processed data passed. National performance does not imply cell accuracy; reported bootstrap bands omit total observation uncertainty.

Reproduction: `python scripts/prepare_sea_history.py` produces isolated outputs. Validate with `python scripts/verify_payloads.py --public-dir work/sea-history-v1/public/data --processed-dir work/sea-history-v1/processed --evaluation work/sea-history-v1/reports/harmonization_eval.csv`. Promotion: `python scripts/promote_sea_history.py`, then `npm run build`. The old raw-pilot integration now refuses to overwrite promoted history. Backup: `work/pre-history-public`.

Weekly-rest-day inference remains unavailable for the changed scope. No push or deployment has been performed.
