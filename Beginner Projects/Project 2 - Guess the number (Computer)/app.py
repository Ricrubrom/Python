import random


def guess(x):
    sec_num = random.randint(1, x)
    tries = 0
    while (tries != 3):
        y = int(input(f'Enter your guess (Between 1 and {x}): '))
        if y == sec_num:
            print('You got the correct number!')
            break
        elif (y < sec_num):
            print('The number you chose is too low ')
        else:
            print('The number you chose is too high ')
        tries += 1
    if tries == 3:
        print('You lost. The correct number was:', sec_num)


def computer_guess(x):
    sec_num = int(input('Select the secret number: '))
    low = 1
    high = x
    while True:
        guess = random.randint(low, high)
        print(f'Guess:{guess}')
        if guess == sec_num:
            print('The computer got the correct number!')
            break
        elif (guess < sec_num):
            print('The number you chose is too low ')
            low = guess + 1
        else:
            print('The number you chose is too high ')
            high = guess - 1


guess(10)
computer_guess(10)
