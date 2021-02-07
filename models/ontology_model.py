from SPARQLWrapper import SPARQLWrapper, JSON
import random
import sys
import os
from owlready2 import *

onto = get_ontology('http://geography-ontology.org')

with onto:
    class Country(Thing):
        pass


    class Capital(Thing):
        pass


    class Area(Thing):
        pass


    class Currency(Thing):
        pass


    class PopRanking(Thing):
        pass


    # data properties
    class is_capital_of(Capital >> Country, FunctionalProperty):
        pass


    class has_capital(Country >> Capital, FunctionalProperty):
        inverse_property = is_capital_of


    class has_an_area_of(Country >> Area, FunctionalProperty):
        pass


    class is_area_of(Area >> Country, FunctionalProperty):
        inverse_property = has_an_area_of


    class is_currency_of(Currency >> Country, FunctionalProperty):
        pass


    class has_currency(Country >> Currency, FunctionalProperty):
        inverse_property = is_currency_of


    class has_a_pop_ranking_of(Country >> PopRanking, FunctionalProperty):
        pass


    class is_pop_ranking_of(PopRanking >> Country, FunctionalProperty):
        inverse_property = has_a_pop_ranking_of


class OntologyModel:

    def __init__(self, queries):
        """
        :param queries: object from sparql query file
        """
        self.queries = queries
        self.raw_data = self.get_sparql_data()
        self.individuals = self.create_onto_individuals()

    def get_sparql_data(self):
        """
        store all the sparql query results in a list
        :return: first is country, then countries + capital / country + area / coutnry + currency / country + pop ranking
        """
        return [self.queries.get_data_from_get_countries(), self.queries.get_data_from_get_capitals_and_countries(),
                self.queries.get_data_from_get_countries_area(), self.queries.get_data_from_get_countries_currency(),
                self.queries.get_data_from_get_countries_population_ranking()]

    def create_onto_individuals(self):
        """
        create all the individuals given query results and the ontology
        :return: list
        """
        # getting countries and capitals
        individuals_created = []
        individuals_created_names = []

        for elmt in self.raw_data[1]:
            if elmt[0] not in individuals_created_names:

                newCountry = Country(name=elmt[0].upper())
                newCap = Capital(name=elmt[1])

                newCap.is_capital_of = newCountry

                hasProperties = 0

                for area in self.raw_data[2]:
                    countryName = area[0]
                    if countryName == elmt[0]:
                        newArea = Area(name=area[1])
                        newCountry.has_an_area_of = newArea
                        hasProperties += 1

                for curr in self.raw_data[3]:
                    countryName = curr[0]
                    if countryName == elmt[0]:
                        newCurr = Currency(name=curr[1])
                        newCountry.has_currency = newCurr
                        hasProperties += 1

                for pop in self.raw_data[4]:
                    countryName = pop[0]
                    if countryName == elmt[0]:
                        newPop = PopRanking(name=pop[1])
                        newCountry.has_a_pop_ranking_of = newPop
                        hasProperties += 1

                if hasProperties == 3:
                    individuals_created.append(newCountry)
                    individuals_created_names.append(elmt[0])

        return individuals_created
