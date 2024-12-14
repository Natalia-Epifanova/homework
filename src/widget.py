from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    """Функция маскирует номер карты или счета"""
    if not isinstance(account_card_info, str) or account_card_info == "":
        raise TypeError("Ошибка типа данных")

    new_account_card_info = account_card_info.split()

    if not new_account_card_info[0].isalpha():
        raise TypeError("Ошибка ввода данных, не хватает указания типа (Счет или название карты)")

    result_mask = ""
    if new_account_card_info[0] == "Счет":
        result_mask = "Счет " + get_mask_account(new_account_card_info[1])
    else:
        name_of_card: list[str] = []
        for element in new_account_card_info:
            if element.isdigit() or element.startswith("0"):
                result_mask = " ".join(name_of_card) + " " + get_mask_card_number(element)
            else:
                name_of_card.append(element)
    return result_mask


def get_date(date_format: str) -> str:
    """Функция возвращает дату в нужном формате"""
    if not isinstance(date_format, str) or date_format == "":
        raise TypeError("Ошибка типа данных")

    new_date_format = date_format[8:10] + "." + date_format[5:7] + "." + date_format[:4]
    return new_date_format


# (mask_account_card('Счет 41878599375303475996'))
