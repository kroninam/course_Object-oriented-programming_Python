# # # Артем Егоров
# # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # //www.youtube.com/c/egoroffchannel
#
# Public, protected, private attributes and methods:
#
# #1_Public:
class BankAccount:

    def __init__(self, name, acc, passport):
        self.name = name
        self.acc = acc
        self.passport = passport

    def get_account(self):
        print(self.name, self.acc, self.passport)

a1 = BankAccount('Bob', 10000, 5454511)
a1.get_account()
print(a1.name)
print(a1.acc)
print(a1.passport)

#2_Protected:
print('-'*20)
class BankAccount:

    def __init__(self, name, acc, passport):
        self._name = name
        self._acc = acc
        self._passport = passport

    def get_account(self):
        print(self._name, self._acc, self._passport)


a1 = BankAccount('Bob', 10000, 5454511)
a1.get_account()
print(a1._name)
print(a1._acc)
print(a1._passport)

#3_Private:
print('-'*20)
class BankAccount:

    def __init__(self, name, acc, passport):
        self.__name = name
        self.__acc = acc
        self.__passport = passport

    def get_account(self):
        print(self.__name, self.__acc, self.__passport)

a1 = BankAccount('Bob', 10000, 5454511)
a1.get_account()
# YOU COULD NOT DO THIS:
# print(a1.__name)
# print(a1.__acc)
# print(a1.__passport)

#4_Private_methods:
print('-'*20)
class BankAccount:

    def __init__(self, name, acc, passport):
        self.__name = name
        self.__acc = acc
        self.__passport = passport

    def show_public(self):
        self.__get_account()
    def __get_account(self):
        print(self.__name, self.__acc, self.__passport)

a1 = BankAccount('Bob', 10000, 5454511)
# a1.__get_account() - YOU COULD NOT DO THIS
# BUT YOU CAN DO THIS:
a1.show_public()

print('*'*20)
# ONE CAN GET PRIVATE DATA USING THIS:
print(dir(a1))
print(a1._BankAccount__name)
print(a1._BankAccount__acc)
print(a1._BankAccount__passport)
print('*'*20)
