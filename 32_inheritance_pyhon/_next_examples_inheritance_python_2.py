##############################################################################
# # Наследование от object и от других встроенных типов
##############################################################################
#
# THE TASK

# Создайте класс NewInt, который унаследован от целого типа int,
# то есть мы будем унаследовать поведение целых чисел и значит
# экземплярам нашего класса будут поддерживать те же операции,
# что и целые числа.
#
# Дополнительно в классе NewInt нужно создать:
#
# метод repeat, который принимает одно целое положительное число n (по умолчанию равное 2),
# обозначающее сколько раз нужно продублировать данное число.
# Метод repeat должен возвращать новое число, продублированное n раз (см пример ниже);
#
# метод to_bin, который возвращает двоичное представление числа в виде числа (может пригодиться функция bin)

class NewInt(int):

    def repeat(self, n = 2):
        return int(str(self)*n)

    def to_bin(self):
        return int(str(bin(self)).lstrip('0b'))

a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35


##############################################################################
# 4.3 Переопределение методов в Python overwriting
##############################################################################

class Person:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'Человек идет')

    def breath(self):
        print(f'Человек дышит')

    def talk(self):
        print(f'Человек говорит')

    def __str__(self):
        return f'Person name: {self.name}'

    def combo(self):
        self.walk()
        self.breath()
        self.talk()

class Doctor(Person):

    def walk(self):
        print(f'Доктор идет')

    def breath(self):
        print(f'Доктор дышит')

    def __str__(self):
        return f'Doctor name: {self.name}'

p = Person('Adam')
d = Doctor('John')

print(d.name)
d.breath()
d.talk()
print('*'*15)
print(p)
print(d)
print('*'*15)
print(p.combo())
print('*'*15)
print(d.combo())

######################################################
# Наследование inheritance расширение extending
######################################################

class Person:
    def can_breath(self):
        print(f'Can breath')

    def get_age(self):
        if hasattr(self, 'age'):
            print(self.age)

class Doctor(Person):
    age = 30
    def can_cure(self):
        print(f'Can cure')

p = Person()
d = Doctor()
# p.can_breath()
# d.can_breath() # - отработает из родительского класса
# d.can_cure() # - extending
# p.can_cure # - ошибка

d.get_age() # - выводит возраст доктора, т.к. есть такой атрибут
p.get_age() # - ничего не выводит

#########################################################################
# 4.5 Делегирование в Python Delegating
#########################################################################


# class Person:
#
#     def breath(self):
#         print('Человек дышит')
#
# class Doctor(Person):
#
#     def breath(self):
#         print('Доктор дышит')
#         super().breath()

# p = Person()
# d = Doctor()
#
# p.breath()
# d.breath() # печатает и метод доктора и метод Person пользуясь вызовом super().breath()
#--------------------------------------------------------------#
class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Doctor(Person):

    def __init__(self, name, surname, age): # у доктора дополнительно есть age
        # self.name = name
        # self.surname = surname
        super().__init__(name, surname) # вместо двух строчек выше пользуемся делигированием к род.классу
        self.age = age

p = Person('ivan', 'ivanov')

d = Doctor('petr', 'petrov', 30)

print(p.name, p.surname)
print(d.name, d.surname, d.age)

## THE TASK
# # 4.5 Делегирование в Python
#
# # Создайте базовый класс Person, у которого есть:
#
# конструктор __init__, который должен принимать на вход имя и номер паспорта и записывать их в атрибуты name, passport
#
# метод display, который печатает на экран сообщение «<имя>: <паспорт>»;
#
# Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:
#
# метод  __init__, который принимает именно в таком порядке четыре значения:
# имя, паспорт, зарплату и отдел. Их нужно сохранить в атрибуты  name, passport, salary,department.
# При этом создание атрибутов name, passport необходимо делегировать базовому классу Person.

class Person:

    def __init__(self, name, passport):
        self.name = name
        self.passport = passport

    def display(self):
        print(f'{self.name}: {self.passport}')

class Employee(Person):

    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department


a = Employee('Raul', 886012, 200000, "QA")

a.display()  # печатает "Raul: 886012"


## NEXT TASK

# 4.5 Делегирование в Python
#
# Создайте базовый класс Vehicle, у которого есть:
#
# метод __init__, принимающий название транспортного средства, пробег и вместимость.
# Их необходимо сохранить в атрибуты экземпляра name, mileage и  capacity соответственно
#
# метод fare , который возвращает стоимость проезда из расчета  capacity * 100:
#
# метод display , который печатает строку следующего вида:
# Total <name> fare is: <метод fare>

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity*100

    def display(self):
        print(f'Total {self.name} fare is: {self.fare()}')

#
# Затем создайте подкласс Bus , унаследованный от Vehicle. В нем необходимо:
#
# переопределить метод __init__. Он должен принимать два значения:
# название транспортного средства и пробег. Необходимо делегировать
# создание атрибутов name, mileage и  capacity базовому классу,
# в качестве аргумента передайте capacity  значение 50
#
# переопределить метод fare .
# Он должен получить стоимость проезда у родительского класса и увеличить ее на 10%.

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity=None):
        super().__init__(name, mileage, capacity)
        self.capacity = 50

    def fare(self):
        return super().fare()*1.1

# После создайте подкласс Taxi , унаследованный от Vehicle. В нем необходимо:
#
# переопределить метод __init__. Он должен принимать два значения:
# название транспортного средства и пробег. Необходимо делегировать создание атрибутов name, mileage и
# capacity базовому классу, в качестве аргумента передайте capacity  значение 4
#
# переопределить метод fare . Он должен получить стоимость проезда у родительского класса и увеличить ее на 35%.

class Taxi(Vehicle):

    def __init__(self, name, mileage, capacity=None):
        super().__init__(name, mileage, capacity)
        self.capacity = 4

    def fare(self):
        return super().fare() * 1.35


sc = Vehicle('Scooter', 100, 2)
sc.display()

merc = Bus("Mercedes", 120000)
merc.display()

polo = Taxi("Volkswagen Polo", 15000)
polo.display()



## NEXT TASK

# 4.5 Делегирование в Python
#
# В этой задаче у нас будет один родительский класс Transport и три дочерних класса: Car, Boat, Plane.
#
# В классе Transport должны быть реализованы:
#
# метод __init__, который создает атрибуты brand, max_speed и kind.
# Значения атрибутов brand, max_speed , kind поступают при вызове метода __init__.
# При этом значение kind не является обязательным и по умолчанию имеет значение None;
#
# метод __str__, который будет возвращать строку формата:
# "Тип транспорта <kind> марки <brand> может развить скорость <максимальная скорость> км/ч".
#
class Transport:

    def __init__(self, brand, max_speed, kind = None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return (f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч')

# В классе Car должны быть реализованы:
#
# метод __init__, создающий у экземпляра атрибуты brand, max_speed, mileage и приватный атрибут
# gasoline_residue. Все значения этих атрибутов передаются при вызове класса Car.
# Внутри инициализации делегируйте создание атрибутов brand, max_speed ,
# kind родительскому классу Transport , при этом атрибуту kind передайте значение "Car";
# свойство-геттер gasoline, который будет возвращать строку: "Осталось бензина на <gasoline_residue> км";
# свойство-сеттер gasoline, которое должно принимать ТОЛЬКО целое число value, увеличивает уровень
# топлива gasoline_residue на переданное значение и затем вывести фразу
# 'Объем топлива увеличен на <value> л и составляет <gasoline_residue> л'.
# Если в значение value подается не целое число, вывести 'Ошибка заправки автомобиля'.
#
class Car(Transport):

    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind = Car)
        self.kind = "Car"
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f'Осталось бензина на {self.__gasoline_residue} км'

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue = self.__gasoline_residue + value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print(f'Ошибка заправки автомобиля')
#
# В классе Boat должны быть реализованы:
#
# метод __init__, принимающий три значения brand, max_speed, owners_name.
# Их нужно сохранить в соответствующие атрибуты. При этом внутри инициализации нужно
# делегировать создание атрибутов brand, max_speed , kind родительскому классу Transport ,
# в атрибут kind при этом передайте значение "Boat";
#
# метод __str__, который будет возвращать строку: 'Этой лодкой марки <brand> владеет <owners_name>'.
#

#
class Boat(Transport):

    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind=Transport)
        self.kind = "Boat"
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


# В классе Plane должны быть реализованы:
#
# метод __init__, создающий у экземпляра атрибуты brand, max_speed, capacity.
# Внутри инициализации делегируйте создание атрибутов brand, max_speed , kind
# родительскому классу Transport , при этом атрибуту kind передайте значение "Plane";
#
# метод __str__, который будет возвращать строку: 'Самолет марки <brand> вмещает в себя <capacity> людей'.

class Plane(Transport):

    def __init__(self, brand, max_speed, capacity, kind = "Plane"):
        super().__init__(brand, max_speed)
        self.kind = "Plane"

        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'


transport = Transport('Telega', 10)
print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
bike = Transport('shkolnik', 20, 'bike')
print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч

first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
first_car = Car('BMW', 230, 75000, 300)
print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
print(first_car.gasoline)  # Осталось бензина на 300 км
first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
print(first_car.gasoline)  # Осталось бензина на 320 км
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)  # Этой лодкой марки Yamaha владеет Petr


## NEXT TASK

# 4.5 Делегирование в Python
#
# Давайте представим, что в 2020 году в Москве проводили опрос и выявили,
# к какому классу люди себя относят. По результатам опроса все люди разделились
# на сладкоежек, вегетарианцев и любителей мяса. Давайте напишем программу,
# которая поможет нам подвести итоги опроса. Для создания программы нужно:
#
# Создать родительский класс Initialization, который состоит из:
#
# Метода инициализации, в который поступают аргументы: capacity - целое число,
# food - список из строковых названий еды. Если в значение capacity  передается
# не целое число, вывести надпись ‘Количество людей должно быть целым числом’ и не
# создавать для таких экземпляров атрибуты capacity и food

class Initialization:

    def __init__(self, capacity, food):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print(f'Количество людей должно быть целым числом')
#
# Создать дочерний класс Vegetarian от класса Initialization, который состоит из:
#
# метода инициализации, принимающего аргументы capacity, food. Нужно создать
# одноименные атрибуты через вызов родительского метода __init__.
#
# метода __str__, который возвращает строку формата
# "<capacity> людей предпочитают не есть мясо! Они предпочитают <food>"

class Vegetarian(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)
    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'
#
# Создать дочерний класс MeatEater от класса Initialization, который состоит из:
#
# Метода инициализации, принимающего аргументы capacity, food. Нужно создать
# одноименные атрибуты через вызов родительского метода __init__.
#
# метода __str__, который возвращает строку формата
# "<capacity> мясоедов в Москве! Помимо мяса они едят еще и <food>"
#
class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)
    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'

# Создать дочерний класс SweetTooth от класса Initialization, который состоит из:
#
# метода инициализации, принимающего аргументы capacity, food. Нужно создать
# одноименные атрибуты через вызов родительского метода __init__.
#
# магического метода __str__, который возвращает строку формата
# ‘Сладкоежек в Москве <capacity>. Их самая любимая еда: <food>’;
class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)
    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'
#
# магического  метода __eq__, который будет позволять сравнивать экземпляры класса
# SweetTooth  с числами и другими нашими классами. Если сравнение происходит с целым
# числом и атрибут capacity с ним совпадает, то необходимо вернуть True, в противном
# случае - False. Если же сравнение идет с другим нашим классом(Vegetarian или MeatEater)
# и значения атрибутов capacity равны, то возвращается True, в противном случае - False.
# А если же сравнивается с другим типом данных, верните ‘Невозможно сравнить количество
# сладкоежек с <значение>’;

    def __eq__(self, other):
        if isinstance(other, int):
            if self.capacity == other:
                return True
            else:
                return False
        elif isinstance(other, (Vegetarian, MeatEater)):
            if self.capacity == other.capacity:
                return True
            else:
                return False
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'
#
# магического  метода __lt__. Если сравнение происходит с целым числом и количество
# сладкоежек (атрибут capacity) меньше, необходимо вернуть True, в противном случае -
# False. Если сравнение происходит с экземпляром одного из наших классов Vegetarian или
# MeatEater и сладкоежек меньше, то верните True, в противном случае верните False.
# В случае если сравнение идет с остальными типами данных, верните ‘Невозможно сравнить
# количество сладкоежек с <значение>’

    def __lt__(self, other):
        if isinstance(other, int):
            if self.capacity < other:
                return True
            else:
                return False
        elif isinstance(other, (Vegetarian, MeatEater)):
            if self.capacity < other.capacity:
                return True
            else:
                return False
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'
#
# магического  метода __gt__. Если сравнение происходит с целым числом и количество сладкоежек
# больше, необходимо вернуть значение True, в противном же случае - False. Если сравнение
# происходит с другим нашим классом Vegetarian или MeatEater и сладкоежек больше, то
# верните True, в противном случае - False. В случае если сравнение идет с остальными
# типами данных, верните ‘Невозможно сравнить количество сладкоежек с <значение>’

    def __gt__(self, other):
        if isinstance(other, int):
            if self.capacity > other:
                return True
            else:
                return False
        elif isinstance(other, (Vegetarian, MeatEater)):
            if self.capacity > other.capacity:
                return True
            else:
                return False
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # True
print(30000 == s_first)  # True
print(s_first == 25000)  # False
print(100000 < s_first)  # False
print(100 < s_first)  # True






