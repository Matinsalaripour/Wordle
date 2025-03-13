import random
import string

# Generate a random 6-letter word
num = 6
key = "".join(random.choice(string.ascii_lowercase) for _ in range(num))
guesses = []
colors = []

# Allow the user to have six guesses
for i in range(num):
    guess = input(f"Enter guess {i+1} (6 letters): ").lower()
    while len(guess) != num or not guess.isalpha():
        guess = input("Invalid input. Enter a 6-letter word: ").lower()
    guesses.append(guess)

    color_row = []
    for j in range(num):
        if key[j] == guess[j]:
            color_row.append('G')
        elif guess[j] in key:
            color_row.append('Y')
        else:
            color_row.append('R')

    colors.append(color_row)

    # Print the color feedback for the current guess
    print("".join(color_row))

    # Check if the user has won
    if color_row == ['G'] * num:
        print("You win!")
        break

# Print the key at the end of the game
print("Key:", key)