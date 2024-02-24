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
    Формирует список выполненных операций из предоставленных данных в формате JSON.

    Функция проходит по каждой операции в исходном списке JSON. Если операция имеет статус 'EXECUTED',
    функция пытается создать объект операции с использованием всех доступных данных. В случае, если
    данные операции не содержат ключ 'from', операция добавляется в список без этого параметра.
    Операции, не имеющие статус 'EXECUTED', игнорируются.

    Параметры:
        operations_json (list of dict): Входной список словарей, где каждый словарь представляет собой
                                        операцию. Ожидается, что каждая операция содержит ключи 'id',
                                        'date', 'state', 'operationAmount', 'description', 'to', и
                                        опционально 'from'.

    Возвращает:
        list: Список объектов операций, где каждый объект операции представляет выполненную операцию,
              включенную в исходные данные. Объекты создаются даже если отсутствует информация о
              отправителе ('from').

    Исключения:
        В процессе обработки каждой операции функция ловит исключения KeyError для случая отсутствия
        ключа 'from'. Если отсутствует любой другой ключ, исключение не обрабатывается и должно
        быть отловлено на более высоком уровне.
    """

    operations_list = []

    for item in operations_json:
        try:
            if item['state'] == 'EXECUTED':
                operations_list.append(operation.Operation(item['id'], item['date'], item['state'],
                                                           item['operationAmount'], item['description'], item['to'],
                                                           item['from']))
        except KeyError as err:
            if err.args[0] == 'from':
                operations_list.append(operation.Operation(item['id'], item['date'], item['state'],
                                                           item['operationAmount'], item['description'], item['to']))

    return operations_list


def print_operations(operations_list):
    """
    Печатает информацию о последних пяти операциях из предоставленного списка.

    Для каждой из последних пяти операций в списке operations_list, функция выводит следующую информацию:
    - дата перевода,
    - описание перевода,
    - откуда,
    - куда,
    - сумма перевода и валюту.
    Все данные выводятся в четко структурированном текстовом формате.

    Параметры:
        operations_list (list): Список, содержащий объекты операций. Ожидается, что каждый объект операции
                                имеет методы get_date(), get_description(), get_operation_from(),
                                get_operation_to() и get_operation_amount(), возвращающие соответствующие
                                атрибуты операции.

    Возвращает:
        None: Функция ничего не возвращает; все данные выводятся в стандартный поток вывода.

    Примеры использования:
        Предположим, что operations_list содержит объекты операций с необходимыми атрибутами.
        > вывод_последних_операций(operations_list)
        2023-01-25 Покупка в интернет-магазине
        Счет Ивана -> Счет интернет-магазина
        5000

        ...

    Примечание:
        - Функция предназначена для вывода информации о последних пяти операциях. Если операций в списке
          менее пяти, будет выведена информация только о существующих операциях.
        - Ожидается, что каждый объект в списке имеет необходимые методы для извлечения информации.
    """

    for step in range(-5, 0):
        operation_ = operations_list[step]

        print(f"{operation_.get_date()} {operation_.get_description()}\n{operation_.get_operation_from()} -> "
              f"{operation_.get_operation_to()}\n{operation_.get_operation_amount()}\n")
