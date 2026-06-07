# ---------------------------------------------------------
# Program: Guess the Number Game
# Description:
# The system has selected a secret number (7).
# The user keeps guessing until the correct number is entered.
# Input validation is included to ensure only valid numbers
# are accepted.
# ---------------------------------------------------------

secret_number = 7

print("Welcome to the Guess the Number Game!")

while True:

    # Accept user input
    guess = input("Enter your guess: ")

    # Validate input
    if not guess.isdigit():
        print("Invalid input! Please enter a valid number.")
        continue

    guess = int(guess)

    # Check the guess
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong Guess. Try Again.")