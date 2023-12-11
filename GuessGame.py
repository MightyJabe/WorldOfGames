import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Choose a number between 1 and {difficulty}: "))
            if 1 <= guess <= difficulty:
                return guess
            else:
                print(f"Please enter a number between 1 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def compare_results(secret_number, guess):
    return "Win" if secret_number == guess else "Lose"


def play(difficulty):
    while True:
        secret_number = generate_number(difficulty)
        user_guess = get_guess_from_user(difficulty)
        result = compare_results(secret_number, user_guess)

        if result == "Win":
            print("Congratulations! You guessed correctly.")
            return True
        else:
            print(f"Sorry, you lost. The correct number was {secret_number}.")
            return False


# Example usage:
# play(3)
