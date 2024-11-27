import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card(number, expected):
    assert mask_account_card(number) == expected


def test_mask_account_card_empty_input_data():
    with pytest.raises(TypeError):
        mask_account_card()


def test_mask_account_card_empty_string():
    with pytest.raises(TypeError):
        mask_account_card("")


def test_mask_account_card_wrong_type():
    with pytest.raises(TypeError):
        mask_account_card([2, 7, 8, 9])


def test_mask_account_card_invalid_type_of_number():
    with pytest.raises(TypeError):
        mask_account_card("544555")


@pytest.mark.parametrize(
    "original_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-02-21T02:26:18.671407", "21.02.2024"),
        ("2023-09-01T02:26:18.671407", "01.09.2023"),
        ("2024-03-12T02:26:18.671407", "12.03.2024"),
    ],
)
def test_get_date(original_date, expected):
    assert get_date(original_date) == expected


def test_get_date_len_of_date_after_twenty_six():
    with pytest.raises(ValueError):
        get_date("2024-03-11T02:26:18.67140755512")


def test_get_date_len_of_date_less_than_twenty_six():
    with pytest.raises(ValueError):
        get_date("2024-03-11T12")


def test_get_date_empty_input_data():
    with pytest.raises(TypeError):
        get_date()


def test_get_date_empty_string():
    with pytest.raises(TypeError):
        get_date("")


def test_get_date_wrong_type():
    with pytest.raises(TypeError):
        get_date(555)
