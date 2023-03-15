def main(name):
    def inner_func():
        print('hello my friend', name)
    return inner_func

r = main('Misha')
r()
b = main('Vasja')

b()
b()
b()
r()

print(__name__)

print('hooollllaaa')