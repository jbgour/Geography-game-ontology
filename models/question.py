import random


class Question:

    def __init__(self, get_ontology_data, type):
        """
        :param get_ontology_data: ontology getter
        :param type: type of question in ["duo", "carre", "cash"]
        """
        self.get_ontology_data = get_ontology_data
        self.type = type
        self.difficulty = ""
        self.body = ""
        self.answer = None
        self.wrong_answers = []
        self.is_correct = False

    def generate_question(self):
        """
        effectively generate the body, the answer ann some wrong answers of the question
        """
        if self.type == "capital_of_country":
            country = self.get_ontology_data.get_random_country()
            capital = self.get_ontology_data.get_capital(country)
            false_capitals = self.get_ontology_data.get_non_capital(country, 3)
            self.body = "What is the capital city of " + str(country) + "?"
            self.answer = capital
            self.wrong_answers = false_capitals

        elif self.type == "country_of_capital":
            capital = self.get_ontology_data.get_random_capital()
            country = self.get_ontology_data.get_country(capital)
            false_countries = self.get_ontology_data.get_non_country(capital, 3)
            self.body = "From which country is " + str(capital) + " the capital city of?"
            self.answer = country
            self.wrong_answers = false_countries

        elif self.type == 'area_of_country':
            country = self.get_ontology_data.get_random_country()
            area = self.get_ontology_data.get_area(country)
            false_areas = self.get_ontology_data.get_non_area(country, 3)
            self.body = "What is the area in sqm of " + str(country) + "?"
            self.answer = area
            self.wrong_answers = false_areas

        elif self.type == 'population_of_country':
            country = self.get_ontology_data.get_random_country()
            population = self.get_ontology_data.get_pop_ranking(country)
            # int
            false_populations = self.get_ontology_data.get_non_pop_ranking(country, 3)
            # string
            self.body = "What is the population rank of " + str(country) + "?"
            self.answer = population
            self.wrong_answers = false_populations

        elif self.type == 'currency_of_country':
            country = self.get_ontology_data.get_random_country()
            currency = self.get_ontology_data.get_currency(country)
            false_currencies = self.get_ontology_data.get_non_currency(country, 3)
            self.body = "What is the currency of " + str(country) + "?"
            self.answer = currency
            self.wrong_answers = false_currencies
            pass

    def get_answers_to_display(self, number):
        """
        suffle the answers displayed
        :param number: 2 or 4, depending on the number of answers we display
        :return:
        """
        display_list = []
        if number == 2:
            display_list = [self.answer, self.wrong_answers[0]]
        if number == 4:
            display_list = [self.answer, self.wrong_answers[0], self.wrong_answers[1], self.wrong_answers[2]]
        random.shuffle(display_list)
        return display_list
