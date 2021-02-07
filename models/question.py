import random


class Question:

    def __init__(self, ontology_model, type):
        self.ontology_model = ontology_model
        self.type = type
        self.difficulty = ""
        self.body = ""
        self.answer = None
        self.wrong_answers = []
        self.is_correct = False

    def generate_question(self):
        if self.type == "capital_of_country":
            # country = self.ontology_model.get_random_country()
            country = "France"
            # capital = self.ontology_model.get_capital(country)
            capital = "Paris"
            # false_capitals = self.ontology_model.get_non_capital(country, 3)
            false_capitals = ["Varsovie", "Rome", "Madrid"]
            self.body = "What is the capital city of " + str(country) + "?"
            self.answer = capital
            self.wrong_answers = false_capitals

        elif self.type == "country_of_capital":
            capital = self.ontology_model.get_random_capital()
            country = self.ontology_model.get_country(capital)
            false_countries = self.ontology_model.get_non_country(capital, 3)
            self.body = "From which contry is " + str(capital) + " the capital city of?"
            self.answer = country
            self.wrong_answers = false_countries

        elif self.type == 'area_of_country':
            country = self.ontology_model.get_random_country()
            area = self.ontology_model.get_capital(country)
            #int
            false_areas = self.ontology_model.get_non_currencies(country, 3)
            # string
            self.body = "What is the currency of " + str(country) + "?"
            self.answer = area
            self.wrong_answers = false_areas

        elif self.type == 'population_of_country':
            country = self.ontology_model.get_random_country()
            population = self.ontology_model.get_capital(country)
            #int
            false_populations = self.ontology_model.get_non_currencies(country, 3)
            # string
            self.body = "What is the population of " + str(country) + "?"
            self.answer = population
            self.wrong_answers = false_populations

        elif self.type == 'currency_of_country':
            country = self.ontology_model.get_random_country()
            currency = self.ontology_model.get_capital(country)
            false_currencies = self.ontology_model.get_non_currencies(country, 3)
            self.body = "What is the currency of " + str(country) + "?"
            self.answer = currency
            self.wrong_answers = false_currencies
            pass

    def get_answers_to_display(self, number):
        display_list = []
        if number == 2:
            r = random.randint(1, 2)
            if r == 1:
                display_list = [self.answer, self.wrong_answers[0]]
            else:
                display_list = [self.answer, self.wrong_answers[0]]
        if number == 4:
            r = random.randint(1, 4)
            if r == 1:
                display_list = [self.answer, self.wrong_answers[0], self.wrong_answers[1], self.wrong_answers[2]]
            elif r == 2:
                display_list = [self.wrong_answers[0], self.answer, self.wrong_answers[1], self.wrong_answers[2]]
            elif r == 3:
                display_list = [self.wrong_answers[0], self.wrong_answers[1], self.answer, self.wrong_answers[2]]
            elif r == 4:
                display_list = [self.wrong_answers[0], self.wrong_answers[1], self.wrong_answers[2], self.answer]
        return display_list
