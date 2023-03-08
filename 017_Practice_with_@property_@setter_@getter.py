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
<<<<<<< HEAD
=======
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







>>>>>>> f7b86f0d82a2b6db982a5ee7bb53d68ee724b9db







