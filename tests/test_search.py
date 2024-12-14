import pytest

from src.search import search_by_categories, search_by_string


def test_search_by_string(transactions_list_for_test):
    result = search_by_string(transactions_list_for_test, "организации")
    assert result == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
        },
    ]


def test_search_by_string_wrong_type(transactions_list_for_test):
    with pytest.raises(TypeError):
        search_by_string(123, "перевод")
    with pytest.raises(TypeError):
        search_by_string(transactions_list_for_test, 123)


def test_search_by_string_empty_list():
    result = search_by_string([], "перевод")
    assert result == []


def test_search_by_categories(transactions_list_for_test):
    result = search_by_categories(transactions_list_for_test, ["EXECUTED", "CANCELED"])
    assert result == {"EXECUTED": 2, "CANCELED": 1}


def test_search_by_categories_ignorecase(transactions_list_for_test):
    result = search_by_categories(transactions_list_for_test, ["Executed", "canceled"])
    assert result == {"EXECUTED": 2, "CANCELED": 1}


def test_search_by_categories_wrong_type(transactions_list_for_test):
    with pytest.raises(TypeError):
        search_by_categories(123, ["EXECUTED", "CANCELED"])
    with pytest.raises(TypeError):
        search_by_categories(transactions_list_for_test, 123)
