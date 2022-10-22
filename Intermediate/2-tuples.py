import sys
import timeit

# ordered,inmutable,allows duplicates
# parenthesis are optional, if you want only one element in a tuple you have to put it like mytuple=('Max',)
# mytuple = ('Max', 28, 'Boston')
# # mytuple=tuple(['Max',28,'Boston'])
# print(mytuple)

# item = mytuple[1]  # how to access each position
# print(item)

# for i in mytuple:
#     print(i)

# if 'Max' in mytuple:
#     print('yes')
# else:
#     print('no')

# mytuple = ('a', 'p', 'p', 'l', 'e')
# print(len(mytuple))  # prints length
# print(mytuple.count('p'))  # returns the ammount of times an element appears
# print(mytuple.index('p'))  # returns the first occurrance of the element
# # returns a list version of the tuple, can be reversed using mytuple2=tuple(mylist)
# mylist = list(mytuple)

# a=(1,2,3,4,5,6,7,8,9)
# b=a[1:5] # slicing, if [:5] starts from beginning and stops at index 5, if [1:] starts from 1 and copies the rest of the indexes, if [:] copies the entire tuple
# # b = mylist[::2]  # the difference between each number copied
# print(b)

# mytuple = ('Max', 28, 'Boston')
# name, age, city = mytuple  # unpacking, returns variables with the data inside the tuple, has to be the exact same ammount of items in the tupple
# print(name, age, city)

# mytuple = (0, 1, 2, 3, 4)
# i1, *i2, i3 = mytuple
# # i2 holds the data between i1=0 and i3=4, so i2=[1,2,3] (it's a list)
# print(i1, i2, i3)

# mylist = [0, 1, 2, 'hello', True]
# mytuple = (0, 1, 2, 'hello', True)
# print(sys.getsizeof(mylist), 'bytes')
# # tuples are more optimized than lists, so sometimes it is better to work with tuples
# print(sys.getsizeof(mytuple), 'bytes')

# print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
# # tuples are also faster to load
# print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))
