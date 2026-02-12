import json

import tracker_storage


def valid_regimen_entry():
    return {
        "date": "2026-02-12",
        "type": "regimen",
        "fuel_activity": "Walk",
        "fuel_minutes": 30,
        "wiring_activity": "Piano / Instrument",
        "frustration_level": 6,
        "systolic_bp": 118,
        "diastolic_bp": 74,
    }


def valid_lab_entry():
    return {
        "date": "2026-02-12",
        "type": "lab",
        "a1c": 7.3,
        "glucose": 247,
        "b12": 1500,
        "vit_d": 120,
        "egfr": 70,
    }


def test_validate_entry_accepts_valid_entries():
    ok_regimen, _ = tracker_storage.validate_entry(valid_regimen_entry())
    ok_lab, _ = tracker_storage.validate_entry(valid_lab_entry())
    assert ok_regimen
    assert ok_lab


def test_save_data_filters_invalid_entries(tmp_path):
    data_file = tmp_path / "data" / "json" / "regimen_data.json"
    payload = [valid_regimen_entry(), {"date": "bad-date", "type": "lab"}]

    saved_count = tracker_storage.save_data(payload, data_file)

    assert saved_count == 1
    saved = json.loads(data_file.read_text(encoding="utf-8"))
    assert len(saved) == 1
    assert saved[0]["type"] == "regimen"


def test_load_data_recovers_from_corrupt_json(tmp_path):
    data_file = tmp_path / "data" / "json" / "regimen_data.json"
    data_file.parent.mkdir(parents=True, exist_ok=True)
    data_file.write_text("{bad json", encoding="utf-8")

    loaded = tracker_storage.load_data(data_file)

    assert loaded == []
    backups = list(data_file.parent.glob("regimen_data.corrupt.*.json"))
    assert backups
    assert data_file.exists()
    assert data_file.read_text(encoding="utf-8").strip() == "[]"


def test_legacy_data_file_is_migrated(monkeypatch, tmp_path):
    legacy_file = tmp_path / "data" / "regimen_data.json"
    target_file = tmp_path / "data" / "json" / "regimen_data.json"
    legacy_file.parent.mkdir(parents=True, exist_ok=True)
    legacy_file.write_text(json.dumps([valid_lab_entry()]), encoding="utf-8")

    monkeypatch.setattr(tracker_storage, "LEGACY_DATA_FILE", legacy_file)

    loaded = tracker_storage.load_data(target_file)

    assert target_file.exists()
    assert not legacy_file.exists()
    assert len(loaded) == 1
    assert loaded[0]["type"] == "lab"
