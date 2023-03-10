## # # # Артем Егоров
# # # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # # //www.youtube.com/c/egoroffchannel

# Practice with @property, @setter, @getter

# THE TASK

# Задача «Оформление заказа»
# Задача «Оформление заказа»
# Задача «Оформление заказа»
# Задача «Оформление заказа»

# Все вы думаю сталкивались с оформлением заказов в онлайн магазинах. Давайте и мы воссоздадим этот процесс

# Часть 1

# Для этого нам понадобится реализовать несколько классов и связать их между собой. Первый класс, который
# мы реализуем, будет Product. Это класс, описывающий товар. В нем должно быть реализовано:
#
# метод __init__, принимающий на вход имя товара и его стоимость. Эти значения необходимо
# сохранить в атрибутах name и price
#
# Пример работы с классом Product
#
# carrot = Product('carrot', 30)
# print(carrot.name, carrot.price)
# Необходимо только написать определение класса.

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

# carrot = Product('carrot', 30)
# print(carrot.name, carrot.price)

# Часть 2

# Далее для оформления заказа нам нужен пользователь. Для этого создадим класс User, который содержит:

# метод __init__, принимающий на вход логин пользователя и необязательный аргумент баланс его счета(по умолчанию 0).
# Логин необходимо сохранить в атрибуте login , а баланс необходимо присвоить сеттеру   balance  (см. пункт 4)
#
# метод __str__, возвращающий строку вида «Пользователь {login}, баланс - {balance}»
#


class User:

    def __init__(self, login, balance = 0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    # Cвойство геттер balance, которое возвращает значение self.__balance;
    #
    # Свойство сеттер balance, принимает новое значение баланса и устанавливает его в атрибут self.__balance ;
    #

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

 # метод deposit  принимает числовое значение и прибавляет его к атрибуту self.__balance ;
    #


    def deposit(self, depoz):
        self.__balance = self.__balance+depoz

# метод payment  принимает числовое значение, которое должно списаться с баланса пользователя.

# Если на счете у пользователя не хватает средств, то необходимо вывести фразу  «Не хватает средств
# на балансе. Пополните счет» и вернуть False. Если средств хватает, списываем с баланса у пользователя
# указанную сумму и возвращаем True

    def payment(self, pay):
        if pay <=  self.__balance:
            self.__balance = self.__balance - pay
            return True
        else:
            print('Не хватает средств на балансе. Пополните счет')
            return False

#Проверка кода выше:
# billy = User('billy@rambler.ru')
# print(billy) # Пользователь billy@rambler.ru, баланс - 0
# billy.deposit(100)
# billy.deposit(300)
# print(billy) # Пользователь billy@rambler.ru, баланс - 400
# billy.payment(500) # Не хватает средств на балансе. Пополните счет
# billy.payment(150)
# print(billy) # Пользователь billy@rambler.ru, баланс - 250

# Часть 3

# Последний штрих - создание класса корзины, куда наш
# пользователь будет складывать товары. Для этого нам понадобятся ранее созданные классы User и Product.
#
# Итак, создаем класс Cart, который содержит:
#
# метод __init__, принимающий на вход экземпляр класса User .
# Его необходимо сохранить в атрибуте user . Помимо этого метод
# должен создать атрибут goods - пустой словарь (лучше использовать defaultdict).
# Он нужен будет для хранения наших товаров и их количества(ключ словаря - товар, значение - количество).
# И еще нам понадобится создать защищенный атрибут .__total со значением 0.
# В нем будет хранится итоговая сумма заказа.
from collections import defaultdict
class Cart:
    def __init__(self, user):
        self.user = user
        self.goods = {}
        self.__total = 0
#
# метод add принимает на вход экземпляр класса Product и необязательный аргумент
# количество товаров (по умолчанию 1). Метод add  должен увеличить в корзине (атрибут goods)
# количество указанного товара  на переданное значение количество и пересчитать атрибут self.__total
    def add(self, Product, amount = 1):
        if Product not in self.goods:
            self.goods.update({Product: amount})
        else:
            self.goods[Product] += amount
        self.__total += amount*Product.price

# метод remove  принимает на вход экземпляр класса Product и необязательный аргумент количество товаров
# (по умолчанию 1).  Метод remove  должен уменьшить в корзине (атрибут goods) количество указанного товара
# на переданное значение количество и пересчитать атрибут self.__total. Обратите внимание на то,
# что количество товара в корзине не может стать отрицательным как и итоговая сумма.

    def remove(self, Product, amount = 1):
        if self.goods[Product] > amount:
            self.goods[Product] -= amount
            self.__total = amount**Product.price
        else:
            self.__total -= self.goods[Product]*Product.price
            del self.goods[Product]


# Cвойство геттер total, которое возвращает значение self.__total;
    @property
    def total(self):
        return self.__total

# метод order  должен использовать метод payment  из класса User и передать
# в него итоговую сумму корзины. В случае, если средств пользователю хватило,
# вывести сообщение «Заказ оплачен», в противном случае - «Проблема с оплатой»;


    def order(self):
        if User.payment(self.user, self.__total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

# метод print_check  печатающий на экран чек. Он должен начинаться со строки
# ---Your check---
# Затем выводится состав корзины в алфавитном порядке по названию товара в виде
# {Имя товара} {Цена товара} {Количество товара} {Сумма}
# И заканчивается чек строкой
# ---Total: {self.total}---

    def print_check(self):
        print('---Your check---')

        for k in sorted(self.goods, key = lambda x: x.name):
            print(k.name, k.price, self.goods[k], k.price*self.goods[k])

        print(f'---Total: {self.total}---')


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
