# # # # Артем Егоров
# # # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # # //www.youtube.com/c/egoroffchannel

# # THE TASK
#
# Создайте класс Robot, у которого есть:
#
# атрибут класса population. В этом атрибуте будет храниться общее количество роботов, изначально принимает значение 0;
#
# конструктор __init__, принимающий 1 аргумент name. Данный метод должен сохранять атрибут name и печатать сообщение вида
# "Робот <name> был создан". Помимо инициализации робота данный метод должен увеличивать популяцию роботов на единицу;
#
# метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение вида "Робот <name> был уничтожен"
#
# метод say_hello, которой печатает сообщение вида "Робот <name> приветствует тебя, особь человеческого рода"
#
# метод класса  how_many, который печатает сообщение вида "<population>, вот сколько нас еще осталось"

class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print(f'Робот {self.name} был создан.')

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} был уничтожен.')

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода.')

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось.')


r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"

# код ниже не нужно удалять, в нем находятся проверки

droid1 = Robot("R2-D2")
assert droid1.name == 'R2-D2'
assert Robot.population == 1
droid1.say_hello()
Robot.how_many()
droid2 = Robot("C-3PO")
assert droid2.name == 'C-3PO'
assert Robot.population == 2
droid2.say_hello()
Robot.how_many()
droid1.destroy()
assert Robot.population == 1
droid2.destroy()
assert Robot.population == 0
Robot.how_many()

## NEXT TASK

# Создайте базовый класс User, у которого есть:
#
# метод __init__, принимающий имя пользователя и его роль.
# Их необходимо сохранить в атрибуты экземпляра name и role соответственно
#
# Затем создайте класс Access , у которого есть:
#
# приватный атрибут класса __access_list , в котором хранится список ['admin', 'developer']
#
# приватный статик-метод __check_access , который принимает название роли и возвращает True,
# если роль находится в списке __access_list , иначе - False
#
# публичный статик-метод get_access , который должен принимать экземпляр класса User и
# проверять есть ли доступ у данного пользователя к ресурсу при помощи метода __check_access  .
# Если у пользователя достаточно прав, выведите на экран сообщение
# «User <name>: success», если прав недостаточно - «AccessDenied»
# Если передается тип данных, отличный от экземпляр класса User, необходимо вывести сообщение:
# «AccessTypeError».

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(role):
        #print(role)
        #print(role in Access.__access_list)

        return role in Access.__access_list

    @staticmethod
    def get_access(a):
        #print(a.role)
        if isinstance(a, User):
            if Access.__check_access(a.role) is True:
                print(f'User {a.name}: success')
            else:
                print(f'AccessDenied')
        else:
            print(f'AccessTypeError')

user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

## NEXT TASK

# Создайте класс BankAccount, который имеет:
#
# атрибут класса bank_name со значением "Tinkoff Bank"
#
# атрибут класса address со значением  "Москва, ул. 2-я Хуторская, д. 38А"
#
# метод __init__, который устанавливает значения атрибутов name и balance : владелец счета и значение счета
#
# класс метод create_account, который возвращает новый экземпляр класса BankAccount. Метод принимает имя клиента и сумму взноса
#
# класс метод bank_info, который возвращает информация о банке в виде:
# «{bank_name} is located in {address}»

class BankAccount:

    bank_name = "Tinkoff Bank"
    address = "Москва, ул. 2-я Хуторская, д. 38А"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def create_account(cls, name, summa):
        return cls(name, summa)


    @classmethod
    def bank_info(cls):
        return f'{cls.bank_name} is located in {cls.address}'

# print(BankAccount.bank_info())
oleg = BankAccount.create_account("Олег Тинкофф", 1000)
assert isinstance(oleg, BankAccount)
assert oleg.name == 'Олег Тинкофф'
assert oleg.balance == 1000