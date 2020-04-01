from random import choice

guess_words = 'python', 'java', 'kotlin', 'javascript'
guess_word = choice(guess_words)
hint = guess_word[:3] + "-" * (len(guess_word) - 3)
user_word = input(f"Guess the word {hint}: ")

print("H A N G M A N")
if user_word == guess_word:
    print("You survived!")
else:
    print("You are hanged!")
