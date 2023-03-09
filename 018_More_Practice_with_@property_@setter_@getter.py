## # # # Артем Егоров
# # # # Автор и бессменный ведущий образовательного канала по разработке на Python https:
# # # # //www.youtube.com/c/egoroffchannel

# Practice with @property, @setter, @getter
#
#
# Задача Корзина
#
# Давайте реализуем ситуацию создания файлов и перемещения их в корзину. Задача будет состоять из двух частей
#
# Часть 1
#
# Создайте класс  File, у которого есть:
#
# метод __init__, который должен принимать на вход имя файла и записывать его в атрибут name.
# Также необходимо создать атрибуты in_trash , is_deleted  и записать в них значение False
#
# метод  restore_from_trash, который печатает фразу «Файл {name} восстановлен из корзины» и
# проставляет атрибут in_trash в значение False
#
# метод  remove, который печатает фразу «Файл {name} был удален» и проставляет атрибут is_deleted  в значение True
#

# метод read, который
# печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
# печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
# печатает фразу «Прочитали все содержимое файла {self.name}» если файл не удален и не в корзине
#

# метод write, который принимает значение content для записи и
# печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
# печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
# печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине
class File:

    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted == True:
            print(f'ErrorReadFileDeleted{self.name})')
            return
        elif self.in_trash == True:
            print(f'ErrorReadFileTrashed({self.name})')
            return
        else:
            print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted == True:
            print(f'ErrorWriteFileDeleted({self.name})')
            return
        elif self.in_trash == True:
            print(f'ErrorWriteFileTrashed({self.name})')
            return
        else:
            print(f'Записали значение {content} в файл {self.name}')

# Ниже код для проверки класса File



f1 = File('puppies.jpg')
assert f1.name == 'puppies.jpg'
assert f1.in_trash is False
assert f1.is_deleted is False

f1.read()  # Прочитали все содержимое файла puppies.jpg
f1.remove()  # Файл puppies.jpg был удален
assert f1.is_deleted is True
f1.read()  # ErrorReadFileDeleted(puppies.jpg)

passwords = File('pass.txt')
assert passwords.name == 'pass.txt'
assert passwords.in_trash is False
assert passwords.is_deleted is False

f3 = File('xxx.doc')

assert f3.__dict__ == {'name': 'xxx.doc', 'in_trash': False, 'is_deleted': False}
f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.in_trash = True
f3.is_deleted = False
f3.read()
f3.write('hello')
f3.restore_from_trash()
assert f3.in_trash is False
f3.write('hello')  # Записали значение «hello» в файл cat.jpg

f2 = File('cat.jpg')
f2.write('hello')  # Записали значение «hello» в файл cat.jpg
f2.write([1, 2, 3])  # Записали значение «hello» в файл cat.jpg
f2.remove()  # Файл cat.jpg был удален
f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)



# Задача Корзина

# Часть 2

# С предыдущего урока у вас должен быть создан класс  File, у которого имеется:
#
# метод __init__
# метод  restore_from_trash
# метод  remove
# метод read
# метод write
class File:

    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted == True:
            print(f'ErrorReadFileDeleted({self.name})')
            return
        elif self.in_trash == True:
            print(f'ErrorReadFileTrashed({self.name})')
            return
        else:
            print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted == True:
            print(f'ErrorWriteFileDeleted({self.name})')
            return
        elif self.in_trash == True:
            print(f'ErrorWriteFileTrashed({self.name})')
            return
        else:
            print(f'Записали значение {content} в файл {self.name}')

# Далее создайте класс  Trash у которого есть:
#
# атрибут класса  content изначально равный пустому списку
#
# статик-метод  add, который принимает файл и сохраняет его в корзину: для этого
# нужно добавить его в атрибут content и проставить файлу атрибут in_trash значение
# True. Если в метод add передается не экземпляр класса File, необходимо вывести
# сообщение «В корзину добавлять можно только файл»

class Trash:
    content = []

    @staticmethod
    def add(file):
        if not isinstance(file, File):
            print(f'В корзину добавлять можно только файл')
        else:
            Trash.content.append(file)
            file.in_trash = True

#
# статик-метод  clear, который запускает процесс очистки файлов в корзине.
# Необходимо для всех файлов, хранящийся в атрибуте content , в порядке их
# добавления в корзину вызвать метод файла remove. Атрибут content  после
# очистки должен стать пустым списком. Сама процедура очистки должна начинаться
# фразой «Очищаем корзину» и заканчиваться фразой «Корзина пуста»

    @staticmethod
    def clear():
        print(f'Очищаем корзину')
        # for i in range(len(Trash.content)-1):
        #     Trash.content[i].is_deleted = True
        #     File.remove(Trash.content[i])
        #     Trash.content.remove(Trash.content[i])

        while len(Trash.content) != 0:
            Trash.content[0].is_deleted = True
            File.remove(Trash.content[0])
            Trash.content.remove(Trash.content[0])
        print(f'Корзина пуста')

#
# статик-метод  restore, который запускает процесс восстановления файлов из корзины.
# Необходимо для всех файлов, хранящийся в атрибуте content , в порядке их добавления
# в корзину вызвать метод файла restore_from_trash. Атрибут content  после очистки должен
# стать пустым списком. Сама процедура восстановления должна начинаться фразой
# «Восстанавливаем файлы из корзины» и заканчиваться фразой «Корзина пуста»

    @staticmethod
    def restore():
        print(f'Восстанавливаем файлы из корзины')

        while len(Trash.content) != 0:
            File.restore_from_trash(Trash.content[0])
            Trash.content.remove(Trash.content[0])

        print(f'Корзина пуста')

# Ниже код для проверки класса File и Trash

f1 = File('puppies.jpg')
f2 = File('cat.jpg')
f3 = File('xxx.doc')
passwords = File('pass.txt')

for file in [f1, f2, f3, passwords]:
    assert file.is_deleted is False
    assert file.in_trash is False

f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.write('hello')

assert Trash.content == []

Trash.add(f2)
Trash.add(passwords)
Trash.add(f3)

f1.read()
Trash.add(f1)
f1.read()

for file in [f1, f2, f3, passwords]:
    assert file.in_trash is True

for f in [f2, passwords, f3, f1]:
    assert f in Trash.content

Trash.restore()
assert Trash.content == [], 'После восстановления корзина должна была очиститься'

Trash.add(passwords)
Trash.add(f2)
Trash.add('hello')
Trash.add(f1)

for f in [passwords, f2, f1]:
    assert f in Trash.content


Trash.clear()

for file in [passwords, f2, f1]:
    assert file.is_deleted is True

assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'

f1.read()