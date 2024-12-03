import json
from typing import Any


def financial_transactions(path: str) -> Any[list]:
    """Функция возвращает список словарей с данными о финансовых транзакциях из JSON-файла"""
    try:
        with open(path, encoding="UTF-8") as json_file:
            transaction_data = json.load(json_file)
        return transaction_data
    except json.JSONDecodeError:
        print("Invalid JSON data.")
        return []
    except TypeError:
        print("This object is not JSON serializable.")
        return []
    except FileNotFoundError:
        print("There is no such file")
        return []


if __name__ == "__main__":
    print(financial_transactions("../data/operations.json"))
