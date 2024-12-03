import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv("../.env")


def sum_of_transaction(transaction: dict) -> float:
    """Функция конвертирует валюту и возвращает сумму транзакции в рублях"""
    transaction_amount = transaction.get("operationAmount").get("amount")
    transaction_currency = transaction.get("operationAmount").get("currency").get("code")
    if transaction_currency == "RUB":
        return float(transaction_amount)
    try:
        if transaction_currency == "EUR" or transaction_currency == "USD":
            url = (
                f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
                f"{transaction_currency}&amount={transaction_amount}"
            )
            headers = {"apikey": os.getenv("API_KEY")}
            response = requests.request("GET", url, headers=headers, data={}, allow_redirects=False)
            response.raise_for_status()
            return float(response.json().get("result"))
    except requests.exceptions.RequestException:
        print("An error occurred. Please try again later.")


# if __name__ == "__main__":
#     print(
#         sum_of_transaction(
#             {
#                 "id": 441945886,
#                 "state": "EXECUTED",
#                 "date": "2019-08-26T10:50:58.294041",
#                 "operationAmount": {"amount": "5", "currency": {"name": "руб.", "code": "USD"}},
#                 "description": "Перевод организации",
#                 "from": "Maestro 1596837868705199",
#                 "to": "Счет 64686473678894779589",
#             }
#         )
#     )

