import random
from words import words
import string
from hangman_visual import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)
    while ('-' in word or ' ' in word):
        word = random.choice(words)
    return word


def hangman():
    word = (get_valid_word(words)).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7
    while (len(word_letters) > 0 and lives != 0):
        print(f"You have {lives} lives left and you have used these letters: ", "".join(
            used_letters))
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word:', "".join(word_list))
        user_letter = (input('Insert a letter to guess: ')).upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                print(f"{user_letter} is in the word")
                word_letters.remove(user_letter)
            else:
                print(f"{user_letter} is not in the word")
                lives -= 1
        elif user_letter in used_letters:
            print('You have already chosen that letter')
        else:
            print('Invalid Character')
        print()
    if lives == 0:
        print(f"You lost, the correct word was {word}")
    else:
        print(f"You guessed the word '{word}' correctly!!!!")


hangman()
