# Exceptions in Python

""" Коспект
try: попробует сделать что-то с возможной ошибкой
except error : может быть несколько вариантов ошибок или несколько except
else: выполнится только если ошибки не будет
finally: выполнится всё равно будет найдена ошибка или нет

s = "hello"
# если try найдёт первый except, то остальные выйдут с блока как break
try:
    s + 12
except KeyError:
    print("KeyError found") # вызов если найдена ошибка типа KeyError
except TypeError:
    print("TypeError found") # вызов если найдена ошибка типа TypeError
except Exception: # вызов если найдена любая ошибка Exception или except: если Base Exception
    print("All Exceptions")
except(KeyError, TypeError, NameError): # вызов если найдена ошибки типа KeyError, TypeError, NameError
    print("3 Error found")
else: # выполниться после try если не будет найдена ошибка
    print("else called")
finally: # выполниться после try несмотря на то будет ли найдена ошибка
    print("finally called")
"""

# try:
#     5/0
#     # 1/5
# except ZeroDivisionError:
#     print('Error')
# except Exception:
#     print('Major Exception Error')
# else:
#     print('OK')
# finally:
#     print('end')

# THE TASK

# Реализуйте класс Wallet, аналог денежного кошелька, содержащий
# информацию о валюте и остатке имеющихся средств на счете.
# В данном классе должны быть реализованы:
#
# метод __init__, который создает атрибуты currency и balance.
# Значения атрибутов currency и balance поступают при вызове метода
# __init__. При этом значение атрибута currency должно быть строкой,
# состоящей только из трех заглавных букв. Для этого необходимо
# сделать именно в такой последовательности следующие проверки:

# В случае, если передается не строка, нужно возбуждать исключение
# TypeError с текстом "Неверный тип валюты" ;
# В случае, если передается строка, длина которой не равна трем
# символам, нужно возбуждать исключение NameError с текстом
# "Неверная длина названия валюты"
# В случае, если строка из трех символов состоит из незаглавных
# букв, нужно возбуждать исключение ValueError с текстом
# "Название должно состоять только из заглавных букв"

# метод __eq__, для возможности сравнивания балансов кошельков.
# Операция сравнения доступна только для кошельков с одинаковой
# валютой. Если валюты различаются, необходимо возбудить исключение
# ValueError с текстом "Нельзя сравнить разные валюты". При попытке
# сравнить экземпляр класса Wallet с другими объектами необходимо
# возбудить исключение TypeError с текстом "Wallet не поддерживает сравнение с <объектом>";

# методы __add__ и __sub__ для возможности суммирования и вычитания
# кошельков. Складывать и вычитать мы можем только с другим экземпляром
# класса Wallet и только в случае, когда у них совпадает валюта
# (атрибуты currency). Результатом такого сложения должен быть новый
# экземпляр класса Wallet , у которого валюта совпадает с валютой
# операндов и значение баланса равно сумме/вычитанию их балансов
# (при вычитании баланс может оказаться отрицательным).
# Если попытаются сложить с объектом не являющимся экземпляром
# Wallet или значения валют у объектов не совпадают,  необходимо
# возбудить исключение ValueError с текстом  "Данная операция запрещена"

class Wallet:

    def __init__(self, currency: str, balance):
        self.balance = balance
        if type(currency) != str:
            raise TypeError('Неверный тип валюты')
        if len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        if currency != currency.upper():
            raise ValueError('Название должно состоять только из заглавных букв')
        else:
            self.currency = currency

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')

        if self.currency != other.currency:
            raise ValueError('Нельзя сравнить разные валюты')

        else:
            return self.balance == other.balance

    def __add__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError(f'Данная операция запрещена')
        else:
            new_balance = self.balance + other.balance
            x = Wallet(self.currency, new_balance)
            return x

    def __sub__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError(f'Данная операция запрещена')
        else:
            new_balance = self.balance - other.balance
            x = Wallet(self.currency, new_balance)
            return x

wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
# wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)  # False
print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
wallet2 + 45  # ValueError('Данная операция запрещена')

## NEXT TASK

# a = int(input("Введите значение a: "))
# b = int(input("Введите значение b: "))
# c = a/b
# print(f"Результат деления a на b: {a/b}")

# могут возникнуть исключения типа ValueError и ZeroDivisionError.
#
# Ваша задача отловить их в одном блоке except и в случае
# возникновения любого из этих исключений вывести
# на экран фразу «Введите корректные значения»

try:
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    a/b
except ValueError:
    print('Введите корректные значения')
except ZeroDivisionError:
    print('Введите корректные значения')
else:
    print(f"Результат деления a на b: {a/b}")

## NEXT TASK

# Каждое возможное исключение отлавливать отдельным блоком except.
#
# Если возникает исключение типа ValueError , то необходимо
# вывести фразу «Введите целое число»
#
# Если возникает исключение типа ZeroDivisionError, то
# необходимо вывести фразу «Делитель не должен быть равен нулю»

try:
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
except ValueError:
    print('Введите целое число')
else:
    try:
        a/b
    except ZeroDivisionError:
        print('Делитель не должен быть равен нулю')
    else:
        print(f"Результат деления a на b: {a/b}")


# # EXAMPLE with Error as...
# try:
#     assert 1 == 2, "Что-то пошло не так"
# except AssertionError as e:
#     print("Отловили AssertionError:", e)
# finally:
#     print("Досвидули")

#THE TASK
# Запустите код ниже, чтобы понять с
# каким типом исключения имеете дело
#
# Обработайте данный тип исключения при помощи
# блока try-except и выведите сообщение
# «Эх, не судьба тайны пентагона узнать»

try:
    file = open('pentagon_secrets.txt', 'r')
except FileNotFoundError:
    print('Эх, не судьба тайны пентагона узнать')
else:
    print(file.read())

# NEXT TASK
# def func(phrase):
#     func(phrase)
#
#
# func('Это рекурсия, детка!')
#
# Задача отловить в блоке try-except именно возникающий
# тип исключения и вывести фразу «Кто-то должен остановить это безумие»

def func(phrase):
    try:
        func(phrase)
    except RecursionError:
        print('Кто-то должен остановить это безумие')

func('Это рекурсия, детка!')


# THE TASK

# Ваша задача  создать класс CustomButton, у которого есть:
#
# метод __init__, принимающий один обязательный аргумент текст
# кнопки, его необходимо сохранить в атрибут text. И также в метод
# может поступать произвольное количество именованных аргументов.
# Их необходимо сохранять в атрибуты экземпляра под тем же названием

# метод config, который принимает произвольное количество именованных
# атрибутов. Он должен создать атрибут с указанным именем или, если
# этот атрибут уже присутствовал в экземпляре, изменить его на новое значение

# метод click, который должен выполнить следующую строчку
# self.command()

# Здесь command является не методом, а атрибутом, который вызывают.
# В момент выполнения этой строчки может произойти две неприятные ситуации

# атрибут command может отсутствовать у экземпляра и тогда возникнет исключение AttributeError
# атрибут command может не поддерживать оператор вызова и тогда возникнет исключение TypeError

# Эти ситуации вам необходимо обработать в блоке try-except.
# При первом варианте нужно вывести сообщение «Кнопка не настроена»,
# при втором - «Кнопка сломалась»

class CustomButton:

    def __init__(self, text, **kwargs):
        self.__dict__ = kwargs
        self.text = text

# s = CustomButton('asdf', f=5, g = 8)
# print(s.__dict__)
# print(s.text)

    def config(self, **kwargs):
        self.__dict__.update(kwargs)

# s = CustomButton('asdf', f=5, g = 8)
# print(s.__dict__)
# print(s.text)
# s.config(g = 10, k = 12)
# print(s.__dict__)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print('Кнопка не настроена')
        except TypeError:
            print('Кнопка сломалась')

# Пример использования класса CustomButton

def func():
    print('Оно живое')


btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa')
btn.click()  # Кнопка не настроена
btn.config(command=func)
btn.click()  # Оно живое