# # # # Артем Егоров
# # # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # # //www.youtube.com/c/egoroffchannel
#
# # ДЕКОРАТОР Property.

# THE TASK

# Создайте класс Notebook, у которого есть:
#
# конструктор __init__, принимающий список записей, в нем могут находиться любые значения.
# Необходимо сохранить его в защищенном атрибуте ._notes
#
# свойство notes_list, которое распечатает содержимое атрибута ._notes в виде упорядоченного списка (см. пример ниже)
#
# note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
# note.notes_list
#
# После этого на экране вы должны увидеть:
# 1.Buy Potato
# 2.Buy Carrot
# 3.Wash car.

class Notebook:

    def __init__(self, *args):
        self._notes = []
        for i in args:
            for j in i:
                self._notes.append(j)

    @property
    def notes_list(self):
        for i in range(len(self._notes)):
            print(str(i+1) + '.' + str(self._notes[i]))

note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list

# NEXT TASK

# Создайте класс Money, у которого есть:

# конструктор __init__, принимающий 2 аргумента: dollars, cents.
# По входным аргументам вам необходимо создать атрибут экземпляра total_cents.

# свойство геттер dollars, которое возвращает количество имеющихся долларов;

# свойство сеттер dollars, которое принимает целое неотрицательное число -
# количество долларов и устанавливает при помощи него новое значение в атрибут
# экземпляра total_cents, при этом значение центов должно сохранятся.
# В случае, если в сеттер передано число, не удовлетворяющее условию,
# нужно печатать на экран сообщение "Error dollars";

# свойство геттер cents, которое возвращает количество имеющихся центов;
#
# свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100
# - количество центов и устанавливает при помощи него новое значение в атрибут
# экземпляра total_cents, при этом значение долларов должно сохранятся.
# В случае, если в сеттер передано число, не удовлетворяющее условию,
# нужно печатать на экран сообщение "Error cents";
#
# метод __str__ (информация по данному методу), который возвращает
# строку вида "Ваше состояние составляет {dollars} долларов {cents} центов".
# Для нахождения долларов и центов в методе __str__ пользуйтесь свойствами.

class Money:
    def __init__(self, dollars, cents):
        self.total_cents = int(dollars*100) + int(cents)

    @property
    def dollars(self):
        return int(self.total_cents//100)

    @dollars.setter
    def dollars(self, summa):
        if type(summa) == int and summa >= 0:
            self.total_cents = self.total_cents - (self.total_cents//100)*100 + summa*100

        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents - (self.total_cents//100)*100

    @cents.setter
    def cents(self, summa_cents):
        if type(summa_cents) == int and summa_cents < 100:
            self.total_cents = (self.total_cents//100)*100 + summa_cents
        else:
            print("Error cents")

    def __repr__(self):
        return f'То, как увидет информацию разработчик'
    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'

Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents) # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов


# NEXT TASK
