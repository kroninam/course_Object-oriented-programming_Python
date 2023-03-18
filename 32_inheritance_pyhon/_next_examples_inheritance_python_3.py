# # Множественное наследование в python
# # Method resolution order __mro__
# Порядок разрешения методов (method resolution order)
# позволяет Питону выяснить, из какого класса-предка
# нужно вызывать метод, если он не обнаружен непосредственно
# в классе-потомке.

# Пример, когда у методов нет доп.параметров кроме self
# class Doctor:
#
#     def can_cure(self):
#         print(f'Doctor can cure')
#
# class Orto:
#     def can_cure(self):
#         print(f'Orto can cure')
#
# class Person(Orto, Doctor):
#     print('Посмотрим')
#     def can_cure(self):
#         Orto.can_cure(self)
#         Doctor.can_cure(self)
#
# p = Person()
# p.can_cure()

# Пример с доп. параметрами:

# class Doctor:
#
#     def __init__(self, degree):
#         self.degree = degree
#
#
# class Orto:
#     def __init__(self, postdegree):
#         self.postdegree = postdegree
#
# class Person(Orto, Doctor):
#
# 
#     def __init__(self, postdegree, degree):
#         # self.degree = degree
#         # self.postdegree = postdegree
#         super().__init__(postdegree)
#         Doctor.__init__(self, degree)
#
#
#     def __str__(self):
#         return f'Person {self.degree}, {self.postdegree}'
#
# p = Person(5, 8)
# print(p)

## THE TASK
# Создайте базовый класс Person, у которого есть:
#
# метод __init__, принимающий имя и возраст человека.
# Их необходимо сохранить в атрибуты экземпляра name и age соответственно
#
# метод display_person_info , который печатает информацию в следующем виде:
# Person: {name}, {age}

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')

# Затем создайте класс Company , у которого есть:
#
# метод __init__, принимающий название компании и город ее основания.
# Их необходимо сохранить в атрибуты экземпляра company_name  и location соответственно
#
# метод display_company_info , который печатает информацию в следующем виде:
# Company: {company_name}, {location}

class Company:

    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location


    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')
#
# И в конце создайте класс Employee , который:
# унаследован от классов Person и Company
#
# имеет метод __init__, принимающий название имя человека, его возраст,
# название компании и город основания. Необходимо делегировать создание атрибутов
# name и age  классу Person , а атрибуты company_name  и location должен
# создать класс Company

class Employee(Person, Company):

    def __init__(self, name, age, company_name, location):
        Person.__init__(self, name, age)
        Company.__init__(self, company_name, location)

# После множественного наследования у экземпляров класса Employee
# будут доступны методы родительских классов

emp = Employee('Jessica', 28, 'Google', 'Atlanta')
emp.display_person_info()
emp.display_company_info()

print(Employee.mro())


## MRO EXAMPLE ##
#
# class A:
#     def a_(self):
#         print('a')
#
# class B:
#     def b_(self):
#         print('b')
#
# class C:
#     def c_(self):
#         print('c')
#
# class D:
#     def d_(self):
#         print('d')
#
# class E(A, B, C, D):
#     def d_(self):
#         print('EEE')
#
# ee = E()
# ee.a_()
# ee.b_()

## Example for mro:

class First(object):
    def __init__(self):
        print("First(): entering")
        super(First, self).__init__()
        print("First(): exiting")


class Second(object):
    def __init__(self):
        print("Second(): entering")
        super(Second, self).__init__()
        print("Second(): exiting")


class Third(Second, First):
    def __init__(self):
        print("Third(): entering")
        Second.__init__(self)
        print("Third(): exiting")


Third()
print(Third.__mro__)