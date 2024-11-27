from src.processing import filter_by_state, sort_by_date
import pytest


@pytest.fixture
def dictionaries():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(dictionaries, state, expected):
    assert filter_by_state(dictionaries, state) == expected


def test_filter_by_state_non_existent_key(dictionaries):
    with pytest.raises(ValueError):
        filter_by_state(dictionaries, state="NJKL")


def test_filter_by_state_wrong_type():
    with pytest.raises(TypeError):
        filter_by_state(12345)


def test_filter_by_state_empty_input_data():
    with pytest.raises(TypeError):
        filter_by_state()


@pytest.mark.parametrize(
    "type_of_sort, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(dictionaries, type_of_sort, expected):
    assert sort_by_date(dictionaries, type_of_sort) == expected


@pytest.fixture
def dictionaries_with_the_same_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
    ]


@pytest.mark.parametrize(
    "type_of_sort, expected",
    [
        (
            True,
            [
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
            ],
        ),
    ],
)
def test_sort_by_date_with_the_same_date(dictionaries_with_the_same_date, type_of_sort, expected):
    assert sort_by_date(dictionaries_with_the_same_date, type_of_sort) == expected


def test_sort_by_date_wrong_type_of_input_data():
    with pytest.raises(TypeError):
        filter_by_state([1, 234, 5])


@pytest.fixture
def dictionaries_with_wrong_format_of_date():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "31st of February, 2023"},
        {"id": 594226727, "state": "CANCELED", "date": "31.02.2023"},
        {"id": 615064591, "state": "CANCELED", "date": "10-2013"},
    ]


def test_sort_by_date_wrong_format_of_date(dictionaries_with_wrong_format_of_date):
    with pytest.raises(ValueError):
        sort_by_date(dictionaries_with_wrong_format_of_date)
