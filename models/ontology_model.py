from SPARQLWrapper import SPARQLWrapper, JSON
import random
import sys, os

class OntologyModel:

    def __init__(self, queries):
        self.queries = queries

    def get_random_country(self):
        return random.choice(self.queries.get_data_from_get_countries())

    def get_random_capital(self):
        capitals = list(zip(*self.queries.get_data_from_get_capitals_and_countries()))
        return random.choice(capitals[-1])
    
    def get_capital(self, country):
        country_capitals = self.queries.get_data_from_get_capitals_and_countries()
        for coun, capital in country_capitals : 
            if country == coun:
                return capital

    def get_country(self, capital):
        country_capitals = self.queries.get_data_from_get_capitals_and_countries()
        for country, cap in country_capitals : 
            if capital == cap:
                return country


    def get_non_capital(self, country, number):
        if country == "Pologne":
            return ["Paris", "Berlin", "Londres"]

    def get_non_country(self, capital, number):
        if capital == "Varsovie":
            return ["France", "Allemagne", "Royaume-Uni"]


if __name__ == '__main__':
    
    sys.path.insert(0, "../sparql")
    from sparql import SparqlQueries
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    s = SparqlQueries(sparql)
    onto = OntologyModel(s)

    print(onto.get_random_country())
    print(onto.get_random_capital())
    print(onto.get_capital("France"))
    print(onto.get_country("Paris"))