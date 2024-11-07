def filter_by_state(dictionary_list: list, state: str = "EXECUTED") -> list:
    new_dictionary_list = list()
    for element in dictionary_list:
        if element["state"] == state:
            new_dictionary_list.append(element)
    return new_dictionary_list


def sort_by_date(dictionary_list: list, type_of_sort: bool = True) -> list:
    return sorted(dictionary_list, key=lambda dictionary: dictionary["date"], reverse=type_of_sort)
