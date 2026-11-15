# FireLert — submission slide points

**Team:** AstraXShip
**Local event:** Malaysia

- Shahrian (Leader)
- Danial
- Farah
- Jiayi
- Varshini

## 1. Did burning change—or did the instrument?

**On-slide points**
- FireLert: historical burning activity with satellite differences made explicit.
- MODIS and VIIRS observe at different resolutions and overpass times.
- A sensor transition can look like a change in burning activity.
- AstraXShip · Malaysia.

**Visual:** Title and a readable raw-versus-harmonized comparison.

**Speaker cue:** “We help users question a historical change before interpreting it as a change in burning.”

## 2. Start with Indonesia and Malaysia

**On-slide points**
- Explore 2003–2024 historical records.
- Choose a country and date range; compare raw and Aqua-reference-equivalent activity.
- Indonesia/Malaysia preparation: 78 verified NASA annual archives and 5,038,770 cleaned observations.

**Visual:** Indonesia calendar with country, date and scale controls visible.

**Speaker cue:** “Hotspots are instrument detections, not unique fires or burned area.”

## 3. Calibrate, then test on unseen years

**On-slide points**
- Preserve distinct Terra, Aqua and Suomi-NPP VIIRS source identities.
- Fit: 2013–2017 → select: 2018–2019 → test: 2020–2024.
- Validation selected B1 for Indonesia and M1 for Malaysia.
- Aqua is a comparison reference, not ground truth.

**Visual:** Three-part timeline plus the held-out comparison table.

**Speaker cue:** “Model selection uses training and validation only; the test years expose remaining error rather than being used to retune the choice.”

## 4. Show the result and the remaining error

| Selected model | Monthly test bias against Aqua, 2020–2024 |
|---|---:|
| Indonesia · B1 | -11.05% |
| Malaysia · M1 | -15.84% |

**On-slide points**
- Negative bias means lower aggregate activity than the reference in this test comparison.
- Bias is not an “accuracy percentage.”
- National performance does not establish local-cell accuracy.

**Visual:** Legible metrics with country, model, test split and monthly aggregation identified.

**Speaker cue:** “The calibration still underestimates the reference. We show this limitation instead of claiming a perfect merged record.”

## 5. Follow a pattern back to evidence

**On-slide points**
- Open a calendar week for source counts, transformation and calibration bounds.
- Inspect seasonality and unusual historical periods.
- Twelve selected daily cells per country; national totals use all analyzed cells.
- Annual globe colors all processed regions with available values. Rotate to explore; Focus repositions the camera.

**Visual:** Evidence drawer and updated globe showing more than one processed region. Do not reuse the earlier selected-country-only screenshot.

**Speaker cue:** “Geographic context is not worldwide data coverage. Uncolored areas do not mean no fire; daily drill-down is limited to selected cells.”

## 6. Share an analytical record, not just an image

**On-slide points**
- Export the current selection as CSV.
- Export historical seasonal periods as an ICS calendar.
- Share supported exploration settings with a reproducible-view link.
- Historical analysis—not forecasts, ignition attribution or emergency alerts.

**Visual:** Export controls and a successfully reopened shared view.

**Speaker cue:** “A view link helps teammates inspect the same selection. It is not a permanent dataset snapshot. Historical calendar periods are not future warnings.”

## 7. Credits, access and limits

**On-slide points**
- AstraXShip: Shahrian (Leader), Danial, Farah, Jiayi, Varshini.
- Based on the MIT-licensed FIRETRACE project; observations from NASA FIRMS.
- Geographic context: Natural Earth via world-atlas. AI assistance disclosed.
- Missing observations are not zero activity; calibration intervals are not total uncertainty.
- NASA does not endorse this project.

**Visual:** Credits. Add demo/source links or QR codes only after verifying the actual FireLert release in a signed-out browser. No public release URL is confirmed in this handoff.

**Closing line:** “FireLert makes satellite differences inspectable, so historical patterns can be questioned and traced back to evidence.”

## Teammate handoff

- Assign deck design, narration, screen recording, factual review and portal submission within the team; no roles beyond leader are assumed here.
- Use `VIDEO_SCRIPT.md` for the recording sequence and captions. Preserve metric signs, model names, years and caveats.
- Verify scientific claims against `../reports/firelert-sea-v1/harmonization_eval.csv` and `../reports/firelert-sea-v1/selection_lock.json`; check credits against `../ATTRIBUTION.md` and `../AI_DISCLOSURE.md`.
- Do not claim global coverage, real-time alerts, forecasting, unique-fire counts or new weekly-rest-day results.
- Avoid a numeric country-coverage claim: the selectable catalog currently has six countries while globe metadata describes seven processed regions. Keep the demo centered on Indonesia/Malaysia and say “processed regions.”
- Confirm portal requirements, eligibility, member details, public links, media formats and permissions before submission.
