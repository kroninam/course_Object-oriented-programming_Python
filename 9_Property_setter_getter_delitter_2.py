# # # Артем Егоров
# # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # //www.youtube.com/c/egoroffchannel

# Property, getter, setter and delitter

# THE TASK

# Создайте класс BankAccount, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов _account_number  и _balance: номер счета и баланс
#
# геттер метод для атрибута _account_number
#
# геттер метод для атрибута _balance
#
# сеттер метод для атрибута _balance

class BankAccount:

    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value


# Ниже код для проверки методов класса BankAccount
account = BankAccount("1234567890", 1000)
assert account._balance == 1000
assert account._account_number == "1234567890"
assert account.get_account_number() == "1234567890"
assert account.get_balance() == 1000
account.set_balance(1500)
assert account.get_balance() == 1500

print('Good')

# NEXT TASK
