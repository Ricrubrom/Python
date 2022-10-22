
def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than zero')
        else:
            print('The amount inserted must be a valid number')
    return amount


def main():
    balance = deposit()
