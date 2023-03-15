# methods __getitem__ __setitem__ & __delitem__

# THE TASK

# Необходимо создать класс Building. Мы должны научиться создавать здание определенной
# этажности и уметь бронировать за компанией определенный этаж в здании.
# Важно, что в нашем классе за одним этажом может быть закреплена только одна компания.
#
# Для этого в классе Building должно быть реализованы:
#
# метод __init__, который принимает количество этажей в здании
#
# метод __setitem__, который закрепляет за определенным этажом компанию.
# Если этаж был занят другой компанией, нужно заменить название другой компанией
#
# метод __getitem__, который возвращает название компании с этого этажа.
# В случае, если этаж пустует, следует вернуть None
#
# метод __delitem__, который высвобождает этаж

class Building:

    def __init__(self, floor):
        self.height = []
        self.height.extend([None] * floor)

    def __setitem__(self, key, value):
        if 0 <= key < len(self.height):
            self.height[key] = value

    def __getitem__(self, item):
        if 0 <= item < len(self.height):
            return self.height[item]

    def __delitem__(self, key):
        if 0 <= key < len(self.height):
            self.height[key] = None


# b = Building(5)
# print(b.height)

iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])

# EXAMPLE WITH DICTIONARY & __getitem__ __setitem__ __delitem__

class Dict:

    def __init__(self, **kwargs):
        self.values = kwargs

    def __str__(self):
        return str(self.values)

    def __setitem__(self, key, value):
        self.values[key] = value

    def __getitem__(self, item):
        return self.values[item]

a = Dict(a=1, b=2, c=3)
print(a)
a['d'] = 4
print(a)
print(a['a'])


# # THE TASK
# Аналог плейлиста
# Необходимо реализовать два класса Song и Playlist
#
# Класс Song должен содержать:

class Song:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
#
# метод __init__, который сохраняет в экземпляре два атрибута title и artist:
# название песни и исполнитель
#
# Класс Playlist должен содержать:
#
# метод __init__. , который создает в экземпляре атрибут songs.
# Изначально должен быть пустым списком;

class Playlist:
    def __init__(self):
        self.songs = []

# метод __getitem__ , который возвращает песню из атрибута songs по индексу
#
# метод __setitem__ , который добавляет песню в атрибут songs в указанный индекс.
# При этом нужно сдвинуть уже имеющиеся песни вправо, у которых индекс был
# до момента вставки равен или больше переданного
#
# метод add_song, который добавляет песню в конец плейлиста

    def __getitem__(self, item):
        return self.songs[item]

    def add_song(self, item):
        if isinstance(item, Song):
            self.songs.append(item)

    def __setitem__(self, key, value):
        if isinstance(value, Song):
            # first_part = self.songs[0:key-1]
            # rest_part = self.songs[key-1:]
            self.songs.insert(key, value)


# Ниже код для проверки методов классов Song и Playlist

playlist = Playlist()
assert len(playlist.songs) == 0
assert isinstance(playlist, Playlist)

s1 = Song("Paradise", "Coldplay")
playlist.add_song(s1)


assert playlist[0].title == 'Paradise'


assert playlist[0].artist == 'Coldplay'
assert len(playlist.songs) == 1
#
playlist[0] = Song("Resistance", "Muse")
assert playlist[0].title == 'Resistance'
assert playlist[0].artist == 'Muse'
assert playlist[1].title == 'Paradise'
assert playlist[1].artist == 'Coldplay'

playlist[1] = Song("Helena", "My Chemical Romance")
assert playlist[1].title == 'Helena'
assert playlist[1].artist == 'My Chemical Romance'

assert playlist[2].title == 'Paradise'
assert playlist[2].artist == 'Coldplay'
print('Good')

# #THE TASK
#
# В этой задаче мы создадим аналог корзины покупок и для этого нам понадобиться реализовать
# класс ShoppingCart. В нем должно содержаться следующее:
#
# метод __init__. , который создает в экземпляре атрибут items. Изначально должен быть пустым
# словарем, в нем будут содержаться покупки;

class ShoppingCart:

    def __init__(self):
        self.items = {}
#
# метод __getitem__ , который возвращает по названию товара его текущее количество или 0,
# если товар отсутствует в корзине

    def __getitem__(self, key):
        if key in self.items:
            return self.items[key]
        else:
            return 0
#
# метод __setitem__ , который проставляет по названию товара его количество в корзине.
# Если товар отсутствовал, его необходимо добавить, если присутствовал - нужно проставить ему новое количество
#
    def __setitem__(self, key, value):
        self.items[key] = value

# метод __delitem__ , который удаляет товар из корзины
#
    def __delitem__(self, key):
        del self.items[key]

# метод add_item, который добавляет товар к текущим. Это значит, что если товар уже присутствовал в корзине,
# то необходимо увеличить его количество. Если товар отсутствовал, нужно его добавить.
# Данный метод принимает обязательно название товара и необязательно его количество
# (по умолчанию количество равно 1).

    def add_item(self, item, value = 1):
        if item in self.items:
            self.items[item] += value
        else:
            self.items[item] = value

# метод remove_item, который удаляет некоторое количество товара из корзины.
# Если хотят удалить из корзины столько же товара, чем там имеется или больше,
# необходимо удалить его из корзины.  В остальных случаях уменьшаем количество
# товара на переденное количество. Данный метод принимает обязательно название
# товара и необязательно его количество (по умолчанию количество равно 1).
# Предусмотрите ситуацию, когда удаляемый товар отсутствует в корзине

    def remove_item(self, item, value = 1):
        if item in self.items:
            if self.items[item] < value:
                del self.items[item]
            else:
                self.items[item] -= value
        else:
            pass

# Ниже код для проверки методов класса ShoppingCart

# Create a new shopping cart
cart = ShoppingCart()

# Add some items to the cart
cart.add_item('Apple', 3)
cart.add_item('Banana', 2)
cart.add_item('Orange')

assert cart['Banana'] == 2
assert cart['Orange'] == 1
assert cart['Kivi'] == 0

cart.add_item('Orange', 9)
assert cart['Orange'] == 10

print("Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

cart['Apple'] = 5
cart['Banana'] = 7
cart['Kivi'] = 11
assert cart['Apple'] == 5
assert cart['Banana'] == 7
assert cart['Kivi'] == 11

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

# Remove an item from the cart
cart.remove_item('Banana')
assert cart['Banana'] == 6

cart.remove_item('Apple', 4)
assert cart['Apple'] == 1

cart.remove_item('Apple', 2)
assert cart['Apple'] == 0
assert 'Apple' not in cart.items

cart.remove_item('Potato')

del cart['Banana']
assert cart['Banana'] == 0
assert 'Banana' not in cart.items

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")