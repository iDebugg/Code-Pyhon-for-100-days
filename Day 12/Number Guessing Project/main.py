import random


def guess_game() :
    numbers = range(1, 101)
    computer_number = (random.choice(numbers))
    print(computer_number)

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")


    if difficulty_level == "easy":
        number_of_attempts = 10
    elif difficulty_level == "hard":
        number_of_attempts = 5
    else:
        print("Wrong input")
        number_of_attempts = 0

    while number_of_attempts > 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number")
        take_guess = int(input("Make a guess: "))

        if take_guess == computer_number:
            print(f"You got it, the answer was {computer_number}")
            break
        elif take_guess > computer_number:
            print("Too high")
        else:
            print("Too low")

        number_of_attempts -= 1

        if number_of_attempts == 0:
            print(f"You've run out of attempts. The number was {computer_number}")
        else:
            print("Guess again")

guess_game()
