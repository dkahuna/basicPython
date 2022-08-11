#module(s)
import random

lives = 9

words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']

secret_word = random.choice(words)

clue = list('?????')

heart_symbol = u'\u2764'

guessed_word_correctly = False


# define/declare a function before the main program
def update_clue(guessed_letter, secret_word, clue):

    index = 0

    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1


#MAIN
difficulty = input('Choose difficulty (type 1, 2, or 3):\n 1 Easy\n 2 Normal\n 3 Hard\n')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
else:
    lives = 5


while lives > 0:
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)

    else:
        print('Incorrect. You lose a life!')
        lives = lives - 1

if guessed_word_correctly:
    print('You won! The secret word is ' + secret_word)
else:
    print('You lost! The secret word is ' + secret_word)
