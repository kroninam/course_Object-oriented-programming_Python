# Класс DictMixin представляет собой миксин, который добавляет в
# класс, наследующий его, метод to_dict().
# Этот метод позволяет преобразовать объект в словарь.
#
# Внутри класса DictMixin вы можете создавать сколько угодно
# служебных методов и атрибутов, которые помогут вам справиться
# с задачей. Главное, это реализовать метод to_dict(), он являться
# точкой входа для взаимодействия с вашим миксином и он должен
# вернуть представление вашего объекта в виде словаря.
# Обратите внимание на вложенность атрибутов.

# Напишите определение класса DictMixin

class DictMixin:

    answer_d= {}
    answer_d_2 = {}

    def to_dict_2(self):
        self.answer_d_2 = {}
        for k, w in self.__dict__.items():
            if type(w) == str or type(w) == int:
                self.answer_d_2[k] = w
            elif type(w) == dict:
                pass
            else:
                self.answer_d_2[k] = w.__dict__
        # self.ans_dict.clear()
        # self.ans_dict_2 = DictMixin.answer_d_2
        # DictMixin.answer_d.clear()
        return self.answer_d_2


    def to_dict(self):
        DictMixin.answer_d.clear()

        for k, w in self.__dict__.items():
            if type(w) == str or type(w) == int:
                DictMixin.answer_d[k] = w
            elif type(w) == dict:
                pass
            elif type(w) == list:
                new_list = []
                for i in w:
                    x = i.to_dict_2()
                    new_list.append(x)
                # print(new_list)

                    # DictMixin.answer_d.clear()
                DictMixin.answer_d.setdefault(k, new_list)

            else:
                DictMixin.answer_d[k] = w.__dict__
        # self.ans_dict.clear()
        self.ans_dict = DictMixin.answer_d
        # DictMixin.answer_d.clear()
        return self.ans_dict

# Ниже код для проверки миксина DictMixin
# Ниже код для проверки миксина DictMixin

class Phone(DictMixin):
    def __init__(self, number):
        self.number = number


class Person(DictMixin):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(DictMixin):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(DictMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address


address = Address("123 Main St", "Anytown", "CA", "12345")
john_doe = Person("John Doe", 30, address)

john_doe_dict = john_doe.to_dict()

assert john_doe_dict == {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip_code': '12345'
    }
}

address = Address("123 Main St", "Albuquerque", "NM", "987654")
assert address.to_dict() == {
    'street': '123 Main St',
    'city': 'Albuquerque',
    'state': 'NM',
    'zip_code': '987654'
}
walter = Person("Walter White", 30, address)
assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': '123 Main St',
                                        'zip_code': '987654'},
                            'age': 30,
                            'name': 'Walter White'}

walter_phone = Phone("555-1234")
walter.phone = walter_phone
assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': '123 Main St',
                                        'zip_code': '987654'},
                            'age': 30,
                            'name': 'Walter White',
                            'phone': {'number': '555-1234'}}

company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
company = Company("SCHOOL", company_address)

assert company.to_dict() == {'address': {'city': 'Albuquerque',
                                         'state': 'NM',
                                         'street': '3828 Piermont Dr',
                                         'zip_code': '12345'},
                             'name': 'SCHOOL'}

jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
jesse.phone = Phone("555-5678")

fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
fring.friends = [walter, jesse]

assert fring.to_dict() == {'address': {'city': 'Albuquerque',
                                       'state': 'NM',
                                       'street': 'Los Pollos Hermanos',
                                       'zip_code': '12345'},
                           'age': 55,
                           'friends': [{'address': {'city': 'Albuquerque',
                                                    'state': 'NM',
                                                    'street': '123 Main St',
                                                    'zip_code': '987654'},
                                        'age': 30,
                                        'name': 'Walter White',
                                        'phone': {'number': '555-1234'}},
                                       {'address': {'city': 'Albuquerque',
                                                    'state': 'NM',
                                                    'street': '456 Oak St',
                                                    'zip_code': '12345'},
                                        'age': 27,
                                        'name': 'Jesse Bruce Pinkman',
                                        'phone': {'number': '555-5678'}}],
                           'name': 'Gustavo Fring'}

print('Good')