class Question:

    def __init__(self, ontology_model, type):
        self.ontology_model = ontology_model
        self.type = type
        self.body = ""
        self.answer = ""
        self.wrong_answers = []

    def generate_question(self):
        if self.type == "capital_of_country":
            country = self.ontology_model.get_random_country()
            capital = self.ontology_model.get_capital(country)
            false_capitals = self.ontology_model.get_non_capital(country, 3)
            self.body = "Quelle est la capitale  de " + str(country) + "?"
            self.answer = capital
            self.wrong_answers = false_capitals
        elif self.type == "country_of_capital":
            capital = self.ontology_model.get_random_capital()
            country = self.ontology_model.get_country(capital)
            false_countries = self.ontology_model.get_non_country(capital, 3)
            self.body = "De quel pays La ville de " + str(capital) + " est-elle la capitale?"
            self.answer = country
            self.wrong_answers = false_countries


class QuestionDuo(Question):

    def __init__(self, body, answers):
        super().__init__(self, body=body)
        self.answer_0 = answers[0]
        self.answer_1 = answers[1]


class QuestionCarre(Question):
    def __init__(self, body, answers):
        super().__init__(self, body=body)
        self.answer_0 = answers[0]
        self.answer_1 = answers[1]
        self.answer_2 = answers[2]
        self.answer_3 = answers[3]


class QuestionCash(Question):
    def __init__(self, body):
        super().__init__(self, body=body)
