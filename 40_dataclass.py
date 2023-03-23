# # dataclass
#
# from dataclasses import dataclass
#
# @dataclass
# class Point:
#
#     x: int
#     y: int
#
# point1 = Point(5,7)
# point2 = Point(-10,12)
#
# print(point1)
# print(point2)

# NEXT EXAMPLE

# Создайте датакласс  Location
#
# В нем должны быть описаны следующие атрибуты
#
# name - обязательный, тип строка
# longitude - необязательный, вещественный тип, значение по умолчанию 0
# latitude - необязательный, вещественный тип, значение по умолчанию 11.5
# Создайте ЭК Location со значениями name='Stonehenge', longitude=51,
# latitude=1.5  и сохраните его в переменную stonehenge

from dataclasses import dataclass

@dataclass
class Location:
    name: str
    longitude: int = 0
    latitude: float = 11.5

stonehenge = Location('Stonehenge', 51, 1.5)
print(stonehenge)

