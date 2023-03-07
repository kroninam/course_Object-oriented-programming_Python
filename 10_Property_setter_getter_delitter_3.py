# # # # Артем Егоров
# # # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # # //www.youtube.com/c/egoroffchannel
#
# # ДЕКОРАТОР Property. На том же примере BankAccount:
# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#     #@property
#     def get_balance(self):
#         print('отработала get_balance')
#         print(self.__balance)
#         return self.__balance
#
#
#     def set_balance(self, num):
#
#         if not isinstance(num, int or float):
#             raise ValueError('Type is not for the balance')
#         else:
#             print('отработал метод set_balance')
#             self.__balance = num
#
#     def delete_balance(self):
#         del self.__balance
#
#     my_balance = property()
#     my_balance = my_balance.getter(get_balance)
#     my_balance = my_balance.setter(set_balance)
#     my_balance = my_balance.deleter(delete_balance)
#
# a = BankAccount('ivan', 100)
# a.my_balance # отработала get_balance
# a.my_balance = 1000
# a.my_balance # отработала get_balance
#
# # То же самое если вызывать просто через get_balance и set_balance
#
# a.get_balance()
# a.set_balance(500)
# a.get_balance()

#декорирование:

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('отработала get_balance')
        print(self.__balance)
        return self.__balance

    @my_balance.setter
    def my_balance(self, num):

        if not isinstance(num, int or float):
            raise ValueError('Type is not for the balance')
        else:
            print('отработал метод set_balance')
            self.__balance = num
    @my_balance.deleter
    def my_balance(self):
        del self.__balance

    # my_balance = property(my_balance) # задается декоратор @
    # my_balance = my_balance.getter(get_balance)
    #my_balance = my_property_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)

a = BankAccount('asdf', 300)
a.my_balance
a.my_balance = 100000
a.my_balance
del a.my_balance

a.my_balance = 12
a.my_balance

# a.set_balance(500)
# a.my_balance



