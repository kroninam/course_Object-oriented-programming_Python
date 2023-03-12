#
# Создайте класс Hero, который имеет следующие методы:
#
# метод __len__, который возвращает количество атрибутов экземпляра
#
# приватный метод __str__, который возвращает строковое представление героя.
# Для этого нужно перечислить все атрибуты в алфавитном порядке на отдельной
# строке, напротив каждого атрибута указать его значение. Вот такой формат
# должен получится:
#
# атрибут_1: значение_атрибут_1
# атрибут_2: значение_атрибут_2
# ...
# атрибут_N: значение_атрибут_N
#
# Если у экземпляра нету атрибутов, необходимо вернуть пустую строку

class Hero:

    def __len__(self):
        return len(self.__dict__) # такой важный метод __dict__ (привет 12.марта.2023)

    def __str__(self):
        if self.__len__() == 0:
            return ''
        else:
            ans: str = ''
            for k, w in sorted(self.__dict__.items(), key=lambda x: x[0]):
               ans += f"{k}: {str(w) }\n"

            return ans.rstrip('\n') # такой важный метод "rstrip('\n')", который отрезает '\n' у "last child"

# Ниже код для проверки методов класса Hero
hero = Hero()
assert len(hero) == 0
hero.health = 50
hero.damage = 10
assert len(hero) == 2
assert str(hero) == '''damage: 10
health: 50'''
hero.weapon = ['sword', ' bow']
hero.skill = 'Некромант'
assert str(hero) == '''damage: 10
health: 50
skill: Некромант
weapon: ['sword', ' bow']'''
print(hero)

villain = Hero()
assert str(villain) == ''
assert len(villain) == 0
villain.level = 15
villain.skill = 'Боец'
villain.armor = 25
assert len(villain) == 3
assert str(villain) == '''armor: 25
level: 15
skill: Боец'''
print(villain)