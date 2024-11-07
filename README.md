# Работа над виджетом банковских операций клиента

## Описание:
IT-отдел крупного банка делает новую фичу для личного кабинета клиента. 
Это виджет, который показывает несколько последних успешных банковских 
операций клиента

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/Natalia-Epifanova/homework.git
```
2. Установите зависимости (**будут готовы позже**):
```
pip install -r requirements.txt
```

## Реализованные функции и примеры их работы:
1. ```mask_account_card``` - на вход принимается строка, содержащая тип и номер карты или счета. Возвращается замаскированный номер
+ Пример работы:
```mask_account_card("Visa Platinum 7000792289606361")``` -> ```Visa Platinum 7000 79** **** 6361```
2. ```get_date``` - на вход принимается строка с датой в формате "2024-03-11T02:26:18.671407"
 и возвращает строку с датой в формате "ДД.ММ.ГГГГ".
+ Пример работы: 
```get_date("2024-07-02T02:26:18.671407")``` -> ```02.07.2024```
3. ```filter_by_state``` - на вход принимается список словарей и опционально значение для ключа (по умолчанию 
**EXECUTED**). На выходе новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению
+ Пример работы: 
```filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]``` -> ```[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]```
4. ```sort_by_date``` - на вход принимается  список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). На выходе - новый список, отсортированный по дате
+ Пример работы: 
```sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])``` -> ```[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
