# Instruction "raise"

# def function_1():
#     raise ValueError("Oops, something went wrong")
##
# def function_2():
#     try:
#         function_1()
#     except Exception as e:
#         print("Exception caught:", e)
#         print(e)
#
# function_2()

#The TASK

# задача создать класс Customer, который содержит:
#
# метод __init__, принимающий на вход имя пользователя и
# необязательный аргумент баланс его счета(по умолчанию 0).
# Эти значения необходимо сохранить в атрибуты name и balance ;
#
# статический метод check_type , принимающий на вход одно значение.
# Если оно не является числом (не принадлежит классу int или float)
# необходимо вызывать исключение TypeError('Банк работает только с числами').
# Это все, метод check_type должен только вызывать исключение в случае
# неправильного типа, возвращать она ничего не должна.

# метод withdraw  , принимающий на вход значение для списания.
# Необходимо сперва проверить переданное значение на тип при помощи
# метода check_type  . Если исключений не возникло, необходимо проверить
# что у покупателя достаточно средств на балансе. Если денег хватает,
# то необходимо уменьшить баланс. Если средств не хватает , нужно
# вызвать исключение ValueError('Сумма списания превышает баланс')

#
# метод deposit  , принимающий на вход значение для зачисления
# на баланс. При помощи метода check_type  проверьте, что передано
# число. Если исключений не возникло, увеличьте значение баланса
# покупателя на указанную сумму

class Customer:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(value):
        if not isinstance(value, (int, float)):
            raise TypeError ('Банк работает только с числами')

    def deposit(self, depoz):
        # try:
        #     self.check_type(depoz)
        # except TypeError:
        #     raise TypeError ('Банк работает только с числами')
        # else:
        #     self.balance = self.balance + depoz

        self.check_type(depoz)
        self.balance = self.balance + depoz

    def withdraw(self, value):
        try:
            self.check_type(value)
        except ValueError:
            print ('Сумма списания превышает баланс')
        else:
            if self.balance < value:
                raise ValueError('Сумма списания превышает баланс')
            else:
                self.balance = self.balance - value
                return self.balance


# Ниже код для проверки класса Customer


assert Customer.check_type(2) is None, 'Метод check_type не должен ничего возращать'
assert Customer.check_type(2.5) is None, 'Метод check_type не должен ничего возращать'

for i in ['hello', [1, 2, 3], dict(), set()]:
    try:
        Customer.check_type(i)
    except TypeError as error:
        print(error)
    else:
        raise TypeError(f'Метод check_type должен вызывать ошибку если передать {i}')

bob = Customer('Bob Odenkirk')
assert bob.balance == 0
assert bob.name == 'Bob Odenkirk'
try:
    bob.deposit('hello')
except TypeError as error:
    print(error)
else:
    raise ValueError("Нельзя вносить на счет баланса строку")

try:
    bob.deposit([])
except TypeError as error:
    print(error)
else:
    raise ValueError("Нельзя вносить на счет баланса список")

bob.deposit(200)
assert bob.balance == 200

try:
    bob.withdraw(300)
except ValueError as e:
    print(e)
else:
    raise ValueError("Проверьте списание при превышении лимита")

bob.withdraw(150)
assert bob.balance == 50

terk = Customer('Terk', 1000)
assert terk.name == 'Terk'
assert terk.balance == 1000
terk.withdraw(999)
assert terk.balance == 1, 'Не списались деньги, проверяйте списание'
terk.withdraw(1)
assert terk.balance == 0, 'Не списались деньги, проверяйте списание'

try:
    terk.withdraw(1)
except ValueError as e:
    print(e)
else:
    raise ValueError("Проверьте списание при превышении лимита")
assert terk.balance == 0

# NEXT TASK
# Напишите функцию sum_numbers, которая принимает один аргумент numbers.
# Это должен быть список, состоящий из целых и вещественных чисел.
# Функция sum_numbers должна возвращать сумму всех элементов списка,
# но прежде чем находить сумму необходимо выполнить следующие проверки:
#
# Аргумент numbers должен быть именно списком, если передан другой тип,
# необходимо выкинуть исключение TypeError('Аргумент numbers должен быть списком')
#
# numbers не должен быть пустым, иначе возбуждаем исключение ValueError("Пустой список")
#
# внутри numbers должны быть только типы int и float, иначе возбуждаем
# исключение TypeError('Неправильный тип элемента')

def sum_numbers(numbers: list):
    if not type(numbers) is list:
        raise TypeError('Аргумент numbers должен быть списком')
    if len(numbers) == 0:
        raise ValueError("Пустой список")
    for i in numbers:
        if not isinstance(i, (int, float)):
            raise TypeError('Неправильный тип элемента')

    return sum(numbers)


# Ниже код для проверки функциии sum_numbers

for value in (True, (1, 2, 3), {1: 'hello'}, {1, 2, 3}):
    try:
        result = sum_numbers(value)
    except TypeError as error:
        print(error)

try:
    result = sum_numbers([])
except ValueError as error:
    print(error)

try:
    sum_numbers([1, 'hello', 2, 3])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, [1, 2, 3]])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, {1, 2, 3}])
except TypeError as error:
    print(error)

try:
    sum_numbers([1, 2, 3, 4, 5, (1, 2, 3)])
except TypeError as error:
    print(error)

assert sum_numbers([1, 2, 3, 4, 5]) == 15
assert sum_numbers([1, 2, 3, 4, 5.0]) == 15.0

