import pytest
from src.generators import filter_by_currency


def test_filter_by_currency_usd(transactions_list, usd_transactions):
    result = filter_by_currency(transactions_list, "USD")
    assert next(result) == usd_transactions


def test_filter_by_currency_rub(transactions_list, rub_transactions):
    result = filter_by_currency(transactions_list, "RUB")
    assert next(result) == rub_transactions


def test_filter_by_currency_exceptions(transactions_list):
    result = filter_by_currency(transactions_list, "EUR")
    assert list(result) == []
    result = filter_by_currency([], "EUR")
    assert result == "Список пустой!"

