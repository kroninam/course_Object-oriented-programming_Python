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







