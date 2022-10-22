# Dictionary: key-value pairs, unordered, mutable
# each pair separated by a ,
# mydict = {'name': 'Max', 'age': 28, 'city': 'New York'}
# mydict =dict(name= 'Max', age= 28, city= 'New York')
# print(mydict)

# value = mydict['name']  # to access a value you have to put in brackets the key
# print(value)

# mydict['email'] = 'max@xyz.com'  # adding to the dictionary
# print(mydict['email'])

# mydict['email'] = 'coolmax@xyz.com'  # overrides the key-pair
# print(mydict['email'])

# # how to delete key-pairs in a dictionary
# del mydict['name']
# print(mydict)

# mydict.pop('age')
# print(mydict)

# mydict.popitem()  # removes the last inserted keypair
# print(mydict)

# if 'name' in mydict:
#     print(mydict['name'])

# try:
#     # if the key is not in the dictionary it will print error
#     print(mydict['lastname'])
# except:
#     print('error')

# for key in mydict:
#     print(mydict[key])

# for key in mydict.keys():
#     print(mydict[key])

# for value in mydict.values():
#     print(value)

# for key, value in mydict.items():
#     print(key, value)

# mydict_cpy = mydict  # modifying the copy also modifies the original
# mydict_cpy = mydict.copy()  # does not affect the original if you alter the copy
# mydict_cpy = dict(mydict)

# mydict = {'name': 'Max', 'age': 28, 'email': 'max@xyz.com'}
# mydict2 = dict(name='Mary', age=27, city='Boston')
# # merges the dictionaries, overrides the original with the second one if there are duplicates
# mydict.update(mydict2)
# print(mydict)

# mydict = {3: 9, 6: 36, 9: 81}
# print(mydict)
# print(mydict[3])

# mytuple = (8, 7)
# mydict = {mytuple: 15}  # you can use tuples as keys but not lists
# print(mydict)
# print(mydict[mytuple])
