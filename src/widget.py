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


def get_date(date_format: str) -> str:
    """Функция возвращает дату в нужном формате"""
    new_date_format = date_format[8:10] + '.' + date_format[5:7] + '.' + date_format[:4]
    return new_date_format


if __name__ == "__main__":
    print(mask_account_card('Visa Platinum 7000792289606361'))
    print(mask_account_card('Счет 73654108430135874305'))
    print(get_date('2024-07-02T02:26:18.671407'))
