import json
from typing import Any


def financial_transactions(path: str) -> list:
    """Функция возвращает список словарей с данными о финансовых транзакциях из JSON-файла"""

    try:
        with open(path, encoding="UTF-8") as json_file:
            transaction_data = json.load(json_file)
        return transaction_data
    except json.JSONDecodeError:
        print("Invalid JSON data.")
        return []
    except FileNotFoundError:
        print("There is no such file")
        return []


# if __name__ == "__main__":
#     res = financial_transactions("../data/operations.json")
#     print(res)