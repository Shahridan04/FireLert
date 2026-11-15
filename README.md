<div align="center">

# 🔥 FireLert

### Explore the history. Question the change. Follow the evidence.

**An interactive burning activity calendar powered by NASA satellite observations.**

Built by **AstraXShip** · NASA Space Apps Challenge · Malaysia

[Explore the features](#what-you-can-explore) · [Our story](#why-firelert) · [Presentation](submission/SLIDES.md) · [30-second demo script](submission/VIDEO_SCRIPT.md)

</div>

---

## Why FireLert?

**Did burning activity change—or did the satellite instrument change?**

More than two decades of satellite observations hold a powerful record of burning activity. But different sensors see the world differently, making their records difficult to compare directly.

FireLert brings that history into an interactive visual experience. Compare raw observations with a calibrated reference record, discover seasonal patterns, and trace a striking week back to its evidence—with a regional focus on **Indonesia and Malaysia**.

## The regional record at a glance

| Historical coverage | NASA annual archives | Cleaned observations |
|:---:|:---:|:---:|
| **2003–2024** | **78** | **5,038,770** |

*Figures above describe the Indonesia and Malaysia preparation. Australia, Brazil, Egypt and the United States are also available in the explorer.*

## What you can explore

| Feature | What it helps you do |
|---|---|
| 🗓️ **Interactive activity calendar** | Choose a country and date range to explore the historical record. |
| 📊 **Raw vs. harmonized comparisons** | See how accounting for satellite differences changes the picture. |
| 🔎 **Evidence behind each week** | Inspect source counts, transformations and reported calibration bounds. |
| 🌿 **Seasons and unusual periods** | Investigate recurring patterns and historical departures from them. |
| 🌍 **Interactive 3D Earth** | Rotate through annual activity across processed regions and inspect grid values. |
| 📍 **Selected local detail** | Explore daily records for 12 selected cells per country. |
| ↗️ **Exports and shared views** | Download CSV data, export historical seasonal calendars, or share an exploration link. |

### From a pattern to its evidence

**Choose a country → explore the calendar → compare the signals → inspect a week → share what you found.**

## Built for questions, not just charts

FireLert is designed to help scientists, land managers and curious explorers interpret historical activity—not simply view a heatmap. Its calibration is evaluated on held-out years, and remaining errors stay visible.

The goal is straightforward: **make satellite differences explicit, and make historical patterns easier to investigate.**

> **Know the limits:** FireLert is a historical analysis tool, not a forecasting or emergency alert service. Hotspots are detections, not unique fires or burned area. Aqua is a reference, not ground truth; missing observations and uncolored areas do not mean no fire. Geographic coverage is limited to processed regions.

## Meet AstraXShip

**Shahrian (Leader) · Danial · Farah · Jiayi · Varshini**

Participating in the **Malaysia** local event.

## Try it locally

With Node.js and Python installed, run from the repository root:

```powershell
npm ci --prefix web
npm run build
python -m http.server 5180 --bind 127.0.0.1 --directory dist
```

Open **http://127.0.0.1:5180**.

For deeper details: [Methods](METHODS.md) · [Limitations](LIMITATIONS.md) · [Reproduction & checks](REPRODUCE.md) · [Deployment](DEPLOYMENT.md).

## Data, credits & transparency

Built on the **MIT-licensed FIRETRACE project**, using **NASA FIRMS** observations and **Natural Earth** geographic context via world-atlas.

[Attribution](ATTRIBUTION.md) · [AI assistance disclosure](AI_DISCLOSURE.md) · [License](LICENSE)

**NASA does not endorse this project.**
