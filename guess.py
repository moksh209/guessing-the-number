# Number Guessing Game
# Python Utility - 1st Year CSE Project

import random


def play_game():
    print("\n==============================")
    print("      NUMBER GUESSING GAME")
    print("==============================")

    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < number:
                print("Too low! Try a bigger number.")

            elif guess > number:
                print("Too high! Try a smaller number.")

            else:
                print("\n🎉 Congratulations!")
                print("You guessed the number correctly!")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask to play again AFTER winning
    while True:
        choice = input("\nDo you want to play again? (yes/no): ")

        if choice.lower() == "yes":
            return True

        elif choice.lower() == "no":
            print("\nThanks for playing!")
            return False

        else:
            print("Please enter yes or no.")


# Main program
while True:

    play_again = play_game()

    if play_again == False:
        break

