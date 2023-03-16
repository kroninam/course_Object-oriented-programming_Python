# methods __iter__ and __next__

# a = [1,2,3,4,5,6]
#
# b = iter(a)
#
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
#
#
# c = a.__iter__()
# print(c.__next__())
# print(c.__next__())

# итератор строки str:
# d = 'asb'
# f = iter(d)
# print(next(f))


class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

# igor = Student('Igor', 'Nikolaev', [5,4,3,3,4,5,6])
# for i in igor:
#     print(i) - # 'Student' object is not iterable

# По умолчанию итерация происходит по методу __getitem__:
    def __getitem__(self, item):
        return self.name[item]
    # def __getitem__(self, item):
    #     return self.surnamename[item]
    # def __getitem__(self, item):
    #     return self.marks[item]

# igor = Student('Igor', 'Nikolaev', [5,4,3,3,4,5,6])
# for i in igor:
#     print(i) - Поочередно выводятся все буквы имени (item принимает значения от 0 до len(self.name))


# # # Первый вариант итератора:
#     def __iter__(self):
#         print('call_iter')
#         return iter(self.surname)
#
# igor = Student('Igor', 'Nikolaev', [5,4,3,3,4,5,6])
# for i in igor:
#     print(i)

# # # Второй вариант итератора (с next) - где описывается как именно обходить коллекцию:
#     def __iter__(self):
#         print('call_iter')
#         self.index = -1
#         return self
#
#     def __next__(self): # __next__ задает логику получения элементов при итерации
#         if self.index >= len(self.name)-1:
#             raise StopIteration
#         self.index +=1
#         return self.name[self.index]
#
# igor = Student('Igor', 'Nikolaev', [5,4,3,3,4,5,6])
# for i in igor:
#     print(i)

# Оценки можно вынести в отдельный класс Marks (ниже), а итерацию по оценкам запусить в этом классе:

    def __iter__(self):
        print('call_iter')
        return self.marks

    def __next__(self):
        # Этот итератор вообще не вызовется, так как выше в __iter__ идет обращение к self.marks - и переключение на class Marks
        pass

class Marks:

    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('call_iter_from_class_Marks')
        if self.index >= len(self.values)-1:
            raise StopIteration
        self.index +=1
        return self.values[self.index]


m = Marks([5,4,3,3,4,5,6])
igor = Student('Igor', 'Nikolaev', m)
for i in igor:
    print(i)


# THE TASK

# Реализация класса FileReader, который должен при итерирации считывать
# построчно содержимое файла
#
# Задача дописать метод __next__, чтобы он возвращал по порядку строки из файла,
# пока содержимое файла не закончится. Строку нужно очистить слева и справа
# от символов пробелов и переносов на новую строку
#
# Файл для проверки можно скачать здесь:
# https://stepik.org/media/attachments/course/114354/lorem.txt

class FileReader:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self
    def __next__(self):
        line = self.file.readline()

        if line  == '': # сложность была в том, что если проверять само self.file.readline(), то считывается лишняя строка
            print(line.strip())
            raise StopIteration
        return line.strip()


for line in FileReader('lorem.txt'):
    print(line)


# NEXT TASK

# Создайте класс Countdown, который должен принимать начальное значение и
# вести обратный отсчет до нуля, возвращая каждое значение в последовательности
# каждый раз, когда вызывается __next__. Когда обратный отсчет достигает
# нуля, итератор должен вызвать исключение StopIteration.
# Для этого вам понадобиться реализовать:
#
# метод __init__. Он должен принимать одно положительное число - начало отсчета
#
# методы __iter__ и __next__ для итерирования по значениям класса Countdown.


class Countdown:

    def __init__(self, n):
        self.beginning = n

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        iteration = self.beginning - self.index
        self.index +=1
        if iteration < 0:

            raise StopIteration
        return iteration


# for i in Countdown(10):
#     print(i)
# Цикл выше должен печатать следующие числа
# 3
# 2
# 1
# 0

# Ниже код для проверки методов класса Countdown

count = Countdown(2)

assert hasattr(count, '__next__') is True
assert hasattr(count, '__iter__') is True

iterator = iter(count)
assert next(iterator) == 2
assert next(iterator) == 1
assert next(iterator) == 0
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('Элементы итератора Countdown(7)')
for i in Countdown(7):
    print(i)

print('-' * 10)
print('Элементы итератора Countdown(10)')
for i in Countdown(10):
    print(i)


## NEXT TASK
# Создайте класс PowerTwo, который возвращает следующую степень двойки,
# начиная с нулевой степени (2Е0=1). Внутри класса реализуйте:
#
# метод __init__. Он должен принимать одно положительное число
# - степень двойки, до которой нужно итеририроваться включительно
# (см пример ниже)
#
# методы __iter__ и __next__ для итерирования по степеням двойки

# for i in PowerTwo(4): # итерируемся до 4й степени двойки
#     print(i)
#
# # Цикл выше печатает следующие числа
# 1
# 2
# 4
# 8
# 16

class PowerTwo:

    def __init__(self, power):
        self.power = power

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index > self.power:
            raise StopIteration
        return 2**self.index

# for i in PowerTwo(4): # итерируемся до 4й степени двойки
#     print(i)

# Ниже код для проверки методов класса PowerTwo

numbers = PowerTwo(2)

assert hasattr(numbers, '__next__') is True
assert hasattr(numbers, '__iter__') is True

iterator = iter(numbers)
print('Элементы итератора PowerTwo(2)')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('-' * 15)
print('Элементы итератора PowerTwo(20)')
for i in PowerTwo(20):
    print(i)


## NEXT TASK

# Создайте класс InfinityIterator, который реализует бесконечный итератор,
# который  при каждой новой итерации или вызове функции next будет
# возвращать число, увеличенное на 10 от предыдущего значения.
# Начинать нужно с нуля.

class InfinityIterator:

    def __init__(self):
        self.beginning = 0
        self.index = -10

    def __iter__(self):
        return self

    def __next__(self):
        self.index +=10
        return self.beginning + self.index

# a = InfinityIterator()
# for i in a:
#     print(i)


a = iter(InfinityIterator())
print(next(a))
# 0
print(next(a))
# 10
print(next(a))
# 20
print(next(a))
# 30
