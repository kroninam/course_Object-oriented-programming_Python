from class_def import Rectangle, Square, Circle

r1 = Rectangle(2, 4)
r2 = Rectangle(60, 80)

# print(r1.get_rect_area())
# print(r2.get_rect_area())

s1 = Square(8)
s2 = Square(0.8)

c1 = Circle(8)
c2 = Circle(0.8)

list_area = [r1, r2, s1, s2, c1, c2 ]
# Without Polymorphysm:
# for i in list_area:
#     if isinstance(i, Rectangle):
#         print (i.get_rect_area())
#     elif isinstance(i, Square):
#         print(i.get_sqare_area())
#     elif isinstance(i, Circle):
#         print(i.get_cir_area())

# Using Polymorphysm:
for i in list_area:
    print (i.get_area())

for i in list_area:
    print (i)