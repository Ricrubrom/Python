# itertool: product, permutations, combinations, accumulate, groupby, infinite iterators


from itertools import groupby
from itertools import combinations, combinations_with_replacement
from itertools import product
from itertools import permutations
from itertools import accumulate
import operator
from itertools import count, cycle, repeat

# product
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)  # "distributes"
print(list(prod))


# permutations
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# returns all possible permutations, second argument specifies the size of the permutation
perm = permutations(a, 1)
print(list(perm))

# combinations
a = [1, 2, 3, 4]
comb = combinations(a, 2)  # returns all possible combinations
print(list(comb))
cwr = combinations_with_replacement(a, 2)
print(list(cwr))

# accumulate
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))


# groupby

def less3(x):
    return x < 3


a = [1, 2, 3, 4]
# key is a function that returns if it is less than 3 or not
go = groupby(a, key=lambda x: x < 3)
for key, value in go:
    print(key, list(value))


# infinite iterators
for i in count(10):  # starts at 10 and goes up, doesnt stop
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):  # cycles through the iterable and doesnt stop
    print(i)
    if i == 3:
        break

for i in repeat(1, 4):  # repeats the number given infinitely, second argument is the ammount of times it is repeated
    print(i)
