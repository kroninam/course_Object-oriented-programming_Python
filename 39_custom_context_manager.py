# Custom Context Manager

# class CustomContextManager:
#
#     def __enter__(self):
#         print('start')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('end')
#
# with CustomContextManager() as cust:
#     print('hello')

# class TextContext:
#
#     def __init__(self, path, mode):
#         self.path = path
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         print('start')
#         try:
#             self.file = open(self.path, self.mode)
#             return self.file
#         except FileNotFoundError:
#             print('No such file')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('end')
#         if self.file:
#             self.file.close()
#
# # with TextContext('Abracadabra__1_.txt', 'r') as file:
# #     print(file.read())
# with TextContext('Ab', 'r') as file:
#     if file:
#         print(file.read())

class Step:

    def __enter__(self):
        print('шаг_1')
        return f'шаг_3'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('шаг_5')

with Step() as s:
    print('шаг_2')
    print(s)
    print('шаг_4')