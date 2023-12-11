from flask import Flask
from Score import read_score

app = Flask(__name__)


def score_server():
    try:
        # Read the score from the scores file
        score = read_score()

        # HTML template
        html_content = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """

        return html_content
    except Exception as e:
        # Error handling: Return an HTML page with the error message in red
        error_message = str(e)
        error_html_content = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">{error_message}</div></h1>
        </body>
        </html>
        """

        return error_html_content


@app.route("/")
def index():
    return score_server()


if __name__ == "__main__":
    app.run(debug=True)
