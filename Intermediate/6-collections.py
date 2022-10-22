# collections: Counter, namedtuple, orderedDict, defaultdict, deque

# from collections import defaultdict
# from collections import namedtuple
# from collections import Counter
# from collections import deque


# # counters
# a = 'aaaaabbbbbcccccc'
# # returns a dictionary with each individual letter as a key, and the data stored is the ammount of times it appears in the string
# # since it is a dictionary, you can do everything you could do with dictionaries
# counter = Counter(a)
# print(counter)
# # returns the most common element in the dict, (1)=results given, 1[0]=first position of the list that it returns, 2[0]=first element of the tuple given
# print(counter.most_common(1)[0][0])


# # namedtuple
# # creates a class with the name given in the first argument
# p = namedtuple('p', 'x,y')
# pt = p(1, -4)
# print(pt.x, pt.y)


# # defaultdict
# # sets a default in case you mention a key that is not set
# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d['c'])  # it will print the default set, in the case of an int it is 0


# # deque
# d = deque()
# d.append(1)
# d.append(2)

# d.appendleft(3)
# print(d)

# d.pop()
# print(d)
# d.popleft()
# print(d)
# d.extend([4, 5, 6])
# print(d)
# d.extendleft([-1, -2, -3])
# print(d)
# d.rotate(1)  # moves everyelement to the right
# print(d)
# d.clear
