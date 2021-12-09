s ='Hello_World!'[7:4:-1]
my_list = [1, 2, 3, 4, 5]
my_number = 3

s = 'dwywywdwywbwhsjhwuwshshwuwwwjtjtit'


s = 'dwywywdwywbwhsjhwuwshshwuwwwjtjtit'
a = (1, 2, 3, 4, 5)
b = 'abcde'
c = tuple(b)


set1 = {2,3,1,5,6,8,99}
set2 = {3,1,7,5,6,8}

d = {'k1':[{'inter':['deep',['hello']]}]}

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]






# class C:
#     def __len__(self):
#         return 42
# c = C()
# print(len(c))

# class C:
#     __a = 42
# c = C()
# print(c._C__a)

# class C:
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return 42
#
# for el in C():
#     print(el)


# for i in range(3,0,-1):
#     print(i)

from geometry.point import *

point1 = Point(0, 0)

from geometry.figures.line import *

point1 = Point(0, 0)

point2 = Point(0, 1)

my_line = Line(point1, point2)
print(my_line)



from geometry.figures.triangle import *

point1 = Point(0, 0)

point2 = Point(0, 1)

point3 = Point(1, 0)

my_triangle = Triangle(point1, point2, point3)

print(my_triangle.square())

s = "привет"
print(s[0:1])
