# Сериализация класса
#
# Ваша задача научить классы конвертиться к json-строке
# при помощи миксина под названием JsonSerializableMixin,
# который добавляет метод to_json() в любой класс,
# использующий этот миксин. Метод to_json() конвертирует
# словарь атрибутов экземпляра в строку JSON, используя
# стандартную библиотеку json в Python.

import json

class JsonSerializableMixin:

    def to_json(self):

        return json.dumps(self.__dict__)


# Ниже код для проверки миксина JsonSerializableMixin
class Car(JsonSerializableMixin):
    def __init__(self, make: str, color: str):
        self.make = make
        self.color = color


class Book(JsonSerializableMixin):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class Person(JsonSerializableMixin):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


car = Car("Toyota", "red")
assert car.to_json() == '{"make": "Toyota", "color": "red"}'

book = Book("The Catcher in the Rye", "J.D. Salinger")
assert book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger"}'
book.ratings = [5, 4, 5, 4, 5]
book.is_bestseller = True
book.to_json() == '{"title": "The Catcher in the Rye", "author": "J.D. Salinger", "ratings": [5, 4, 5, 4, 5], "is_bestseller": true}'

person = Person("John", 30)
assert person.to_json() == '{"name": "John", "age": 30}'
print('Good')