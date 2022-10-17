"""
This is a guess the number game.
"""

import random

def guess_guaging():
    """Check if the guess is more, less or correct."""
    if guess > random_number:
        print("Your guess is too high.")
    elif guess < random_number:
        print("Your guess is too low.")


def count_guesses(count):
    """Count how many guesses and return the right print statement."""
    if count == 1:
        return f"Good job! You guessed my number in 1 guess!"
    else:
        return f"Good job! You guessed my number in {count} guesses!"


# --- STORE A RANDOM NUMBER AND INITIAL GUESS IN THE VARIABLES
random_number = random.randint(1, 20)
guess = -1
count = 0

# --- ASK USER FOR A GUESS
print("I am thinking of a number between 1 and 20.")


while guess != random_number:
    guess = int(input("Take a guess.\n"))

    count += 1
    guess_guaging()

print(count_guesses(count))
