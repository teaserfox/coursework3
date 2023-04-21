import json
import re
from datetime import date


def open_file(path):
    """
    Функция, возвращающая Python-список всех операций
    """
    with open(path, 'r', encoding='utf-8') as file:
        banking_operations = json.load(file)
        return banking_operations


def last_num_lines(banking_operations):
    """
    Функция, возвращающая в виде списка словарей 5 последних операций

    TODO

    1) Тут от цикла можно избавится, так как в любом случае возвращается целый список,
    цикл  в main
    2) Смысла использовать reverse нет, 5 последних элментов достаточно выбрать срезом
    3) Нужно выбрать последние 5 выполненных (EXECUTED) операций

    """

    #     for line in reversed(banking_operations[-5:]):
    #         five_recent_operations = line
    #         return five_recent_operations

    executed_operations = []

    for operation in banking_operations:
        if operation.get("state") == "EXECUTED":
            executed_operations.append(operation)

    return executed_operations[-5:]


def date_format(recent_operation):
    """
    Функция, форматирующая дату в вид YYYY-MM-DD

    TODO

    1) Изменино название аргумента, т.к. берем теперь только одну операцию
    2) Немного сокращён код

    """

    # data = recent_operation['date']
    # res_data = data[:10]
    # thedate = date.fromisoformat(res_data)
    # return thedate

    data = recent_operation['date'][:10]
    thedate = date.fromisoformat(data)

    return thedate


def type_of_payment(recent_operation):
    """
    Функция, возвращающая вид операции
    """

    description = recent_operation['description']
    return description


def payment_system_and_account(recent_operation):
    """
    Функция, возвращающая название и номер счета отправителя
    """

    fromm = recent_operation.get('from', '')
    str1 = fromm.split()
    str2 = ''.join(str1[:1])

    return fromm, str2


def user_account(recent_operation):
    """
    Функция, возвращающая название и номер счета получателя
    """

    account_user = recent_operation['to']
    str3 = account_user.split()
    str4 = ''.join(str3[:1])

    return account_user, str4


def number_account_sender(full_bill):
    """
    Функция, возвращающая скрытый номер счета отправителя
    """

    nums1 = re.findall(r'\d+', full_bill)  # ['3', '10', '88', '13']
    nums1_str = ''.join(map(str, nums1))

    simbol = (len(nums1_str) - 10) * '*'
    requisites_code1 = nums1_str[:6] + simbol + nums1_str[-4:]
    requisites1 = [requisites_code1[i:i + 4] for i in range(0, len(requisites_code1), 4)]
    requisites_format1 = ' '.join(requisites1)

    return requisites_format1


def number_account_recipient(full_bill):
    """
    Функция, возвращающая скрытый номер счета получателя
    """

    nums2 = re.findall(r'\d+', full_bill)
    nums2_str = ''.join(map(str, nums2))

    requisites_code2 = '**' + nums2_str[-4:]
    requisites_format2 = ''.join(requisites_code2)

    return requisites_format2


def accessing_the_dict(recent_operation):
    """
    Функция, возвращающая сумму платежа
    """

    summ = recent_operation['operationAmount']

    # Название валюты
    currency = summ['currency']["name"]
    # Сумма платежа
    amount = summ['amount']

    return {
        "currency": currency,
        "amount": amount
    }
