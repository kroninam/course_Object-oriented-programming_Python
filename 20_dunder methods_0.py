# Dunder methods (Double underscore methods)

# What are dunder methods? In Python, dunder methods are methods that allow
# instances of a class to interact with the built-in functions and operators
# of the language. The word “dunder” comes from “double underscore”, because
# the names of dunder methods start and end with two underscores, for example
# __str__ or __add__ .

class Lion:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'DUNDER_METHOD__REPR__:Object Lion - {self.name}' # how developer see in system

    def __str__(self):
        return f'DUNDER_METHOD__STR__: Object Lion - {self.name}' # how user will see

s = Lion('Simba')
print(s)
print(s.__str__())
print(str(s))
print('#'*25)

print(f'{repr(s)}')
print(f'{s!r}')
print('#'*25)
#########################

# Some practice

# THE TASK

# Создайте класс Person, у которого есть:
#
# конструктор __init__, принимающий 3 аргумента: name, surname, gender.
# Атрибут gender может принимать только 2 значения: "male" и "female", по
# умолчанию "male". Если в атрибут gender передается любое другое значение,
# печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
# и проставить атрибут gender значением "male"

# переопределить метод __str__ следующим образом:
# если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>"
# если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>"

class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender != 'male' and gender != 'female':
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            gender = 'male'
        self.gender = gender

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        elif self.gender == 'female':
            return f'Гражданка {self.surname} {self.name}'


p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3) # печатает "Гражданин Кеноби Оби-Ван"

# Ниже код для проверки методов класса Person
p1 = Person('Chuck', 'Norris')
assert p1.name == 'Chuck'
assert p1.surname == 'Norris'
assert p1.gender == 'male'
assert isinstance(p1, Person)
assert str(p1) == 'Гражданин Norris Chuck'

p2 = Person('Оби-Ван', 'Кеноби', True) #  нужно распечатать предупреждение из условия
assert str(p2) == 'Гражданин Кеноби Оби-Ван'
assert p2.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'gender': 'male'}
assert isinstance(p2, Person)

p3 = Person('Mila', 'Kunis', 'female')
assert isinstance(p3, Person)
assert str(p3) == 'Гражданка Kunis Mila'

print(p1)
print(p2)
print(p3)

print('*'*50)
print('*'*50)
print('*'*50)

# Также работает с setter and getter (но системой ответ не принимается)

class Person:

    def __init__(self, name, surname, gender = 'male'):
        self.name = name
        self.surname = surname
        self.gender = gender

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, new_gender):
        if new_gender == 'male' or new_gender == 'female':
            self.__gender = new_gender
        else:
            print(f'Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.__gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        elif self.gender == 'female':
            return f'Гражданка {self.surname} {self.name}'



p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"

# print(p3.gender)

print(p3) # печатает "Гражданин Кеноби Оби-Ван"

print('*'*50)
print('*'*50)
print('*'*50)

