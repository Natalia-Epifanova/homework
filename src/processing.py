from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(dictionary_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    соответствует указанному значению."""
    new_dictionary_list = list()
    for element in dictionary_list:
        if "state" in element:
            if element["state"] == state:
                new_dictionary_list.append(element)

    if len(new_dictionary_list) == 0:
        raise ValueError("По данному ключу словари отсутствуют")

    return new_dictionary_list


def sort_by_date(dictionary_list: List[Dict[str, Any]], type_of_sort: bool = True) -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отсортированный по дате"""
    format_list = ["%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%SZ"]

    for element in dictionary_list:
        for format_of_date in format_list:
            try:
                datetime.strptime(element["date"], format_of_date)
                return sorted(dictionary_list, key=lambda dictionary: dictionary["date"], reverse=type_of_sort)
            except ValueError:
                continue
        raise ValueError("Неверный тип даты")
