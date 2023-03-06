# Instructors
# Артем Егоров
# Автор и бессменный ведущий образовательного канала по разработке на Python https:
# //www.youtube.com/c/egoroffchannel

# 2.1 Методы экземпляра. Аргумент self
# Создайте класс Lion. В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!"
# Необходимо написать только определение класса
# Пример работы с классом Lion
# simba = Lion()
# simba.roar() # печатает Rrrrrrr!!!

class Lion:
    sound = 'Rrrrrrr!!!'
    def roar(self):
        print(self.sound)
simba = Lion()
simba.roar()

# vs (without slef argument)

class Lion:
    sound = 'Rrrrrrr!!!'
    def roar():
        print(Lion.sound)
Lion.roar()

# Создайте класс Robot, в котором реализованы:
#
# Метод say_hello , печатающий на экран фразу «Hello, human! My name is C-3PO»
# Метод say_bye ,  печатающий на экран фразу «See u later alligator»
#
# После определения класса создайте 2 экземпляра и сохраните их в переменные  c3po и r2d2
# Затем вызовите у переменной  c3po  метод say_hello , а затем метод say_bye
# И то же самое сделайте с переменной r2d2:  вызовите метод say_hello , потом — метод say_bye.

class Robot:
    name = 'C-3PO'

    def say_hello(self):
        print(f'Hello, human! My name is {self.name}')

    def say_bye(self):
        print('See u later alligator')

c3po = Robot()
r2d2 = Robot()

c3po.say_hello()
c3po.say_bye()

r2d2.say_hello()
r2d2.say_bye()

# NEXT TASK

# В предыдущей задаче вы могли обратить внимание на то, что выводится
# всегда одно и то же имя робота в методе say_hello . Давайте это исправим
# при помощи атрибута экземпляра name . Для этого переопределяем класс Robot,
# в котором должны быть реализованы:
#
# Метод set_name , принимающий имя робота и сохраняющий его в атрибуте экземпляра name
#
# Метод say_hello . Метод должен проверить, есть ли у ЭК атрибут name . Если атрибут name
# присутствует, необходимо напечатать фразу «Hello, human! My name is <name>». Если атрибут
# name  отсутствует у экземпляра, печатайте сообщение «У робота нет имени»
#
# Метод say_bye ,  печатающий на экран фразу «See u later alligator»
#
# Пример работы с классом Robot
#
# c3po = Robot()
# c3po.say_hello() # печатает У робота нет имени
# c3po.set_name('R2D2')
# c3po.say_hello() # печатает Hello, human! My name is R2D2
# c3po.say_bye() # печатает See u later alligator
#
# r = Robot()
# r.set_name('Chappy')
# r.say_hello()# печатает Hello, human! My name is Chappy

class Robot:

    def set_name(self, value):
        self.name = value

    def say_hello(self):
        #print(f'Hello, human! My name is {self.name}')

        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')

a = Robot()
a.set_name('rrr12')
a.say_hello()
a.say_bye()

#NEXT TASK

# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
#
# В классе Counter нужно определить:
#
# Метод start_from, который принимает один необязательный аргумент.
# Значение, с которого начинается подсчет, по умолчанию равно 0.
#
# Метод increment, который увеличивает счетчик на 1.
#
# Метод display, который печатает фразу "Текущее значение счетчика = <value>".
#
# Метод reset,  который обнуляет накопившееся значение счетчика.
#
# Пример работы с классом Counter
#
# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display() # печатает "Текущее значение счетчика = 0"
#
# c2 = Counter()
# c2.start_from(3)
# c2.display() # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display() # печатает "Текущее значение счетчика = 4"

class Counter:
    start = 0

    def start_from(self, value=0):
        self.start = value

    def increment(self):
        self.start +=1

    def display(self):
        print(f'Текущее значение счетчика = {self.start}')

    def reset(self):
        self.start = 0


c1 = Counter()
c1.start_from()
c1.increment()
c1.display() # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display() # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display() # печатает "Текущее значение счетчика = 0"
c2 = Counter()
c2.start_from(3)
c2.display() # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display() # печатает "Текущее значение счетчика = 4"

#NEXT TASK

# Создайте класс Constructor, в котором реализованы:
#
# Метод add_atribute , принимающий на вход название атрибута
# в виде строки и его значение. При помощи функции setattr необходимо
# создать или изменить атрибут для ЭК, у которого этот метод был вызван.
#
# Метод display ,  печатающий на экран словарь __dict__ у ЭК.
#
# Пример работы с классом Constructor
#
# obj1 = Constructor()
# obj1.display() # печатает {}
# obj1.add_atribute('color', 'red')
# obj1.add_atribute('width', 20)
# obj1.display() # печатает {'color': 'red', 'width': 20}
#
# obj2 = Constructor()
# obj2.display() # печатает {}
# obj2.add_atribute('height', 100)
# obj2.display() # печатает {'height': 100}

class Constructor:
    def add_atribute(self, name, val):
        setattr(self, name, val)
    def display(self):
        print(self.__dict__)

obj1 = Constructor()
obj1.add_atribute('color', 'red')
obj1 = Constructor()
obj1.display() # печатает {}
obj1.add_atribute('color', 'red')
obj1.add_atribute('width', 20)
obj1.display() # печатает {'color': 'red', 'width': 20}
obj2 = Constructor()
obj2.display() # печатает {}
obj2.add_atribute('height', 100)
obj2.display() # печатает {'height': 100}

#NEXT TASK

# Создайте класс Point. У этого класса должны быть:
#
# Метод set_coordinates, который принимает координаты точки
# на плоскости и сохраняет их в экземпляр класса в атрибуты x и y
#
# Метод get_distance, который обязательно принимает экземпляр класса Point
# и возвращает расстояние между двумя точками по теореме Пифагора. В случае,
# если в данный метод передается не экземпляр класса Point, необходимо
# вывести сообщение "Передана не точка".

# Пример работы с классом Point
#
# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2) # вернёт 5.0
# p1.get_distance(10) # Распечатает "Передана не точка"
from math import sqrt
class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, p):
        if hasattr(p, 'x' and 'y'):
            self.d = sqrt(((p.x - self.x)**2) + ((p.y-self.y)**2))
            print(self.d)
        else:
            print('Передана не точка')

# Пример работы с классом Point
p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
p1.get_distance(10) # Распечатает "Передана не точка"