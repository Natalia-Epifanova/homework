import masks

def mask_account_card(account_card_info: str) -> str:
    """Функция маскирует номер карты или счета"""
    new_account_card_info = account_card_info.split()
    result_mask = ''
    if new_account_card_info[0] == 'Счет':
        result_mask = 'Счет ' + masks.get_mask_account(int(new_account_card_info[1]))
    else:
        name_of_card = []
        for element in new_account_card_info:
            if element.isdigit():
                result_mask = " ".join(name_of_card) + " " + masks.get_mask_card_number(int(element))
            else:
                name_of_card.append(element)
    return result_mask

if __name__ == "__main__":
    print(mask_account_card('Visa Platinum 7000792289606361'))
    print(mask_account_card('Счет 73654108430135874305'))
    print(mask_account_card('MasterCard 7158300734726758'))
    print(mask_account_card('Visa Classic 6831982476737658'))
    print(mask_account_card('Visa Gold 5999414228426353'))
