from Score import read_score
from flask import Flask, render_template, request
from MemoryGameWeb import generate_sequence, is_guess_correct, calculate_points

import random
import requests

app = Flask(__name__)


# MemoryGame logic
def memory_game_logic(difficulty):
    sequence_length = difficulty + 2  # More numbers for higher difficulty
    display_time = max(1, 5 - difficulty)  # Less time for higher difficulty
    sequence = [random.randint(1, 101) for _ in range(sequence_length)]
    return sequence, display_time


def check_memory_game_guess(sequence, guess):
    return sequence == guess


# GuessGame logic
def guess_game_logic(guess, difficulty):
    correct_number = random.randint(1, difficulty)
    return guess == correct_number


# CurrencyRouletteGame logic
def currency_roulette_game_logic(guess, difficulty):
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        currency_rate = data['rates']['ILS']
        total_money = random.randint(1, 100) * currency_rate
        lower_bound = total_money - (5 - difficulty)
        upper_bound = total_money + (5 - difficulty)
        return lower_bound <= guess <= upper_bound
    except requests.RequestException:
        return False


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('home.html', name=name, show_games=True)
    return render_template('home.html', show_games=False)


@app.route('/memory-game', methods=['GET', 'POST'])
def memory_game():
    if request.method == 'POST':
        if 'sequence' in request.form:
            user_guess = [int(num) for num in request.form.getlist('user_guess')]
            sequence = [int(num) for num in request.form.get('sequence').split(',')]
            difficulty = int(request.form.get('difficulty'))
            correct = is_guess_correct(sequence, user_guess)
            points = calculate_points(difficulty, correct)
            return render_template('memory_game_result.html', correct=correct, points=points)
        else:
            difficulty = int(request.form.get('difficulty', 1))
            sequence = generate_sequence(difficulty)
            return render_template('memory_game_play.html', sequence=sequence, difficulty=difficulty)
    return render_template('memory_game.html')


@app.route('/guess-game', methods=['GET', 'POST'])
def guess_game():
    if request.method == 'POST':
        guess = int(request.form.get('guess', 0))
        difficulty = int(request.form.get('difficulty', 1))
        result = guess_game_logic(guess, difficulty)
        return render_template('guess_game_result.html', guess=guess, result=result, difficulty=difficulty)
    return render_template('guess_game.html')


@app.route('/currency-roulette-game', methods=['GET', 'POST'])
def currency_roulette_game():
    if request.method == 'POST':
        guess = float(request.form.get('guess', 0))
        difficulty = int(request.form.get('difficulty', 1))
        result = currency_roulette_game_logic(guess, difficulty)
        return render_template('currency_roulette_game_result.html', guess=guess, result=result, difficulty=difficulty)
    return render_template('currency_roulette_game.html')


@app.route('/scores')
def score():
    try:
        current_score = read_score()  # Retrieve the score
        return render_template('scores.html', score=current_score)
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == '__main__':
    app.run(debug=True)
