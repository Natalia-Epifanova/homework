def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    cards_mask = str(card_number)[0:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]
    return cards_mask


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account_mask = "**" + str(account_number)[-4:]
    return account_mask


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))

if __name__ == "__main__":
    print(get_mask_account(73654108430135874305))
