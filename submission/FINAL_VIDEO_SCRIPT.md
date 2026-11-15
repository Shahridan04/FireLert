# FireLert - separate 3-5-minute final-video draft

**Team:** AstraXShip
**Local event:** Malaysia

- Shahrian (Leader)
- Danial
- Farah
- Jiayi
- Varshini

**Purpose:** Separate longer draft. AstraXShip Project.pdf page 2 lists a 3-5-minute final video in addition to the 30-second demo. Use VIDEO_SCRIPT.md for the short demo. Rehearse this longer version to meet the organizer-confirmed duration; its timeline alone does not guarantee a three-minute recording.

## Prepare the recording

1. From the repository root run `npm run build`, then `python -m http.server 5180 --bind 127.0.0.1 --directory dist`. Open `http://127.0.0.1:5180`. This local URL is not a public submission link.
2. Begin with Indonesia, national scope and 2003–2024. Close old evidence drawers, use a readable desktop viewport and hide notifications/private information.
3. Rehearse the scale controls, a populated week, held-out metrics, a selected daily cell, globe, CSV and sharing. Choose the week from the actual build; do not invent a date or value.
4. Preload the globe and rotate to show multiple processed regions. Confirm Focus changes the camera without hiding other countries. Reset to the opening state before capture.
5. Prepare Indonesia B1 and Malaysia M1 monthly test rows. Do not present validation results as test results.
6. Test a share link in another tab and open the exported CSV. Assign narrator, recorder and reviewer within the team.

## Timed narration and screen actions

| Time | Screen / action | Spoken narration |
|---|---|---|
| 0:00–0:20 | Slide 1, then FireLert opening view | “We are AstraXShip from the Malaysia local event. FireLert asks: did burning activity change, or did the satellite instrument change? MODIS and VIIRS observe differently, so a sensor transition can look like a change in burning.” |
| 0:20–0:43 | Indonesia; show full date range and switch raw/harmonized scale | “We focus on Indonesia and Malaysia, with historical records from 2003 to 2024. Their preparation used 78 verified NASA annual archives and over five million cleaned observations. Compare the raw baseline with an Aqua-reference-equivalent record. These are hotspot detections, not unique fires.” |
| 0:43–1:05 | Open a populated calendar week; pause on source counts and provenance | “A pattern should lead back to evidence. Open a week to inspect separate source counts, how values were observed or transformed, and calibration bounds. Missing observations are not silently treated as zero, and those bounds do not represent every source of uncertainty.” |
| 1:05–1:35 | Held-out comparison: Indonesia B1 and Malaysia M1, or a clearly labeled edited split-screen | “We fit on 2013 to 2017, select models on 2018 and 2019, and reserve 2020 to 2024 for testing. Validation selected B1 for Indonesia and M1 for Malaysia. Their monthly test biases against Aqua are minus 11.05 percent and minus 15.84 percent. Error remains, and Aqua is a reference—not ground truth.” |
| 1:35–1:53 | Return to Explore; show seasonality and a selected daily cell | “Seasonal summaries and unusual historical periods help users investigate the record. Daily detail covers twelve selected cells per country; national totals include all analyzed cells. Good national performance does not prove that every local estimate is accurate.” |
| 1:53–2:16 | Reset national scope; open 3D Earth, rotate, select an annual cell, then use Focus | “The annual globe shows all processed regions with available values, rather than hiding every country except the selected one. Rotate Earth to explore; Focus repositions the camera. This is not worldwide coverage. Uncolored areas do not establish an absence of burning.” |
| 2:16–2:37 | Export CSV; show seasonal ICS option; copy and reopen a supported view link | “Export the current analytical selection as CSV, or historical seasonal periods as a calendar file. A shared view lets a teammate reopen supported exploration settings and inspect the same selection. It is a reproducible view, not a permanent snapshot of the data.” |
| 2:37–3:00 | Closing slide: team, credits and verified links only | “FireLert supports historical analysis, not forecasts or emergency alerts. It builds on the MIT-licensed FIRETRACE project, NASA FIRMS observations, and Natural Earth geography, with AI assistance disclosed. NASA does not endorse this project. Our aim is to make satellite differences visible, and historical patterns traceable to evidence.” |

## Editing notes

- Rehearse aloud and adjust pauses to the actual limit. Allow loading time and readable metrics instead of rushing the narration.
- Record separate segments if needed. Label country changes so Malaysia's results cannot be mistaken for Indonesia's.
- Use captions, high-contrast text and a visible pointer; keep music below speech.
- For a shorter limit, cut the cell-detail segment and shorten exports first. Preserve the problem, method split, results, scope limits and credits.
- If WebGL is unavailable, show the annual grid table and explain that fallback; do not narrate unseen 3D interaction.
- Call ICS a historical seasonal calendar, not an alert subscription. Do not show archived weekly-rest-day analysis as an active feature.
- Avoid a numeric country count: selectable catalog and globe metadata currently differ. Say “processed regions” and focus on Indonesia/Malaysia.

## Final submission checklist

- [ ] Confirm portal duration, resolution, format, file-size limit, deadline and timezone.
- [ ] All members approve names, scientific wording, inherited-code attribution and AI disclosure.
- [ ] Capture the updated all-processed-region globe, not the earlier selected-country-only view.
- [ ] Check captions: Aqua, VIIRS, B1, M1, -11.05%, -15.84%, and all year ranges.
- [ ] Watch the final rendered video end to end with sound and captions; check for private information.
- [ ] Verify actual FireLert demo/source links in a signed-out browser before adding URLs or QR codes. No public FireLert release URL is confirmed here; do not reuse an earlier project's URL as this release.
- [ ] Cross-check `SLIDES.md`; retain NASA non-endorsement and historical-only limits.
- [ ] Submit through the confirmed portal and retain its receipt. These materials do not mean anything has been submitted.
