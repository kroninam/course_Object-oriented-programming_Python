################################
# __slots__

# class Point:
#
#     def __init__(self,x, y):
#         self.x = x
#         self.y = y
#
# # p1 = Point(3, 5)
# # print(p1.__dict__)
# # p1.z = 100
# # print(p1.__dict__)
#
# class SlotsPoint:
#
#     __slots__ = ('x', 'y', 'z') # Перечисляем все возможные атрибуты экземпляров класса
#
#     def __init__(self,x, y):
#         self.x = x
#         self.y = y
#
# # p2 = SlotsPoint(3, 5)
# # # print(p2.__dict__) # 'SlotsPoint' object has no attribute '__dict__'
# # p2.z = 200
# # print(p2.x, p2.y)
#
# ##################################
# # Проверка занимаемого места в памяти:
#
# p1 = Point(3, 5)
# p2 = SlotsPoint(3,5)
#
# print(p1.__sizeof__(), p1.__dict__.__sizeof__())
# print(p2.__sizeof__(), p2.__slots__.__sizeof__()) # а здесь словаря-довеска нет.
# ###############################################################
#
# # Проверка быстродейтвия
# from timeit import timeit
#
# def time_p1():
#     p1 = Point(3, 5)
#     p1.x = 2
#     p1.y = 50
#     p1.x
#
#     del p1.y
#
#
# def time_p2():
#     p2 = SlotsPoint(3, 5)
#     p2.x = 2
#     p2.y = 50
#     p2.x
#     del p2.y
#
# print(timeit(time_p1))
# print(timeit(time_p2))


# THE TASK

# Создайте класс с именем Person , экземпляры которого имеют следующие атрибуты:
#
# first_name хранит имя человека в виде строки;
# last_name строка, хранит фамилию человека в виде строки;
# age хранит возраст человека в виде целого числа.
#
# Переопределите также метод __str__ так, чтобы он возвращал строку
# {Имя} {Фамилия} is {Возраст} years old
#
# Используйте атрибут __slots__ для указания атрибутов, чтобы каждый экземпляр
# класса использовал только память, необходимую для хранения перечисленных атрибутов.

class Person:

    __slots__ = ('first_name', 'last_name', 'age')

    def __init__(self, name, surname, age):
        self.first_name = name
        self.last_name = surname
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'

# Код ниже не удаляйте, он нужен для проверок
arshavin = Person("Andrew", "Arshavin", 35)
assert arshavin.first_name == 'Andrew'
assert arshavin.last_name == 'Arshavin'
assert arshavin.age == 35
print(arshavin)

mg = Person("Max", "Galkin", 44)
assert mg.first_name == 'Max'
assert mg.last_name == 'Galkin'
assert mg.age == 44
print(mg)

try:
    arshavin.city = 'SPB'
except AttributeError:
    print('Нельзя создавать новые атрибуты')


# Slots: свойства(property) и наследования
#
#
# class Rectangle:
#
#     __slots__ = ('width', 'height')
#
#     def __init__(self, a, b):
#         self.width = a
#         self.height = b
#
# # r = Rectangle(10, 20)
# # print(r.__slots__)
#
#     @property
#     def perimetr(self):
#         return (self.height + self.width)*2
#
#     @property
#     def area(self):
#         return (self.height * self.width)
#
# r = Rectangle(10, 20)
# print(r.perimetr, r.area)

# ##########################################################
# # Задаем значения переменных через сеттер:
# class Rectangle:
#
#     __slots__ = ('__width', 'height')
#
#     def __init__(self, a, b):
#         self.width = a
#         self.height = b
#
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         print('setter was called')
#         self.__width = value
#         return
# r5 = Rectangle(5, 7)
# #############################################################

# наследование __slots__:

class Rectangle:

    __slots__ = ('width', 'height')

    def __init__(self, a, b):
        self.width = a
        self.height = b

class Square(Rectangle):

    # __slots__ = tuple() - # таким образом наследуется весь __slot__ от родителя
    __slots__ = ('color') # - таким образом __slot__ родителя расширяется.

    def __init__(self, a, b, color):
       # super().__init__(a,b)
       Rectangle.__init__(self, a, b)

s = Square(5, 6, 'red')