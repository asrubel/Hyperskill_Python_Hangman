from random import choice

guess_words = 'python', 'java', 'kotlin', 'javascript'
guess_word = choice(guess_words)
guess_letters = set(guess_word)
word = list("-" * len(guess_word))

print("H A N G M A N")
print()
for _i in range(8):
    print("".join(word))
    letter = input("Input a letter: ")

    if letter in guess_letters:
        for j in range(len(word)):
            if letter == guess_word[j]:
                word[j] = letter
    else:
        print("No such letter in the word")
    print()

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
