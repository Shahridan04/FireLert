# FireLert judge Q&A

**Team:** AstraXShip
**Local event:** Malaysia

- Shahrian (Leader)
- Danial
- Farah
- Jiayi
- Varshini

## Who is presenting?
AstraXShip: Shahrian (Leader), Danial, Farah, Jiayi and Varshini. Participation is in the Malaysia local event. Other responsibilities have not been assigned in these documents.

## Is this entirely new code?
FireLert builds on the existing project handed over to AstraXShip. Applicable software licensing, NASA data credits and AI assistance are documented.

## What does harmonization mean?
VIIRS counts are expressed on an Aqua-reference scale. This does not recover the true number of fires or eliminate all sensor effects.

## How was the regional model evaluated?
Training: 2013-2017. Selection: 2018-2019. Test: 2020-2024. Regional provenance, locked choices and metrics are in reports/firelert-sea-v1/.

## What errors remain?
Selected-model monthly test bias is -11.05% in Indonesia and -15.84% in Malaysia. Monthly test correlation is approximately 0.969 and 0.919. High correlation does not guarantee accurate peak timing: Malaysia's selected model has mean peak-week error of 4.8 weeks. National accuracy does not prove cell accuracy.

## What do uncertainty intervals cover?
Training-year bootstrap variability in calibration, not total cloud, sampling, observation or prediction uncertainty. Daily bounds must not be summed into an unsupported weekly confidence interval.

## Is this an emergency service?
No. It is historical, descriptive research software. Neither a hotspot nor an unusual-period flag establishes ignition cause or an operational warning.

## Are weekly-rest-day results part of this release?
No. Old analyses are preserved as historical records, not recomputed results for the current country scope.

## Where can judges open it?
Confirm and test the actual FireLert deployment and source links before submission. Do not substitute an earlier release's URL.
