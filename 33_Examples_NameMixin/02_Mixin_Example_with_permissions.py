# Миксин для доступов
#
# Разрешения в операционной системе  это права доступа, которые определяют,
# какие действия могут быть выполнены в рамках системы. Разрешения могут
# ограничивать использование определенного программного обеспечения, доступ к
# файлам и настройки системы безопасности. Давайте мы создадим миксин, который
# имитирует управления правами доступами.
#
# Для этого создайте класс PermissionMixin, который будет иметь следующие методы:
#
# __init__(self): метод инициализации, который создает множество permissions для
# хранения разрешений. В него мы будем сохранять действия, которые будут доступны
# пользователям, например Чтение, Запись, Выполнение и т.д.

class PermissionMixin:

    def __init__(self):
        self.permissions = set()

    def grant_permission(self, permission):
        self.permissions.add(permission)
#
# grant_permission(self, permission): метод для назначения разрешения.
# Добавляет переданное разрешение в множество permissions
#
# revoke_permission(self, permission): метод для отмены разрешения.
# Удаляет переданное разрешение из множества permissions
#
# has_permission(self, permission): метод для проверки наличия разрешения.
# Возвращает True, если переданное разрешение присутствует в множестве
# permissions, и False в противном случае.
#
    def revoke_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)

    def has_permission(self, permission):
        return permission in self.permissions

# Создайте класс User, который будет наследоваться от PermissionMixin и иметь следующие атрибуты:
# name: имя пользователя.
# email: email пользователя.

class User(PermissionMixin):

    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email

# Ниже код для проверки миксина PermissionMixin
user1 = User('Alice', 'alice@example.com')
user2 = User('Bob', 'bob@example.com')

assert user1.email == 'alice@example.com'
assert user1.name == 'Alice'
assert user1.permissions == set()

assert user2.email == 'bob@example.com'
assert user2.name == 'Bob'
assert user2.permissions == set()


user1.grant_permission('read')
user1.grant_permission('write')
user2.grant_permission('read')
assert user1.permissions == {'read', 'write'}
assert user2.permissions == {'read'}

assert user1.has_permission('read') is True
assert user1.has_permission('write') is True
assert user1.has_permission('execute') is False

assert user2.has_permission('read') is True
assert user2.has_permission('write') is False
assert user2.has_permission('execute') is False

user1.revoke_permission('write')
user1.revoke_permission('execute')

assert user1.has_permission('read') is True
assert user1.has_permission('write') is False
assert user1.has_permission('execute') is False

print('Good')