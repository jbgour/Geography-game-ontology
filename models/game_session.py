from .question import Question
import random as rd


class GameSession:

    def __init__(self, player, ontology_model):
        """
        :param player: str, Player Object
        """
        self.player = player
        self.ontology_model = ontology_model
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
        random_number = rd.randint(1, 1)
        if random_number == 1:
            question = Question(self.ontology_model, "capital_of_country")
        elif random_number == 2:
            question = Question(self.ontology_model, "country_of_capital")
        question.generate_question()
        self.current_question = question

    def update_score(self, given_answer):
        """
        each time a question is answerd, update the score
        :param given_answer: str, anwer provided by player
        :param question_type: str in ["duo", "carre", "cash"]
        """
        if self.current_question.answer.lower() == given_answer.lower():
            self.current_question.is_correct = True
            if self.current_question.difficulty == "duo":
                self.score += 1
            elif self.current_question.difficulty == "carre":
                self.score += 3
            else:
                self.score += 5

        else:
            self.current_question.is_correct = False
            self.score = self.score
            return False
