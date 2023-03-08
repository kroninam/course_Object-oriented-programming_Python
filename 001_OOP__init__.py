# # Instructors
# # Артем Егоров
# # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # //www.youtube.com/c/egoroffchannel
#
# 2.2 Инициализация объекта. Метод init
#
# Создайте класс Vehicle, у которого есть:
#
# Конструктор __init__, принимающий максимальную скорость и пробег.
# Их необходимо сохранить в атрибуты экземпляра max_speed и mileage соответственно.
#
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)# 240 18.

#NEXT TASK

# Перед Василием поставили задачу создать класс Person и реализовать в нем следующие методы:
#
# __init__ метод, который устанавливает значения атрибутов name и age
#
# метод greet, возвращающий строку в следующем формате:
#
# «Hello, my name is [name], and I am [age] years old»
#
# Вот что нашкодил Василий, посмотрите реализацию кода ниже.
# Он не проходит проверки, которые написаны ниже определения класса Person.
# Ваша задача найти ошибки в коде и их исправить/

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = 30
#
#     def greet(self):
#         return f"Hello, my name is {self.name.upper()}, and I am {self.age} years"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}, and I am {self.age} years old"

# NEXT TASK

# Создайте класс Laptop, у которого есть:
#
# конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука.
# На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price
# и также атрибут laptop_name  строковое значение, следующего вида: "<brand> <model>"
#
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price) # выводит 57000
# print(hp.laptop_name) # выводит "hp 15-bw0xx"
# И затем создайте 2 экземпляра класса Laptop и сохраните их в переменные laptop1 и laptop2.


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand +' '+ model

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"

laptop1 = Laptop('dell', 'd2', 100)
laptop2 = Laptop('Lenovo', 'Thinkbook', 200)

#NEXT TASK

# Создайте класс SoccerPlayer, у которого есть:
#
# Конструктор __init__, принимающий 2 аргумента: name, surname.
# Также во время инициализации необходимо создать 2 атрибута экземпляра:
# goals и assists — общее количество голов и передач игрока, изначально
# оба значения должны быть 0.
#
# Метод score, который принимает количество голов, забитых игроком.
# По умолчанию данное значение равно единице. Метод должен увеличить
# общее количество забитых голов игрока на переданное значение.
#
# Метод make_assist, который принимает количество передач, сделанных
# игроком за матч. По умолчанию данное значение равно единице.
# Метод должен увеличить общее количество сделанных передач игроком
# на переданное значение.
#
# Метод statistics, который вывод на экран статистику игрока в виде:
#
# <Фамилия> <Имя> - голы: <goals>, передачи: <assists>.

class SoccerPlayer:
    def __init__(self, name, surname, goals = 0, assists = 0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, goals = 1):
        self.goals += goals

    def make_assist(self, assists = 1):
        self.assists += assists

    def statistics(self):
        print(f'{self.surname + " " + self.name} - голы: {self.goals}, передачи: {self.assists}')

#TESTING:
leo = SoccerPlayer('Leo', 'Messi')
assert isinstance(leo, SoccerPlayer)
assert leo.__dict__ == {'name': 'Leo', 'surname': 'Messi', 'goals': 0, 'assists': 0}
leo.score(700)
assert leo.goals == 700
leo.make_assist(500)
assert leo.assists == 500

leo.statistics()

kokorin = SoccerPlayer('Alex', 'Kokorin')
assert isinstance(kokorin, SoccerPlayer)
assert kokorin.name == 'Alex'
assert kokorin.surname == 'Kokorin'
assert kokorin.assists == 0
assert kokorin.goals == 0
kokorin.score()
assert kokorin.goals == 1
kokorin.score(5)
assert kokorin.goals == 6
kokorin.make_assist()
assert kokorin.assists == 1
kokorin.make_assist(10)
assert kokorin.assists == 11

kokorin.statistics()


obi = SoccerPlayer('Оби-Ван', 'Кеноби')
obi.make_assist()
assert obi.name == 'Оби-Ван'
assert obi.surname == 'Кеноби'
assert obi.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'goals': 0, 'assists': 1}
obi.statistics()

mila = SoccerPlayer('Mila', 'Kunis')
mila.make_assist()
mila.statistics()

#NEXT TASK

# Создайте класс Zebra, внутри которого есть метод which_stripe ,
# который поочередно печатает фразы "Полоска белая", "Полоска черная",
# начиная именно с фразы "Полоска белая"
#
# Пример работы с классом Zebra
#
# z1 = Zebra()
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe() # печатает "Полоска белая"

class Zebra:
    def __init__(self, stripe1 = 'Полоска белая', stripe2 = 'Полоска черная'):
        self.stripe = stripe1

    def which_stripe(self, stripe1 = 'Полоска белая', stripe2 = 'Полоска черная'):
        print(self.stripe)
        if self.stripe == stripe1:
            self.stripe = stripe2
        else:
            self.stripe = stripe1

z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
print('-'*20)
z2 = Zebra()
z2.which_stripe()

#NEXT TASK

# Создайте класс Person, у которого есть:
#
# Конструктор __init__, принимающий имя, фамилию и возраст.
# Их необходимо сохранить в атрибуты экземпляра first_name , last_name, age.
#
# Метод full_name, который возвращает строку в виде "<Фамилия> <Имя>".
#
# Метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return(f'{self.last_name} {self.first_name}')

    def is_adult(self):
        return self.age >= 18


# Ниже код для проверки методов класса Person
p1 = Person('Ash', 'Ketchum', 20)
assert isinstance(p1, Person)
assert p1.full_name() == 'Ketchum Ash'
assert p1.age == 20
assert p1.first_name == 'Ash'
assert p1.last_name == 'Ketchum'
assert p1.is_adult() is True

p2 = Person('Hermione', 'Granger', 16)
assert isinstance(p2, Person)
assert p2.age == 16
assert p2.first_name == 'Hermione'
assert p2.last_name == 'Granger'
assert p2.full_name() == 'Granger Hermione'
assert p2.is_adult() is False
print('Good')