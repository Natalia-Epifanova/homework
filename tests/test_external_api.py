import json
from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import sum_of_transaction

#
# @patch('requests.get')
# def test_sum_of_transaction_convert_currency(mock_get, transaction_for_test_external_api):
#     mock_get.return_value.json.return_value = {'result': 10}
#     assert sum_of_transaction({}) == 10
#     #mock_get.assert_called_once_with('https://api.github.com/users/testuser')
# #


# C:\Users\User1\AppData\Local\pypoetry\Cache\virtualenvs\homework-ILI2lnVY-py3.11\Scripts\python.exe C:\Users\User1\Desktop\мое\Учеба\my_prj\homework\src\external_api.py
# {'success': True,
# 'query':
#       {'from': 'USD', 'to': 'RUB', 'amount': 5},
#  'info': {'timestamp': 1733231405, 'rate': 105.945524},
#  'date': '2024-12-03',
#  'result': 529.72762}
# 529.72762
# def sum_of_transaction(transaction: dict) -> Any[float]:
#     """Функция конвертирует валюту и возвращает сумму транзакции в рублях"""
#     transaction_amount = transaction.get("operationAmount").get("amount")
#     transaction_currency = transaction.get("operationAmount").get("currency").get("code")
#     if transaction_currency == "RUB":
#         return float(transaction_amount)
#     try:
#         if transaction_currency == "EUR" or transaction_currency == "USD":
#             url = (
#                 f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from="
#                 f"{transaction_currency}&amount={transaction_amount}"
#             )
#             headers = {"apikey": os.getenv("API_KEY")}
#             response = requests.request("GET", url, headers=headers, data={}, timeout=20, allow_redirects=False)
#             response.raise_for_status()
#             return float(response.json().get("result"))
#     except requests.exceptions.RequestException:
#         print("An error occurred. Please try again later.")
