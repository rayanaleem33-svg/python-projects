import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    secret_number = random.randint(1, 100)
    guesses = 0

    while True:
        guess = input("Enter your guess: ")

        # Check if input is a number
        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess)
        guesses += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"You guessed it in {guesses} tries!")
            break

# Run the game
number_guessing_game()
