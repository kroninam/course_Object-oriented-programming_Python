# Method __bool__

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self): # если нет функции __bool__ - вызывается эта.
        print('call: __len__')
        return self.x - self.y

    # @property
    def __bool__(self):
        print('call: __bool__')
        return self.x != 0 or self.y != 0

p = Point(1,0)
print(p.__bool__())
print(bool(p))

if p:
    print('Hello')

# а если вызов через @property
# print(p.__bool__)

# THE TASK

# # Создайте класс City, у которого есть:
#
# конструктор __init__, принимающий единственный аргумент - название города.
# Вам необходимо сохранить его в качестве атрибута экземпляра name, причем
# вам нужно преобразовать переданное имя города таким образом, чтобы первая
# буква каждого слова была заглавной, а остальные оказались строчными
# (пример "new york" - > "New York")
#
# магический метод __str__ таким образом, чтобы он возвращал имя города
#
# магический метод __bool__ так, чтобы он возвращал False ,если название города
# заканчивается на любую гласную букву латинского алфавита (a, e, i, o, u),
# в противном случае True

class City:

    def __init__(self, name: str):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        vowel = ['a', 'e', 'i', 'o', 'u'] # 'aeiou' это тоже коллекция, не обязательно заводить список.
        if self.name[-1] not in vowel:
            return True
        else:
            return False

# Ниже код для проверки методов класса City

p1 = City('new york')
assert p1.name == "New York"
assert p1.__str__() == "New York"
assert isinstance(p1, City)
print(p1)
assert bool(p1)

p2 = City('SaN frANCISco')
assert isinstance(p2, City)
assert p2.name == "San Francisco"
print(p2)
assert not bool(p2)

p3 = City('NIZHNY NoVGORod')
assert p3.name == "Nizhny Novgorod"
print(p3)
assert bool(p3)
assert isinstance(p3, City)

## NEXT TASK

# Сейчас вам нужно создать класс Quadrilateral(четырехугольник), в котором есть:
#
# метод __init__. Он должен сохранять в экземпляр класса два атрибута: width и height.
# При этом в сам метод __init__ может передаваться один аргумент(тогда в width и
# height присваивать это одно одинаковое значение, тем самым делать квадрат),
# либо два аргумента( первый идет в атрибут width, второй - в height)
#
# метод __str__ , который работает следующим образом:
#
# если width и height одинаковые, возвращать строку «Квадрат размером <width>х<height>»
#
# в противном случае, возвращать строку «Прямоугольник размером <width>х<height>»
#
# переопределить метод __bool__ так, чтобы он возвращал True,
# если объект является квадратом, и False в противном случае

class Quadrilateral:

    def __init__(self, width, height = 0):
        self.width = width
        if height != 0:
            self.height = height
        else:
            self.height = width

    def __str__(self):
        if self.width == self.height:
            return f'Квадрат размером {self.width}х{self.height}'
        else:
            return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height

# Ниже код для проверки методов класса Quadrilateral

q1 = Quadrilateral(10)
print(q1)
assert q1.height == 10
assert q1.width == 10
assert bool(q1) is True
assert q1.__str__() == "Квадрат размером 10х10"
assert isinstance(q1, Quadrilateral)

q2 = Quadrilateral(3, 5)
print(q2)
assert q2.__str__() == "Прямоугольник размером 3х5"
assert bool(q2) is not True
assert isinstance(q2, Quadrilateral)

q3 = Quadrilateral(4, 7)
print(q3)
assert bool(q3) is False
assert q3.__str__() == "Прямоугольник размером 4х7"
assert isinstance(q3, Quadrilateral)
