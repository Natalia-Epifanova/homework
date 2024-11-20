def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if not isinstance(card_number, int):
        raise TypeError("Ошибка типа данных")

    if len(str(card_number)) != 16:
        raise ValueError("Номер карты должен быть из 16 символов")

    cards_mask = str(card_number)[0:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]
    return cards_mask


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if not isinstance(account_number, int):
        raise TypeError("Ошибка типа данных")

    if len(str(account_number)) != 20:
        raise ValueError("Номер счета должен быть из 20 символов")

    account_mask = "**" + str(account_number)[-4:]
    return account_mask
