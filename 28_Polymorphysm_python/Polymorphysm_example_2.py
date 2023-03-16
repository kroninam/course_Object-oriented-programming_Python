class Dog:

    def __init__(self, name):
        self.name = name

    def sound(self):
        return 'Bark'

    def say_hello(self):
        return f'Hello, my name is {self.name}'


class Cat:

    def __init__(self, name):
        self.name = name

    def sound(self):
        return 'Meow'

    def say_hello(self):
        return f'Hello, my name is {self.name}'

dog = Dog('Bob')
cat = Cat('Blo-Blo')

print(dog.name, dog.sound(), dog.say_hello())
print(cat.name, cat.sound(), cat.say_hello())

animals = [dog, cat]
for animal in animals:
    print(animal.sound())
    print(animal.say_hello())

