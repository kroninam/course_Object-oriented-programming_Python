class BasePizza:
    BASE_PIZZA_PRICE = 15

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.toppings = ['cheese']

    def __str__(self):
        return f"{self.name} with {self.toppings}, ${self.price:.2f}"


class PepperoniMixin:
    def add_pepperoni(self):
        print("Adding pepperoni!")
        self.price += 5
        self.toppings += ['pepperoni']


class MushroomMixin:
    def add_mushrooms(self):
        print("Adding mushrooms!")
        self.price += 3
        self.toppings += ['mushrooms']


class OnionMixin:
    def add_onion(self):
        print("Adding onion!")
        self.price += 2
        self.toppings += ['onion']


class BaconMixin:
    def add_bacon(self):
        print("Adding bacon!")
        self.price += 6
        self.toppings += ['bacon']


class OlivesMixin:
    def add_olives(self):
        print("Adding olives!")
        self.price += 1
        self.toppings += ['olives']


class OlivesPizza(BasePizza, OlivesMixin):

    def __init__(self):
        super().__init__('Море оливок', BasePizza.BASE_PIZZA_PRICE)
        self.add_olives()


class PepperoniPizza(BasePizza, PepperoniMixin):

    def __init__(self):
        super().__init__('Колбасятина', BasePizza.BASE_PIZZA_PRICE)
        self.add_pepperoni()


class MushroomOnionBaconPizza(BasePizza, MushroomMixin, OnionMixin, BaconMixin):

    def __init__(self):
        super().__init__('Грибной пяточок с луком', BasePizza.BASE_PIZZA_PRICE)
        self.add_mushrooms()
        self.add_onion()
        self.add_bacon()

class HamMixin:
    def add_olives(self):
        print("Adding ham!")
        self.price += 5
        self.toppings += ['ham']

class HamMixin:
    def add_ham(self):
        print("Adding ham!")
        self.price += 5
        self.toppings += ['ham']

class PepperMixin:
    def add_pepper(self):
        print("Adding pepper!")
        self.price += 5
        self.toppings += ['pepper']

class ChickenMixin:
    def add_chicken(self):
        print("Adding chicken!")
        self.price += 5
        self.toppings += ['chicken']



# Создайте экземпляр CountryPizza в переменной pizza
class CountryPizza(BasePizza, HamMixin, PepperMixin, OlivesMixin, PepperoniMixin, MushroomMixin, ChickenMixin):
    def __init__(self):
        super().__init__('Деревенская пицца', BasePizza.BASE_PIZZA_PRICE)
        self.add_ham()
        self.add_pepper()
        self.add_olives()
        self.add_pepperoni()
        self.add_mushrooms()
        self.add_chicken()


pizza = CountryPizza()

# Код для проверки

assert pizza.name == 'Деревенская пицца'
assert pizza.price == 39
assert pizza.toppings == ['cheese', 'ham', 'pepper', 'olives', 'pepperoni', 'mushrooms', 'chicken']
print(pizza)