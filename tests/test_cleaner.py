import pytest
from src.cleaner import clean_and_validate_row

def test_valid_data():
    raw_input = {
        "id_user": 1,
        "nama": "  Budi Santoso  ",
        "email": "budi@example.com",
        "nik": "6171012345678901",
        "umur": 25
    }
    cleaned_data, errors = clean_and_validate_row(raw_input)
    assert errors == []
    assert cleaned_data["nama"] == "Budi Santoso"

def test_invalid_nik_and_email():
    raw_input = {
        "id_user": 2,
        "nama": "Andi",
        "email": "email-salah",
        "nik": "12345ABC",
        "umur": 30
    }
    cleaned_data, errors = clean_and_validate_row(raw_input)
    assert cleaned_data is None
    assert len(errors) >= 2

def test_empty_payload():
    cleaned_data, errors = clean_and_validate_row({})
    assert cleaned_data is None
    assert "Payload data kosong" in errors