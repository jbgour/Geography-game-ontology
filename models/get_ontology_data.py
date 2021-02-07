
from SPARQLWrapper import SPARQLWrapper, JSON
from ontology_model import OntologyModel
import os, sys
import random

class GetOntologyData:

    def __init__(self, individuals):
        #individual are taken from attribute individuals of Ontology model
        #individuals is a list of ontology object
        self.individuals = individuals

    def get_random_country(self):
        return str(random.choice(self.individuals)).split('.')[-1]

    def get_random_capital(self):
        return str(random.choice(self.individuals).has_capital).split('.')[-1]
        
    def get_capital(self, country):
        for ind in self.individuals :
            if ind.name.lower() == country.lower():
                return str(ind.has_capital).split('.')[-1]

    def get_country(self, capital):
        for ind in self.individuals :
            if str(ind.has_capital).split('.')[-1].lower() == capital.lower():
                return str(ind).split('.')[-1]

    def get_area(self, country):
        for ind in self.individuals :
            if ind.name.lower() == country.lower():
                return int(str(ind.has_an_area_of).split('.')[-1].lower())

    def get_currency(self, country):
       for ind in self.individuals :
            if ind.name.lower() == country.lower():
                return str(ind.has_currency).split('.')[-1]

    def get_pop_ranking(self, country):
        for ind in self.individuals :
            if ind.name.lower() == country.lower():
                return str(ind.has_a_pop_ranking_of).split('.')[-1]

    def get_non_capital(self, country, number):
        counter, l = 0, []
        while counter != number : 
            capital = self.get_random_capital()
            count = self.get_country(capital)
            if count != country:
                l.append(capital)
                counter +=1
        return l

    def get_non_country(self, capital, number):
        counter, l = 0, []
        while counter != number : 
            country = self.get_random_country()
            cap = self.get_capital(country)
            if cap != capital:
                l.append(cap)
                counter +=1
        return l    
        
    def get_non_currency(self, currency, number):
        counter, l = 0, []
        while counter != number : 
            country = self.get_random_country()
            curr = self.get_currency(country)
            if curr.lower() != currency.lower():
                l.append(curr)
                counter +=1
        return l  
    
    def get_non_area(self, area, number):
        counter, l = 0, []
        while counter != number : 
            country = self.get_random_country()
            a = self.get_area(country)
            if float(a) != float(area):
                l.append(a)
                counter +=1
        return l  
    
    def get_non_pop_ranking(self, pop_ranking, number):
        counter, l = 0, []
        while counter != number : 
            country = self.get_random_country()
            pop = self.get_pop_ranking(country)
            if pop != pop_ranking:
                l.append(pop)
                counter +=1
        return l  
        
    
if __name__ == '__main__':
    
    sys.path.insert(0, "../sparql_package")
    from sparql_queries import SparqlQueries
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    s = SparqlQueries(sparql)
    onto = OntologyModel(s)
    l = onto.raw_data
    individuals = onto.individuals
    #print(individuals)
    data = GetOntologyData(individuals)
    print(data.get_random_country())
    print(data.get_random_capital())
    print(data.get_capital("Togo"))
    print(data.get_country("Jerusalem"))
    print(data.get_area("Togo"))
    print(data.get_currency("Togo"))
    print(data.get_pop_ranking("Togo"))
    print(data.get_non_capital("Jerusalem", 3))
    print(data.get_non_country("Togo", 5))
    print(data.get_non_currency("Euro", 5))
    print(data.get_non_area("12",4))
    print(data.get_non_pop_ranking("1",4))