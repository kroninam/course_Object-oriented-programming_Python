# # # # Артем Егоров
# # # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # # //www.youtube.com/c/egoroffchannel

# Practice with @property, @setter, @getter

## TASK #1

from string import digits
class Password:

    def __init__(self, password):
        self.password = password
        self.__secret = 'abracadabra'

    @property
    def password(self):
        print('getter')
        return self.__password

    @staticmethod
    def check(password):
        with open('passwords.txt') as p:
            return password in p.read()


    @property
    def secret(self):
        s = input('Input password: ')
        if s == self.__password:
            return self.__secret
        else:
            return 'Нет доступа'


    # @staticmethod
    # def check(password):
    #     print(password)
    #     for i in digits:
    #         if i in password:
    #
    #             return True
    #     return False

    @password.setter
    def password(self, new_password):
        print('setter')

        if Password.check(new_password) is True:
            self.__password = new_password
        else:
            print('No')

a = Password('qwerty')
print(a.password)
print(a.secret)

## NEXT TASK
# # NEXT TASK
#
# Задача Регистрация
#
# Допустим, у нас есть сайт и для успешной регистрации
# на нем необходимо придумать логин и пароль.
# Но мы хотим, чтобы при этом выполнялись определенные
# проверки с предоставленной пользователем
# информацией, например, чтобы пароль был непростым.
# Мы можем делегировать данные проверки классу
# Registration , который вам необходимо создать.
#
# Задача будет состоять из двух частей.
#
# Часть 1
# Создайте класс Registration, который пока будет проверять только
# введенный логин.
# Под логином мы будем подразумевать почту пользователя, поэтому
# необходимо будет сделать некоторые проверки.
#
# В классе Registration необходимо реализовать:
#
# метод __init__ принимающий один аргумент логин пользователя.
# Метод __init__ должен сохранить переданный логин через сеттер
# (см пункт 3). То есть когда отработает данный код.
#
# def __init__(self, логин):
#     self.login = логин # передаем в сеттер login значение логин
#
# должно сработать свойство сеттер login из пункта 3
# для проверки валидности переданного значения
#
# Cвойство геттер login, которое возвращает значение self.__login;
#
# Свойство сеттер login, принимает значение нового логина.
# Новое значение мы должны проверить на следующее:
#
# строковое значение, если поступают другие типы данных необходимо
# вызвать исключение при помощи строки raise TypeError
#
# логин, так как является почтой, должен содержать один символ собаки «@».
# В случае, если в логине отсутствует символ «@»,
# вызываем исключение при помощи строки raise ValueError
#
# логин должен содержать символ точки «.» после символа «@».
# В случае, если после @ нету точки,
# вызываем исключение при помощи строки raise ValueError
#
# Если значение проходит проверку новое значение логина
# сохраняется в атрибут self.__login

class Registration:

    def __init__(self, login):
        self.login = login

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        if type(new_login) != str:
            raise TypeError
        if '@' not in new_login:
            raise ValueError
        if '.' not in new_login and new_login.index('@') < new_login.index('.'):
            raise ValueError
        else:
            self.__login = new_login


a = Registration('fg.@a')
print(a.login)

# Ниже код для проверки класса Registration

try:
    result = Registration("fga")
except ValueError as error:
    print("Логин fga должен содержать один символ '@'")

try:
    result = Registration(1234)
except TypeError as error:
    print("Пароль должен быть строкой")

try:
    result = Registration("f@ga@")
except ValueError as error:
    print("Логин f@ga@ должен содержать только один символ '@'")

try:
    result = Registration("fg@a")
except ValueError as error:
    print("В логине fg@a должен быть символ '.' после символа '@'")

try:
    result = Registration("fg.@a")
except ValueError as error:
    print("В логине fg.@a должна быть '.' после символа '@'")

result = Registration("translate@gmail.com")
assert result.login == "translate@gmail.com"
assert result._Registration__login == "translate@gmail.com"

try:
    result.login = "asdsa12asd."
except ValueError as error:
    print("Логин asdsa12asd. должен содержать один символ '@'")

try:
    result.login = "asdsa12@asd"
except ValueError as error:
    print("asdsa12@asd должен быть символ '.' после символа '@'")

result.login = "alligator13@how.do"
assert result.login == "alligator13@how.do"
assert result._Registration__login == "alligator13@how.do"

# # Вторая часть задачи
#
# в метод  __init__ добавляется еще один аргумент: пароль. Как в примере с логином,
# вы должны будете сохранить переданный пароль через password через сеттер  password
# (см пункт 3 в этом задании). Примерный код метода __init__
#
# def __init__(self, логин, пароль):
#     self.login = логин # передаем в сеттер login значение логин
#     self.password = пароль # передаем в сеттер password значение пароль


# Должны сработать свойства сеттер login из предыдущего задания  и сеттер password из
# пункта 3 для проверки валидности переданных значений
#
# Свойство геттер password, которое возвращает значение self.__password;
#
# Свойство сеттер password, принимает значение нового пароля. Его необходимо перед сохранением проверить на следующее:
#
# новое значение пароля должно быть строкой(не список, словарь и т.д. ) в противном случае вызываем исключение
# TypeError("Пароль должен быть строкой")

# Длина нового пароля должна быть от 5 до 11 символов, в противном случае вызывать исключение
# ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')

# Новый пароль должен содержать хотя бы одну цифру. Для этого создаем staticmethod is_include_digit ,
# который проходит по всем элементам строки и проверяет наличие цифр. В случае отсутствия цифрового
# символа вызываем исключение: ValueError('Пароль должен содержать хотя бы одну цифру')

# Строка password должна содержать элементы верхнего и нижнего регистра. Создаем staticmethod is_include_all_register,
# который с помощью цикла проверяет элемента строчки на регистр. В случае ошибки
# вызываем: ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')

# Строка password помимо цифр должна содержать только латинские символы. Для этого
# создайте staticmethod is_include_only_latin , который проверяет каждый элемент нового значения
# на принадлежность к латинскому алфавиту(проверка должна быть как в верхнем, так и нижнем регистре).
# В случае, если встретится нелатинский символ, вызвать ошибку ValueError('Пароль должен содержать
# только латинский алфавит').
# Подсказка: из модуля string можно импортировать переменную ascii_letters, она хранит в себе все латинские символы
# в верхнем и нижнем регистре

# Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt.
# Сохраните данный файл к себе в папку с вашей программой и не меняйте название. С помощью staticmethod
# создаем метод check_password_dictionary и проверяем наличие нашего пароля в данном файле.
# Если значение совпадет со значением из файла, то в сеттер вызываем
# исключение: ValueError('Ваш пароль содержится в списке самых легких')

from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters

class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        if type(new_login) != str:
            raise TypeError
        if '@' not in new_login:
            raise ValueError
        if '.' not in new_login and new_login.index('@') < new_login.index('.'):
            raise ValueError
        else:
            self.__login = new_login

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_digit(password):
        for i in password:
            if i in digits:
                return True
            else:
                continue
        return False

    @staticmethod
    def is_include_all_register(password):
        x = 0
        y = 0
        for i in password:
            if i in ascii_lowercase:
                x +=1
            if i in ascii_uppercase:
                y +=1
        if x==0 and y==0:
            return False

    @staticmethod
    def is_include_only_latin(password):
        for i in password:
            if i not in digits:
                if i in ascii_letters:
                    pass
                else:
                    return False

    @staticmethod
    def check_password_dictionary(password):
        with open('easy_passwords.txt') as p_list:
            if password in p_list.read().strip():
                return False
            else:
                return True

    @password.setter
    def password(self, value):
        if type(value) != str:
            raise TypeError ('Пароль должен быть строкой')

        if self.is_include_digit(value) is False:
            raise ValueError('Пароль должен содержать хотя бы одну цифру')

        if len(value) < 5 or len(value) > 12:
            raise ValueError ('Пароль должен быть длиннее 4 и меньше 12 символов')

        if self.is_include_all_register(value) is False:
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if self.is_include_only_latin(value) is False:
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if self.check_password_dictionary(value) is False:
            raise ValueError('Ваш пароль содержится в списке самых легких')

        else:
            self.__password = value


# Пример работы класса Registration

r1 = Registration('qwerty@rambler.ru', 'QwrRt24') # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
r1.password = '1111234567'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124
# r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
# r1.password = 43  # raise TypeError("Пароль должен быть строкой")















