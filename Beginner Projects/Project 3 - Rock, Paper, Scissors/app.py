import random


def play():
    plays = ('R', 'P', 'S')
    user_wins = 0
    computer_wins = 0
    while ((user_wins < 3) and (computer_wins < 3)):
        user = (input("'R' for rock, 'P' for paper, 'S' for scissors: ")).upper()
        computer = random.choice(plays)
        if (computer == 'R' and user == 'P') or (computer == 'P' and user == 'S') or (computer == 'S' and user == 'R'):
            print(f"User wins the round with {user} against {computer}")
            user_wins += 1
        elif (computer == 'P' and user == 'R') or (computer == 'S' and user == 'P') or (computer == 'R' and user == 'S'):
            print(f"Computer wins the round with {computer} against {user}")
            computer_wins += 1
        else:
            print(f"It's a tie between {user}")
        print('')
    if user_wins == 3:
        print("The user wins!")
    else:
        print("The computer wins!")


play()
