import requests
import random


def get_money_interval(difficulty, total_money):
    lower_bound = total_money - (5 - difficulty)
    upper_bound = total_money + (5 - difficulty)
    return lower_bound, upper_bound


def get_currency_rate():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return data['rates']['ILS']
    except requests.RequestException as e:
        print(f"Error fetching currency rates: {e}")
        return None


def get_guess_from_user(total_money):
    while True:
        try:
            guess = float(input(f"Guess the value of {total_money} USD in ILS: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play(difficulty):
    total_money = random.randint(1, 100)  # You can adjust the total money as needed
    currency_rate = get_currency_rate()

    if currency_rate is None:
        print("Game cannot be played. Exiting.")
        return False

    correct_value = total_money * currency_rate
    interval = get_money_interval(difficulty, correct_value)
    print(f"Current exchange rate: 1 USD = {currency_rate} ILS")
    user_guess = get_guess_from_user(total_money)

    if interval[0] <= user_guess <= interval[1]:
        print("Congratulations! You guessed correctly.")
        return True
    else:
        print(f"Sorry, you lost. The correct value was {correct_value} ILS.")
        return False
