import pytest

from account_transactions import utils
from account_transactions import operation


class OperationMock:
    def __init__(self, id_, date, state, operation_amount, description, to, from_=None):
        self.id_ = id_
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.to = to
        self.from_ = from_


@pytest.fixture(autouse=True)
def operation_mock(monkeypatch):
    monkeypatch.setattr(operation, "Operation", OperationMock)


def test_executed_operations():
    """Тестирование с успешно выполненными операциями (с параметром `from`)."""

    operations_json = [
        {"id": 1, "date": "2023-01-01", "state": "EXECUTED",
         "operationAmount": 1000, "description": "Test 1", "to": "Account 1", "from": "Account 2"},
    ]

    result = utils.init_operations(operations_json)
    assert len(result) == 1
    assert result[0].from_ == "Account 2"


def test_executed_operations_without_from():
    """Тестирование выполненных операций без параметра `from`."""

    operations_json = [
        {"id": 2, "date": "2023-01-02", "state": "EXECUTED",
         "operationAmount": 2000, "description": "Test 2", "to": "Account 3"},
    ]

    result = utils.init_operations(operations_json)
    assert len(result) == 1
    assert result[0].from_ is None


def test_invalid_state_operations():
    """Тестирование операции с неверным состоянием (не должны добавляться)."""

    operations_json = [
        {"id": 3, "date": "2023-01-03", "state": "PENDING",
         "operationAmount": 3000, "description": "Test 3", "to": "Account 4"},
    ]

    result = utils.init_operations(operations_json)
    assert len(result) == 0


def test_mixed_operations():
    """Тестирование смешанных операций."""

    operations_json = [
        {"id": 4, "date": "2023-01-04", "state": "EXECUTED",
         "operationAmount": 4000, "description": "Test 4", "to": "Account 5"},
        {"id": 5, "date": "2023-01-05", "state": "PENDING",
         "operationAmount": 5000, "description": "Test 5", "to": "Account 6"},
        {"id": 6, "date": "2023-01-06", "state": "EXECUTED",
         "operationAmount": 6000, "description": "Test 6", "to": "Account 7", "from": "Account 8"}
    ]

    result = utils.init_operations(operations_json)
    assert len(result) == 2
    assert result[0].operation_amount == 4000 and result[1].operation_amount == 6000
    assert result[1].from_ == "Account 8"
