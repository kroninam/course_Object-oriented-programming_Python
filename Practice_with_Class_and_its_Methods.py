# # Instructors
# # Артем Егоров
# # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # //www.youtube.com/c/egoroffchannel

# 2.3 Практика "Создание класса и его методов"

# Создайте класс Dog, у которого есть:

# метод __init__, принимающий имя и возраст собаки и сохраняющий их в аргументы name и age
#
# метод description, который возвращает строку в виде «{name} is {age} years old»
#
# метод speak принимающий один аргумент, который возвращает строку вида «{name} says {sound}»

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        self.sound = sound
        return f'{self.name} says {self.sound}'


# NEXT TASK
# Создайте класс Rectangle, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов width и height
#
# метод area, который возвращает площадь прямоугольника
#
# метод perimeter , который возвращает периметр прямоугольника

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        self.area = self.height * self.width
        return self.area

    def perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter


#NEXT TASK

# В этом задании вам предстоит реализовать свой стек (stack) — это упорядоченная коллекция элементов,
# организованная по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).

# Ваша задача реализовать класс Stack, у которого есть:
#
# метод __init__создаёт новый пустой стек. Параметры данный метод не принимает.
# Создает атрибут экземпляра values, где будут в дальнейшем храниться элементы стека в виде списка (list),
# изначально при инициализации задайте значение атрибуту values, равное пустому списку;
#
# метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает;
#
# метод pop() удаляет верхний элемент из стека. Параметры не требуются, метод возвращает элемент.
# Стек изменяется. Если пытаемся удалить элемент из пустого списка, необходимо вывести сообщение "Empty Stack";
#
# метод peek() возвращает верхний элемент стека, но не удаляет его. Параметры не требуются, стек не модифицируется.
# Если элементов в стеке нет, распечатайте сообщение "Empty Stack", верните None после этого;
#
# метод is_empty() проверяет стек на пустоту. Параметры не требуются, возвращает булево значение.
#
# метод size() возвращает количество элементов в стеке. Параметры не требуются, тип результата — целое число.

# Напишите определение класса Stack
class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.is_empty():
            print("Empty Stack")
        else:
            return self.values.pop()

    def peek(self):
        if self.is_empty():
            print("Empty Stack")
            return None
        else:
            return self.values[-1]

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)


# Ниже код для проверки класса Stack

s = Stack()
assert s.values == []
assert isinstance(s, Stack)

s.peek()  # распечатает 'Empty Stack'
assert s.is_empty() is True
s.push('cat')
assert s.size() == 1
assert s.peek() == 'cat'

s.push('dog')
assert s.size() == 2
assert s.peek() == 'dog'

s.push(True)
assert s.size() == 3
assert s.is_empty() is False

s.push(777)
assert s.size() == 4

assert s.pop() == 777
assert s.size() == 3

assert s.pop() is True
assert s.size() == 2

s.push(123)
s.push(123456)
assert s.peek() == 123456
assert s.size() == 4

assert s.pop() == 123456
assert s.pop() == 123
assert s.pop() == 'dog'
assert s.is_empty() is False
assert s.pop() == 'cat'
assert s.is_empty() is True

d = Stack()
assert d.peek() is None  # Печатает "Empty Stack"
assert d.pop() is None  # Печатает "Empty Stack"
d.push('hello')
assert d.size() == 1
d.push('world')
assert d.size() == 2
assert d.peek() == 'world'
assert d.pop() == 'world'
assert d.peek() == 'hello'

#NEXT TASK

# Создайте класс Worker, у которого есть:
#
# метод __init__, принимающий 4 аргумента:
# имя, зарплата, пол и паспорт. Необходимо сохранить их в следующих атрибутах:
# name, salary, gender и passport.
#
# метод get_info, который распечатает информацию о сотруднике в следующем виде:
# «Worker {name}; passport-{passport}»

# Пример использования класса Worker
# bob = Worker('Bob Moore', 330000, 'M', '1635777202')
# bob.get_info() # печатает "Worker Bob Moore; passport-1635777202"
#
# Ниже имеется список кортежей persons, содержащий информацию о десяти работниках.
# На основании этих данных необходимо создать 10 экземпляров класса Worker и добавить
# их в список  worker_objects. Работников в списке следует разместить в том же порядке,
# в каком они встречаются в списке persons.

persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]
#
# В этом же порядке для каждого объекта в списке worker_objects вызовите метод get_info

class Worker:

    def __init__(self, name, salary, gender, passport):
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        print(f"Worker {self.name}; passport-{self.passport}")

# bob = Worker('Bob Moore', 330000, 'M', '1635777202')
# bob.get_info() # печатает "Worker Bob Moore; passport-1635777202"

worker_objects = []
for i in persons:
    s = Worker(i[0], i[1], i[2], i[3])
    worker_objects.append(s)


for i in worker_objects:
    i.get_info()


# NEXT TASK

# Необходимо создать класс CustomLabel, у которого есть:
#
# метод __init__, принимающий один обязательный аргумент — текст виджета, который необходимо
# сохранить в атрибут text. Также в метод  может поступать произвольное количество именованных аргументов.
# Их необходимо сохранять в атрибуты экземпляра под тем же названием.
#
# метод config, который принимает произвольное количество именованных атрибутов.
# Он должен создать атрибут с указанным именем или, если этот атрибут уже присутствовал в экземпляре,
# изменить его на новое значение
#
# Пример использования:
#
# label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
#
# print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
#
# label.config(color='red', bd=100)
#
# print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}

class CustomLabel:

    def __init__(self, text, **kwargs):
        self.text = text
        # for i,j in kwargs.items():
        #     self.__dict__[i] = j
        self.__dict__.update(kwargs)


    def config(self, **kwargs):
        # for i,j in kwargs.items():
        #     self.__dict__[i] = j
        self.__dict__.update(kwargs)

# Ниже код для проверки методов класса CustomLabel
label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
label2 = CustomLabel(text="Username")
label3 = CustomLabel(text="Password", font=("Comic Sans MS", 24, "bold"), bd=20, bg='#ffaaaa')
label4 = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
label5 = CustomLabel(text="qwwerty", a=20, b='#ffaaaa', r=[3, 4, 5, 6], p=32)

assert label1.__dict__ == {'text': 'Hello Python', 'fg': '#eee', 'bg': '#333'}
assert label2.__dict__ == {'text': 'Username'}
assert label3.__dict__ == {'text': 'Password', 'font': ('Comic Sans MS', 24, 'bold'), 'bd': 20, 'bg': '#ffaaaa'}
assert label4.__dict__ == {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
assert label5.__dict__ == {'text': 'qwwerty', 'a': 20, 'b': '#ffaaaa', 'r': [3, 4, 5, 6], 'p': 32}

print(label1.__dict__)
print(label2.__dict__)
print(label3.__dict__)
print(label4.__dict__)
print(label5.__dict__)

label4.config(color='red', bd=100)
label5.config(color='red', bd=100, a=32, b=432, p=100, z=432)

assert label4.__dict__ == {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
assert label5.__dict__ == {'text': 'qwwerty', 'a': 32, 'b': 432, 'r': [3, 4, 5, 6], 'p': 100,
                           'color': 'red', 'bd': 100, 'z': 432}


# NEXT TASK

# Создайте базовый класс Person, у которого есть:
#
# метод __init__, принимающий имя и возраст человека. Их необходимо сохранить в атрибуты экземпляра nameи age соответственно.
#
# метод display_person_info , который печатает информацию в следующем виде:
# Person: {name}, {age}
#
# Затем создайте класс Company , у которого есть:
#
# метод __init__, принимающий название компании и город ее основания.
# Их необходимо сохранить в атрибуты экземпляра company_name  и location соответственно.
#
# метод display_company_info , который печатает информацию в следующем виде:
# Company: {company_name}, {location}
#
# И в конце создайте класс Employee , который:
#
# имеет метод __init__, принимающий имя человека, его возраст, название компании и город основания.
# Необходимо создать атрибут personal_data и сохранить в него экземпляр класса Person.
# И также создать атрибут work  и сохранить в него экземпляр класса Company.
#
# После этого через атрибуты personal_data и work  вы можете обращаться к методам соответствующих классов Personи Company
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# print(emp.personal_data.name)
# print(emp.personal_data.age)
# emp.personal_data.display_person_info()
# print(emp.work.company_name)
# print(emp.work.location)
# emp.work.display_company_info()


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Person {self.name}, {self.age}")


class Company:

    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f"Company {self.company_name}, {self.location}")

class Employee:

    def __init__(self, name, age, name_company, location):
        self.personal_data = Person(name, age)
        self.work = Company(name_company, location)

emp = Employee('Jessica', 28, 'Google', 'Atlanta')
print(emp.personal_data.name)
print(emp.personal_data.age)
emp.personal_data.display_person_info()
print(emp.work.company_name)
print(emp.work.location)
emp.work.display_company_info()

# NEXT TASK


