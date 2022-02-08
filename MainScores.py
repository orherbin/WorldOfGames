from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def score_server():
    res = 0
    score_file = open("Scores.txt", 'w+').readlines()
    if score_file is None:
        return render_template("ScoreError.html", ERROR="Can't open file"), 400
    while score_file:
        res = res + int(score_file.pop())
    return render_template("Score.html", SCORE=res), 200


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=30000)

