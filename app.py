# app.py (1/3)

from flask import Flask, render_template, request, redirect, url_for
from models import *
from sparql_package import *
from SPARQLWrapper import SPARQLWrapper
import time
app = Flask(__name__)

app.debug = True
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sq = SparqlQueries(sparql)
ontology_model = OntologyModel(sq)


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
    if game_session.questions_to_answer == -1:
        return redirect(url_for('get_end_page'))
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
    game_session.update_difficulty("duo")
    question_duo = game_session.current_question
    answer_list = question_duo.get_answers_to_display(2)

    if request.method == "POST":
        req = request.form
        given_answer = req.get("answer")
        game_session.update_score(given_answer)
        game_session.update()
        return redirect(url_for('get_question'))

    return render_template(
        'question_duo.html',
        number=game_session.questions_answered,
        question_body=question_duo.body,
        answer_1=answer_list[0],
        answer_2=answer_list[1]
    )


@app.route("/question/carre", methods=["GET", "POST"])
def get_question_carre():
    game_session.update_difficulty("carre")
    question_carre = game_session.current_question
    answer_list = question_carre.get_answers_to_display(4)
    if request.method == "POST":
        req = request.form
        given_answer = req.get("answer")
        game_session.update_score(given_answer)
        game_session.update()
        return redirect(url_for('get_question'))

    return render_template(
        'question_carre.html',
        number=game_session.questions_answered,
        question_body=question_carre.body,
        answer_1 = answer_list[0],
        answer_2 = answer_list[1],
        answer_3 = answer_list[2],
        answer_4 = answer_list[3]
    )


@app.route("/question/cash", methods=["GET", "POST"])
def get_question_cash():
    game_session.update_difficulty("cash")
    question_cash = game_session.current_question
    if request.method == "POST":
        req = request.form
        given_answer = req.get("answer")
        game_session.update_score(given_answer)
        game_session.update()
        return redirect(url_for('get_question'))

    return render_template(
        'question_cash.html',
        number=game_session.questions_answered,
        question_body=question_cash.body
    )



@app.route("/end", methods=["GET", "POST"])
def get_end_page():
    if request.method == "POST":
        return redirect(url_for('home'))
    return render_template(
            'end.html',
            pseudo = player.pseudo,
            score=game_session.score,
        )


if __name__ == "__main__":
    app.run()
