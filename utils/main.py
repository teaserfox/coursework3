import os
from utils import open_file, last_num_lines, date_format, \
    type_of_payment, payment_system_and_account, user_account, accessing_the_dict, number_account_sender, number_account_recipient

# TODO константа пути перенесена из utils
PATH = os.path.join('operations.json')

raw_data = open_file(PATH)
last_lines = last_num_lines(raw_data)

for item in last_lines:
    thedate = date_format(item)  # дата в ISO
    description = type_of_payment(item)  # описание платежа

    # (полный_счет, название_счета)
    sender_bill = payment_system_and_account(item)
    # (полный_счет, название_счета)
    getter_bill = user_account(item)

    sender_bill_num = number_account_sender(sender_bill[0])  # Скрытый счет отправителя (только цифры)
    getter_bill_num = number_account_recipient(getter_bill[0])  # Скрытый счет получателя (только цифры)

    bill_amount = accessing_the_dict(item)  # Сумма платежа в заданной валюте

    print(f'''{thedate.day}.{thedate.month}.{thedate.year} {description}
{sender_bill[1]} {sender_bill_num} -> {getter_bill[1]} {getter_bill_num}
{bill_amount['amount']} {bill_amount['currency']}\n''')




