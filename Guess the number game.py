import random

def guess_number():
    print("Welcome to the Guess the Number Game!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get user's guess
            guessed_number = int(input("Guess the number between 1 and 100: "))
            attempts += 1

            # Check if the guess is too low, too high, or correct
            if guessed_number < number_to_guess:
                print("Too low! Try again.")
            elif guessed_number > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break  # Exit the loop when the guess is correct
        except ValueError:
            print("Please enter a valid number.")

# Start the game
guess_number()
