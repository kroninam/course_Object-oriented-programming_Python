## Dunder methods __add__, __mul__, __sub__ и __truediv__
# определяют как именно будут производиться операции +, -, * and /

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'{self.name}, {self.balance}'


    def __add__(self, other):
        print('call __add__method')
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance+other)
        if isinstance(other, BankAccount):
            return self.balance + other.balance

a = BankAccount('Ivan', 200)
print(a+500)

b = BankAccount('Vasja', 100)
print(a+b)

print('###############################################')

class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MyPoint(2 * self.x + other.x, 2 * self.y + other.y)

p1 = MyPoint(3, 4)
p2 = MyPoint(5, 12)
p3 = p1 + p2
print(p3.x + p3.y)

print('###############################################')

#NEXT TASK

# Создайте класс Rectangle, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов width и height: ширина и высота прямоугольника
#
# магический метод __add__, который описывает сложение двух прямоугольников.
# Результатом такого сложения должен быть новый прямоугольник, в котором
# ширина и высота получились в результате сложения исходных прямоугольников.
# Новый прямоугольник нужно вернуть в качестве результата вызова метода __add__.
# Сложения с другими типами данных реализовывать не нужно
#
# магический метод __str__, который возвращает строковое представление  прямоугольника в следующем виде:
# Rectangle({width}x{height})

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width+other.width, self.height+other.height)

    def __str__(self):
        return f'Rectangle({self.width}x{self.height})'


# Ниже код для проверки методов класса Rectangle

r1 = Rectangle(5, 10)
assert r1.width == 5
assert r1.height == 10
print(r1)

r2 = Rectangle(20, 5)
assert r2.width == 20
assert r2.height == 5
print(r2)

r3 = r2 + r1
assert isinstance(r3, Rectangle)
assert r3.width == 25
assert r3.height == 15
print(r3)

# NEXT TASK #####



