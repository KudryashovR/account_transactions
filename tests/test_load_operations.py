import pytest
import json
import os
from account_transactions.utils import load_operations


def create_test_file(filename, content, mode):
    """
    Создаёт тестовый файл с указанным содержимым.
    """

    filepath = os.path.join("data", filename)

    with open(filepath, "w") as file:
        if mode == 1:
            json.dump(content, file)
        else:
            file.write(content)


def delete_test_file(filename):
    """
    Удаляет тестовый файл.
    """

    filepath = os.path.join("data", filename)
    os.remove(filepath)


def test_load_operations_with_valid_data():
    filename = "test_operations.json"
    test_data = {"operation": "test", "value": 123}
    create_test_file(filename, test_data, 1)

    result = load_operations(filename)

    assert result == test_data, "Загруженные данные не совпадают с тестовыми данными"

    delete_test_file(filename)


def test_load_operations_with_nonexistent_file():
    filename = "nonexistent_file.json"

    with pytest.raises(FileNotFoundError):
        load_operations(filename)


def test_load_operations_with_invalid_json():
    filename = "invalid_json.json"
    create_test_file(filename, "{invalid: }", 2)

    with pytest.raises(json.JSONDecodeError):
        load_operations(filename)

    delete_test_file(filename)
