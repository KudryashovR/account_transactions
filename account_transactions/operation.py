from datetime import datetime


class Operation:
    """
    Класс для представления информации о финансовой операции.

    Этот класс содержит всю необходимую информацию о финансовых операциях,
    включая дату операции, статус, сумму и описание. Также предусмотрено форматирование
    номеров счетов и карт для вывода, скрывающее часть информации для конфиденциальности.

    Атрибуты:
        id_operation (int): Идентификатор операции.
        operation_date (str): Дата операции, форматируется в "ДД.ММ.ГГГГ" из строки формата ISO.
        state (str): Статус операции.
        operation_amount (dict): Словарь с суммой операции и информацией о валюте.
                                 Пример: {"amount": 100, "currency": {"name": "RUB"}}
        description (str): Описание операции.
        operation_from (str, optional): Откуда совершена операция (номер карты или счет). По умолчанию None.
        operation_to (str): Куда направлена операция (номер карты или счет).

    Методы:
        __lt__(other): Метод для сравнения объектов по дате. Позволяет использовать операции в сортировках.
        __repr__(): Возвращает представление объекта в виде строки с основной информацией о операции.
        get_operation_from(): Возвращает форматированную строку с информацией, откуда совершена операция,
                              с частичным скрытием номера карты или счета.
        get_operation_to(): Возвращает форматированную строку с информацией, куда направлена операция,
                            с частичным скрытием номера карты или счета.
        get_date(): Возвращает дату операции.
        get_description(): Возвращает описание операции.
        get_operation_amount(): Возвращает строку с суммой операции и названием валюты.

    Пример:
        > operation = Operation(1, "2023-05-12T15:40:00.000", "Выполнена", {"amount": 1000, "currency": {"name":
                                    "RUB"}}, "Перевод денег", "Счет 1234567890123456", "Карта 1234567890123456")
        ...
        > print(operation)
        Id транзакциии: 1
        Информация о дате совершения операции: 12.05.2023
        Cтатус перевода: Выполнена
        Cумма операции и валюта: 1000 RUB
        Описание типа перевода: Перевод денег
        Откуда: Карта 1234 56 **** 3456
        Куда: Счет ****3456
    """

    def __init__(self, id_operation, operation_date, state, operation_amount, description, operation_to,
                 operation_from=None):
        self.id_operation = id_operation

        date_string = operation_date
        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        self.operation_date = datetime.strptime(date_string, date_format).strftime("%d.%m.%Y")
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.__operation_from = operation_from
        self.__operation_to = operation_to

    def __lt__(self, other):
        date1 = datetime.strptime(self.operation_date, "%d.%m.%Y")
        date2 = datetime.strptime(other.operation_date, "%d.%m.%Y")
        return date1 < date2

    def __repr__(self):
        return (f"Id транзакциии: {self.id_operation}\nИнформация о дате совершения операции: {self.operation_date}\n"
                f"Cтатус перевода: {self.state}\nCумма операции и валюта: {self.operation_amount}\n"
                f"Описание типа перевода: {self.description}\nОткуда: {self.get_operation_from()}\n"
                f"Куда: {self.get_operation_to()}")

    def get_operation_from(self):
        if self.__operation_from is not None:
            operation_from = self.__operation_from.split()

            if operation_from[0] != "Счет":
                card_number = operation_from[-1]
                formatted_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
            else:
                bank_account_number = operation_from[-1]
                formatted_number = f"**{bank_account_number[-4:]}"

            operation_from[-1] = formatted_number
            result = " ".join(operation_from)
            return result
        else:
            return ""

    def get_operation_to(self):
        operation_to = self.__operation_to.split()

        if operation_to[0] != "Счет":
            card_number = operation_to[-1]
            formatted_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        else:
            bank_account_number = operation_to[-1]
            formatted_number = f"**{bank_account_number[-4:]}"

        operation_to[-1] = formatted_number
        result = " ".join(operation_to)
        return result

    def get_date(self):
        return self.operation_date

    def get_description(self):
        return self.description

    def get_operation_amount(self):
        amount = self.operation_amount["amount"]
        amount_currency_name = self.operation_amount["currency"]["name"]
        return f"{amount} {amount_currency_name}"
