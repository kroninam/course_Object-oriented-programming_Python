# abstract class and methods

from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def make_sound(self):
        pass

class Cat(AbstractClass):

    def __init__(self, name, age):
        super().__init__(name, age) ### __init__ вообще можно не задавать - см. class Dog ниже

    def make_sound(self):
        print('Meooww')

c = Cat('Blo', 0.5)
print(c.name, c.age)
c.make_sound()

class Dog(AbstractClass):

    def make_sound(self):
        print('RRRR')

d = Dog('Lari', 1)
d.make_sound()


### THE TASK
# # abstract class and methods
#
# # THE TASK
#
# Создайте абстрактный класс Employee, имеющий абстрактный метод calculate_salary().
#
# Реализуйте два класса HourlyEmployee и SalariedEmployee, унаследованные от
# Employee, реализующие метод calculate_salary() для расчета заработной
# платы по часам и окладу соответственно.
#
# Класс HourlyEmployee при инициализации должен создавать атрибуты
# hours_worked и hourly_rate.
#
# Класс SalariedEmployee при инициализации должен создавать только
# атрибут monthly_salary.

from abc import ABC, abstractmethod

class Employee(ABC):


    @abstractmethod
    def calculate_salary(self):
        pass

class HourlyEmployee(Employee):

    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked*self.hourly_rate

class SalariedEmployee(Employee):
    def __init__(self, salary):
        self.monthly_salary = salary

    def calculate_salary(self):
        return self.monthly_salary


# Код для проверки

hourly_employee = HourlyEmployee(100, 25)
assert hourly_employee.hours_worked == 100
assert hourly_employee.hourly_rate == 25
assert hourly_employee.calculate_salary() == 2500

salaried_employee = SalariedEmployee(4000)
assert salaried_employee.monthly_salary == 4000
assert salaried_employee.calculate_salary() == 4000
print('Good')

## NEXT TASK

# abstract class and methods

# Создайте абстрактный класс Database, в котором имеются следующие абстрактные методы:
#
# connect
# disconnect
# execute

from abc import ABC, abstractmethod
from time import sleep

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self):
        pass

# Создайте классы MySQLDatabase и PostgreSQLDatabase, которые будут наследовать
# абстрактный класс Database и реализовывать его абстрактные методы. В каждом классе,
# должны быть реализованы метод connect для подключения к соответствующей базе данных
# и метод disconnect для отключения от базы данных, также метод execute, который
# должен выполнять запрос на соответствующей базе данных.

# Внутри класса MySQLDatabase:
# # Метод connect должен печатать на экран сообщение Connecting to MySQL database...
# # Метод  disconnect должен печатать на экран сообщение Disconnecting from MySQL database...
# # Метод  execute должен принимать запрос к базе данных в виде строки и печатать
# на экран сообщение Executing query '{query}' in MySQL database...

class MySQLDatabase(Database):

    def connect(self):
        sleep(1)
        print('Connecting to MySQL database')

    def disconnect(self):
        print('Disconnecting from MySQL database')

    def execute(self, value):
        self.query = value
        print(f"Executing query '{self.query}' in MySQL database...")


#
# Внутри класса PostgreSQLDatabase:
#
# Метод connect должен печатать на экран сообщение Connecting to PostgreSQL database...
#
# Метод  disconnect должен печатать на экран сообщение Disconnecting from PostgreSQL database...
#
# Метод  execute должен принимать запрос к базе данных в виде строки и печатать
# на экран сообщение Executing query '{query}' in PostgreSQL database...

class PostgreSQLDatabase(Database):

    def connect(self):
        print('Connecting to PostgreSQL database...')

    def disconnect(self):
        print('Disconnecting from PostgreSQL database...')

    def execute(self, value):
        self.query = value
        print(f"Executing query '{self.query}' in PostgreSQL database...")


# Код для проверки

mysql_db = MySQLDatabase()
postgresql_db = PostgreSQLDatabase()

mysql_db.connect()
mysql_db.execute(
    "SELECT * FROM customers;")
mysql_db.disconnect()

postgresql_db.connect()
postgresql_db.execute(
    "SELECT * FROM customers;")
postgresql_db.disconnect()