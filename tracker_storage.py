from __future__ import annotations

import json
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_DATA_FILE = PROJECT_ROOT / "data" / "json" / "regimen_data.json"
LEGACY_DATA_FILE = PROJECT_ROOT / "data" / "regimen_data.json"
LOG_FILE = PROJECT_ROOT / "data" / "logs" / "app.log"


def _build_logger() -> logging.Logger:
    logger = logging.getLogger("white_matter_tracker")
    if logger.handlers:
        return logger

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=500_000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


LOGGER = _build_logger()


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _is_valid_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        datetime.fromisoformat(value)
        return True
    except ValueError:
        return False


def normalize_entry(entry: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(entry)
    if not normalized.get("type") and "fuel_minutes" in normalized:
        normalized["type"] = "regimen"
    return normalized


def validate_entry(entry: dict[str, Any]) -> tuple[bool, str]:
    if not isinstance(entry, dict):
        return False, "Entry must be a dictionary."

    if not _is_valid_date(entry.get("date")):
        return False, "Invalid or missing ISO date."

    entry_type = entry.get("type")
    if entry_type == "regimen":
        required = [
            "fuel_activity",
            "fuel_minutes",
            "wiring_activity",
            "frustration_level",
            "systolic_bp",
            "diastolic_bp",
        ]
        missing = [field for field in required if field not in entry]
        if missing:
            return False, f"Missing regimen fields: {', '.join(missing)}"

        numeric_fields = ["fuel_minutes", "frustration_level", "systolic_bp", "diastolic_bp"]
        if not all(_is_number(entry[field]) for field in numeric_fields):
            return False, "Regimen numeric fields must be numbers."
        if entry["fuel_minutes"] < 0:
            return False, "Fuel minutes cannot be negative."
        if not 1 <= entry["frustration_level"] <= 10:
            return False, "Frustration level must be 1-10."
        if entry["systolic_bp"] <= 0 or entry["diastolic_bp"] <= 0:
            return False, "Blood pressure values must be greater than 0."
        return True, ""

    if entry_type == "lab":
        required = ["a1c", "glucose", "b12", "vit_d", "egfr"]
        missing = [field for field in required if field not in entry]
        if missing:
            return False, f"Missing lab fields: {', '.join(missing)}"

        if not all(_is_number(entry[field]) for field in required):
            return False, "Lab values must be numbers."
        if any(entry[field] < 0 for field in required):
            return False, "Lab values cannot be negative."
        return True, ""

    return False, f"Unsupported entry type: {entry_type}"


def _migrate_legacy_file(data_file: Path = DEFAULT_DATA_FILE) -> None:
    if data_file.exists():
        return
    if not LEGACY_DATA_FILE.exists():
        return

    data_file.parent.mkdir(parents=True, exist_ok=True)
    LEGACY_DATA_FILE.replace(data_file)
    LOGGER.info("Migrated legacy data file from %s to %s", LEGACY_DATA_FILE, data_file)


def ensure_data_file(data_file: Path = DEFAULT_DATA_FILE) -> None:
    _migrate_legacy_file(data_file)
    data_file.parent.mkdir(parents=True, exist_ok=True)
    if not data_file.exists():
        data_file.write_text("[]\n", encoding="utf-8")
        LOGGER.info("Initialized empty data file at %s", data_file)


def load_data(data_file: Path = DEFAULT_DATA_FILE) -> list[dict[str, Any]]:
    ensure_data_file(data_file)

    try:
        raw = json.loads(data_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        backup_file = data_file.with_name(
            f"{data_file.stem}.corrupt.{datetime.now().strftime('%Y%m%d%H%M%S')}{data_file.suffix}"
        )
        data_file.replace(backup_file)
        LOGGER.exception("Corrupt JSON detected. Backed up to %s", backup_file)
        data_file.write_text("[]\n", encoding="utf-8")
        return []

    if not isinstance(raw, list):
        LOGGER.warning("Expected a list in %s, found %s", data_file, type(raw).__name__)
        return []

    cleaned: list[dict[str, Any]] = []
    dropped = 0
    for idx, entry in enumerate(raw):
        if not isinstance(entry, dict):
            LOGGER.warning("Dropping non-dict entry at index %s", idx)
            dropped += 1
            continue

        normalized = normalize_entry(entry)
        is_valid, reason = validate_entry(normalized)
        if is_valid:
            cleaned.append(normalized)
        else:
            dropped += 1
            LOGGER.warning("Dropping invalid entry at index %s: %s", idx, reason)

    if dropped:
        LOGGER.warning("Loaded %s valid entries and dropped %s invalid entries", len(cleaned), dropped)

    return cleaned


def save_data(data: list[dict[str, Any]], data_file: Path = DEFAULT_DATA_FILE) -> int:
    ensure_data_file(data_file)

    if not isinstance(data, list):
        raise TypeError("Data must be a list of entries.")

    cleaned: list[dict[str, Any]] = []
    dropped = 0

    for idx, entry in enumerate(data):
        if not isinstance(entry, dict):
            dropped += 1
            LOGGER.warning("Skipping non-dict entry at save index %s", idx)
            continue

        normalized = normalize_entry(entry)
        is_valid, reason = validate_entry(normalized)
        if is_valid:
            cleaned.append(normalized)
        else:
            dropped += 1
            LOGGER.warning("Skipping invalid entry at save index %s: %s", idx, reason)

    temp_file = data_file.with_suffix(f"{data_file.suffix}.tmp")
    temp_file.write_text(json.dumps(cleaned, indent=4), encoding="utf-8")
    temp_file.replace(data_file)

    LOGGER.info("Saved %s entries to %s (dropped=%s)", len(cleaned), data_file, dropped)
    return len(cleaned)
