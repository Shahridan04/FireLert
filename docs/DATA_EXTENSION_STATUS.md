# Indonesia/Malaysia data extension acquisition

## Downloaded and verified

Four NASA FIRMS 2025 country archives are downloaded under the ignored local directory `work/sea-extension/archives`:

| Country | MODIS records | Suomi-NPP VIIRS records |
|---|---:|---:|
| Indonesia | 17,847 | 96,056 |
| Malaysia | 1,617 | 7,208 |

CSV structure and SHA-256 checksums are recorded in the local download manifest. MODIS files contain Terra/Aqua; VIIRS files identify the Suomi-NPP platform (`N`). Exact cleaned count partitions are staged in `work/sea-extension/prepared`. No new data has been promoted into the published application.

## Publication blocker: local-day boundaries

The existing pipeline requires adjacent UTC annual archives before declaring a complete local civil year (`pipeline/harmonize.py`, `_archive_years`). Although the 2025 UTC archives exist, the canonical 2026 MODIS and Suomi-NPP country archive URLs for both countries return HTTP 404. Consequently, a complete local 2025 year cannot yet be established with these inputs. A maximum acquisition timestamp is not a completeness guarantee.

Do not bypass this guard, fabricate a 2026 manifest entry, or fill unverified boundary days with zero. Do not label the downloaded 2025 files as 2026 observations: local-time conversion can move a small number of late-December UTC records into January without establishing January coverage.

## Safe next steps

1. Obtain verified adjacent 2026 observations with documented coverage, or implement a separately tested partial-period publication path that excludes unverified local boundary days.
2. Preserve the frozen model and 2020–2024 evaluation. Distinguish the original training-source fingerprint from the extension input fingerprint rather than rewriting the locked provenance.
3. Preserve the existing 12 training-selected daily cells when preparing extension counts; the extension alone has no training-period data and cannot select them.
4. Regenerate and reconcile national, selected-cell, annual-map and globe outputs. Keep other countries' unavailable extension years null.
5. Publish actual coverage dates, partial-year map labels and an explicit outside-evaluation notice before adding newer years to selectors.

The production release remains 2003–2024 until these checks pass. Downloaded source data alone is not a completed system update.