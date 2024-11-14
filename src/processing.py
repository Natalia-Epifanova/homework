from typing import Any, Dict, List


def filter_by_state(dictionary_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    соответствует указанному значению."""
    new_dictionary_list = list()
    for element in dictionary_list:
        if element["state"] == state:
            new_dictionary_list.append(element)
    return new_dictionary_list


def sort_by_date(dictionary_list: List[Dict[str, Any]], type_of_sort: bool = True) -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(dictionary_list, key=lambda dictionary: dictionary["date"], reverse=type_of_sort)
