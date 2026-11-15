# FireLert

**Challenge:** Harmonization of MODIS and VIIRS Hot Spots

**Team:** AstraXShip
**Local event:** Malaysia

- Shahrian (Leader)
- Danial
- Farah
- Jiayi
- Varshini

## Problem

Different satellite instruments detect burning at different resolutions and overpass times. A change in sensor can therefore look like a change in burning activity.

## Our application

FireLert lets users inspect historical burning activity, compare raw and Aqua-reference-equivalent observations, explore seasonal patterns, open weekly evidence, inspect selected daily cells and export analytical records.

The current country catalog covers Indonesia, Malaysia, Australia, Brazil, Egypt and the United States for 2003-2024. Indonesia/Malaysia history was generated from 78 verified NASA annual archives and 5,038,770 cleaned observations. Each country has 12 selected daily cells; national totals include all analyzed cells.

## Method and evidence

Terra, Aqua and Suomi-NPP VIIRS remain distinct. Training uses 2013-2017, model selection 2018-2019 and final testing 2020-2024. Validation selected B1 for Indonesia and M1 for Malaysia. Selected-model monthly test bias is -11.05% and -15.84% respectively. Errors and limitations are shown, not tuned away using test results.

Hotspots are detections, not unique fires. Calibration is an instrument reference scale, not ground truth. National performance does not establish local accuracy. The application is historical and descriptive, not an emergency alert or forecasting service. Weekly-rest-day analysis has not been recomputed for the changed country scope and is not an active feature.

## Attribution and access

FireLert is developed by AstraXShip using the project handed over to the team. License and data credits are in ATTRIBUTION.md; AI assistance is recorded in AI_DISCLOSURE.md. NASA FIRMS supplies the observations and Natural Earth supplies geographic context.

The updated FireLert build is local; a public FireLert deployment URL is not yet confirmed. Do not submit the earlier project's URL as this release.

NASA does not endorse this project.
