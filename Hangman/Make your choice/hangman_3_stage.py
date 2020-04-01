from random import choice

guess_words = 'python', 'java', 'kotlin', 'javascript'
guess_word = choice(guess_words)
user_word = input("Guess the word: ")

print("H A N G M A N")
if user_word == guess_word:
    print("You survived!")
else:
    print("You are hanged!")
