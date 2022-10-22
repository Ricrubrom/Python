# lambda functions: lambda (arguments): expression
from functools import reduce


def add10(x): return x+10
#add10=lambda x: x+10


print(add10(2))


def mult(x, y): return x*y
#mult=lambda x,y:x*y


print(mult(2, 7))


# sorted
p2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
p2ds = sorted(p2d, key=lambda x: x[0] + x[1])
print(p2d)
print(p2ds)


# map(func,seq)
a = [1, 2, 3, 4, 5]
b = list(map(lambda x: x*2, a))
print(b)

c = [x*2 for x in a]  # better
print(c)


# filter(func,seq)
a = [1, 2, 3, 4, 5, 6]
b = list(filter(lambda x: x % 2 == 0, a))
print(b)

c = [x for x in a if x % 2 == 0]
print(c)


# reduce(func,seq)
a = [1, 2, 3, 4]
prod = reduce(lambda x, y: x*y, a)
print((prod))
