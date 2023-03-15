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

d = Dog('Bob')
c = Cat('Blo-Blo')

print(d.name, d.sound(), d.say_hello())
print(c.name, c.sound(), c.say_hello())

