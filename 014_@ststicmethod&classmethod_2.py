# # # # Артем Егоров
# # # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # # //www.youtube.com/c/egoroffchannel

# staticmethod & classmethod
# TASKS

#
# Создайте класс TemperatureConverter, который имеет следующие методы:
#
# статический метод celsius_to_fahrenheit, который принимает температуру в градусах
# Цельсия и переводит ее в градусы по Фаренгейту: t_c*(9/5)+32
#
# статический метод fahrenheit_to_celsius, который принимает температуру в градусах
# по Фаренгейту и переводит ее в градусы по Цельсия: (t_f-32)*(5/9)

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(t_c):
        return t_c*(9/5)+32

    @staticmethod
    def fahrenheit_to_celsius(t_f):
        return (t_f-32)*(5/9)

# Ниже код для проверки методов класса TemperatureConverter
assert TemperatureConverter.celsius_to_fahrenheit(0) == 32.0
assert TemperatureConverter.celsius_to_fahrenheit(10) == 50.0
assert TemperatureConverter.celsius_to_fahrenheit(15) == 59.0
assert TemperatureConverter.celsius_to_fahrenheit(20) == 68.0
assert TemperatureConverter.celsius_to_fahrenheit(25) == 77.0
assert TemperatureConverter.celsius_to_fahrenheit(30) == 86.0

assert TemperatureConverter.fahrenheit_to_celsius(86) == 30.0
assert TemperatureConverter.fahrenheit_to_celsius(77) == 25.0
assert TemperatureConverter.fahrenheit_to_celsius(68) == 20.0
assert TemperatureConverter.fahrenheit_to_celsius(59) == 15.0
assert TemperatureConverter.fahrenheit_to_celsius(50) == 10.0
assert TemperatureConverter.fahrenheit_to_celsius(32) == 0
print('Good')


# NEXT TASK

# @classmethod - Factory method - с помощью @classmethod задаётся необходимый цвет для всего класса

class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    @classmethod
    def get_red_car(cls, model):
        return cls(model, 'red')

car1 = Car('bmw', 'black')
print(car1.model, car1.color)

car2 = Car.get_red_car('Audi')
print(car2.model, car2.color)

car3 = Car.get_red_car('Lada')
print(car3.model, car3.color)


# NEW TASK

# Перед вами имеется реализация класса Circle. Ваша задача добавить в него следующее:
#

# статик-метод is_positive, принимающий одно число.
# Метод is_positive должен возвращать ответ является ли переданное число положительным

# класс-метод from_diameter, принимающий диаметр круга.
# Метод from_diameter должен возвращать новый экземпляр класса Circle
# (учитывайте, что экземпляры круга создаются по радиусу);
#
#
# статик-метод area, который принимает радиус и возвращает площадь круга. Для этого воспользуйтесь формулой
# 2*pi*r^22∗pi∗r 2  и в качестве значения pi возьмите 3.14

class Circle:
    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @staticmethod
    def is_positive(radius):
        return radius >=0

    @classmethod
    def from_diameter(cls, d):
        return cls(d/2)

    @staticmethod
    def area(radius):
        return 2*3.14*radius**2

# код ниже не нужно удалять, в нем находятся проверки
circle_1 = Circle.from_diameter(10)
assert isinstance(circle_1, Circle)
assert circle_1.radius == 5.0
print(f"circle_1.radius={circle_1.radius}")
assert Circle.is_positive(10)
assert not Circle.is_positive(-5)
assert Circle.area(1) == 6.28


