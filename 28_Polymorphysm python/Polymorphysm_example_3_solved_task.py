# #THE TASK
#
# Создайте класс UnitedKingdom, у которого необходимо реализовать:
#
# статический метод capital, который печатает строку "London is the capital of Great Britain."
#
# статический метод language, который печатает строку "English is the primary language of Great Britain."
#
# Создайте класс Spain, у которого необходимо реализовать:
#
# статический метод capital, который печатает строку "Madrid is the capital of Spain."
#
# статический метод language, который печатает строку "Spanish is the primary language of Spain."

class UnitedKingdom:

    @staticmethod
    def capital():
        print('London is the capital of Great Britain.')

    @staticmethod
    def language():
        print('English is the primary language of Great Britain.')


class Spain:

    @staticmethod
    def capital():
        print('Madrid is the capital of Spain.')

    @staticmethod
    def language():
        print('Spanish is the primary language of Spain.')

obj_uk = UnitedKingdom()
obj_spa = Spain()
for country in (obj_spa, obj_uk):
    country.capital()
    country.language()