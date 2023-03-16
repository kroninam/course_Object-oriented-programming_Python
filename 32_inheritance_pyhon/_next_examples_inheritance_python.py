# THE TASK

# Необходимо написать определение классов, соответствующие условию проверки:
#
# Ваша задача создать следующие пустые классы
# Vehicle
# Car
# Plane
# Boat
# RaceCar


class Vehicle: #parent
    pass

class Car(Vehicle): #subclass
    pass

class Plane(Vehicle): #subclass
    pass
class Boat(Vehicle): #subclass
    pass

class RaceCar(Car): # sub_subclass
    pass

# Ниже располагается код для проверки
vehicle = Vehicle()
car = Car()
plane = Plane()
boat = Boat()
race_car = RaceCar()

assert isinstance(vehicle, Vehicle)
assert isinstance(car, Car)
assert isinstance(plane, Plane)
assert isinstance(boat, Boat)
assert isinstance(race_car, RaceCar)
assert vehicle.__dict__ == {}
assert car.__dict__ == {}

assert issubclass(Car, Vehicle), "Класс Car должен наследоваться от Venicle"
assert issubclass(Plane, Vehicle), "Класс Plane должен наследоваться от Venicle"
assert issubclass(Boat, Vehicle), "Класс Boat должен наследоваться от Venicle"
assert issubclass(RaceCar, Car), "Класс RaceCar должен наследоваться от Venicle"
assert issubclass(RaceCar, Vehicle), "Класс RaceCar должен наследоваться от Venicle"
print('Good')


## NEXT TASK

# Создайте базовый класс Vehicle, у которого есть:
#
# конструктор __init__, принимающий название транспортного средства,
# его максимальную скорость и пробег. Их необходимо сохранить в атрибуты
# экземпляра name, max_speed и mileage соответственно
#
# метод display_info , который печатает информацию в следующем виде:
#
# Vehicle Name: {name}, Speed: {max_speed}, Mileage: {mileage}
#
# Затем создайте подкласс Bus , унаследованный от Vehicle. Оставьте его пустым

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')

class Bus(Vehicle):
    pass

# bus_99 = Bus("Ikarus", 66, 124567)
# bus_99.display_info() #печатает "Vehicle Name: Ikarus, Speed: 66, Mileage: 124567"

# Ниже располагается код для проверки

assert issubclass(Bus, Vehicle)
bus_99 = Bus("Ikarus", 66, 124567)
assert bus_99.name == 'Ikarus'
assert bus_99.max_speed == 66
assert bus_99.mileage == 124567
bus_99.display_info()

modelX = Vehicle('modelX', 240, 18)
assert modelX.__dict__ == {'max_speed': 240, 'mileage': 18, 'name': 'modelX'}
modelX.display_info()

audi = Bus('audi', 123, 43)
assert audi.__dict__ == {'max_speed': 123, 'mileage': 43, 'name': 'audi'}, 'Видимо забыли создать какой-то атрибут'
audi.display_info()


## NEXT TASK

# Создайте базовый класс  Person, у которого есть:
#
# конструктор __init__, который должен принимать на вход имя и записывать его в атрибут name
#
# метод get_name, который возвращает атрибут name;
#
# метод  is_employee, который возвращает  False
#
# Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:
#
# метод  is_employee, который возвращает  True


class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False

class Employee(Person):

    def is_employee(self):
        return True


# emp1 = Person("vasya")
# print(emp1.get_name(), emp1.is_employee())  # vasya False
#
# emp2 = Employee("gena bukin")
# print(emp2.get_name(), emp2.is_employee())  # gena bukin True

# Ниже располагается код для проверки
assert issubclass(Employee, Person)

p = Person("just human")
assert p.name == 'just human'
assert p.get_name() == 'just human'
assert p.is_employee() is False

emp = Employee("Geek")
assert emp.name == 'Geek'
assert emp.get_name() == 'Geek'
assert emp.is_employee() is True
print('Good')