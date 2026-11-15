# FireLert scope and detail audit

## Root causes

The application had independently published calendar, globe and weekly-rhythm datasets. Changing the calendar catalog did not change the rhythm analysis or files copied into dist. The globe rendered all processed countries by design, so India remained visible behind Australia. India remains an active selectable country; only Nepal and Bangladesh were requested removed.

Indonesia and Malaysia were integrated from a one-year 2019 raw pilot, while other countries retain 2003–2024 calibrated products. Empty regional cells were an integration omission, not an absence of coordinates. No Southeast Asia multi-year calibration has been fitted.

## Changes

- Regional payloads now include twelve 0.5-degree cells ranked by 2019 activity, with independent Terra/Aqua/VIIRS daily series. This is exploratory selection, not training-selected validation.
- Regional monthly raw comparison charts and accessible tables use the selected date window.
- A separate raw VIIRS globe contains all occupied regional cells for 2019. National and globe totals reconcile. It cannot be mistaken for the calibrated layer.
- Globe coloring is limited to the selected country. Raw/calibrated layers use separate caches and remount when switching scale families.
- Removed-country cells are excluded from the calibrated globe.
- Weekly Rhythm navigation and embedded entry points are removed. The old hypothesis family cannot legitimately be subsetted and reported as a newly tested country scope. Original source/reports remain archived for provenance.
- Production build prunes data not reachable from the active catalog, including removed-country and rhythm payloads. Source artifacts remain preserved.
- Raw cell evidence no longer claims a national calibration or shows an empty calibrated headline.

## Remaining work

Indonesia/Malaysia still have 2019 only, UTC dates, and no fitted calibration, multi-year seasonality, anomalies or bootstrap uncertainty. Their new detail does not create missing years. Equal historical depth requires additional archives, civil-time preparation, scoped training/validation/test evaluation and new scientific outputs. Full reproduction's 10 GiB reserve remains above the approximately 8.6 GiB currently available on D:. No safety threshold was disabled.

## Validation

Frontend tests, TypeScript build, Python tests and real browser walkthrough exercised country switching, selected-cell evidence, raw globe grid table, calibrated globe, removed navigation and mobile overflow. Automated scope tests check raw globe/national/cell reconciliation and production exclusion of removed-country/rhythm files. No push or deployment was performed.
