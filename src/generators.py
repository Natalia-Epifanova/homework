from collections.abc import Iterator
from typing import Any, Dict, Generator, List


def filter_by_currency(list_of_transactions: List[Dict[str, Any]], currency: str) -> filter | str:
    """Функция должна возвращает итератор, выдающий транзакции, где валюта операции соответствует заданной"""
    if not isinstance(list_of_transactions, list) or not isinstance(currency, str):
        raise TypeError("Ошибка типа данных")
    if len(list_of_transactions) > 0:
        if any("operationAmount" in x for x in list_of_transactions):
            filtered_transaction = filter(
                lambda x: x["operationAmount"]["currency"]["code"] == currency, list_of_transactions
            )
        elif any("currency_name" in x for x in list_of_transactions):
            filtered_transaction = filter(lambda x: x["currency_code"] == currency, list_of_transactions)
        return filtered_transaction
    else:
        return "Список пустой!"


def transaction_descriptions(list_of_transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """Генератор, принимающий список словарей с транзакциями и возвращающий описание каждой операции по очереди"""
    if not isinstance(list_of_transactions, list):
        raise TypeError("Ошибка типа данных")
    for transaction in list_of_transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор номеров банковских карт в формате 'XXXX XXXX XXXX XXXX'"""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Ошибка типа данных")
    if stop < start:
        raise ValueError("Границы диапазона указаны неверно (в обратном порядке)!")
    if len(str(start)) <= 16:
        for number in range(start, stop + 1):
            formated_card_number = "{:016}".format(number)
            yield " ".join(formated_card_number[i * 4 : (i + 1) * 4] for i in range(4))
    else:
        raise ValueError("Входные данные превышают допустимые значения!!!")


# trans = [
#   {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#   {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   },
#   {
#     "id": 939719570,
#     "state": "EXECUTED",
#     "date": "2018-06-30T02:08:58.425572",
#     "operationAmount": {
#       "amount": "9824.07",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     }
#   }
# ]
#
# rez = filter_by_currency(trans, "RUB")
# for value in rez:
#     print(value)
