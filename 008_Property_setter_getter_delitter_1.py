# # # Артем Егоров
# # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # //www.youtube.com/c/egoroffchannel

# Property, getter, setter and delitter

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print(self.__balance)
        return self.__balance

    def set_balance(self, num):
        if not isinstance(num, int or float):
            raise ValueError('Type is not for the balance')
        else:
            self.__balance = num

    def delete_balance(self):
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel= delete_balance)

#WITHOUT Property function:
a = BankAccount('hsdaf', 400)
a.set_balance(500)
a.get_balance()

#WITH Property function:
a.balance
a.balance = 800
a.balance
del a.balance
a.balance = 5
a.balance
print('*'*20)
print('NEXT EXAMPLE')
print('*'*20)