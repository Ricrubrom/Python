v = [7, 45, 3]
v.append(20)
print(v)
v.insert(3, 10)
print(v)
v.pop()
print(v)
print(10 in v)
v.sort()
v.reverse()
print(v)
v2 = v.copy()
v.append(18)
print(v)
print(v2)
v.clear()
print(v)


list = [1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9, 10, 10]
i = 0
uniques = []
for i in list:
    if i not in uniques:
        uniques.append(i)
    else:
        list.remove(i)
print(list)
print(uniques)
