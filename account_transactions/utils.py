import os.path
import json

from account_transactions import operation


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


def init_operations(operations_json):
    """
    Создает список выполненных операций на основе входных данных в формате JSON.

    Итерируется по каждому элементу списка operations_json, проверяет состояние каждой операции. Если
    состояние операции указано как 'EXECUTED', пытается создать объект operation.Operation с полным
    набором данных из текущего элемента. Если не удается найти ключ 'from' в данных операции, создает
    объект без этого поля. Операции, состояние которых не равно 'EXECUTED', игнорируются.

    Параметры:
        operations_json (list of dict): список словарей, представляющих данные операций. Ожидается, что каждый
                                        словарь содержит ключи 'id', 'date', 'state', 'operationAmount',
                                        'description', 'to', а также опционально 'from'.

    Возвращает:
        list of operation.Operation: список объектов операций, где каждый объект представляет собой выполненную
                                     операцию с возможным отсутствием информации о поле 'from'.

    Исключения:
        Функция обрабатывает KeyError для каждой операции при попытке доступа к несуществующему ключу 'from',
        но не прерывает выполнение из-за этого исключения, позволяя добавить операцию без этого параметра.
    """

    operations_list = []

    for item in operations_json:
        if item['state'] == 'EXECUTED':
            try:
                operations_list.append(operation.Operation(item['id'], item['date'], item['state'],
                                                           item['operationAmount'], item['description'], item['to'],
                                                           item['from']))
            except KeyError:
                operations_list.append(operation.Operation(item['id'], item['date'], item['state'],
                                                           item['operationAmount'], item['description'], item['to']))

    return operations_list
