# # # # Артем Егоров
# # # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # # //www.youtube.com/c/egoroffchannel
#
# # Вычесляемы свойства. Property.

# # # # Артем Егоров
# # # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # # //www.youtube.com/c/egoroffchannel
#
# # Вычесляемы свойства. Property.

## AN EXAMPLE

class Square:

    def __init__(self, s):
        self.side = s
        self.__sqr_one = None

    @property
    def sqr(self):
        if self.__sqr_one is None:
            print('calculate area_1')
            self.__sqr_one = self.side**2
        return self.__sqr_one

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, ss):
        self.__side = ss
        self.__sqr_one = None

a = Square(10)
print(a.sqr)
print(a.sqr)
a.side = 4
print(a.sqr)


## THE TASK

#Создайте класс Rectangle, у которого есть:

# конструктор __init__, принимающий 2 аргумента: длину и ширину.

# свойство area, которое возвращает площадь прямоугольника;

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        self.srea = self.length * self.width
        return self.srea

r1 = Rectangle(5, 10)
assert isinstance(r1, Rectangle)
assert r1.area == 50
assert isinstance(type(r1).area, property), 'Вы не создали property area'

r2 = Rectangle(15, 3)
assert isinstance(r2, Rectangle)
assert r2.area == 45
assert isinstance(type(r2).area, property), 'Вы не создали property area'

r3 = Rectangle(43, 232)
assert r3.area == 9976
print('Good')

# NEXT TASK

# Создайте класс Password, который имеет:
#
# метод __init__, который устанавливает значение атрибута password
#
# вычисляемое свойство strength, которое определяет стойкость пароля.
# Если длина пароля меньше 8 символов, то такой пароль считается слабым,
# свойство должно вернуть строку  "Weak". Сильным паролем считается тот,
# в котором длина символов 12 и более, в таком случае свойство возвращает
# строку "Strong". Во всех остальных случаях необходимо вернуть "Medium"

class Password:

    def __init__(self, password):
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pass):
        self.__password = new_pass

    @property
    def strength(self):
        if len(self.__password) < 8:
            return f"Weak"
        elif len(self.__password) >= 12:
            return f"Strong"
        else:
            return f"Medium"

# Ниже код для проверки методов класса Password
pass_1 = Password("Alligator34")
assert pass_1.password == "Alligator34"
assert pass_1.strength == "Medium"
assert len(pass_1.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

pass_2 = Password("Alligator345678")
assert pass_2.password == "Alligator345678"
assert pass_2.strength == "Strong"
pass_1.password = "123"
assert pass_1.strength == "Weak"
assert len(pass_2.__dict__) == 1, 'У ЭК должен храниться только один атрибут'

pass_3 = Password("345678")
assert pass_3.strength == "Weak"
print('Good')
assert len(pass_3.__dict__) == 1, 'У ЭК должен храниться только один атрибут'





