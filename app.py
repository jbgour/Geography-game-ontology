# app.py (1/3)

from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)

app.debug = True

ontology_model = OntologyModel()


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


@app.route("/home", methods=["GET", "POST"])
def home():
    ## home page
    pseudo = player.pseudo
    if request.method == "POST":
        global game_session
        game_session = GameSession(player, ontology_model)
        game_session.update()
        return redirect(url_for('get_question'))
    return render_template(
        'home.html',
        pseudo=pseudo,
    )


@app.route("/question", methods=["GET", "POST"])
def get_question():
    question = game_session.current_question
    if request.method == "POST":
        if request.form['question_button'] == 'Duo':
            return redirect(url_for('get_question_duo'))
        elif request.form['question_button'] == 'Carré':
            return redirect(url_for('get_question_carre'))
        elif request.form['question_button'] == 'Cash':
            return redirect(url_for('get_question_cash'))
    return render_template(
        'question.html',
        number=game_session.questions_answered,
        question_body=question.body
    )


@app.route("/question/duo", methods=["GET", "POST"])
def get_question_duo():
    return render_template(
        'question_duo.html',
    )


@app.route("/question/carre", methods=["GET", "POST"])
def get_question_carre():
    return render_template(
        'question_carre.html',
    )


@app.route("/question/cash", methods=["GET", "POST"])
def get_question_cash():
    return render_template(
        'question_cash.html',
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
