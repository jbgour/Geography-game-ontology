import re
from .question import Question
import random as rd
import unidecode


class GameSession:

    def __init__(self, player, get_ontology_data):
        """
        :param player: str, Player Object
        """
        self.player = player
        self.get_ontology_data = get_ontology_data
        self.score = 0
        self.questions_answered = 0
        self.questions_to_answer = 10
        self.current_question = None

    def update(self):
        self.update_question()
        self.update_questions_count()

    def update_difficulty(self, difficulty):
        self.current_question.difficulty = difficulty

    def update_questions_count(self):
        """
        each time a question is answerd, update the count
        """
        self.questions_answered += 1
        self.questions_to_answer -= 1

    def update_question(self):
        random_number = rd.randint(1, 5)
        if random_number == 1:
            question = Question(self.get_ontology_data, "capital_of_country")
        elif random_number == 2:
            question = Question(self.get_ontology_data, "country_of_capital")
        elif random_number == 3:
            question = Question(self.get_ontology_data, "area_of_country")
        elif random_number == 4:
            question = Question(self.get_ontology_data, "population_of_country")
        elif random_number == 5:
            question = Question(self.get_ontology_data, "currency_of_country")
        question.generate_question()
        self.current_question = question

    def update_score(self, given_answer):
        """
        each time a question is answerd, update the score
        :param given_answer: str, anwer provided by player
        :param question_type: str in ["duo", "carre", "cash"]
        """
        if self.current_question.type in ['capital_of_country', 'country_of_capital', 'currency_of_country']:
            correct_answer = re.sub(r'[\W_]', ' ', unidecode.unidecode(self.current_question.answer.lower()))
            given_answer = re.sub(r'[\W_]', ' ', unidecode.unidecode(given_answer.lower()))
            print(correct_answer)
            print(given_answer)
            if correct_answer == given_answer:
                self.current_question.is_correct = True
            else:
                self.current_question.is_correct = False

        if self.current_question.type in ['area_of_country', 'population_of_country']:
            if 0.9 * int(self.current_question.answer) < int(given_answer) < 1.1 * int(self.current_question.answer):
                self.current_question.is_correct = True
            else:
                self.current_question.is_correct = False

        if self.current_question.is_correct:
            if self.current_question.difficulty == "duo":
                self.score += 1
            elif self.current_question.difficulty == "carre":
                self.score += 3
            else:
                self.score += 5

        else:
            self.score = self.score
