#ordered, immutable
# s = "jsdjsdjsdj"
# s = 'lasjdjasdlksajd'  # both work
# s = """sdsd
# sdsds
# sdsd
# """
# # multiline string
# s = """Hello \
# world"""  # will print it as a single line

# # prints the char at the specified index, works the same as a list in this sense.
# print(s[1])

# s = '       Hello world          '
# s = s.strip()  # removes white space, doesnt change the string itself, just returns a version without the white space
# print(s)

# print(s.lower())  # sets all characters to lowercase
# print(s.upper())  # sets all characters to uppercase

# # returns a boolean of weather the sentence starts with the given word or not
# print(s.startswith('w'))

# # returns the index in which there is the first instance of the letter given, -1 if its not in the string
# print(s.find('x'))

# # returns the ammount of instances of the letter/substring given
# print(s.count('o'))

# # replaces the first argument with the second one, if there is no instance of the first argument in the string it will not change anything
# print(s.replace('world', 'universe'))

# # puts each word in a position of the list, the argument says when to split, usually a ' '
# l = s.split()
# print(l)

# s = '*'.join(l)  # puts all the elements of the list together as a string, depending on whats between the '' it will put that between each position of the list
# print(s)
