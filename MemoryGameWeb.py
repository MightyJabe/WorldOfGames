import random
from Score import calculate_points_of_winning

def generate_sequence(difficulty):
    sequence_length = difficulty + 2
    return [random.randint(1, 101) for _ in range(sequence_length)]

def is_guess_correct(sequence, guess):
    return sequence == guess

def calculate_points(difficulty, correct):
    if correct:
        return calculate_points_of_winning(difficulty)
    return 0
