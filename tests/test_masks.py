import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (5544269931566745, "5544 26** **** 6745"),
        (5555559931569999, "5555 55** **** 9999"),
    ],
)
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


def test_get_mask_card_number_len_of_num_after_sixteen():
    with pytest.raises(ValueError):
        get_mask_card_number(12345678912034866)


def test_get_mask_card_number_len_of_num_less_than_sixteen():
    with pytest.raises(ValueError):
        get_mask_card_number(123456667488152)


def test_get_mask_card_wrong_type():
    with pytest.raises(TypeError):
        get_mask_card_number("1234akl")


def test_get_mask_card_empty_input_data():
    with pytest.raises(TypeError):
        get_mask_card_number()


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == "**4305"
    assert get_mask_account(55442699315667454512) == "**4512"
    assert get_mask_account(55555599315699995555) == "**5555"


def test_get_mask_account_len_of_num_after_twenty():
    with pytest.raises(ValueError):
        get_mask_account(12345678912034866522225426)


def test_get_mask_account_len_of_num_less_than_twenty():
    with pytest.raises(ValueError):
        get_mask_account(2225426)


def test_get_mask_account_wrong_type():
    with pytest.raises(TypeError):
        get_mask_account("1234akl")


def test_get_mask_account_empty_input_data():
    with pytest.raises(TypeError):
        get_mask_account()
