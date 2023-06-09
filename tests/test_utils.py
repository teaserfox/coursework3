import pytest
import datetime
from utils.utils import (open_file,
                        last_num_lines,
                        date_format,
                        type_of_payment,
                         payment_system_and_account,
                         user_account,
                         accessing_the_dict,
                         number_account_sender,
                         number_account_recipient)


def test_open_file():
    #assert open_file("operations.json") is not None
    #assert type(open_file("operations.json")) is list

    with pytest.raises(FileNotFoundError):
        open_file("test.json")

def test_last_num_lines():

    test_data = [
        {"state": "EXECUTED"},
        {"state": "EXECUTED"},
        {"state": "EXECUTED"},
        {"state": "CANCELED"},
        {},
    ]

    assert last_num_lines(test_data) == [
        {"state": "EXECUTED"},
        {"state": "EXECUTED"},
        {"state": "EXECUTED"}
    ]


@pytest.mark.parametrize("operation_dict, result_date_month", [({"date": "2019-08-26T10:50:58.294041"}, 8), 
                                                         ({"date": "2019-07-03T18:35:29.512364"}, 7), 
                                                         ({"date": "2018-03-23T10:45:06.972075"}, 3)])
def test_data_format(operation_dict, result_date_month):
    assert type(date_format(operation_dict)) is datetime.date
    assert date_format(operation_dict).month == result_date_month


@pytest.mark.parametrize('open_description, result_payment', [({'description': 'Перевод организации'}, str),
                                                          ({'description': 'Открытие вклада'}, str),
                                                          ({'description': 'Перевод со счета на счет'}, str),
                                                          ({'description': 'Перевод со счета на счет'}, str)])

def test_type_of_payment(open_description, result_payment):
    assert type(type_of_payment(open_description)) is str


@pytest.mark.parametrize('text, account', [({'from': 'Maestro 1308795367077170'}, tuple)])

def test_payment_system_and_account(text, account):
    assert type(payment_system_and_account(text)) is tuple



@pytest.mark.parametrize('text2, account2', [({'to': 'Счет 96527012349577388612'}, tuple)])

def test_user_account(text2, account2):
    assert type(user_account(text2)) is tuple



def test_number_account_sender():

     assert number_account_sender('1308795367077170') == '1308 79** **** 7170'
     assert number_account_sender('46363668439560358409') == '4636 36** **** **** 8409'
     assert number_account_sender('26406253703545413262') == '2640 62** **** **** 3262'
     assert number_account_sender('5211277418228469') == '5211 27** **** 8469'


def test_number_account_recipient():

     assert number_account_recipient('58518872592028002662') == '**2662'
     assert number_account_recipient('20735820461482021315') == '**1315'
     assert number_account_recipient('18889008294666828266') == '**8266'
     assert number_account_recipient('96527012349577388612') == '**8612'
     assert number_account_recipient('35737585785074382265') == '**2265'


def test_accessing_the_dict():
    pass




