import pytest
from src.generators import filter_by_currency, transaction_descriptions


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


def test_filter_by_currency_wrong_type():
    with pytest.raises(TypeError):
        next(filter_by_currency(1, [4, 3, 2]))
    with pytest.raises(TypeError):
        next(filter_by_currency("some_sring", 2))


def test_transaction_descriptions(transactions_list):
    result = transaction_descriptions(transactions_list)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"


def test_transaction_descriptions_exceptions():
    with pytest.raises(StopIteration):
        next(transaction_descriptions([]))


def test_transaction_descriptions_wrong_type():
    with pytest.raises(TypeError):
        next(transaction_descriptions(1))
    with pytest.raises(TypeError):
        next(transaction_descriptions("some_sring"))

