from typing import Any, Dict, List
from datetime import datetime


def filter_by_state(dictionary_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    соответствует указанному значению."""
    new_dictionary_list = list()
    for element in dictionary_list:
        if element["state"] == state:
            new_dictionary_list.append(element)

    if len(new_dictionary_list) == 0:
        raise ValueError("По данному ключу словари отсутствуют")

    return new_dictionary_list


def sort_by_date(dictionary_list: List[Dict[str, Any]], type_of_sort: bool = True) -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отсортированный по дате"""
    necessary_format = "%Y-%m-%dT%H:%M:%S.%f"
    try:
        for element in dictionary_list:
            result_of_the_match = bool(datetime.strptime(element['date'], necessary_format))
    except ValueError:
        raise ValueError("Неверный тип даты")
    else:
        return sorted(dictionary_list, key=lambda dictionary: dictionary["date"], reverse=type_of_sort)

