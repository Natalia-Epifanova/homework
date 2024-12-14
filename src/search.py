import re
from collections import Counter
from typing import Any, Dict, List


def search_by_string(list_of_transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """Функция возвращает список словарей с транзакциями, у которых в описании есть необходимая слово/строка"""
    if not isinstance(list_of_transactions, list) or not isinstance(search_string, str):
        raise TypeError("Неверный тип входных данных")
    pattern = rf"{search_string}"
    result = []
    for transaction in list_of_transactions:
        if re.findall(pattern, transaction["description"], flags=re.IGNORECASE):
            result.append(transaction)

    return result


def search_by_categories(list_of_transactions: List[Dict[str, Any]], list_of_category: List[str]) -> Dict[str, Any]:
    """Функция возвращает словарь, в котором ключи — это названия категорий, а значения —
    это количество операций в каждой категории"""
    if not isinstance(list_of_transactions, list) or not isinstance(list_of_category, list):
        raise TypeError("Неверный тип входных данных")
    list_of_category_up = [category.upper() for category in list_of_category]
    transactions_count = Counter(
        transaction["state"] for transaction in list_of_transactions if transaction["state"] in list_of_category_up
    )
    result = {}
    for category, count in transactions_count.items():
        result[category] = count

    return result
