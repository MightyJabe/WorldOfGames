import random
import time

SEQUENCE_UPPER_LIMIT = 101


def generate_sequence(difficulty):
    return [random.randint(1, SEQUENCE_UPPER_LIMIT) for _ in range(difficulty)]


def display_sequence(sequence):
    print("Memorize the numbers:")
    print(" ".join(map(str, sequence)))
    time.sleep(0.7)  # Display numbers for 0.7 seconds


def get_list_from_user(difficulty):
    try:
        return [int(input(f"Enter number {i + 1}: ")) for i in range(difficulty)]
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_list_from_user(difficulty)


def compare_sequences(sequence1, sequence2):
    return sequence1 == sequence2


def play(difficulty):
    while True:
        print("Get ready to memorize the numbers...")
        sequence = generate_sequence(difficulty)
        display_sequence(sequence)

        print("Time's up! Now, enter the numbers.")
        user_guess = get_list_from_user(difficulty)

        if compare_sequences(sequence, user_guess):
            print("Congratulations! You won.")
            return True
        else:
            print("Sorry, you lost. Better luck next time.")
            print(f"The correct sequence was: {sequence}")
            return False


# Example usage:
# play(3)
