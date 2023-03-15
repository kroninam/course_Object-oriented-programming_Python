# methods __getitem__,__setitem__&__delitem__

class Vector():

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
       return (f'{self.values}')

    def __getitem__(self, item):
        if 0<=item<len(self.values):
            return self.values[item]
        else:
            raise (IndexError)

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        elif key >= len(self.values):
            diff = key+1 - len(self.values)
            self.values.extend([0]*diff)
            self.values[key] = value

        else:
            raise (IndexError)

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise (IndexError)

v = Vector(1, 2, 3)
print(v.values)
print(v.__repr__())

v2 = Vector(1,4,6,8,67)
print(v2[4])
################################
v2[4] = 100
print(v2[4])
#######################################
print(v2.values)
del v2[4]
print(v2.values)
#########################################

v3 = Vector(1,2,3)
v3[30] = 5
print(v3.__repr__())