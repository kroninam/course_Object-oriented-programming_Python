# Dunder methods (Double underscore methods)

# What are dunder methods? In Python, dunder methods are methods that allow
# instances of a class to interact with the built-in functions and operators
# of the language. The word “dunder” comes from “double underscore”, because
# the names of dunder methods start and end with two underscores, for example
# __str__ or __add__ .

#THE TASK

# Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
#
# конструктор __init__, принимающий произвольное количество аргументов.
# Среди всех переданных аргументов необходимо оставить только целые числа и
# сохранить их в атрибут values в виде списка;
#
# переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
#
# «Вектор(<value1>, <value2>, <value3>, ...)», если вектор не пустой. При этом значения должны
# быть упорядочены по возрастанию (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);
#
# «Пустой вектор», если наш вектор не хранит в себе значения
#(Первое решение через str.removesuffix - вроде всё работает, но сисетма не принимает).
# class Vector:
#
#     def __init__(self, *args):
#         self.values = []
#         for i in args:
#             if type(i) == int and i >= 0:
#                 self.values.append(i)
#
#     def __str__(self):
#
#         b = ''
#         if len(self.values) > 0:
#             for i in range(len(self.values)):
#                 b += str((sorted(self.values))[i]) + ',' + ' '
#             return f'Вектор({b.removesuffix(", ")})'
#
#         else:
#             return f'Пустой вектор'

# # Ниже код для проверки методов класса Vector
#
# v1 = Vector(1, 2, 3)
# assert isinstance(v1, Vector)
# assert str(v1) == 'Вектор(1, 2, 3)'
#
# v2 = Vector()
# assert isinstance(v2, Vector)
# assert str(v2) == 'Пустой вектор'
#
# v3 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
# assert isinstance(v3, Vector)
# assert sorted(v3.values) == [1, 2, 3]
# assert str(v3) == 'Вектор(1, 2, 3)'
#
# v4 = Vector([4, 5], 'hello')
# assert str(v2) == 'Пустой вектор'
# assert v2.values == []
#
# v5 = Vector(1, 2, True)
# assert isinstance(v5, Vector)
# assert str(v5) == 'Вектор(1, 2)'
#
# print(v1)
# print(v2)
# print(v3)
# print(v4)
# print(v5)

# Следующее решение через tuple(sorted(list)) - системой принято.
class Vector:

    def __init__(self, *args):
        self.values = []
        for i in args:
            if type(i) == int and i >= 0:
                self.values.append(i)

    def __str__(self):

        b = ''
        if len(self.values) > 0:
            return f'Вектор{tuple(sorted(self.values))}'

        else:
            return f'Пустой вектор'

# Ниже код для проверки методов класса Vector

v1 = Vector(1, 2, 3)
assert isinstance(v1, Vector)
assert str(v1) == 'Вектор(1, 2, 3)'

v2 = Vector()
assert isinstance(v2, Vector)
assert str(v2) == 'Пустой вектор'

v3 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
assert isinstance(v3, Vector)
assert sorted(v3.values) == [1, 2, 3]
assert str(v3) == 'Вектор(1, 2, 3)'

v4 = Vector([4, 5], 'hello')
assert str(v2) == 'Пустой вектор'
assert v2.values == []

v5 = Vector(1, 2, True)
assert isinstance(v5, Vector)
assert str(v5) == 'Вектор(1, 2)'

print(v1)
print(v2)
print(v3)
print(v4)

# NEXT TASK
# Давайте определим магические методы __str__ и __repr__ для класса
# GroceryItem, представляющего продуктовый товар:
#
# Создайте класс GroceryItem, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов name,
# price и quantity: название товара, его цену и количество
#
# магический метод __str__, который возвращает строковое представление товара в следующем виде:
# Name: {name}
# Price: {price}
# Quantity: {quantity}
#
# магический метод __repr__, который возвращает однозначное строковое представление объекта
# GroceryItem({name}, {price}, {quantity})

class GroceryItem:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'

    def __repr__(self):
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'

# Ниже код для проверки методов класса GroceryItem
banana = GroceryItem('Banana', 10, 5)
assert banana.__str__() == """Name: Banana
Price: 10
Quantity: 5"""
assert repr(banana) == 'GroceryItem(Banana, 10, 5)'
print(banana)
print(f"{banana!r}")

dragon_fruit = GroceryItem('Dragon fruit', 5, 350)
assert dragon_fruit.__str__() == """Name: Dragon fruit
Price: 5
Quantity: 350"""
assert repr(dragon_fruit) == 'GroceryItem(Dragon fruit, 5, 350)'
print(dragon_fruit)
print(f"{dragon_fruit!r}")

