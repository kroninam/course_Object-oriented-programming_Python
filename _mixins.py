# Миксины (от английского слова «mixins», обозначающего примеси)
#

# # FIRST example mixin
#
# class Mixin:
#
#     def say_mixin(self):
#         print('I am mixin')
#
#
# class Some(Mixin):
#
#     def say_hello(self):
#         print('hello')
#         self.say_mixin()
#
# s = Some()
# s.say_hello()
# # s.say_mixin()

## SECOND example mixin


class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def breath(self):
        print(f'{self.species} по имени {self.name} умеет дышать')

    def walk(self):
        print(f'{self.species} по имени {self.name} умеет ходить')

class Cat(Animal):

    def __init__(self, name, breed):
        super().__init__(name, 'cat') # здесь self писать не надо
        # Animal.__init__(self, name, species) # а здесь надо писать self при таком вызове
        self.breed = breed


    def say_cat(self):
        print('Meow')


class Dog(Animal):

    def __init__(self, name, color):
        super().__init__(name, 'dog')
        self.color = color

    def say_dog(self):
        print('rrr')

# c = Cat('blo-blo', 'blo')
# c.say_cat()
# c.breath()
# c.walk()
#
# d = Dog('lari', 'sob')
# d.say_dog()
# d.breath()
# d.walk()

# У классов Dog и Cat свои собстевнне методы и конфликта нет.

# Но теперь мы создаем двух животных с одинаковм методом can_fly

# class Bat(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'bat')
#
#     def can_fly(self):
#         print(f'{self.name} умеет летать')
#
#
# # b = Bat('batty')
# # b.walk()
# # b.breath()
# # b.can_fly()
#
# class FlyingSquirrel(Animal):
#     def __init__(self, name):
#         super().__init__(name, 'squirrel')
#
#     def can_fly(self):
#         print(f'{self.name} умеет летать')

# s = FlyingSquirrel('Squirrel')
# s.walk()
# s.breath()
# s.can_fly()
###################################################################################
# Можно создать промежуточный класс FlyngAnimal и наследоваться от него:

# class FlyingAnimal(Animal):
#
#     def can_fly(self):
#         print(f'{self.name} can fly')
#
#
# class Bat(FlyingAnimal):
#     def __init__(self, name):
#         super().__init__(name, 'bat')
#     #
#     # def can_fly(self):
#     #     print(f'{self.name} умеет летать')
#
#
# class FlyingSquirrel(FlyingAnimal):
#     def __init__(self, name):
#         super().__init__(name, 'squirrel')
#     #
#     # def can_fly(self):
#     #     print(f'{self.name} умеет летать')
#
#
# b = Bat('batty')
# b.walk()
# b.breath()
# b.can_fly()
#
# s = FlyingSquirrel('Squirrel')
# s.walk()
# s.breath()
# s.can_fly()

######################################################################
# И есть другой способ примешать (mixin) новое свойство:

class FlyMixin:
    def can_fly(self):
        print(f'Это {self.species} по имени {self.name} и оно умеет летать')


class Bat(Animal, FlyMixin):
    def __init__(self, name):
        super().__init__(name, 'bat')

    # def can_fly(self):
    #     print(f'{self.name} умеет летать')

class FlyingSquirrel(Animal, FlyMixin):
    def __init__(self, name):
        super().__init__(name, 'squirrel')
    #
    # def can_fly(self):
    #     print(f'{self.name} умеет летать')



# b = Bat('batty')
# b.walk()
# b.breath()
# b.can_fly()
# s = FlyingSquirrel('Squirrel')
# s.walk()
# s.breath()
# s.can_fly()


class F_Dog(Animal, FlyMixin):

    def __init__(self, name, color):
        super().__init__(name, 'dog')
        self.color = color

    def say_dog(self):
        print('rrr')

f_d = F_Dog('flyffy', 'brown')
# f_d.name
# f_d.species
print(f_d.__dict__)
f_d.say_dog()
f_d.can_fly()

####################################################
####################################################


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'hello from {self.name} {self.age}')


# class Employee:
#
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

# def pay(self, hours):
#     payment = self.salary*hours # передаем метод в MixinSalary

# def say_hello(self):
#     print(f'hello from {self.name} {self.age} my salary is {self.salary} ') # передаем метод в MixinSalary


# p = Person('asdf', 45)
# e = Employee('asdf', 55, 554)
#
# p.say_hello()
# e.say_hello()


# В данном примере, оба класса имеют метод say_hello(),
# но в Employee метод дополнительно выводит зарплату.
#
# Это означает, что если мы хотим создать новый класс,
# например, Manager, который наследует и Person и Employee,
# нам придется повторно реализовывать метод say_hello()
# и добавлять логику для вывода зарплаты.
#
# Мы можем избежать дублирования кода, используя миксины.
# Мы можем создать класс SalaryMixin, который будет добавлять
# метод calculate_pay() в класс Employee, а также определять
# атрибут salary:


# Перепишим класс Employee убрав из не salary, т.к. передаем ее в mixin:

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Mixin ни от кого не наследуется, имеет свой __init__ и свои методы которые передаёт потомкам:
class SalaryMixin:

    def __init__(self, salary):
        self.salary = salary

    def pay(self, hours):
        self.payment = self.salary * hours  # передаем метод в MixinSalary (раньше он был в Employee)
        print(f'Сегодня я работал {hours} часов и заработал {self.payment} $')

    def say_hello(self):
        print(f'hello from {self.name} {self.age} my salary is {self.salary}')


class Manager(Employee, SalaryMixin):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        SalaryMixin.__init__(self, salary)


m = Manager('vv', 45, 500)
m.say_hello()
m.pay(5)


# И теперь по аналогии можно создавать новые профессии: ! наследуя нужные нам миксины и не дублируя код.

class Engineer(Employee, SalaryMixin):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        SalaryMixin.__init__(self, salary)


class Doctor(Employee, SalaryMixin):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        SalaryMixin.__init__(self, salary)

####################################################################

## NEXT EXAMPLE

# Pizza

class BasePizza:

    base_price = 10 # прописываем базовую цену

    def __init__(self, name, price):
        self.name = name
        self.price = BasePizza.base_price
        self.components = ['cheese']

    def bill(self, amount):
        self.bill = amount*self.price
        print(f'Пицца {self.name} за одну штуку стоит {self.price} $, заказано {amount} штук, общая цена {self.bill}$.')
        print(f'В пицце присутстуют компоненты {self.components}')

# p1 = BasePizza('Ch', 10)
# p1.bill(5)

class MixinAll: # в Миксине прописвываем метод добавления: add_onion

    def add_onion(self):
        print('добавляем лук')
        self.price += 5
        self.components += ['onion']

    def add_mashrooms(self):
        print('добавляем грибы')
        self.price += 500
        self.components += ['mushrooms']


class OnionPizza(BasePizza, MixinAll):
    def __init__(self): # наследуемся от родительского класса там требуется name и price, А ЗДЕСЬ НЕТ!
        super().__init__('луковая', BasePizza.base_price) # здесь прописываем имя и прайс.
        self.add_onion() # здесь добавляем Миксин.

# p2 = OnionPizza('Ony', 20)
# p2.bill(5)

class OnionMuSHPizza(BasePizza, MixinAll):
    def __init__(self): # наследуемся от родительского класса там требуется name и price, А ЗДЕСЬ НЕТ!
        super().__init__('mUshroom', BasePizza.base_price) # здесь прописываем имя и прайс.
        #self.add_onion() # здесь добавляем Миксин лук
        self.add_mashrooms() # здесь добавляем Миксин mushroom

p3 = OnionMuSHPizza()
p3.bill(10)

################################################################################
# Миксин для преобразования к строке
# class MyClass:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# m = MyClass(1,2)
# print(m) # Печатает: <__main__.MyClass object at 0x00000294318079D0> так как не реализован метод __str__

# Если же сначала определить Mixin для распечатки, то можно им воспользоваться в потомках:

class StrMixin:
    def __str__(self):
        return f'Hello, your x = {self.x}, and your y = {self.y}'


class MyClass(StrMixin):
    def __init__(self, x, y):
        self.x = x
        self.y = y


m = MyClass(1, 2)
print(m)  # Здесь нечего добавить...

##########################################################################
# Миксин для подсчета количества экземпляров

class CountMixin:

    count = 0

    def __init__(self, *args, **kwargs):
        self.__class__.count += 1 # подсчет экземпляров класса + 1

    def __str__(self):
        return f'Это экземпляр класса {self.__class__}, это уже {self.count} штука'

class Dog(CountMixin):

    def __init__(self, name):
        self.name = name
        super().__init__()

# d1 = Dog('Bob')
# print(Dog.count)
# d2 = Dog('Dod')
# print(Dog.count)

class Cat(CountMixin):

    def __init__(self, name):
        self.name = name
        super().__init__()

c1 = Cat('Blo-blo')
print(c1)

c2 = Cat('Figoroha')
print(c2)

c3 = Cat('Tigoroha')
print(c3)





