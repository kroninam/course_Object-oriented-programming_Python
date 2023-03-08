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
#
# Создайте класс Employee, который имеет следующие методы:
#
# метод __init__, который устанавливает значения приватных атрибутов __name  и __salary: имя работника и его зарплату.
#
# приватный геттер метод для атрибута __name
#
# приватный геттер метод для атрибута __salary
#
# приватный сеттер метод для атрибута __salary: он должен позволять сохранять в атрибут __salary только положительные числа.
# В остальных случаях не сохраняем переданное значение в сеттер и печатаем на экран сообщение "ErrorValue:<value>".
#
# свойство title, у которого есть только геттер из пункта 2.
#
# свойство reward, у которого геттером будет метод из пункта 3, а сеттером — метод из пункта 4.

class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, value):
        if (type(value) == int or type(value) ==float) and value>=0:
            self.__salary = value
        else:
            print(f'ErrorValue:{value}')

    title = property(fget=__get_name)
    reward = property(fget=__get_salary, fset=__set_salary)

# Ниже код для проверки методов класса Employee
employee = Employee("John Doe", 50000)
assert employee.title == "John Doe"
assert employee._Employee__name == "John Doe"
assert isinstance(employee, Employee)
assert isinstance(type(employee).title, property), 'Вы не создали property title'
assert isinstance(type(employee).reward, property), 'Вы не создали property reward'

assert employee.reward == 50000
employee.reward = -100  # ErrorValue:-100

employee.reward = 1.5
assert employee.reward == 1.5

employee.reward = 70000
assert employee.reward == 70000
employee.reward = 'hello'  # Печатает ErrorValue:hello
employee.reward = '777'  # Печатает ErrorValue:777
employee.reward = [1, 2]  # Печатает ErrorValue:[1, 2]
assert employee.reward == 70000
employee._Employee__set_salary(55000)
assert employee._Employee__get_salary() == 55000

# NEXT TASK

# Создайте класс UserMail, у которого есть:
#
# конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес.
# Их необходимо сохранить в экземпляр, как атрибуты login и __email
# (обратите внимание, защищенный атрибут).
#
# метод геттер get_email, который возвращает защищенный атрибут __email.
#
# метод сеттер set_email, который принимает в виде строки новую почту.
# Метод должен проверять, что в новой почте есть только один символ @ и
# после нее есть точка. Если данные условия выполняются, новая почта сохраняется
# в атрибут __email, в противном случае выведите сообщение "ErrorMail:<почта>".
#
# создайте свойство email, у которого геттером будет метод get_email, а сеттером  метод set_email.

# Напишите определение класса UserMail
class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_mail):
        if '@' in new_mail and new_mail.count('@') == 1 and '.' in new_mail[new_mail.index('@'):]:
            self.__email = new_mail
        else:
            print(f'ErrorMail:{new_mail}')

    email = property(fget=get_email, fset=set_email)

# Ниже код для проверки методов класса UserMail

jim = UserMail("aka47", 'hello@com.org')
assert jim.login == "aka47"
assert jim._UserMail__email == "hello@com.org"
assert isinstance(jim, UserMail)
assert isinstance(type(jim).email, property), 'Вы не создали property email'

jim.email = [1, 2, 3]  # печатает ErrorMail:[1, 2, 3]
jim.email = 'hello@@re.ee'  # печатает ErrorMail:hello@@re.ee
jim.email = 'hello@re.w3'
assert jim.email == 'hello@re.w3'

k = UserMail('belosnezhka', 'prince@wait.you')
assert k.email == 'prince@wait.you'
assert k.login == 'belosnezhka'
assert isinstance(k, UserMail)

k.email = {1, 2, 3}  # печатает ErrorMail:{1, 2, 3}
k.email = 'prince@still@.wait'  # печатает ErrorMail:prince@still@.wait
k.email = 'prince@stillwait'  # печатает ErrorMail:prince@stillwait
k.email = 'prince@still.wait'
assert k.get_email() == 'prince@still.wait'
k.email = 'pri.nce@stillwait'  # печатает ErrorMail:pri.nce@stillwait
assert k.email == 'prince@still.wait'