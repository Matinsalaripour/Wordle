import random
import string

num = 6
key = "".join(random.choice(string.ascii_lowercase) for _ in range(num))

# Allow the user to have six guesses
for i in range(num):
    if i == 0:
        suffix = "st"
    elif i == 1:
        suffix = "nd"
    elif i == 2:
        suffix = "rd"
    else:
        suffix = "th"
    
    guess = input(f"Enter {i+1}{suffix} guess (6 letters): ").lower()
    
    while len(guess) != num or not guess.isalpha():
        guess = input("Invalid input. Enter a 6-letter word: ").lower()
    
    # Create a list of colors for the current guess
    color_row = []
    for j in range(num):
        if key[j] == guess[j]:
            color_row.append('G')
        elif guess[j] in key:
            color_row.append('Y')
        else:
            color_row.append('R')

    # Print the color feedback for the current guess    
    print("".join(color_row))

    # Check if the user has won
    if color_row == ['G'] * num:
        print("You win!")
        break

# Print the key at the end of the game
print("key: ", key)