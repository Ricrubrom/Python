# sets: unordered, mutable, no duplicates
# myset = {1, 2, 3, 1, 2}  # same as dictionaries but with no key-pairs
# myset = set('hello')
# print(myset)

# myset = set()  # only way to have an empty set
# myset.add(2)
# myset.add(1)
# myset.add(3)

# myset.remove(2)
# # does the same as remove but does not raise an error when it is not in the set
# myset.discard(4)

# print(myset)

# print(myset.pop())  # returns and removes the last element in the set

# myset.clear()  clears the set

# print(myset)

# for i in myset:
#     print(i)

# if 1 in myset:
#     print('yes')


# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# u = odds.union(evens)  # union
# print(u)

# i = odds.intersection(primes)    #intersection
# print(i)

# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {1, 2, 3, 10, 11, 12}

# # removes the ones that both sets have, and keeps the uniques to the set that called the functions
# d = a.difference(b)
# print(d)

# # prints the elements that are unique to each set
# diff = b.symmetric_difference(a)
# print(diff)

# a.update(b)  # adds both sets
# print(a)

# a.intersection_update(b)  # only prints the intersection
# print(a)

# a.difference_update(b)  # only prints the elements unique to a
# print(a)

# a.symmetric_difference_update(b)  # prints the elements unique to both sets
# print(a)

# a = {1, 2, 3, 4, 5, 6}
# b = {1, 2, 3}

# print(b.issubset(a))  # prints if it is a subset or not
# print(a.issuperset(b))  # prints if it is a superset or not
# print(a.isdisjoint(b))  # prints if true if they dont have nothing in common

# a = frozenset([1, 2, 3, 4, 5])  #it is not possible to change this set
# print(a)
