from unittest.mock import Mock, patch

import pytest

from requests import RequestException

from src.external_api import sum_of_transaction


@pytest.fixture
def transaction_for_test_external_api_rub():
    return {"id": 41428829, "operationAmount": {"amount": "10", "currency": {"code": "RUB"}}}


def test_sum_of_transaction_value_error():
    with pytest.raises(ValueError):
        sum_of_transaction("")


def test_sum_of_transaction_rub(transaction_for_test_external_api_rub):
    result = sum_of_transaction(transaction_for_test_external_api_rub)
    assert result == 10


@patch("src.external_api.requests.get")
def test_sum_of_transaction_convert_currency(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 10},
        "info": {"timestamp": 1733231405, "rate": 105.945524},
        "date": "2024-12-03",
        "result": 1060.5509,
    }
    result = sum_of_transaction({"id": 41428829, "operationAmount": {"amount": "10", "currency": {"code": "USD"}}})
    assert result == 1060.5509
    mock_get.assert_called_once()


@patch("src.external_api.requests.get", side_effect=RequestException)
def test_sum_of_transaction_request_exception(mock_get):
    result = sum_of_transaction({"id": 41428829, "operationAmount": {"amount": "10", "currency": {"code": "USD"}}})
    assert result == 0.0


@patch("src.external_api.requests.get")
def test_sum_of_transaction_wrong_currency(mock_get):
    result = sum_of_transaction({"id": 41428829, "operationAmount": {"amount": "10", "currency": {"code": "AER"}}})
    assert result == 0.0
