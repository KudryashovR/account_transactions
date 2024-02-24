import pytest
from account_transactions import operation


@pytest.fixture
def set_operation1():
    temp = operation.Operation(441945886, "2019-08-26T10:50:58.294041", "EXECUTED",
                               {"amount": 100, "currency": {"name": "USD", "code": "USD"}},
                               "Перевод организации", "Maestro 1596837868705199",
                               "Maestro 1596837868705199")
    return temp


@pytest.fixture
def set_operation2():
    temp = operation.Operation(441945886, "2020-08-26T10:50:58.294041", "EXECUTED",
                               {"amount": 100, "currency": {"name": "USD", "code": "USD"}},
                               "Перевод организации", "Maestro 1596837868705199",
                               "Maestro 1596837868705199")
    return temp


def test_get_operation_amount(set_operation1):
    test_data = "100 USD"

    assert set_operation1.get_operation_amount() == test_data


def test_lt(set_operation1, set_operation2):
    test_data = True

    assert set_operation1.__lt__(set_operation2) == test_data


def test_get_date(set_operation1):
    test_data = "26.08.2019"

    assert set_operation1.get_date() == test_data


def test_get_description(set_operation1):
    test_data = "Перевод организации"

    assert set_operation1.get_description() == test_data
