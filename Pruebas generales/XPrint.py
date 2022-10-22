import json
numbers = [2, 2, 2, 5, 5]
for i in range(len(numbers)):
    output = ""
    for j in range(numbers[i]):
        output += 'x'
    print(output)
