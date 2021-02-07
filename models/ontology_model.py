from SPARQLWrapper import SPARQLWrapper, JSON
import random
import sys, os


class OntologyModel:

    def __init__(self, queries):
        self.queries = queries
        self.raw_data = self.get_sparql_data()

    def init_models(self):
        with onto :
            class Country(Thing): pass
            class Capital(Thing): pass
            class Area(Thing): pass
            class Currency(Thing): pass
            class PopRanking(Thing): pass

            #data properties 
            class is_capital_of(Capital >> Country, FunctionalProperty):pass
            class has_an_area_of(Country >> Area, FunctionalProperty ):pass
            class is_currency_of(Currency >> Country, FunctionalProperty):pass
            class has_a_pop_ranking_of(Country >> PopRanking, FunctionalProperty ):pass
                
    def get_sparql_data(self):
        #first is country, then countries + capital / country + area / coutnry + currency / country + pop ranking
        return [self.queries.get_data_from_get_countries(), self.queries.get_data_from_get_capitals_and_countries(), self.queries.get_data_from_get_countries_area(), self.queries.get_data_from_get_countries_currency(), s.get_data_from_get_countries_population_ranking()]


    def create_onto_individuals(self):
        #getting countries and capitals
        individuals_created = []
        self.init_models()
        for elmt in self.raw_data[1]:
            if elmt[0] not in individuals_created :
                individuals_created.append(elmt[0])
                elmt[0] = Country(name=elmt[0])
                elmt[1] = Capital(name=elmt[1])
                elmt[1].is_capital_of = [elmt[0]]
        
        for countries in individuals_created : 
            pass



if __name__ == '__main__':
    
    sys.path.insert(0, "../sparql_package")
    from sparql_queries import SparqlQueries
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    s = SparqlQueries(sparql)
    onto = OntologyModel(s)
    l = onto.raw_data
    print(l[1], '\n\n', l[2])
    onto.create_onto_individuals()
    # print(onto.get_random_country())
    # print(onto.get_random_capital())
    # print(onto.get_capital("France"))
    # print(onto.get_country("Paris"))
    # print(onto.get_area("France"))
    # # France is not in query of Currency
    # print(onto.get_currency("Belgium"))
    # print(onto.get_currency("France"))
    # print(onto.get_pop_ranking("France"))
