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

# Создайте класс  Order, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов cart и customer: список покупок и имя покупателя
#
# магический метод __add__, который описывает добавления товара в список покупок.
# Результатом такого сложения должен быть новый заказ, в котором все покупки берутся из
# старого заказа и в конец добавляется новый товар. Покупатель в заказе остается прежним
#
# магический метод __radd__, который описывает добавления товара в список покупок
# при правостороннем сложении. Результатом такого сложения должен быть новый заказ,
# в котором все покупки берутся из старого заказа и в начало списка покупок добавляется
# новый товар. Покупатель в заказе остается прежним
#
# магический метод __sub__, который описывает исключение товара из списка покупок.
# Результатом вычитания должен быть новый заказ
#
# магический метод __rsub__, который описывает исключение товара из списка покупок
# при правостороннем вычитании. Результатом должен быть таким же как и при __sub__
from collections import Counter
class Order:

    def __init__(self, cart, customer):

        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        new_list = [other]
        return Order(self.cart + new_list, self.customer)


    def __radd__(self, other):
        new_list = [other]
        return Order(new_list + self.cart, self.customer)

    def __sub__(self, other):
        new_value = [other]
        c = []
        if other in self.cart:

            for i in self.cart:
                if not (i in new_value):
                    c.append(i)
            return Order(c, self.customer)
        else:
            return Order(self.cart, self.customer)

    def __rsub__(self, other):
        new_value = [other]
        c = []
        if other in self.cart:

            for i in self.cart:
                if not (i in new_value):
                    c.append(i)
            return Order(c, self.customer)
        else:
            return Order(self.cart, self.customer)

# Ниже код для проверки методов класса Order

order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
print(order.cart)


assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')

## NEXT TASK

# Ваша задача создать класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
#
# конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных
# аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде списка.
# Причем значения должны хранится в порядке неубывания. В случае, если целых чисел не передано,
# нужно в атрибут values сохранять пустой список;
#
# переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
# "Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть
# упорядочены по возрастанию; "Пустой вектор", если наш вектор не хранит в себе значения.

class Vector:

    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)
                self.values.sort()

    def __str__(self):
        if len(self.values) > 0:
            ans = ''
            for i in sorted(self.values):
                ans += str(i) + ', '

            return f'Вектор({ans.rstrip(", ")})'
        else:
            return f'Пустой вектор'

# *переопределить метод __add__ так, чтобы экземпляр класса Vector мог складываться
# с целым числом, в результате должен получиться новый Vector, у которого каждый элемент
# атрибута values увеличен на число

# *с другим вектором такой же длины. В результате должен получиться новый Vector,
# состоящий из суммы элементов, расположенных на одинаковых местах.
# Если длины векторов различаются, выведите сообщение
# "Сложение векторов разной длины недопустимо";


# *В случае, если вектор складывается с другим типом(не числом и не вектором),
# нужно вывести сообщение "Вектор нельзя сложить с <значением>".

    def __add__(self, other):
        if isinstance(other, int):
            new_args_1 = []
            for i in self.values:
                new_args_1.append(i + other)
            return Vector(*new_args_1)

        elif isinstance(other, Vector):
            new_args_2 = []
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_args_2.append(self.values[i] + other.values[i])
                return Vector(*new_args_2)

        else:
            print(f'Вектор нельзя сложить с {other}')

# переопределить метод __mul__ так, чтобы экземпляр класса Vector мог умножаться
#
# *на целое число. В результате должен получиться новый Vector, у которого каждый
# элемент атрибута values умножен на переданное число;

#
# *на другой вектор такой же длины. В результате должен получиться новый Vector,
# состоящий из произведения элементов, расположенных на одинаковых местах.
# Если длины векторов различаются, выведите сообщение "Умножение векторов разной длины недопустимо";
#
#
# *В случае, если вектор умножается с другим типом(не числом и не вектором),
# нужны вывести сообщение "Вектор нельзя умножать с <значением>";

    def __mul__(self, other):
        if isinstance(other, int):
            new_args_3 = []
            for i in self.values:
                new_args_3.append(i * other)
            return Vector(*new_args_3)

        elif isinstance(other, Vector):
            new_args_2 = []
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_args_2.append(self.values[i] * other.values[i])
                return Vector(*new_args_2)
            else:
                print(f'Умножение векторов разной длины недопустимо')

        else:
            print(f'Вектор нельзя умножать с {other}')


v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"

v5 = v4+555
print(v5) # печатает "Вектор(9, 11, 13)"


