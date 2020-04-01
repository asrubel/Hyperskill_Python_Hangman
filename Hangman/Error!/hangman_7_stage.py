from random import choice
from string import ascii_lowercase

guess_words = 'python', 'java', 'kotlin', 'javascript'
guess_word = choice(guess_words)
guess_letters = set(guess_word)
guessed_letters = set()
entered_letters = set()

attempts = 8
print("H A N G M A N")
while attempts > 0:
    if guess_letters == guessed_letters:
        print("You guessed the word!")
        break
    print()
    print("".join([letter if letter in guessed_letters else '-'
                   for letter in guess_word]))
    input_letter = input("Input a letter: ")

    if input_letter in guess_letters and input_letter not in guessed_letters:
        guessed_letters.add(input_letter)
        entered_letters.add(input_letter)
    elif len(input_letter) > 1:
        print("You should print a single letter")
    elif input_letter not in ascii_lowercase:
        print("It is not an ASCII lowercase letter")
    elif input_letter in entered_letters:
        print("You already typed this letter")
    else:
        attempts -= 1
        entered_letters.add(input_letter)
        print("No such letter in the word")

if guess_letters == guessed_letters:
    print("You survived!")
else:
    print("You are hanged!")
