# # # Артем Егоров
# # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # //www.youtube.com/c/egoroffchannel
#
# Public, protected, private attributes and methods:
# # # Артем Егоров
# # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # //www.youtube.com/c/egoroffchannel
#
# Public, protected, private attributes and methods:

# THE TASK

# Создайте класс Student, у которого есть:
#
# конструктор __init__, который принимает 3 аргумента и создает приватные атрибуты __name, __age, __branch;
#
# приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде:
#
# Имя: <name>
# Возраст: <age>
# Направление: <branch>
#
# метод access_private_method, который вызывает приватный метод __display_details.
#
# Пример использования кода:
#
# obj = Student("Adam Smith", 25, "Information Technology")
# obj.access_private_method()
#
# #Output
# Имя: Adam Smith
# Возраст: 25
# Направление: Information Technology

class Student:

    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}\n'
              f'Возраст: {self.__age}\n'
              f'Направление: {self.__branch}')


    def access_private_method(self):
        self.__display_details()

obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()


# NEXT TASK

# Создайте класс BankDeposit, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов name, balance и rate:
# владелец депозита, значение депозита и годовая процентная ставка.
#
# приватный метод __calculate_profit, который возвращает количество денег,
# которое получит владелец счета через год с учетом его годовой ставки.
#
# публичный метод get_balance_with_profit, который возвращает общее
# количество средств, которое будет у владельца депозита через год.

class BankDeposit:

    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
        return self.balance*self.rate/100

    def get_balance_with_profit(self):
        return self.balance + self.__calculate_profit()

# a = BankDeposit("John Connor", 1000, 5)
# a.get_balance_with_profit()
# print(dir(BankDeposit))
# print(a._BankDeposit__calculate_profit())

# Ниже код для проверки методов класса BankDeposit
account = BankDeposit("John Connor", 1000, 5)
assert account.name == "John Connor"
assert account.balance == 1000
assert account.rate == 5
assert account._BankDeposit__calculate_profit() == 50.0
assert account.get_balance_with_profit() == 1050.0

account_2 = BankDeposit("Sarah Connor", 200, 27)
assert account_2.name == "Sarah Connor"
assert account_2.balance == 200
assert account_2.rate == 27
assert account_2._BankDeposit__calculate_profit() == 54.0
assert account_2.get_balance_with_profit() == 254.0
print('Good')

# NEXT TASK

# Создайте класс Library, который имеет следующие методы:
#
# метод __init__, который принимает список названий книг и сохраняет его в приватном атрибуте __books.
#
# приватный метод check_availability, который принимает название книги и возвращает True, если книга
# присутствует в библиотеке, в противном случае возвращается False.
#
# публичный метод search_book, который ищет книгу в библиотеке при помощи приватного метода
# check_availability. Возвращает True, если нашел,  иначе False.
#
# публичный метод return_book, который принимает название книги, которую нужно вернуть
# в библиотеку (добавить в конец атрибута __books), ничего возвращать не нужно.
#
# защищенный метод checkout_book, который принимает на вход название книги. Если книга имеется в
# наличии, ее необходимо выдать читателю и удалить из списка книг. Метод в таком случае должен вернуть
# True , как знак того, что операция выдачи книги прошла успешно. Если книга отсутствовала, необходимо вернуть False.

class Library:

    def __init__(self, *args):
        for i in args:
            self.__books = i

    def __check_availability(self, name):
        return name in self.__books

    def search_book(self, name_for_search):
        return self.__check_availability(name_for_search)

    def return_book(self, name_return):
        self.__books.append(name_return)

    def _checkout_book(self, name_check):
        if name_check in self.__books:
            self.__books.remove(name_check)
            return True
        else:
            return False

library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])
assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
assert library.search_book("Moby-Dick") == True
assert library.search_book("Jane Air") == False

assert library._Library__check_availability("War and Peace") == True
assert library._checkout_book("Moby-Dick") == True
assert library._Library__books == ["War and Peace", "Pride and Prejudice"]

assert library.search_book("Moby-Dick") == False
assert library.return_book("Moby-Dick") is None
assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
assert library.search_book("Moby-Dick") == True
print('Good')



# NEXT TASK

# Создайте класс Employee, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов name, __position, __hours_worked и __hourly_rate.
#
# приватный метод calculate_salary, который считает зарплату сотрудника, умножая отработанные часы на часовую оплату.
# Метод должен вернуть посчитанную зарплату.
#
# защищенный метод _set_position, который принимает название должности и изменяет пользователю значение атрибута __position.
#
# публичный метод get_position, который возвращает атрибут __position.
#
# публичный метод get_salary, который возвращает результат вызова приватного метода calculate_salary.
#
# публичный метод get_employee_details, который возвращает информацию о работнике в виде следующий строки
#
# "Name: {name}, Position: {position}, Salary: {salary}"
#
# Здесь значение salary должно рассчитываться при помощи приватного метода calculate_salary.

class Employee:

    def __init__(self, name, position, hours_worked, hourly_rate):
        self.name = name
        self.__position = position
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    def __calculate_salary(self):
        return self.__hourly_rate*self.__hours_worked

    def _set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()

    def get_employee_details(self):
        return (f'Name: {self.name}, Position: {self.__position}, Salary: {self.get_salary()}')


# Ниже код для проверки методов класса Employee
employee = Employee("Джеки Чан", 'manager', 20, 40)
assert employee.name == 'Джеки Чан'
assert employee._Employee__hours_worked == 20
assert employee._Employee__hourly_rate == 40
assert employee._Employee__position == 'manager'
assert employee.get_position() == 'manager'
assert employee.get_salary() == 800
assert employee._Employee__calculate_salary() == 800
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
employee._set_position('Director')
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'

employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
assert employee_2._Employee__calculate_salary() == 1050
assert employee_2.get_employee_details() == 'Name: Пирс Броснан, Position: actor, Salary: 1050'

print('Good')

