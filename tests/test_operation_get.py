import pytest

from account_transactions import operation


@pytest.fixture
def set_operation1():
    temp = operation.Operation(441945886, "2019-08-26T10:50:58.294041", "EXECUTED",
                               "31957.58", "Перевод организации",
                               "Maestro 1596837868705199", "Maestro 1596837868705199")
    return temp


@pytest.fixture
def set_operation2():
    temp = operation.Operation(441945886, "2019-08-26T10:50:58.294041", "EXECUTED",
                               "31957.58", "Перевод организации",
                               "Счет 75106830613657916952", "Счет 75106830613657916952")
    return temp


@pytest.fixture
def set_operation3():
    temp = operation.Operation(441945886, "2019-08-26T10:50:58.294041", "EXECUTED",
                               "31957.58", "Перевод организации",
                               "Счет 64686473678894779589")
    return temp


def test_get_operation_from(set_operation1, set_operation2, set_operation3):
    result = set_operation1.get_operation_from()
    test_data = "Maestro 1596 83** **** 5199"

    assert result == test_data

    result = set_operation2.get_operation_from()
    test_data = "Счет **6952"

    assert result == test_data

    result = set_operation3.get_operation_from()
    test_data = ""

    assert result == test_data


def test_get_operation_to(set_operation1, set_operation2, set_operation3):
    result = set_operation1.get_operation_to()
    test_data = "Maestro 1596 83** **** 5199"

    assert result == test_data

    result = set_operation2.get_operation_to()
    test_data = "Счет **6952"

    assert result == test_data
