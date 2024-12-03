from unittest.mock import mock_open, patch

from src.utils import financial_transactions


@patch("builtins.open", new_callable=mock_open, read_data='{"transaction_id": 1}')
def test_financial_transactions(mock_file):
    transactions_for_test = financial_transactions("data/operations.json")
    assert transactions_for_test == {"transaction_id": 1}


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_financial_transactions_empty_file(mock_file):
    transactions_for_test = financial_transactions("data/operations.json")
    assert transactions_for_test == []


@patch("builtins.open", new_callable=mock_open, read_data='("some_string", [4, 5], 3)')
def test_financial_transactions_wrong_type_of_data(mock_file):
    transactions_for_test = financial_transactions("data/operations.json")
    assert transactions_for_test == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_financial_transactions_file_not_found(mock_file):
    transactions_for_test = financial_transactions("data/test.json")
    assert transactions_for_test == []
