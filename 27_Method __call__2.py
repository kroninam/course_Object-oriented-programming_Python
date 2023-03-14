## Method __call__

# Квадратичная функция:

# Воссоздадим эту формулу в виде класса QuadraticFunction, в котором есть:
#
# метод __init__. Он должен сохранять в экземпляр класса три атрибута: a , b и c.
#
# метод __call__ , который принимает аргумент x, подставляет его в формулу выше,
# находит значение и возвращает его в качестве результата

class QuadraticFunction:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        y = self.a * x**2 + self.b * x + self.c
        return y

# Ниже код для проверки методов класса QuadraticFunction

f = QuadraticFunction(2, 5, 7)
assert f(1) == 14
assert f(-3) == 10
assert f(2) == 25
assert f(5) == 82

f_2 = QuadraticFunction(-1, 2, 4)
assert f_2(5) == -11
assert f_2(2) == 4
assert f_2(-3) == -11
assert f_2(1) == 5
print('Good')

# NEXT TASK

# Создайте класс Addition, у которого необходимо:
#
# определить метод __call__. Он должен принимать произвольное
# количество аргументов и среди этих аргументов находить числа
# и их суммировать. Все остальные типы данных необходимо пропускать.
# В результате метод __call__ должен вернуть строку в следующем в виде:
#
# Сумма переданных значений = {сумма}

class Addition:

    def __call__(self, *args):
        self.summa = 0
        for i in args:
            if isinstance(i, (int, float)):
                self.summa += i
            else:
                continue
        return (f'Сумма переданных значений = {self.summa}')


# Ниже код для проверки методов класса Addition
add = Addition()
assert add(10, 20) == "Сумма переданных значений = 30"
# assert add(1, 2, 3.4) == "Сумма переданных значений = 6.4"
assert add(1, 2, 'hello', [1, 2], 3) == "Сумма переданных значений = 6"


add2 = Addition()
assert add2(10, 20, 3, 3, 4, 3, 2, 43, 43) == "Сумма переданных значений = 131"
assert add2() == "Сумма переданных значений = 0"
assert add2('hello') == "Сумма переданных значений = 0"

print('Good')


# NEXT EXAMPLE:

#  А поскольку метод __call__ делает экземпляр вызываемым,
#  мы можем использовать его в качестве декоратора.
#
#  Для этого класс-декоратор должен принять функцию в
#  качестве аргумента при его инициализации и сохранить в
#  качестве атрибута экземпляра. И затем при вызове можно
#  обращаться к атрибуту, в котором хранится функция.
#  Вот взгляните на пример реализации класса-декоратора Storage

class Storage:

    def __init__(self, function):
        self.func = function

    def __call__(self):
        print('Хранилище открывается')
        self.func()
        print('Хранилище закрывается')

@Storage
def upl():
    print (f'Загружаются файлы ...')

upl()

## NEXT EXAMPLE

# По предыдущему примеру создайте класс-декоратор Timer.
# Он должен замерять время работы декорируемой функции,
# в качестве примера можете использовать функцию calculate

from time import perf_counter

# a = perf_counter()
# print('hello world')
# b = perf_counter()
# print(b-a)


class Timer:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        start = perf_counter()
        self.function(*args)
        end = perf_counter()
        print(f'Время на выполнение программы {self.function.__name__} : {end - start} секунд.')

@Timer
def factorial(x):
    pr = 1
    for i in range(1, x+1):
        pr *= i
    return pr


@Timer
def calc():
    for i in range(10000000):
        2**100

calc()
factorial(10)








