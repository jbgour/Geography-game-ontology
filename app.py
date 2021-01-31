# app.py (1/3)

from flask import Flask, render_template, request, redirect, url_for
from models import *

# initialize instance of WSGI application
# act as a central registry for the view functions, URL rules, template configs
app = Flask(__name__)

app.debug = True


@app.route("/", methods=["GET", "POST"])
def login():
    ## login page

    if request.method == "POST":
        req = request.form

        pseudo = req.get("pseudo")
        global player
        player = Player(pseudo)

        return redirect(url_for('home'))

    return render_template(
        'login.html',
    )


@app.route("/home", methods=["GET"])
def home():
    ## home page
    pseudo = player.pseudo
    global game_session
    game_session = GameSession(player)
    return render_template(
        'home.html',
        pseudo=pseudo,
    )


@app.route("/question")
def get_question():
    game_session.update_questions_count()
    return render_template(
        'question.html',
        number=game_session.questions_answered,
    )


# @app.route("/question/")
# def by_date(day_to_pull=None):
#     return render_template(
#         'index.html',
#         Post=Post,
#         day_to_pull=day_to_pull
#         )
#
# @app.route("/question/end")
# def by_date(day_to_pull=None):
#     return render_template(
#         'index.html',
#         Post=Post,
#         day_to_pull=day_to_pull
#         )


if __name__ == "__main__":
    app.run()
