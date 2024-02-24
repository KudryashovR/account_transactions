from account_transactions import utils


class OperationMock:
    """Мок класса Operation для тестирования"""

    def __init__(self, id_, date, state, operation_amount, description, to, from_):
        self.id_ = id_
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.to = to
        self.from_ = from_


def test_empty_input():
    """Проверка на пустой список входных данных"""

    assert utils.init_operations([]) == [], "Должен вернуться пустой список"


def test_all_executed_operations(monkeypatch):
    """Проверка на список с операциями в состоянии EXECUTED"""

    operations_json = [
        {"id": 1, "date": "2022-01-01", "state": "EXECUTED", "operationAmount": 100,
         "description": "Test Op 1", "to": "Account1", "from": "Account2"},
        {"id": 2, "date": "2022-02-01", "state": "EXECUTED", "operationAmount": 200,
         "description": "Test Op 2", "to": "Account2", "from": "Account3"},
    ]

    monkeypatch.setattr('account_transactions.operation.Operation', OperationMock)
    result = utils.init_operations(operations_json)

    assert len(result) == 2, "Должны быть обработаны обе операции"

    for item in result:
        assert isinstance(item, OperationMock), "Все элементы должны быть экземплярами мок класса Operation"


def test_no_executed_operations():
    """Проверка списка операций без выполненных"""

    operations_json = [
        {"id": 1, "date": "2022-01-01", "state": "PENDING", "operationAmount": 100,
         "description": "Test Op 1", "to": "Account1", "from": "Account2"},
        {"id": 2, "date": "2022-02-01", "state": "FAILED", "operationAmount": 200,
         "description": "Test Op 2", "to": "Account2", "from": "Account3"},
    ]
    assert utils.init_operations(operations_json) == [], ("Должен вернуться пустой список, так как нет выполненных "
                                                          "операций")


def test_mixed_state_operations(monkeypatch):
    """Проверка списка операций с разными состояниями"""

    operations_json = [
        {"id": 1, "date": "2022-01-01", "state": "PENDING", "operationAmount": 100,
         "description": "Test Op 1", "to": "Account1", "from": "Account2"},
        {"id": 2, "date": "2022-02-01", "state": "EXECUTED", "operationAmount": 200,
         "description": "Test Op 2", "to": "Account2", "from": "Account3"},
    ]

    monkeypatch.setattr('account_transactions.operation.Operation', OperationMock)
    result = utils.init_operations(operations_json)

    assert len(result) == 1, "Должна быть обработана одна выполненная операция"
    assert isinstance(result[0], OperationMock), "Элемент должен быть экземпляром мок класса Operation"
    assert result[0].id_ == 2, "ID обработанной операции должен быть 2"
