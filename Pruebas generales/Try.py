age = 0
while age >= 0:
    try:
        age = int(input("Age: "))
        income = 20000
        risk = income/age
        print(age)
    except ValueError:
        print("Invalid value")
    except ZeroDivisionError:
        print("You cannot divde by zero")
