# mylist = ['banana', 'cherry', 'apple']  # Loaded list
# print(mylist)

# # l = list()      # empty list

# # mylist2 = [5, True, 'Apple', 5]  # can have different types and dupes
# # print(mylist2)

# # can reference using [], if using negatives as the index it starts from the back
# item = mylist[2]
# print(item, '\n')

# for i in mylist:
#     print(i)

# if "banana" in mylist:
#     print('Yes')
# else:
#     print('No')

# print(len(mylist))  # len gives the length of the list

# mylist.append('lemon')  # adds something to the end of the list
# print(mylist)

# # insert in a specific index, first index then data to be inserted
# mylist.insert(1, 'strawberry')
# print(mylist)

# item = mylist.pop()  # returns the last element of the list and removes it from the list
# print(item)
# print(mylist)

# mylist.remove('cherry')  # Removes an specific element in the list
# print(mylist)

# mylist.reverse()  # reverses the list
# print(mylist)

# new_list = sorted(mylist)  # returns a sorted list, doesnt change the original
# print(new_list)

# mylist.sort()  # sorts the list
# print(mylist)

# l = [0]*5  # puts 5 zeros in the list
# print(l)

# l2 = [1, 2, 3, 4, 5, 5]
# new_list = l+l2  # makes a mixture of two lists
# print(new_list)

# mylist.clear()  # clears the list
# print(mylist)

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = mylist[1:5]  # slicing, if [:5] starts from beginning, if [1:] starts from 1 and copies the rest of the indexes, if [:] copies the entire list
# b = mylist[::2]  # the difference between each number copied
# print(mylist)
# print(a)
# print(b)

# list_org = ['banana', 'cherry', 'apple']
# list_copy = list_org
# # this copies the 'pointer', so if you change the copy, it also changes the original
# list_copy.append('lemon')
# print(list_org)

# list_org = ['banana', 'cherry', 'apple']
# list_copy = list_org.copy()  # correct way of copying
# # list_copy = list(list_org)
# # list_copy=list_org[:]
# list_copy.append('lemon')
# print(list_org)
# print(list_copy)

# a = [1, 2, 3, 4, 5, 6]
# # list comprehension, saves the squared numbers of a in this case
# b = [i*i for i in a]
# print(b)
