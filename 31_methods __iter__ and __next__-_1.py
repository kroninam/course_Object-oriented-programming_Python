# methods __iter__ and __next__

# a = [1,2,3,4,5,6]
#
# b = iter(a)
#
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
#
#
# c = a.__iter__()
# print(c.__next__())
# print(c.__next__())

# итератор строки str:
# d = 'asb'
# f = iter(d)
# print(next(f))


class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

# igor = Student('Igor', 'Nikolaev', [5,4,3,3,4,5,6])
# for i in igor:
#     print(i) - # 'Student' object is not iterable

# По умолчанию итерация происходит по методу __getitem__:
    def __getitem__(self, item):
        return self.name[item]
    # def __getitem__(self, item):
    #     return self.surnamename[item]
    # def __getitem__(self, item):
    #     return self.marks[item]

# igor = Student('Igor', 'Nikolaev', [5,4,3,3,4,5,6])
# for i in igor:
#     print(i) - Поочередно выводятся все буквы имени (item принимает значения от 0 до len(self.name))


# # # Первый вариант итератора:
#     def __iter__(self):
#         print('call_iter')
#         return iter(self.surname)
#
# igor = Student('Igor', 'Nikolaev', [5,4,3,3,4,5,6])
# for i in igor:
#     print(i)

# # # Второй вариант итератора (с next) - где описывается как именно обходить коллекцию:
#     def __iter__(self):
#         print('call_iter')
#         self.index = -1
#         return self
#
#     def __next__(self): # __next__ задает логику получения элементов при итерации
#         if self.index >= len(self.name)-1:
#             raise StopIteration
#         self.index +=1
#         return self.name[self.index]
#
# igor = Student('Igor', 'Nikolaev', [5,4,3,3,4,5,6])
# for i in igor:
#     print(i)

# Оценки можно вынести в отдельный класс Marks (ниже), а итерацию по оценкам запусить в этом классе:

    def __iter__(self):
        print('call_iter')
        return self.marks

    def __next__(self):
        # Этот итератор вообще не вызовется, так как выше в __iter__ идет обращение к self.marks - и переключение на class Marks
        pass

class Marks:

    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('call_iter_from_class_Marks')
        if self.index >= len(self.values)-1:
            raise StopIteration
        self.index +=1
        return self.values[self.index]


m = Marks([5,4,3,3,4,5,6])
igor = Student('Igor', 'Nikolaev', m)
for i in igor:
    print(i)
