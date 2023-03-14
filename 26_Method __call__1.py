## Method __call__


class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0

    def __call__(self, *args, **kwargs):
        self.counter +=1
        self.summa += sum(args) # args передается в виде tuple поэтому можно вызывать sum(args) b len(args)
        self.length += len(args)
        return f'Метод __call__ вызывался {self.counter} раз'

    def average(self):
        return self.summa/self.length

p = Counter()
print(p())
print(p())
d = Counter()

d(1, 2, 3, 8845544)
print(d.average())
print(callable(d))


# Функция таймер без использования @property

from time import perf_counter

# class Time:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         start = perf_counter()
#         print(f'Вызывается функция {self.func.__name__}')
#         result = self.func (*args, **kwargs)
#         end = perf_counter()
#         print (f'Функция отработала за {end - start} секунд')
#         return result
#
# def factorial(x):
#     pr = 1
#     for i in range(1, x+1):
#         pr *= i
#     return pr
#
# t = Time(factorial)
# print(t(7))
#
#
# # Ниже с использованием @property:
# from time import perf_counter
#
# class Time:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         start = perf_counter()
#         print(f'Вызывается функция {self.func.__name__}')
#         result = self.func (*args, **kwargs)
#         end = perf_counter()
#         print (f'Функция отработала за {end - start} секунд')
#         return result
# @Time
# def factorial(x):
#     pr = 1
#     for i in range(1, x+1):
#         pr *= i
#     return pr
#
# print(factorial(5))
#
#
#
#
