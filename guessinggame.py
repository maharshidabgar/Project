import random

number_to_guess = random.randint(1, 100)
print("Welcome to the Number Guessing Game !!!")
print("I have thought of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Guess the number: "))

        if guess < 1 or guess > 100: 
            print("Your guess is out of the 1 to 100 range. Please try again.")
        elif guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print("Congratulations! You guessed the number!")
            break # Exit the loop when the guess is correct

    except ValueError:
        print("Invalid input. Please enter a whole number.")
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")