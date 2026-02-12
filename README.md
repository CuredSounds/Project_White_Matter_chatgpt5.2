# Project White Matter: Enhancement Master Framework

## Overview
This project is dedicated to ingesting and tracking the "White Matter Enhancement Master Framework," designed to improve brain connectivity, processing speed, and motor function through targeted lifestyle changes.

The framework is based on the biological principles of **Myelination** (insulating neural pathways) and **Neurogenesis** (supporting brain health).

## The Three Pillars
Success relies on three core pillars working in unison:

### 1. The Fuel (Aerobics) 🏃‍♀️
**Goal:** Increase Brain-Derived Neurotrophic Factor (BDNF).
- **Target:** 30–40 minutes of moderate-to-vigorous activity, 3-4 times a week.
- **Activities:** Brisk walking, swimming, recumbent cycling.
- **Why:** This acts as the "supply chain," delivering oxygen and growth factors to the white matter.

### 2. The Wiring (Complex Skills) 🎹
**Goal:** Trigger the "Frustration Signal" to stimulate myelination.
- **Target:** Engage in activities that feel challenging and require focus.
- **Principle:** The feeling of "effort" signals oligodendrocytes to wrap more myelin around active neural circuits.
- **Activities:**
    - **Motor-Cognitive:** Playing an instrument (e.g., piano), complex coordination with non-dominant hand.
    - **Cognitive Switching:** Language learning, strategy games (Chess, Go).
    - **New Skills:** Learning a new dance or motor pattern.

### 3. The Protection (Health Metrics) 🛡️
**Goal:** Prevent chronic "wear and tear" on white matter.
- **Key Metric:** Blood Pressure Management (<120/80 mmHg).
- **Secondary:** Glucose control and nutrition.
- **Nutrition:** Omega-3s (Salmon, Walnuts) and B Vitamins (Leafy greens) to support myelin structure.

## Medical Watchlist & Risks
Based on the **longitudinal analysis (Oct 2024 - Feb 2026)**, the following specific risks are being monitored in this project:

-   **Vitamin B12 Toxicity:** Latest levels were >1,500 pg/mL. Risks: Diagnostic masking, potential toxicity.
-   **Vitamin D Toxicity:** Levels >100 ng/mL. Risk: Hypercalcemia, renal stress.
-   **Diabetes Volatility:** Recent spikes (e.g., 247 mg/dL) despite "safe" A1c. Monitoring for "U-shaped" trajectory.

## Regimen Tracker App

This project includes a **Streamlit** application to track daily progress against these pillars.

### How to Run
1.  Ensure you have Python installed.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    streamlit run app.py
    ```

### Data Export
The application allows you to export your logs to **CSV format**, which can be easily imported into **Google Sheets** for further analysis or sharing with doctors.

### File Structure
- `app.py`: The main tracker application.
- `tracker_storage.py`: Data IO, validation, migration, and logging helpers.
- `data/json/regimen_data.json`: Canonical local storage for logs.
- `data/logs/app.log`: Application log file.
- `documents/clinical/`: Clinician-facing summaries.
- `documents/transcripts/`: AI conversation exports and working notes.

### Notes
- Legacy data at `data/regimen_data.json` is auto-migrated on first load.
- Keep secrets out of git-tracked files. Use `gcp.env.example` as a template.
