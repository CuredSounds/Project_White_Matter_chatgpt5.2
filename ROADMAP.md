# Project White Matter Roadmap

## Product goal
Build a reliable, patient-friendly health tracking tool that supports day-to-day decisions and clinician conversations with clean longitudinal data.

## North-star outcomes
- Fewer missing or inconsistent records.
- Clear trend visibility for high-risk markers.
- Faster, better-prepared clinician visits.
- Reduced manual effort to ingest records.

## Phase 0: Foundation and Safety (Done/In Progress)
Timeline: Week 1

- Secret hygiene and repo cleanup.
- Canonical document structure (`documents/clinical`, `documents/transcripts`).
- Data path standardization and legacy migration.
- Logging and JSON validation.
- Baseline automated tests for storage.

## Phase 1: Data Integrity and UX Reliability
Timeline: Weeks 2-3

- Add explicit data schema versioning.
- Add edit/delete flows in Streamlit with confirmation and audit trail.
- Add duplicate detection for same-day duplicate entries.
- Add import flow for lab CSVs with validation report.
- Add clearer error surfaces in UI (not just logs).

## Phase 2: Clinical Utility Layer
Timeline: Weeks 3-5

- Build a "Visit Prep" page with:
  - latest values,
  - recent deltas,
  - out-of-range flags,
  - physician questions list.
- Add threshold-based alerts:
  - BP trend alerts,
  - glucose spike alerts,
  - micronutrient over-range alerts.
- Add medication/supplement tracker tied to lab timeline.

## Phase 3: Longitudinal Intelligence
Timeline: Weeks 5-8

- Trend decomposition (short/medium/long windows).
- Variability scoring (for glucose and BP volatility).
- Adherence overlays (exercise + regimen consistency vs labs).
- Exportable clinician packet (PDF/CSV bundle).

## Phase 4: Integrations
Timeline: Weeks 8-12

- MyChart/Lab PDF ingestion pipeline (semi-automated).
- Optional CGM data import (Dexcom/Libre CSV).
- Google Sheets sync with conflict-safe merge.
- Secure cloud backup with encrypted snapshots.

## Phase 5: Advanced Features
Timeline: Quarter 2

- Personalized goal recommendations constrained by clinician settings.
- Cohort-style benchmarking (age/comorbidity adjusted, if authorized data exists).
- Explainable risk scoring for specific watchlist items.
- Optional caregiver view with permission controls.

## Prioritized feature backlog
1. Data correction workflow (edit/delete + audit trail).
2. Visit-prep one-pager generator.
3. CSV lab import with strict schema checks.
4. Alert center for threshold breaches and trend deterioration.
5. Medication/supplement timeline.
6. Record provenance tags (manual entry vs imported PDF vs inferred).
7. Reminder system for labs, appointments, and follow-up questions.
8. Role-based views (patient, caregiver, clinician summary).

## Quality gates for every release
- Schema validation passes.
- Regression tests green.
- No plaintext secrets.
- Backup/export round-trip tested.
- Clinician summary refresh checked.
