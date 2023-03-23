# # Пользовательские исключения в Python
# Custom Exceptions
#
# Перед вами имеется часть готового кода. Ваша задача дописать
# функцию get_user: она должна принимать логин пользователя и
# возвращать имя пользователя из словаря users. Если логин
# отсутствует, необходимо возбуждать исключение UserNotFoundError
# с текстом User not found
#
# Также не забудьте реализовать класс-исключение UserNotFoundError
#
# users = {
#     "alice": {"name": "Alice Smith", "email": "alice@example.com"},
#     "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
#     "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
# }
#
#
# def get_user(username):
#     #  напишите реализацию функции
#
# try:
#     username = get_user(input())
# except UserNotFoundError as e:
#     print(e)
# else:
#     print(username)


class UserNotFoundError(Exception):
    '''User not found'''
    def __str__(self):
        return 'User not found'

users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}

def get_user(username):
    if username in users:
        return users[username]['name']
    else:
        raise UserNotFoundError
try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)



# NEXT TASK
# Создайте класс BankAccount, который представляет банковский счет, у которого есть:
#
# метод __init__, принимающий баланс(атрибут balance)
#
# метод deposit для пополнения баланса. Если пользователь пытается
# внести отрицательную сумму на счет, должно возникать исключение
# NegativeDepositError("Нельзя пополнить счет отрицательным значением"):
#
# метод withdraw для вывода денег. Если пользователь пытается снять больше
# денег, чем есть на счете, должно возникать исключение
# InsufficientFundsError("Недостаточно средств для снятия")
#
# Исключения NegativeDepositError и InsufficientFundsError вам также необходимо создать

class NegativeDepositError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, value):
        if value < 0:
            raise NegativeDepositError("Нельзя пополнить счет отрицательным значением")
        else:
            self.balance +=value

    def withdraw(self, value):
        if self.balance < value:
            raise InsufficientFundsError("Недостаточно средств для снятия")
        else:
            self.balance -= value

# Ниже код для проверки

try:
    raise InsufficientFundsError("Недостаточно средств")
except Exception as e:
    if not isinstance(e, InsufficientFundsError):
        raise ValueError('Реализуйте исключение InsufficientFundsError')

try:
    raise NegativeDepositError("Внесено отрицательное значение")
except Exception as e:
    if not isinstance(e, NegativeDepositError):
        raise ValueError('Реализуйте исключение NegativeDepositError')

account = BankAccount(100)
assert account.balance == 100

account.deposit(50)
assert account.balance == 150

account.withdraw(75)
assert account.balance == 75

try:
    account.withdraw(100)
except InsufficientFundsError as e:
    print(e)  # "Недостаточно средств"

assert account.balance == 75

try:
    account.deposit(-50)
except NegativeDepositError as e:
    print(e)  # "Внесено отрицательное значение"



# NEXT TASK

# Нужно реализовать базовым класс исключения PasswordInvalidError,
# который наследуется от стандартного класса исключений Exception.
# Этот класс можно использовать для обработки любых общих ошибок,
# связанных с неверными паролями.
#
# От него нужно унаследовать следующие классы:
#
# PasswordLengthError представляет ошибку, связанную с недостаточной длиной пароля;
#
# PasswordContainUpperError представляет ошибку, связанную с отсутствием заглавных букв в пароле;
#
# PasswordContainDigitError представляет ошибку, связанную с отсутствием цифр в пароле.

class PasswordInvalidError(Exception):
    pass

class PasswordLengthError(PasswordInvalidError):
    pass
class PasswordContainUpperError(PasswordInvalidError):
    pass
class PasswordContainDigitError(PasswordInvalidError):
    pass

# Создайте класс User с атрибутами username и password(пароль по умолчанию None).
# Класс должен иметь метод set_password, который принимает пароль и устанавливает
# его как значение атрибута password. Метод set_password должен также проверять,
# соответствует ли пароль заданным требованиям безопасности:


# Длина пароля должна быть не менее 8 символов (в противном случае
# генерируется исключение PasswordLengthError с текстом Пароль
# должен быть не менее 8 символов);

#
# Пароль должен содержать хотя бы одну заглавную букву (в противном случае
# генерируется исключение PasswordContainUpperError с текстом Пароль должен
# содержать хотя бы одну заглавную букву);
#
# Пароль должен содержать хотя бы одну цифру (в противном
# случае генерируется исключение PasswordContainDigitError
# с текстом Пароль должен содержать хотя бы одну цифру);


class User:
    def __init__(self, username, password = 'None'):
        self.username = username
        self.password = password
    #
    # @property
    # def set_password(self):
    #     return self.password

    # @set_password.setter
    def set_password(self, value):
        if len(value) < 8:
            raise PasswordLengthError ('Пароль должен быть не менее 8 символов')
        x = []
        for i in value:
            if i.isupper():
                x.append(i)
        if len(x) == 0:
            raise PasswordContainUpperError('Пароль должен содержать хотя бы одну заглавную букву')

        y = []
        for i in value:
            if i.isdigit():
                y.append(i)
        if len(y) == 0:
            raise PasswordContainDigitError('Пароль должен содержать хотя бы одну цифру')

        else:
            self.password = value

# Ниже код для проверки


assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'



