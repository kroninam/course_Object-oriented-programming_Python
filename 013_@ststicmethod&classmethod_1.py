# # # # Артем Егоров
# # # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # # //www.youtube.com/c/egoroffchannel

# staticmethod & classmethod

# class Example:
#     #чтобы вызывать просто от класса без self:
#     def hello():
#         print('hello')
#
# print(Example.hello)  # возвращает <function Example.hello at 0x0000023896AD8E00>
#
# p = Example()
# print(p.hello) # возвращает <bound method Example.hello of <__main__.Example object at 0x00000238970D7950>>
# Example.hello() # без проблем отрабатывает print(hello)
# print(p.hello()) # вернет ошибку т.к. нужен аргумент self


# class Example:
#     #чтобы вызывать просто от экземпляра класса - нужен self:
#     def hello(self):
#         print('hello')
#
# p = Example()
# p.hello() # НЕ вернет ошибку т.к. прописан аргумент self
#
# ## но здесь уже не работает вызов от класса:
# Example.hello()



# class Example:
#     @staticmethod
#     def stat_hello():
#         print('hello')
#
# ## ТЕПЕРЬ РАБОТАЕТ ОТ КЛАССА БЕЗ ЭКЗЕМПЛЯРА КЛАССА:
# Example.stat_hello()
#
# p = Example()
# p.stat_hello() # И ЭТОТ ВЫЗОВ ТОЖЕ РАБОТАЕТ !!!



class Example:
    @classmethod
    def class_hello(cls):
        print(f'hello {cls}')

p = Example()
p.class_hello() # вызывается как от ЭК
Example.class_hello() # так и от класса.
