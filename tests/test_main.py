from unittest.mock import mock_open, patch

from main import choose_file, choose_sort, choose_status, choose_rub_currency, choose_string_for_search, final_printing

transaction_list_sample = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "amount": 31957.58,
        "currency_name": "руб.",
        "currency_code": "RUB",
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
]


@patch("main.financial_transactions")
@patch("main.input")
def test_choose_file_json(mock_input, mock_read_data) -> None:
    mock_input.return_value = 1
    mock_read_data.return_value = transaction_list_sample
    assert choose_file() == transaction_list_sample


@patch("main.reading_csv")
@patch("main.input")
def test_choose_file_csv(mock_input, mock_read_data) -> None:
    mock_input.return_value = 2
    mock_read_data.return_value = transaction_list_sample
    assert choose_file() == transaction_list_sample


@patch("main.reading_excel")
@patch("main.input")
def test_choose_file_xlsx(mock_input, mock_read_data) -> None:
    mock_input.return_value = 3
    mock_read_data.return_value = transaction_list_sample
    assert choose_file() == transaction_list_sample


@patch("main.input")
def test_choose_status(mock_input) -> None:
    mock_input.return_value = "EXECUTED"
    assert choose_status(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_choose_sort_ascending(mock_input):
    mock_input.side_effect = ["да", "по возрастанию"]
    assert choose_sort(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_choose_sort_descending(mock_input):
    mock_input.side_effect = ["да", "по убыванию"]
    assert choose_sort(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_choose_sort_no(mock_input):
    mock_input.return_value = "нет"
    assert choose_sort(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_choose_rub_currency_yes(mock_input):
    mock_input.return_value = "да"
    assert choose_rub_currency(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_choose_rub_currency_no(mock_input):
    mock_input.return_value = "нет"
    assert choose_rub_currency(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_choose_string_for_search_yes(mock_input):
    mock_input.side_effect = ["да", "перевод"]
    assert choose_string_for_search(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_choose_string_for_search_no(mock_input):
    mock_input.return_value = "нет"
    assert choose_string_for_search(transaction_list_sample) == transaction_list_sample


def test_final_printing(capsys):
    final_printing(transaction_list_sample)
    result = capsys.readouterr()
    assert (
        result.out
        == "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\nСумма: 31957.58 RUB\n\n"
    )


def test_final_printing_for_account(capsys):
    final_printing([])
    result = capsys.readouterr()
    assert result.out == "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n"
