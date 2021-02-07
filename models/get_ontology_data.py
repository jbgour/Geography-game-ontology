from SPARQLWrapper import SPARQLWrapper, JSON
from models import *
import os, sys
import random


class GetOntologyData:

    def __init__(self, individuals):
        """
        create the Ontology getter
        :param individuals: list of ontology object, taken from attribute individuals of Ontology model
        """
        self.individuals = individuals

    def get_random_country(self):
        """
        get a country of the ontology
        :return: str, country
        """
        return str(random.choice(self.individuals)).split('.')[-1]

    def get_random_capital(self):
        """
        get a capital of the ontology
        :return: str, capital
        """
        return str(random.choice(self.individuals).has_capital).split('.')[-1]

    def get_capital(self, country):
        """
        get the capital of a country
        :param country: str
        :return: str, capital
        """
        for ind in self.individuals:
            if ind.name.lower() == country.lower():
                return str(ind.has_capital).split('.')[-1]

    def get_country(self, capital):
        """
        get the country of a capital
        :param capital: str
        :return: str, country
        """
        for ind in self.individuals:
            if str(ind.has_capital).split('.')[-1].lower() == capital.lower():
                return str(ind).split('.')[-1]

    def get_area(self, country):
        """
        get the area of a country
        :param country: str
        :return: int, area
        """
        for ind in self.individuals:
            if ind.name.lower() == country.lower():
                return int(str(ind.has_an_area_of).split('.')[-1].lower())

    def get_currency(self, country):
        """
        get the currency of a country
        :param country: str
        :return: str, currency
        """
        for ind in self.individuals:
            if ind.name.lower() == country.lower():
                return str(ind.has_currency).split('.')[-1]

    def get_pop_ranking(self, country):
        """
        get the population rank of a country
        :param country: str
        :return: int, rank
        """
        for ind in self.individuals:
            if ind.name.lower() == country.lower():
                return str(ind.has_a_pop_ranking_of).split('.')[-1]

    def get_non_capital(self, country, number=3):
        """
        get 3 capitals that are not the capital of the given country
        :param country: str
        :param number: int
        :return: list of str
        """
        counter, l = 0, []
        while counter != number:
            capital = self.get_random_capital()
            count = self.get_country(capital)
            if count != country:
                l.append(capital)
                counter += 1
        return l

    def get_non_country(self, capital, number=3):
        """
        get 3 countries that are not the country of the given capital
        :param capital: str
        :param number: int
        :return: list of str
        """
        counter, l = 0, []
        while counter != number:
            country = self.get_random_country()
            cap = self.get_capital(country)
            if cap != capital:
                l.append(country)
                counter += 1
        return l

    def get_non_currency(self, currency, number=3):
        """
        get 3 currencies that are not the given currency
        :param currency: str
        :param number: int
        :return: list of str
        """
        counter, l = 0, []
        while counter != number:
            country = self.get_random_country()
            curr = self.get_currency(country)
            if curr.lower() != currency.lower():
                l.append(curr)
                counter += 1
        return l

    def get_non_area(self, country, number=3):
        """
        get 3 areas that are not the area of the given country
        :param country: str
        :param number: int
        :return: list of int
        """
        b = self.get_area(country)
        counter, l = 0, []
        while counter != number:
            country = self.get_random_country()
            a = self.get_area(country)
            if float(a) != float(b):
                l.append(a)
                counter += 1
        return l

    def get_non_pop_ranking(self, pop_ranking, number=3):
        """
        get 3 ranks that are not the ranks of the given country
        :param pop_ranking: int
        :param number: int
        :return: list of int
        """
        counter, l = 0, []
        while counter != number:
            country = self.get_random_country()
            pop = self.get_pop_ranking(country)
            if pop != pop_ranking:
                l.append(pop)
                counter += 1
        return l
