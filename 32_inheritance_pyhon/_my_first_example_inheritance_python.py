class Person: #parent

    def __init__(self, name):
        self.name = name


    def can_talk(self):
        print(f'{self.name} I can talk')


    def can_walk(self):
        print(f'{self.name} I can walk')

# a = Person('Vasja')
# a.can_talk()
# a.can_walk()


class Doctor(Person): #subclass

    def can_cure(self):
        print(f'{self.name} I can cure')


# a = Person('Vasja')
# a.can_talk()
# a.can_walk()

# b = Doctor('Blo-Blo')
# b.can_cure()
# b.can_talk()
# b.can_walk()

class Dentist(Doctor):

    def can_cure_teeth(self):
        print(f'{self.name} I can cure teeth')

l = Dentist('Lyena')
l.can_cure_teeth()
l.can_cure()
l.can_talk()
l.can_walk()

print(issubclass(Dentist, Doctor)) #True
print(issubclass(Doctor, Dentist)) #False

print(issubclass(Dentist, Person)) #True
