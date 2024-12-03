import os

import requests
from dotenv import load_dotenv

load_dotenv("../.env")


def sum_of_transaction(transaction: dict) -> float:
    """Функция конвертирует валюту и возвращает сумму транзакции в рублях"""
    if not (isinstance(transaction, dict)):
        raise ValueError("Uncorrect type of input data")
    transaction_amount = transaction["operationAmount"]["amount"]
    transaction_currency = transaction["operationAmount"]["currency"]["code"]
    if transaction_currency == "RUB":
        return float(transaction_amount)
    try:
        if transaction_currency == "EUR" or transaction_currency == "USD":
            url = (
                f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
                f"{transaction_currency}&amount={transaction_amount}"
            )
            headers = {"apikey": os.getenv("API_KEY")}
            response = requests.get(url, headers=headers, data={}, allow_redirects=False)
            response.raise_for_status()
            return float(response.json()["result"])
        else:
            return 0.0
    except requests.exceptions.RequestException:
        print("An error occurred. Please try again later.")
        return 0.0
