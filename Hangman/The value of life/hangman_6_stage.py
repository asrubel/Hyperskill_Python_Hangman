from random import choice

guess_words = 'python', 'java', 'kotlin', 'javascript'
guess_word = choice(guess_words)
guess_letters = set(guess_word)
guessed_letters = set()

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
    elif input_letter in guessed_letters:
        attempts -= 1
        print("No improvements")
    else:
        attempts -= 1
        print("No such letter in the word")

if guess_letters == guessed_letters:
    print("You survived!")
else:
    print("You are hanged!")
