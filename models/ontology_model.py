class OntologyModel:

    def __init__(self):
        pass

    def get_random_country(self):
        return "Pologne"

    def get_random_capital(self):
        return "Varsovie"

    def get_capital(self, country):
        if country == "Pologne":
            return "Varsovie"

    def get_country(self, capital):
        if capital == "Varsovie":
            return "Varsovie"

    def get_non_capital(self, country, number):
        if country == "Pologne":
            return ["Paris", "Berlin", "Londres"]

    def get_non_country(self, capital, number):
        if capital == "Varsovie":
            return ["France", "Allemagne", "Royaume-Uni"]
