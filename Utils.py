import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    # Function to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')


# Additional utility functions can be added here as needed
