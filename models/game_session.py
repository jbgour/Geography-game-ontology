from .question import Question


class GameSession:

    def __init__(self, player):
        """
        :param player: str, Player Object
        """
        self.player = player
        self.score = 0
        self.questions_answered = 0
        self.questions_to_answer = 10
        self.current_question = None

    def update(self):
        self.update_question()
        self.update_questions_count()

    def update_questions_count(self):
        """
        each time a question is answerd, update the count
        """
        self.questions_answered += 1
        self.questions_to_answer -= 1

    def update_question(self):
        question = Question(body="Quelle est la capitale de la France")
        self.current_question = question

    def update_score(self, question_type, is_correct_answer):
        """
        each time a question is answerd, update the score
        :param question_type: str in ["duo", "carre", "cash"]
        :param is_correct_answer: bool
        """
        if is_correct_answer:
            if question_type == "duo":
                self.score += 1
            elif question_type == "carre":
                self.score += 3
            else:
                self.score += 5
        else:
            self.score = self.score
