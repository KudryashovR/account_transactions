from datetime import datetime


class Operation:
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

    def __repr__(self):
        return (f"Id транзакциии: {self.id_operation}\nИнформация о дате совершения операции: {self.operation_date}\n"
                f"Cтатус перевода: {self.state}\nCумма операции и валюта: {self.operation_amount}\n"
                f"Описание типа перевода: {self.description}\nОткуда: {self.get_operation_from()}\n"
                f"Куда: {self.get_operation_to()}")

    def get_operation_from(self):
        operation_from = self.__operation_from.split()

        if operation_from:
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
