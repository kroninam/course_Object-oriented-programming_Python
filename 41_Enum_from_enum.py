## модуль enum класс Enum

#THE TASK

# Создайте перечисление Size, в котором хранятся размеры одежды:
#
# S - small
# M - medium
# L - large
# XL - extra large
# XXL - extra extra large
# В списке сперва указаны названия атрибута, затем его строковое значение
#
# Ваша задача написать только определения класса Size

from enum import Enum

class Size(Enum):
    S = 'small'
    M = 'medium'
    L = 'large'
    XL = 'extra large'
    XXL = 'extra extra large'

print(Size.S.name)


