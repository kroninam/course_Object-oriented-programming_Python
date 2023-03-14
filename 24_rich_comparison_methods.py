# # Специальные методы сравнения объектов классов
# rich comparison methods
#
# __ge__ - greater of equal >=
#
# __gt__ - greater than >
#
# __le__ - lower or equal <=
#
# __eq__ - equal ==
#
# __ne__ - not equal !=
#
# __lt__ - lower than <

#THE TASK

# Создайте класс  Fruit, который имеет:
#
# метод __init__, который устанавливает значения атрибутов name и price:
# название и цена фрукта
#
# методы сравнения. Здесь вы сами решаете какие магические методы реализовывать, главное
# чтобы фрукты могли сравниваться с числами и другими фруктами по цене. Смотрите тесты ниже в коде

class Fruit:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
        if isinstance(other, Fruit):
            return self.price > other.price
        elif isinstance(other, (int, float)):
            return self.price > other

    def __eq__(self, other):
        if isinstance(other, Fruit):
            return self.price == other.price
        elif isinstance(other, (int, float)):
            return self.price == other

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        if isinstance(other, Fruit):
            return self.price < other.price
        elif isinstance(other, (int, float)):
            return self.price < other

    def __le__(self, other):
        return self < other or self == other



# Ниже код для проверки методов класса Fruit

apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False

assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')

# NEXT TASK

# Для выражения относительной силы шахматистов используется система рейтингов.
# Наиболее популярная система рейтингов, которая используется Международной
# шахматной федерацией (ФИДЕ), большинством других шахматных федераций и игровых
# шахматных сайтов, является система рейтингов Эло.
#
# В зависимости от выступлений на различных соревнованиях каждому шахматисту
# начисляются баллы в его рейтинг. Давайте с вами реализуем класс ChessPlayer
# и научимся сравнивать рейтинги шахматистов между собой.
#
# И так, ваша задача реализовать класс ChessPlayer, который состоит из:
#
# метода инициализации, принимающего аргументы name, surname, rating;

class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating


# магического  метода __eq__, который будет позволять сравнивать экземпляры класса
# ChessPlayer с числами и другими экземплярами этого класса. Если сравнение происходит
# с целым числом и атрибут rating с ним совпадает, то необходимо вернуть True, в
# противном случае - False. Если же сравнение идет с другим шахматистом(экземпляром
# класса ChessPlayer)  и значения атрибутов rating равны, то возвращается True, в
# противном случае - False. А если же сравнивается с другим типом данных, верните ‘
# Невозможно выполнить сравнение’;

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        elif isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return f'Невозможно выполнить сравнение'
#
# магического  метода __gt__. Если сравнение происходит с целым числом и атрибут rating
# больше его, необходимо вернуть значение True, в противном же случае - False. Если
# сравнение происходит с другим шахматистом(экземпляром класса ChessPlayer) и атрибут
# rating у нашего экземпляра больше, то верните True, в противном случае - False.
# В случае если сравнение идет с остальными типами данных, верните
# ‘Невозможно выполнить сравнение’

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        elif isinstance(other, ChessPlayer):
            return self.rating > other.rating
        else:
            return f'Невозможно выполнить сравнение'

#
# магического  метода __lt__. Если сравнение происходит с целым числом и атрибут
# rating меньше его, необходимо вернуть значение True, в противном же случае - False.
# Если сравнение происходит с другим шахматистом(экземпляром класса ChessPlayer) и
# атрибут rating у нашего экземпляра меньше, то верните True, в противном случае - False.
# В случае если сравнение идет с остальными типами данных, верните
# ‘Невозможно выполнить сравнение’.

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        elif isinstance(other, ChessPlayer):
            return self.rating < other.rating
        else:
            return f'Невозможно выполнить сравнение'

# Ниже код для проверки методов класса ChessPlayer
magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
assert magnus.name == 'Carlsen'
assert magnus.surname == 'Magnus'
assert magnus.rating == 2847
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
assert not magnus == 4000
assert ian == 2789
assert not magnus == ian
assert magnus > ian
assert not magnus < ian
assert (magnus < [1, 2]) == 'Невозможно выполнить сравнение'

v1 = ChessPlayer('Гарри ', 'Каспаров', 10)
v2 = ChessPlayer('Бобби', 'Фишер', 20)
v3 = ChessPlayer('Bot', 'Bot', 20)

assert isinstance(v1, ChessPlayer)
assert isinstance(v2, ChessPlayer)
assert v2.__dict__ == {'name': 'Бобби', 'surname': 'Фишер', 'rating': 20}
assert v1.__dict__ == {'name': 'Гарри ', 'surname': 'Каспаров', 'rating': 10}
assert v1 > 5
assert not v1 > 10
assert not v1 > 11
assert not v1 < 5
assert not v1 < 10
assert v1 < 11
assert not v1 == 5
assert v1 == 10
assert not v1 == 11
assert not v1 > v2
assert not v1 == v2
assert v3 == v2
assert not v3 != v2
assert v1 < v2
assert (v1 > 'fdsfd') == 'Невозможно выполнить сравнение'
assert (v1 < 'fdsfd') == 'Невозможно выполнить сравнение'
assert (v1 == 'fdsfd') == 'Невозможно выполнить сравнение'
assert (v1 == [1, 2]) == 'Невозможно выполнить сравнение'
assert (v1 < [1, 2]) == 'Невозможно выполнить сравнение'
print('Good')

# NEXT TASK

# NOTE:

# total_ordering
# Чтобы не реализовывать все магические методы сравнения,
# можно использовать декоратор functools.total_ordering,
# который позволяет  сократить код, реализовав
# только методы __eq__ и __lt__

# Создайте класс  Rectangle, который имеет:
#
# метод __init__, который устанавливает значения атрибутов width и height: ширина и высота прямоугольника
#
# свойство area, возвращающее площадь прямоугольника
#
# методы сравнения. Здесь вы сами решаете какие магические методы реализовывать,
# главное чтобы прямоугольники могли сравниваться с числами и между собой по значению площади.
# Используйте декоратор  @total_ordering
# Sample Input:

import functools

@functools.total_ordering
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        if isinstance(other, (int, float)):
            return self.area == other

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        if isinstance(other, (int, float)):
            return self.area < other


# Ниже код для проверки методов класса Rectangle

r1 = Rectangle(3, 4)
assert r1.width == 3
assert r1.height == 4
assert r1.area == 12
assert isinstance(type(r1).area, property), 'Вы не создали property area'

assert r1 > 11
assert not r1 > 12
assert r1 >= 12
assert r1 <= 12
assert not r1 > 13
assert not r1 == 13
assert r1 != 13
assert r1 == 12

r2 = Rectangle(2, 6)
assert r1 == r2
assert not r1 != r2
assert not r1 > r2
assert not r1 < r2
assert r1 >= r2
assert r1 <= r2

r3 = Rectangle(5, 2)
assert not r2 == r3
assert r2 != r3
assert r2 > r3
assert not r2 < r3
assert r2 >= r3
assert not r2 <= r3
print('Good')
