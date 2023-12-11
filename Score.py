SCORES_FILE_NAME = "Scores.txt"


def calculate_points_of_winning(difficulty):
    return (difficulty * 3) + 5


def add_score(difficulty):
    # Read the current score from the scores file
    current_score = read_score()

    # Calculate the points for winning based on the given difficulty
    points_won = calculate_points_of_winning(difficulty)

    # Update the current score
    new_score = current_score + points_won

    # Save the updated score to the scores file
    save_score(new_score)


def read_score():
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
            return current_score
    except FileNotFoundError:
        # If the file doesn't exist, return 0 as the default score
        return 0
    except ValueError:
        # If the file contains invalid data, return 0 as the default score
        return 0


def save_score(score):
    try:
        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(score))
    except Exception as e:
        print(f"Error saving score: {e}")

# Example usage:
# (Assuming you've called add_score after winning a game)
# add_score(3)  # Add score for winning a game with difficulty 3
# print(read_score())  # Print the current score