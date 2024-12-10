from unittest.mock import patch

import pytest

from src.reading_csv_excel import reading_csv, reading_excel


@patch("pandas.read_csv")
def test_reading_csv(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]
    assert reading_csv("test_file.csv") == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]


@patch("pandas.read_csv", side_effect=FileNotFoundError)
def test_reading_csv_file_not_found(mock_file):
    try_to_read_csv = reading_csv("test_file.csv")
    assert try_to_read_csv == []


def test_reading_csv_wrong_input_data():
    with pytest.raises(TypeError):
        reading_csv(1, 2)
    with pytest.raises(TypeError):
        reading_csv([1, 2])


@patch("pandas.read_excel")
def test_reading_excel(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]
    assert reading_excel("test_file.excel") == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_reading_excel_file_not_found(mock_file):
    try_to_read_excel = reading_excel("test_file.excel")
    assert try_to_read_excel == []


def test_reading_excel_wrong_input_data():
    with pytest.raises(TypeError):
        reading_excel(1, 2)
    with pytest.raises(TypeError):
        reading_excel([1, 2])
