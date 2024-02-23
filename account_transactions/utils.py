import os.path
import json


def load_operations(filename):
    """
    Загружает и возвращает данные операций из JSON-файла.

    Эта функция считывает данные из файла, расположенного в поддиректории 'data',
    преобразует их из формата JSON и возвращает в виде словаря или списка Python.

    Параметры:
    filename : str
        Имя файла, из которого будут загружены данные. Путь к файлу формируется
        путём добавления поддиректории 'data' перед именем файла.

    Возвращает:
    result : dict или list
        Данные, загруженные из файла и преобразованные из формата JSON. Тип возвращаемого
        значения зависит от структуры данных в исходном JSON-файле.

    Пример использования:
        > data = load_operations("operations.json")
    """

    filepath = os.path.join("data", filename)

    try:
        with open(filepath) as file:
            result = json.loads(file.read())
            return result
    except json.decoder.JSONDecodeError as original_error:
        raise original_error
