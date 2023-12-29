from MemoryGame import play as play_memory_game
from GuessGame import play as play_guess_game
from CurrencyRouletteGame import play as play_currency_roulette
from Score import add_score

MEMORY_GAME = '1'
GUESS_GAME = '2'
CURRENCY_ROULETTE = '3'


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play")


def load_game():
    while True:
        print("""Please choose a game to play:
        1. Memory Game - A sequence of numbers will appear for 1 second, and you have to
           guess it back.
        2. Guess Game - Guess a number and see if you chose like the computer.
        3. Currency Roulette - Try and guess the value of a random amount of USD in ILS.""")

        while True:
            game_choice = input("Enter the number of the game you want to play: ")
            if game_choice in (MEMORY_GAME, GUESS_GAME, CURRENCY_ROULETTE):
                break
            else:
                print("Invalid game choice. Please enter a valid game number.")

        difficulty = get_difficulty()

        if game_choice == MEMORY_GAME:
            if play_memory_game(difficulty):
                add_score(difficulty)
        elif game_choice == GUESS_GAME:
            if play_guess_game(difficulty):
                add_score(difficulty)
        elif game_choice == CURRENCY_ROULETTE:
            if play_currency_roulette(difficulty):
                add_score(difficulty)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break


def get_difficulty():
    while True:
        try:
            difficulty = int(input("Choose difficulty: "))
            if difficulty > 0:
                return difficulty
            else:
                print("Please enter a difficulty greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")



