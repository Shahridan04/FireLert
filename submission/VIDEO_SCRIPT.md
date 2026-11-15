# FireLert - 30-second submission demo

**Team:** AstraXShip - **Local event:** Malaysia
**Members:** Shahrian (Leader), Danial, Farah, Jiayi, Varshini
**Maximum duration:** 30 seconds, including titles, transitions and credits.

## Requirements checked

- `D:\FireLert\Challenge Detail\AstraXShip Project.pdf`, page 3: maximum 30-second demo; suggested structure is team 2s, challenge 3s, project 5s, how it works 10s, vision/impact 10s. Cover problem, data, insight, solution, impact and demo.
- `D:\FireLert\Challenge Detail\NASA Space Apps Challenge.pdf`, pages 4-5: harmonize MODIS/VIIRS hotspots into a web-based burning activity calendar, with region/date selection, historical comparisons and downloadable analytics.
- Important: the project PDF page 2 separately lists **two compulsory videos: a 30s project demo and a 3-5-minute final video**. Page 3 also describes a demo video OR a maximum-seven-slide deck. Confirm the organizer's exact submission fields; do not assume the short demo replaces the final video. The longer draft is preserved in `D:\FireLert\submission\FINAL_VIDEO_SCRIPT.md`.

## Timed storyboard - record this version

| Time | Purpose / screen action | Spoken narration | On-screen text |
|---|---|---|---|
| 0:00-0:02 | Team: title over the app, no separate intro animation | "We're AstraXShip." | FireLert - AstraXShip - Malaysia |
| 0:02-0:05 | Challenge: show raw-versus-harmonized comparison | "Different sensors can distort fire trends." | Harmonization of MODIS and VIIRS Hot Spots |
| 0:05-0:10 | Project: show Indonesia calendar and country/date controls | "FireLert compares historical burning across Indonesia and Malaysia." | Historical burning calendar - 2003-2024 |
| 0:10-0:20 | Demo/data/insight: switch raw/harmonized view, then open a populated week's evidence | "Using NASA FIRMS, we calibrate MODIS and VIIRS observations to an Aqua reference. Explore dates, compare patterns, and inspect evidence." | NASA FIRMS - MODIS + VIIRS - Aqua-reference scale. Then: Sensor differences matter; calibration still has error. |
| 0:20-0:30 | Impact/vision: briefly show seasonality and CSV export; finish on app with credits overlay | "Our goal: help scientists and land managers interpret seasonal activity through transparent historical comparisons, not forecasts or emergency alerts." | Historical analysis, not alerts. Final overlay: Based on FIRETRACE (MIT) - NASA FIRMS - Natural Earth - AI assistance disclosed - NASA does not endorse this project. |

## Full voiceover - copy for narrator

> We're AstraXShip. Different sensors can distort fire trends. FireLert compares historical burning across Indonesia and Malaysia. Using NASA FIRMS, we calibrate MODIS and VIIRS observations to an Aqua reference. Explore dates, compare patterns, and inspect evidence. Our goal: help scientists and land managers interpret seasonal activity through transparent historical comparisons, not forecasts or emergency alerts.

## Recording instructions

1. Rehearse the voiceover with a stopwatch. Target a 29-30-second export; never exceed 30 seconds. The word-count estimate is not a substitute for timing the actual delivery.
2. Capture the current working build at readable resolution. Preload data, choose a genuinely populated week and hide personal information. Record short clips and edit them together; do not spend submission time waiting for loads.
3. Use large captions and one focused action per shot. Keep the challenge label short-lived and credits visible over the closing app footage, rather than adding time after 0:30. Do not squeeze in all seven slides or the full evaluation table.
4. Keep the focus on the calendar, harmonization and evidence. The globe is optional background footage, not a required extra shot. If used, show the current all-processed-region version and never imply worldwide coverage.
5. Do not call hotspots unique fires, Aqua ground truth, calibration error-free, or historical periods predictions. Put detailed evaluation metrics and limitations in the written project/final video rather than rushing them into this pitch.
6. If recording locally, from `D:\FireLert` run `npm run build`, then `python -m http.server 5180 --bind 127.0.0.1 --directory dist`. Open `http://127.0.0.1:5180`. Do not submit localhost as the public project link.

## Submission checklist

- [ ] Final exported duration is at most 30 seconds, including every frame and credit.
- [ ] Audio and captions are understandable at normal speed; watch the rendered file end to end.
- [ ] Title identifies FireLert and AstraXShip; source attribution, AI disclosure and NASA non-endorsement remain legible.
- [ ] Demo uses actual working interactions; no unsupported alerts, forecasts or global-coverage claims.
- [ ] Test the demo link signed out: page 1 of the project PDF specifies ONE public demo link. Confirm local upload format, permissions and final-video requirements with the organizer.
- [ ] The public final-project link is separate from the demo field; verify the actual live release before submission. Source: https://github.com/Shahridan04/FireLert.
- [ ] Team approves the final video and retains the submission receipt. These documents do not constitute a submission.
